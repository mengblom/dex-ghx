#!/usr/bin/env node

/**
 * Unified LLM Client
 *
 * Supports AWS Bedrock, Anthropic, OpenAI, and Google Gemini with automatic provider selection
 * based on available credentials.
 *
 * Priority order: Bedrock > Anthropic > OpenAI > Gemini
 * (Bedrock first since it uses existing AWS credentials - no additional API key needed)
 */

require('dotenv').config();

const AWS_REGION = process.env.AWS_REGION || process.env.AWS_DEFAULT_REGION || 'us-east-1';
const USE_BEDROCK = process.env.USE_BEDROCK !== 'false'; // Enabled by default if AWS credentials exist
const ANTHROPIC_API_KEY = process.env.ANTHROPIC_API_KEY;
const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

// Check if AWS credentials are available
async function hasAWSCredentials() {
  try {
    const { defaultProvider } = require('@aws-sdk/credential-provider-node');
    const credentials = await defaultProvider()();
    return credentials && credentials.accessKeyId;
  } catch (e) {
    return false;
  }
}

// Determine which provider to use
async function getAvailableProvider() {
  if (USE_BEDROCK && await hasAWSCredentials()) return 'bedrock';
  if (ANTHROPIC_API_KEY) return 'anthropic';
  if (OPENAI_API_KEY) return 'openai';
  if (GEMINI_API_KEY) return 'gemini';
  return null;
}

// ============================================================================
// AWS BEDROCK CLIENT
// ============================================================================

async function generateWithBedrock(prompt, options = {}) {
  const { BedrockRuntimeClient, InvokeModelCommand } = require('@aws-sdk/client-bedrock-runtime');

  const client = new BedrockRuntimeClient({
    region: options.region || AWS_REGION
  });

  // Use Claude Sonnet 4 on Bedrock (same model you're using now)
  const modelId = options.model || 'us.anthropic.claude-sonnet-4-20250514-v1:0';

  const payload = {
    anthropic_version: 'bedrock-2023-05-31',
    max_tokens: options.maxOutputTokens || 4096,
    messages: [
      {
        role: 'user',
        content: prompt
      }
    ]
  };

  const command = new InvokeModelCommand({
    modelId,
    contentType: 'application/json',
    accept: 'application/json',
    body: JSON.stringify(payload)
  });

  const response = await client.send(command);
  const responseBody = JSON.parse(new TextDecoder().decode(response.body));

  return responseBody.content[0].text;
}

// ============================================================================
// ANTHROPIC CLIENT
// ============================================================================

async function generateWithAnthropic(prompt, options = {}) {
  const Anthropic = require('@anthropic-ai/sdk');
  const anthropic = new Anthropic({ apiKey: ANTHROPIC_API_KEY });

  const message = await anthropic.messages.create({
    model: options.model || 'claude-sonnet-4-6',
    max_tokens: options.maxOutputTokens || 4096,
    messages: [
      {
        role: 'user',
        content: prompt
      }
    ]
  });

  return message.content[0].text;
}

// ============================================================================
// OPENAI CLIENT
// ============================================================================

async function generateWithOpenAI(prompt, options = {}) {
  const OpenAI = require('openai');
  const openai = new OpenAI({ apiKey: OPENAI_API_KEY });
  
  const completion = await openai.chat.completions.create({
    model: options.model || 'gpt-4o',
    max_tokens: options.maxOutputTokens || 4096,
    messages: [
      {
        role: 'user',
        content: prompt
      }
    ]
  });
  
  return completion.choices[0].message.content;
}

// ============================================================================
// GEMINI CLIENT
// ============================================================================

async function generateWithGemini(prompt, options = {}) {
  const { GoogleGenerativeAI } = require('@google/generative-ai');
  const genAI = new GoogleGenerativeAI(GEMINI_API_KEY);
  
  const model = genAI.getGenerativeModel({
    model: options.model || 'gemini-2.0-flash-thinking-exp-1219',
    generationConfig: {
      maxOutputTokens: options.maxOutputTokens || 4096,
      temperature: options.temperature || 1.0,
    }
  });
  
  const result = await model.generateContent(prompt);
  return result.response.text();
}

// ============================================================================
// UNIFIED INTERFACE
// ============================================================================

/**
 * Generate content using the first available LLM provider
 * 
 * @param {string} prompt - The prompt to send to the LLM
 * @param {object} options - Generation options
 * @param {string} options.model - Model to use (provider-specific)
 * @param {number} options.maxOutputTokens - Max tokens to generate
 * @param {number} options.temperature - Temperature (0-1)
 * @param {string} options.provider - Force a specific provider ('anthropic', 'openai', 'gemini')
 * @returns {Promise<string>} Generated text
 */
async function generateContent(prompt, options = {}) {
  const provider = options.provider || await getAvailableProvider();

  if (!provider) {
    throw new Error(
      'No LLM provider available. Either configure AWS credentials for Bedrock, or set ANTHROPIC_API_KEY, OPENAI_API_KEY, or GEMINI_API_KEY in your .env file'
    );
  }

  switch (provider) {
    case 'bedrock':
      return await generateWithBedrock(prompt, options);
    case 'anthropic':
      return await generateWithAnthropic(prompt, options);
    case 'openai':
      return await generateWithOpenAI(prompt, options);
    case 'gemini':
      return await generateWithGemini(prompt, options);
    default:
      throw new Error(`Unknown provider: ${provider}`);
  }
}

/**
 * Get the currently active provider
 */
async function getActiveProvider() {
  return await getAvailableProvider();
}

/**
 * Check if any provider is configured
 */
async function isConfigured() {
  return await getAvailableProvider() !== null;
}

module.exports = {
  generateContent,
  getActiveProvider,
  isConfigured,
  ANTHROPIC_API_KEY,
  OPENAI_API_KEY,
  GEMINI_API_KEY
};
