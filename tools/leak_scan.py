"""Fail if a tracked file holds anything the exporter would have masked: a private word or path, a perk code,
an email, an IP address, a key or a user folder. Uses the exporter's own rules. Run before every commit."""
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_transcripts  # noqa: E402

ROOT = export_transcripts.ROOT


def private_hits(text, rules):
    """Count matches the exporter would change (a mask already in place matches nothing)."""
    return sum(1 for pat, repl, _ in rules for m in pat.finditer(text) if m.expand(repl) != m.group(0))


def main():
    rules = export_transcripts.build_redactions()
    files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
    bad = 0
    unread = 0
    for name in filter(None, files):
        if Path(name).suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".mp4", ".webm"):
            unread += 1  # a picture or video: text rules cannot check it, a person or agent looks at each one
            continue
        hits = private_hits((ROOT / name).read_text(encoding="utf-8"), rules)
        if hits:
            print(f"{name}: {hits} private item(s)")
            bad += hits
    print("leak scan:", "FAILED" if bad else "clean", f"({unread} picture or video file(s) not text-scanned)" if unread else "")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
