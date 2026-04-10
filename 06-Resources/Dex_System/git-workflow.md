# Git Workflow for Personal Vault Content

**Last Updated:** April 10, 2026

This document explains how to use git to track your personal vault content in your forked Dex repository.

---

## Overview

Your Dex vault is now configured to track personal content in git for backup and version control purposes.

**What's tracked:**
- ✅ Personal vault folders (00-Inbox, 04-Projects, 05-Areas, etc.)
- ✅ Configuration files (System/user-profile.yaml, System/pillars.yaml)
- ✅ Task management (03-Tasks/)
- ✅ Weekly and quarterly planning (02-Week_Priorities/, 01-Quarter_Goals/)

**What's NOT tracked (privacy guards):**
- 🔒 Files matching `private-*.md`, `*.confidential.md`, `*.private.md`
- 🔒 API keys and credentials (.env files)
- 🔒 Obsidian workspace settings (.obsidian/workspace.json)
- 🔒 Session learnings and temporary files

**Your repository setup:**
- **Origin:** `git@github.com:mengblom/dex-ghx.git` (your fork)
- **Upstream:** `https://github.com/davekilleen/dex` (official Dex repo)

---

## Daily Workflow

### Making Changes

As you work in Dex, your personal content accumulates changes. Commit and push regularly:

```bash
# Check what's changed
git status

# Stage all changes
git add .

# Commit with a meaningful message
git commit -m "Update vault content - $(date +%Y-%m-%d)"

# Push to your fork
git push origin main
```

**Recommended frequency:** Daily or weekly, depending on how much you're capturing.

### Quick Commit Alias

Add this to your `~/.zshrc` or `~/.bashrc` for fast commits:

```bash
alias dex-commit='cd ~/Documents/dex && git add . && git commit -m "Vault update - $(date +%Y-%m-%d)" && git push origin main'
```

Then just run: `dex-commit`

---

## Receiving Dex System Updates

Your fork allows you to receive updates from the official Dex repository while maintaining your personal content.

### Update Process

```bash
# 1. Fetch latest changes from official Dex
git fetch upstream

# 2. Review what's changed
git log upstream/main --oneline -10

# 3. Merge upstream changes into your fork
git merge upstream/main

# 4. Resolve conflicts if any (see below)

# 5. Push updated fork to GitHub
git push origin main
```

### Handling Merge Conflicts

If conflicts occur, they'll likely be in:
- `.claude/` files (skills, reference docs)
- `System/` template files
- `CLAUDE.md` or other system documentation

**Resolution strategy:**
- **Personal content conflicts** (04-Projects/, 05-Areas/): Keep your changes
- **System file conflicts** (.claude/, CLAUDE.md): Accept upstream changes
- **Configuration conflicts** (System/user-profile.yaml): Manually merge (keep your values, add new fields from upstream)

```bash
# View conflicts
git status

# Edit conflicted files, resolve markers (<<<<<<<, =======, >>>>>>>)
# Then:
git add <resolved-file>
git commit -m "Merge upstream updates, resolve conflicts"
git push origin main
```

---

## Privacy Best Practices

### Marking Sensitive Files

Use naming conventions to automatically exclude sensitive content:

```bash
# These patterns are NEVER committed:
04-Projects/private-acquisition-notes.md     # private-*.md
05-Areas/People/Internal/sensitive.confidential.md  # *.confidential.md
00-Inbox/Ideas/stealth-mode.private.md      # *.private.md
```

### Before Pushing, Review Changes

Always review what you're committing:

```bash
# See what's staged
git diff --cached

# Or use a GUI tool
# VS Code: Source Control panel
# GitHub Desktop: Visual diff
```

### Privacy Reminders

- ⚠️ Even private GitHub repos are accessible to GitHub (and potentially via subpoena)
- ⚠️ Meeting notes may contain sensitive business information
- ⚠️ Career documents may contain salary/compensation details
- ✅ Use `private-*.md` naming for highly sensitive notes
- ✅ Consider additional backups (Time Machine, iCloud) for redundancy
- ✅ Regularly audit what's in your repo

---

## Backup Verification

### Check Backup Status

```bash
# View recent commits
git log --oneline -10

# Check remote sync
git remote -v
git status

# Verify files are on GitHub
# Visit: https://github.com/mengblom/dex-ghx
```

### Restoring from Backup

If you need to restore your vault from GitHub:

```bash
# Clone your fork to a new location
git clone git@github.com:mengblom/dex-ghx.git ~/Documents/dex-restored

# Or reset current vault to a previous state
git log  # Find the commit hash you want
git reset --hard <commit-hash>
```

---

## Troubleshooting

### Problem: "Push rejected - non-fast-forward"

**Cause:** Your local branch is behind the remote.

**Solution:**
```bash
git pull origin main
# Resolve any conflicts
git push origin main
```

### Problem: "Accidentally committed sensitive file"

**Solution (if not yet pushed):**
```bash
# Remove from staging
git reset HEAD <file>

# Add to .gitignore
echo "<file-pattern>" >> .gitignore
git add .gitignore
git commit --amend
```

**Solution (if already pushed):**
```bash
# Remove from history (requires force push)
git rm --cached <file>
echo "<file-pattern>" >> .gitignore
git add .gitignore
git commit -m "Remove sensitive file, update .gitignore"
git push origin main

# Note: File is still in git history. For complete removal:
# Use git-filter-repo or BFG Repo-Cleaner (advanced)
```

### Problem: "Too many merge conflicts during update"

**Solution:** Consider switching to Option B (separate repo for personal content) documented in the implementation plan.

---

## Alternative: Separate Personal Repo (Advanced)

If managing merge conflicts becomes burdensome, consider this structure:

```
~/Documents/
├── dex/                  # System files only (upstream tracking)
└── dex-personal/         # Personal content only (separate repo)
```

**Benefits:**
- Zero merge conflicts
- Cleaner separation
- Can use different remotes

**Drawback:** More complex workflow (two repos to manage)

---

## Git Configuration Tips

### Set Up GPG Signing (Recommended)

```bash
# Generate GPG key
gpg --full-generate-key

# Configure git to use it
git config --global user.signingkey <your-key-id>
git config --global commit.gpgsign true
```

### Useful Git Aliases

Add to `~/.gitconfig`:

```ini
[alias]
    st = status
    co = commit
    br = branch
    last = log -1 HEAD
    unstage = reset HEAD --
    visual = log --oneline --graph --decorate --all
```

---

## Questions?

- Run `/xray` to learn more about how Dex works under the hood
- Check `06-Resources/Dex_System/Dex_Technical_Guide.md` for architecture details
- Review the implementation plan at `~/.claude/plans/vectorized-roaming-eagle.md`

---

## Changelog

- **2026-04-10:** Initial setup - enabled git tracking for personal vault content with privacy guards
