#!/usr/bin/env bash
# Export the transcripts and commit the log. Usage: bash tools/sync.sh "what happened"
# The push is a separate step (see the README) so nothing leaves this PC unread.
set -euo pipefail
cd "$(dirname "$0")/.."
python -I tools/export_transcripts.py
python -I tools/leak_scan.py
git add -A
git commit -q -m "${1:?give a commit message}" && git log --oneline -1
