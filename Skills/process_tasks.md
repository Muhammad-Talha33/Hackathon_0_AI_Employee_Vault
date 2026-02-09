# Skill: process_tasks

## Trigger
Human command: `run process_tasks`

## Behavior

1. **Read Needs_Action**
   - Scan all `.md` files in `/Needs_Action`
   - If empty, report "No tasks to process"

2. **Summarize each file**
   - Extract filename and key content
   - Create one-line summary per file

3. **Append summary to Dashboard**
   - Add timestamped entry to `Dashboard.md`
   - Format: `- [YYYY-MM-DD] filename: summary`

4. **Move file to Done**
   - Move processed file from `/Needs_Action` to `/Done`
   - Preserve original filename

## Constraints
- Never invent data
- Only process existing files
- Log all actions
- Require human trigger before execution

## Output
Report completion status after processing all files.
