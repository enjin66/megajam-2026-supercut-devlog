"""Export the jam's agent sessions as readable Markdown, with private details removed.

Run:  python -I tools/export_transcripts.py
Reads the Claude Code session files on this PC, keeps entries from START on, writes
transcripts/<label>.md. Raw session files never enter this repo.

Which sessions: every id in sessions.json, plus any session whose first prompt carries the
marker line `GLASSBOX-MEGAJAM-2026 lane=<name>` (every brief sent to a helper agent has it).

The private word list, tools/redact.local.json (not in git), holds:
  notes_root        the notes repo's folder; JAM.md and SUBMISSION.md are read from it, and every
                    spelling of the folder becomes [notes] in the export
  replace_anywhere  {text: mask}, case-insensitive, matched anywhere, even inside other words;
                    a space, dot, dash or underscore in the text also matches any of those
                    (and regex forms such as \\. or [ _-]) or nothing
  replace_token     {text: mask}, case-insensitive, matched only as a whole token
  replace           {text: mask}, case-sensitive, whole word (some private names are ordinary
                    words in lower case)
"""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "transcripts"
START = datetime(2026, 11, 12, 21, 41, 0, tzinfo=timezone.utc)  # Fri 13 Nov 2026, 05:41 SGT
SGT = timezone(timedelta(hours=8))
MARKER = re.compile(r"GLASSBOX-MEGAJAM-2026 lane=([A-Za-z0-9_-]+)")
CLAUDE_DIRS = [Path.home() / d / "projects" for d in (".claude", ".claude-b", ".claude-c")]
LOCAL = ROOT / "tools" / "redact.local.json"  # not in git: the private words themselves

RESULT_CAP = 2500
INPUT_CAP = 3000
FULL_INPUT_TOOLS = ("delegate_task", "t3_thread_send", "Agent", "Write", "Edit")
FULL_INPUT_CAP = 40000
# A tool call that touches one of these gets its result withheld, and its input too unless it is a
# brief to another agent (briefs name these files to forbid them; a brief is kept, redacted).
SENSITIVE = re.compile(
    r"JAM\.md|JAM[_ ]PERK|[\\/]memory[\\/]|MEMORY\.md|API\.md|\.claude[^\\/\s]*[\\/]+projects|\.t3[\\/]+userdata|\.codex|\.env\b|credential"
    r"|redact\.local|_merged_words|new_keys\.json|request_secret"
    r"|EpicGamesLauncher[\\/]+Saved",  # the Launcher's own logs and settings name the signed-in account
    re.I,
)
BRIEF_TOOLS = re.compile(r"(?:^|__)(?:Agent|Task|delegate_task|t3_thread_send|t3_thread_launch|create_threads|SendMessage)$")
# NVIDIA's DLSS and Streamline plugins: their licence does not allow publishing their source.
PLUGIN_PATH = re.compile(r"Plugins[\\/]+(?:Marketplace[\\/]+)?(?:DLSS|NIS|Streamline)\w*", re.I)
PLUGIN_FILE = re.compile(r"(?<![A-Za-z0-9])(?:DLSS(?!Test)|NGX|NIS|Streamline)\w*\.(?:cpp|h|hpp|inl|cs)\b")
CODE_LINE = re.compile(r"[;{}]\s*$|^\s*\d+\s*[\t→]|#include|::|^[+-]\s*\S.*[;{}(]", re.M)
# Tools that read the PC's screen. A screen dump can hold anything (a signed-in name, another
# window), and no word list can know it in advance, so their results are never exported.
SCREEN_TOOLS = re.compile(r"^mcp__(cua-|win-computer|t3-code__(preview_|device_))", re.I)
# Thread search and thread list results name every agent thread on the PC, and a thread read can open
# one from other work. Only reads of this jam's own threads (its delegated lanes and its top-level
# threads) are exported.
THREAD_LIST_TOOLS = re.compile(r"t3_thread_(search|list)$")
JAM_THREADS = (
    "delegated-task",
    "b85fc87c-ee36-41e0-9b68-443c6300eaba",
    "d847c349-ce86-4fd2-ace5-9dfd2b09703a",
    "mcp:launch:e3bfc049a0af5d32ac4befec1744b5b5ce27a46d7514676eb1a618c098b8a173",
)
# Helpers whose whole session is kept out, with the reason shown in place of the transcript.
WITHHELD_LANES = {
    "lane-trailerstudy1": "to collect trailer-editing rules it read the owner's notes and agent threads from work "
    "outside this jam, and quoted them throughout. What it produced for the jam is the trailer rules file the "
    "trailer helpers worked from.",
}
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
# A space, dot, dash, underscore or &, or a regex way of writing one, between two parts of a private text.
SEP = r"(?:\\{0,4}[\s._&-]|%20|\(\?:|\\{1,2}[dDsSwW]|\[[^\]\n]{1,8}\]|\{\d*,?\d*\}|[()*+?]|\\{1,4}){0,6}"

counts = {}


def bump(kind, n):
    if n:
        counts[kind] = counts.get(kind, 0) + n


def loose(text):
    """Regex for text where each separator may be written any way, or left out."""
    parts = [p for p in re.split(r"[\s._&-]+", text) if p]
    rx = SEP.join(re.escape(p).replace(r"\\", r"\\{1,4}") for p in parts)
    if text[:1].isdigit():
        rx = r"(?<!\d)" + rx
    if text[-1:].isdigit():
        rx += r"(?!\d)"
    return rx


def path_rx(root):
    """Every spelling of a Windows folder: either slash, doubled backslashes, /d/ or /mnt/d/, any case, %20 for spaces."""
    drive, *parts = [p for p in re.split(r"[\\/:]+", root) if p]
    sep = r"(?:\\{1,4}|/)+"
    comp = sep.join(re.escape(p).replace(r"\ ", r"(?:\\{0,2} |%20)") for p in parts)
    lead = rf"(?:(?:\b{drive}:|/{drive}|/mnt/{drive}){sep})?"
    return re.compile(lead + comp, re.I)


def section(path, heading):
    text = path.read_text(encoding="utf-8")
    start = text.index("\n" + heading)  # ValueError names the missing heading
    end = text.find("\n## ", start + 1)
    return text[start:end if end > 0 else len(text)]


def build_redactions():
    """Return (pattern, replacement, kind) triples, most specific first."""
    if not LOCAL.exists():
        sys.exit(f"missing {LOCAL}: the private word list is required, the export will not run without it")
    words = json.loads(LOCAL.read_text(encoding="utf-8"))
    for key in ("notes_root", "replace_anywhere", "replace_token", "replace"):
        if key not in words:
            sys.exit(f"{LOCAL} has no '{key}' key: add it (see this file's docstring); the export will not run without it")
    notes = Path(words["notes_root"])
    jam_md = notes / "unreal" / "megajam-2026" / "JAM.md"
    sub_md = notes / "unreal" / "megajam-2026" / "SUBMISSION.md"
    for p in (jam_md, sub_md):
        if not p.exists():
            sys.exit(f"missing {p.name} under notes_root: needed to keep the jam's perk codes out of the export")
    rules = [
        # the agents' own config folder (session files, memory) and its encoded project-folder name
        (re.compile(r"(?i)(?:(?:[A-Z]:|/[a-z])?[\\/]+)?(?:Users[\\/]+[^\\/\s\"'<>|]+[\\/]+)?\.claude[\w-]*[\\/]+projects[\\/]+[^\\/\s\"'<>|`]+"), "[agent-config]", "agent config path"),
        (re.compile(re.escape(re.sub(r"[^A-Za-z0-9]", "-", str(notes))), re.I), "[agent-config]", "agent config path"),
        (path_rx(str(notes)), "[notes]", "notes path"),
    ]
    for kind, key, make in (
        ("private word", "replace_anywhere", lambda w: re.compile(loose(w), re.I)),
        ("private word", "replace_token", lambda w: re.compile(r"(?<![A-Za-z0-9])" + re.escape(w) + r"(?![A-Za-z0-9])", re.I)),
        ("private word", "replace", lambda w: re.compile(r"(?<![A-Za-z0-9])" + re.escape(w) + r"(?![A-Za-z0-9])")),
    ):
        for word, repl in sorted(words[key].items(), key=lambda kv: len(kv[0]), reverse=True):
            rules.append((make(word), repl, kind))
    perks = section(jam_md, "## Perks")  # only that section holds the registered-only links and codes
    public = section(sub_md, "## Tools used")  # tool names the submission must show are not perk codes
    tokens = set(re.findall(r"https?://[^\s)>\]|`\"']+", perks))
    tokens |= {
        t for t in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]{5,}", perks)
        if re.search(r"\d", t) and re.search(r"[A-Z]", t) and not re.search(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", public)
    }
    for t in sorted(tokens, key=len, reverse=True):
        rules.append((re.compile(re.escape(t)), "[jam-perk]", "jam perk"))
    rules += [
        (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[email]", "email"),
        (re.compile(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"), "[ip]", "ip"),
        (re.compile(r"(?i)\b(?:sk|ghp|gho|github_pat|xox[abp])[-_][A-Za-z0-9_-]{16,}"), "[secret]", "secret"),
        (re.compile(r"(?i)((?:api[_-]?key|secret|token|password|passwd|subscription[_-]?key|access[_-]?key)[\"']?\s*[:=]\s*[\"']?)[A-Za-z0-9_\-./+]{20,}"), r"\1[secret]", "secret"),
        (re.compile(r"\b(?:DESKTOP|LAPTOP|WIN)-[A-Z0-9]{6,}\b"), "[computer]", "computer name"),
        (re.compile(r"(?i)((?:[A-Z]:[\\/]+|/[a-z]/)Users[\\/]+)[^\\/\s\"'<>|]+"), r"\1USER", "user folder"),
    ]
    return rules


def redact(text, rules):
    for pat, repl, kind in rules:
        text, n = pat.subn(repl, text)
        bump(kind, n)
    return text


def clip(text, cap):
    text = text.strip()
    if len(text) <= cap:
        return text
    return text[:cap] + f"\n[... {len(text) - cap} more characters not shown]"


def fence(text):
    ticks = "```"
    while ticks in text:
        ticks += "`"
    return f"{ticks}\n{text}\n{ticks}"


def result_text(content):
    if isinstance(content, str):
        return content
    parts = []
    for b in content or []:
        if b.get("type") == "text":
            parts.append(b.get("text", ""))
        elif b.get("type") == "image":
            parts.append("[image]")
    return "\n".join(parts)


def when(entry):
    ts = entry.get("timestamp")
    return datetime.fromisoformat(ts.replace("Z", "+00:00")) if ts else None


def first_prompt(path):
    """The text of the first prompt in a session file, read from the top of the file only."""
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i > 40:
                return ""
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") != "user":
                continue
            c = (d.get("message") or {}).get("content")
            return c if isinstance(c, str) else result_text(c)
    return ""


def find_sessions():
    """Map label -> list of session files (a session and its helper side-sessions)."""
    listed = {s["id"]: s["label"] for s in json.loads((ROOT / "sessions.json").read_text(encoding="utf-8"))}
    found = {}
    for base in CLAUDE_DIRS:
        for path in base.glob("*/*.jsonl"):
            if datetime.fromtimestamp(path.stat().st_mtime, timezone.utc) < START:
                continue
            label = listed.get(path.stem)
            if label is None:
                m = MARKER.search(first_prompt(path))
                if not m:
                    continue
                label = f"lane-{m.group(1)}"
            files = found.setdefault(label, [])
            if all(p.stem != path.stem for p in files):  # the three account folders can share files
                files.append(path)
                files += sorted((path.parent / path.stem / "subagents").glob("*.jsonl"))
    return found


def render(path, label, rules):
    lines = []
    withheld = set()
    screen = set()
    other_threads = set()
    plugin = set()
    orchestrator = label == "orchestrator"
    for raw in open(path, encoding="utf-8"):
        try:
            d = json.loads(raw)
        except ValueError:
            continue
        t = when(d)
        if t is None or t < START or d.get("type") not in ("user", "assistant") or d.get("isMeta"):
            continue
        stamp = t.astimezone(SGT).strftime("%a %d %b %H:%M:%S")
        if d.get("isCompactSummary"):
            lines.append(f"### {stamp} · Harness\n\n[The session's context was summarised here. The summary is not exported.]\n")
            continue
        msg = d.get("message") or {}
        content = msg.get("content")
        blocks = [{"type": "text", "text": content}] if isinstance(content, str) else (content or [])
        for b in blocks:
            kind = b.get("type")
            if kind == "text":
                text = REMINDER.sub("", b.get("text", "")).strip()
                if not text:
                    continue
                if d["type"] == "assistant":
                    who = f"Agent ({msg.get('model', 'model not recorded')})"
                elif text.startswith("Delegated task "):
                    who = "Helper agent's report"
                elif not orchestrator or d.get("isSidechain"):
                    who = "Brief from the orchestrating agent"
                else:
                    who = "Owner"
                lines.append(f"### {stamp} · {who}\n\n{redact(text, rules)}\n")
            elif kind == "tool_use":
                name = b.get("name", "")
                inp = b.get("input") or {}
                dump = json.dumps(inp, ensure_ascii=False)
                private = bool(SENSITIVE.search(dump))
                touches_plugin = bool(PLUGIN_PATH.search(dump) or PLUGIN_FILE.search(dump))
                if private:
                    withheld.add(b.get("id"))
                if touches_plugin:
                    plugin.add(b.get("id"))
                if SCREEN_TOOLS.search(name):
                    screen.add(b.get("id"))
                if THREAD_LIST_TOOLS.search(name) or (name.endswith("t3_thread_read") and not any(k in str(inp.get("threadId", "")) for k in JAM_THREADS)):
                    other_threads.add(b.get("id"))
                cap = FULL_INPUT_CAP if name.endswith(FULL_INPUT_TOOLS) else INPUT_CAP
                if isinstance(inp.get("command"), str):
                    body = inp["command"]
                    note = inp.get("description", "")
                else:
                    body = json.dumps(inp, ensure_ascii=False, indent=1)
                    note = ""
                head = f"**{stamp} · Tool call: {redact(name, rules)}**" + (f" ({redact(note, rules)})" if note else "")
                if private and not BRIEF_TOOLS.search(name):
                    lines.append(f"{head}\n\n[input withheld: this {redact(name, rules)} call named a private file or folder]\n")
                elif touches_plugin and len(CODE_LINE.findall(body)) >= 2:
                    lines.append(f"{head}\n\n[input withheld: it held NVIDIA plugin source, which the plugin's licence keeps private]\n")
                else:
                    lines.append(f"{head}\n\n{fence(redact(clip(body, cap), rules))}\n")
            elif kind == "tool_result":
                if b.get("tool_use_id") in withheld:
                    lines.append("Result: [withheld: the call read a private file]\n")
                    continue
                if b.get("tool_use_id") in screen:
                    lines.append("Result: [withheld: the call read this PC's screen]\n")
                    continue
                if b.get("tool_use_id") in other_threads:
                    lines.append("Result: [withheld: the call listed or read agent threads that are not part of this jam]\n")
                    continue
                text = REMINDER.sub("", result_text(b.get("content")))
                shows_plugin = b.get("tool_use_id") in plugin or PLUGIN_PATH.search(text) or PLUGIN_FILE.search(text)
                if shows_plugin and len(CODE_LINE.findall(text)) >= 2:
                    lines.append("Result: [withheld: it showed NVIDIA plugin source, which the plugin's licence keeps private]\n")
                    continue
                lines.append(f"Result:\n\n{fence(redact(clip(text, RESULT_CAP), rules))}\n")
    return lines


def main():
    rules = build_redactions()
    OUT.mkdir(exist_ok=True)
    sessions = find_sessions()
    if "orchestrator" not in sessions:
        sys.exit("the orchestrator session listed in sessions.json was not found on disk")
    for label, files in sorted(sessions.items()):
        body = []
        for i, path in enumerate(files):
            part = render(path, label, rules)
            if part and i:
                body.append(f"## Helper side-session {path.stem}\n")
            body += part
        head = (
            f"# Transcript: {label}\n\n"
            f"Session {files[0].stem}. Exported by `tools/export_transcripts.py`; entries from Fri 13 Nov 2026 05:41 SGT on. "
            "Times are Singapore time. See the README for what is removed.\n\n"
        )
        if label in WITHHELD_LANES:
            body = [f"[This helper's transcript is withheld: {WITHHELD_LANES[label]}]\n"]
        (OUT / f"{label}.md").write_text(head + "\n".join(body), encoding="utf-8", newline="\n")
        print(f"{label}: {len(body)} blocks from {len(files)} file(s)")
    print("removed:", ", ".join(f"{k} x{v}" for k, v in sorted(counts.items())) or "nothing")


if __name__ == "__main__":
    main()
