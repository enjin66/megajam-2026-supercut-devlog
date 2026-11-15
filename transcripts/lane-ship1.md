# Transcript: lane-ship1

Session ea92763d-b91e-4163-8658-22436987d5b9. Exported by `tools/export_transcripts.py`; entries from Fri 13 Nov 2026 05:41 SGT on. Times are Singapore time. See the README for what is removed.

### Mon 16 Nov 00:20:49 · Brief from the orchestrating agent

Act as the test sub-agent for this task.

GLASSBOX-MEGAJAM-2026 lane=ship1

You are a helper on SUPERCUT, a UE 5.9 C++ game for a jam that closes in under ten hours. Read `[notes]\unreal\megajam-2026\lanes\COMMON_RULES.md` first and follow it. Your lane folder is `[notes]\unreal\megajam-2026\lanes\ship1\` (make it; write only there). You change no game source, run no git in the game repo, and build nothing on c4 (the main PC). Run `date "+%d %b %H:%M"` before you write any time. Do not wait for replies: decide, mark [pick], carry on. Keep LOG.md as you go and end with HANDOFF.md.

WHY. The owner decided at 00:19 on 16 Nov that the judges' build is a SHIPPING build if it can be (Development only if Shipping fails), with the symbols file left out of the zip. Every check tonight ran on Development. The last Shipping package was made on 14 Nov, many merges ago, and code inside `#if !UE_BUILD_SHIPPING` has grown since. I need to know NOW, on a machine that is not the busy one, whether today's main packages and plays as Shipping, so that the final build on the main PC at about 02:00 holds no surprise.

WHAT. On pc2 only (farm host `pc2`, slow, one slot, nobody else is using it right now; never [pc-c], never c4, never [pc-b]):
1. Source: the pinned worktree `D:\UE\wt\maincheck_x` holds main `ae8614e` (read only for you; check `git -C /d/UE/wt/maincheck_x log --oneline -1` prints ae8614e and stop if it does not). Farm script: `[notes]\unreal\megajam-2026\farm\farm.sh` (read its header). Use farm name `ship1`, logs under `/d/UE/ship1_farmlogs`.
   `farm.sh mirror pc2 ship1 /d/UE/wt/maincheck_x`, then `farm.sh build pc2 ship1 <logs> -Jobs 8` (the package step needs an editor build under the same name first), then `farm.sh package-shipping pc2 ship1 <logs>` (runs Tools\package_shipping.cmd; output in `...\_builds\ship1\Supercut59_ship`).
2. Prove the Shipping package: build log has no error, package log has `BUILD SUCCESSFUL`, 0 `Failed to compile Material`, 0 `missing usage flag`.
3. Run it once through the scripted run, the way earlier lanes proved a Shipping build. A Shipping build writes no log (`unreal/GOTCHAS.md`, section "Shipping builds and user settings", about line 880 on: read that whole section before any run, it also says a Shipping run writes into a user settings folder that must be copied aside first and put back after). Find how lanes `held1` and `shell1` got their `main8_shipping.log` proof (their HANDOFF.md files under `lanes\`, and `Tools\run_demo.ps1` in the mirror) and do the same: `-Run main8 -Seed 1 -Script <mirror>\Script\main8.txt -FixedFps 240 -Silent`. The Development reference is `RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9`. Say exactly what evidence a Shipping run gives (a result file, an exit code, a line) and whether it matches. If the script or run options are compiled out of Shipping, say so plainly: that is a finding, not a failure of yours.
4. Measure: size of the Shipping folder in bytes, the largest ten files, whether it holds a `.pdb` and where, and whether `Supercut.exe` there needs anything a clean Windows 10 or 11 PC lacks (look for the prerequisites installer in the package and say what the package script does about it; do not install anything).
5. `unreal/GOTCHAS.md` about line 582 to 590 says every non-Shipping Unreal program opens a trace listener that raises a Windows Firewall prompt, and that Shipping should not, "not yet seen". If you can check the Shipping exe's listeners during the scripted run without admin rights and without touching firewall settings, do it and report; if not, say it was not checked.
6. List every place the game's source differs by configuration, so the owner knows what a judge will not get in Shipping: `git -C /d/UE/wt/maincheck_x grep -n "UE_BUILD_SHIPPING" -- Source` (read only), one line each on what is compiled out (for example the recording switch, on-screen debug text such as "TUNED: n values" or "NO DAMAGE", tuning file loading, dev keys). Flag anything a player would miss or anything that looks like it should NOT be compiled out (for example the tuning file, if the game's balance depends on a `Tuning.txt` beside the exe).

RULES THAT BITE HERE. No sound aloud (`-Silent`). On pc2 never close, resize or click a [another platform] Studio window; install nothing; no admin prompt; if a Windows prompt of any kind appears, stop and report it. Do not print computer, user or account names (logs that farm.sh brings back are already masked). Do not copy the Shipping build anywhere and do not zip it: it is a trial, the judges' build is compiled on the main PC by me. Nothing paid, no web sign-ins.

REPORT to me by 01:30 at the latest, failures first: does main compile and package as Shipping (yes/no, with the error text if no), does the scripted run pass, sizes, the configuration differences, and how long each step took on pc2. If the Shipping compile fails, report at once with the first error and its file and line, without trying to fix source.

**Mon 16 Nov 00:20:54 · Tool call: Bash** (Get time, read common rules, list lanes)

```
date "+%d %b %H:%M"; cat "[notes]/unreal/megajam-2026/lanes/COMMON_RULES.md"; ls "[notes]/unreal/megajam-2026/lanes/"
```

Result:

```
16 Nov 00:21
# Rules every SUPERCUT lane follows (15 Nov 2026)

These are part of your brief. Where your brief says something different, the brief wins.

## Where things are

- The game: SUPERCUT, Unreal Engine 5.9 (`D:\UE\UE_5.9`), C++. The main copy is `D:\UE\Projects\Supercut59`
  (branch `ue59`). It is not yours: never edit, build or run git commands that change it. Other folders under
  `D:\UE\wt` and everything under `D:\UE\Builds` are not yours either, unless your brief names one.
- If your brief gives you a worktree (`D:\UE\wt\<lane>`, branch `<lane>`), edit and commit only there. I merge it.
- Notes repo: `[notes]\unreal\`. Read `unreal\AGENTS.md`, `unreal\GOTCHAS.md` and
  `unreal\megajam-2026\FARM.md` before you start. Your lane folder is `unreal\megajam-2026\lanes\<lane>\`:
  `LOG.md` as you go (clock times from `date`), `HANDOFF.md` or the report your brief names at the end.
- Other lanes' handoffs are in `unreal\megajam-2026\lanes\<name>\HANDOFF.md`. The game's state and decisions are in
  `unreal\megajam-2026\GAME.md` (long: search it, do not read it whole).

## The farm

- Builds, tests, packages, runs and pictures go through `farm\farm.sh` as `FARM.md` describes, under your own
  farm name, on the PC your brief or my latest message names. Git stays on this PC.
- **c4 is a farm host since 15 Nov 13:25** (the owner freed it: "C4 is free for lanes to use... speed is the
  priority"). Use it exactly like the others: `farm.sh mirror c4 <name> <your worktree>` (nothing is copied; it
  makes `D:\UE\Farm\<name>` a junction to your worktree, so the steps build inside your worktree), then
  `build`, `test`, `package`, `run` with host `c4`. `{P}` in run arguments is `D:\UE\Farm\<name>`. Packages land
  in `D:\UE\Farm\_builds\<name>\`, never in `D:\UE\Builds`. Runs are offscreen and `-Silent`: no window, no
  sound. `-TimeoutSeconds 540` on c4. Still forbidden on c4: real keyboard or mouse input,
  `Tools\input_check.ps1`, sound aloud, touching `D:\UE\Builds\Supercut59_play`, `D:\UE\Projects\Supercut59` or
  any program you did not start, and running the project's `Tools\*.cmd` or `*.ps1` directly (always through
  `farm.sh`, so two lanes never write one output folder). Do not commit or edit sources while a c4 build of
  your worktree is running: it compiles the very files you would be editing.
- **`farm.sh` queues by itself since 15 Nov 13:25.** `build`, `test`, `package`, `package-shipping` and `run`
  take a slot on the host 
[... 8409 more characters not shown]
```

**Mon 16 Nov 00:21:11 · Tool call: Bash** (Make lane folder, check worktree commit, read farm.sh header)

```
mkdir -p "[notes]/unreal/megajam-2026/lanes/ship1"; git -C /d/UE/wt/maincheck_x log --oneline -1; git -C /d/UE/wt/maincheck_x status --short | head; sed -n 1,80p "[notes]/unreal/megajam-2026/farm/farm.sh"
```

**Mon 16 Nov 00:21:12 · Tool call: Bash** (Search FARM.md for shipping and pc2 notes)

```
wc -l "[notes]/unreal/megajam-2026/FARM.md"; grep -n -i "shipping\|pc2\|package-shipping" "[notes]/unreal/megajam-2026/FARM.md" | head -50
```

Result:

```
ae8614e SUPERCUT stack: merge normfix1 09c6870 onto main (fixed normals on 58 prop meshes, re-baked and new normal maps, the revolver's barrel map)
#!/bin/bash
# farm.sh: build, test, package and run a SUPERCUT project copy on a farm PC, driven from c4. Details: ../FARM.md.
#
#   farm.sh mirror  <host> <name> <project folder on c4>     copy the project to <root>\Farm\<name> (changed files only)
#   farm.sh build   <host> <name> <log folder> [build.ps1 args, e.g. -Target Supercut -Jobs 8]
#   farm.sh test    <host> <name> <log folder> [run_tests.ps1 args, e.g. -Filter Supercut.Rooms]
#   farm.sh package <host> <name> <log folder>               Tools\package.cmd   -> <root>\Farm\_builds\<name>\Supercut59
#   farm.sh package-shipping <host> <name> <log folder>      Tools\package_shipping.cmd -> ...\_builds\<name>\Supercut59_ship
#   farm.sh run     <host> <name> <log folder> [run_demo.ps1 args]   {P} = the mirror folder there, e.g. -Script {P}\Script\main8.txt
#   farm.sh fetch   <host> <name> <remote path> <local folder>   path in the mirror, or builds/... or out/...
#   farm.sh status  <host>
#   farm.sh slots                                             who holds or waits for which PC right now
#
# Each step brings its logs back to <log folder>/<step>/ and exits with the remote step's exit code.
# Logs that come back have the PC's user and computer names replaced by USER and PC.
#
# Hosts: [pc-b], pc2, [pc-c], pc4 over ssh, and c4 itself (15 Nov: the owner freed c4 for lanes). On c4 nothing is
# copied: "mirror" makes D:\UE\Farm\<name> a junction to the project folder, so the steps build in that folder.
#
# Slots (15 Nov): build, test, package, package-shipping and run take one of the host's slots and wait for one
# when all are taken, so the lanes no longer pile onto one PC. A slot whose farm.sh has died is taken over.
set -u
here=$(cd "$(dirname "$0")" && pwd)

root_of() {   # one line per farm PC: ssh alias, root folder there (engine in <root>\UE_5.9, mirrors in <root>\Farm)
  case "$1" in
    [pc-b]) echo 'C:\UE' ;;
    pc2)    echo 'C:\UE' ;;
    [pc-c])   echo 'F:\UE' ;;
    pc4)    echo 'C:\UE' ;;
    c4)     echo 'D:\UE' ;;
    *) echo "FARM unknown host '$1' ([pc-b], pc2, [pc-c], pc4, c4)" >&2; exit 64 ;;
  esac
}
slots_of() {  # heavy steps at once on each PC
  case "$1" in
    [pc-b]) echo 2 ;;
    pc2)    echo 1 ;;
    [pc-c])   echo 3 ;;
    c4)     echo 2 ;;
    *)      echo 1 ;;
  esac
}
fwd() { echo "${1//\\//}"; }   # C:\UE -> C:/UE for scp and tar
[... 1772 more characters not shown]
```

Result:

```
185 [notes]/unreal/megajam-2026/FARM.md
14:- **`farm.sh` queues by itself.** `build`, `test`, `package`, `package-shipping` and `run` take a slot in
16:  Slots: [pc-c] 3, c4 2, [pc-b] 2, pc2 1. A `run` takes slot 1 only, so one game per PC at a time holds without
20:- **Compiling steps go one at a time per PC (15 Nov 14:05).** `build`, `package` and `package-shipping` also hold
40:| `[pc-b]` | `C:\UE` | **yes** (17:33) | yes | yes | Development and Shipping | yes, offscreen | 2 (builds queue, see below) |
41:| `pc2` | `C:\UE` | **yes** (18:02) | yes | yes | Development | yes, offscreen, slow: add `-TimeoutSeconds 900` | 1 (16 GB RAM, Studio windows open) |
57:The commands below use `[pc-b]`; `[pc-c]` and `pc2` take the same commands (on pc2 add `-TimeoutSeconds 900` to `run`).
82:- `package-shipping` builds the Shipping package to `{B}\Supercut59_ship\Windows`.
109:- **No Shipping runs.** A Shipping game saves to `%LOCALAPPDATA%\Supercut` in the PC user's own profile, outside
110:  `<root>`. The wrapper builds Shipping packages but do not run them on a farm PC.
116:  [pc-b], 179 s on [pc-c] and 472 s on pc2 (its GTX 1070 draws about 70 frames a second, and a fixed-step run draws
117:  every one of the 23,500 steps). On pc2 always pass `-TimeoutSeconds 900`.
125:  `package-shipping` compile at one job (`-MaxParallelActions=1` in the scripts); that is the scripts' choice.
134:A person uses [pc-b] and [pc-c], and pc2 has [another platform] Studio windows open. Before each heavy step run
150:First build of a new name (cold) unless marked. Build jobs: [pc-b] 8, [pc-c] 6 (its user had the CPU at 53%), pc2 6.
153:| Step | [pc-b] | [pc-c] | pc2 | c4 |
161:| Shipping package | 178 s | | | |
165:Compilers: [pc-b] MSVC 14.50.35728 (VS 2026 Build Tools, already there); [pc-c], pc2 and c4 14.44.35230.
170:- pc2, [pc-c], pc4: Visual Studio Build Tools 2022 were installed by this lane; remove with
173:- pc2 and pc4: the engine's VC++ runtime 14.50.35719 was installed (over 14.44 on pc2; pc4 had none). Other
180:- pc2's cook failed (exit 25) until the VC++ runtime was raised to 14.50.35719: the editor logs
```

**Mon 16 Nov 00:21:59 · Tool call: Bash** (Check farm slots and pc2 status)

```
cd "[notes]/unreal/megajam-2026/farm"; ./farm.sh slots; ./farm.sh status pc2 2>&1 | tail -20
```

Result:

```
[pc-b]: CLOSED: [pc-b]'s drive is stalling (NVMe resets, 15 Nov 14:19); no farm work on it for the rest of the jam
[pc-b]: 0 of 2 slot(s) held
pc2: 0 of 1 slot(s) held
[pc-c]: gen4 package since 00:18:33 (3 min, running)
[pc-c]: 1 of 3 slot(s) held
c4: CLOSED: c4 runs no compile, package, editor or game step until the final judges build: its D: drive dropped twice under that load (15 Nov 19:28 and 21:01). Use [pc-c] (or pc2). Main thread, 15 Nov 21:28
c4: 0 of 2 slot(s) held
free_ram_gb=10.3 of 15.9
commit_free_gb=21.7
cpu_load_pct=1 threads=12
disk_free=C:36GB
busy_procs=none
desktop_sessions=1 this_session=0
gpu=NVIDIA GeForce GTX 1070, 0 %, 286 MiB, 9.62 W
farm_names=gruntai1 gunfix1 hands2 home1 light2 perf3 set2 sfx5 submit1
engine=60351404
```

**Mon 16 Nov 00:22:18 · Tool call: Bash** (Read the mirror step in farm.sh)

```
cd "[notes]/unreal/megajam-2026/farm"; grep -n "mirror)" -A40 farm.sh | head -70
```

Result:

```
162:  mirror)
163-    [ $# -eq 3 ] || { echo "usage: farm.sh mirror <host> <name> <project folder on c4>" >&2; exit 64; }
164-    root=$(root_of "$1") || exit $?
165-    if is_local "$1"; then
166-      froot=$(fwd "$root")/Farm
167-      mkdir -p "$froot/_farm" "$froot/_out" "$froot/_builds" || exit 1
168-      cp "$here"/remote/*.ps1 "$froot/_farm/" || exit 1
169-      [ -f "$3/Supercut.uproject" ] || { echo "FARM no Supercut.uproject in $3" >&2; exit 10; }
170-      if [ -e "$froot/$2" ]; then
171-        [ "$froot/$2/Supercut.uproject" -ef "$3/Supercut.uproject" ] ||
172-          { echo "FARM $froot/$2 exists and is not $3; pick another name" >&2; exit 12; }
173-      else
174-        cmd //c "mklink /J $root\\Farm\\$2 $(cygpath -w "$3")" > /dev/null || exit 1
175-      fi
176-      rm -f "$3"/Tools/farm_*
177-      echo "FARM mirror c4: $froot/$2 is the folder $3 (a junction, nothing copied)"
178-    else
179-      scp -q "$here"/remote/*.ps1 "$1:$(fwd "$root")/Farm/_farm/" || exit 1
180-      python -I "$here/mirror.py" "$1" "$root" "$2" "$(cygpath -w "$3")"
181-    fi ;;
182-  build|test|package|package-shipping|run)
183-    [ $# -ge 3 ] || { echo "usage: farm.sh $verb <host> <name> <log folder> [args]" >&2; exit 64; }
184-    step "$verb" "$@" ;;
185-  fetch)
186-    [ $# -eq 4 ] || { echo "usage: farm.sh fetch <host> <name> <remote path> <local folder>" >&2; exit 64; }
187-    root=$(fwd "$(root_of "$1")") || exit $?
188-    case "$3" in
189-      builds/*) src="$root/Farm/_builds/$2/${3#builds/}" ;;
190-      out/*)    src="$root/Farm/_out/$2/${3#out/}" ;;
191-      *)        src="$root/Farm/$2/$3" ;;
192-    esac
193-    pull "$1" "$src" "$4" ;;
194-  status)
195-    [ $# -eq 1 ] || { echo "usage: farm.sh status <host>" >&2; exit 64; }
196-    root=$(root_of "$1") || exit $?
197-    if is_local "$1"; then
198-      powershell -NoProfile -ExecutionPolicy Bypass -File "$here/remote/status.ps1" -Engine "$root\\UE_5.9" -Root "$root"
199-    else
200-      ssh "$1" "powershell -NoProfile -ExecutionPolicy Bypass -File $root\\Farm\\_farm\\status.ps1 -Engine $root\\UE_5.9 -Root $root"
201-    fi ;;
202-  slots)
```

**Mon 16 Nov 00:22:22 · Tool call: Bash** (Read mirror.py header)

```
cd "[notes]/unreal/megajam-2026/farm"; sed -n 1,40p mirror.py; grep -n -i "seed\|clone\|robocopy\|existing" mirror.py | head
```

Result:

```
"""farm mirror: make <root>/Farm/<name> on a farm PC match a project folder on c4.

Sends only files whose size or modified time differ (tar keeps the times, so the next build is incremental), never
sends Intermediate, Binaries, Saved, DerivedDataCache or .git, and deletes files under Source, Content, Config, Tools
and Script that no longer exist on c4. Usage: python -I mirror.py <host> <root> <name> <project folder on c4>
"""
import os
import subprocess
import sys
import tempfile
import time

SKIP = {"Intermediate", "Binaries", "Saved", "DerivedDataCache", ".git"}
PRUNE = ("Source/", "Content/", "Config/", "Tools/", "Script/")
TAR = r"C:\Windows\System32\tar.exe"


def ssh(host, cmd, data=None):
    r = subprocess.run(["ssh", host, cmd], input=data, capture_output=True)
    if r.returncode:
        sys.exit(f"FARM ssh {host} failed ({r.returncode}): {cmd}\n{r.stderr.decode(errors='replace')}")
    return r.stdout.decode("utf-8", errors="replace")


def main():
    host, root, name, proj = sys.argv[1:5]
    proj = os.path.abspath(proj)
    if not os.path.isfile(os.path.join(proj, "Supercut.uproject")):
        sys.exit(f"FARM no Supercut.uproject in {proj}")
    dest = f"{root}\\Farm\\{name}"
    t0 = time.time()
    remote = {}
    for line in ssh(host, f"powershell -NoProfile -ExecutionPolicy Bypass -File {root}\\Farm\\_farm\\list.ps1 -Dir {dest}").splitlines():
        rel, size, mtime = line.rsplit("|", 2)
        remote[rel] = (int(size), int(mtime))
    local = {}
    for top in os.listdir(proj):
        if top in SKIP:
            continue
        p = os.path.join(proj, top)
```

### Mon 16 Nov 00:22:25 · Agent (claude-opus-5-5)

Lane folder made, worktree is on ae8614e, pc2 is free with 36 GB on C:. Starting the mirror now, then reading the gotchas while it copies.

**Mon 16 Nov 00:22:28 · Tool call: Bash** (Mirror the worktree to pc2 as ship1)

```
cd "[notes]/unreal/megajam-2026/farm"; mkdir -p /d/UE/ship1_farmlogs; date "+%d %b %H:%M:%S"; time ./farm.sh mirror pc2 ship1 /d/UE/wt/maincheck_x > /d/UE/ship1_farmlogs/mirror.out 2>&1; echo "exit $?"; date "+%d %b %H:%M:%S"; tail -5 /d/UE/ship1_farmlogs/mirror.out
```

Result:

```
Command running in background with ID: b2qxquw9t. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\b2qxquw9t.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\farm; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Mon 16 Nov 00:22:28 · Tool call: Bash** (List GOTCHAS section headings near the target lines)

```
G="[notes]/unreal/GOTCHAS.md"; grep -n "^## \|^### " "$G" | awk -F: '$1>560 && $1<1000'
```

Result:

```
580:## Windows Firewall prompt for every new Unreal exe path (13 Nov 2026, verified)
599:## SUPERCUT enemies lane (13 Nov 2026, c4, engine 5.9 preview)
631:## SUPERCUT pc2 test lane 2: launcher and frame rate (13 Nov 2026, c4 to pc2, engine 5.9 preview)
670:## Scripted game runs depend on frame timing unless the time step is fixed (13 Nov 2026, verified)
682:## SUPERCUT puzzles lane (13 Nov 2026, c4, engine 5.9 preview)
710:## SUPERCUT audiowire lane (13 Nov 2026, c4, engine 5.9 preview)
746:## SUPERCUT slice lane (13 Nov 2026, c4, engine 5.9 preview)
769:## SUPERCUT slice2 lane (13 Nov 2026, c4, engine 5.9 preview)
784:## SUPERCUT feel1 lane: tuning file and practice keys (13 Nov 2026, c4, engine 5.9 preview)
804:## SUPERCUT figin lane: skinned enemies (13 Nov 2026, c4, engine 5.9 preview)
829:## SUPERCUT feel2 lane: hit feedback (14 Nov 2026, c4, engine 5.9 preview)
845:## SUPERCUT light1 lane: lamp, glows, sketch (14 Nov 2026, c4, engine 5.9 preview)
880:## Shipping builds and user settings (5.9, lane shell1)
912:## SUPERCUT onboard1 lane (14 Nov 2026, c4, engine 5.9 preview)
941:## SUPERCUT mix1 lane: master limiter and mix measuring (14 Nov 2026, c4, engine 5.9 preview)
962:## SUPERCUT first1 lane: first start, sound tuning, title hatching (14 Nov 2026, c4 and pc2, engine 5.9 preview)
982:## SUPERCUT props1 lane: set props (14 Nov 2026, c4, engine 5.9 preview)
```

**Mon 16 Nov 00:22:38 · Tool call: Bash** (Read firewall, Shipping and tuning sections of GOTCHAS)

```
G="[notes]/unreal/GOTCHAS.md"; sed -n 580,598p "$G"; echo ----; sed -n 880,911p "$G"; echo ----; sed -n 784,803p "$G"
```

Result:

```
## Windows Firewall prompt for every new Unreal exe path (13 Nov 2026, verified)

- **Trap.** Every non-Shipping Unreal program (editor, UnrealEditor-Cmd, UnrealPak, a packaged Development game)
  listens on TCP port 1985 on all addresses: the trace control port (`LogTrace: Display: Control listening on port
  1985`, `TraceLog/Private/Trace/Control.cpp`). Windows Firewall shows a "Windows Security Alert" with an admin
  shield for each new exe path, so every new package folder raises one. It looks like a UAC prompt. The game runs
  whether or not anyone answers it.
- **No runtime switch.** The listener is compiled in (`TRACE_PRIVATE_ALLOW_TCP_CONTROL`). Tracing is off in Shipping
  builds (`UE_TRACE_ENABLED` is 0 there, `TraceLog/Public/Trace/Config.h`), so a Shipping build should not listen and
  should not raise the prompt. Not yet seen: check the listeners of our Shipping build before it goes to judges
  (`Get-NetTCPConnection -State Listen -OwningProcess <pid>`).
- **Fix on our PCs (owner asked, 13 Nov 10:00).** The prompt is turned off on c4 and pc2:
  `Set-NetFirewallProfile -All -NotifyOnListen False` (needs admin; on c4 it went through ElevRunner request
  `megajam-fw-notify-off-20261113`). The firewall stays on. A new app that listens is now blocked from inbound
  connections without a prompt. Undo: the same command with `True`.
- **How it was found.** The firewall's event log names the exe behind each prompt:
  `Microsoft-Windows-Windows Firewall With Advanced Security/Firewall`, event 2097 when the prompt is raised and 2099
  when someone answers it.

----
## Shipping builds and user settings (5.9, lane shell1)

- **A Shipping build writes no log, and `-log` / `-abslog=` change nothing** (14 Nov 2026, verified). Shipping has
  `NO_LOGGING`, so `UE_LOG` compiles away. `bUseLoggingInShipping` would turn it back on, but it needs a unique build
  environment, which an installed engine refuses (RulesAssembly.cs). A Shipping run with `-log -abslog=<file>`
  left no file. SUPERCUT's fix: under `NO_LOGGING`, `Supercut.h` redefines `UE_LOG` to write to the file named by
  `-SupercutLog=<file>` (Fatal still stops the game).
- **Shipping ignores `-FPS=`** (14 Nov 2026, verified). LaunchEngineLoop.cpp reads it inside
  `#if !UE_BUILD_SHIPPING`, so `-UseFixedTimeStep` alone steps at the default 1/30 s. The game module reads `-FPS=`
  itself in Shipping and calls `FApp::SetFixedDeltaTime`. `-UseFixedTimeStep` and `-DeterministicAudio` work in
  every build.
-
[... 3953 more characters not shown]
```

**Mon 16 Nov 00:23:00 · Tool call: Bash** (Find how held1 and shell1 ran Shipping)

```
L="[notes]/unreal/megajam-2026/lanes"; for l in held1 shell1; do echo "=== $l"; grep -n -i "shipping\|SupercutLog\|LOCALAPPDATA\|main8_ship" "$L/$l/HANDOFF.md" | head -30; done; ls "$L/held1" "$L/shell1"
```

Result:

```
=== held1
86:- Shipping package (d7d0115): `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17` (`logs/main8_shipping.log`)
143:cmd /c Tools\package_shipping.cmd
145:powershell -File Tools\run_demo.ps1 -Shipping -Run main8 -Seed 1 -Script "D:\UE\Projects\Supercut59\Script\main8.txt" -FixedFps 240 -Silent -Log <log>
151:Check the make_held log for `SUPERCUT make_held: 7 meshes`. Copy `%LOCALAPPDATA%\Supercut` aside before a Shipping
158:- No pictures from the Shipping package, only its run line.
169:- The Shipping package writes `%LOCALAPPDATA%\Supercut` (GameUserSettings.ini, a crash client folder). Back it up and restore it.
=== shell1
239:- The Shipping package. Only the development package was run.
[notes]/unreal/megajam-2026/lanes/held1:
BRIEF.md
HANDOFF.md
LOG.md
logs
scripts
shots
tools

[notes]/unreal/megajam-2026/lanes/shell1:
BRIEF.md
HANDOFF.md
HANDOFF_menus_14nov_am.md
LOG.md
LOG_menus_14nov_am.md
hall_4up.jpg
out
shots
shots_menus_14nov_am
```

**Mon 16 Nov 00:23:20 · Tool call: Bash** (Read held1's Shipping run procedure)

```
L="[notes]/unreal/megajam-2026/lanes"; sed -n 138,172p "$L/held1/HANDOFF.md"; grep -n -i "shipping\|LOCALAPPDATA" "$L/held1/LOG.md" | head -30
```

Result:

````
D:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor-Cmd.exe D:\UE\Projects\Supercut59\Supercut.uproject -run=pythonscript -Script=D:\UE\Projects\Supercut59\Tools\make_held.py -AllowCommandletRendering -unattended -nopause -nosplash -abslog=<log>
powershell -File Tools\build.ps1
powershell -File Tools\run_tests.ps1 -Filter Supercut.Held
powershell -File Tools\run_tests.ps1
cmd /c Tools\package.cmd
cmd /c Tools\package_shipping.cmd
powershell -File Tools\run_demo.ps1 -Packaged -Run main8 -Seed 1 -Script "D:\UE\Projects\Supercut59\Script\main8.txt" -FixedFps 240 -Silent -Log <log>
powershell -File Tools\run_demo.ps1 -Shipping -Run main8 -Seed 1 -Script "D:\UE\Projects\Supercut59\Script\main8.txt" -FixedFps 240 -Silent -Log <log>
powershell -File Tools\run_demo.ps1 -Packaged -Room fight/01_wind_machine -Dev -Script <copy of scripts\pics.txt> -Shots <folder> -ResX 1920 -ResY 1080 -FixedFps 240 -Silent -Log <log>
python -I tools\tojpg.py <png folder> <jpg folder> after_
python -I tools\gun_area.py <reload-mid picture> <picture> [mask.png]
```

Check the make_held log for `SUPERCUT make_held: 7 meshes`. Copy `%LOCALAPPDATA%\Supercut` aside before a Shipping
run and put it back after. Give run_demo a script path with no space in it (I used a scratch copy of `pics.txt`).

## Not done or not checked

- No one has played it by hand. This PC allows no real input, so every check is scripted.
- The hammer, trigger and cylinder motion is checked by test only. No picture shows it at a readable size.
- No pictures from the Shipping package, only its run line.
- Nothing holds the gun. The brief says to import no glove or hand mesh, so this stays until a hand is approved.
- The revolver body texture has about 0.36% red-orange pixels (worn brass). I read that as material, not a new signal colour, but it is the owner's call.
- The gotchas below are not copied to `unreal/GOTCHAS.md`, and there is no DEVLOG entry: the brief lets me write only in this folder outside the game repo.
- The LOG.md clock times from 13:20 to 14:00 run ahead of the real ones; the note at 13:22 there gives the real commit times.

## Gotchas

- `UStaticMesh::IsNaniteEnabled` is editor only. `package.cmd` builds the game target with the dev automation tests, so a test that calls it compiles in the editor and breaks the package (C2039). `HasValidNaniteData()` works in both.
- Importing `make_props` from `make_held` writes `Tools/__pycache__` unless the importer sets `sys.dont_write_bytecode = True` first.
- The
[... 1117 more characters not shown]
````

**Mon 16 Nov 00:23:26 · Tool call: Bash** (Read run_demo.ps1 options for Shipping)

```
cd /d/UE/wt/maincheck_x; grep -n -i "shipping\|SupercutLog\|param\|\$Log\b\|exit" Tools/run_demo.ps1 | head -60
```

**Mon 16 Nov 00:23:26 · Tool call: Bash** (See how farm.sh run step calls run_demo)

```
cd "[notes]/unreal/megajam-2026/farm"; ls remote; grep -n "step()" -A60 farm.sh | grep -n -i "run\|ship\|builds\|{P}\|{B}" | head -40
```

Result:

```
5:#        [-FixedFps <n>] [-Silent] [-Record <file.wav>] [-Upgrades <name>,<name>] [-Dev] [-Title] [-Shipping]
7:# Exit code: 0 the script finished, 2 the script failed (the player died when the script did not expect it,
9:param(
17:    [string]$Log = "$(Split-Path -Parent $PSScriptRoot)\Saved\Logs\demo.log",
29:    [switch]$Shipping  # the Shipping package (D:\UE\Builds\Supercut59_ship unless -Exe says otherwise). It writes no engine
30:                       # log, so -Log is filled by the game's own -SupercutLog= instead of -abslog=
32:if ($Shipping) {
34:    if (-not $PSBoundParameters.ContainsKey('Exe')) { $Exe = "D:\UE\Builds\Supercut59_ship\Windows\Supercut.exe" }
49:if ($Shipping) { $gameArgs += "`"-SupercutLog=$Log`"" } else { $gameArgs += "`"-abslog=$Log`"" }
65:$null = $p.Handle   # without this PowerShell does not keep the exit code of a process it did not wait on
66:if (-not $p.WaitForExit($TimeoutSeconds * 1000)) {
73:    exit 3
75:Write-Output "game exit code $($p.ExitCode)"
76:exit $p.ExitCode
Shell cwd was reset to [notes]
```

Result:

```
del.ps1
list.ps1
status.ps1
step.ps1
tree.ps1
vs_install.ps1
4:129-  case "$s" in build|package|package-shipping) take_ubt "$host" "$name" "$s" ;; esac
42:167-      mkdir -p "$froot/_farm" "$froot/_out" "$froot/_builds" || exit 1
57:182-  build|test|package|package-shipping|run)
```

**Mon 16 Nov 00:23:33 · Tool call: Bash** (Read remote step.ps1 and run_demo.ps1)

```
cd "[notes]/unreal/megajam-2026/farm"; cat remote/step.ps1; sed -n 1,76p /d/UE/wt/maincheck_x/Tools/run_demo.ps1
```

Result:

```
# farm step: runs one of the project's own Tools scripts in the mirror <Root>\Farm\<Name> and leaves its logs in
# <Root>\Farm\_out\<Name>\<Step>. Exit code: the Tools script's exit code.
# The project's package.cmd, package_shipping.cmd, run_tests.ps1 and run_demo.ps1 name c4's D:\UE\UE_5.9 and
# D:\UE\Builds. Each run writes a copy of the script beside it as Tools\farm_<file> with those paths mapped to this
# PC (engine <Root>\UE_5.9, builds <Root>\Farm\_builds\<Name>), and runs the copy. The next mirror deletes the copy
# (it is not on c4). Any other D:\ left in a copy stops the step.
param(
    [Parameter(Mandatory)][string]$Root,
    [Parameter(Mandatory)][string]$Name,
    [Parameter(Mandatory)][ValidateSet('build', 'test', 'package', 'package-shipping', 'run')][string]$Step,
    [string]$ArgsFile = ''   # one argument per line, passed on to the Tools script
)
$ErrorActionPreference = 'Stop'
$proj = "$Root\Farm\$Name"
$engine = "$Root\UE_5.9"
$builds = "$Root\Farm\_builds\$Name"
$out = "$Root\Farm\_out\$Name\$Step"
if (-not (Test-Path "$proj\Supercut.uproject")) { Write-Output "FARM no project at $proj (mirror first)"; exit 10 }
if (-not (Test-Path "$engine\Engine\Build\Build.version")) { Write-Output "FARM no engine at $engine"; exit 11 }
if (Test-Path $out) { Remove-Item $out -Recurse -Force }
New-Item -ItemType Directory -Force $out, $builds | Out-Null
$extra = @()
if ($ArgsFile) { $extra = @(Get-Content $ArgsFile | Where-Object { $_ -ne '' } | ForEach-Object { $_.Replace('{P}', $proj).Replace('{B}', $builds).Replace('{O}', $out) }) }

$latin1 = [Text.Encoding]::GetEncoding(28591)
function Map([string]$file) {
    $t = [IO.File]::ReadAllText("$proj\Tools\$file", $latin1)
    $t = $t.Replace('D:\UE\UE_5.9', $engine).Replace('D:\UE\Builds', $builds).Replace('cd /d D:\UE', "cd /d $Root")
    # On c4 itself (Root D:\UE) the D:\ paths are the right ones, so the check is for the other PCs only.
    if ($Root -notlike 'D:*' -and $t -match '(?i)\bD:\\') { throw "FARM Tools\$file names a D:\ path the farm does not map: $($Matches[0]) ... fix farm\remote\step.ps1" }
    $dst = "$proj\Tools\farm_$file"
    [IO.File]::WriteAllText($dst, $t, $latin1)
    $dst
}
function Keep([string[]]$files) { foreach ($f in $files) { if (Test-Path $f) { Copy-Item $f $out -Recurse -Force } } }

$logs = "$proj\Saved\Logs"
$ErrorActionPreference = 'Continue'   # under Stop, PowerShell 5.1 turns a native program's stderr line into a terminating error
# The lock on c4 says whose 
[... 9188 more characters not shown]
```

### Mon 16 Nov 00:23:40 · Agent (claude-opus-5-5)

Mirror is copying to pc2. I have the Shipping run method: `farm.sh run ... -Shipping` maps the exe to the ship1 build folder and fills the log through `-SupercutLog=`. Writing LOG.md now.

**Mon 16 Nov 00:23:40 · Tool call: Bash** (Check time and mirror progress)

```
date "+%d %b %H:%M"; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\b2qxquw9t.output"
```

Result:

```
16 Nov 00:23
16 Nov 00:22:29
```

**Mon 16 Nov 00:23:48 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\LOG.md",
 "content": "# ship1 log (16 Nov 2026)\n\nJob: does main `ae8614e` package and play as Shipping, on pc2, farm name `ship1`, logs `/d/UE/ship1_farmlogs`.\n\n- 00:21 Read COMMON_RULES.md. `git -C /d/UE/wt/maincheck_x log --oneline -1` prints `ae8614e`. Lane folder made.\n- 00:22 `farm.sh slots`: pc2 0 of 1 held, c4 CLOSED, [pc-b] CLOSED, [pc-c] has gen4 packaging. pc2 status: 10.3 GB RAM\n  free, CPU 1%, C: 36 GB free, no busy processes.\n- 00:22 Read GOTCHAS \"Shipping builds and user settings\" (880-910) and \"Windows Firewall prompt\" (580-597).\n  FARM.md line 109 says \"No Shipping runs\" on farm PCs because Shipping writes `%LOCALAPPDATA%\\Supercut`; the brief\n  asks for one, so [pick] back that folder up on pc2 before the run and restore it after, as held1 did on c4.\n- 00:22 How held1 proved Shipping (HANDOFF line 145, LOG 22-27): `run_demo.ps1 -Shipping -Run main8 -Seed 1 -Script\n  ... -FixedFps 240 -Silent -Log <log>`. `-Shipping` sets the exe to `D:\\UE\\Builds\\Supercut59_ship\\Windows\\Supercut.exe`\n  and passes `-SupercutLog=<log>` (the game's own log under NO_LOGGING). farm `step.ps1` maps `D:\\UE\\Builds` to\n  `C:\\UE\\Farm\\_builds\\ship1`, so `farm.sh run pc2 ship1 <logs> -Shipping ...` finds the ship1 package.\n- 00:22 Mirror started.\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\LOG.md (file state is current in your context — no need to Read it back)
```

### Mon 16 Nov 00:23:50 · Agent (claude-opus-5-5)

While the mirror runs, step 6: the configuration differences in source.

**Mon 16 Nov 00:23:51 · Tool call: Bash** (Grep Shipping-dependent code in Source)

```
cd /d/UE/wt/maincheck_x; git grep -n "UE_BUILD_SHIPPING\|NO_LOGGING\|WITH_EDITOR\b\|UE_BUILD_DEVELOPMENT\|WITH_DEV_AUTOMATION_TESTS" -- Source | wc -l; git grep -n "UE_BUILD_SHIPPING\|NO_LOGGING" -- Source
```

Result:

```
59
Source/Supercut/Supercut.cpp:18:#if NO_LOGGING
Source/Supercut/Supercut.cpp:57:#if UE_BUILD_SHIPPING
Source/Supercut/Supercut.h:11:#if NO_LOGGING
Source/Supercut/SupercutAudio.cpp:253:	const bool bRawMix = !UE_BUILD_SHIPPING && FParse::Param(FCommandLine::Get(), TEXT("SupercutRawMix"));
Source/Supercut/SupercutAudio.cpp:288:#if !UE_BUILD_SHIPPING
Source/Supercut/SupercutDevGate.cpp:30:		return !UE_BUILD_SHIPPING && FParse::Param(FCommandLine::Get(), TEXT("SupercutDev"));
Source/Supercut/SupercutGameMode.cpp:29:#if !UE_BUILD_SHIPPING
Source/Supercut/SupercutGeneratedRuns.cpp:78:#if UE_BUILD_SHIPPING
Source/Supercut/SupercutPlayerController.cpp:68:#if !UE_BUILD_SHIPPING
Source/Supercut/SupercutPlayerController.cpp:382:#if !UE_BUILD_SHIPPING
Source/Supercut/SupercutPractice.cpp:51:	bOn = !UE_BUILD_SHIPPING && FParse::Param(FCommandLine::Get(), TEXT("SupercutDev"));
Shell cwd was reset to [notes]
```

**Mon 16 Nov 00:24:00 · Tool call: Bash** (Read Shipping-gated code blocks, part 1)

```
cd /d/UE/wt/maincheck_x/Source/Supercut; s(){ echo "=== $1 $2-$3"; sed -n "$2,$3p" "$1"; }; s Supercut.cpp 10 80; s Supercut.h 5 30; s SupercutAudio.cpp 245 300; s SupercutDevGate.cpp 15 40
```

**Mon 16 Nov 00:24:01 · Tool call: Bash** (Read Shipping-gated code blocks, part 2)

```
cd /d/UE/wt/maincheck_x/Source/Supercut; s(){ echo "=== $1 $2-$3"; sed -n "$2,$3p" "$1"; }; s SupercutGameMode.cpp 20 50; s SupercutGeneratedRuns.cpp 65 95; s SupercutPlayerController.cpp 60 95; s SupercutPlayerController.cpp 375 400; s SupercutPractice.cpp 40 60
```

Result:

```
=== Supercut.cpp 10-80
#include "Misc/FileHelper.h"
#include "Misc/Parse.h"
#include "Misc/ScopeLock.h"
#include "Modules/ModuleManager.h"

DEFINE_LOG_CATEGORY(LogSupercut);
DEFINE_LOG_CATEGORY(LogSupercutSound);

#if NO_LOGGING
namespace SupercutShippingLog
{
	void Write(const TCHAR* Category, const TCHAR* Verbosity, const FString& Text)
	{
		static FCriticalSection Lock;
		static TUniquePtr<IFileHandle> File;
		static bool bOpened = false;
		FScopeLock Guard(&Lock);
		if (!bOpened)
		{
			bOpened = true;
			FString Path;
			if (FParse::Value(FCommandLine::Get(), TEXT("-SupercutLog="), Path))
			{
				File.Reset(FPlatformFileManager::Get().GetPlatformFile().OpenWrite(*Path));
			}
		}
		if (!File)
		{
			return;
		}
		// As the engine writes a line: "Log" verbosity has no word of its own.
		const FString Word = FCString::Strcmp(Verbosity, TEXT("Log")) == 0 ? FString() : FString(Verbosity) + TEXT(": ");
		const FString Line = FString::Printf(TEXT("[%s][%3d]%s: %s%s\r\n"),
			*FDateTime::Now().ToString(TEXT("%Y.%m.%d-%H.%M.%S:%s")), int32(GFrameCounter % 1000), Category, *Word, *Text);
		const FTCHARToUTF8 Utf8(*Line);
		File->Write(reinterpret_cast<const uint8*>(Utf8.Get()), Utf8.Length());
		File->Flush();
	}
}
#endif

/** The game module. Its one job of its own: "-SupercutWriteTuning" writes Tuning.example.txt and quits before a window opens. */
class FSupercutModule : public FDefaultGameModuleImpl
{
public:
	virtual void StartupModule() override
	{
#if UE_BUILD_SHIPPING
		// -UseFixedTimeStep is read in every build, but -FPS= only outside Shipping (LaunchEngineLoop.cpp). A scripted
		// Shipping run needs the same fixed step as the Development one, so the game reads it here.
		float Fps = 0.f;
		if (FParse::Value(FCommandLine::Get(), TEXT("-FPS="), Fps) && Fps > 0.f)
		{
			FApp::SetFixedDeltaTime(1.0 / Fps);
		}
#else
		// After engine init, before the first world: FEngineLoop::FinalizePreInit, which runs after this module starts, turns
		// screen messages back on, and the gameplay debugger's manager is made at world start (SupercutDevGate.h).
		if (!SupercutDevGate::IsOn())
		{
			FCoreDelegates::GetOnPostEngineInit().AddLambda([]()
			{
				SupercutDevGate::CloseEngine(*GetMutableDefault<UInputSettings>());
			});
		}
#endif
		if (!FParse::Param(FCommandLine::Get(), TEXT("SupercutWriteTuning")))
		{
			return;
		}
		const FString Path = SupercutTuningFile::TemplatePath();
=== Supercut.h 5-30
// Every line the game writes to the log goes through this
[... 5615 more characters not shown]
```

Result:

```
=== SupercutGameMode.cpp 20-50
	DefaultPawnClass = nullptr;
	PlayerControllerClass = ASupercutPlayerController::StaticClass();
	HUDClass = ASupercutHUD::StaticClass();
}

void ASupercutGameMode::InitGame(const FString& MapName, const FString& Options, FString& ErrorMessage)
{
	Super::InitGame(MapName, Options, ErrorMessage);

#if !UE_BUILD_SHIPPING
	// Before anything is built from the numbers. The time system read the defaults at world start; Begin sets its rules again.
	// A Shipping build plays the numbers it was built with: it never reads Tuning.txt.
	SupercutTuningFile::Load(SupercutTuningFile::FilePath());
#endif

	SupercutProps::Catalogue();   // a bad catalogue stops the game here, before any room is read
	SupercutCredits::Get();       // so does a missing or empty credits file

	FString RunName = TEXT("main");
	FString RoomName;
	int32 Seed = int32(FPlatformTime::Cycles64() & 0x7fffffff);
	FString UpgradeText;
	// Read in every build, so a Shipping build can be checked with a script.
	FParse::Value(FCommandLine::Get(), TEXT("-SupercutRun="), RunName);
	FParse::Value(FCommandLine::Get(), TEXT("-SupercutRoom="), RoomName);
	FParse::Value(FCommandLine::Get(), TEXT("-SupercutSeed="), Seed);
	FParse::Value(FCommandLine::Get(), TEXT("-SupercutUpgrades="), UpgradeText, false);   // false: read past the commas (Parse.cpp)
	TArray<FString> UpgradeNames;
	UpgradeText.ParseIntoArray(UpgradeNames, TEXT(","));
	TArray<FName> Upgrades;
	for (const FString& Name : UpgradeNames)
=== SupercutGeneratedRuns.cpp 65-95
		for (const FString& Word : Words)
		{
			if (!Word.StartsWith(TEXT("catalogue="), ESearchCase::CaseSensitive))
			{
				continue;
			}
			const FString Made = Word.RightChop(10);
			if (Loaded.IsSet() && Made == FString::Printf(TEXT("%08x"), Loaded.GetValue()))
			{
				return;
			}
			const FString Problem = FString::Printf(TEXT("%s:%d: catalogue: the room was made with catalogue %s and the game loaded %s: bake the room again"),
				*File, Index + 1, *Made, Loaded.IsSet() ? *FString::Printf(TEXT("catalogue %08x"), Loaded.GetValue()) : TEXT("no catalogue"));
#if UE_BUILD_SHIPPING
			UE_LOG(LogSupercut, Warning, TEXT("ROOM FILE %s"), *Problem);
#else
			OutErrors.Add(Problem);
#endif
			return;
		}
	}
}
=== SupercutPlayerController.cpp 60-95
{
	// The upgrade and wrap screens pause the game. PlayerTick has to run there, to read the keys and to keep a script going.
	bShouldPerformFullTickWhenPaused = true;
}

void ASupercutPlayerController::InitInputSys
[... 2933 more characters not shown]
```

### Mon 16 Nov 00:24:17 · Agent (claude-opus-5-5)

Notable already: Shipping never reads `Tuning.txt`. Checking whether that changes balance, i.e. whether a tuning file in the repo differs from compiled defaults.

**Mon 16 Nov 00:24:18 · Tool call: Bash** (Find tuning file paths and debug text in source)

```
cd /d/UE/wt/maincheck_x; git grep -n "FilePath()\|TemplatePath()" -- Source | head; git ls-files | grep -i tuning; git grep -n -i "TUNED\|NO DAMAGE" -- Source | head -20
```

Result:

```
Source/Supercut/Supercut.cpp:80:		const FString Path = SupercutTuningFile::TemplatePath();
Source/Supercut/SupercutCredits.cpp:7:FString SupercutCredits::FilePath()
Source/Supercut/SupercutCredits.cpp:64:		const FString File = FilePath();
Source/Supercut/SupercutCredits.h:28:	FString FilePath();
Source/Supercut/SupercutGameMode.cpp:32:	SupercutTuningFile::Load(SupercutTuningFile::FilePath());
Source/Supercut/SupercutPractice.cpp:158:		ReloadTuning(SupercutTuningFile::FilePath());
Source/Supercut/SupercutTuningFile.cpp:596:	FString FilePath()
Source/Supercut/SupercutTuningFile.cpp:601:	FString TemplatePath()
Source/Supercut/SupercutTuningFile.h:77:	FString FilePath();          // <Folder>/Tuning.txt
Source/Supercut/SupercutTuningFile.h:78:	FString TemplatePath();      // <Folder>/Tuning.example.txt
Script/tuning_bad.txt
Script/tuning_f5.txt
Script/tuning_start.txt
Source/Supercut/SupercutTuning.h
Source/Supercut/SupercutTuningFile.cpp
Source/Supercut/SupercutTuningFile.h
Source/Supercut/SupercutTuningTests.cpp
Tools/gen/data/tuning.json
Source/Supercut/SupercutCharacter.cpp:1065:		UE_LOG(LogSupercut, Display, TEXT("PLAYER hit for %.0f, no damage (practice key F4), health %.0f"), Damage, Health);
Source/Supercut/SupercutHUD.cpp:311:	// ---- Top right: tuned values, no damage, the last practice key's answer, the key list.
Source/Supercut/SupercutHUD.cpp:315:	const int32 Tuned = SupercutTuningFile::ChangedNames(FSupercutTuning::Get()).Num();
Source/Supercut/SupercutHUD.cpp:316:	if (Tuned > 0)
Source/Supercut/SupercutHUD.cpp:318:		Label(FString::Printf(TEXT("TUNED: %d value%s"), Tuned, Tuned == 1 ? TEXT("") : TEXT("s")), X, Y, 17.f * S, Gold, false);
Source/Supercut/SupercutHUD.cpp:328:		Label(TEXT("NO DAMAGE"), X, Y, 17.f * S, Red, false);
Source/Supercut/SupercutHUD.h:46:	/** Tuning.txt's bad lines and TUNED count; the practice keys' lines (NO DAMAGE, the last key's answer, the key list). */
Source/Supercut/SupercutPlayerController.h:47: *   report                   log the tuned numbers where they are used: walk speed, view angle, freeze length, charges, look speed, enemy health
Source/Supercut/SupercutPractice.cpp:28:			{ EKeys::F4, TEXT("F4  no damage on / off") },
Source/Supercut/SupercutPractice.cpp:105:		Say(bNoDamage ? TEXT("F4: no damage on") : TEXT("F4: no damage off"));
Source/Supercut/SupercutPractice.cpp:169:	Say(FString::Printf(TEXT("F5: tuning read, %d values tuned, %d bad lines; scene %d restarted"), Changed, Bad, Run.GetSce
[... 1448 more characters not shown]
```

**Mon 16 Nov 00:24:19 · Tool call: Bash** (Check mirror progress)

```
cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\b2qxquw9t.output"; date "+%H:%M"
```

Result:

```
16 Nov 00:22:29
00:24
```

**Mon 16 Nov 00:24:26 · Tool call: Bash** (List other preprocessor gates and read package_shipping.cmd)

```
cd /d/UE/wt/maincheck_x; git grep -n "^#if\|^#elif\|^\s*#if" -- Source | grep -v "UE_BUILD_SHIPPING\|NO_LOGGING" | awk -F: '{print $1": "$3}' | sort | uniq -c | sort -rn | head -30; echo ---; cat Tools/package_shipping.cmd
```

Result:

```
1 Source/SupercutEditor.Target.cs: #if UE_5_9_OR_LATER
      1 Source/Supercut/SupercutWalkTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutViewMotionTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutUiTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutTuningTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutTuningFile.cpp: #if WITH_EDITOR
      1 Source/Supercut/SupercutTracerTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutShoveTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutShellTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutRunTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutRules1Tests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutRoomDoorTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutPuzzleTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutPlayerController.cpp: #if UE_ENABLE_DEBUG_DRAWING
      1 Source/Supercut/SupercutPaceTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutMaterialTests.cpp: #if WITH_DEV_AUTOMATION_TESTS && WITH_EDITOR
      1 Source/Supercut/SupercutLoopTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutLitterTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutHudTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutHudCylinderTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutHudCardsTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutHeldTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutHandsTests.cpp: #if WITH_DEV_AUTOMATION_TESTS && WITH_EDITOR
      1 Source/Supercut/SupercutHandsSkin.h: #if WITH_DEV_AUTOMATION_TESTS && WITH_EDITOR
      1 Source/Supercut/SupercutGunfix1Tests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutGunPartsTests.cpp: #if WITH_DEV_AUTOMATION_TESTS && WITH_EDITOR   // the hands are measured from their imported model (lane hands4)
      1 Source/Supercut/SupercutGunFeelTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutGruntAITests.cpp: #if WITH_DEV_AUTOMATION_TESTS
      1 Source/Supercut/SupercutGenRunTests.cpp: #if WITH_DEV_AUTOMATION_TESTS
---
@echo off
rem Packages the Windows Shipping 
[... 2248 more characters not shown]
```

**Mon 16 Nov 00:24:31 · Tool call: Bash** (Read mirror result)

```
cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\b2qxquw9t.output"; tail -3 /d/UE/ship1_farmlogs/mirror.out
```

Result:

```
16 Nov 00:22:29

real	1m57.096s
user	0m0.077s
sys	0m0.137s
exit 0
16 Nov 00:24:27
FARM mirror pc2:C:\UE\Farm\ship1 sent 3493 files (3557.3 MB), deleted 0, 3493 files in project, 113.8 s

[exited with code 0]
FARM mirror pc2:C:\UE\Farm\ship1 sent 3493 files (3557.3 MB), deleted 0, 3493 files in project, 113.8 s
```

**Mon 16 Nov 00:24:35 · Tool call: Bash** (Build the editor target on pc2 as ship1)

```
cd "[notes]/unreal/megajam-2026/farm"; date "+%d %b %H:%M:%S"; time ./farm.sh build pc2 ship1 /d/UE/ship1_farmlogs -Jobs 8 > /d/UE/ship1_farmlogs/build.out 2>&1; echo "exit $?"; date "+%d %b %H:%M:%S"; tail -5 /d/UE/ship1_farmlogs/build.out
```

Result:

```
Command running in background with ID: bf31zx4r3. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]; directory changes made by the backgrounded command do not apply to subsequent commands.
```

### Mon 16 Nov 00:24:41 · Agent (claude-opus-5-5)

Mirror took 114 s (3,557 MB). Editor build started on pc2. Meanwhile, checking prerequisites settings in the project config.

**Mon 16 Nov 00:24:41 · Tool call: Bash** (Search project config for packaging prerequisite settings)

```
cd /d/UE/wt/maincheck_x; grep -n -i "prereq\|AppLocal\|bShareMaterialShaderCode\|Staging\|ForDistribution\|BuildConfiguration\|CrashReporter" Config/*.ini | head -20
```

Result:

```
Shell cwd was reset to [notes]
```

**Mon 16 Nov 00:24:45 · Tool call: Bash** (Read packaging settings and engine defaults)

```
cd /d/UE/wt/maincheck_x; ls Config; grep -n -i "ProjectPackagingSettings" -A15 Config/DefaultGame.ini | head -30; grep -rn "bIncludePrerequisites\|bIncludeAppLocalPrerequisites" /d/UE/UE_5.9/Engine/Config/BaseGame.ini
```

Result:

```
DefaultEngine.ini
DefaultGame.ini
DefaultInput.ini
5:[/Script/UnrealEd.ProjectPackagingSettings]
6-+MapsToCook=(FilePath="/Game/Maps/Boot")
7-+DirectoriesToAlwaysCook=(Path="/Game/Materials")
8-+DirectoriesToAlwaysCook=(Path="/Game/Audio")
9-+DirectoriesToAlwaysCook=(Path="/Game/Figures")
10-+DirectoriesToAlwaysCook=(Path="/Game/Props")
11-+DirectoriesToAlwaysCook=(Path="/Game/VFX")
12-+DirectoriesToAlwaysCook=(Path="/Game/Hands")
13-+DirectoriesToAlwaysCook=(Path="/Engine/BasicShapes")
14-; The HUD's icons and the two font slots are loaded by name at run time (FSupercutUiStyle), so nothing references them.
15-+DirectoriesToAlwaysCook=(Path="/Game/UI")
16-; Room files and run lists are plain text read at run time. They ship as loose files beside the pak, in Supercut/Content.
17-+DirectoriesToAlwaysStageAsNonUFS=(Path="Rooms")
18-+DirectoriesToAlwaysStageAsNonUFS=(Path="Runs")
19-; The hand poses (Content/Hands/Poses) are read the same way.
20-+DirectoriesToAlwaysStageAsNonUFS=(Path="Hands/Poses")
```

**Mon 16 Nov 00:24:49 · Tool call: Bash** (Find engine prerequisite packaging defaults)

```
grep -rn "IncludePrerequisites\|AppLocalPrerequisites\|ApplocalPrerequisitesDirectory" /d/UE/UE_5.9/Engine/Config/BaseGame.ini /d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/Win/*.cs 2>/dev/null | head; grep -rln "UEPrereqSetup" /d/UE/UE_5.9/Engine/Source/Programs/AutomationTool 2>/dev/null | head -3
```

Result:

```
/d/UE/UE_5.9/Engine/Config/BaseGame.ini:109:IncludePrerequisites=True
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/Win/WinPlatform.Automation.cs
```

**Mon 16 Nov 00:24:54 · Tool call: Bash** (Read how UAT stages prerequisites)

```
F=/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/Win/WinPlatform.Automation.cs; grep -n -i "prereq\|applocal" $F | head -30; sed -n 100,115p /d/UE/UE_5.9/Engine/Config/BaseGame.ini
```

Result:

```
207:		if (Params.Prereqs)
209:			//SC.StageFile(StagedFileType.NonUFS, FileReference.Combine(SC.EngineRoot, "Extras", "Redist", "en-us", "UEPrereqSetup_x64.exe"));
216:		if (!string.IsNullOrWhiteSpace(Params.AppLocalDirectory))
220:				StageAppLocalDependencies(Params, SC, "Win64", Architecture);
246:			Console.WriteLine("Including Game Input prereq installer!");
474:	public void StageAppLocalDependencies(ProjectParams Params, DeploymentContext SC, string SourcePlatformDir, UnrealArch Architecture)
481:		string[] AppLocalDirectories = Params.AppLocalDirectory.Split(';');
482:		foreach (string AppLocalDirectory in AppLocalDirectories)
484:			string ExpandedAppLocalDir = Utils.ExpandVariables(AppLocalDirectory, PathVariables);
487:			DirectoryReference BaseAppLocalDependenciesPath = Path.IsPathRooted(ExpandedAppLocalDir) ? new DirectoryReference(CombinePaths(ExpandedAppLocalDir, SourcePlatformDir, ArchitectureDir)) : DirectoryReference.Combine(SC.ProjectRoot, ExpandedAppLocalDir, SourcePlatformDir, ArchitectureDir);
488:			if (!DirectoryReference.Exists(BaseAppLocalDependenciesPath))
490:				BaseAppLocalDependenciesPath = BaseAppLocalDependenciesPath.ParentDirectory!; // no architecture subfolder - must be user-supplied dependency folder in need of upgrade
491:				if (DirectoryReference.Exists(BaseAppLocalDependenciesPath))
493:					Logger.LogWarning("{path} should have {arch} subfolder with the redist DLLs inside. Falling back to use {path} directly", BaseAppLocalDependenciesPath, Architecture, BaseAppLocalDependenciesPath);
496:			if (DirectoryReference.Exists(BaseAppLocalDependenciesPath))
498:				StageAppLocalDependenciesToDir(SC, BaseAppLocalDependenciesPath, Architecture, StagedDirectoryReference.Combine("Engine", "Binaries", PlatformType.ToString()));
499:				StageAppLocalDependenciesToDir(SC, BaseAppLocalDependenciesPath, Architecture, StagedDirectoryReference.Combine(SC.RelativeProjectRootForStage, "Binaries", PlatformType.ToString()));
503:				Logger.LogWarning("Unable to deploy AppLocalDirectory dependencies. No such path: {BaseAppLocalDependenciesPath}", BaseAppLocalDependenciesPath);
508:	static void StageAppLocalDependenciesToDir(DeploymentContext SC, DirectoryReference BaseAppLocalDependenciesPath, UnrealArch Architecture, StagedDirectoryReference StagedBinariesDir)
521:			Logger.LogInformation("Copying AppLocal dependencies from {BaseAppLocalDependenciesPath} to {StagedArchitectureBinariesDir}", BaseAppLocalDependenciesPath, StagedArchitectur
[... 672 more characters not shown]
```

**Mon 16 Nov 00:25:00 · Tool call: Bash** (Read prereq staging code and app-local folder)

```
F=/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/Win/WinPlatform.Automation.cs; sed -n 200,250p $F; ls /d/UE/UE_5.9/Engine/Binaries/ThirdParty/AppLocalDependencies/Win64/ 2>&1; ls /d/UE/UE_5.9/Engine/Binaries/ThirdParty/AppLocalDependencies/Win64/* 2>&1 | head -30
```

Result:

```
StageBootstrapExecutable(SC, BootstrapExeName, PrimaryExecutable.Path, null, BootstrapArguments, RemappedStagedFiles);
						}
					}
				}
			}
		}

		if (Params.Prereqs)
		{
			//SC.StageFile(StagedFileType.NonUFS, FileReference.Combine(SC.EngineRoot, "Extras", "Redist", "en-us", "UEPrereqSetup_x64.exe"));
			SC.StageFile(StagedFileType.NonUFS, FileReference.Combine(SC.EngineRoot, "Extras", "Redist", "en-us", "vc_redist.x64.exe"));
			SC.StageFile(StagedFileType.NonUFS, FileReference.Combine(SC.EngineRoot, "Extras", "Redist", "en-us", "vc_redist.arm64.exe")); // always staging arm64 redist in case we are run on an arm64 device in emulation mode

			StageGameInputWindowsRedist(SC);
		}

		if (!string.IsNullOrWhiteSpace(Params.AppLocalDirectory))
		{
			foreach (UnrealArch Architecture in SC.StageTargets.Select( T => T.Receipt.Architectures.SingleArchitecture ).Distinct() )
			{
				StageAppLocalDependencies(Params, SC, "Win64", Architecture);
			}
		}
	}

	/**
	 * Returns true if the project has set the config setting to include the GameInputRedist with its packaging
	 */
	protected bool ShouldStageGameInputWindowsRedist(DeploymentContext SC)
	{
		// Only include the Game Input redist file if the project has opted into via the Engine config setting for their project
		ConfigHierarchy EngineConfig = ConfigCache.ReadHierarchy(ConfigHierarchyType.Engine, DirectoryReference.FromFile(SC.RawProjectPath), UnrealTargetPlatform.Win64);
		
		//		; In YourGameProject/Config/DefaultEngine.ini...
		//		[GameInput]
		//		IncludeRedistFiles=True
		
		EngineConfig.GetBool("GameInput", "IncludeRedistFiles", out bool bShouldIncludeRedistFiles);

		return bShouldIncludeRedistFiles;
	}
	
	protected void StageGameInputWindowsRedist(DeploymentContext SC)
	{
		if (ShouldStageGameInputWindowsRedist(SC))
		{
			Console.WriteLine("Including Game Input prereq installer!");
			
			// Engine/Extras/Redist/en-us/GameInputRedist.msi
			SC.StageFile(StagedFileType.NonUFS, FileReference.Combine(SC.EngineRoot, "Extras", "Redist", "en-us", "GameInputRedist.msi"));	
		}
x64
DirectX
Microsoft.VC.CRT
UCRT
```

**Mon 16 Nov 00:25:08 · Tool call: Bash** (Check how prereqs flag is set; check build progress)

```
grep -rn "Prereqs\b\|IncludePrerequisites" /d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/Scripts/ProjectParams.cs /d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs 2>/dev/null | head; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output"
```

Result:

```
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs:540:			this.Prereqs = InParams.Prereqs;
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs:684:			bool? Prereqs = null,
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs:1054:			this.Prereqs = GetParamValueIfNotSpecified(Command, Prereqs, this.Prereqs, "prereqs");
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs:2614:		public bool Prereqs { get; set; }
/d/UE/UE_5.9/Engine/Source/Programs/AutomationTool/AutomationUtils/ProjectParams.cs:3665:				Logger.LogDebug("Prereqs={Prereqs}", Prereqs);
16 Nov 00:24:35
```

**Mon 16 Nov 00:25:18 · Tool call: Bash** (Append progress to LOG.md)

```
cat >> "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md" <<'EOF'
- 00:24 Mirror done: exit 0, 3493 files, 3557.3 MB, 114 s (00:22:29 to 00:24:27).
- 00:24 Editor build started: `farm.sh build pc2 ship1 /d/UE/ship1_farmlogs -Jobs 8` (00:24:35).
- 00:25 Config differences read (step 6), notes in HANDOFF. No `Tuning.txt` is tracked in git, so balance lives in
  the compiled defaults (`SupercutTuning.h`); Shipping skipping `Tuning.txt` changes nothing for a judge.
- 00:27 Prerequisites: `package_shipping.cmd` passes `-applocaldirectory=...\AppLocalDependencies` and no `-prereqs`.
  Engine: `WinPlatform.Automation.cs:207-214` stages `vc_redist.x64.exe` only when `Params.Prereqs` is set, and
  `ProjectParams.cs:1054` sets that from the `-prereqs` switch alone (BaseGame.ini `IncludePrerequisites=True` is
  the editor's packaging setting). `WinPlatform.Automation.cs:216-222, 474-499` copies the app-local folder
  (`x64\DirectX`, `x64\Microsoft.VC.CRT`, `x64\UCRT`) into `Engine\Binaries\Win64` and `Supercut\Binaries\Win64`.
  To confirm in the package.
EOF
```

Result:

```
(Bash completed with no output)
```

**Mon 16 Nov 00:25:26 · Tool call: Bash** (Check whether the Development package ships a Tuning.txt)

```
cd /d/UE/wt/maincheck_x; grep -n -i "tuning" Tools/package.cmd; sed -n 590,610p Source/Supercut/SupercutTuningFile.cpp; grep -n -i "tuning" .gitignore
```

Result:

```
12:rem Beside Supercut.exe: Tuning.example.txt, written by the packaged game itself so it always matches FSupercutTuning,
13:rem and Play_dev.bat, which starts the game with the practice keys. A Tuning.txt left in the folder is not touched.
15:if exist "%OUT%\Tuning.example.txt" del /q "%OUT%\Tuning.example.txt"
16:"%OUT%\Supercut.exe" -SupercutWriteTuning -nullrhi -unattended -nosplash "-abslog=%PROJ%\Saved\Logs\write_tuning.log"
17:if not exist "%OUT%\Tuning.example.txt" (
18:  echo Tuning.example.txt was not written: see Saved\Logs\write_tuning.log
		return FPaths::ConvertRelativePathToFull(FPaths::ProjectDir());
#else
		return FPaths::ConvertRelativePathToFull(FPaths::RootDir());
#endif
	}

	FString FilePath()
	{
		return FPaths::Combine(Folder(), TEXT("Tuning.txt"));
	}

	FString TemplatePath()
	{
		return FPaths::Combine(Folder(), TEXT("Tuning.example.txt"));
	}

	void Load(const FString& Path)
	{
		FSupercutTuning& Tuning = FSupercutTuning::Get();
		Tuning = FSupercutTuning();
		Problems.Reset();
16:# Tuning.txt and its template, when an editor build reads or writes them in the project folder
17:/Tuning.txt
18:/Tuning.example.txt
Shell cwd was reset to [notes]
```

**Mon 16 Nov 00:25:31 · Tool call: ToolSearch**

```
{
 "query": "select:mcp__t3-code__t3_background_wait",
 "max_results": 1
}
```

Result:

```

```

**Mon 16 Nov 00:25:32 · Tool call: mcp__t3-code__t3_background_wait**

```
{
 "taskIds": [
  "bf31zx4r3"
 ]
}
```

Result:

```
{"matched":["bf31zx4r3"],"unmatched":[]}
```

**Mon 16 Nov 00:25:36 · Tool call: Bash** (Read debug-drawing block and engine define)

```
cd /d/UE/wt/maincheck_x/Source/Supercut; n=$(grep -n "UE_ENABLE_DEBUG_DRAWING" SupercutPlayerController.cpp | cut -d: -f1); sed -n "$((n-3)),$((n+20))p" SupercutPlayerController.cpp; grep -rn "define UE_ENABLE_DEBUG_DRAWING" /d/UE/UE_5.9/Engine/Source/Runtime/Core/Public/Misc/Build.h
```

Result:

```
const FViewport* Viewport = Client ? Client->Viewport : nullptr;
	const bool bSlate = FSlateApplicationBase::IsInitialized();
	const TSharedPtr<GenericApplication> Platform = bSlate ? FSlateApplicationBase::Get().GetPlatformApplication() : nullptr;
#if UE_ENABLE_DEBUG_DRAWING
	const FString Mode = GetCurrentInputModeDebugString();
#else
	const FString Mode = TEXT("(not kept in this build)");
#endif
	return FString::Printf(TEXT("input mode %s, capture %s, lock %s, viewport has capture %d, raw input %d, cursor %s, app active %d"),
		*Mode,
		Client ? *UEnum::GetValueAsString(Client->GetMouseCaptureMode()) : TEXT("none"),
		Client ? *UEnum::GetValueAsString(Client->GetMouseLockMode()) : TEXT("none"),
		Viewport && Viewport->HasMouseCapture() ? 1 : 0,
		Platform.IsValid() && Platform->IsUsingHighPrecisionMouseMode() ? 1 : 0,
		bShowMouseCursor ? TEXT("shown") : TEXT("hidden"),
		bSlate && FSlateApplicationBase::Get().IsActive() ? 1 : 0);
}

void ASupercutPlayerController::WatchMouse()
{
	// A read, each frame, of the live mouse state; any change is logged. Without capture the engine reads the look
	// from the cursor's travel over the viewport, which stops at the screen's edge. So in play, with the window in
	// front, a lost capture (alt-tab, a click outside, a released button) is taken again through the one way back.
	const bool bActive = FSlateApplicationBase::IsInitialized() && FSlateApplicationBase::Get().IsActive();
```

**Mon 16 Nov 00:25:50 · Tool call: Bash** (Check engine console and debug defaults in Shipping)

```
B=/d/UE/UE_5.9/Engine/Source/Runtime/Core/Public/Misc/Build.h; grep -n "ALLOW_CONSOLE\|UE_ENABLE_DEBUG_DRAWING\|define ENABLE_VISUAL_LOG\|ALLOW_DEBUG_FILES\b" $B | head; sed -n 1,60p /d/UE/wt/maincheck_x/Source/Supercut/SupercutDevGate.cpp | sed -n 40,60p; grep -rn "WITH_GAMEPLAY_DEBUGGER\b" /d/UE/UE_5.9/Engine/Source/Runtime/Engine/Engine.Build.cs /d/UE/UE_5.9/Engine/Source/Developer/GameplayDebugger/GameplayDebugger.Build.cs 2>/dev/null | head -5
```

Result:

```
214:#ifndef ALLOW_CONSOLE_IN_SHIPPING
215:	#define ALLOW_CONSOLE_IN_SHIPPING 0
235:	ALLOW_DEBUG_FILES								If true, then debug files like screen shots and profiles can be saved from the executable.
260:	#ifndef ALLOW_DEBUG_FILES
261:		#define ALLOW_DEBUG_FILES								1
263:	#ifndef ALLOW_CONSOLE
264:		#define ALLOW_CONSOLE									1
288:	#ifndef ALLOW_DEBUG_FILES
289:		#define ALLOW_DEBUG_FILES								1
291:	#ifndef ALLOW_CONSOLE
		// Every engine screen message is drawn behind this (UnrealEngine.cpp:13004 and :18654).
		GAreScreenMessagesEnabled = false;
	}

	void CloseInput(UPlayerInput& Input)
	{
		// GetBind looks only here (PlayerInput.cpp:2646), and InputKey runs what GetBind returns (:388, :475).
		Input.DebugExecBindings.Empty();
	}

	FString StartLine(bool bOn, const UInputSettings& Settings, const UPlayerInput& Input)
	{
		return FString::Printf(TEXT("DEV features %s: console keys %d, debug bindings %d, gameplay debugger %s, on-screen messages %s"),
			bOn ? TEXT("on (-SupercutDev)") : TEXT("off"), Settings.ConsoleKeys.Num(), Input.DebugExecBindings.Num(),
			DevGateDebugger().GetBool() ? TEXT("on") : TEXT("off"), GAreScreenMessagesEnabled ? TEXT("on") : TEXT("off"));
	}
}
```

**Mon 16 Nov 00:25:59 · Tool call: Bash** (Check Shipping console default; build progress)

```
B=/d/UE/UE_5.9/Engine/Source/Runtime/Core/Public/Misc/Build.h; sed -n 300,330p $B | grep -n "ALLOW_CONSOLE\|UE_BUILD_SHIPPING\|define" ; grep -n "ALLOW_CONSOLE" $B; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output"; date +%H:%M
```

Result:

```
3:		#define DO_CHECK										USE_CHECKS_IN_SHIPPING
6:		#define DO_ENSURE										USE_ENSURES_IN_SHIPPING
9:		#define ENABLE_STATNAMEDEVENTS							(!FORCE_USE_STATS && !USE_STATS_WITHOUT_ENGINE)
12:		#define ENABLE_STATNAMEDEVENTS_UOBJECT 					(ENABLE_STATNAMEDEVENTS)
15:		#define STATS											(FORCE_USE_STATS && !ENABLE_STATNAMEDEVENTS)
18:		#define ALLOW_DEBUG_FILES								1
20:	#ifndef ALLOW_CONSOLE
21:		#define ALLOW_CONSOLE									1
24:		#define NO_LOGGING										!USE_LOGGING_IN_SHIPPING
26:#elif UE_BUILD_SHIPPING
28:		#define DO_GUARD_SLOW								0
31:		#define DO_CHECK									USE_CHECKS_IN_SHIPPING
214:#ifndef ALLOW_CONSOLE_IN_SHIPPING
215:	#define ALLOW_CONSOLE_IN_SHIPPING 0
263:	#ifndef ALLOW_CONSOLE
264:		#define ALLOW_CONSOLE									1
291:	#ifndef ALLOW_CONSOLE
292:		#define ALLOW_CONSOLE									1
319:	#ifndef ALLOW_CONSOLE
320:		#define ALLOW_CONSOLE									1
347:	#ifndef ALLOW_CONSOLE
348:		#define ALLOW_CONSOLE								ALLOW_CONSOLE_IN_SHIPPING
16 Nov 00:24:35
00:26
```

**Mon 16 Nov 00:26:13 · Tool call: Bash** (Check engine screen message and debugger guards)

```
U=/d/UE/UE_5.9/Engine/Source/Runtime/Engine/Private/UnrealEngine.cpp; sed -n 12990,13010p $U; grep -n "ENABLE_DRAW_DEBUG\b" /d/UE/UE_5.9/Engine/Source/Runtime/Engine/Public/EngineDefines.h | head -3; grep -rn "WITH_GAMEPLAY_DEBUGGER_CORE=\|WITH_GAMEPLAY_DEBUGGER_CORE\"" /d/UE/UE_5.9/Engine/Source/Runtime/Engine/Engine.Build.cs | head -3
```

Result:

```
const int32 FPSXOffset	= (FPlatformProperties::SupportsWindowedMode() ? 110 : 250);
	const int32 StatsXOffset = 100;// FPlatformProperties::SupportsWindowedMode() ? 4 : 100;

	static const int32 MessageStartY = GIsEditor ? 45 : 100; // Account for safe frame
	int32 MessageY = MessageStartY;

	const FVector2D FontScale(1, 1);
	const int32 FontSizeY = 20;
#if !UE_BUILD_SHIPPING
	const int32 MessageX = 40;
	FCanvasTextItem SmallTextItem(FVector2D(0, 0), FText::GetEmpty(), GEngine->GetSmallFont(), FLinearColor::White);
	SmallTextItem.Scale = FontScale;
	SmallTextItem.EnableShadow(FLinearColor::Black);

	bool bShowScreenMessages = !GIsHighResScreenshot && !GIsDumpingMovie && GAreScreenMessagesEnabled;
	if (bShowScreenMessages)
	{
		// Draw map warnings?
		if (!GEngine->bSuppressMapWarnings)
		{
			MessageY = DrawMapWarnings(World, Viewport, Canvas, CanvasObject, MessageX, MessageY);
```

**Mon 16 Nov 00:26:20 · Tool call: Bash** (Check whether pc2 has a Supercut user settings folder)

```
ssh pc2 'powershell -NoProfile -Command "$d=Join-Path $env:LOCALAPPDATA ''Supercut''; if (Test-Path $d) { ''exists''; Get-ChildItem $d -Recurse -File | ForEach-Object { $_.FullName.Substring($d.Length) + '' '' + $_.Length } } else { ''absent'' }"'
```

Result:

```
exists : The term 'exists' is not recognized as the name of a cmdlet, function, script file, or operable program. 
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:62
+ ... n-Path $env:LOCALAPPDATA Supercut; if (Test-Path $d) { exists; Get-Ch ...
+                                                            ~~~~~~
    + CategoryInfo          : ObjectNotFound: (exists:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
\Saved\Supercut_PCD3D_SM6.upipelinecache34800
\Saved\Config\CrashReportClient\UECC-Windows-1C547C3841C4675998E366BAC55A27D3\CrashReportClient.ini239
\Saved\Config\CrashReportClient\UECC-Windows-2818CCBD4EE58FC16BDF909119830C1B\CrashReportClient.ini239
\Saved\Config\CrashReportClient\UECC-Windows-3FB9F4814BCBF415EE87818563806BE0\CrashReportClient.ini239
\Saved\Config\CrashReportClient\UECC-Windows-9972FFF54AA6D331FE11F8A59045AD88\CrashReportClient.ini239
\Saved\Config\CrashReportClient\UECC-Windows-F96CE6124C1473806CBE07846138D9FD\CrashReportClient.ini239
\Saved\Config\Windows\GameUserSettings.ini2244
```

**Mon 16 Nov 00:26:38 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\appdata.ps1",
 "content": "# ship1: back up or restore %LOCALAPPDATA%\\Supercut on the PC this runs on, around a Shipping run.\n# backup: copies the folder to C:\\UE\\Farm\\_out\\ship1\\appdata_backup (fails if a backup is already there).\n# restore: deletes the live folder and puts the backup back, then lists both so they can be compared.\n# list: prints relative path, size and SHA256 of every file in the live folder. Prints no user or computer names.\nparam([Parameter(Mandatory)][ValidateSet('backup', 'restore', 'list')][string]$Mode)\n$ErrorActionPreference = 'Stop'\n$live = Join-Path $env:LOCALAPPDATA 'Supercut'\n$bak = 'C:\\UE\\Farm\\_out\\ship1\\appdata_backup'\nfunction Show([string]$dir, [string]$tag) {\n    if (-not (Test-Path $dir)) { Write-Output \"$tag absent\"; return }\n    Get-ChildItem $dir -Recurse -File | Sort-Object FullName | ForEach-Object {\n        \"$tag $($_.FullName.Substring($dir.Length)) $($_.Length) $((Get-FileHash $_.FullName -Algorithm SHA256).Hash.Substring(0,12))\"\n    }\n}\nswitch ($Mode) {\n    'backup' {\n        if (Test-Path $bak) { throw \"backup already exists at $bak\" }\n        if (-not (Test-Path $live)) { New-Item -ItemType Directory -Force $bak | Out-Null; New-Item -ItemType File \"$bak\\.was_absent\" | Out-Null; Write-Output 'live folder absent; marker written'; break }\n        New-Item -ItemType Directory -Force (Split-Path $bak) | Out-Null\n        Copy-Item $live $bak -Recurse\n        Show $bak 'BAK'\n    }\n    'restore' {\n        if (-not (Test-Path $bak)) { throw \"no backup at $bak\" }\n        if (Test-Path $live) { Remove-Item $live -Recurse -Force }\n        if (-not (Test-Path \"$bak\\.was_absent\")) { Copy-Item $bak $live -Recurse }\n        Show $live 'LIVE'\n        Show $bak 'BAK'\n    }\n    'list' { Show $live 'LIVE' }\n}\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\appdata.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:26:44 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\listen.ps1",
 "content": "# ship1: while a Shipping run is going, record which TCP and UDP ports the game's processes listen on.\n# Needs no admin: Get-NetTCPConnection and Get-NetUDPEndpoint read the tables for every process.\n# Polls every 5 s for up to $Seconds, writes one line per sample to $Out. Prints no user or computer names.\nparam([int]$Seconds = 900, [string]$Out = 'C:\\UE\\Farm\\_out\\ship1\\listen.txt')\n$end = (Get-Date).AddSeconds($Seconds)\n$seen = $false\n\"start $(Get-Date -Format HH:mm:ss)\" | Out-File -Encoding ascii $Out\nwhile ((Get-Date) -lt $end) {\n    $procs = @(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -like 'Supercut*' })\n    if ($procs.Count -gt 0) {\n        $seen = $true\n        foreach ($p in $procs) {\n            $tcp = @(Get-NetTCPConnection -State Listen -OwningProcess $p.Id -ErrorAction SilentlyContinue | ForEach-Object { \"$($_.LocalAddress):$($_.LocalPort)\" })\n            $udp = @(Get-NetUDPEndpoint -OwningProcess $p.Id -ErrorAction SilentlyContinue | ForEach-Object { \"$($_.LocalAddress):$($_.LocalPort)\" })\n            \"$(Get-Date -Format HH:mm:ss) $($p.ProcessName) pid=$($p.Id) tcp_listen=[$($tcp -join ' ')] udp=[$($udp -join ' ')]\" | Out-File -Append -Encoding ascii $Out\n        }\n    } elseif ($seen) {\n        break\n    }\n    Start-Sleep -Seconds 5\n}\n\"end $(Get-Date -Format HH:mm:ss) seen=$seen\" | Out-File -Append -Encoding ascii $Out\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\listen.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:26:50 · Tool call: Bash** (Copy helper scripts to pc2 and check build progress)

```
ssh pc2 'powershell -NoProfile -Command "New-Item -ItemType Directory -Force C:\UE\Farm\_out\ship1_tools | Out-Null"' && scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/"*.ps1 pc2:C:/UE/Farm/_out/ship1_tools/ && echo copied; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output"; date +%H:%M; ssh pc2 'powershell -NoProfile -Command "Get-ChildItem C:\UE\Farm\ship1\Saved\Logs -Filter ubt*.log | Sort LastWriteTime | Select -Last 1 | ForEach-Object { Get-Content $_.FullName -Tail 3 }"'
```

Result:

```
copied
16 Nov 00:24:35
00:27
[109/158] Compile [x64] SupercutRun.cpp [NoUba]
[110/158] Compile [x64] SupercutRusher.cpp [NoUba]
[111/158] Compile [x64] SupercutRunTests.cpp [NoUba]
```

### Mon 16 Nov 00:27:08 · Agent (claude-opus-5-5)

Editor build is at 111 of 158 actions. Waiting for it.

**Mon 16 Nov 00:27:09 · Tool call: Bash** (Wait for editor build to finish)

```
until grep -q "^exit" "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output"; do sleep 20; done; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bf31zx4r3.output"
```

Result:

```
16 Nov 00:24:35

real	2m52.451s
user	0m0.182s
sys	0m0.689s
exit 0
16 Nov 00:27:27
build SupercutEditor on C:\UE\UE_5.9: exit 0. Log: C:\UE\Farm\ship1\Saved\Logs\ubt_SupercutEditor.log
FARM step=build name=ship1 exit=0 secs=168

[exited with code 0]
```

### Mon 16 Nov 00:27:34 · Agent (claude-opus-5-5)

Editor build passed in 168 s. Starting the Shipping package, then checking the build log for errors.

**Mon 16 Nov 00:27:35 · Tool call: Bash** (Package the Shipping build on pc2 as ship1)

```
cd "[notes]/unreal/megajam-2026/farm"; date "+%d %b %H:%M:%S"; time ./farm.sh package-shipping pc2 ship1 /d/UE/ship1_farmlogs > /d/UE/ship1_farmlogs/package_ship.out 2>&1; echo "exit $?"; date "+%d %b %H:%M:%S"; tail -5 /d/UE/ship1_farmlogs/package_ship.out
```

**Mon 16 Nov 00:27:37 · Tool call: Bash** (Check editor build log for errors)

```
ls -R /d/UE/ship1_farmlogs | head; L=$(ls /d/UE/ship1_farmlogs/build/*.log | head -1); echo $L; grep -c . "$L"; grep -n -i "error\b\|error:\| error \|warning C\|: warning" "$L" | head -10; tail -4 "$L"
```

Result:

```
Command running in background with ID: bjfk7af0i. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bjfk7af0i.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]; directory changes made by the backgrounded command do not apply to subsequent commands.
```

Result:

```
/d/UE/ship1_farmlogs:
build
build.out
mirror.out
package_ship.out

/d/UE/ship1_farmlogs/build:
console.txt
farm_step.txt
ubt_SupercutEditor.log
/d/UE/ship1_farmlogs/build/ubt_SupercutEditor.log
348
177:C:\UE\Farm\ship1\Source\Supercut\SupercutHallTests.cpp(311,10): warning C4996: 'UMaterial::bUsedWithInstancedStaticMeshes': Always use the GetUsageByFlag() accessor. - Please update your code to the new API before upgrading to the next release, otherwise your project will no longer compile.
183:C:\UE\Farm\ship1\Source\Supercut\SupercutHudCardsTests.cpp(463,30): warning C4996: 'UFont::CompositeFont': Public access to CompositeFont is deprecated. Use GetCompositeFont(), GetInternalCompositeFont(), or GetMutableInternalCompositeFont() instead. - Please update your code to the new API before upgrading to the next release, otherwise your project will no longer compile.
199:C:\UE\Farm\ship1\Source\Supercut\SupercutMaterialTests.cpp(64,13): warning C4996: 'FMaterial::CacheShaders': Call CacheShaders without EShaderPlatform as its now cached inside the FMaterial - Please update your code to the new API before upgrading to the next release, otherwise your project will no longer compile.
   0.260          [167.423]  +0.000 SaveCasTable
   0.260          [167.427]  +0.061 Saving caches
   0.260          [167.488]  +0.000 FileMetadataPrefetch.Stop()
   0.260          [167.489]  +0.002 TelemetryService.FlushEvents
```

**Mon 16 Nov 00:27:55 · Tool call: Bash** (Count errors and warnings in build log)

```
L=/d/UE/ship1_farmlogs/build/ubt_SupercutEditor.log; grep -c "error" $L; grep -n "error C\|error LNK\|): error" $L | head; grep -c "warning C4996" $L; grep -n "Result: \|Total execution time\|Succeeded" $L | head
```

Result:

```
0
3
275:Result: Succeeded
```

**Mon 16 Nov 00:28:04 · Tool call: Bash** (Append build result to LOG.md)

```
cat >> "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md" <<'EOF'
- 00:27 Editor build done: exit 0, farm step 168 s (00:24:35 to 00:27:27). `ubt_SupercutEditor.log`: `Result: Succeeded`,
  0 lines with "error", 3 deprecation warnings C4996 (all in test files: SupercutHallTests.cpp:311,
  SupercutHudCardsTests.cpp:463, SupercutMaterialTests.cpp:64).
- 00:27 pc2 `%LOCALAPPDATA%\Supercut` already exists (GameUserSettings.ini, 5 CrashReportClient folders, a pipeline
  cache) from an earlier Shipping test. [pick] back it up with `scripts/appdata.ps1 backup` right before the run,
  restore after, and compare hashes. `scripts/listen.ps1` copied to pc2 for the listener check.
- 00:28 Shipping package started: `farm.sh package-shipping pc2 ship1 /d/UE/ship1_farmlogs`.
EOF
```

**Mon 16 Nov 00:28:04 · Tool call: mcp__t3-code__t3_background_wait**

```
{
 "taskIds": [
  "bjfk7af0i"
 ]
}
```

Result:

```
(Bash completed with no output)
```

Result:

```
{"matched":["bjfk7af0i"],"unmatched":[]}
```

### Mon 16 Nov 00:28:12 · Agent (claude-opus-5-5)

Shipping package is running on pc2. It compiles at one job and cooks cold, so I'm checking FARM.md for pc2's expected package time.

**Mon 16 Nov 00:28:12 · Tool call: Bash** (Read farm timing table)

```
sed -n 148,165p "[notes]/unreal/megajam-2026/FARM.md"
```

Result:

```
## Measured (14 Nov, game head 683bff6, against c4)

First build of a new name (cold) unless marked. Build jobs: [pc-b] 8, [pc-c] 6 (its user had the CPU at 53%), pc2 6.
`package` compiles at one job, as the project's script sets.

| Step | [pc-b] | [pc-c] | pc2 | c4 |
| --- | --- | --- | --- | --- |
| Engine copy, 33.5 GiB, 280k files, two at a time | 30 min | 28 min | 26 min | |
| Mirror, first / no change | 4.3 s / 0.6 s | 13.9 s | 13.8 s | |
| Editor build, cold, 41 files | 69 s | 116 s | 277 s | (pc4: 101 s at 4 jobs; game target 83 s) |
| Editor build, 9 changed files, 1 job | 56 s | | | 137 s (10 files, 15:32) |
| Tests, 112 pass | 52 s | 119 s | 91 s | 112 pass |
| Development package | 254 s | 303 s | about 380 s (cook failed at the end, see gotchas), 79 s after | |
| Shipping package | 178 s | | | |
| main8 scripted run, offscreen | 118 s | 179 s | 472 s | |
| `RUN wrapped` line | equal | equal | equal | `takes 1, time 98.2 s, shots 46, freezes 14, kills 17` |

Compilers: [pc-b] MSVC 14.50.35728 (VS 2026 Build Tools, already there); [pc-c], pc2 and c4 14.44.35230.
```

### Mon 16 Nov 00:28:18 · Agent (claude-opus-5-5)

pc2 uses MSVC 14.44, the one that crashed on a Shipping PCH through UBA; the script passes `-NoUBA`, so this run tests that fix too. Waiting on the package.

**Mon 16 Nov 00:28:21 · Tool call: Bash** (Wait up to 9 min for the package, show progress)

```
O="C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bjfk7af0i.output"; for i in $(seq 1 28); do grep -q "^exit" "$O" && break; sleep 20; done; cat "$O"; date +%H:%M; ssh pc2 'powershell -NoProfile -Command "$f=''C:\UE\Farm\ship1\Saved\Logs\package_ship_run.log''; if (Test-Path $f) { (Get-Content $f | Measure-Object -Line).Lines; Get-Content $f -Tail 4 }"' | cut -c1-200
```

Result:

```
16 Nov 00:27:44

real	7m26.586s
user	0m0.105s
sys	0m0.320s
exit 0
16 Nov 00:35:11
FARM step=package-shipping name=ship1 exit=0 secs=438

[exited with code 0]
00:35
Test-Path : Cannot bind argument to parameter 'Path' because it is null.
At line:1 char:68
+ ... \Farm\ship1\Saved\Logs\package_ship_run.log; if (Test-Path $f) { (Get ...
+                                                                ~~
    + CategoryInfo          : InvalidData: (:) [Test-Path], ParameterBindingValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationErrorNullNotAllowed,Microsoft.PowerShell.Commands.TestPathCom 
   mand
```

### Mon 16 Nov 00:35:27 · Agent (claude-opus-5-5)

Shipping package exit 0 in 438 s. Now checking its logs for BUILD SUCCESSFUL, material failures and compile errors.

**Mon 16 Nov 00:35:29 · Tool call: Bash** (Check Shipping package logs for success and errors)

```
D=/d/UE/ship1_farmlogs/package-shipping; ls $D; P=$D/package_ship_run.log; U=$D/ubt_package_ship.log; wc -l $P $U; grep -c "BUILD SUCCESSFUL" $P; grep -c "Failed to compile Material" $P; grep -ci "missing usage flag" $P; grep -n "error C\|error LNK\|): error\|Error: " $P $U | head; grep -n -i "Shipping\b.*Supercut\|Building Supercut\|Result:" $U | head -5; grep -n "Warning:" $P | wc -l
```

Result:

```
console.txt
farm_step.txt
package_ship_run.log
  1228 /d/UE/ship1_farmlogs/package-shipping/package_ship_run.log
wc: /d/UE/ship1_farmlogs/package-shipping/ubt_package_ship.log: No such file or directory
  1228 total
1
0
0
grep: /d/UE/ship1_farmlogs/package-shipping/ubt_package_ship.log: No such file or directory
grep: /d/UE/ship1_farmlogs/package-shipping/ubt_package_ship.log: No such file or directory
2
```

**Mon 16 Nov 00:35:34 · Tool call: Bash** (Find compile, cook and stage milestones in package log)

```
P=/d/UE/ship1_farmlogs/package-shipping/package_ship_run.log; grep -c "Compile \[x64\]" $P; grep -n "Link \[x64\]\|Supercut-Win64-Shipping\|ubt_package_ship\|Total execution time\|Took \|Warning:\|BUILD SUCCESSFUL\|Cook.*Done\|Cooked packages\|Stage command time\|Packaged\|Archive command time\|NoUba\]" $P | head -40
```

Result:

```
115
4:Parsing command line: BuildCookRun -nop4 -utf8output -unattended -nocompileuat -cook -build -project=C:\UE\Farm\ship1\Tools\..\Supercut.uproject -unrealexe=C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor-Cmd.exe -platform=Win64 -installed -stage -archive -package -pak -iostore -compressed -nodebuginfo -applocaldirectory=C:\UE\UE_5.9\Engine\Binaries\ThirdParty\AppLocalDependencies -archivedirectory=C:\UE\Farm\_builds\ship1\Supercut59_ship -clientconfig=Shipping -ubtargs="-MaxParallelActions=1 -NoUBA -NoHotReloadFromIDE -Log=C:\UE\Farm\ship1\Tools\..\Saved\Logs\ubt_package_ship.log"
11:Running: C:\UE\UE_5.9\Engine\Binaries\ThirdParty\DotNet\10.0\win-x64\dotnet.exe "C:\UE\UE_5.9\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.dll" -Target="SupercutEditor Win64 Development -Project=C:\UE\Farm\ship1\Supercut.uproject" -Target="Supercut Win64 Shipping -Project=C:\UE\Farm\ship1\Supercut.uproject  -remoteini=\"C:\UE\Farm\ship1\"  -MaxParallelActions=1 -NoUBA -NoHotReloadFromIDE -Log=C:\UE\Farm\ship1\Tools\..\Saved\Logs\ubt_package_ship.log -skipdeploy " -log="C:\Users\USER\AppData\Roaming\Unreal Engine\AutomationTool\Logs\C+UE+UE_5.9\UBA-SupercutEditor-Win64-Development.txt"
16:Warning: Plugin 'Fab' does not list plugin 'ToolsetRegistry' as a dependency, but module 'FabToolset' depends on module 'ToolsetRegistry'.
55:** For Supercut-Win64-Shipping **
56:[1/124] Compile [x64] SharedPCH.Engine.Project.ValApi.ValExpApi.Cpp20.cpp [NoUba]
57:[2/124] Copy Supercut-Win64-Shipping-Default.rc2 [NoUba]
58:[3/124] Compile Resource [x64] Supercut-Win64-Shipping-Default.rc2 [NoUba]
59:[4/124] Compile [x64] Module.Supercut.cpp [NoUba]
60:[5/124] Compile [x64] Supercut.cpp [NoUba]
61:[6/124] Compile [x64] SupercutAudio.cpp [NoUba]
62:[7/124] Compile [x64] SupercutAudioTests.cpp [NoUba]
63:[8/124] Compile [x64] SupercutChainTests.cpp [NoUba]
64:[9/124] Compile [x64] SupercutCharacter.cpp [NoUba]
65:[10/124] Compile [x64] SupercutChips.cpp [NoUba]
66:[11/124] Compile [x64] SupercutClapMotion.cpp [NoUba]
67:[12/124] Compile [x64] SupercutClapMotionTests.cpp [NoUba]
68:[13/124] Compile [x64] SupercutClapMove.cpp [NoUba]
69:[14/124] Compile [x64] SupercutCredits.cpp [NoUba]
70:[15/124] Compile [x64] SupercutCreditsTests.cpp [NoUba]
71:[16/124] Compile [x64] SupercutCrosshair.cpp [NoUba]
72:[17/124] Compile [x64] SupercutDevGate.cpp [NoUba]
73:[18/124] Compile [x64] SupercutDevGateTests.cpp [NoUba]
74:[19/124] Compile [x64] SupercutDlss.cpp [NoUba]
75:[20/124] Compile [x6
[... 933 more characters not shown]
```

**Mon 16 Nov 00:35:39 · Tool call: Bash** (Show link result, timing and warnings from package log)

```
P=/d/UE/ship1_farmlogs/package-shipping/package_ship_run.log; sed -n 175,190p $P | cut -c1-220; grep -n "Link \[x64\]\|Result:\|Total time in\|took\|Cook command\|LogCook: Display: Cook\b\|Cooked packages\|\*\*\*\*\|ExitCode=\|AutomationTool exiting" $P | cut -c1-200 | head -40; grep -n "Warning:" $P | cut -c1-250
```

Result:

```
[117/124] Compile [x64] StreamlineNGXCommon.cpp [NoUba]
[118/124] Link [x64] Supercut-Win64-Shipping.exe [NoUba]
[119/124] Copy D3D12Core.dll [NoUba]
[120/124] Copy d3d12SDKLayers.dll [NoUba]
[121/124] Copy DirectML.dll [NoUba]
[122/124] Copy tbb12.dll [NoUba]
[123/124] Copy tbbmalloc.dll [NoUba]
[124/124] WriteMetadata Supercut-Win64-Shipping.target [NoUba]

Total time in Unreal Build Accelerator local executor: 314.59 seconds
Output binary: C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor.exe
Output binary: C:\UE\Farm\ship1\Binaries\Win64\Supercut-Win64-Shipping.exe

Result: Succeeded
Trace written to file C:\Users\USER\AppData\Local\UnrealBuildTool\Trace.uba with size 54.9kb
Took 319.08s to run dotnet.exe, ExitCode=0
10:********** BUILD COMMAND STARTED **********
176:[118/124] Link [x64] Supercut-Win64-Shipping.exe [NoUba]
184:Total time in Unreal Build Accelerator local executor: 314.59 seconds
188:Result: Succeeded
190:Took 319.08s to run dotnet.exe, ExitCode=0
193:********** BUILD COMMAND COMPLETED **********
194:********** COOK COMMAND STARTED **********
225:LogConfig: Display: Loading VulkanPC ini files took 0.04 seconds
226:LogConfig: Display: Loading Mac ini files took 0.06 seconds
227:LogConfig: Display: Loading Unix ini files took 0.06 seconds
228:LogConfig: Display: Loading Windows ini files took 0.06 seconds
229:LogConfig: Display: Loading Android ini files took 0.07 seconds
230:LogConfig: Display: Loading IOS ini files took 0.07 seconds
231:LogConfig: Display: Loading TVOS ini files took 0.07 seconds
232:LogConfig: Display: Loading Linux ini files took 0.07 seconds
233:LogConfig: Display: Loading VisionOS ini files took 0.04 seconds
234:LogConfig: Display: Loading Wasm ini files took 0.04 seconds
322:LogWorldPartition: Display: FWorldPartitionClassDescRegistry::Initialize took 7.921 ms
412:LogCook: Display: Sandbox cleanup took 0.014 seconds for platforms Windows
456:LogCook: Display: Cooked packages 0 Packages Remain 1395 Total 1395
457:LogCook: Display: Cook Diagnostics: OpenFileHandles=278, VirtualMemory=1863MiB, VirtualMemoryAvailable=20055MiB
506:LogCook: Display: Cooked packages 95 Packages Remain 1378 Total 1473
525:LogCook: Display: Cooked packages 378 Packages Remain 1095 Total 1473
529:LogCook: Display: Cooked packages 513 Packages Remain 960 Total 1473
591:LogCook: Display: Cooked packages 894 Packages Remain 579 Total 1473
597:LogCook: Display: Cooked packages 1469 Packages Remain 4 Total 1473
601:LogCook: Display: Cooked packages
[... 1236 more characters not shown]
```

**Mon 16 Nov 00:35:45 · Tool call: Bash** (Check package log errors, warnings, prereqs, end)

```
P=/d/UE/ship1_farmlogs/package-shipping/package_ship_run.log; grep -n -i "error" $P | grep -v -i "errors: 0\|0 error\|ErrorCode=0\|bError\|LogHttp\|-error" | cut -c1-220 | head; grep -c ": Warning:" $P; grep -n ": Warning:" $P | cut -c1-200 | sed 's/^\([0-9]*\):.*\(Log[A-Za-z]*\): Warning:/\1 \2/' | awk '{print $2}' | sort | uniq -c; grep -n -i "AppLocal\|prereq\|vc_redist" $P | cut -c1-200; sed -n 1190,1228p $P | cut -c1-200
```

Result:

```
1
      1 LogCore
4:Parsing command line: BuildCookRun -nop4 -utf8output -unattended -nocompileuat -cook -build -project=C:\UE\Farm\ship1\Tools\..\Supercut.uproject -unrealexe=C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealE
961:Copying AppLocal dependencies from C:\UE\UE_5.9\Engine\Binaries\ThirdParty\AppLocalDependencies\Win64\x64 to Supercut/Binaries/Win64
LogIoStore: Display:     Supercut-Windows              37            1466               0
LogIoStore: Display: --------------------------------------------------------------------
LogIoStore: Display:                Total              37            1466               0
LogIoStore: Display:
LogIoStore: Display:
LogIoStore: Display: Input:      1466 Packages
LogIoStore: Display: Input:         0   B UExp
LogIoStore: Display: Input:    227.89 MiB UAsset
LogIoStore: Display: Input:    418.30 MiB UBulk
LogIoStore: Display: Input:     68.95 MiB for 1043 Global shaders
LogIoStore: Display: Input:      1.77 MiB for 206 Shared shaders
LogIoStore: Display: Input:         0   B for 0 Unique shaders
LogIoStore: Display: Input:     10.68 MiB for 237 Inline shaders
LogIoStore: Display:
LogIoStore: Display: Output:     1531 Imported package entries
LogIoStore: Display: Output:      854 Packages without imports
LogIoStore: Display: Output:        0 Public runtime script objects
LogIoStore: Display: Output:     3.32 MiB InitialLoadData
LogIoStore: Display:
LogIoStore: Display: Success
LogPakFile: Display: UnrealPak executed in 3.588744 seconds
Took 3.83s to run UnrealPak.exe, ExitCode=0
DumpManifest: C:\Users\USER\AppData\Roaming\Unreal Engine\AutomationTool\Logs\C+UE+UE_5.9\FinalCopyWin64_UFSFiles.txt, NumItems: 4083
DumpManifest: C:\Users\USER\AppData\Roaming\Unreal Engine\AutomationTool\Logs\C+UE+UE_5.9\FinalCopyWin64_NonUFSFiles.txt, NumItems: 822
DumpManifest: C:\Users\USER\AppData\Roaming\Unreal Engine\AutomationTool\Logs\C+UE+UE_5.9\FinalCopyWin64_NonUFSFilesDebug.txt, NumItems: 3
Copying NonUFSFiles to staging directory: C:\UE\Farm\ship1\Saved\StagedBuilds\Windows
Stage command time: 37.22 s
********** STAGE COMMAND COMPLETED **********
********** PACKAGE COMMAND STARTED **********
Package command time: 0.00 s
********** PACKAGE COMMAND COMPLETED **********
********** ARCHIVE COMMAND STARTED **********
Archiving to C:\UE\Farm\_builds\ship1\Supercut59_ship
Archive command time: 0.79 s
********** ARCHIVE COMMAND COMPLETED **********
BuildCookRun time: 436.18 s
BUILD SUCCESSFUL
AutomationTool executed for 0h 7m 17s
Aut
[... 45 more characters not shown]
```

### Mon 16 Nov 00:35:55 · Agent (claude-opus-5-5)

Package passed: `BUILD SUCCESSFUL`, exit 0, 0 errors, 0 `Failed to compile Material`. Now measuring the package folder on pc2 (sizes, largest files, .pdb, runtime DLLs and the exe's dependencies).

**Mon 16 Nov 00:36:00 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\measure.ps1",
 "content": "# ship1: measure the Shipping package folder. Read only. Prints no user or computer names.\nparam([string]$Dir = 'C:\\UE\\Farm\\_builds\\ship1\\Supercut59_ship\\Windows')\n$files = Get-ChildItem $Dir -Recurse -File\n$total = ($files | Measure-Object Length -Sum).Sum\n\"TOTAL bytes=$total files=$($files.Count)\"\n\"TOP10\"\n$files | Sort-Object Length -Descending | Select-Object -First 10 | ForEach-Object { \"  $($_.Length) $($_.FullName.Substring($Dir.Length))\" }\n\"PDB\"\n$p = @($files | Where-Object Extension -eq '.pdb'); if ($p.Count -eq 0) { '  none' } else { $p | ForEach-Object { \"  $($_.Length) $($_.FullName.Substring($Dir.Length))\" } }\n\"EXE_DLL (every .exe, .dll, .msi, .bat)\"\n$files | Where-Object { $_.Extension -in '.exe', '.dll', '.msi', '.bat' } | Sort-Object FullName | ForEach-Object { \"  $($_.Length) $($_.FullName.Substring($Dir.Length))\" }\n\"TOPLEVEL\"\nGet-ChildItem $Dir | ForEach-Object { \"  $($_.Name)\" }\n\"DEPENDENTS\"\n$db = Get-ChildItem 'C:\\Program Files (x86)\\Microsoft Visual Studio', 'C:\\Program Files\\Microsoft Visual Studio' -Recurse -Filter dumpbin.exe -ErrorAction SilentlyContinue | Where-Object FullName -like '*Hostx64\\x64*' | Select-Object -First 1\nif (-not $db) { '  no dumpbin found' } else {\n    foreach ($e in @(\"$Dir\\Supercut.exe\", \"$Dir\\Supercut\\Binaries\\Win64\\Supercut-Win64-Shipping.exe\")) {\n        \"  == $($e.Substring($Dir.Length))\"\n        & $db.FullName /nologo /dependents $e | Where-Object { $_ -match '\\.dll' } | ForEach-Object { \"    $($_.Trim())\" }\n    }\n}\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\measure.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:36:03 · Tool call: Bash** (Measure the Shipping package on pc2)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/measure.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\measure.ps1' | tee "[notes]/unreal/megajam-2026/lanes/ship1/measure.txt"
```

Result:

```
TOTAL bytes=854824624 files=827
TOP10
  500986480 \Supercut\Content\Paks\Supercut-Windows.ucas
  175716352 \Supercut\Binaries\Win64\Supercut-Win64-Shipping.exe
  58956912 \Supercut\Plugins\DLSS\Binaries\ThirdParty\Win64\nvngx_dlss.dll
  18538488 \Supercut\Binaries\Win64\DML\x64\DirectML.dll
  17339384 \Engine\Plugins\NNE\NNERuntimeORT\Binaries\ThirdParty\Onnxruntime\Win64\onnxruntime.dll
  16648304 \Supercut\Audio\music\wav\mx_strings.wav
  16648304 \Supercut\Audio\music\wav\mx_arcade.wav
  11505830 \Supercut\Content\Paks\Supercut-Windows.pak
  5799016 \Engine\Binaries\ThirdParty\NVIDIA\NVaftermath\Win64\GFSDK_Aftermath_Lib.x64.dll
  5034768 \Supercut\Binaries\Win64\D3D12\x64\D3D12Core.dll
PDB
  none
EXE_DLL (every .exe, .dll, .msi, .bat)
  2232688 \Engine\Binaries\ThirdParty\DbgHelp\dbghelp.dll
  2547080 \Engine\Binaries\ThirdParty\MsQuic\v220\win64\msquic.dll
  5799016 \Engine\Binaries\ThirdParty\NVIDIA\NVaftermath\Win64\GFSDK_Aftermath_Lib.x64.dll
  59832 \Engine\Binaries\ThirdParty\Ogg\Win64\VS2015\libogg_64.dll
  1724856 \Engine\Binaries\ThirdParty\Vorbis\Win64\VS2015\libvorbis_64.dll
  48568 \Engine\Binaries\ThirdParty\Vorbis\Win64\VS2015\libvorbisfile_64.dll
  858144 \Engine\Binaries\ThirdParty\Windows\XAudio2_9\x64\xaudio2_9redist.dll
  17339384 \Engine\Plugins\NNE\NNERuntimeORT\Binaries\ThirdParty\Onnxruntime\Win64\onnxruntime.dll
  174080 \Supercut.exe
  32848 \Supercut\Binaries\Win64\api-ms-win-core-console-l1-1-0.dll
  32848 \Supercut\Binaries\Win64\api-ms-win-core-console-l1-2-0.dll
  32824 \Supercut\Binaries\Win64\api-ms-win-core-datetime-l1-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-debug-l1-1-0.dll
  32848 \Supercut\Binaries\Win64\api-ms-win-core-errorhandling-l1-1-0.dll
  32848 \Supercut\Binaries\Win64\api-ms-win-core-fibers-l1-1-0.dll
  36944 \Supercut\Binaries\Win64\api-ms-win-core-file-l1-1-0.dll
  32824 \Supercut\Binaries\Win64\api-ms-win-core-file-l1-2-0.dll
  32824 \Supercut\Binaries\Win64\api-ms-win-core-file-l2-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-handle-l1-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-heap-l1-1-0.dll
  32824 \Supercut\Binaries\Win64\api-ms-win-core-interlocked-l1-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-libraryloader-l1-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-localization-l1-2-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-memory-l1-1-0.dll
  32840 \Supercut\Binaries\Win64\api-ms-win-core-na
[... 4494 more characters not shown]
```

**Mon 16 Nov 00:36:20 · Tool call: Bash** (Split hard vs delay-load imports, list loose content folders)

```
ssh pc2 'powershell -NoProfile -Command "$db = Get-ChildItem ''C:\Program Files (x86)\Microsoft Visual Studio'',''C:\Program Files\Microsoft Visual Studio'' -Recurse -Filter dumpbin.exe -ErrorAction SilentlyContinue | Where-Object FullName -like ''*Hostx64\x64*'' | Select-Object -First 1; & $db.FullName /nologo /dependents C:\UE\Farm\_builds\ship1\Supercut59_ship\Windows\Supercut\Binaries\Win64\Supercut-Win64-Shipping.exe | Select-String ''dependencies|\.dll'' | ForEach-Object { $_.Line.Trim() }; $d=''C:\UE\Farm\_builds\ship1\Supercut59_ship\Windows\Supercut''; Get-ChildItem $d -Directory | ForEach-Object { $f=Get-ChildItem $_.FullName -Recurse -File; ''DIR '' + $_.Name + '' files='' + $f.Count + '' bytes='' + ($f | Measure-Object Length -Sum).Sum }; Get-ChildItem $d\Audio -Recurse -File | Group-Object Extension | ForEach-Object { ''AUDIO '' + $_.Name + '' '' + $_.Count + '' '' + ($_.Group | Measure-Object Length -Sum).Sum }; Get-ChildItem C:\UE\Farm\ship1\Binaries\Win64 -Filter *Shipping*.pdb | ForEach-Object { ''MIRROR_PDB '' + $_.Name + '' '' + $_.Length }"' | grep -v "^\s*$" | sed -n '1,200p' | grep -n "dependencies\|MF\|XAudio2_9\|DIR \|AUDIO \|MIRROR_PDB"
```

Result:

```
<persisted-output>
Output too large (48.6KB). Full output saved to: [agent-config]\ea92763d-b91e-4163-8658-22436987d5b9\tool-results\bfp9ec2o2.txt

Preview (first 2KB):
x86 : The term 'x86' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the 
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:39
+ $db = Get-ChildItem C:\Program Files (x86)\Microsoft Visual Studio,C: ...
+                                       ~~~
    + CategoryInfo          : ObjectNotFound: (x86:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
The expression after '&' in a pipeline element produced an object that was not valid. It must result in a command 
name, a script block, or a CommandInfo object.
At line:1 char:240
+ ...  -like *Hostx64\x64* | Select-Object -First 1; & $db.FullName /nologo ...
+                                                      ~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException
    + FullyQualifiedErrorId : BadExpression
 
Get-ChildItem : A positional parameter cannot be found that accepts argument '+'.
At line:1 char:600
+ ... urse -File; DIR  + $_.Name +  files= + $f.Count +  bytes= + ($f | Mea ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-ChildItem], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand
 
Get-ChildItem : A positional parameter cannot be found that accepts argument '+'.
At line:1 char:600
+ ... urse -File; DIR  + $_.Name +  files= + $f.Count +  bytes= + ($f | Mea ...
+                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-ChildItem], ParameterBindingException
    + FullyQualifiedErrorId : PositionalParameterNotFound,Microsoft.PowerShell.Commands.GetChildItemCommand
 
Get-ChildItem : A positional parameter cannot be found that accepts argument '+'.
...
</persisted-output>
```

### Mon 16 Nov 00:39:17 · Agent (claude-opus-5-5)

Quoting broke over ssh. Moving it into a script file instead.

**Mon 16 Nov 00:39:22 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\measure2.ps1",
 "content": "# ship1: hard vs delay-load imports of the Shipping exe, loose content folders, the pdb left in the mirror. Read only.\n$pkg = 'C:\\UE\\Farm\\_builds\\ship1\\Supercut59_ship\\Windows'\n$db = Get-ChildItem 'C:\\Program Files (x86)\\Microsoft Visual Studio', 'C:\\Program Files\\Microsoft Visual Studio' -Recurse -Filter dumpbin.exe -ErrorAction SilentlyContinue | Where-Object FullName -like '*Hostx64\\x64*' | Select-Object -First 1\n& $db.FullName /nologo /dependents \"$pkg\\Supercut\\Binaries\\Win64\\Supercut-Win64-Shipping.exe\" | ForEach-Object { $_.Trim() } | Where-Object { $_ -match 'dependencies|\\.dll$' } | ForEach-Object { \"IMP $_\" }\nGet-ChildItem \"$pkg\\Supercut\" -Directory | ForEach-Object {\n    $f = @(Get-ChildItem $_.FullName -Recurse -File)\n    \"DIR Supercut\\$($_.Name) files=$($f.Count) bytes=$(($f | Measure-Object Length -Sum).Sum)\"\n}\nGet-ChildItem \"$pkg\\Supercut\\Audio\" -Recurse -File | Group-Object Extension | ForEach-Object { \"AUDIO $($_.Name) count=$($_.Count) bytes=$(($_.Group | Measure-Object Length -Sum).Sum)\" }\nGet-ChildItem \"$pkg\\Supercut\\Audio\" -Recurse -Directory | ForEach-Object { \"AUDIODIR $($_.FullName.Substring($pkg.Length))\" }\nGet-ChildItem 'C:\\UE\\Farm\\ship1\\Binaries\\Win64' -Filter '*Shipping*' | ForEach-Object { \"MIRROR_BIN $($_.Name) $($_.Length)\" }\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\measure2.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:39:25 · Tool call: Bash** (Run second measure script on pc2)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/measure2.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\measure2.ps1' | tee "[notes]/unreal/megajam-2026/lanes/ship1/measure2.txt" | grep -v "IMP api-ms"
```

Result:

```
IMP Image has the following dependencies:
IMP dxgi.dll
IMP DSOUND.dll
IMP WS2_32.dll
IMP WINMM.dll
IMP KERNEL32.dll
IMP USER32.dll
IMP GDI32.dll
IMP ADVAPI32.dll
IMP SHELL32.dll
IMP ole32.dll
IMP OLEAUT32.dll
IMP IPHLPAPI.DLL
IMP SETUPAPI.dll
IMP dwmapi.dll
IMP IMM32.dll
IMP CRYPT32.dll
IMP UIAutomationCore.DLL
IMP WINHTTP.dll
IMP OPENGL32.dll
IMP MSVCP140.dll
IMP VERSION.dll
IMP tbs.dll
IMP bcrypt.dll
IMP UxTheme.dll
IMP VCRUNTIME140.dll
IMP VCRUNTIME140_1.dll
IMP Image has the following delay load dependencies:
IMP d3d11.dll
IMP d3d12.dll
IMP XINPUT1_4.dll
IMP libvorbis_64.dll
IMP libvorbisfile_64.dll
IMP GFSDK_Aftermath_Lib.x64.dll
IMP DirectML.dll
IMP dbghelp.dll
IMP MFPlat.DLL
IMP XAudio2_9.dll
IMP MFReadWrite.dll
IMP SHLWAPI.dll
IMP MF.dll
DIR Supercut\Audio files=2 bytes=33296608
DIR Supercut\Binaries files=62 bytes=209914688
DIR Supercut\Content files=749 bytes=521612760
DIR Supercut\Plugins files=1 bytes=58956912
AUDIO .wav count=2 bytes=33296608
AUDIODIR \Supercut\Audio\music
AUDIODIR \Supercut\Audio\music\wav
MIRROR_BIN Supercut-Win64-Shipping.exe 175716352
MIRROR_BIN Supercut-Win64-Shipping.exp 66700
MIRROR_BIN Supercut-Win64-Shipping.lib 114696
MIRROR_BIN Supercut-Win64-Shipping.pdb 257544192
MIRROR_BIN Supercut-Win64-Shipping.target 115288
```

**Mon 16 Nov 00:39:32 · Tool call: Bash** (Find why music wavs ship as loose files)

```
cd /d/UE/wt/maincheck_x; git grep -n -i "music/wav\|music\\\\\\\\wav\|mx_strings\|mx_arcade" -- Source Config Tools/*.cmd | head; git ls-files | grep -i "mx_strings\|mx_arcade" | head; grep -n -i "RuntimeDependencies\|NonUFS" Source/Supercut/Supercut.Build.cs
```

Result:

```
Source/Supercut/Supercut.Build.cs:13:		foreach (string Name in new string[] { "mx_arcade", "mx_strings" })
Source/Supercut/Supercut.Build.cs:15:			RuntimeDependencies.Add("$(ProjectDir)/Audio/music/wav/" + Name + ".wav", StagedFileType.NonUFS);
Source/Supercut/SupercutMusic.cpp:23:		const FString Path = FPaths::ProjectDir() / TEXT("Audio/music/wav") / FileName;
Source/Supercut/SupercutMusic.cpp:83:		MusicLoadWav(TEXT("mx_arcade.wav"), FSupercutMusicMixer::LoopFrames, Tracks->Arcade);
Source/Supercut/SupercutMusic.cpp:84:		MusicLoadWav(TEXT("mx_strings.wav"), FSupercutMusicMixer::LoopFrames, Tracks->Strings);
Source/Supercut/SupercutMusic.cpp:86:		UE_LOG(LogSupercut, Display, TEXT("MUSIC read 2 files of %lld frames from %s"), FSupercutMusicMixer::LoopFrames, *(FPaths::ProjectDir() / TEXT("Audio/music/wav")));
Source/Supercut/SupercutMusic.cpp:94:// (Audio/music/wav/measurements.md before lane music2; lanes/mix1/HANDOFF.md). The arcade song is -12.75 LUFS, so
Source/Supercut/SupercutMusic.h:15: * The songs are 48 kHz 16-bit stereo WAV files in Audio/music/wav, read from disk at run time (the build stages
Source/Supercut/SupercutMusic.h:40:	/** Reads the files from Audio/music/wav under the project folder. A missing or odd file stops the game with its name. */
Audio/music/wav/mx_arcade.wav
Audio/music/wav/mx_strings.wav
15:			RuntimeDependencies.Add("$(ProjectDir)/Audio/music/wav/" + Name + ".wav", StagedFileType.NonUFS);
18:		RuntimeDependencies.Add("$(ProjectDir)/Content/Props/catalogue.txt", StagedFileType.NonUFS);
Shell cwd was reset to [notes]
```

**Mon 16 Nov 00:39:41 · Tool call: Bash** (Back up pc2 Supercut settings folder)

```
date "+%d %b %H:%M:%S"; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\appdata.ps1 -Mode backup' | tee /d/UE/ship1_farmlogs/appdata_backup.txt
```

Result:

```
16 Nov 00:39:42
BAK \Saved\Config\CrashReportClient\UECC-Windows-1C547C3841C4675998E366BAC55A27D3\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\CrashReportClient\UECC-Windows-2818CCBD4EE58FC16BDF909119830C1B\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\CrashReportClient\UECC-Windows-3FB9F4814BCBF415EE87818563806BE0\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\CrashReportClient\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\CrashReportClient\UECC-Windows-9972FFF54AA6D331FE11F8A59045AD88\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\CrashReportClient\UECC-Windows-F96CE6124C1473806CBE07846138D9FD\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Config\Windows\GameUserSettings.ini 2244 C43957121298
BAK \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\CrashContext.runtime-xml 29621 3C0E6EC02E29
BAK \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\CrashReportClient.ini 239 CE69D7E7BBD1
BAK \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\UEMinidump.dmp 606088 766E73088BF7
BAK \Saved\Supercut_PCD3D_SM6.upipelinecache 34800 3338B04C5FA8
```

**Mon 16 Nov 00:39:54 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\crashinfo.ps1",
 "content": "# ship1: print the safe fields of each crash report under %LOCALAPPDATA%\\Supercut\\Saved\\Crashes. Read only.\n# Skips every field that can hold a user, computer or account name.\n$root = Join-Path $env:LOCALAPPDATA 'Supercut\\Saved\\Crashes'\nGet-ChildItem $root -Directory | ForEach-Object {\n    \"== $($_.Name) written $($_.LastWriteTime.ToString('dd MMM HH:mm:ss'))\"\n    $x = [xml](Get-Content (Join-Path $_.FullName 'CrashContext.runtime-xml') -Raw)\n    $p = $x.FGenericCrashContext.RuntimeProperties\n    foreach ($k in 'CrashType', 'ExecutableName', 'GameName', 'BuildConfiguration', 'BuildVersion', 'EngineVersion', 'IsEnsure', 'IsAssert', 'SecondsSinceStart', 'ProcessId', 'CrashReporterMessage') {\n        \"  $k = $($p.$k)\"\n    }\n    \"  ErrorMessage = $(($p.ErrorMessage -replace '[A-Za-z]:\\\\Users\\\\[^\\\\]+', '%USERPROFILE%'))\"\n    \"  CommandLine = $(($p.CommandLine -replace '[A-Za-z]:\\\\Users\\\\[^\\\\]+', '%USERPROFILE%'))\"\n    \"  CallStack (first 12 lines):\"\n    ($p.CallStack -split \"`n\" | Select-Object -First 12) | ForEach-Object { \"    $(($_ -replace '[A-Za-z]:\\\\Users\\\\[^\\\\]+', '%USERPROFILE%').Trim())\" }\n}\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\crashinfo.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:39:57 · Tool call: Bash** (Read safe fields of the pc2 crash report)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/crashinfo.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\crashinfo.ps1'
```

Result:

```
== UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000 written 16 Nov 00:36:23
  CrashType = Assert
  ExecutableName = Supercut-Win64-Shipping
  GameName = UE-Supercut
  BuildConfiguration = Shipping
  BuildVersion = ++UE5+Release-5.9-CL-60351404
  EngineVersion = 5.9.0-60351404+++UE5+Release-5.9
  IsEnsure = false
  IsAssert = true
  SecondsSinceStart = 0
  ProcessId = 2176
  CrashReporterMessage =  Attended
  ErrorMessage = LowLevelFatalError [File:D:\build\++UE5\Sync\Engine\Source\Runtime\D3D12RHI\Private\D3D12Util.cpp] [Line: 1062] 
hr failed 
 at D:\build\++UE5\Sync\Engine\Source\Runtime\D3D12RHI\Private\Windows\WindowsD3D12Viewport.cpp:162 
 with error DXGI_ERROR_NOT_CURRENTLY_AVAILABLE




  CommandLine =  Supercut
  CallStack (first 12 lines):
```

**Mon 16 Nov 00:40:22 · Tool call: Bash** (Check slots, running Unreal processes and recent farm folders on pc2)

```
cd "[notes]/unreal/megajam-2026/farm"; ./farm.sh slots; ssh pc2 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -like ''Supercut*'' -or $_.Name -like ''Unreal*'' -or $_.Name -like ''dotnet*'' } | ForEach-Object { $_.Name + '' '' + $_.ProcessId + '' '' + $_.CreationDate.ToString(''HH:mm:ss'') + '' '' + ($_.ExecutablePath -replace ''Users\\[^\\]+'',''Users\USER'') }; Get-ChildItem C:\UE\Farm\_builds -Directory | ForEach-Object { Get-ChildItem $_.FullName -Directory | Where-Object Name -like ''*ship*'' | ForEach-Object { $_.FullName + '' '' + $_.LastWriteTime.ToString(''dd MMM HH:mm'') } }; Get-ChildItem C:\UE\Farm\_out -Directory | Sort-Object LastWriteTime | Select-Object -Last 6 | ForEach-Object { $_.Name + '' '' + $_.LastWriteTime.ToString(''dd MMM HH:mm'') }"'
```

Result:

```
Exit code 1
[pc-b]: CLOSED: [pc-b]'s drive is stalling (NVMe resets, 15 Nov 14:19); no farm work on it for the rest of the jam
[pc-b]: 0 of 2 slot(s) held
pc2: 0 of 1 slot(s) held
[pc-c]: clap3 run since 00:38:47 (1 min, running)
[pc-c]: hud2 package since 00:37:06 (3 min, running)
[pc-c]: 2 of 3 slot(s) held
c4: CLOSED: c4 runs no compile, package, editor or game step until the final judges build: its D: drive dropped twice under that load (15 Nov 19:28 and 21:01). Use [pc-c] (or pc2). Main thread, 15 Nov 21:28
c4: 0 of 2 slot(s) held
At line:1 char:61
+ Get-CimInstance Win32_Process | Where-Object { $_.Name -like Supercut ...
+                                                             ~
You must provide a value expression following the '-like' operator.
At line:1 char:62
+ ... stance Win32_Process | Where-Object { $_.Name -like Supercut* -or $_. ...
+                                                         ~~~~~~~~~
Unexpected token 'Supercut*' in expression or statement.
At line:1 char:203
+ ...  { $_.Name +   + $_.ProcessId +   + $_.CreationDate.ToString(HH:mm:ss ...
+                                                                  ~
Missing ')' in method call.
At line:1 char:203
+ ... me +   + $_.ProcessId +   + $_.CreationDate.ToString(HH:mm:ss) +   +  ...
+                                                          ~~~~~~~~
Unexpected token 'HH:mm:ss' in expression or statement.
At line:1 char:143
+ ...  -like Unreal* -or $_.Name -like dotnet* } | ForEach-Object { $_.Name ...
+                                                                 ~
Missing closing '}' in statement block or type definition.
At line:1 char:211
+ ... e +   + $_.ProcessId +   + $_.CreationDate.ToString(HH:mm:ss) +   + ( ...
+                                                                 ~
Unexpected token ')' in expression or statement.
At line:1 char:246
+ ... tionDate.ToString(HH:mm:ss) +   + ($_.ExecutablePath -replace Users\[ ...
+                                                                  ~
You must provide a value expression following the '-replace' operator.
At line:1 char:247
+ ... tring(HH:mm:ss) +   + ($_.ExecutablePath -replace Users\[^\]+,Users\U ...
+                                                       ~~~~~~~~~~~
Unexpected token 'Users\[^\]+' in expression or statement.
At line:1 char:246
+ ... tionDate.ToString(HH:mm:ss) +   + ($_.ExecutablePath -replace Users\[ ...
+                                                         
[... 476 more characters not shown]
```

**Mon 16 Nov 00:40:32 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\procs.ps1",
 "content": "# ship1: who else is using Unreal on this PC. Read only. Masks the user folder.\nGet-CimInstance Win32_Process | Where-Object { $_.Name -like 'Supercut*' -or $_.Name -like 'Unreal*' -or $_.Name -like 'ShaderCompileWorker*' } | ForEach-Object {\n    \"PROC $($_.Name) pid=$($_.ProcessId) parent=$($_.ParentProcessId) started=$($_.CreationDate.ToString('HH:mm:ss')) $($_.ExecutablePath -replace 'Users\\\\[^\\\\]+', 'Users\\USER')\"\n}\nGet-ChildItem 'C:\\UE\\Farm\\_builds' -Directory | ForEach-Object {\n    Get-ChildItem $_.FullName -Directory | ForEach-Object { \"BUILD $($_.FullName) $($_.LastWriteTime.ToString('dd MMM HH:mm'))\" }\n}\nGet-ChildItem 'C:\\UE\\Farm\\_out' -Directory | Sort-Object LastWriteTime | Select-Object -Last 6 | ForEach-Object { \"OUT $($_.Name) $($_.LastWriteTime.ToString('dd MMM HH:mm'))\" }\n# Application event log: Supercut starts and crashes in the last hour (Windows Error Reporting and app errors).\nGet-WinEvent -FilterHashtable @{ LogName = 'Application'; StartTime = (Get-Date).AddMinutes(-60) } -ErrorAction SilentlyContinue |\n    Where-Object { $_.Message -like '*Supercut*' } | Select-Object -First 10 | ForEach-Object {\n        \"EVT $($_.TimeCreated.ToString('HH:mm:ss')) id=$($_.Id) $($_.ProviderName) $((($_.Message -split \"`n\")[0..3] -join ' | ') -replace 'Users\\\\[^\\\\]+', 'Users\\USER')\"\n    }\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\procs.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:40:35 · Tool call: Bash** (List Unreal processes, builds and recent crash events on pc2)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/procs.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\procs.ps1' | cut -c1-300
```

Result:

```
BUILD C:\UE\Farm\_builds\gruntai1\Supercut59 15 Nov 21:51
BUILD C:\UE\Farm\_builds\perf3\Supercut59 15 Nov 11:17
BUILD C:\UE\Farm\_builds\set2\Supercut59 15 Nov 12:13
BUILD C:\UE\Farm\_builds\sfx5\Supercut59 15 Nov 13:12
BUILD C:\UE\Farm\_builds\ship1\Supercut59_ship 16 Nov 00:34
BUILD C:\UE\Farm\_builds\submit1\ports 15 Nov 13:36
BUILD C:\UE\Farm\_builds\submit1\tools 15 Nov 12:38
OUT gunfix1 15 Nov 13:13
OUT sfx5 15 Nov 13:35
OUT hands2 15 Nov 13:54
OUT gruntai1 15 Nov 23:25
OUT ship1 16 Nov 00:24
OUT ship1_tools 16 Nov 00:40
```

**Mon 16 Nov 00:40:43 · Tool call: Bash** (Check timestamps of my measure files)

```
cd "[notes]/unreal/megajam-2026/lanes/ship1"; for f in measure.txt measure2.txt scripts/measure.ps1; do echo "$f $(date -r $f +%H:%M:%S)"; done; date -r /d/UE/ship1_farmlogs/package-shipping/package_ship_run.log +%H:%M:%S
```

Result:

```
measure.txt 00:36:05
measure2.txt 00:39:27
scripts/measure.ps1 00:36:00
00:35:11
```

**Mon 16 Nov 00:41:06 · Tool call: Bash** (Log package result and the stray launch)

```
cat >> "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md" <<'EOF'
- 00:35 Shipping package done: farm exit 0, 438 s (00:27:44 to 00:35:11). `package_ship_run.log`: `BUILD SUCCESSFUL`,
  `AutomationTool exiting with ExitCode=0`, 0 `Failed to compile Material`, 0 `missing usage flag`, no compile error.
  Shipping game target 124 actions, every one `[NoUba]`, `Result: Succeeded`, UBT 319 s at one job. Cook 1473
  packages, 77.9 s. Stage 37.2 s. Warnings: the Fab plugin dependency line and `LogCore: Warning: UTS: Timed out
  waiting for the Unreal Trace Server process to start` (cook side, harmless). `ubt_package_ship.log` did not come
  back (farm Keep found no file at that path); the package log holds the full compile list.
- 00:36 Measured the package (`measure.txt`, `measure2.txt`): 854,824,624 bytes, 827 files, no `.pdb` (the exe's
  257,544,192-byte pdb stays in the mirror's `Binaries\Win64`). VC runtime and UCRT DLLs are copied beside the game
  exe (log line 961, "Copying AppLocal dependencies"); no `vc_redist` or prereq installer is staged.
- 00:36 MY MISTAKE: an inline ssh command lost its '' quotes on pc2 (the ssh shell is cmd), and PowerShell ran
  `$d=C:\UE\Farm\_builds\ship1\Supercut59_ship\Windows\Supercut` as a command: it started `Supercut.exe` with no
  arguments in the ssh session. It died at second 0 (assert, `DXGI_ERROR_NOT_CURRENTLY_AVAILABLE`,
  WindowsD3D12Viewport.cpp:162, the known no-desktop failure) and left crash folders `UECC-Windows-8B89ED0C...` in
  pc2's `%LOCALAPPDATA%\Supercut`. No process left, nothing on the desktop. From here every remote command is a
  .ps1 file in `scripts/`, never inline. The crash's folders get deleted after the restore.
- 00:39 `appdata.ps1 backup` done (`/d/UE/ship1_farmlogs/appdata_backup.txt`); the backup includes my crash folders.
EOF
```

Result:

```
(Bash completed with no output)
```

**Mon 16 Nov 00:41:07 · Tool call: Bash** (Watch Supercut listeners on pc2 during the run)

```
ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\listen.ps1 -Seconds 1200'; echo "listen exit $?"
```

Result:

```
Command running in background with ID: b7ajx66lv. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\b7ajx66lv.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**Mon 16 Nov 00:41:11 · Tool call: Bash** (Run main8 scripted run on the Shipping package on pc2)

```
cd "[notes]/unreal/megajam-2026/farm"; date "+%d %b %H:%M:%S"; time ./farm.sh run pc2 ship1 /d/UE/ship1_farmlogs -Shipping -Run main8 -Seed 1 -Script '{P}\Script\main8.txt' -FixedFps 240 -Silent -TimeoutSeconds 900 > /d/UE/ship1_farmlogs/run.out 2>&1; echo "exit $?"; date "+%d %b %H:%M:%S"; tail -5 /d/UE/ship1_farmlogs/run.out
```

Result:

```
Command running in background with ID: bkg2bg8ws. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bkg2bg8ws.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\lanes\ship1; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Mon 16 Nov 00:41:11 · Tool call: mcp__t3-code__t3_background_wait**

```
{
 "taskIds": [
  "b7ajx66lv"
 ]
}
```

Result:

```
{"matched":["b7ajx66lv"],"unmatched":[]}
```

**Mon 16 Nov 00:41:13 · Tool call: mcp__t3-code__t3_background_wait**

```
{
 "taskIds": [
  "bkg2bg8ws"
 ]
}
```

Result:

```
{"matched":["bkg2bg8ws"],"unmatched":[]}
```

**Mon 16 Nov 00:41:16 · Tool call: Bash** (Check run start and listener output)

```
sleep 45; cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bkg2bg8ws.output"; ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\_out\ship1\listen.txt -Tail 3; Get-Content C:\UE\Farm\_out\ship1\run\run.log -Tail 3"' 2>&1 | cut -c1-250
```

Result:

```
<tool_use_error>Blocked: sleep 45 followed by: cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bkg2bg8ws.output" ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\_out\ship1\listen.txt -Tail 3; Get-Content C:\UE\Farm\_out\ship1\run\run.log -Tail 3"' cut -c1-250. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```

**Mon 16 Nov 00:41:19 · Tool call: Bash** (Check run start and listener output)

```
cat "C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bkg2bg8ws.output"; ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\_out\ship1\listen.txt -Tail 3; Get-Content C:\UE\Farm\_out\ship1\run\run.log -Tail 3"' 2>&1 | cut -c1-250
```

Result:

```
16 Nov 00:41:11
00:41:14 Supercut-Win64-Shipping pid=14248 tcp_listen=[] udp=[]
00:41:20 Supercut pid=23320 tcp_listen=[] udp=[]
00:41:20 Supercut-Win64-Shipping pid=14248 tcp_listen=[] udp=[]
Get-Content : The process cannot access the file 'C:\UE\Farm\_out\ship1\run\run.log' because it is being used by 
another process.
At line:1 char:55
+ ... en.txt -Tail 3; Get-Content C:\UE\Farm\_out\ship1\run\run.log -Tail 3
+                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ReadError: (C:\UE\Farm\_out\ship1\run\run.log:String) [Get-Content], IOException
    + FullyQualifiedErrorId : GetContentReaderIOError,Microsoft.PowerShell.Commands.GetContentCommand
```

**Mon 16 Nov 00:41:25 · Tool call: Bash** (Find where RUN wrapped line is written)

```
cd /d/UE/wt/maincheck_x; git grep -n "SupercutTrace\|SupercutShots\|SupercutFps\|SupercutScript" -- Source/Supercut/SupercutPlayerController.cpp | head -5; grep -n "RUN wrapped" -r Source/Supercut/*.cpp | head -3; tail -5 Script/main8.txt
```

Result:

```
Source/Supercut/SupercutPlayerController.cpp:85:	if (FParse::Value(FCommandLine::Get(), TEXT("-SupercutScript="), ScriptPath))
Source/Supercut/SupercutPlayerController.cpp:89:	if (FParse::Value(FCommandLine::Get(), TEXT("-SupercutShots="), ShotFolder))
Source/Supercut/SupercutPlayerController.cpp:93:	bCountFps = FParse::Param(FCommandLine::Get(), TEXT("SupercutFps"));
Source/Supercut/SupercutPlayerController.cpp:95:	bTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));
Source/Supercut/SupercutPlayerController.cpp:180:		UE_LOG(LogSupercut, Fatal, TEXT("-SupercutScript: cannot read %s"), *Path);
Source/Supercut/SupercutRun.cpp:387:	UE_LOG(LogSupercut, Display, TEXT("RUN wrapped: takes %d, time %.1f s, shots %d, freezes %d, kills %d, scenes %d"), Take, Stats.Seconds, Stats.Shots, Stats.Freezes, Stats.Kills, ScenesCleared);
0 scene 10 1
0 charges full
0 move 0 0
0.50 shot s10_lap_room
1.00 end
Shell cwd was reset to [notes]
```

**Mon 16 Nov 00:41:30 · Tool call: Bash** (Wait for the Shipping run to finish)

```
O="C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\ea92763d-b91e-4163-8658-22436987d5b9\tasks\bkg2bg8ws.output"; until grep -q "^exit" "$O"; do sleep 15; done; cat "$O"
```

Result:

```
16 Nov 00:41:11

real	6m16.634s
user	0m0.463s
sys	0m1.255s
exit 0
16 Nov 00:47:28
game exit code 0
FARM step=run name=ship1 exit=0 secs=372

[exited with code 0]
```

### Mon 16 Nov 00:47:34 · Brief from the orchestrating agent

GLASSBOX-MEGAJAM-2026 lane=ship1
From the main thread, 16 Nov 00:41. The owner at 00:39: the final build must be ready before 02:00, and it is a Shipping build. I start the Shipping build on the main PC at about 01:00, so I need what you know NOW, not at 01:30. Carry on with the trial after answering.

Send me a short interim report at once (five minutes at most to write it), with facts you have already seen and "not known yet" for the rest:
1. Did package-shipping of ae8614e finish on pc2? Exit code, how long each part took, and any error line.
2. How a scripted run of a Shipping package is proven with no log: which file or output carries the RUN line (the earlier lanes left a main8_shipping.log; say what produced it and the exact command).
3. Where the symbols file lands in a Shipping package (path), and whether any other file there is not needed by the game.
4. Unzipped size of the Shipping package, and the size of its exe, ucas, utoc, pak.
5. Anything a judge's PC needs installed (the prerequisites installer: is it in the package, where, how big).
6. Any code path that behaves differently under UE_BUILD_SHIPPING that a player would notice (list file and line; do not fix).
One more fact for you: Tools/entry_folder.py on main (0e37ce5) now keeps Content/Rooms/rest and leaves out every .pdb. Do not make an entry folder or a zip yourself.

**Mon 16 Nov 00:47:38 · Tool call: Bash** (Get the RUN line from the Shipping run log)

```
ls /d/UE/ship1_farmlogs/run/; grep -n "RUN wrapped\|Fatal\|Error\|missing usage flag" /d/UE/ship1_farmlogs/run/run.log | head; grep -c "missing usage flag" /d/UE/ship1_farmlogs/run/run.log; grep -n "Supercut-Windows.utoc\|Supercut-Windows.pak\|global.utoc\|global.ucas" "[notes]/unreal/megajam-2026/lanes/ship1/measure.txt"
```

Result:

```
console.txt
farm_step.txt
run.log
shots
2189:[2026.11.16-00.47.23:238][201]LogSupercut: Display: RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9
0
10:  11505830 \Supercut\Content\Paks\Supercut-Windows.pak
```

**Mon 16 Nov 00:47:42 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\paks.ps1",
 "content": "# ship1: sizes of every container file in the Shipping package, and the listener log. Read only.\n$pkg = 'C:\\UE\\Farm\\_builds\\ship1\\Supercut59_ship\\Windows'\nGet-ChildItem $pkg -Recurse -File | Where-Object { $_.Extension -in '.pak', '.ucas', '.utoc', '.sig' -or $_.Name -eq 'NOTICES.txt' } | ForEach-Object { \"FILE $($_.Length) $($_.FullName.Substring($pkg.Length))\" }\nGet-Content 'C:\\UE\\Farm\\_out\\ship1\\listen.txt' | ForEach-Object { \"LISTEN $_\" }\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\paks.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:47:46 · Tool call: Bash** (Get container sizes and listener summary)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/paks.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\paks.ps1' > "[notes]/unreal/megajam-2026/lanes/ship1/paks_listen.txt"; grep FILE "[notes]/unreal/megajam-2026/lanes/ship1/paks_listen.txt"; grep LISTEN "[notes]/unreal/megajam-2026/lanes/ship1/paks_listen.txt" | wc -l; grep LISTEN "[notes]/unreal/megajam-2026/lanes/ship1/paks_listen.txt" | grep -v "tcp_listen=\[\] udp=\[\]"
```

Result:

```
FILE 111 \NOTICES.txt
FILE 3483584 \Supercut\Content\Paks\global.ucas
FILE 842 \Supercut\Content\Paks\global.utoc
FILE 11505830 \Supercut\Content\Paks\Supercut-Windows.pak
FILE 500986480 \Supercut\Content\Paks\Supercut-Windows.ucas
FILE 447634 \Supercut\Content\Paks\Supercut-Windows.utoc
146
LISTEN start 00:41:09
LISTEN end 00:47:29 seen=True
```

### Mon 16 Nov 00:48:16 · Agent (claude-opus-5-5)

**Interim report, ship1, 16 Nov 00:49.** Everything below is seen in logs or files, not guessed.

1. **Package-shipping of ae8614e on pc2: yes, it passed.** Farm exit 0, `BUILD SUCCESSFUL`, `AutomationTool exiting with ExitCode=0`. No compile error, 0 `Failed to compile Material`, 0 `missing usage flag`.
   - Times on pc2: mirror 114 s, editor build 168 s (3 C4996 deprecation warnings in test files only), package 438 s in all.
   - Inside the package: the Shipping compile was 124 actions at one job, all `[NoUba]`, `Result: Succeeded`, 319 s. Cook 1473 packages, 78 s. Stage 37 s.
   - The only warnings were the Fab plugin dependency line and `LogCore: Warning: UTS: Timed out waiting for the Unreal Trace Server`.
   - **The scripted Shipping run matched the reference exactly:** `RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9`. Game exit code 0, run step 372 s, 0 `missing usage flag`.

2. **How a Shipping run is proven without an engine log:** the game writes its own log through `-SupercutLog=<file>`.
   - Shipping has `NO_LOGGING`, and `Supercut.h:11-30` redirects the module's `UE_LOG` lines to that file (`Supercut.cpp:18-50`).
   - `Tools\run_demo.ps1 -Shipping` passes `-SupercutLog=<Log>` instead of `-abslog`. The default exe is `D:\UE\Builds\Supercut59_ship\Windows\Supercut.exe`.
   - held1's exact command (its HANDOFF line 145): `powershell -File Tools\run_demo.ps1 -Shipping -Run main8 -Seed 1 -Script "D:\UE\Projects\Supercut59\Script\main8.txt" -FixedFps 240 -Silent -Log <log>`.
   - Mine: `farm.sh run pc2 ship1 <logs> -Shipping -Run main8 -Seed 1 -Script '{P}\Script\main8.txt' -FixedFps 240 -Silent -TimeoutSeconds 900`. The RUN line is at line 2189 of `run/run.log`.
   - Evidence: that line plus run_demo's `game exit code 0`.
   - `-FPS=` is read by the game itself in Shipping (`Supercut.cpp:57-64`).
   - Back up `%LOCALAPPDATA%\Supercut` before the run and restore it after.

3. **Symbols:** the package folder holds no `.pdb`. The UAT staging uses `-nodebuginfo`, and `package_shipping.cmd` also deletes any `*.pdb` it finds. The pdb, 257,544,192 bytes, stays in the project at `Binaries\Win64\Supercut-Win64-Shipping.pdb`, next to `.exp`, `.lib` and `.target` files, none of which are in the package.
   - Files in the package the game may not need: `Engine\Plugins\NNE\...\onnxruntime.dll` (17.3 MB), `Supercut\Binaries\Win64\D3D12\x64\d3d12SDKLayers.dll` (5.0 MB, the D3D debug layer) and `NOTICES.txt` (111 B). The engine stages these itself. I have not tested removing them, so leave them in.

4. **Sizes, unzipped:** 854,824,624 bytes in 827 files.

   | File | Bytes |
   | --- | --- |
   | `Supercut\Binaries\Win64\Supercut-Win64-Shipping.exe` | 175,716,352 |
   | `Supercut.exe` (the launcher) | 174,080 |
   | `Supercut-Windows.ucas` | 500,986,480 |
   | `Supercut-Windows.utoc` | 447,634 |
   | `Supercut-Windows.pak` | 11,505,830 |
   | `global.ucas` | 3,483,584 |
   | `global.utoc` | 842 |
   | `nvngx_dlss.dll` | 58,956,912 |
   | Loose music wavs `mx_arcade.wav` and `mx_strings.wav` (intended, `Supercut.Build.cs:13-15`) | 16,648,304 each |

5. **Prerequisites: no installer is in the package, and none is needed for the VC runtime.**
   - `package_shipping.cmd` passes `-applocaldirectory=...\AppLocalDependencies` and no `-prereqs`. So UAT copies `msvcp140*`, `vcruntime140*`, `ucrtbase` and the `api-ms-win-*` DLLs beside the game exe (package log line 961).
   - It does not stage `vc_redist.x64.exe` (`WinPlatform.Automation.cs:207-214` does that only with `-prereqs`).
   - Every hard import of the game exe is a Windows 10/11 system DLL or ships app-local. The Media Foundation DLLs (`MF`, `MFPlat`, `MFReadWrite`) are delay-loaded only, which matters only on Windows "N" editions. Not tested on a clean PC.

6. **Code that behaves differently under UE_BUILD_SHIPPING.** Nothing looks wrong to me. Balance is not affected: no `Tuning.txt` is tracked in git, and the Development package doesn't ship one either.
   - `SupercutGameMode.cpp:29` skips `Tuning.txt`, so the compiled defaults are used.
   - `SupercutPractice.cpp:51` and `SupercutDevGate.cpp:30` turn off the practice keys, F1-F6/F9, and `-SupercutDev`. As a result the HUD's "TUNED"/"NO DAMAGE" labels never show.
   - `SupercutPlayerController.cpp:68` and `:382` drop dev-gate log lines and the practice-key check.
   - `Supercut.cpp:57` reads `-FPS=` (Shipping only); the non-Shipping branch closes the console and screen messages. The engine compiles the console out of Shipping anyway (`Build.h:347`) and on-screen messages too (`UnrealEngine.cpp:12998`).
   - `SupercutAudio.cpp:253` and `:288` remove `-SupercutRawMix` and `-SupercutRecord` (recording is Development only).
   - `SupercutGeneratedRuns.cpp:78`: a room baked with a stale catalogue only logs a warning in Shipping, where Development stops on it. A player would not see it, but a stale bake would get past Shipping.

**Firewall listener:** I sampled every 5 s through the whole run (146 samples, no admin needed). Neither the launcher nor `Supercut-Win64-Shipping` had any TCP listen port or UDP endpoint. So the Shipping build should not raise the firewall prompt.

**One incident, my fault:** at 00:36 an inline ssh command lost its quotes and started the Shipping `Supercut.exe` with no arguments in pc2's ssh session. It died at once (`DXGI_ERROR_NOT_CURRENTLY_AVAILABLE`, no desktop) and left a crash folder in pc2's `%LOCALAPPDATA%\Supercut`. No process is left over. I'm cleaning it up now.

Carrying on: restore pc2's settings folder, look at the run's pictures, write HANDOFF.

**Mon 16 Nov 00:48:17 · Tool call: Bash** (List pc2 settings folder after the run)

```
ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\appdata.ps1 -Mode list' | tee /d/UE/ship1_farmlogs/appdata_after_run.txt
```

Result:

```
LIVE \Saved\Config\CrashReportClient\UECC-Windows-1C547C3841C4675998E366BAC55A27D3\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-2818CCBD4EE58FC16BDF909119830C1B\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-3FB9F4814BCBF415EE87818563806BE0\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-9972FFF54AA6D331FE11F8A59045AD88\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-C7EBDAF848DC46FA0A630DAFBAD98FFB\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-F96CE6124C1473806CBE07846138D9FD\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\Windows\GameUserSettings.ini 2244 C43957121298
LIVE \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\CrashContext.runtime-xml 29621 3C0E6EC02E29
LIVE \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\UEMinidump.dmp 606088 766E73088BF7
LIVE \Saved\Supercut_PCD3D_SM6.upipelinecache 37730 6FDD919883D5
```

### Mon 16 Nov 00:48:22 · Agent (claude-opus-5-5)

The run added one crash-client config folder and grew the pipeline cache. `GameUserSettings.ini` is unchanged (same hash). Restoring now, then removing the two folders from my stray launch.

**Mon 16 Nov 00:48:24 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\dropmine.ps1",
 "content": "# ship1: delete the two folders my stray launch at 00:36:23 left in %LOCALAPPDATA%\\Supercut (crash GUID 8B89ED0C...).\n$s = Join-Path $env:LOCALAPPDATA 'Supercut\\Saved'\nforeach ($p in \"$s\\Config\\CrashReportClient\\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1\", \"$s\\Crashes\\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000\") {\n    if (-not (Test-Path $p)) { throw \"not found: $($p.Substring($s.Length))\" }\n    Remove-Item $p -Recurse -Force\n    \"deleted $($p.Substring($s.Length))\"\n}\nif (@(Get-ChildItem \"$s\\Crashes\" -Force).Count -eq 0) { Remove-Item \"$s\\Crashes\" -Force; 'deleted \\Crashes (empty)' }\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\dropmine.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:48:29 · Tool call: Bash** (Restore pc2 settings folder and drop my crash folders)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/dropmine.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\appdata.ps1 -Mode restore' | grep LIVE > /d/UE/ship1_farmlogs/appdata_restored.txt; diff <(sed 's/^LIVE //' /d/UE/ship1_farmlogs/appdata_restored.txt) <(sed 's/^BAK //' /d/UE/ship1_farmlogs/appdata_backup.txt) && echo "restore matches backup"; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\dropmine.ps1'; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\appdata.ps1 -Mode list' | tee /d/UE/ship1_farmlogs/appdata_final.txt
```

Result:

```
restore matches backup
deleted \Config\CrashReportClient\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1
deleted \Crashes\UECC-Windows-8B89ED0C4390133BDE5C29AF332D9AC1_0000
deleted \Crashes (empty)
LIVE \Saved\Config\CrashReportClient\UECC-Windows-1C547C3841C4675998E366BAC55A27D3\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-2818CCBD4EE58FC16BDF909119830C1B\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-3FB9F4814BCBF415EE87818563806BE0\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-9972FFF54AA6D331FE11F8A59045AD88\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\CrashReportClient\UECC-Windows-F96CE6124C1473806CBE07846138D9FD\CrashReportClient.ini 239 CE69D7E7BBD1
LIVE \Saved\Config\Windows\GameUserSettings.ini 2244 C43957121298
LIVE \Saved\Supercut_PCD3D_SM6.upipelinecache 34800 3338B04C5FA8
```

### Mon 16 Nov 00:48:35 · Agent (claude-opus-5-5)

pc2's settings folder now matches the 00:26 state: same 5 crash-client folders, `GameUserSettings.ini` 2244 bytes, pipeline cache 34800 bytes. Now the run's pictures.

**Mon 16 Nov 00:48:36 · Tool call: Bash** (List the run's screenshot files)

```
ls -la /d/UE/ship1_farmlogs/run/shots | awk '{print $5, $9}'; cat /d/UE/ship1_farmlogs/run/console.txt | tail -5; grep -n "shot " /d/UE/wt/maincheck_x/Script/main8.txt | wc -l
```

Result:

```
0 .
0 ..
1043514 s10_lap_room.png
1087438 s1_01_start.png
950166 s1_02_at_the_machine.png
892929 s1_03_machine_stopped.png
883148 s1_04_out_of_the_tunnel.png
891338 s1_05_grunt_frozen.png
906152 s1_06_three_shots_hang.png
1076674 s1_07_action.png
1179684 s1_08_grunt_0_gone.png
967997 s1_09_three_more_hang.png
1146905 s1_10_stage_clear.png
996256 s1_11_gate_ahead.png
86741 s1_upgrade_screen.png
1156962 s2_01_start.png
1108046 s2_02_frozen_door_held_open.png
717222 s2_03_nearly_there.png
1093847 s3_01_start.png
1131780 s3_02_rusher_coming.png
991574 s3_03_frozen_in_its_crouch.png
926413 s3_04_two_shots_hang.png
1262884 s3_05_rusher_0_gone.png
1228457 s3_06_rusher_1_coming.png
1020445 s3_07_two_for_the_rusher.png
979177 s3_08_both_set_up.png
1278565 s3_09_action.png
1178737 s3_10_from_the_stage.png
1197046 s4_01_start.png
1269278 s4_02_the_line.png
1264794 s4_03_line_locked_rusher_coming.png
1076482 s4_04_two_for_the_rusher.png
987185 s4_05_two_for_the_marksman.png
1163098 s4_06_set_up.png
1217658 s4_07_action.png
1018536 s4_08_three_for_the_grunt.png
1007453 s4_09_grunt_gone.png
1249350 s4_10_from_the_camera_stage.png
86748 s4_upgrade_screen.png
1189100 s5_01_start.png
885212 s5_02_frozen_three_marks.png
859804 s5_03_three_shots_hang.png
1222605 s5_04_door_open.png
1040322 s5r_rest_scene.png
1159895 s6_01_start.png
1116836 s6_02_four_shots_hang.png
1320297 s6_03_rushers_gone.png
879776 s6_04_from_the_rock.png
1082664 s6_05_marksman_gone.png
987502 s6_06_three_for_the_grunt.png
1018338 s6_07_grunt_gone.png
88700 s6_upgrade_screen.png
1177728 s7_01_start.png
750148 s7_02_frozen_bridge.png
654537 s7_03_target_seen_from_the_bridge.png
681434 s7_04_shot_hangs.png
767829 s7_05_door_ahead_shut_shot_still_hanging.png
723947 s7_06_door_open.png
1161256 s8_01_start.png
979415 s8_02_six_shots_hang.png
1126646 s8_03_three_gone.png
939779 s8_04_six_for_the_grunts.png
1100968 s8_05_set_is_clear.png
1295165 s8_06_from_tower_2.png
﻿game exit code 0
64
```

**Mon 16 Nov 00:48:48 · Tool call: Bash** (Make contact sheets and upgrade-screen JPGs)

```
mkdir -p "[notes]/unreal/megajam-2026/lanes/ship1/shots"; cat > "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/ea92763d-b91e-4163-8658-22436987d5b9/scratchpad/sheets.py" <<'EOF'
import sys, os
from PIL import Image, ImageDraw
src, dst = sys.argv[1], sys.argv[2]
names = sorted(f for f in os.listdir(src) if f.endswith('.png'))
order = lambda n: (int(n[1:].split('_')[0].rstrip('r')) if n[1:].split('_')[0].rstrip('r').isdigit() else 99, n)
names.sort(key=order)
for i in range(0, len(names), 16):
    sheet = Image.new('RGB', (960, 540), 'black')
    d = ImageDraw.Draw(sheet)
    for j, n in enumerate(names[i:i+16]):
        im = Image.open(os.path.join(src, n)).convert('RGB').resize((240, 135))
        x, y = (j % 4) * 240, (j // 4) * 135
        sheet.paste(im, (x, y)); d.text((x + 3, y + 122), n[:-4][:38], fill='yellow')
    sheet.save(os.path.join(dst, f'sheet_{i//16+1}.jpg'), quality=85)
for n in names:
    if 'upgrade' in n:
        Image.open(os.path.join(src, n)).convert('RGB').resize((960, 540)).save(os.path.join(dst, n[:-4] + '.jpg'), quality=88)
print(len(names), Image.open(os.path.join(src, names[0])).size)
EOF
python -I "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/ea92763d-b91e-4163-8658-22436987d5b9/scratchpad/sheets.py" /d/UE/ship1_farmlogs/run/shots "[notes]/unreal/megajam-2026/lanes/ship1/shots"; ls "[notes]/unreal/megajam-2026/lanes/ship1/shots"
```

Result:

```
62 (1280, 720)
s1_upgrade_screen.jpg
s4_upgrade_screen.jpg
s6_upgrade_screen.jpg
sheet_1.jpg
sheet_2.jpg
sheet_3.jpg
sheet_4.jpg
```

**Mon 16 Nov 00:48:51 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\shots\\sheet_1.jpg"
}
```

Result:

```
[image]
```

**Mon 16 Nov 00:48:52 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\shots\\s1_upgrade_screen.jpg"
}
```

Result:

```
[image]
```

**Mon 16 Nov 00:48:55 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\shots\\sheet_2.jpg"
}
```

**Mon 16 Nov 00:48:55 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\shots\\sheet_3.jpg"
}
```

Result:

```
[image]
```

Result:

```
[image]
```

**Mon 16 Nov 00:48:55 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\shots\\sheet_4.jpg"
}
```

Result:

```
[image]
```

**Mon 16 Nov 00:49:07 · Tool call: Bash** (Log run, listener, restore and pictures)

```
date "+%d %b %H:%M"; cat >> "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md" <<'EOF'
- 00:41 `scripts/listen.ps1` started on pc2 (every 5 s, 1200 s max), then the run:
  `farm.sh run pc2 ship1 /d/UE/ship1_farmlogs -Shipping -Run main8 -Seed 1 -Script '{P}\Script\main8.txt' -FixedFps 240 -Silent -TimeoutSeconds 900`.
- 00:47 Run done: farm exit 0, 372 s (00:41:11 to 00:47:28), console `game exit code 0`. `run/run.log` (filled by
  `-SupercutLog=`) line 2189: `RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9`, the
  Development reference exactly. 0 `missing usage flag`, no Fatal.
- 00:47 Listeners: 146 samples from 00:41:09 to 00:47:29, both `Supercut` (launcher) and `Supercut-Win64-Shipping`
  showed `tcp_listen=[] udp=[]` every time. No trace listener on 1985, nothing else either. (`paks_listen.txt`)
- 00:48 Main thread asked for an interim report at 00:41; sent at 00:49 in chat.
- 00:50 pc2 `%LOCALAPPDATA%\Supercut` after the run: one new CrashReportClient config folder (each Shipping start
  makes one), pipeline cache 34800 -> 37730 bytes, GameUserSettings.ini unchanged (same hash). `appdata.ps1 restore`:
  live folder equals the backup (diff empty). `dropmine.ps1` deleted my 00:36 crash folders. Final listing equals the
  00:26 one: 5 CrashReportClient folders, GameUserSettings.ini 2244 bytes, pipeline cache 34800 bytes.
- 00:52 62 run pictures (1280x720) came back. Contact sheets `shots/sheet_1..4.jpg` and the three upgrade screens
  looked at: scene, HUD, freeze sketch view, CUT/ACTION cards and upgrade cards all draw; no debug text on screen, no
  black or empty frame. The upgrade PNGs are small (87 KB) only because the background is flat. The yellow names on
  the sheets are mine. No Development pictures of this run to compare against.
EOF
```

Result:

```
16 Nov 00:49
[This command modified 1 file you've previously read: unreal\megajam-2026\lanes\ship1\LOG.md. Call Read before editing.]
```

**Mon 16 Nov 00:49:12 · Tool call: Bash** (Correct log times to match the clock)

```
F="[notes]/unreal/megajam-2026/lanes/ship1/LOG.md"; sed -i 's/^- 00:48 Main thread/- 00:47 Main thread/; s/^- 00:50 pc2/- 00:49 pc2/; s/^- 00:52 62 run/- 00:49 62 run/; s/sent at 00:49 in chat/sent at about 00:48 in chat/' "$F"; grep -n "^- 00:4[6-9]" "$F" | cut -c1-60
```

Result:

```
51:- 00:47 Run done: farm exit 0, 372 s (00:41:11 to 00:47:2
54:- 00:47 Listeners: 146 samples from 00:41:09 to 00:47:29,
56:- 00:47 Main thread asked for an interim report at 00:41;
57:- 00:49 pc2 `%LOCALAPPDATA%\Supercut` after the run: one 
61:- 00:49 62 run pictures (1280x720) came back. Contact she
[This command modified 1 file you've previously read: unreal\megajam-2026\lanes\ship1\LOG.md. Call Read before editing.]
```

### Mon 16 Nov 00:49:17 · Agent (claude-opus-5-5)

Cleaning up my helper files and the settings backup on pc2. The backup holds a minidump, which can contain names.

**Mon 16 Nov 00:49:19 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\scripts\\cleanup.ps1",
 "content": "# ship1: remove this lane's helper files on pc2 after the restore: the settings backup and the scripts folder.\n# The mirror C:\\UE\\Farm\\ship1 and the package C:\\UE\\Farm\\_builds\\ship1 stay, as every farm name's do.\nforeach ($p in 'C:\\UE\\Farm\\_out\\ship1\\appdata_backup', 'C:\\UE\\Farm\\_out\\ship1_tools') {\n    if (Test-Path $p) { Remove-Item $p -Recurse -Force; \"deleted $p\" } else { \"absent $p\" }\n}\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\scripts\cleanup.ps1 (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:49:21 · Tool call: Bash** (Remove helper files on pc2, check free disk)

```
scp -q "[notes]/unreal/megajam-2026/lanes/ship1/scripts/cleanup.ps1" pc2:C:/UE/Farm/_out/ship1_tools/ && ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\ship1_tools\cleanup.ps1'; ssh pc2 'powershell -NoProfile -Command "Get-PSDrive C | ForEach-Object { [int]($_.Free/1GB) }"'
```

Result:

```
deleted C:\UE\Farm\_out\ship1\appdata_backup
deleted C:\UE\Farm\_out\ship1_tools
24
```

**Mon 16 Nov 00:50:04 · Tool call: Write**

````
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\ship1\\HANDOFF.md",
 "content": "# ship1 handoff: main `ae8614e` as a Shipping build, on pc2 (16 Nov 2026)\n\nNo failures. Main `ae8614e` compiles, packages and plays as Shipping on pc2. The scripted run gives the Development\nline exactly. No game source was touched, no git was run in the game repo, nothing was built on c4.\n\n## Results\n\n| Check | Result |\n| --- | --- |\n| Worktree | `git -C /d/UE/wt/maincheck_x log --oneline -1` prints `ae8614e` |\n| Editor build (`-Jobs 8`) | exit 0, `Result: Succeeded`, 0 errors, 3 C4996 deprecation warnings in test files |\n| Shipping package | farm exit 0, `BUILD SUCCESSFUL`, `ExitCode=0 (Success)`, 0 errors |\n| `Failed to compile Material` | 0 (package log) |\n| `missing usage flag` | 0 (package log and run log) |\n| main8 Shipping run | `RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9`, same as the Development reference; `game exit code 0` |\n| Listeners during the run | none: 146 samples, `tcp_listen=[] udp=[]` for the launcher and the game |\n| Pictures | 62 of 62 written and drawn; no debug text, no black frame |\n\nTime on pc2:\n\n| Step | Time |\n| --- | --- |\n| Mirror (3493 files, 3557.3 MB) | 114 s |\n| Editor build, cold, 8 jobs | 168 s |\n| Shipping package in all | 438 s: compile 124 actions at one job 319 s, cook 1473 packages 78 s, stage 37 s |\n| main8 run, offscreen, `-FixedFps 240` | 372 s |\n\nPackage log warnings: the Fab plugin dependency line, and `LogCore: Warning: UTS: Timed out waiting for the Unreal\nTrace Server process to start` (cook side). Neither is new or harmful.\n\n## How the Shipping run is proven\n\nA Shipping build has `NO_LOGGING`, so the engine writes no log. The game's own log takes its place: `Supercut.h:11-30`\nredefines `UE_LOG` under `NO_LOGGING` to write to the file named by `-SupercutLog=<file>` (`Supercut.cpp:18-50`).\n`Tools\\run_demo.ps1 -Shipping` passes `-SupercutLog=<Log>` instead of `-abslog=`. `-FPS=` is read by the game module\nin Shipping (`Supercut.cpp:57-64`), because the engine reads it only outside Shipping.\n\nThe evidence is the line `LogSupercut: Display: RUN wrapped: ...` in the `-Log` file (line 2189 here), plus\n`game exit code 0` printed by run_demo. The command:\n\n```\nfarm.sh run pc2 ship1 /d/UE/ship1_farmlogs -Shipping -Run main8 -Seed 1 -Script '{P}\\Script\\main8.txt' -FixedFps 240 -Silent -TimeoutSeconds 900\n```\n\nOn c4 directly (held1, its HANDOFF line 145):\n`powershell -File Tools\\run_demo.ps1 -Shipping -Run main8 -Seed 1 -Script \"D:\\UE\\Projects\\Supercut59\\Script\\main8.txt\" -FixedFps 240 -Silent -Log <log>`.\nBack up `%LOCALAPPDATA%\\Supercut` first and put it back after: each Shipping start adds a CrashReportClient folder and\nchanges the pipeline cache there.\n\n## The package\n\n- Size: 854,824,624 bytes, 827 files (`measure.txt`).\n- Largest ten: `Supercut-Windows.ucas` 500,986,480; `Supercut-Win64-Shipping.exe` 175,716,352; `nvngx_dlss.dll`\n  58,956,912; `DirectML.dll` 18,538,488; `onnxruntime.dll` 17,339,384; `mx_strings.wav` and `mx_arcade.wav`\n  16,648,304 each; `Supercut-Windows.pak` 11,505,830; `GFSDK_Aftermath_Lib.x64.dll` 5,799,016; `D3D12Core.dll` 5,034,768.\n- Also: `Supercut-Windows.utoc` 447,634; `global.ucas` 3,483,584; `global.utoc` 842; launcher `Supercut.exe` 174,080.\n- The two music wavs are loose on purpose (`Supercut.Build.cs:13-15` stages them, `SupercutMusic.cpp:23` reads them).\n- `.pdb`: none in the package. UAT runs with `-nodebuginfo` and `package_shipping.cmd` deletes any `*.pdb`. The\n  game's pdb (257,544,192 bytes) stays in the project at `Binaries\\Win64\\Supercut-Win64-Shipping.pdb`.\n- Files the game may not need: `Engine\\Plugins\\NNE\\NNERuntimeORT\\...\\onnxruntime.dll` (17 MB),\n  `Supercut\\Binaries\\Win64\\D3D12\\x64\\d3d12SDKLayers.dll` (the D3D debug layer, 5 MB), `NOTICES.txt`. The engine\n  stages them; removing them was not tested, so leave them.\n\n## What a clean Windows 10 or 11 PC needs\n\nNothing to install, as far as the files show. `package_shipping.cmd` passes\n`-applocaldirectory=...\\AppLocalDependencies` and no `-prereqs`. So:\n\n- UAT copies the VC++ runtime and UCRT (`msvcp140*`, `vcruntime140*`, `concrt140`, `vccorlib140`, `ucrtbase`,\n  `api-ms-win-*`) beside the game exe (package log line 961; `WinPlatform.Automation.cs:216-222, 474-499`).\n- No prerequisites installer is in the package: `vc_redist.x64.exe` is staged only with `-prereqs`\n  (`WinPlatform.Automation.cs:207-214`, `ProjectParams.cs:1054`).\n- Hard imports of the game exe (dumpbin, `measure2.txt`) are Windows system DLLs or app-local ones. Media Foundation\n  (`MF`, `MFPlat`, `MFReadWrite`), `XAudio2_9`, `d3d11`, `d3d12`, `XINPUT1_4` are delay-loaded. Windows \"N\" editions\n  lack Media Foundation; delay-loaded, so it matters only if the game plays media through it. Not tested.\n- Not checked: a real clean PC, or a PC without an up-to-date GPU driver.\n\n## Firewall listener (GOTCHAS 580-597)\n\nChecked without admin and without touching firewall settings: `Get-NetTCPConnection -State Listen` and\n`Get-NetUDPEndpoint` per process, every 5 s through the whole run (`scripts/listen.ps1`, `paks_listen.txt`). Neither\n`Supercut.exe` nor `Supercut-Win64-Shipping.exe` listened on any TCP port or held any UDP endpoint. The Shipping build\ndoes not open the trace listener on 1985, so it should not raise the Windows Firewall prompt. (pc2 has\n`NotifyOnListen False`, so a prompt could not have been seen there anyway; the listener tables are the evidence.)\n\n## What a judge does not get in Shipping\n\n`git -C /d/UE/wt/maincheck_x grep -n \"UE_BUILD_SHIPPING\" -- Source`, plus `NO_LOGGING`:\n\n| Place | In Shipping |\n| --- | --- |\n| `Supercut.h:11`, `Supercut.cpp:18` (`NO_LOGGING`) | Engine log gone; the game's lines go to `-SupercutLog=` only when given |\n| `Supercut.cpp:57` | Reads `-FPS=` itself. The other branch (not Shipping) closes the console, gameplay debugger and engine screen messages when `-SupercutDev` is off. Shipping needs none of that: the engine compiles the console out (`Build.h:347`) and screen messages out (`UnrealEngine.cpp:12998`) |\n| `SupercutGameMode.cpp:29` | `Tuning.txt` is never read; the compiled defaults play |\n| `SupercutDevGate.cpp:30`, `SupercutPractice.cpp:51` | No practice keys (F1-F6, F9), `-SupercutDev` ignored, so the HUD's \"TUNED: n values\" and \"NO DAMAGE\" never show |\n| `SupercutPlayerController.cpp:68` | Dev-gate start line and debug-binding removal skipped (Shipping has no debug bindings to remove) |\n| `SupercutPlayerController.cpp:382` | Practice-key clash check skipped |\n| `SupercutAudio.cpp:253` | `-SupercutRawMix` ignored: the master limiter is always on |\n| `SupercutAudio.cpp:288` | `-SupercutRecord` (wav recording) compiled out |\n| `SupercutGeneratedRuns.cpp:78` | A room baked with a stale prop catalogue logs a warning instead of failing the load |\n\nNothing here should stay in Shipping. The tuning file does not matter for balance. No `Tuning.txt` is tracked in\ngit (`.gitignore:16-18`), and the Development package ships only `Tuning.example.txt`, so Development and Shipping\nboth play the compiled defaults in `SupercutTuning.h`. The one thing to keep an eye on is\n`SupercutGeneratedRuns.cpp:78`: in Shipping a stale room bake gets through with only a warning a judge never sees.\nDevelopment stops on it, so it only matters if a room is re-baked after the last Development check.\n`[taste: owner review]` on whether that is wanted.\n\n## Incident (mine)\n\nAt 00:36:23 an inline ssh command lost its quotes on pc2 (the ssh shell is cmd). PowerShell then ran\n`$d=C:\\UE\\Farm\\_builds\\ship1\\Supercut59_ship\\Windows\\Supercut` as a command, which started `Supercut.exe` with no\narguments inside the ssh session. It died at second 0: assert, `DXGI_ERROR_NOT_CURRENTLY_AVAILABLE` at\n`WindowsD3D12Viewport.cpp:162`, the known no-desktop failure. It left a crash folder and a CrashReportClient folder in\npc2's `%LOCALAPPDATA%\\Supercut`; both are deleted. No process was left, and nothing showed on the desktop. After\nthat, every remote command went through a `.ps1` file in `scripts/`.\n\nGotcha for the notes: over ssh to pc2, `''` quotes inside `powershell -Command \"...\"` are eaten, and an unquoted path\nto a game folder in PowerShell runs the game. Put remote PowerShell in a file.\n\n## State left on pc2\n\n- `%LOCALAPPDATA%\\Supercut` is as it was at 00:26: 5 CrashReportClient folders, `GameUserSettings.ini` 2244 bytes\n  (same hash before and after), pipeline cache 34800 bytes (`/d/UE/ship1_farmlogs/appdata_*.txt`).\n- Left: mirror `C:\\UE\\Farm\\ship1`, package `C:\\UE\\Farm\\_builds\\ship1\\Supercut59_ship`, step logs under\n  `C:\\UE\\Farm\\_out\\ship1`. C: free went from 36 GB to 24 GB. Delete `C:\\UE\\Farm\\ship1` and\n  `C:\\UE\\Farm\\_builds\\ship1` when pc2 needs the room.\n- Not copied anywhere, not zipped. No entry folder made.\n\n## Not checked\n\n- A run on a desktop with a real window (pc2 runs offscreen through ssh), and any frame-rate figure.\n- A clean Windows PC, a Windows \"N\" edition, or a PC without Visual C++ ever installed.\n- The generated run (`s7.txt`) and the tests: the brief asked for main8 only.\n- The UBT compile log `ubt_package_ship.log` did not come back from pc2; the package log lists every compile step.\n\n## Files\n\n- [LOG.md](<[notes]/unreal/megajam-2026/lanes/ship1/LOG.md>)\n- [measure.txt](<[notes]/unreal/megajam-2026/lanes/ship1/measure.txt>), [measure2.txt](<[notes]/unreal/megajam-2026/lanes/ship1/measure2.txt>), [paks_listen.txt](<[notes]/unreal/megajam-2026/lanes/ship1/paks_listen.txt>)\n- Contact sheets: [sheet_1.jpg](<[notes]/unreal/megajam-2026/lanes/ship1/shots/sheet_1.jpg>) to `sheet_4.jpg`, upgrade screens `s1_`, `s4_`, `s6_upgrade_screen.jpg`\n- Farm logs: `/d/UE/ship1_farmlogs` (build, package-shipping, run with `run.log` and 62 PNGs)\n- Scripts: `scripts/appdata.ps1`, `listen.ps1`, `measure.ps1`, `measure2.ps1`, `paks.ps1`, `procs.ps1`, `crashinfo.ps1`, `dropmine.ps1`, `cleanup.ps1`\n"
}
````

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\ship1\HANDOFF.md (file state is current in your context — no need to Read it back)
```

**Mon 16 Nov 00:50:07 · Tool call: Bash** (Final log entry with clock time)

```
date "+%d %b %H:%M"; printf -- "- %s pc2 cleanup: deleted %s and %s. C: free 24 GB. HANDOFF.md written.\n" "$(date +%H:%M)" '`_out\ship1\appdata_backup`' '`_out\ship1_tools`' >> "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md"; tail -1 "[notes]/unreal/megajam-2026/lanes/ship1/LOG.md"
```

Result:

```
16 Nov 00:50
- 00:50 pc2 cleanup: deleted `_out\ship1\appdata_backup` and `_out\ship1_tools`. C: free 24 GB. HANDOFF.md written.
```

### Mon 16 Nov 00:50:21 · Agent (claude-opus-5-5)

Main `ae8614e` builds, packages and plays as Shipping on pc2. Nothing failed. Finished at 00:50; nothing has changed since the interim report except that pc2 is cleaned up.

**Build, package and run**
- **Shipping package:** passed. Farm exit 0 and `BUILD SUCCESSFUL`. No compile error, 0 `Failed to compile Material`, 0 `missing usage flag`. Every compile step is tagged `[NoUba]`, so MSVC 14.44 on pc2 didn't hit the earlier Shipping header crash.
- **Scripted run:** `RUN wrapped: takes 1, time 108.8 s, shots 22, freezes 14, kills 17, scenes 9`. That is the Development reference exactly. The game exited with code 0.
  - The proof is the game's own log, written through `-SupercutLog=`, which `run_demo.ps1 -Shipping` passes. The line is at line 2189 of `/d/UE/ship1_farmlogs/run/run.log`.
  - All 62 run pictures came back and draw correctly. No debug text and no black frames.
- **Time on pc2:**

  | Step | Time |
  | --- | --- |
  | Mirror | 114 s |
  | Editor build | 168 s |
  | Shipping package | 438 s (compile 319 s at one job, cook 78 s, stage 37 s) |
  | Scripted run | 372 s |

**Package contents**
- **Size:** 854,824,624 bytes in 827 files. The game exe is 175,716,352 bytes; `Supercut-Windows.ucas` 500,986,480, `.utoc` 447,634, `.pak` 11,505,830.
- **Symbols:** no `.pdb` in the package. The game's pdb (257 MB) stays in the project's `Binaries\Win64` folder.
- **What a judge's PC needs:** nothing to install, as far as the files show.
  - The package script copies the VC++ runtime and UCRT DLLs beside the game exe, so there is no prerequisites installer and none is needed for those.
  - The Media Foundation DLLs are delay-loaded only, which matters only on Windows "N" editions.
  - Not tried on a clean PC.

**Firewall:** I checked the game's ports every 5 s through the whole run, with no admin rights. Neither the launcher nor the Shipping game listened on any TCP port or held any UDP port. The Shipping build should not raise the Windows Firewall prompt.

**What Shipping leaves out** (full table in HANDOFF):
- `Tuning.txt` is not read. Balance doesn't change, because no `Tuning.txt` is tracked in git, so both builds play the compiled defaults.
- No practice keys. Because of that, "TUNED" and "NO DAMAGE" never show on screen.
- `-SupercutRawMix` and `-SupercutRecord` are compiled out.
- The engine itself compiles out the console and on-screen debug messages.

Nothing there should stay in Shipping. One thing to watch: `SupercutGeneratedRuns.cpp:78`. In Shipping, a room baked against an old prop list only logs a warning, where Development stops on it. It only matters if a room is re-baked after the last Development check. [taste: owner review]

**My mistake:** at 00:36 a remote command lost its quotes and started the Shipping game on pc2 with no arguments. It crashed at once (no display over ssh) and left two crash folders. No process was left running and nothing appeared on the desktop.
- I deleted both folders. pc2's `%LOCALAPPDATA%\Supercut` now matches its 00:26 state, with the same `GameUserSettings.ini` hash.
- Every remote command after that ran from a script file.

**Left on pc2:** the mirror and the package. Its C: drive went from 36 GB free to 24 GB. Nothing was copied off pc2, zipped, or made into an entry folder.

**Not checked:** a run in a real window, a clean Windows PC, the generated run and the tests (the brief asked for main8 only).

Files are in `unreal/megajam-2026/lanes/ship1/`:
- [HANDOFF.md](<[notes]/unreal/megajam-2026/lanes/ship1/HANDOFF.md>)
- [LOG.md](<[notes]/unreal/megajam-2026/lanes/ship1/LOG.md>)
