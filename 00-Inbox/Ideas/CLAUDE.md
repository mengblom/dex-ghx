# Obsidian Vault Instructions for Claude

## Vault Information
- **Name**: GHX
- **Path**: C:\obsidian\GHX
- **Files**: 1702 files across 53 folders

## Critical: Always Use Obsidian CLI

**IMPORTANT**: For ALL vault interactions, use the `obsidian` CLI command instead of standard file operations. This ensures proper Obsidian integration, metadata handling, and link updates.

## Core Principles

1. **File Resolution**: Use `file=<name>` for wikilink-style name matching, `path=<path>` for exact paths
2. **JSON Output**: Add `format=json` for parseable structured output
3. **Quotes**: Quote values with spaces: `name="My Note"`
4. **Special Characters**: Use `\n` for newline, `\t` for tab in content
5. **Active File**: Most commands default to the currently active file when file/path is omitted

## Essential Commands by Category

### Reading & Searching

```bash
# Read file contents
obsidian read file="Note Name"
obsidian read path="folder/note.md"

# Search vault (full-text search)
obsidian search query="search term" format=json
obsidian search query="keyword" path="folder" case limit=10

# Search with context lines
obsidian search:context query="pattern" format=json
```

### Creating & Writing

```bash
# Create new file
obsidian create name="New Note" content="Initial content"
obsidian create path="folder/note.md" content="Text" open

# Append to file
obsidian append file="Note Name" content="New content"
obsidian append file="Note" content="Text" inline  # no newline

# Prepend to file
obsidian prepend file="Note Name" content="Top content"

# Use templates
obsidian create name="Meeting" template="Meeting Template" open
```

### Daily Notes

```bash
# Get daily note path
obsidian daily:path

# Read daily note
obsidian daily:read

# Append to daily note
obsidian daily:append content="Task completed"

# Prepend to daily note
obsidian daily:prepend content="## Morning Notes"

# Open daily note
obsidian daily paneType=tab
```

### Properties (Frontmatter)

```bash
# List all properties in vault
obsidian properties format=json counts sort=count

# List properties for specific file
obsidian properties file="Note Name" format=yaml

# Read property value
obsidian property:read name="tags" file="Note Name"

# Set property
obsidian property:set name="status" value="in-progress" file="Note"
obsidian property:set name="tags" value="project,important" type=list file="Note"

# Remove property
obsidian property:remove name="draft" file="Note Name"
```

### Tags

```bash
# List all tags in vault
obsidian tags format=json counts sort=count

# List tags for specific file
obsidian tags file="Note Name" format=json

# Get tag info and file list
obsidian tag name="project" verbose

# Count tag occurrences
obsidian tag name="important" total
```

### Links & Backlinks

```bash
# List outgoing links from a file
obsidian links file="Note Name" format=json total

# List backlinks (incoming links) to a file
obsidian backlinks file="Note Name" format=json counts

# List unresolved (broken) links
obsidian unresolved format=json counts verbose

# List orphaned files (no incoming links)
obsidian orphans format=json total

# List dead-end files (no outgoing links)
obsidian deadends format=json total
```

### File Management

```bash
# List files
obsidian files folder="subfolder" format=json
obsidian files ext=md total

# Get file info
obsidian file file="Note Name"
obsidian file path="folder/note.md"

# Move/rename file
obsidian move file="Old Name" to="new-folder/"
obsidian rename file="Old Name" name="New Name"

# Delete file
obsidian delete file="Note Name"
obsidian delete path="folder/note.md" permanent  # skip trash
```

### Folder Operations

```bash
# List folders
obsidian folders format=json total
obsidian folders folder="parent/path"

# Get folder info
obsidian folder path="folder/path" info=files
obsidian folder path="folder/path" info=size
```

### Tasks

```bash
# List all tasks
obsidian tasks format=json verbose

# Filter tasks
obsidian tasks todo format=json  # incomplete only
obsidian tasks done format=json  # completed only
obsidian tasks file="Project" verbose

# Toggle task status
obsidian task file="Note" line=10 toggle
obsidian task ref="note.md:15" done
```

### Outline & Structure

```bash
# Show file outline (headings)
obsidian outline file="Note Name" format=json
obsidian outline path="note.md" format=tree

# Word count
obsidian wordcount file="Note Name"
obsidian wordcount path="note.md" words
```

### Aliases

```bash
# List all aliases
obsidian aliases format=json verbose total

# List aliases for file
obsidian aliases file="Note Name"
```

### Templates

```bash
# List available templates
obsidian templates format=json

# Read template
obsidian template:read name="Template Name"
obsidian template:read name="Template" resolve title="Meeting"

# Insert template (into active file)
obsidian template:insert name="Template Name"
```

### Vault Operations

```bash
# Get vault info
obsidian vault
obsidian vault info=name
obsidian vault info=files

# List all vaults
obsidian vaults verbose

# Reload vault
obsidian reload
```

### Recent Files

```bash
# List recently opened files
obsidian recents format=json total
```

## Advanced Features

### Version History

```bash
# List file history versions
obsidian history file="Note Name"

# Read specific version
obsidian history:read file="Note" version=1

# Restore version
obsidian history:restore file="Note" version=3
```

### Sync (if enabled)

```bash
# Sync status
obsidian sync:status

# Pause/resume sync
obsidian sync off
obsidian sync on

# List sync versions
obsidian sync:history file="Note Name"

# Read sync version
obsidian sync:read file="Note" version=1
```

### Bookmarks

```bash
# List bookmarks
obsidian bookmarks format=json verbose

# Add bookmark
obsidian bookmark file="Note Name" title="Important"
obsidian bookmark folder="projects" title="Projects"
obsidian bookmark search="tag:#todo" title="All TODOs"
```

### Random Notes

```bash
# Open random note
obsidian random folder="projects"

# Read random note
obsidian random:read folder="ideas"
```

## Best Practices

1. **Always use `format=json`** when you need to parse output programmatically
2. **Use `file=` for wikilink matching**, `path=` for exact file paths
3. **Quote multi-word values**: `file="My Long Note Name"`
4. **Check file existence** with `obsidian file` before operations
5. **Use `verbose` or `total` flags** for detailed info when needed
6. **Leverage search** for discovery: `obsidian search query="keyword" format=json`
7. **Work with properties** for metadata: tags, status, dates, etc.
8. **Track relationships** with `backlinks` and `links` commands
9. **Use daily notes commands** for journal/log entries
10. **Respect vault structure**: use proper paths and check folder structure first

## Common Workflows

### Creating a New Note with Metadata
```bash
obsidian create name="Project Ideas" content="# Project Ideas\n\n" open
obsidian property:set name="tags" value="projects,ideas" type=list file="Project Ideas"
obsidian property:set name="created" value="2026-02-28" type=date file="Project Ideas"
```

### Finding Related Notes
```bash
obsidian search query="keyword" format=json
obsidian backlinks file="Main Note" format=json
obsidian tags file="Main Note" format=json
```

### Daily Log Entry
```bash
obsidian daily:append content="## Completed\n- Task one\n- Task two"
obsidian property:set name="mood" value="productive" file="$(obsidian daily:path)"
```

## Examples with JSON Output

```bash
# Get structured search results
obsidian search query="obsidian" format=json | jq '.[] | .file'

# Get all tags with counts
obsidian tags format=json counts | jq -r '.[] | "\(.tag): \(.count)"'

# List files in JSON
obsidian files format=json | jq -r '.[].path'

# Get backlinks as JSON
obsidian backlinks file="Index" format=json
```
