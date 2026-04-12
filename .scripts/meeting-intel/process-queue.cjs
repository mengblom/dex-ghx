#!/usr/bin/env node

/**
 * Process queued meetings from manual mode
 *
 * Reads JSON files from queue directory and processes them with LLM analysis.
 * Uses the same logic as sync-from-granola.cjs but for pre-queued meetings.
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const VAULT_ROOT = path.resolve(__dirname, '../..');
const QUEUE_DIR = path.join(VAULT_ROOT, '00-Inbox', 'Meetings', 'queue');
const STATE_FILE = path.join(__dirname, 'processed-meetings.json');
const MEETINGS_DIR = path.join(VAULT_ROOT, '00-Inbox', 'Meetings');
const PILLARS_FILE = path.join(VAULT_ROOT, 'System', 'pillars.yaml');
const PROFILE_FILE = path.join(VAULT_ROOT, 'System', 'user-profile.yaml');

const { generateContent, isConfigured, getActiveProvider } = require('../lib/llm-client.cjs');

async function main() {
  console.log('Processing queued meetings...\n');

  // Check if queue directory exists
  if (!fs.existsSync(QUEUE_DIR)) {
    console.log('No queue directory found. Nothing to process.');
    return;
  }

  // Load configuration
  const profile = loadUserProfile();
  const pillars = loadPillars();
  const state = loadState();

  // Get all JSON files from queue
  const queueFiles = fs.readdirSync(QUEUE_DIR)
    .filter(f => f.endsWith('.json'))
    .sort();

  if (queueFiles.length === 0) {
    console.log('No meetings in queue. Nothing to process.');
    return;
  }

  console.log(`Found ${queueFiles.length} meetings in queue\n`);

  // Check LLM provider
  if (!await isConfigured()) {
    console.error('ERROR: No LLM provider available. Configure AWS credentials for Bedrock, or set API keys in .env');
    process.exit(1);
  }

  const provider = await getActiveProvider();
  console.log(`Using LLM provider: ${provider}\n`);

  let processed = 0;
  let failed = 0;

  for (const filename of queueFiles) {
    const filepath = path.join(QUEUE_DIR, filename);
    const meeting = JSON.parse(fs.readFileSync(filepath, 'utf-8'));

    console.log(`\n[${processed + failed + 1}/${queueFiles.length}] Processing: ${meeting.title || 'Untitled'}`);
    console.log(`  Date: ${meeting.createdAt.split('T')[0]}`);
    console.log(`  ID: ${meeting.id.slice(0, 8)}`);

    try {
      // Build prompt
      const prompt = buildAnalysisPrompt(meeting, profile, pillars);

      // Analyze with LLM
      console.log(`  Analyzing with ${provider}...`);
      const analysis = await generateContent(prompt, {
        maxOutputTokens: 3000
      });

      // Create meeting note
      console.log('  Creating meeting note...');
      const result = createMeetingNote(meeting, analysis, profile, pillars);

      // Mark as processed
      state.processedMeetings[meeting.id] = {
        title: meeting.title,
        processedAt: new Date().toISOString(),
        filepath: result.filepath,
        source: meeting.source || 'queue'
      };

      // Remove from queue
      fs.unlinkSync(filepath);

      console.log(`  ✓ Done: ${result.wikilink}`);
      processed++;

      // Small delay between LLM calls
      await new Promise(r => setTimeout(r, 500));

    } catch (err) {
      console.error(`  ✗ Failed: ${err.message}`);
      failed++;
    }
  }

  // Save state
  saveState(state);

  console.log('\n' + '='.repeat(60));
  console.log('QUEUE PROCESSING COMPLETE');
  console.log(`Processed: ${processed} meetings`);
  console.log(`Failed: ${failed} meetings`);
  console.log('='.repeat(60));
}

// Import helper functions
function buildAnalysisPrompt(meeting, profile, pillars) {
  const content = buildMeetingContent(meeting);
  const intelSection = buildIntelligenceSection(profile);
  const pillarList = pillars.join(', ');

  return `You are analyzing a meeting for a ${profile.role}${profile.company ? ` at ${profile.company}` : ''}. Extract structured intelligence from this meeting.

**Meeting:** ${meeting.title}
**Date:** ${meeting.createdAt}
**Participants:** ${meeting.participants.join(', ') || 'Unknown'}
${meeting.company ? `**Company:** ${meeting.company}` : ''}

**Content:**
${content}

---

Generate a structured analysis in this exact markdown format:

## Summary

[2-3 sentence overview of what the meeting was about and key outcomes]

## Key Discussion Points

### [Topic 1]
[Key details and context]

### [Topic 2]
[Key details and context]

## Decisions Made

- [Decision 1]
- [Decision 2]

## Action Items

### For Me
- [ ] [Specific task] - by [timeframe if mentioned] ^task-${new Date().toISOString().split('T')[0].replace(/-/g, '')}-${generateTaskId()}

### For Others
- [ ] @[Person]: [Specific task]

${intelSection}

## Pillar Assignment

[Choose ONE primary pillar from: ${pillarList}]

Rationale: [One sentence explaining why this pillar fits]

---

Be concise but thorough. Extract real insights, not generic summaries. If something isn't clear from the content, say so rather than making things up.`;
}

function buildIntelligenceSection(profile) {
  const intel = profile.meeting_intelligence || {};
  let sections = [];

  if (intel.extract_customer_intel) {
    sections.push(`## Meeting Intelligence

**Pain Points:**
- [Any pain points or challenges mentioned, or "None identified"]

**Requests/Needs:**
- [Any requests or feature needs mentioned, or "None identified"]`);
  }

  if (intel.extract_competitive_intel) {
    sections.push(`**Competitive Mentions:**
- [Any competitors or alternatives mentioned, or "None identified"]`);
  }

  return sections.join('\n\n');
}

function buildMeetingContent(meeting) {
  let content = '';

  if (meeting.notes && meeting.notes.length > 0) {
    content += `## Notes\n\n${meeting.notes}\n\n`;
  }

  if (meeting.transcript && meeting.transcript.length > 0) {
    // Truncate long transcripts
    const maxTranscript = 30000;
    const transcript = meeting.transcript.length > maxTranscript
      ? meeting.transcript.slice(0, maxTranscript) + '\n\n[Transcript truncated...]'
      : meeting.transcript;
    content += `## Transcript\n\n${transcript}\n\n`;
  }

  if (!content.trim()) {
    content = '[No detailed content available - meeting may have been brief or not transcribed]';
  }

  return content;
}

function slugify(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '')
    .slice(0, 60);
}

function generateTaskId() {
  const now = new Date();
  const ms = now.getMilliseconds();
  const seconds = now.getSeconds();
  const num = ((seconds * 1000 + ms) % 999) + 1;
  return num.toString().padStart(3, '0');
}

function createMeetingNote(meeting, analysis, profile, pillars) {
  const date = meeting.createdAt.split('T')[0];
  const time = meeting.createdAt.split('T')[1]?.slice(0, 5) || '00:00';

  const outputDir = path.join(MEETINGS_DIR, date);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const slug = slugify(meeting.title);
  const filename = `${slug}.md`;
  const filepath = path.join(outputDir, filename);

  // Extract pillar from analysis
  const pillarMatch = analysis.match(/## Pillar Assignment\n\n([^\n]+)/i);
  let pillar = pillarMatch ? pillarMatch[1].trim() : pillars[0];
  pillar = pillar.replace(/[\[\]"']/g, '').trim();

  // Filter participants to exclude the owner
  const ownerName = profile.name || '';
  const filteredParticipants = meeting.participants.filter(p =>
    p.toLowerCase() !== ownerName.toLowerCase() &&
    !p.toLowerCase().includes(ownerName.toLowerCase().split(' ')[0])
  );

  const sourceLabel = meeting.source === 'api' ? 'API' : 'Cache';

  const content = `---
date: ${date}
time: ${time}
type: meeting-note
source: granola
title: "${meeting.title.replace(/"/g, '\\"')}"
participants: [${filteredParticipants.map(p => `"${p}"`).join(', ')}]
company: "${meeting.company}"
pillar: "${pillar}"
duration: ${meeting.duration || 'unknown'}
granola_id: ${meeting.id}
processed: ${new Date().toISOString()}
---

# ${meeting.title}

**Date:** ${date} ${time}
**Participants:** ${filteredParticipants.map(p => `05-Areas/People/External/${p.replace(/\s+/g, '_')}.md`).join(', ') || 'Unknown'}
${meeting.company ? `**Company:** 05-Areas/Companies/${meeting.company}.md` : ''}

---

${analysis}

---

## Raw Content

<details>
<summary>Original Notes</summary>

${meeting.notes || 'No notes captured'}

</details>

${meeting.transcript ? `
<details>
<summary>Transcript (${meeting.transcript.split(' ').length} words)</summary>

${meeting.transcript.slice(0, 5000)}${meeting.transcript.length > 5000 ? '\n\n[Truncated...]' : ''}

</details>
` : ''}

---
*Processed by Dex Meeting Intel (${sourceLabel} source)*
`;

  fs.writeFileSync(filepath, content);

  return {
    filepath,
    wikilink: `00-Inbox/Meetings/${date}/${slug}.md`
  };
}

function loadPillars() {
  if (!fs.existsSync(PILLARS_FILE)) {
    return ['General'];
  }
  try {
    const pillarsData = yaml.load(fs.readFileSync(PILLARS_FILE, 'utf-8'));
    return pillarsData.pillars.map(p => p.name || p.id);
  } catch (e) {
    return ['General'];
  }
}

function loadUserProfile() {
  const defaults = {
    name: 'User',
    role: 'Professional',
    company: '',
    meeting_intelligence: {
      extract_customer_intel: true,
      extract_competitive_intel: true,
      extract_action_items: true,
      extract_decisions: true
    }
  };

  if (!fs.existsSync(PROFILE_FILE)) {
    return defaults;
  }

  try {
    const profile = yaml.load(fs.readFileSync(PROFILE_FILE, 'utf-8'));
    return { ...defaults, ...profile };
  } catch (e) {
    return defaults;
  }
}

function loadState() {
  if (!fs.existsSync(STATE_FILE)) {
    return { processedMeetings: {}, lastSync: null };
  }
  try {
    return JSON.parse(fs.readFileSync(STATE_FILE, 'utf-8'));
  } catch (e) {
    return { processedMeetings: {}, lastSync: null };
  }
}

function saveState(state) {
  state.lastSync = new Date().toISOString();
  fs.writeFileSync(STATE_FILE, JSON.stringify(state, null, 2));
}

if (require.main === module) {
  main()
    .then(() => process.exit(0))
    .catch(err => {
      console.error(`FATAL: ${err.message}`);
      console.error(err);
      process.exit(1);
    });
}

module.exports = { main };
