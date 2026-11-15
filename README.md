# Dev log: 2026 Epic AI MegaJam

This repo is the record of how our jam game gets made, kept for the Glass Box prize ("the best
dev log documenting how the Entrant created their Submission").

The record starts at **Fri 13 Nov 2026, 05:41 Singapore time**, when we scrapped our first game
and started again from nothing. Everything after that moment is here.

## What is in it

| Path | What it holds |
| --- | --- |
| `DEVLOG.md` | The log itself: what we did, why, what went wrong. Written as we go, newest at the bottom. |
| `transcripts/` | The agent sessions, word for word: what the owner asked, what each agent answered, every tool call and its result. One file per session. |
| `sessions.json` | Which session files are exported. |
| `tools/export_transcripts.py` | The script that turns raw session files into the Markdown in `transcripts/`. |
| `tools/sync.sh` | Runs the export and commits. |

The game's own code lives in a separate repo. Its commit history covers the same hours.

## Who is who

- **Owner**: the person running the jam entry. Every line marked "Owner" was typed by a person.
- **Orchestrator**: one Claude agent (Claude Code, run through T3 Code) that plans, writes
  briefs, checks results and keeps this log.
- **Helper agents**: agents the orchestrator starts for one job each. Each gets a written brief,
  which appears in full in the orchestrator's transcript, and its own transcript file.
- **The team**: named on the jam entry page. Play testers ran builds on their own PCs.
- **Submitting**: a person on the team submits the entry on itch.io. No agent submits it,
  accepts terms or types a password, here or anywhere in the jam.

## How the transcripts are made

Claude Code saves every session as a file on the PC. The export script reads those files and
writes Markdown. It changes nothing in what was said, except as listed here. It leaves out:

- everything before 05:41 on 13 Nov;
- the agent's standing instructions and private notes, which the harness injects into each
  session and which cover the studio's other projects, and the summaries the harness writes
  when a session's context fills up;
- the agent's private reasoning blocks (free-form notes that often name the studio's other work);
- tool results longer than 2,500 characters and tool inputs longer than 3,000 (40,000 for briefs
  and file writes), cut with the number of characters left out;
- any call that names a private file or folder: the jam's private notes, the agents' memory and
  settings, key files and the export's own word list. Its result is shown as "withheld", and so is
  its input, unless the call is a brief to another agent (briefs name those files to forbid them);
- the results of calls that read the PC's screen (the call itself, such as where the agent
  clicked, stays);
- the source code of NVIDIA's DLSS and Streamline plugins, which their licence keeps private:
  a result or input that shows it is shown as "withheld";
- these, each replaced by a tag in square brackets such as `[email]` or `[pc-b]`: emails, IP
  addresses (also partial ones), Windows user names, computer names, keys and tokens, account
  names, the names of the people whose PCs did work (their PCs carry their names), the local
  folders of the studio's notes and of the agents' settings, the jam's registered-only perk codes,
  the names of the studio's other projects and of another game platform, and the names of
  commercial games and real gun makers that came up as references.

Tool names that the submission sheet lists stay readable. `tools/leak_scan.py` runs the same
rules over every file before each commit and stops the commit if anything would still be masked.

To rebuild: `python -I tools/export_transcripts.py`. It needs the raw session files and a local
word list, neither of which is in this repo.

## Times

All times are Singapore time (UTC+8). The jam closes Mon 16 Nov 2026, 09:59.

## This repo's history

The working repo's history held private details: people's names used as PC names, local paths
and an account name. So this repo is a clean export, made on 15 Nov 2026 as its first commit.
Every dev log entry carries its own date and time, and every transcript carries its session's
timestamps. Commits after the first one are the real, incremental ones.
