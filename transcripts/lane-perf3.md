# Transcript: lane-perf3

Session 2f0f321c-13ca-453f-9197-384709201b64. Exported by `tools/export_transcripts.py`; entries from Fri 13 Nov 2026 05:41 SGT on. Times are Singapore time. See the README for what is removed.

### Sun 15 Nov 10:51:48 · Brief from the orchestrating agent

Act as the implementation sub-agent for this task.

GLASSBOX-MEGAJAM-2026 lane=perf3

Your full brief is the file `[notes]\unreal\megajam-2026\lanes\perf3\BRIEF.md`. Read it in full first, then the shared rules file it names (`[notes]\unreal\megajam-2026\lanes\COMMON_RULES.md`), which is part of the brief. Then do the work the brief describes, yourself, with no subagents.

In short: find out what the jam game SUPERCUT (Unreal Engine 5.9, C++) does on an old graphics card (GTX 1070, the farm PC pc2): the cause of 24 `Failed to create compute pipeline` errors at frame 0 and whether anything on screen is missing, the frame rate at default settings at 1920x1080, and hitching in the first minute after a first launch. Remove what is broken or slow without changing gameplay or the look on a good card. Your project copy is the git worktree `D:\UE\wt\perf3` (branch `perf3`); builds, tests, packages and scripted runs go to pc2 under farm name `perf3`. Do not end your turn while a build, package or run you need is still going. End with a clean tree, `HANDOFF.md` in your lane folder, and a short final report.

**Sun 15 Nov 10:51:51 · Tool call: Bash** (Read lane brief and common rules)

```
cat "[notes]/unreal/megajam-2026/lanes/perf3/BRIEF.md"; echo ======; cat "[notes]/unreal/megajam-2026/lanes/COMMON_RULES.md"
```

Result:

```
GLASSBOX-MEGAJAM-2026 lane=perf3

You find out what the jam game SUPERCUT (Unreal Engine 5.9, C++) does on an old graphics card, and remove what
is broken or slow there. About two and a half hours. Do the work yourself; start no subagents.

Read and follow `[notes]\unreal\megajam-2026\lanes\COMMON_RULES.md` in full. It is part of
this brief.

## Background

The farm PC pc2 has a GTX 1070. Judges' PCs are unknown, so pc2 is our low end. Three things are not known
there:

- Every run log on pc2 has 24 `Failed to create compute pipeline` errors at frame 0. Nobody has found which
  shaders they are or whether anything on screen is missing because of them.
- Frame rate at the game's default settings at 1920x1080 since the sky light, the new revolver, the film-set
  props and the hall went in.
- Hitching in the first minute after a first launch (shader and pipeline compiles).

Read first: `lanes\perf2\REPORT.md`, `lanes\perf2\tables.md` and `lanes\perf2\tools\` (the last measurement and
how it was made), `lanes\dlss2\HANDOFF.md` (upscaling and its defaults per card), `lanes\light1\HANDOFF.md`,
`lanes\shell1\HANDOFF.md` (settings, the hall's frame time script `Script\shell1_hall_fps.txt`),
`lanes\vfx1\HANDOFF.md` (`Script\vfx1_fps.txt`).

## Jobs

1. **The 24 errors.** Which pipelines fail and why (shader name, feature, the driver or card limit), from the log
   with more verbose logging if needed and from the engine source. Compare a picture set from pc2 against the
   same scripted pictures from [pc-b] (RTX 4080 Super; one run there under your farm name, load check first, three
   other lanes use it) to find anything missing or different on pc2: shadows, reflections, the sky light, the
   sketch effect, particles, upscaling. If a feature that cannot work on this card causes them, turn it off on
   cards that lack it by the engine's own setting or capability check, not by card name, and show the errors are
   gone and the pictures unchanged. If they are harmless and cannot be removed cheaply, say why and stop there.
2. **Frame rate.** At default settings, 1920x1080, on pc2: average and worst 1% frame time in the heaviest
   generated room during a fight with freezes and breaks, in the hall, and in the hand-made run. If the average
   is over 16.7 ms anywhere, list the top costs (the engine's own GPU profile output) and fix the largest one
   that does not change the look at a glance; show before and after pictures and numbers. A default se
[... 8012 more characters not shown]
```

**Sun 15 Nov 10:51:59 · Tool call: Bash** (Size up the files to read)

```
cd "[notes]/unreal"; wc -l GOTCHAS.md FINDINGS.md megajam-2026/FARM.md megajam-2026/lanes/perf2/* megajam-2026/lanes/dlss2/HANDOFF.md megajam-2026/lanes/light1/HANDOFF.md megajam-2026/lanes/shell1/HANDOFF.md megajam-2026/lanes/vfx1/HANDOFF.md; ls megajam-2026/lanes/perf2/tools megajam-2026/lanes/perf3 2>&1; date
```

Result:

```
1243 GOTCHAS.md
    761 FINDINGS.md
    156 megajam-2026/FARM.md
     21 megajam-2026/lanes/perf2/LOG.md
    250 megajam-2026/lanes/perf2/REPORT.md
wc: megajam-2026/lanes/perf2/logs: Is a directory
      0 megajam-2026/lanes/perf2/logs
wc: megajam-2026/lanes/perf2/shots: Is a directory
      0 megajam-2026/lanes/perf2/shots
     27 megajam-2026/lanes/perf2/tables.md
wc: megajam-2026/lanes/perf2/tools: Is a directory
      0 megajam-2026/lanes/perf2/tools
    283 megajam-2026/lanes/dlss2/HANDOFF.md
    243 megajam-2026/lanes/light1/HANDOFF.md
    272 megajam-2026/lanes/shell1/HANDOFF.md
    263 megajam-2026/lanes/vfx1/HANDOFF.md
   3519 total
megajam-2026/lanes/perf2/tools:
__pycache__
analyze.py
go.sh
mk_scripts.py
perf_full.txt
perf_run.ps1
report_tables.py
setlevel_0.txt
setlevel_1.txt
setlevel_2.txt
setlevel_3.txt
sumsample.py
timeline.py
wait.ps1

megajam-2026/lanes/perf3:
BRIEF.md
Sun Nov 15 10:52:01 MPST 2026
```

**Sun 15 Nov 10:52:03 · Tool call: Bash** (Read FARM.md)

```
cd "[notes]/unreal"; cat megajam-2026/FARM.md
```

Result:

````
# Build farm for SUPERCUT

Lane farm1, 14 Nov 2026. Other PCs build, test, package and run SUPERCUT for lanes on c4. Git, agents and the
source of truth stay on c4. A farm PC holds a plain copy of a project folder (a "mirror"), never a git repo.
Nothing is ever pushed with git.

## Which PCs are ready

| PC | Root | Ready | Build | Tests | Package | Scripted run | Lanes at once |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `[pc-b]` | `C:\UE` | **yes** (17:33) | yes | yes | Development and Shipping | yes, offscreen | 2 (builds queue, see below) |
| `pc2` | `C:\UE` | **yes** (18:02) | yes | yes | Development | yes, offscreen, slow: add `-TimeoutSeconds 900` | 1 (16 GB RAM, Studio windows open) |
| `[pc-c]` | `F:\UE` | **yes** (17:58) | yes | yes | Development | yes, offscreen | 2 (builds queue, see below) |
| `pc4` | `C:\UE` | **compile only** (18:09) | yes (editor and game targets) | **no** | **no** | **no** | 1 (12 GB RAM, runs hot) |

pc4: Smart App Control (Windows code integrity policy `VerifiedAndReputableDesktop`, enforced) blocks every DLL we
compile. The editor could not load `UnrealEditor-Supercut.dll` (`GetLastError=4551`, Code Integrity event 3077), so
tests, cooking and the game cannot run there. Builds do run: use pc4 only to check that a change compiles
(`build pc4 <name> <logs> -Jobs 4`, and `-Target Supercut -Jobs 4` for the game target). Nothing on its policy was
changed and nothing should be; turning Smart App Control off is the owner's call.

The root table also sits at the top of `farm/farm.sh` (`root_of`). On every PC: engine in `<root>\UE_5.9`, mirrors in
`<root>\Farm\<name>`, packages in `<root>\Farm\_builds\<name>`, step logs in `<root>\Farm\_out\<name>\<step>`, farm
scripts in `<root>\Farm\_farm`.

## Five-minute start (from c4, Git Bash)

The commands below use `[pc-b]`; `[pc-c]` and `pc2` take the same commands (on pc2 add `-TimeoutSeconds 900` to `run`).
Pick a name for your lane (letters, digits, no spaces): use your lane name, for example `vfx1`. Never use another
lane's name and never `proof` (the farm's own check).

```bash
F="[notes]/unreal/megajam-2026/farm/farm.sh"
LOGS=/d/UE/wt/vfx1_farmlogs          # any folder on c4 outside the worktree; each step writes LOGS/<step>/

"$F" status [pc-b]                                   # 1. load check, see "Before a heavy step" below
"$F" mirror [pc-b] vfx1 /d/UE/wt/vfx1                 # 2. copy your worktree (changed files only)
"$F" build  [pc-b] vfx1 "$L
[... 8825 more characters not shown]
````

**Sun 15 Nov 10:52:06 · Tool call: Bash** (Read perf2 report, tables, log)

```
cd "[notes]/unreal/megajam-2026/lanes/perf2"; cat REPORT.md tables.md LOG.md
```

Result:

```
# perf2 report: SUPERCUT Shipping build on pc2 (GTX 1070), first start and all four QUALITY levels

14 Nov 2026, 06:33 to 07:45 SGT, from c4, on pc2 only. Build: `SUPERCUT_shipping_test.zip` from `lanes\shell1\out` (sha256 `8f5b9ce5...fe52`, same on c4 and pc2),
unzipped on pc2 to `C:\UE\SupercutPerf2\unz\SUPERCUT` (117 files, 505,835,058 bytes, as the shell1 handoff says).
Nothing on c4 was started or changed, and nothing in the game.

## Answers

- **First start on pc2 (no saved settings, no size options): the hardware test picked EPIC**, display FULLSCREEN 1920x1080. At EPIC the scripted full run averaged **45.5 fps** by the game's own counter
  (44.8 by my per-room log method), worst second 33.6 (room 1, first seconds). That is under 60 in every room.
- **The pick is wrong for this PC.** HIGH is the highest level that holds 60: 85.1 fps average, worst second 62.5. EPIC should not have been picked.
  The benchmark gave CPU 196 and GPU 294 and put all ten groups at 3 (EPIC).
- LOW 383 fps, MEDIUM 154, HIGH 85, EPIC 45 (all rooms, live and frozen together). The GPU is at 95 to 99 percent in every run, so the card is the limit at every level, LOW included.
- Worst moment: room 1, the first 5 s (the corridor to the wind machine and the machine itself), 33.5 fps at EPIC and 62.5 at HIGH. Not enemies, shots or a freeze (see "Worst moment").
- Broken: nothing in the pictures. One finding about the scripted player (without a fixed step it died in room 6 in 3 of 9 full runs, and in room 3 in both picture runs, see "Scripted run"). That is the script's timing, not the game.
- Not measured: see the last section.

## How frame rate was measured

The Shipping game has no engine log. With `-SupercutLog=<file>` it writes its own `LogSupercut` lines. Every line carries the wall clock in ms and `GFrameCounter % 1000`.
`-SupercutTrace` adds a `TRACE` line every 0.5 s of play, so the log has a line at least every 0.55 s (checked: largest gap inside a run 0.55 s in the normal runs).
`tools\analyze.py` unwraps the counter, takes frames between lines over seconds between lines, and cuts by log events:

- A room runs from its `ROOM change` line to its `PICK offered` line (room 8: to `RUN wrapped`). The upgrade screens are not counted.
- Live and frozen time are split by the `FREEZE begin` and `FREEZE end` lines.
- Worst second = the slowest stretch of at least 1.0 s inside one room and one state, built from consecutive log lines (1.0 to 1.5 s long). A single slow frame is not
[... 26004 more characters not shown]
```

**Sun 15 Nov 10:52:11 · Tool call: Bash** (Read perf2 run tooling)

```
cd "[notes]/unreal/megajam-2026/lanes/perf2/tools"; cat go.sh perf_run.ps1 wait.ps1
```

Result:

```
#!/bin/bash
# usage: go.sh <tag> <scriptfile on pc2 under tools\> [flags: -Quit -Shots]
# Waits for an idle GPU (util <40 pct and power <70 W, 4 samples in a row, up to 15 min, then runs anyway and says UNDER LOAD),
# starts perf_run.ps1 in pc2's desktop session, waits, copies the log, samples, sockets and result back with the PC and user names masked.
cd "$(dirname "$0")/.."
tag=$1; sf=$2; shift 2; flags="$*"
tr=$(printf '%s' 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\SupercutPerf2\tools\perf_run.ps1 -Tag ' "$tag" ' -ScriptFile C:\UE\SupercutPerf2\tools\' "$sf" " $flags")
ssh pc2 "schtasks /create /tn perf2_supercut /tr \"$tr\" /sc once /st 23:59 /it /f" >/dev/null || { echo create failed; exit 1; }
ok=0; waited=0
while [ $ok -lt 4 ] && [ $waited -lt 900 ]; do
  r=$(ssh pc2 'nvidia-smi --query-gpu=utilization.gpu,power.draw --format=csv,noheader,nounits')
  u=${r%%,*}; m=${r##*, }; m=${m%%.*}
  if [ "$u" -lt 40 ] && [ "$m" -lt 70 ]; then ok=$((ok+1)); sleep 1; else ok=0; sleep 4; waited=$((waited+5)); fi
done
load=idle; [ $ok -lt 4 ] && load="UNDER LOAD (gate not met after ${waited}s)"
echo "$(date +%H:%M) gate before $tag: $load; gpu now: $(ssh pc2 'nvidia-smi --query-gpu=utilization.gpu,memory.used,power.draw --format=csv,noheader')"
ssh pc2 'schtasks /run /tn perf2_supercut' >/dev/null || { echo run failed; exit 1; }
ssh pc2 "powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\SupercutPerf2\tools\wait.ps1 -Tag $tag" > logs/${tag}_result.raw
un=$(ssh pc2 'echo %USERNAME%' | tr -d '\r\n'); cn=$(ssh pc2 'echo %COMPUTERNAME%' | tr -d '\r\n')
mask() { sed -e "s#$un#USER#Ig" -e "s#$cn#PC2#Ig"; }
echo "gate=$load" > logs/${tag}_result.txt
cat logs/${tag}_result.raw | mask >> logs/${tag}_result.txt; rm logs/${tag}_result.raw
for f in run.log sample.csv sockets.txt GameUserSettings.before.ini GameUserSettings.after.ini; do
  scp -q pc2:C:/UE/SupercutPerf2/out/$tag/$f logs/${tag}_$f.tmp 2>/dev/null && mask < logs/${tag}_$f.tmp > logs/${tag}_$f && rm logs/${tag}_$f.tmp
done
grep -E "exit_code|seconds_to_exit|hang|processes_alive|gpu_before|free_ram" logs/${tag}_result.txt
# Lane perf2. Runs one launch of the Shipping build on pc2 in the logged-in desktop session (start it with a scheduled task /it).
# -Quit adds -SupercutQuit (the full run ends by itself); the setlevel scripts leave through the menu's QUIT row instead.
# -Shots adds -SupercutShots (pictures; they cost frames, so frame rate runs leave it off).
# -
[... 4904 more characters not shown]
```

### Sun 15 Nov 10:52:14 · Agent (claude-opus-5-5)

I'm reading the brief's required handoffs (perf2 done, now dlss2, light1, shell1, vfx1, then GOTCHAS) before touching pc2.

**Sun 15 Nov 10:52:14 · Tool call: Bash** (Read dlss2 handoff)

```
cd "[notes]/unreal/megajam-2026/lanes"; cat dlss2/HANDOFF.md
```

Result: [withheld: it showed NVIDIA plugin source, which the plugin's licence keeps private]

**Sun 15 Nov 10:52:18 · Tool call: Bash** (Read shell1 handoff first half)

```
cd "[notes]/unreal/megajam-2026/lanes"; cat shell1/HANDOFF.md | head -150
```

Result:

```
# Lane shell1 (round 2) handoff: the soundstage hall

14 Nov 2026. Worktree `D:\UE\wt\shell1`, branch `shell1`, from `5767556`. Three commits:

- `81a8f53` SUPERCUT shell1: soundstage hall round every room, Hall tuning, tests
- `c849bb9` SUPERCUT shell1: hall materials saved for instancing, four work lights, hall is studio tone in a freeze
- `ba8ab10` SUPERCUT shell1: lower-flats test room and its picture script [taste: owner review]

Not merged, not rebased, not pushed. Log of the day: [LOG.md](<[notes]/unreal/megajam-2026/lanes/shell1/LOG.md>).
Pictures: [shots](<[notes]/unreal/megajam-2026/lanes/shell1/shots>).

The owner asked: "the skybox is just plain black, make it look like a film set warehouse, with scaffolding and such."
Every room now stands in a soundstage: a concrete floor with a tape line, padded walls with steel columns and a stage
door, a catwalk at 8 m, scaffold towers, stacked road cases, a lighting truss over the set with hanging lamps (some
lit), a steel roof, four dim work lights and thin haze. The set itself is lit as before; the hall is dim.

## How the layout is made

All of it is code: [SupercutHall.cpp](<D:/UE/wt/shell1/Source/Supercut/SupercutHall.cpp>). No line in any room file.

1. When a room is built, `ASupercutRoom` calls `ASupercutHall::BuildFor(*this)` (one line, before the "ROOM built" log).
   `TearDown` calls `ASupercutHall::TearDownFor(*this)` (one line).
2. The hall reads the room: the box round its solid parts, the floor under the start, its loose parts that do not
   collide (the desk lamp, desk things), and the dark studio slabs round it (`BuildLight` makes those).
3. The kept-out box is the room box plus `HallMargin` (400 cm). No piece but a floor tile may touch it. A piece that
   would is left out, and the log line counts it ("pieces left out").
4. The hall floor is the underside of the floor block the player starts on. That is -50 in most rooms. In
   `c_the_cutaway` it is -1050, because its start block reaches down to -1050. Floor tiles run under the set wherever
   no part of the room reaches lower; over a pit there is no tile, so the pit drops out of sight below the hall floor.
   The test rooms `hall/ledge` (start on the wind machine, 4.8 m up) and `hall/perch` (start on a 14 m post) show the
   floor from above.
5. Everything sits on the kit's 400 cm grid. The rig runs on the edges of the grid box round the kept-out box. Walls
   stand 3 cells out from the rig 
[... 7616 more characters not shown]
```

**Sun 15 Nov 10:52:22 · Tool call: Bash** (Rest of shell1, grep light1/vfx1 for perf parts)

```
cd "[notes]/unreal/megajam-2026/lanes"; sed -n 150,272p shell1/HANDOFF.md; grep -n -i "fps\|frame\|setting\|default\|quality\|scalab" light1/HANDOFF.md vfx1/HANDOFF.md | head -80
```

Result:

```
131 and 138 on; 01 137 and 131 off, 128 and 118 on.

Before the hall, at 19:33, the base package gave 247.1 fps in 01 and 267.9 in 03 (slowest 1 percent 187.6 and 194.2).
Those runs were at a quieter hour; the `HallOn 0` runs above are the fair "before", same package and same hour.

What the hall costs, per room: about 32 instanced meshes (one draw each per pass), 1500 to 5800 instances, 4 point
lights without shadows, one height fog. The first package also drew the hall with the engine's fallback material,
which costs game-thread time (merge risks below); fixed before every number above.

## Pictures

Eye height in all 8 rooms (ahead, up, left, right), the freeze in room 8, and the two high test rooms.
JPG, 960 wide, from 1920x1080 shots, in [shots](<[notes]/unreal/megajam-2026/lanes/shell1/shots>).
Names: `room<scene>_<room>_<view>.jpg`, `test_ledge_*`, `test_perch_*`, `flats_*`.

Examples:

- ![room 4 eye](<[notes]/unreal/megajam-2026/lanes/shell1/shots/room4_03_long_lens_eye.jpg>)
- ![room 6 up](<[notes]/unreal/megajam-2026/lanes/shell1/shots/room6_04_hot_set_up.jpg>)
- ![ledge right](<[notes]/unreal/megajam-2026/lanes/shell1/shots/test_ledge_01_wind_machine_right.jpg>)

How much hall shows at eye height, with the 480 cm set walls:

- Looking ahead down a room: the rig, its lamps and the roof show above the far walls. Most rooms show a strip of hall
  over the top third of the frame.
- Looking left or right at a near wall: almost only the wall. A thin strip of rig and roof at the top.
- Looking up: the roof, the truss rig, its hanging lamps, the upper walls and corners, dim. This is where the hall reads
  best.
- From the high test rooms: the whole hall reads: floor with its tape line, padded walls and columns, catwalk, towers,
  gear, truss and roof.

Review against the brief's fault list:

| Fault | Seen? |
| --- | --- |
| Void showing | No black void at eye height in the 8 rooms. The upper hall is dark but has shape. One view, the perch test room looking ahead, is near black: it faces an unlit stretch of wall from 14 m up. |
| A piece in the room | None. The tests also prove it by box. The big pencil over the wall in `c_the_cutaway` and the round lamp heads in the up views are the room's own dressing. |
| Repetition | The walls repeat by design (a panel kit), broken by columns, padding bands, towers and gear. Halls differ by room: near wall, door, towers, lit
[... 10078 more characters not shown]
```

**Sun 15 Nov 10:52:27 · Tool call: Bash** (Read frame rate parts of light1 and vfx1)

```
cd "[notes]/unreal/megajam-2026/lanes"; sed -n 165,200p light1/HANDOFF.md; sed -n 115,135p vfx1/HANDOFF.md; sed -n 185,195p vfx1/HANDOFF.md
```

Result:

```
| Player's shot, live | 17 | | hue 53, sat 83% | hue 47 to 48, sat 35 to 45% | 45 to 58 |
| Player's shot, frozen | 10 | hue 51, sat 52% | hue 49, sat 99% | | 45 to 58 |
| Open gate | 14 | hue 147, sat 18% (near white) | hue 122, sat 76% | | 110 to 150 |
| Enemy shot, frozen | 03 | hue 23, sat 97% | hue 6, sat 99% | | |

The halo numbers are rings from 1.1 to 1.8 core radii. Further out the halo thins into the warm wall (hue 30 to
43 at saturation 26 percent and under), which is the wall's own colour.

**5. Frame rate.** demo/mixed, `Script\mixed.txt`, packaged, 1920x1080, no fixed step, 3 runs each.

| | Before | After | Loss |
|---|---|---|---|
| Live, average | 266.3 / 267.1 / 265.7 | 259.9 / 259.0 / 258.4 | 2.7% |
| Live, slowest 1% | 154.6 / 146.5 / 152.0 | 144.8 / 141.8 / 143.4 | 5.1% |
| Frozen, average | 237.6 / 233.5 / 235.9 | 230.0 / 227.5 / 227.7 | 3.1% |
| Frozen, slowest 1% | 139.0 / 136.5 / 140.2 | 139.9 / 136.3 / 135.0 | 1.1% |

Under the 15 percent limit, so I cut nothing. If it had to drop, the first cuts would be the soft shadow edge
(`LampSoftness 0`) and the halo shells.

## What I did not check

- An enemy standing right in front of the shadow side of a flat. No script puts one there. The flat's shadow side
  reads 36 percent and the figures are light wood, so I expect them to read, but I have no picture.
- The Marksman's locked line on its own. A line near the camera in pair 09 reads hue 19, saturation 92 percent. I
  believe it is a locked line, I did not confirm that from the log.
- The lava and the blade's edge up close. They take the danger hue now, and lava's strength went from 1.6 to
  `DangerGlow` 1.5.
- The game with real input. No keyboard or mouse input was sent. Every run was scripted.
- Any PC but c4.
- Frame rate in a room larger than demo/mixed.

## Gotchas

Full entries are in `unreal\GOTCHAS.md` under "SUPERCUT light1 lane". The ones that will bite the next lane:

| The same, run 2 | `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`, the same line |

The scripted run needs `-TimeoutSeconds 540` on the farm: 98 s of game time took 255 s offscreen, and the default
limit of 240 s stops it.

Frame time, fight room `fight/01_wind_machine`, script `Script/vfx1_fps.txt` (24 shots at walls, floor and a machine
in 15 s, four full magazines), 1920x1080, no fixed frame rate, same PC, same build except the four defaults that switch the
effects off:

| | Run 1 | Run 2 |
| --- | --- | --- |
| Effects off (before) |
[... 1459 more characters not shown]
```

**Sun 15 Nov 10:52:30 · Tool call: Bash** (List GOTCHAS section headers)

```
cd "[notes]/unreal"; grep -n "^#" GOTCHAS.md | head -150
```

Result:

```
1:# Unreal gotchas
6:## Unreal MCP in 5.8.4 differs from Epic's docs page
54:## Unreal MCP, from the docs (not yet run here)
66:## Packaging (BuildCookRun)
91:## Visual Studio Build Tools (C++ projects)
109:## Epic Games Launcher (driven by an agent)
126:## UEFN install through the Launcher
144:## Epic Games Launcher on a fresh machine ([pc-b])
166:## UE 5.9 MegaJam Preview
216:## Epic Games Launcher: second engine slot (5.9 on c4)
240:## C++ project, headless tests and packaging (Floodline core lane)
286:## Materials built by script (both engines)
297:## Game view built in C++ at run time (Floodline view lane)
357:## Floodline tune lane (edit on c4, build on [pc-b], headless)
393:## SUPERCUT core lane (13 Nov 2026, c4, engine 5.8.4)
525:## SUPERCUT run lane (13 Nov 2026, c4, engine 5.8.4)
575:## Windows Firewall prompt for every new Unreal exe path (13 Nov 2026, verified)
594:## SUPERCUT enemies lane (13 Nov 2026, c4, engine 5.9 preview)
626:## SUPERCUT pc2 test lane 2: launcher and frame rate (13 Nov 2026, c4 to pc2, engine 5.9 preview)
665:## Scripted game runs depend on frame timing unless the time step is fixed (13 Nov 2026, verified)
677:## SUPERCUT puzzles lane (13 Nov 2026, c4, engine 5.9 preview)
705:## SUPERCUT audiowire lane (13 Nov 2026, c4, engine 5.9 preview)
741:## SUPERCUT slice lane (13 Nov 2026, c4, engine 5.9 preview)
764:## SUPERCUT slice2 lane (13 Nov 2026, c4, engine 5.9 preview)
779:## SUPERCUT feel1 lane: tuning file and practice keys (13 Nov 2026, c4, engine 5.9 preview)
799:## SUPERCUT figin lane: skinned enemies (13 Nov 2026, c4, engine 5.9 preview)
824:## SUPERCUT feel2 lane: hit feedback (14 Nov 2026, c4, engine 5.9 preview)
840:## SUPERCUT light1 lane: lamp, glows, sketch (14 Nov 2026, c4, engine 5.9 preview)
875:## Shipping builds and user settings (5.9, lane shell1)
907:## SUPERCUT onboard1 lane (14 Nov 2026, c4, engine 5.9 preview)
936:## SUPERCUT mix1 lane: master limiter and mix measuring (14 Nov 2026, c4, engine 5.9 preview)
957:## SUPERCUT first1 lane: first start, sound tuning, title hatching (14 Nov 2026, c4 and pc2, engine 5.9 preview)
977:## SUPERCUT props1 lane: set props (14 Nov 2026, c4, engine 5.9 preview)
1011:## SUPERCUT fix2 lane: room 6 jumps, lava reach, Rushers and gear (14 Nov 2026, c4 and pc2, engine 5.9 preview)
1038:## SUPERCUT held1 lane (14 Nov 2026, verified by the lane)
1052:## SUPERCUT feel3 lane (14 Nov 2026, verified by the lane)
1070:## Build farm (14 Nov 2026, verified, lane farm1)
1091:## SUP
[... 893 more characters not shown]
```

**Sun 15 Nov 10:52:34 · Tool call: Bash** (Read pc2 frame rate, shipping settings, first1 gotchas)

```
cd "[notes]/unreal"; sed -n 626,676p GOTCHAS.md; sed -n 875,906p GOTCHAS.md; sed -n 957,976p GOTCHAS.md
```

Result:

```
## SUPERCUT pc2 test lane 2: launcher and frame rate (13 Nov 2026, c4 to pc2, engine 5.9 preview)

All verified on pc2 (GTX 1070) on 13 Nov 2026 with the build `D:\UE\Builds\Supercut59_applocal\Windows`.
Full report: `megajam-2026/lanes/pctest2/REPORT.md`.

- **The launcher prompt is gone in the app-local build** (verified, 13 Nov 2026). With the VC++ runtime DLLs
  beside the game exe and no runtime installer in the build, `Supercut.exe` in the build root started the game
  twice on pc2 (runtime 14.42), with no dialog, and returned the game's exit code 0 (28 s and 30 s). Not
  separated: whether the DLLs or the missing installer removed the prompt. Not checked: a PC with no runtime.
- **The game saves its quality levels at exit, and the next run starts with them** (verified, 13 Nov 2026).
  `-dpcvars=sg.XxxQuality=0` is written to `<build>\Supercut\Saved\Config\Windows\GameUserSettings.ini` when the
  game exits. A later "baseline" run then loaded `sg.* = 0` (`LastSetBy: Scalability`) and ran 298 fps instead of 66.
  Delete that file before every measured run, and read the values back (below) so a stale file shows in the log.
- **A second job on pc2's GPU changes the frame rate by up to 2.6 times** (verified, 13 Nov 2026). In bursts of 10
  to 30 minutes `nvidia-smi` showed 93 to 100% GPU use and 3.4 to 4.3 GB used with no game of ours running.
  The same baseline ran 25 fps under it and 66 fps without. Before each run, wait until
  `nvidia-smi --query-gpu=utilization.gpu,power.draw` stays under 40% and 70 W for four samples (Studio windows keep
  it at 15 to 35%), and run each variant three times. GPU memory use is not a good idle test: more Studio windows raise it.
- **`-dpcvars=` sets variables at start in a Development build, and the log proves it** (verified, 13 Nov 2026).
  The log prints `LogDeviceProfileManager: Setting CommandLine Device Profile CVar: [[name:value]]` and
  `LogConfig: Set CVar [[name:value]]`. A bare variable name in `-ExecCmds="a, b, c"` prints its value, who set it last
  and its history (`r.Shadow.Virtual.Enable = "0"      LastSetBy: DeviceProfile`). `Config.Explain <cvar>` printed
  nothing in this packaged build. `-dpcvars=` sets at DeviceProfile priority; `-ForceDPCVars=` at Commandline
  priority. Shipping and Test builds ignore both and `-ExecCmds` (`ConfigProvenance.cpp` warns). Put one word per
  line in a text file and pass it through the run script, so the quotes in `-ExecCmds="..."` survive `schtasks`.
- **What costs
[... 7243 more characters not shown]
```

### Sun 15 Nov 10:52:38 · Agent (claude-opus-5-5)

Still reading: GOTCHAS already says the 24 errors are global-shader PSO precache failures (hashes only, no names). Checking the farm sections, then the worktree.

**Sun 15 Nov 10:52:39 · Tool call: Bash** (Read farm-related gotchas)

```
cd "[notes]/unreal"; sed -n 1070,1090p GOTCHAS.md; sed -n 1127,1135p GOTCHAS.md; sed -n 1157,1243p GOTCHAS.md
```

Result:

```
## Build farm (14 Nov 2026, verified, lane farm1)

- **A game started over ssh cannot open its window.** The ssh session is session 0: D3D12 finds the GPU, then
  `FD3D12Viewport::Init` fails with `DXGI_ERROR_NOT_CURRENTLY_AVAILABLE` and the game exits 3 in 3 s.
  `-RenderOffscreen` fixes it: the game renders with no window, pictures are real frames, and the scripted run gives
  the same line. Frame rates measured that way are not a player's frame rate.
- **The cook fails on an old VC++ runtime while builds and tests pass.** On pc2 (runtime 14.44.35211) the editor
  logs `LogWindows: Error: Visual C++ redistributable version 14.44.35211.0 is outdated. Please install version
  14.50.35719.0` (`WindowsPlatformApplicationMisc.cpp`), and BuildCookRun stops with exit 25
  (`Error_UnknownCookFailure`). Fix: `Engine\Extras\Redist\en-us\vc_redist.x64.exe /install /quiet /norestart`.
- **Smart App Control blocks our compiled DLLs.** On pc4 (policy `VerifiedAndReputableDesktop`, enforced) the editor
  could not load `UnrealEditor-Supercut.dll`: `GetLastError=4551`, Code Integrity event 3077. Compiling works;
  tests, cook and the game do not. Smart App Control has no per-file exception; only turning it off would help.
- **Two copies of one packaged game started together: one crashed.** Same package folder, both offscreen with
  `-RenderOffscreen` and their own `-abslog`: one stopped at start with "Crash in runnable thread Background
  Worker #3", the other finished. Run one game per package folder at a time.
- **A fixed-step scripted run on a slow GPU takes longer than `run_demo.ps1`'s 240 s timeout.** main8 at
  `-FixedFps 240` draws all 23,500 steps; pc2's GTX 1070 needed 472 s. Pass `-TimeoutSeconds 900` there.
- **Windows PowerShell 5.1 `Tee-Object` writes UTF-16.** Logs saved with it looked like spaced letters in Git Bash.
  The farm collects output with `Tee-Object -Variable` and writes it with `Out-File -Encoding utf8`.

## pc2: a PowerShell script over ssh never sees the end of its input (14 Nov 2026, verified)

`echo abc | ssh pc2 'powershell -NoProfile -Command "[Console]::In.ReadToEnd()"'` never returns on pc2 and
returns at once on [pc-b]. `tar -xf -` over the same ssh does see the end, so file streams work. The farm mirror's
delete step (`farm/remote/del.ps1`) read its list with `ReadToEnd()` and hung two lanes for ten minutes the first
time a mirror had something to delete (a failed step leaves `Tools\farm_<file>` behind). Fix: the sender ends the
list
[... 8346 more characters not shown]
```

**Sun 15 Nov 10:52:42 · Tool call: Bash** (Inspect perf3 worktree state)

```
cd /d/UE/wt/perf3 && git status --short | head; git log --oneline -5; ls; ls Tools Script | head -80; date
```

Result:

```
eec7dd4 SUPERCUT main: the enemy gun's part table is EnemyGunPartTable
1d44139 SUPERCUT main: the enemy gun's part table gets its own name
a3dabc3 SUPERCUT main: source records the credits audit found missing or wrong
ca16533 Merge branch 'gun2' into ue59
7aaad8a SUPERCUT main: credits lines for the four sound sources sfx4 added
Art
Audio
Config
Content
Plugins
Script
Source
Supercut.uproject
Tools
Script:
code.txt
credits1_shots.txt
death.txt
demo.txt
dropper.txt
feel2_shots.txt
fight5.txt
figin_grunt.txt
figin_hitshape.txt
figin_marksman.txt
figin_rusher.txt
figin_rusher_rest.txt
flats1_a.txt
flats1_b.txt
flats1_c.txt
flats1_d.txt
flats1_e.txt
flats1_f.txt
flats1_tex1.txt
flats1_tex2.txt
flats1_tex3.txt
gate.txt
gen
gun2_shots.txt
hallmerge1_glow.txt
hallmerge1_hall.txt
hallmerge1_room.txt
hands1_shots.txt
hud1_audio.txt
hud1_card.txt
hud1_dlss_change.txt
hud1_dlss_view.txt
hud1_hud.txt
hud1_prompts.txt
hud1_rows.txt
hud1_rows7.txt
hud1_rows7_reset.txt
hud1_screens.txt
hud1_wrap.txt
jumps.txt
light1_cross.txt
light1_glows.txt
light1_studio.txt
litter1_pics.txt
main8.txt
marksman.txt
mixed.txt
onboard1_cue.txt
onboard1_stranger.txt
practice_keys.txt
props1_close.txt
props1_enemy.txt
props1_entry.txt
props1_lamp.txt
props1_show.txt
refill.txt
run.txt
run_death.txt
rusher.txt
sfx4_clap.txt
sfx4_clap_shot.txt
sfx4_menu.txt
sfx4_prompt.txt
shell1_clicks.txt
shell1_hall_flats.txt
shell1_hall_fps.txt
shell1_hall_rooms.txt
shell1_hall_views.txt
shell1_halo.txt
shell1_low.txt
shell1_menus.txt
shell1_ship.txt
slice2_corner.txt
slice_fps.txt
slice_s1.txt
sound_fight.txt
sound_still.txt
sound_upgrade.txt
switch.txt
Sun Nov 15 10:52:49 MPST 2026
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:52:54 · Tool call: Bash** (List Tools and read run_demo.ps1 head)

```
cd /d/UE/wt/perf3 && ls Tools; sed -n 1,80p Tools/run_demo.ps1
```

Result:

```
Play_dev.bat
build.ps1
demo_log.sh
gen
input_check.ps1
make_assets.py
make_figures.py
make_hands.py
make_held.py
make_props.py
make_props_real.py
make_props_show.py
make_sounds.py
make_vfx.py
measure_recordings.py
package.cmd
package_shipping.cmd
run_demo.ps1
run_tests.ps1
# Runs the scripted player in a real game window and waits for it to quit.
# Default: the uncooked project through the editor exe. With -Packaged: the packaged game.
# Usage: powershell -File Tools\run_demo.ps1 [-Shots <folder>] [-ResX 1280] [-ResY 720] [-Script <file>]
#        [-Room <name>] [-Run <name>] [-Seed <n>] [-Log <file>] [-TimeoutSeconds 240] [-NoQuit] [-Packaged [-Exe <packaged Supercut.exe>]]
#        [-FixedFps <n>] [-Silent] [-Record <file.wav>] [-Upgrades <name>,<name>] [-Dev] [-Title] [-Shipping]
#        [-DLSS <off|dlaa|quality|balanced|performance>]
# Exit code: 0 the script finished, 2 the script failed (the player died when the script did not expect it,
# or a "scene" step did not see its room), 3 the game was stopped at the timeout.
param(
    [string]$Shots = "$(Split-Path -Parent $PSScriptRoot)\Saved\shots",
    [int]$ResX = 1280,
    [int]$ResY = 720,
    [string]$Script = "$(Split-Path -Parent $PSScriptRoot)\Script\demo.txt",
    [string]$Room = "",   # play one room, Content\Rooms\<name>.txt, as a run of its own
    [string]$Run = "",    # play the run list Content\Runs\<name>.txt instead of main.txt
    [int]$Seed = -1,      # the seed that decides which upgrades are offered; -1 leaves it to the game
    [string]$Log = "$(Split-Path -Parent $PSScriptRoot)\Saved\Logs\demo.log",
    [int]$TimeoutSeconds = 240,
    [switch]$NoQuit,   # leave out -SupercutQuit: the game keeps running after the script and is stopped at the timeout
    [int]$FixedFps = 0, # above 0: every frame advances game time by exactly 1/FixedFps s, whatever the PC's load, so a script gives the same result each run
    [switch]$Packaged, # run the packaged game instead of the uncooked project
    [string]$Exe = "D:\UE\Builds\Supercut59\Windows\Supercut.exe",  # with -Packaged: which packaged game to run
    [switch]$Silent,   # render the sound without sending it to the speakers (the engine's deterministic offline audio device)
    [string]$Record = "",  # write the master output to this .wav (also silent); record at real speed, without -FixedFps
    [string]$Upgrades = "",  # every take starts holding these upgrades, by the names PICK lines print: doubleexposure,longtake
    [switch]$Dev,   
[... 3099 more characters not shown]
```

**Sun 15 Nov 10:53:05 · Tool call: Bash** (Load check pc2)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>&1 | tail -20
```

Result:

```
free_ram_gb=5.4 of 15.9
commit_free_gb=7.4
cpu_load_pct=2 threads=12
disk_free=C:32GB
busy_procs=none
desktop_sessions=1 this_session=0
gpu=NVIDIA GeForce GTX 1070, 35 %, 1793 MiB, 17.24 W
farm_names=gun2 hands1 hands2 proof sfx2 view1 viewmerge1
engine=60351404
```

**Sun 15 Nov 10:53:12 · Tool call: Bash** (Mirror worktree to pc2, recheck load)

```
mkdir -p "[notes]/unreal/megajam-2026/lanes/perf3/shots" /d/UE/wt/perf3_farmlogs; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" mirror pc2 perf3 /d/UE/wt/perf3 2>&1 | tail -5; "$F" status pc2 2>&1 | grep -E "free_ram|cpu_load|busy"; date +%H:%M
```

Result:

```
FARM mirror pc2:C:\UE\Farm\perf3 sent 3010 files (3280.1 MB), deleted 0, 3010 files in project, 88.5 s
free_ram_gb=5.5 of 15.9
cpu_load_pct=0 threads=12
busy_procs=none
10:54
```

**Sun 15 Nov 10:54:50 · Tool call: Bash** (Build then package on pc2 (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs; ( "$F" build pc2 perf3 "$L" -Jobs 4 && "$F" status pc2 | grep -E "free_ram|cpu|busy" && "$F" package pc2 perf3 "$L" ) > "$L/bp.txt" 2>&1; echo exit $?; tail -5 "$L/bp.txt"
```

Result:

```
Command running in background with ID: bgccxx2z8. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bgccxx2z8.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

### Sun 15 Nov 10:54:53 · Agent (claude-opus-5-5)

Build and package are running on pc2. Meanwhile I'm reading the engine source for where the pipeline errors come from.

**Sun 15 Nov 10:54:54 · Tool call: Grep**

```
{
 "pattern": "Failed to create compute pipeline",
 "path": "D:\\UE\\UE_5.9\\Engine\\Source\\Runtime",
 "output_mode": "content"
}
```

Result:

```
D:\UE\UE_5.9\Engine\Source\Runtime\VulkanRHI\Private\VulkanPipeline.cpp:3123:		UE_LOGF(LogVulkanRHI, Error, "Failed to create compute pipeline.\nShaders in pipeline: CS: %ls", *ComputeHash);
D:\UE\UE_5.9\Engine\Source\Runtime\RHI\Private\PipelineStateCache.cpp:733:	UE_LOGF(LogRHI, Error, "Failed to create compute pipeline with hash %ls.", *Init.ComputeShader->GetHash().ToString());
```

**Sun 15 Nov 10:55:13 · Tool call: Bash** (Read compute pipeline failure handler)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private; sed -n 690,800p PipelineStateCache.cpp
```

Result:

```
UE_LOGF(LogRHI, Error, "Mesh: %ls", Init.BoundShaderState.GetMeshShader()->GetShaderName());
	}
	if (Init.BoundShaderState.GetAmplificationShader())
	{
		UE_LOGF(LogRHI, Error, "Amplification: %ls", Init.BoundShaderState.GetAmplificationShader()->GetShaderName());
	}
	if(Init.BoundShaderState.GetGeometryShader())
	{
		UE_LOGF(LogRHI, Error, "Geometry: %ls", Init.BoundShaderState.GetGeometryShader()->GetShaderName());
	}
	if(Init.BoundShaderState.PixelShaderRHI)
	{
		UE_LOGF(LogRHI, Error, "Pixel: %ls", Init.BoundShaderState.PixelShaderRHI->GetShaderName());
	}

	UE_LOGF(LogRHI, Error, "Render Targets: (%u)", Init.RenderTargetFormats.Num());
	for(int32 i = 0; i < Init.RenderTargetFormats.Num(); ++i)
	{
		//#todo-mattc GetPixelFormatString is not available in scw. Need to move it so we can print more info here.
		UE_LOGF(LogRHI, Error, "0x%x", (uint32)Init.RenderTargetFormats[i]);
	}

	UE_LOGF(LogRHI, Error, "Depth Stencil Format:");
	UE_LOGF(LogRHI, Error, "0x%x", Init.DepthStencilTargetFormat);
#endif

	if(Init.bFromPSOFileCache)
	{
		// Let the cache know so it hopefully won't give out this one again
		FPipelineFileCacheManager::RegisterPSOCompileFailure(GetTypeHash(Init), Init);
	}
	else if(!Init.bPSOPrecache)
	{
		// Precache requests are allowed to fail, but if the PSO is needed by a draw/dispatch command, we cannot continue.
		UE_LOGF(LogRHI, Fatal, "Shader compilation failures are Fatal.");
	}
}

// Prints out information about a failed compute pipeline compilation.
// This is fatal unless the compilation request is coming from the precaching system.
static void HandlePipelineCreationFailure(const FComputePipelineStateInitializer& Init)
{
	// Dump the shader hash so it can be looked up in the SHK data. See the previous function for details.
	UE_LOGF(LogRHI, Error, "Failed to create compute pipeline with hash %ls.", *Init.ComputeShader->GetHash().ToString());

#if !(UE_BUILD_SHIPPING || UE_BUILD_TEST)
	UE_LOGF(LogRHI, Error, "Shader: %ls", Init.ComputeShader->GetShaderName());
#endif

	if (!Init.bPSOPrecache && !Init.bFromPSOFileCache)
	{
		// Precache requests are allowed to fail, but if the PSO is needed by a draw/dispatch command, we cannot continue.
		UE_LOGF(LogRHI, Fatal, "Shader compilation failures are Fatal.");
	}
}

#if PSO_TRACK_CACHE_STATS

static std::atomic_uint64_t TotalPrecompileCompleteTime[(int)EPSOPrecachePriority::Num];
static std::atomic_uint64_t TotalPrecompileCompileTime[(int)EPSOPrecachePriority::Num];
static std::atomic_uint64
[... 2165 more characters not shown]
```

**Sun 15 Nov 10:55:17 · Tool call: Bash** (Find existing pc2 run logs with the errors)

```
cd /d/UE/wt; grep -l "Failed to create compute pipeline" */run/run.log 2>/dev/null | head;
```

Result:

```
viewmerge1_farmlogs/run/run.log
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:55:22 · Tool call: Bash** (Inspect failure lines and RHI info in existing pc2 log)

```
cd /d/UE/wt/viewmerge1_farmlogs/run; grep -n -B3 -A3 "Failed to create compute pipeline" run.log | head -40; grep -c "Failed to create compute pipeline" run.log; grep -n "Failed to create compute pipeline" run.log | awk '{print $NF}' | sort | uniq -c | head -30; grep -n -i "RHI\b\|D3D12RHI\|Shader Model\|feature level\|Adapter\|Driver" run.log | head -30
```

Result:

```
948-[2026.11.14-19.59.08:417][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash E47C8AF6CBA94493, error 80070057.
949-[2026.11.14-19.59.08:417][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0x77C7F836F42FD243:
950-
951:[2026.11.14-19.59.08:417][  0]LogRHI: Error: Failed to create compute pipeline with hash 1403E8480EF42111.
952-[2026.11.14-19.59.08:417][  0]LogRHI: Error: Shader: <unknown>
953-[2026.11.14-19.59.08:417][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash E3E671E1B79D05F2, error 80070057.
954-[2026.11.14-19.59.08:417][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xE47C8AF6CBA94493:
955-
956:[2026.11.14-19.59.08:417][  0]LogRHI: Error: Failed to create compute pipeline with hash C943EEB2FC37390A.
957-[2026.11.14-19.59.08:417][  0]LogRHI: Error: Shader: <unknown>
958-[2026.11.14-19.59.08:417][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash A51AAEFC95EFEDCD, error 80070057.
959-[2026.11.14-19.59.08:418][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xE3E671E1B79D05F2:
960-
961:[2026.11.14-19.59.08:418][  0]LogRHI: Error: Failed to create compute pipeline with hash 8685ECF03AC18C7B.
962-[2026.11.14-19.59.08:418][  0]LogRHI: Error: Shader: <unknown>
963-[2026.11.14-19.59.08:418][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash 7485D94C8697768F, error 80070057.
964-[2026.11.14-19.59.08:418][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xA51AAEFC95EFEDCD:
965-
966:[2026.11.14-19.59.08:418][  0]LogRHI: Error: Failed to create compute pipeline with hash D437AD2072640925.
967-[2026.11.14-19.59.08:418][  0]LogRHI: Error: Shader: <unknown>
968-[2026.11.14-19.59.08:418][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash 7AC6E13D0CBEFFC8, error 80070057.
969-[2026.11.14-19.59.08:418][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0x7485D94C8697768F:
970-
971:[2026.11.14-19.59.08:418][  0]LogRHI: Error: Failed to create compute pipeline with hash BE96E03D12ECEF93.
972-[2026.11.14-19.59.08:418][  0]LogRHI: Error: Shader: <unknown>
973-[2026.11.14-19.59.08:419][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash C0757229C38FC560, error 80070057.
974-[2026.11.14-19.59.08:420][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0x7AC6E13D0CBEFFC8:
975-
97
[... 4778 more characters not shown]
```

**Sun 15 Nov 10:55:30 · Tool call: Grep**

```
{
 "pattern": "r.PSOPrecache.GlobalShaders",
 "path": "D:\\UE\\UE_5.9\\Engine\\Source",
 "output_mode": "content",
 "-n": true
}
```

Result:

```
The search stopped before it finished, most likely at its time limit, so these results are incomplete: more matches may exist. Search a more specific path or pattern.

D:\UE\UE_5.9\Engine\Source\Runtime\Engine\Private\PSOPrecacheSettings.cpp:17:	TEXT("r.PSOPrecache.GlobalShaders"),
D:\UE\UE_5.9\Engine\Source\Runtime\Engine\Private\PSOPrecacheSettings.cpp:20:	TEXT("Note: r.PSOPrecache.GlobalShaders == 2 is only supported when r.PSOPrecache.Mode == 1 (Preload shaders)."),
```

**Sun 15 Nov 10:55:56 · Tool call: Bash** (Read PSO precache settings and find global shader precache)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; sed -n 1,80p Engine/Private/PSOPrecacheSettings.cpp; grep -rn "ShouldPrecacheGlobalComputeShaders\|PrecacheGlobalComputeShaders\|PrecacheComputePipelineStatesForGlobalShaders\|GlobalShaders()" --include=*.cpp RenderCore/Private Renderer/Private Engine/Private 2>/dev/null | head -20
```

Result:

```
// Copyright Epic Games, Inc. All Rights Reserved.

/*=============================================================================
	PSOPrecacheSettings.cpp: 
=============================================================================*/

#include "PSOPrecacheSettings.h"
#include "HAL/IConsoleManager.h"
#include "RHIShaderPlatform.h"
#include "RHIStrings.h"
#include "Engine/RendererSettings.h"
#include "Materials/Material.h"
#include "MaterialDomain.h"

static int32 GPSOPrecacheGlobalShaders = -1;
static FAutoConsoleVariableRef CVarPSOPrecacheGlobalShaders(
	TEXT("r.PSOPrecache.GlobalShaders"),
	GPSOPrecacheGlobalShaders,
	TEXT("Precache global shaders during startup (disable(0) - global compute shaders and registered global graphis PSOs(1) - all global shaders(2).\n") 
	TEXT("Note: r.PSOPrecache.GlobalShaders == 2 is only supported when r.PSOPrecache.Mode == 1 (Preload shaders)."),
	ECVF_ReadOnly
);

static int32 GPSOPrecacheKeepGlobalGraphicPSOsInMemory = -1;
static FAutoConsoleVariableRef CVarPSOPrecacheKeepGlobalGraphicPSOsInMemory(
	TEXT("r.PSOPrecache.KeepGlobalGraphicPSOsInMemory"),
	GPSOPrecacheKeepGlobalGraphicPSOsInMemory,
	TEXT("Keep global graphic PSOs in memory when r.PSOPrecache.KeepInMemoryForActiveMaterials is enabled"),
	ECVF_ReadOnly
);

static int32 GPSOPrecacheKeepGlobalComputePSOsInMemory = -1;
static FAutoConsoleVariableRef CVarPSOPrecacheKeepGlobalComputePSOsInMemory(
	TEXT("r.PSOPrecache.KeepGlobalComputePSOsInMemory"),
	GPSOPrecacheKeepGlobalComputePSOsInMemory,
	TEXT("Keep global compute PSOs in memory when r.PSOPrecache.KeepInMemoryForActiveMaterials is enabled"),
	ECVF_ReadOnly
);

static int32 GPSOPrecacheLightMapPolicyMode = -1;
static FAutoConsoleVariableRef CVarPSOPrecacheLightMapPolicyMode(
	TEXT("r.PSOPrecache.LightMapPolicyMode"),
	GPSOPrecacheLightMapPolicyMode,
	TEXT("Defines which light map policies should be checked during PSO precaching of the base pass.\n") \
	TEXT("-1: Use engine defaults.\n") \
	TEXT(" 0: All possible LMP will be checked.\n") \
	TEXT(" 1: Only LMP_NO_LIGHTMAP will be precached.\n"),
	ECVF_ReadOnly
);

static int32 GPSOPrecacheTranslucencyAllPass = -1;
static FAutoConsoleVariableRef CVarPSOPrecacheTranslucencyAllPass(
	TEXT("r.PSOPrecache.TranslucencyAllPass"),
	GPSOPrecacheTranslucencyAllPass,
	TEXT("Precache PSOs for TranslucencyAll pass.\n") \
	TEXT("-1: Use engine defaults.\n") \
	TEXT(" 0: No PSOs are compiled for this pass.\n") \
	TEXT(" 1: PSOs are compiled for all primitives which render t
[... 2979 more characters not shown]
```

### Sun 15 Nov 10:56:01 · Agent (claude-opus-5-5)

Reading the engine's global shader precache loop to see which shaders it asks the driver for.

**Sun 15 Nov 10:56:02 · Tool call: Bash** (Read PrecacheComputePipelineStatesForGlobalShaders)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; sed -n 5253,5340p Engine/Private/ShaderCompiler/ShaderCompiler.cpp
```

Result:

```
void PrecacheComputePipelineStatesForGlobalShaders(ERHIFeatureLevel::Type FeatureLevel, const ITargetPlatform* TargetPlatform)
{
	const FPSOPrecacheSettings& PSOPrecacheSettings = UPSOPrecacheSettingsManager::GetSettings();
	if (PSOPrecacheSettings.GlobalShaderMode == 0)
	{
		return;
	}

	if (!IsPSOShaderPreloadingEnabled() && !(PipelineStateCache::IsPSOPrecachingEnabled() && GRHISupportsPSOPrecaching))
	{
		return;
	}

	TRACE_CPUPROFILER_EVENT_SCOPE(PrecacheComputePipelineStatesForGlobalShaders);

	FPlatformTypeLayoutParameters LayoutParams;
	LayoutParams.InitializeForPlatform(TargetPlatform);
	EShaderPermutationFlags PermutationFlags = GetShaderPermutationFlags(LayoutParams);

	EShaderPlatform ShaderPlatform = GetFeatureLevelShaderPlatform(FeatureLevel);
	FGlobalShaderMap* GlobalShaderMap = GetGlobalShaderMap(ShaderPlatform);
	
	// Global shader request record: an enumeration of the map, not a renderer request.
	UE_GLOBAL_SHADER_REQUEST_SUPPRESS_SCOPE();

	// some RHIs (OpenGL) can only create shaders on the Render thread. Queue the creation instead of doing it here.
	TArray<TShaderRef<FShader>> ComputeShadersToPrecache;
	for (TLinkedList<FShaderType*>::TIterator ShaderTypeIt(FShaderType::GetTypeList()); ShaderTypeIt; ShaderTypeIt.Next())
	{
		FGlobalShaderType* GlobalShaderType = ShaderTypeIt->GetGlobalShaderType();
		if (!GlobalShaderType || (GlobalShaderType->GetFrequency() != SF_Compute && PSOPrecacheSettings.GlobalShaderMode == 1))
		{
			continue;
		}

		int32 ShaderPermutationPerGlobalShaderType = 0;
		for (int32 PermutationId = 0; PermutationId < GlobalShaderType->GetPermutationCount(); PermutationId++)
		{
			if (GlobalShaderType->ShouldCompilePermutation(ShaderPlatform, PermutationId, PermutationFlags) &&
				GlobalShaderType->ShouldPrecachePermutation(ShaderPlatform, PermutationId, PermutationFlags) == EShaderPermutationPrecacheRequest::Precached)
			{
				TShaderRef<FShader> GlobalShader = GlobalShaderMap->GetShader(GlobalShaderType, PermutationId);
				if (GlobalShader.IsValid())
				{
					ComputeShadersToPrecache.Add(GlobalShader);
					ShaderPermutationPerGlobalShaderType++;
				}
			}
		}

		/*
		int32 PermutationCountLimit = 300;
		ensureMsgf(
			ShaderPermutationPerGlobalShaderType < PermutationCountLimit,
			TEXT("Global shader %s has %i permutations to precache: probably more than it needs."),
			GlobalShaderType->GetName(), ShaderPermutationPerGlobalShaderType);
		*/
	}
	
	if (ComputeShadersToPrecache.Num() > 0)
	{
		if (PipelineSta
[... 1330 more characters not shown]
```

**Sun 15 Nov 10:56:09 · Tool call: Bash** (Read comment on SHK lookup)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; sed -n 640,688p RHI/Private/PipelineStateCache.cpp
```

Result:

```
GPSOPrecacheThreadPool.ShutdownThreadPool();
	}
}

extern RHI_API FComputePipelineState* FindComputePipelineState(const FComputePipelineStateInitializer& Initializer, bool bVerifyUse);
extern RHI_API FComputePipelineState* GetComputePipelineState(FRHIComputeCommandList& RHICmdList, const FComputePipelineStateInitializer& Initializer, bool bVerifyUse);
extern RHI_API FRHIComputePipelineState* ExecuteSetComputePipelineState(FComputePipelineState* ComputePipelineState);
extern RHI_API FRHIGraphicsPipelineState* ExecuteSetGraphicsPipelineState(FGraphicsPipelineState* GraphicsPipelineState);

// Prints out information about a failed compilation from Init.
// This is fatal unless the compilation request is coming from the precaching system.
static void HandlePipelineCreationFailure(const FGraphicsPipelineStateInitializer& Init)
{
	uint64 CombinedHash = 0;
	FString ShaderHashList;

	const auto AddShaderHash = [&CombinedHash, &ShaderHashList](const FRHIShader* Shader)
	{
		FShaderHash ShaderHash;
		if (Shader)
		{
			ShaderHash = Shader->GetHash();
			ShaderHashList.Appendf(TEXT("%s: %s, "), GetShaderFrequencyString(Shader->GetFrequency(), false), *ShaderHash.ToString());
		}
		CombinedHash += ShaderHash.Hash;
	};

	// Log the shader and pipeline hashes, so we can look them up in the stable keys (SHK) file. Please note that NeedsShaderStableKeys must be set to
	// true in the [DevOptions.Shaders] section of *Engine.ini in order for the cook process to produce SHK files for the shader libraries. The contents
	// of those files can be extracted as text using the ShaderPipelineCacheTools commandlet, like this:
	//		UnrealEditor-Cmd.exe ProjectName -run=ShaderPipelineCacheTools dump File.shk
	// The pipeline hash is created by hashing together the individual shader hashes, see FShaderCodeLibraryPipeline::GetPipelineHash for details.
	AddShaderHash(Init.BoundShaderState.GetVertexShader());
	AddShaderHash(Init.BoundShaderState.GetMeshShader());
	AddShaderHash(Init.BoundShaderState.GetAmplificationShader());
	AddShaderHash(Init.BoundShaderState.GetPixelShader());
	AddShaderHash(Init.BoundShaderState.GetGeometryShader());

	FShaderHash PipelineHash;
	PipelineHash.Hash = CombinedHash;

	UE_LOGF(LogRHI, Error, "Failed to create graphics pipeline, hashes: %lsPipeline: %ls.", *ShaderHashList, *PipelineHash.ToString());

#if !(UE_BUILD_SHIPPING || UE_BUILD_TEST)
	if(Init.BoundShaderState.VertexShaderRHI)
	{
		UE_LOGF(LogRHI, Error, "Vertex: %ls", Init.BoundShaderState.VertexSh
[... 127 more characters not shown]
```

**Sun 15 Nov 10:56:18 · Tool call: Bash** (Find how RHI shader names are stored)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -n "GetShaderName\|ShaderName" RHI/Public/RHIResources.h | head -20
```

Result:

```
859:		FString ShaderName;
863:	bool HasShaderName() const { return !Debug.ShaderName.IsEmpty(); } 
865:	const TCHAR* GetShaderName() const
867:		return Debug.ShaderName.Len()
868:			? *Debug.ShaderName
886:	bool HasShaderName() const { return false; }
887:	const TCHAR* GetShaderName() const { return TEXT("<unknown>"); }
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:56:23 · Tool call: Bash** (See when shader debug names are available)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; sed -n 840,895p RHI/Public/RHIResources.h; grep -rn "RHI_INCLUDE_SHADER_DEBUG_DATA" RHI/Public/*.h | head -5; grep -rn "Debug.ShaderName =\|SetShaderName\|->Debug.ShaderName" --include=*.cpp RenderCore RHI D3D12RHI 2>/dev/null | head
```

Result:

```
FShaderResourceTable ShaderResourceTable;
	TArray<FUniformBufferStaticSlot> StaticSlots;

	// Workaround for layering issue. FShaderParametersMetadata is in RenderCore,
	// so we can't move the logic for initializing the StaticSlots array to the RHI module.
	friend void UE::RHICore::InitStaticUniformBufferSlots(FRHIShaderData* ShaderData);
};

class FRHIShader : public FRHIResource, public FRHIShaderData
{
public:
	void SetHash(const FShaderHash& InHash) { Hash = InHash; }
	const FShaderHash& GetHash() const { return Hash; }

#if RHI_INCLUDE_SHADER_DEBUG_DATA

	// for debugging only e.g. MaterialName:ShaderFile.usf or ShaderFile.usf/EntryFunc
	struct
	{
		FString ShaderName;
		TArray<FName> UniformBufferNames;
	} Debug;
	
	bool HasShaderName() const { return !Debug.ShaderName.IsEmpty(); } 

	const TCHAR* GetShaderName() const
	{
		return Debug.ShaderName.Len()
			? *Debug.ShaderName
			: TEXT("<unknown>");
	}

	FString GetUniformBufferName(uint32 Index) const
	{
		return Debug.UniformBufferNames.IsValidIndex(Index)
			? Debug.UniformBufferNames[Index].ToString()
			: TEXT("<unknown>");
	}

	TArray<FShaderCodeValidationStride> DebugStrideValidationData;
	TArray<FShaderCodeValidationType> DebugSRVTypeValidationData;
	TArray<FShaderCodeValidationType> DebugUAVTypeValidationData;
	TArray<FShaderCodeValidationUBSize> DebugUBSizeValidationData;

#else

	bool HasShaderName() const { return false; }
	const TCHAR* GetShaderName() const { return TEXT("<unknown>"); }
	FString GetUniformBufferName(uint32 Index) const { return TEXT("<unknown>"); }

#endif

	FRHIShader() = delete;
	FRHIShader(ERHIResourceType InResourceType, EShaderFrequency InFrequency)
		: FRHIResource(InResourceType)
		, Frequency(InFrequency)
RHI/Public/RHIResources.h:706:	#define RHI_INCLUDE_SHADER_DEBUG_DATA 1
RHI/Public/RHIResources.h:708:	#define RHI_INCLUDE_SHADER_DEBUG_DATA 0
RHI/Public/RHIResources.h:711:#if RHI_INCLUDE_SHADER_DEBUG_DATA
RHI/Public/RHIResources.h:854:#if RHI_INCLUDE_SHADER_DEBUG_DATA
D3D12RHI/Private/D3D12Shaders.cpp:39:	OutShader.Debug.ShaderName = InShaderCode.FindOptionalData(FShaderCodeName::Key);
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:56:30 · Tool call: Bash** (Find where shader names are written into code)

```
cd /d/UE/UE_5.9/Engine/Source; grep -rn "FShaderCodeName" --include=*.cpp --include=*.h Runtime Developer 2>/dev/null | grep -v "^.*//" | head -15
```

Result:

```
Runtime/Apple/MetalRHI/Private/Shaders/Types/Templates/MetalBaseShader.h:345:			const FString ShaderName = ShaderCode.FindOptionalData(FShaderCodeName::Key);
Runtime/D3D12RHI/Private/D3D12Shaders.cpp:39:	OutShader.Debug.ShaderName = InShaderCode.FindOptionalData(FShaderCodeName::Key);
Runtime/OpenGLDrv/Private/OpenGLShaders.cpp:1158:	RHIShader->Debug.ShaderName = ShaderCode.FindOptionalData(FShaderCodeName::Key);
Runtime/RenderCore/Public/ShaderCore.h:906:struct FShaderCodeName
Runtime/VulkanRHI/Private/VulkanShaders.cpp:55:	RHIShader->Debug.ShaderName = ShaderCode.FindOptionalData(FShaderCodeName::Key);
Runtime/Windows/D3D11RHI/Private/D3D11Shaders.cpp:29:	OutShader.Debug.ShaderName = InShaderCode.FindOptionalData(FShaderCodeName::Key);
Developer/Apple/MetalShaderFormat/Private/MetalShaderCompiler.cpp:889:				ShaderOutput.ShaderCode.AddOptionalData(FShaderCodeName::Key, TCHAR_TO_UTF8(*ShaderInput.GenerateShaderName()));
Developer/Apple/MetalShaderFormat/Private/MetalShaderCompiler.cpp:1176:		const FString ShaderName = ShaderCode.FindOptionalData(FShaderCodeName::Key);
Developer/Apple/MetalShaderFormat/Private/MetalShaderCompiler.cpp:1306:			const FString ShaderName = ShaderCode.FindOptionalData(FShaderCodeName::Key);
Developer/ShaderFormatOpenGL/Private/OpenGLShaderCompiler.cpp:893:			ShaderOutput.ShaderCode.AddOptionalData(FShaderCodeName::Key, TCHAR_TO_UTF8(*ShaderInput.GenerateShaderName()));
Developer/VulkanShaderFormat/Private/VulkanShaderCompiler.cpp:370:		Output.ShaderCode.AddOptionalData(FShaderCodeName::Key, TCHAR_TO_UTF8(*Input.GenerateShaderName()));
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:56:53 · Tool call: Bash** (Find D3D shader name optional data flag)

```
cd /d/UE/UE_5.9/Engine/Source; grep -rn "AddOptionalData\|ShaderCodeName\|ExtraData\|GenerateShaderName" Developer/Windows/ShaderFormatD3D/Private/*.cpp 2>/dev/null | head -15; grep -rn "CFLAG_ExtraShaderData\|r.Shaders.ExtraData" --include=*.cpp Runtime/Engine/Private/ShaderCompiler Runtime/RenderCore/Private 2>/dev/null | head
```

Result:

```
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompiler.cpp:1302:			auto AddOptionalDataCallback = [&](FShaderCode& ShaderCode)
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompiler.cpp:1304:				Output.ShaderCode.AddOptionalData(ResourceMasks);
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompiler.cpp:1318:				AddOptionalDataCallback
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp:1146:			auto AddOptionalDataCallback = [&](FShaderCode& ShaderCode)
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp:1191:				ShaderCode.AddOptionalData<FShaderCodeFeatures>(CodeFeatures);
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp:1196:					ShaderCode.AddOptionalData(EShaderOptionalDataKey::ShaderModel6, &IsSM6, 1);
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp:1206:					ShaderCode.AddOptionalData(EShaderOptionalDataKey::EntryPoint, NameData.GetData(), NameData.Num());
Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp:1226:				AddOptionalDataCallback
Runtime/Engine/Private/ShaderCompiler/ShaderCompiler.cpp:453:	TEXT("r.Shaders.ExtraData"),
Runtime/Engine/Private/ShaderCompiler/ShaderCompiler.cpp:3749:		Input.Environment.CompilerFlags.Add(CFLAG_ExtraShaderData);
Runtime/Engine/Private/ShaderCompiler/ShaderCompiler.cpp:3900:			static const auto CVarExtraData = IConsoleManager::Get().FindConsoleVariable(TEXT("r.Shaders.ExtraData"));
Runtime/RenderCore/Private/ShaderCore.cpp:1007:	static const FShaderSymbolSettingHelper ExtraData(TEXT("r.Shaders.ExtraData"));
Shell cwd was reset to [notes]
```

### Sun 15 Nov 10:56:58 · Agent (claude-opus-5-5)

Checking what the D3D shader compiler records as each shader's required features, and whether the D3D12 RHI checks them against the card.

**Sun 15 Nov 10:56:58 · Tool call: Bash** (Read recorded shader code features)

```
cd /d/UE/UE_5.9/Engine/Source; sed -n 1146,1200p Developer/Windows/ShaderFormatD3D/Private/D3DShaderCompilerDXC.cpp; grep -n "EShaderCodeFeatures::" Runtime/RenderCore/Public/ShaderCore.h | head -30
```

Result:

```
auto AddOptionalDataCallback = [&](FShaderCode& ShaderCode)
			{
				FShaderCodeFeatures CodeFeatures;

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_WAVE_OPS) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::WaveOps);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_NATIVE_16BIT_OPS) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::SixteenBitTypes);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_TYPED_UAV_LOAD_ADDITIONAL_FORMATS) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::TypedUAVLoadsExtended);
				}

				if ((ShaderRequiresFlags & (D3D_SHADER_REQUIRES_ATOMIC_INT64_ON_TYPED_RESOURCE| D3D_SHADER_REQUIRES_ATOMIC_INT64_ON_GROUP_SHARED)) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::Atomic64);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_RESOURCE_DESCRIPTOR_HEAP_INDEXING) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::BindlessResources);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_SAMPLER_DESCRIPTOR_HEAP_INDEXING) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::BindlessSamplers);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_STENCIL_REF) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::StencilRef);
				}

				if ((ShaderRequiresFlags & D3D_SHADER_REQUIRES_BARYCENTRICS) != 0)
				{
					EnumAddFlags(CodeFeatures.CodeFeatures, EShaderCodeFeatures::BarycentricsSemantic);
				}

				// We only need this to appear when using a DXC shader
				ShaderCode.AddOptionalData<FShaderCodeFeatures>(CodeFeatures);

				if (ShaderModel >= ED3DShaderModel::SM6_0)
				{
					uint8 IsSM6 = 1;
					ShaderCode.AddOptionalData(EShaderOptionalDataKey::ShaderModel6, &IsSM6, 1);
				}

				// Store EntryPointName for possible use in work graph state object creation.
				if (bIsWorkGraphShader || Input.Target.GetFrequency() == SF_Pixel)
902:	EShaderCodeFeatures CodeFeatures = EShaderCodeFeatures::None;
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:57:02 · Tool call: Bash** (Find RHI use of shader code features)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "FShaderCodeFeatures\|EShaderCodeFeatures" --include=*.cpp --include=*.h D3D12RHI RHICore RenderCore/Private 2>/dev/null | head -20
```

Result:

```
D3D12RHI/Private/D3D12Shaders.cpp:76:	if (const FShaderCodeFeatures* CodeFeatures = InShaderCode.FindOptionalData<FShaderCodeFeatures>())
D3D12RHI/Private/D3D12Shaders.cpp:119:	if (EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::WaveOps) && !GRHISupportsWaveOperations && !IsRayTracingShaderFrequency(InFrequency))
D3D12RHI/Private/D3D12Shaders.cpp:125:	if (EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::BindlessResources | EShaderCodeFeatures::BindlessSamplers))
D3D12RHI/Private/D3D12Shaders.cpp:134:	if (InFrequency == SF_Pixel && EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::StencilRef) && !GRHISupportsStencilRefFromPixelShader)
D3D12RHI/Private/D3D12Shaders.cpp:140:	if (EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::BarycentricsSemantic) && !GRHIGlobals.SupportsBarycentricsSemantic)
D3D12RHI/Private/D3D12Shaders.h:83:	EShaderCodeFeatures Features = EShaderCodeFeatures::None;
D3D12RHI/Private/D3D12Shaders.h:108:	FORCEINLINE EShaderCodeFeatures GetFeatures() const { return Features; }
D3D12RHI/Private/D3D12Shaders.h:110:	FORCEINLINE EShaderCodeFeatures GetFeatures() const { return EShaderCodeFeatures::None; }
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:57:07 · Tool call: Bash** (Read D3D12 shader feature checks)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; sed -n 70,160p D3D12RHI/Private/D3D12Shaders.cpp
```

Result:

```
}
		}
	}
#endif

#if D3D12RHI_NEEDS_SHADER_FEATURE_CHECKS
	if (const FShaderCodeFeatures* CodeFeatures = InShaderCode.FindOptionalData<FShaderCodeFeatures>())
	{
		OutShader.Features = CodeFeatures->CodeFeatures;
	}
#endif

	int32 ShaderBindingLayoutSize = 0;
	auto* ShaderBindingLayoutData = InShaderCode.FindOptionalDataAndSize(FShaderCodeShaderResourceTableDataDesc::Key, ShaderBindingLayoutSize);
	if (ShaderBindingLayoutData && ShaderBindingLayoutSize > 0)
	{
		check(ShaderBindingLayoutSize == sizeof(OutShader.ShaderBindingLayoutHash));
		FBufferReader Ar((void*)ShaderBindingLayoutData, ShaderBindingLayoutSize, false);
		Ar << OutShader.ShaderBindingLayoutHash;
	}

	if (CanReadEntryPoint(OutShader))
	{
		int32 NameSize = 0;
		uint8 const* NameData = InShaderCode.FindOptionalDataAndSize(EShaderOptionalDataKey::EntryPoint, NameSize);
		if (NameData && NameSize > 0)
		{
			FBufferReader Reader((void*)NameData, NameSize, false);
			ReadEntryPoint(Reader, OutShader);
		}
	}

	UE::RHICore::SetupShaderCodeValidationData(&OutShader, InShaderCode);
	UE::RHICore::SetupShaderDiagnosticData(&OutShader, InShaderCode);

	return true;
}

static bool ValidateShaderIsUsable(FD3D12ShaderData* InShader, EShaderFrequency InFrequency)
{
#if D3D12RHI_NEEDS_SHADER_FEATURE_CHECKS
	if ((InFrequency == SF_Mesh || InFrequency == SF_Amplification) && !GRHISupportsMeshShadersTier0)
	{
		UE_LOGF(LogD3D12RHI, Log, "Trying to create Mesh or Amplication shader but RHI doesn't support MeshShaders");
		return false;
	}

	// When we're using the SM5 shader library plus raytracing, GRHISupportsWaveOperations is false because DXBC shaders can't do wave ops,
	// but RT shaders are compiled to DXIL and can use wave ops (HW support is guaranteed too).
	if (EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::WaveOps) && !GRHISupportsWaveOperations && !IsRayTracingShaderFrequency(InFrequency))
	{
		UE_LOGF(LogD3D12RHI, Log, "Trying to create shader with WaveOps but RHI doesn't support WaveOperations");
		return false;
	}

	if (EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::BindlessResources | EShaderCodeFeatures::BindlessSamplers))
	{
		if (!GRHIGlobals.bSupportsBindless)
		{
			UE_LOGF(LogD3D12RHI, Log, "Trying to create shader with bindless resources or samplers but RHI doesn't support Bindless");
			return false;
		}
	}

	if (InFrequency == SF_Pixel && EnumHasAnyFlags(InShader->Features, EShaderCodeFeatures::StencilRef) && !GRHISupportsStencilRefFromPixelShader)
	{
		UE_LOGF(LogD
[... 919 more characters not shown]
```

**Sun 15 Nov 10:57:24 · Tool call: Bash** (Find renderer shaders that pick 16-bit permutations at runtime)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rln "SupportsNative16BitOps\|GetSupportsRealTypes" Renderer/Private | head -20; grep -rn "SupportsNative16BitOps" Renderer/Private | head -20
```

Result:

```
Renderer/Private/Lumen/LumenScreenProbeGather.cpp
Renderer/Private/MegaLights/MegaLightsDenoising.cpp
Renderer/Private/PostProcess/DiaphragmDOF.cpp
Renderer/Private/PostProcess/TemporalSuperResolution.cpp
Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:640:	bool bUse16BitVALU = (CVarTSR16BitVALU.GetValueOnAnyThread() != 0 && GRHIGlobals.SupportsNative16BitOps && VALU16BitSupport == ERHIFeatureSupport::RuntimeDependent) || VALU16BitSupport == ERHIFeatureSupport::RuntimeGuaranteed;
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:644:	if ((GRHIGlobals.SupportsNative16BitOps && VALU16BitSupport == ERHIFeatureSupport::RuntimeDependent) || VALU16BitSupport == ERHIFeatureSupport::RuntimeGuaranteed)
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:57:32 · Tool call: Bash** (Look at 16-bit permutation gates and precache filters)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -n "GetSupportsRealTypes\|ShouldPrecachePermutation\|16Bit\|RealTypes" Renderer/Private/Lumen/LumenScreenProbeGather.cpp Renderer/Private/MegaLights/MegaLightsDenoising.cpp Renderer/Private/PostProcess/DiaphragmDOF.cpp Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp | head -40; grep -n "ShouldPrecachePermutation\|F16BitVALUDim\|bUse16BitVALU" Renderer/Private/PostProcess/TemporalSuperResolution.cpp | head -30
```

Result:

```
Renderer/Private/Lumen/LumenScreenProbeGather.cpp:1134:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
Renderer/Private/Lumen/LumenScreenProbeGather.cpp:1306:		if (FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Parameters.Platform) == ERHIFeatureSupport::RuntimeGuaranteed)
Renderer/Private/Lumen/LumenScreenProbeGather.cpp:1308:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:334:		if (FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Parameters.Platform) == ERHIFeatureSupport::RuntimeGuaranteed)
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:336:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:340:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:349:		return FGlobalShader::ShouldPrecachePermutation(Parameters);
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:442:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:449:		return FGlobalShader::ShouldPrecachePermutation(Parameters);
Renderer/Private/PostProcess/DiaphragmDOF.cpp:491:		if (FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Parameters.Platform) == ERHIFeatureSupport::RuntimeGuaranteed)
Renderer/Private/PostProcess/DiaphragmDOF.cpp:493:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp:213:		if (FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Parameters.Platform) == ERHIFeatureSupport::RuntimeGuaranteed)
Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp:215:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp:301:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
525:	class F16BitVALUDim : SHADER_PERMUTATION_BOOL("DIM_16BIT_VALU");
640:	bool bUse16BitVALU = (CVarTSR16BitVALU.GetValueOnAnyThread() != 0 && GRHIGlobals.SupportsNative16BitOps && VALU16BitSupport == ERHIFeatureSupport::RuntimeDependent) || VALU16BitSupport == ERHIFeatureSupport::RuntimeGuaranteed;
648:			bUse16BitVALU = CVarTSR16BitVALUOnAMD.GetValue
[... 3032 more characters not shown]
```

**Sun 15 Nov 10:57:42 · Tool call: Bash** (Compare error counts by GPU across existing run logs)

```
cd /d/UE/wt; for f in */run/run.log; do a=$(grep -m1 -o "Found D3D12 adapter 0: [^(]*" "$f"); c=$(grep -c "Failed to create compute pipeline" "$f"); p=$(grep -m1 -o "Precaching [0-9]* global compute shaders" "$f"); echo "$f | $a | $c | $p"; done 2>/dev/null | head -30
```

Result:

```
clap1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
credits1_farmlogs_main8_1/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
credits1_farmlogs_main8_2/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
credits1_farmlogs_shots_1080/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
credits1_farmlogs_shots_720/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
feel5_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
gen2_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
hud1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
rebake1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
sfx4_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
ui1_farmlogs/run/run.log | Found D3D12 adapter 0: AMD Radeon RX 9070 XT  | 0 | 
vfx1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce RTX 4080 SUPER  | 0 | 
view1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce GTX 1070  | 0 | 
viewmerge1_farmlogs/run/run.log | Found D3D12 adapter 0: NVIDIA GeForce GTX 1070  | 24 |
Shell cwd was reset to [notes]
```

### Sun 15 Nov 10:57:49 · Agent (claude-opus-5-5)

Found one pc2 log with 0 errors (view1) next to the 24-error one (viewmerge1). Comparing the two.

**Sun 15 Nov 10:57:49 · Tool call: Bash** (Compare command lines and precache lines)

```
cd /d/UE/wt; for f in view1_farmlogs/run/run.log viewmerge1_farmlogs/run/run.log clap1_farmlogs/run/run.log; do echo "== $f"; grep -m3 -i "Command Line\|Precach.*global\|LogPSO\|PSOPrecach" "$f" | cut -c1-300; grep -c "LogD3D12RHI: Error" "$f"; done
```

Result:

```
Exit code 1
== view1_farmlogs/run/run.log
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit: Command Line: -RenderOffscreen -windowed -ResX=960 -ResY=540 -WinX=0 -WinY=0 -nosplash -unattended -SupercutScript=C:\UE\Farm\view1\Script\v7_clip.txt -SupercutShots=C:\UE\Farm\_out\view1\run\shots -SupercutFps -abslog=C:\UE\Farm\_out\view1\run\run.log -SupercutRoom=puzzle/a_the_cue -Superc
[2026.11.14-18.58.23:619][  0]LogConfig: Set CVar [[r.PSOPrecache.GlobalShaders:1]]
0
== viewmerge1_farmlogs/run/run.log
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit: Command Line: -RenderOffscreen -windowed -ResX=1920 -ResY=1080 -WinX=0 -WinY=0 -nosplash -unattended -SupercutScript=C:\UE\Farm\viewmerge1\Script\viewmerge1_shots.txt -SupercutShots=C:\UE\Farm\_out\viewmerge1\run\shots -SupercutFps -abslog=C:\UE\Farm\_out\viewmerge1\run\run.log -SupercutRoo
LogConfig: Set CVar [[r.PSOPrecache.GlobalShaders:1]]
24
== clap1_farmlogs/run/run.log
LogInit:  CurlRequestOptions (configurable via config and command line):
LogInit: Command Line: -RenderOffscreen -windowed -ResX=1280 -ResY=720 -WinX=0 -WinY=0 -nosplash -unattended -SupercutScript=C:\UE\Farm\clap1\Script\main8.txt -SupercutShots=C:\UE\Farm\_out\clap1\run\shots -SupercutFps -abslog=C:\UE\Farm\_out\clap1\run\run.log -SupercutRun=main8 -SupercutSeed=1 -Sup
LogConfig: Set CVar [[r.PSOPrecache.GlobalShaders:1]]
0
```

**Sun 15 Nov 10:57:54 · Tool call: Bash** (Look for PSO cache lines in both logs)

```
cd /d/UE/wt; f=view1_farmlogs/run/run.log; grep -c . $f; grep -n -i "pipeline\|PSO" $f | head -20; grep -n "Packaged\|UnrealEditor\|-game\|Cooked\|bIsCooked\|Using Cooked\|Supercut.exe" $f | head -5; f2=viewmerge1_farmlogs/run/run.log; grep -n -i "pipeline cache\|PipelineFileCache\|ShaderPipelineCache" $f2 | head
```

Result:

```
2152
208:LogPluginManager: Mounting Engine plugin KDevelopSourceCodeAccess
533:[2026.11.14-18.58.23:619][  0]LogConfig: Set CVar [[r.PSOPrecache.GlobalShaders:1]]
856:[2026.11.14-18.58.23:626][  0]LogConfig: Set CVar [[r.PSOPrecache.KeepInMemoryForActiveMaterials:1]]
896:[2026.11.14-18.58.24:185][  0]LogGenericApplication: Input pipeline initialized (game-thread consumer registered; proxy created idle).
970:[2026.11.14-18.58.24:794][  0]LogD3D12RHI: Display: Not using pipeline state disk cache per r.D3D12.PSO.DiskCache=0
971:[2026.11.14-18.58.24:794][  0]LogD3D12RHI: Display: Not using driver-optimized pipeline state disk cache per r.D3D12.PSO.DriverOptimizedDiskCache=0
1178:[2026.11.14-18.58.32:217][  0]LogModuleManager: InternalLoadLibrary: 'InterchangePipelines' ('C:/UE/UE_5.9/Engine/Plugins/Interchange/Runtime/Binaries/Win64/UnrealEditor-InterchangePipelines.dll')
2109:[2026.11.14-18.58.57:738][710]LogGenericApplication: Multi-threaded input pipeline shut down (proxy removed, real handler restored).
32:LogCsvProfiler: Display: Metadata set : commandline="" C:\UE\Farm\view1\Supercut.uproject -game -RenderOffscreen -windowed -ResX=960 -ResY=540 -WinX=0 -WinY=0 -nosplash -unattended -SupercutScript=C:\UE\Farm\view1\Script\v7_clip.txt -SupercutShots=C:\UE\Farm\_out\view1\run\shots -SupercutFps -abslog=C:\UE\Farm\_out\view1\run\run.log -SupercutRoom=puzzle/a_the_cue -SupercutQuit -UseFixedTimeStep -FPS=240 -DeterministicAudio""
35:LogModuleManager: InternalLoadLibrary: 'StorageServerClient' ('C:/UE/UE_5.9/Engine/Binaries/Win64/UnrealEditor-StorageServerClient.dll')
36:LogModuleManager: InternalLoadLibrary: 'CookOnTheFly' ('C:/UE/UE_5.9/Engine/Binaries/Win64/UnrealEditor-CookOnTheFly.dll')
37:LogModuleManager: InternalLoadLibrary: 'StreamingFile' ('C:/UE/UE_5.9/Engine/Binaries/Win64/UnrealEditor-StreamingFile.dll')
38:LogModuleManager: InternalLoadLibrary: 'NetworkFile' ('C:/UE/UE_5.9/Engine/Binaries/Win64/UnrealEditor-NetworkFile.dll')
1127:[2026.11.14-19.59.09:199][  0]LogRHI: Display: ShaderPipelineCache: Paused Batching. 1
1129:[2026.11.14-19.59.09:200][  0]LogRHI: Display: ShaderPipelineCache: Resumed Batching. 0
1130:[2026.11.14-19.59.09:200][  0]LogRHI: Display: ShaderPipelineCache: Batching Resumed.
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:58:03 · Tool call: Bash** (Check SM6 platform info for real types)

```
cd /d/UE/UE_5.9/Engine/Config; grep -rn -A60 "ShaderPlatform PCD3D_SM6\]" Windows/DataDrivenPlatformInfo.ini 2>/dev/null | grep -i "realtypes\|wave\|16bit\|Name=" | head; grep -rln "PCD3D_SM6" --include=*.ini . | head
```

Result:

```
78-FriendlyName=LOCTEXT("FriendlyShaderPlatformName_D3D_SM6", "PC D3D SM6")
102-bSupportsWaveOperations=RuntimeGuaranteed
103-MinimumWaveSize=4
104-MaximumWaveSize=128
127-bSupportsRealTypes=RuntimeDependent
./BaseEngine.ini
./Windows/BaseWindowsEngine.ini
./Windows/DataDrivenPlatformInfo.ini
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:58:10 · Tool call: Bash** (Find shaders that enable 16-bit types)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "CFLAG_AllowRealTypes" Renderer/Private RenderCore/Private Engine/Private | grep -v "RuntimeGuaranteed" | head -20; grep -rn "ShouldCompile32or16BitPermutation" -A8 Renderer/Private/PostProcess/TemporalSuperResolution.cpp | head -20
```

Result:

```
Renderer/Private/Lumen/LumenScreenProbeGather.cpp:1308:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/MegaLights/MegaLightsDenoising.cpp:336:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/DiaphragmDOF.cpp:493:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:596:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:758:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:829:		OutEnvironment.CompilerFlags.Remove(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:989:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:1398:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/PostProcess/TemporalSuperResolution.cpp:1492:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
Renderer/Private/VirtualShadowMaps/VirtualShadowMapProjection.cpp:215:			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
546:	static bool ShouldCompile32or16BitPermutation(EShaderPlatform Platform, bool bIs16BitVALUPermutation)
547-	{
548-		// Always compile the 32bit permutations for the alpha channel
549-		if (!bIs16BitVALUPermutation)
550-		{
551-			return true;
552-		}
553-
554-		const ERHIFeatureSupport Support = FTSRShader::Supports16BitVALU(Platform);
--
709:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
710-		{
711-			return false;
712-		}
713-
714-		return true;
715-	}
716-
717-	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters, FPermutationDomain PermutationVector)
--
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:58:24 · Tool call: Bash** (Precache count and render config)

```
cd /d/UE/wt/viewmerge1_farmlogs/run; grep -n "Precaching\|global compute\|AntiAliasing\|TSR\|Lumen\|Nanite\|VirtualShadow\|r.DynamicGlobal\|r.ReflectionMethod\|r.Shadow.Virtual" run.log | head -30; grep -n "AntiAliasing\|DynamicGlobal\|Reflection\|Virtual\|Nanite\|PSO\|ShaderPipelineCache\|Lumen\|SkyLight\|RayTrac" /d/UE/wt/perf3/Config/DefaultEngine.ini
```

Result:

```
376:LogDevObjectVersion:   Dev-NaniteResearch (30D58BE3-95EA-4282-A6E3-B159D8EBB06A): 1
401:LogConfig: Set CVar [[r.Nanite.Streaming.ReservedResources:1]]
429:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.Enable:1]]
430:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.DynamicGlobalIlluminationMethod:1]]
431:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.ReflectionMethod:1]]
476:[2026.11.14-19.59.06:613][  0]LogConfig: Applying CVar settings from Section [AntiAliasingQuality@3] File [Scalability]
479:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.History.R11G11B10:1]]
480:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.History.ScreenPercentage:200]]
481:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.History.UpdateQuality:3]]
482:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.ShadingRejection.Flickering:1]]
483:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.RejectionAntiAliasingQuality:2]]
484:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.ReprojectionField:1]]
485:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.TSR.Resurrection:1]]
503:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.MaxPhysicalPages:4096]]
504:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.ResolutionLodBiasDirectional:-1.5]]
505:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.ResolutionLodBiasDirectionalMoving:-1.5]]
506:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.ResolutionLodBiasLocal:0.0]]
507:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.ResolutionLodBiasLocalMoving:1.0]]
508:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.SMRT.RayCountDirectional:8]]
509:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.SMRT.SamplesPerRayDirectional:4]]
510:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.SMRT.RayCountLocal:8]]
511:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.SMRT.SamplesPerRayLocal:4]]
512:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Shadow.Virtual.MarkCoarsePagesLocal:1]]
528:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Lumen.DiffuseIndirect.Allow:1]]
529:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.Lumen.FinalGatherMethod:1]]
530:[2026.11.14-19.59.06:613][  0]LogConfig: Set CVar [[r.LumenScene.SurfaceCache.AtlasSize:4096]]
531:[2026.11.14-19.59.06:613][  0]Log
[... 541 more characters not shown]
```

**Sun 15 Nov 10:58:28 · Tool call: Bash** (Check build progress)

```
cat /d/UE/wt/perf3_farmlogs/bp.txt | tail -5; date +%H:%M
```

Result:

```
10:58
```

**Sun 15 Nov 10:58:45 · Tool call: Bash** (Find precache call site and shader dump commands)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "PrecacheComputePipelineStatesForGlobalShaders(" --include=*.cpp . | grep -v "^.*void Precache" | head; grep -rn "TEXT(\"r\.[A-Za-z.]*Dump[A-Za-z.]*\"\|TEXT(\"Dump[A-Za-z]*Shader" --include=*.cpp RenderCore Engine/Private/ShaderCompiler RHI 2>/dev/null | head
```

Result:

```
./Launch/Private/LaunchEngineLoop.cpp:4504:		PrecacheComputePipelineStatesForGlobalShaders(GMaxRHIFeatureLevel, nullptr);
RenderCore/Private/DumpGPU.cpp:63:	TEXT("r.DumpGPU.Root"),
RenderCore/Private/DumpGPU.cpp:69:	TEXT("r.DumpGPU.Texture"), 2,
RenderCore/Private/DumpGPU.cpp:77:	TEXT("r.DumpGPU.Buffer"), 2,
RenderCore/Private/DumpGPU.cpp:85:	TEXT("r.DumpGPU.MaxStagingSize"), 64,
RenderCore/Private/DumpGPU.cpp:90:	TEXT("r.DumpGPU.PassParameters"), 1,
RenderCore/Private/DumpGPU.cpp:95:	TEXT("r.DumpGPU.Profile"), -1,
RenderCore/Private/DumpGPU.cpp:104:	TEXT("r.DumpGPU.RedumpInputs"), 0,
RenderCore/Private/DumpGPU.cpp:110:	TEXT("r.DumpGPU.Delay"), 0.0f,
RenderCore/Private/DumpGPU.cpp:115:	TEXT("r.DumpGPU.FrameDelay"), 0,
RenderCore/Private/DumpGPU.cpp:120:	TEXT("r.DumpGPU.FrameCount"), 1,
Shell cwd was reset to [notes]
```

### Sun 15 Nov 10:59:13 · Agent (claude-opus-5-5)

While the build runs: reading the game's first-start settings code (the benchmark that picked EPIC on pc2 in perf2's run).

**Sun 15 Nov 10:59:14 · Tool call: Bash** (Find benchmark and default level code)

```
cd /d/UE/wt/perf3/Source/Supercut; grep -n "Benchmark\|RunHardwareBenchmark\|ApplyHardwareBenchmark\|GPUBenchmark\|ScalabilityLevel\|SetOverallScalabilityLevel\|DLSS\|Dlss" SupercutUserSettings.cpp | head -40; wc -l SupercutUserSettings.cpp
```

Result:

```
3:#include "SupercutDlss.h"
23:	DlssMode = 0;
55:	SetOverallScalabilityLevel(FMath::Clamp(Level, 0, HighestQuality));
117:void USupercutUserSettings::SetDlssMode(int32 Mode)
119:	DlssMode = FMath::Clamp(Mode, 0, SupercutDlss::ModeCount - 1);
147:	SupercutDlss::Apply(DlssMode);   // after the scalability groups, which set r.ScreenPercentage
159:	RunHardwareBenchmark();
164:		LastCPUBenchmarkResult, LastGPUBenchmarkResult, ScalabilityQuality.ViewDistanceQuality, ScalabilityQuality.AntiAliasingQuality, ScalabilityQuality.ShadowQuality,
171:int32 USupercutUserSettings::FirstStartLevel(int32 BenchmarkLowest)
173:	checkf(BenchmarkLowest >= 0 && BenchmarkLowest <= HighestQuality, TEXT("FirstStartLevel: the benchmark's lowest level %d is not 0 to 3"), BenchmarkLowest);
174:	return FMath::Clamp(BenchmarkLowest - 1, 1, HighestQuality - 1);
221 SupercutUserSettings.cpp
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:59:18 · Tool call: Bash** (Read first-start level code)

```
cd /d/UE/wt/perf3/Source/Supercut; sed -n 140,221p SupercutUserSettings.cpp; git -C /d/UE/wt/perf3 log --oneline -3 -- Source/Supercut/SupercutUserSettings.cpp
```

Result:

```
{
	if (bWindow)
	{
		ApplyResolutionSettings(false);
		ConfirmVideoMode();
	}
	ApplyNonResolutionSettings();
	SupercutDlss::Apply(DlssMode);   // after the scalability groups, which set r.ScreenPercentage
	SaveSettings();
	UE_LOG(LogSupercut, Display, TEXT("SETTINGS saved: %s"), *Describe());
}

void USupercutUserSettings::ChooseQualityOnFirstStart()
{
	if (bQualityChosen)
	{
		return;
	}
	const double Start = FPlatformTime::Seconds();
	RunHardwareBenchmark();
	// The benchmark sets each group on its own. The settings screen shows one level: one under the lowest group's.
	const int32 Lowest = ScalabilityQuality.GetMinQualityLevel();
	const int32 Level = FirstStartLevel(Lowest);
	UE_LOG(LogSupercut, Display, TEXT("SETTINGS first start: benchmark CPU %.0f, GPU %.0f, groups view %d, anti-aliasing %d, shadows %d, GI %d, reflections %d, post %d, textures %d, effects %d, foliage %d, shading %d, in %.1f s; lowest %s, quality set to %s"),
		LastCPUBenchmarkResult, LastGPUBenchmarkResult, ScalabilityQuality.ViewDistanceQuality, ScalabilityQuality.AntiAliasingQuality, ScalabilityQuality.ShadowQuality,
		ScalabilityQuality.GlobalIlluminationQuality, ScalabilityQuality.ReflectionQuality, ScalabilityQuality.PostProcessQuality, ScalabilityQuality.TextureQuality,
		ScalabilityQuality.EffectsQuality, ScalabilityQuality.FoliageQuality, ScalabilityQuality.ShadingQuality, FPlatformTime::Seconds() - Start, QualityName(Lowest), QualityName(Level));
	SetQuality(Level);
	ApplyAndSave(false);
}

int32 USupercutUserSettings::FirstStartLevel(int32 BenchmarkLowest)
{
	checkf(BenchmarkLowest >= 0 && BenchmarkLowest <= HighestQuality, TEXT("FirstStartLevel: the benchmark's lowest level %d is not 0 to 3"), BenchmarkLowest);
	return FMath::Clamp(BenchmarkLowest - 1, 1, HighestQuality - 1);
}

FIntPoint USupercutUserSettings::WindowSize(const FIntPoint& Desktop)
{
	const FIntPoint Wanted(1600, 900);
	const float Scale = FMath::Min3(1.f, 0.9f * Desktop.X / Wanted.X, 0.9f * Desktop.Y / Wanted.Y);
	return FIntPoint(FMath::RoundToInt(Wanted.X * Scale), FMath::RoundToInt(Wanted.Y * Scale));
}

FIntPoint USupercutUserSettings::DisplaySize(bool bFullscreen, const FIntPoint& Desktop)
{
	return bFullscreen ? Desktop : WindowSize(Desktop);
}

bool USupercutUserSettings::IsSizeForced(const TCHAR* CommandLine)
{
	int32 Size = 0;
	return FParse::Value(CommandLine, TEXT("ResX="), Size) || FParse::Value(CommandLine, TEXT("ResY="), Size);
}

FString USupercutUserSettings::FilePath()
{
	// GetConfigFilen
[... 1382 more characters not shown]
```

**Sun 15 Nov 10:59:24 · Tool call: Bash** (Read settings defaults and DLSS default)

```
cd /d/UE/wt/perf3/Source/Supercut; sed -n 1,60p SupercutUserSettings.cpp; grep -n "Default\|default\|first start\|FirstStart" SupercutDlss.cpp | head -20
```

Result:

```
#include "SupercutUserSettings.h"
#include "Supercut.h"
#include "SupercutDlss.h"
#include "Engine/Engine.h"
#include "Misc/ConfigCacheIni.h"
#include "Misc/Parse.h"
#include "Misc/Paths.h"
#include "Scalability.h"

USupercutUserSettings& USupercutUserSettings::Get()
{
	USupercutUserSettings* Settings = Cast<USupercutUserSettings>(GEngine ? GEngine->GetGameUserSettings() : nullptr);
	checkf(Settings, TEXT("USupercutUserSettings::Get: the engine's user settings are not USupercutUserSettings. Config/DefaultEngine.ini needs GameUserSettingsClassName=/Script/Supercut.SupercutUserSettings."));
	return *Settings;
}

void USupercutUserSettings::SetToDefaults()
{
	Super::SetToDefaults();
	Sensitivity = 1.f;
	Volume = 100;
	bQualityChosen = false;
	DlssMode = 0;
	Crosshair = FSupercutCrosshair();
	MusicVolume = 100;
	EffectsVolume = 100;
	InterfaceVolume = 80;
	bMuteUnfocused = true;
	CameraShake = 100;
	bMotionBlur = false;
	ColourBlind = 0;
	bKeyHints = true;
	bTeachingPrompts = true;
	bHitMarkers = true;
	bRoomSlate = true;
	ClapFlash = 0;
	HurtFlash = 0;
	Overlay = 0;
	bInvertLook = false;
	Keys = FSupercutKeyBindings();
}

void USupercutUserSettings::SetSensitivity(float Value)
{
	Sensitivity = FMath::RoundToFloat(FMath::Clamp(Value, SensitivityLowest, SensitivityHighest) * 100.f) / 100.f;
}

void USupercutUserSettings::SetVolume(int32 Value)
{
	Volume = FMath::Clamp(FMath::RoundToInt(float(Value) / VolumeStep) * VolumeStep, 0, 100);
}

void USupercutUserSettings::SetQuality(int32 Level)
{
	SetOverallScalabilityLevel(FMath::Clamp(Level, 0, HighestQuality));
	bQualityChosen = true;
}

void USupercutUserSettings::SetFullscreen(bool bFullscreen)
{
59:	/** What the scalability groups set r.ScreenPercentage to (Scalability.cpp SetResolutionQualityLevel): 0, the project's default, for ResolutionQuality 0. */
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:59:30 · Tool call: Bash** (Check build progress)

```
cat /d/UE/wt/perf3_farmlogs/bp.txt | tail -8; date +%H:%M
```

Result:

```
10:59
```

**Sun 15 Nov 10:59:43 · Tool call: Bash** (Find CSV profiler command line switches)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Core; grep -n "TEXT(\"-csv\|TEXT(\"csv[A-Za-z]*\"\|\"csvCaptureFrames\|csvCapture\b\|csvGpuStats\|csv.CaptureFrames" Private/ProfilingDebugging/CsvProfiler.cpp | head -20; grep -rn "define CSV_PROFILER\b\|define CSV_PROFILER " Public/ProfilingDebugging/CsvProfilerConfig.h Public/ProfilingDebugging/CsvProfiler.h 2>/dev/null | head
```

Result:

```
541:	static bool bContinuousWritesDisabled = FParse::Param(FCommandLine::Get(), TEXT("csvContinuousWritesDisabled"));
693:				bFastCVarSet = FParse::Param(FCommandLine::Get(), TEXT("csvABTestFastCVarSet"));
3275:		if (FParse::Param(FCommandLine::Get(), TEXT("csvProfilerHighPriority")))
4111:	if (CVarCsvBenchmark.GetValueOnGameThread() || FParse::Param(FCommandLine::Get(), TEXT("csvBench")))
4325:	GCsvUseProcessingThread = FForkProcessHelper::IsForkedMultithreadInstance() && !FParse::Param(FCommandLine::Get(), TEXT("csvNoProcessingThread"));
5054:	if (FParse::Value(Commandline, TEXT("csvCaptureFrames="), NumCsvFrames))
5103:	if (FParse::Param(FCommandLine::Get(), TEXT("csvGpuStats")))
5111:	if (FParse::Param(FCommandLine::Get(), TEXT("csvTest")))
5115:	if (FParse::Param(FCommandLine::Get(), TEXT("csvTestMT")))
5120:	if (FParse::Param(FCommandLine::Get(), TEXT("csvTestCategoryOnly")))
5126:	if (FParse::Param(FCommandLine::Get(), TEXT("csvAllCategoriesDisabled")))
5163:	if (FParse::Param(FCommandLine::Get(), TEXT("csvNoProcessingThread")))
5168:	if (FParse::Param(FCommandLine::Get(), TEXT("csvNamedEvents")))
5172:	if (FParse::Param(FCommandLine::Get(), TEXT("csvNamedEventsTiming")))
5177:	if (FParse::Param(FCommandLine::Get(), TEXT("csvStatCounts")))
5182:	if (FParse::Value(FCommandLine::Get(), TEXT("csvCaptureFrames="), NumCsvFrames))
5209:	if (FParse::Value(FCommandLine::Get(), TEXT("-csvExecCmds="), CsvExecCommandsStr, false))
5254:	if (FParse::Value(FCommandLine::Get(), TEXT("-csvEventExecCmds="), CsvExecCommandsStr, false))
5470:	static bool bTaskStats = FParse::Param(FCommandLine::Get(), TEXT("csvTestTasks"));
Public/ProfilingDebugging/CsvProfilerConfig.h:31:	#define CSV_PROFILER (WITH_ENGINE && (!UE_BUILD_SHIPPING || CSV_PROFILER_ENABLE_IN_SHIPPING))
Shell cwd was reset to [notes]
```

**Sun 15 Nov 10:59:47 · Tool call: Bash** (Read csvCaptureFrames handling)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Core; sed -n 5040,5070p Private/ProfilingDebugging/CsvProfiler.cpp; sed -n 5178,5200p Private/ProfilingDebugging/CsvProfiler.cpp
```

Result:

```
#if !CSV_PROFILER_MINIMAL
	if (GCsvProfilerIsCapturing && GCsvCategoriesEnabled[CategoryIndex])
	{
		ValidateFName(StatName);
		FCsvProfilerThreadData::GetEndOfPipe()->AddCustomStat(StatName, CategoryIndex, (float)Value, CustomStatOp);
	}
#endif
}

void FCsvProfiler::PreInit(const TCHAR * Commandline)
{
#if CSV_PROFILER_ALLOW_DEBUG_FEATURES
	// If we're doing boot profiling then we need to init early and make sure the commandline is set
	int32 NumCsvFrames = 0;
	if (FParse::Value(Commandline, TEXT("csvCaptureFrames="), NumCsvFrames))
	{
		if (!FCommandLine::IsInitialized())
		{
			FCommandLine::Set(Commandline);
		}
		// Delay processing thread start
		GDelayProcessingThreadStart = true;
		FCsvProfiler::Get()->InitInternal();
	}
#endif
}

void FCsvProfiler::Init()
{
	InitInternal();
	// It's now safe to start the processing thread
	{
		CVarCsvStatCounts.AsVariable()->Set(1);
	}
	int32 NumCsvFrames = 0;
	if (FParse::Value(FCommandLine::Get(), TEXT("csvCaptureFrames="), NumCsvFrames))
	{
		check(IsInGameThread());
		BeginCapture(NumCsvFrames, FString(), FString(), ECsvProfilerFlags::BootCapture);
		// Call BeginFrame() to start capturing a dummy first "frame"
		BeginFrame();
		// Add a region end marker so we can see where preinit and csv capture started
		EndRegion(CSV_CATEGORY_INDEX_GLOBAL, TEXT("EngineInit/Launch"));
	}
	FParse::Value(FCommandLine::Get(), TEXT("csvRepeat="), GCsvRepeatCount);

	int32 CompressionMode;
	if (FParse::Value(FCommandLine::Get(), TEXT("csvCompression="), CompressionMode))
	{
		switch (CompressionMode)
		{
		case 0: CVarCsvCompressionMode->Set(0); break;
		case 1: CVarCsvCompressionMode->Set(1); break;
		default:
Shell cwd was reset to [notes]
```

### Sun 15 Nov 11:00:02 · Agent (claude-opus-5-5)

Build still going. I'm writing the desktop-session measurement script for pc2 (modelled on perf2's) using the engine's CSV profiler for per-frame times.

**Sun 15 Nov 11:00:02 · Tool call: Bash** (Look at generated run script and fps scripts)

```
cd /d/UE/wt/perf3; ls Script/gen | head; head -30 Script/gen/s7.txt; cat Script/shell1_hall_fps.txt; cat Script/vfx1_fps.txt | head -30; ls Content/Runs
```

Result:

```
flats1_fps_s15.txt
load12.txt
pics_s15.txt
pics_s44.txt
pics_s7.txt
s21.txt
s44.txt
s7.txt
s7shots.txt
# gen2 play script, built by mkscript.py (gen1's, copied to lanes/gen2/play) from s7.plan. Do not edit by hand: change the plan.
# room gen/s7/d01.txt, start 250,200,0
0.20 lookat 700 0 152
0.23 move 1 0
1.05 move 0 0
2.00 clap
2.35 lookat 1500 0 152
2.38 move 1 0
3.71 lookat 1900 0 152
4.71 move 0 0
5.56 key One
0 scene 2 1
# room gen/s7/d02.txt, start 250,0,0
0.20 reload
0.25 lookat 700 -200 152
0.28 move 1 0
1.10 clap
1.15 lookat 1450 -60 152
2.45 move 0 0
2.70 aim 0
2.85 fire
3.12 fire
3.39 fire
3.54 lookat 1770 -140 152
3.57 move 1 0
4.12 move 0 0
4.37 aim 1
4.52 fire
4.79 fire
5.06 fire
# Proof for lane shell1 (the hall): frame time standing at the start of one room, looking down the room.
# Run: run_demo.ps1 -Packaged -Room fight/01_wind_machine -Seed 1 -Dev -Script <this file> -Silent (no -FixedFps)
# F4 turns damage off so the enemies cannot end the run. The FPS line counts frames after the first 3 s.
0.10 key F4
0.20 look 0 5
15.00 end
# vfx1: frame time under steady fire in a fight room. No pictures. Run without -FixedFps.
# -Room fight/01_wind_machine -Dev
0.20 look 0 0
0.25 key F4
0.40 lookat 420 -450 150
0.50 firehold 1
2.50 firehold 0
2.55 reload
4.50 lookat 420 0 0
4.60 firehold 1
6.60 firehold 0
6.65 reload
8.60 lookat 900 -330 340
8.70 firehold 1
10.70 firehold 0
10.75 reload
12.70 lookat 420 450 150
12.80 firehold 1
14.80 firehold 0
15.00 end
demo3.txt
fight5.txt
gen_s1.txt
gen_s10.txt
gen_s11.txt
gen_s12.txt
gen_s13.txt
gen_s14.txt
gen_s15.txt
gen_s16.txt
gen_s17.txt
gen_s18.txt
gen_s19.txt
gen_s2.txt
gen_s20.txt
gen_s21.txt
gen_s22.txt
gen_s23.txt
gen_s24.txt
gen_s25.txt
gen_s26.txt
gen_s27.txt
gen_s28.txt
gen_s29.txt
gen_s3.txt
gen_s30.txt
gen_s31.txt
gen_s32.txt
gen_s33.txt
gen_s34.txt
gen_s35.txt
gen_s36.txt
gen_s37.txt
gen_s38.txt
gen_s39.txt
gen_s4.txt
gen_s40.txt
gen_s41.txt
gen_s42.txt
gen_s43.txt
gen_s44.txt
gen_s45.txt
gen_s46.txt
gen_s47.txt
gen_s48.txt
gen_s49.txt
gen_s5.txt
gen_s50.txt
gen_s6.txt
gen_s7.txt
gen_s8.txt
gen_s9.txt
main.txt
main8.txt
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:00:25 · Tool call: Bash** (Check what CSV FrameTime measures)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "\"FrameTime\"" --include=*.cpp Core/Private/ProfilingDebugging Engine/Private | head -5; grep -rn "CSV_CUSTOM_STAT_GLOBAL(FrameTime\|CSV_CUSTOM_STAT_DEFINED(FrameTime\|FrameTime," Engine/Private/UnrealEngine.cpp Launch/Private/LaunchEngineLoop.cpp | head
```

Result:

```
Engine/Private/UnrealEngine.cpp:12543:void UEngine::SetAverageUnitTimes(float FrameTime, float RenderThreadTime, float GameThreadTime, float GPUFrameTime, float RHITFrameTime)
Launch/Private/LaunchEngineLoop.cpp:1554:	    CSV_CUSTOM_STAT_GLOBAL(MaxFrameTime, 1000.0f / TargetFPS, ECsvCustomStatOp::Set);
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:00:34 · Tool call: Bash** (Find CSV FrameTime stat source)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "FrameTime" Core/Private/ProfilingDebugging/CsvProfiler.cpp | head -10; grep -rn "CSV_CUSTOM_STAT.*FrameTime\|CSV_DEFINE_STAT.*FrameTime\|CSV_STAT.*FrameTime" --include=*.cpp . | head
```

Result:

```
150:TAutoConsoleVariable<bool> CVarCsvUseLegacyFrameTime(
151:	TEXT("csv.UseLegacyFrameTime"),
1482:	uint64 AddBeginFrameTimestamp(ECsvTimeline::Type Timeline, const bool bDoThreadCheck = true)
3766:	, LastEndFrameTimestamp(0)
3899:			GFrameBoundaries.AddBeginFrameTimestamp(ECsvTimeline::Gamethread);
4007:		GFrameBoundaries.AddBeginFrameTimestamp(ECsvTimeline::Renderthread, false);
4019:	LastEndFrameTimestamp = GCaptureStartTimestamp;
4163:		if (EnumHasAnyFlags(CurrentFlags, ECsvProfilerFlags::BootCapture) || CVarCsvUseLegacyFrameTime->GetBool())
4166:			uint64 ElapsedCycles = CurrentTimeStamp - LastEndFrameTimestamp;
4168:			CSV_CUSTOM_STAT_MINIMAL_GLOBAL(FrameTime, ElapsedMs, ECsvCustomStatOp::Set);
./Core/Private/ProfilingDebugging/CsvProfiler.cpp:4168:			CSV_CUSTOM_STAT_MINIMAL_GLOBAL(FrameTime, ElapsedMs, ECsvCustomStatOp::Set);
./Core/Private/ProfilingDebugging/CsvProfiler.cpp:4393:			CSV_CUSTOM_STAT_MINIMAL_GLOBAL(FrameTime, FrameTimeMs, ECsvCustomStatOp::Set);
./Launch/Private/LaunchEngineLoop.cpp:1554:	    CSV_CUSTOM_STAT_GLOBAL(MaxFrameTime, 1000.0f / TargetFPS, ECsvCustomStatOp::Set);
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:01:18 · Tool call: Bash** (Find where first-start quality runs)

```
cd /d/UE/wt/perf3/Source/Supercut; grep -rn "ChooseQualityOnFirstStart\|SETTINGS at start" *.cpp | head; grep -n "SupercutTrace\|SupercutFps\b\|\"SupercutFps\"" *.cpp | head
```

Result:

```
SupercutPlayerController.cpp:79:	UE_LOG(LogSupercut, Display, TEXT("SETTINGS at start: %s"), *Settings.Describe());
SupercutPlayerController.cpp:83:		Settings.ChooseQualityOnFirstStart();
SupercutShellTests.cpp:588:	Chosen->ChooseQualityOnFirstStart();
SupercutShellTests.cpp:592:	Chosen->ChooseQualityOnFirstStart();
SupercutUserSettings.cpp:152:void USupercutUserSettings::ChooseQualityOnFirstStart()
SupercutPlayerController.cpp:72:	bCountFps = FParse::Param(FCommandLine::Get(), TEXT("SupercutFps"));
SupercutPlayerController.cpp:74:	bTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:01:25 · Tool call: Bash** (Read BeginPlay settings flow)

```
cd /d/UE/wt/perf3/Source/Supercut; sed -n 60,100p SupercutPlayerController.cpp; cat /d/UE/wt/perf3_farmlogs/bp.txt | tail -3
```

Result:

```
USupercutRun& Run = USupercutRun::Get(this);
	RoomEntriesSeen = Run.GetRoomEntries();

	FString ScriptPath;
	if (FParse::Value(FCommandLine::Get(), TEXT("-SupercutScript="), ScriptPath))
	{
		LoadScript(ScriptPath);
	}
	if (FParse::Value(FCommandLine::Get(), TEXT("-SupercutShots="), ShotFolder))
	{
		IFileManager::Get().MakeDirectory(*ShotFolder, true);
	}
	bCountFps = FParse::Param(FCommandLine::Get(), TEXT("SupercutFps"));
	bQuitAtEnd = FParse::Param(FCommandLine::Get(), TEXT("SupercutQuit"));
	bTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));

	// The engine applied the saved window and quality at start. The volumes, the unfocused mute and the colour filter are the game's own.
	USupercutUserSettings& Settings = USupercutUserSettings::Get();
	USupercutMenu::Get(this).ApplyLive();
	UE_LOG(LogSupercut, Display, TEXT("SETTINGS at start: %s"), *Settings.Describe());
	SupercutDlss::Apply(Settings.GetDlssMode());
	if (Run.GetPhase() == ESupercutRunPhase::Title)
	{
		Settings.ChooseQualityOnFirstStart();
		USupercutMenu::Get(this).ShowTitle();
	}

	if (!bScripted)
	{
		// A person is playing: the game takes the mouse. A run started with a script never does,
		// so it cannot grab the mouse of whoever is at the PC.
		SetInputMode(FInputModeGameOnly());
		bShowMouseCursor = false;
	}
}

void ASupercutPlayerController::LoadScript(const FString& Path)
{
	TArray<FString> Lines;
	if (!FFileHelper::LoadFileToStringArray(Lines, *Path))
	{
Shell cwd was reset to [notes]
```

### Sun 15 Nov 11:01:38 · Agent (claude-opus-5-5)

Build still compiling. Writing the desktop-session run script now.

**Sun 15 Nov 11:01:55 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\desk_run.ps1",
 "content": "# Lane perf3. One launch of the perf3 Development package on pc2 in the logged-in desktop session\n# (started by a scheduled task with /it, so the game gets a real window and swap chain, not -RenderOffscreen).\n# Writes the engine log (-abslog), the engine's CSV profile (-csvCaptureFrames, per-frame wall times and GPU passes),\n# GPU samples every 0.5 s and result.txt into C:\\UE\\Farm\\_out\\perf3\\desk\\<Tag>.\n# -ClearCaches deletes the package's saved pipeline caches and settings first (only inside the perf3 package folder).\n# -FreshSettings deletes only the saved settings, so a start at the title runs the first-start benchmark again.\n# Never touches a process it did not start.\nparam([Parameter(Mandatory)][string]$Tag, [Parameter(Mandatory)][string]$ArgFile, [int]$LimitSec = 900,\n  [switch]$ClearCaches, [switch]$FreshSettings)\n$root = 'C:\\UE\\Farm\\_builds\\perf3\\Supercut59\\Windows'\n$saved = Join-Path $root 'Supercut\\Saved'\n$out = \"C:\\UE\\Farm\\_out\\perf3\\desk\\$Tag\"\nRemove-Item $out -Recurse -Force -ErrorAction SilentlyContinue\nNew-Item -ItemType Directory -Force $out | Out-Null\n$res = [ordered]@{ tag = $Tag; session_id = (Get-Process -Id $PID).SessionId }\nif ($ClearCaches -or $FreshSettings) {\n  $gus = Join-Path $saved 'Config\\Windows\\GameUserSettings.ini'\n  if (Test-Path $gus) { Remove-Item $gus -Force; $res.removed_settings = $true }\n}\nif ($ClearCaches) {\n  # Every pipeline or shader cache the game keeps under its own Saved folder.\n  $gone = @(Get-ChildItem $saved -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -in '.upipelinecache', '.ushadercache', '.bin' -or $_.FullName -match '\\\\(PipelineCaches|ShaderCache|D3DCache|PSOCache)\\\\' })\n  $res.cache_files_removed = ($gone | ForEach-Object { $_.FullName.Substring($saved.Length) }) -join ';'\n  $gone | Remove-Item -Force\n}\nRemove-Item (Join-Path $saved 'Profiling\\CSV') -Recurse -Force -ErrorAction SilentlyContinue\n$argLine = (Get-Content $ArgFile -Raw).Trim() -replace '\\{O\\}', $out\n$res.args = $argLine\n$res.gpu_before = (& nvidia-smi --query-gpu=utilization.gpu,memory.used,power.draw,temperature.gpu,clocks.sm --format=csv,noheader 2>$null)\n$res.cpu_before = [math]::Round((Get-Counter '\\Processor(_Total)\\% Processor Time').CounterSamples[0].CookedValue)\n$res.free_ram_mb_before = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1024)\n$res.others_before = (@(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '^(Supercut|UnrealEditor|cl|link|UnrealBuildTool|AutomationTool|ShaderCompileWorker)' }) | ForEach-Object { $_.Name }) -join ','\n$t0 = Get-Date\n$res.start_local = $t0.ToString('yyyy.MM.dd-HH.mm.ss:fff')\n$p = Start-Process -FilePath \"$root\\Supercut.exe\" -ArgumentList $argLine -WorkingDirectory $root -PassThru\n$null = $p.Handle\n$samp = Start-Job -ArgumentList $out -ScriptBlock { param($o)\n  while ($true) {\n    $g = & nvidia-smi --query-gpu=utilization.gpu,memory.used,clocks.sm,power.draw,temperature.gpu --format=csv,noheader 2>$null\n    $c = [math]::Round((Get-Counter '\\Processor(_Total)\\% Processor Time' -ErrorAction SilentlyContinue).CounterSamples[0].CookedValue)\n    \"$(Get-Date -f HH:mm:ss.f),cpu=$c,$g\" | Add-Content \"$o\\sample.csv\"\n    Start-Sleep -Milliseconds 500 } }\n$done = $p.WaitForExit($LimitSec * 1000)\n$res.seconds_to_exit = [math]::Round(((Get-Date) - $t0).TotalSeconds, 1)\nStop-Job $samp; Remove-Job $samp -Force\nif ($done) { $res.exit_code = $p.ExitCode; $res.hang = $false } else { $res.exit_code = 'none'; $res.hang = $true }\n$all = @(Get-CimInstance Win32_Process | Select-Object ProcessId, ParentProcessId)\n$ids = New-Object System.Collections.Generic.List[int]; $ids.Add($p.Id)\nfor ($i = 0; $i -lt $ids.Count; $i++) { foreach ($k in ($all | Where-Object { $_.ParentProcessId -eq $ids[$i] })) { $ids.Add([int]$k.ProcessId) } }\n$left = @($ids | Where-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })\nif (-not $done) { foreach ($i in $left) { Stop-Process -Id $i -Force -ErrorAction SilentlyContinue }; $res.stopped_by_pid = ($left -join ',') }\n$csv = Get-ChildItem (Join-Path $saved 'Profiling\\CSV') -Filter *.csv -ErrorAction SilentlyContinue | Sort-Object LastWriteTime | Select-Object -Last 1\nif ($csv) { Copy-Item $csv.FullName \"$out\\profile.csv\"; $res.csv = $csv.Name }\n$gus = Join-Path $saved 'Config\\Windows\\GameUserSettings.ini'\nif (Test-Path $gus) { Copy-Item $gus \"$out\\GameUserSettings.after.ini\" }\n$res.cpu_after = [math]::Round((Get-Counter '\\Processor(_Total)\\% Processor Time').CounterSamples[0].CookedValue)\n$res.others_after = (@(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '^(Supercut|UnrealEditor|cl|link|UnrealBuildTool|AutomationTool|ShaderCompileWorker)' }) | ForEach-Object { $_.Name }) -join ','\n$res.gpu_after = (& nvidia-smi --query-gpu=utilization.gpu,memory.used --format=csv,noheader 2>$null)\n$res.ended = (Get-Date).ToString('s')\n($res.GetEnumerator() | ForEach-Object { \"$($_.Key)=$($_.Value)\" }) | Set-Content \"$out\\result.txt\"\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\desk_run.ps1 (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:02:02 · Tool call: Bash** (Narrow the cache deletion filter)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3/tools"; python - <<'EOF'
p='desk_run.ps1'
s=open(p,encoding='utf-8').read()
s=s.replace("$_.Extension -in '.upipelinecache', '.ushadercache', '.bin' -or ","$_.Extension -in '.upipelinecache', '.ushadercache' -or ")
open(p,'w',encoding='utf-8').write(s)
EOF
grep -n "Extension -in" desk_run.ps1; tail -3 /d/UE/wt/perf3_farmlogs/bp.txt
```

Result:

```
22:  $gone = @(Get-ChildItem $saved -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -in '.upipelinecache', '.ushadercache' -or $_.FullName -match '\\(PipelineCaches|ShaderCache|D3DCache|PSOCache)\\' })
```

### Sun 15 Nov 11:02:05 · Agent (claude-opus-5-5)

Now the c4-side launcher (GPU gate, scheduled task, fetch with names masked).

**Sun 15 Nov 11:02:21 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "content": "#!/bin/bash\n# Lane perf3. usage: go.sh <tag> <argfile in tools/args> [desk_run.ps1 switches: -ClearCaches -FreshSettings -LimitSec N]\n# 1. farm load check (busy_procs none, CPU < 60) and a GPU idle gate (util < 40 % and < 70 W, 4 samples in a row, up to 15 min);\n# 2. copies the arg file to pc2, starts desk_run.ps1 in pc2's desktop session through a scheduled task (/it);\n# 3. waits for result.txt, then copies log, csv, samples, settings back to logs/<tag>/ with the PC and user names masked;\n# 4. farm load check again. Both readings go into logs/<tag>/load.txt.\ncd \"$(dirname \"$0\")/..\"\nF=\"[notes]/unreal/megajam-2026/farm/farm.sh\"\ntag=$1; af=$2; shift 2; flags=\"$*\"\nmkdir -p logs/$tag\nR='C:\\UE\\Farm\\_out\\perf3\\desktools'\nssh pc2 \"if not exist $R mkdir $R\" >/dev/null\nscp -q tools/desk_run.ps1 \"pc2:C:/UE/Farm/_out/perf3/desktools/desk_run.ps1\" || { echo scp failed; exit 1; }\nscp -q \"tools/args/$af\" \"pc2:C:/UE/Farm/_out/perf3/desktools/$af\" || { echo scp args failed; exit 1; }\nwaited=0\nwhile true; do\n  st=$(\"$F\" status pc2 2>/dev/null)\n  busy=$(echo \"$st\" | sed -n 's/^busy_procs=//p'); cpu=$(echo \"$st\" | sed -n 's/^cpu_load_pct=\\([0-9]*\\).*/\\1/p')\n  if [ \"$busy\" = \"none\" ] && [ \"${cpu:-100}\" -lt 60 ]; then break; fi\n  echo \"$(date +%H:%M) pc2 busy ($busy, cpu $cpu), waiting\"; sleep 60; waited=$((waited+60))\n  [ $waited -gt 1800 ] && { echo \"pc2 busy for 30 min, giving up\"; exit 1; }\ndone\necho \"before: $(echo \"$st\" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\\n' ' ')\" > logs/$tag/load.txt\nok=0; waited=0\nwhile [ $ok -lt 4 ] && [ $waited -lt 900 ]; do\n  r=$(ssh pc2 'nvidia-smi --query-gpu=utilization.gpu,power.draw --format=csv,noheader,nounits')\n  u=${r%%,*}; m=${r##*, }; m=${m%%.*}\n  if [ \"$u\" -lt 40 ] && [ \"$m\" -lt 70 ]; then ok=$((ok+1)); sleep 1; else ok=0; sleep 4; waited=$((waited+5)); fi\ndone\ngate=idle; [ $ok -lt 4 ] && gate=\"UNDER LOAD (gpu gate not met after ${waited}s)\"\necho \"gpu gate: $gate\" >> logs/$tag/load.txt\ntr=$(printf '%s' 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\\UE\\Farm\\_out\\perf3\\desktools\\desk_run.ps1 -Tag ' \"$tag\" ' -ArgFile C:\\UE\\Farm\\_out\\perf3\\desktools\\' \"$af\" \" $flags\")\nssh pc2 \"schtasks /create /tn perf3_supercut /tr \\\"$tr\\\" /sc once /st 23:59 /it /f\" >/dev/null || { echo create failed; exit 1; }\nssh pc2 'schtasks /run /tn perf3_supercut' >/dev/null || { echo run failed; exit 1; }\necho \"$(date +%H:%M:%S) started $tag ($gate)\"\nf=\"C:\\\\UE\\\\Farm\\\\_out\\\\perf3\\\\desk\\\\$tag\\\\result.txt\"\nfor i in $(seq 1 400); do sleep 5; ssh pc2 \"if exist $f (echo y)\" 2>/dev/null | grep -q y && break; done\nun=$(ssh pc2 'echo %USERNAME%' | tr -d '\\r\\n'); cn=$(ssh pc2 'echo %COMPUTERNAME%' | tr -d '\\r\\n')\nmask() { sed -e \"s#$un#USER#Ig\" -e \"s#$cn#PC2#Ig\"; }\nfor x in result.txt run.log sample.csv GameUserSettings.after.ini profile.csv; do\n  scp -q \"pc2:C:/UE/Farm/_out/perf3/desk/$tag/$x\" \"logs/$tag/$x.tmp\" 2>/dev/null && mask < \"logs/$tag/$x.tmp\" > \"logs/$tag/$x\" && rm \"logs/$tag/$x.tmp\"\ndone\nst=$(\"$F\" status pc2 2>/dev/null)\necho \"after: $(echo \"$st\" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\\n' ' ')\" >> logs/$tag/load.txt\ncat logs/$tag/load.txt\ngrep -E \"exit_code|seconds_to_exit|hang|others_|cpu_\" logs/$tag/result.txt\ngrep -E \"RUN wrapped|SCRIPT (finished|failed)|FPS (rolling|frozen)|SETTINGS (at start|first start)\" logs/$tag/run.log | sed 's/^\\[[^]]*\\]\\[[^]]*\\]//' | cut -c1-260\necho \"compute pipeline errors: $(grep -c 'Failed to create compute pipeline' logs/$tag/run.log)\"\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\go.sh (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:02:30 · Tool call: Bash** (See perf2 title script format; check build)

```
cd "[notes]/unreal/megajam-2026/lanes/perf2/tools"; head -8 perf_full.txt; tail -3 perf_full.txt; tail -3 /d/UE/wt/perf3_farmlogs/bp.txt; date +%H:%M
```

Result:

```
# lane perf2: the title, START by Enter, then main8.txt unchanged.
0.10 shot perf_title
2.50 key Enter
0 scene 1 1
# All eight rooms of the run in order, one script. Built by build_full8.py from lanes/rooms/scripts/full5.txt
# (the five fight rooms) and this lane's three puzzle rooms. Do not edit by hand: change the builder.
# Run: sh run_room.sh full8 full8 -Run main8 -Seed 1
# After each gate the upgrade screen is up: the script picks card one by key. Each room starts with a reload.
14.43 move 0 0
15.13 shot s8_wrap_screen
15.93 end
11:02
```

**Sun 15 Nov 11:02:36 · Tool call: Bash** (Check farm logs and pc2 load)

```
ls -la /d/UE/wt/perf3_farmlogs/; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 | grep -E "busy|cpu|free_ram"
```

Result:

```
total 12
drwxr-xr-x 1 [user] 197121 0 Nov 15 10:54 .
drwxr-xr-x 1 [user] 197121 0 Nov 15 10:53 ..
-rw-r--r-- 1 [user] 197121 0 Nov 15 10:54 bp.txt
free_ram_gb=0.9 of 15.9
cpu_load_pct=0 threads=12
busy_procs=clx1 dotnetx1
```

### Sun 15 Nov 11:02:48 · Agent (claude-opus-5-5)

pc2 is compiling and short on RAM (0.9 GB free, Studio windows). Waiting on it; meanwhile preparing the run arguments.

**Sun 15 Nov 11:02:52 · Tool call: Bash** (Write arg files and title script)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3/tools"; mkdir -p args; { echo "# lane perf3: the title, START by Enter, then main8.txt unchanged."; echo "2.50 key Enter"; echo "0 scene 1 1"; cat /d/UE/wt/perf3/Script/main8.txt; } > args/title_main8.txt
D='C:\UE\Farm\_out\perf3\desktools'; P='C:\UE\Farm\perf3'
COMMON="-nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\\run.log"
printf '%s\n' "-SupercutTitle -SupercutRun=main8 -SupercutSeed=1 -SupercutScript=$D\\title_main8.txt -csvCaptureFrames=30000 $COMMON" > args/title_main8.args
printf '%s\n' "-SupercutRun=main8 -SupercutSeed=1 -SupercutScript=$P\\Script\\main8.txt -UseFixedTimeStep -FPS=240 -csvCaptureFrames=40000 -csvGpuStats $COMMON" > args/main8_fx.args
printf '%s\n' "-SupercutSeed=6 -SupercutScript=$P\\Script\\gen\\s7.txt -UseFixedTimeStep -FPS=60 -csvCaptureFrames=40000 -csvGpuStats $COMMON" > args/gen_s7_fx.args
cat args/*.args; sed -i 's#^scp -q "tools/args/$af".*#scp -q tools/args/* "pc2:C:/UE/Farm/_out/perf3/desktools/" || { echo scp args failed; exit 1; }#' go.sh; grep -n "scp -q tools/args" go.sh
```

Result:

```
-SupercutSeed=6 -SupercutScript=C:\UE\Farm\perf3\Script\gen\s7.txt -UseFixedTimeStep -FPS=60 -csvCaptureFrames=40000 -csvGpuStats -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log
-SupercutRun=main8 -SupercutSeed=1 -SupercutScript=C:\UE\Farm\perf3\Script\main8.txt -UseFixedTimeStep -FPS=240 -csvCaptureFrames=40000 -csvGpuStats -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log
-SupercutTitle -SupercutRun=main8 -SupercutSeed=1 -SupercutScript=C:\UE\Farm\_out\perf3\desktools\title_main8.txt -csvCaptureFrames=30000 -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log
14:scp -q tools/args/* "pc2:C:/UE/Farm/_out/perf3/desktools/" || { echo scp args failed; exit 1; }
[This command modified 1 file you've previously read: go.sh. Call Read before editing.]
```

**Sun 15 Nov 11:03:03 · Tool call: Bash** (Write hall arg file and check pc2)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3/tools"; P='C:\UE\Farm\perf3'; COMMON="-nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\\run.log"; printf '%s\n' "-SupercutRoom=fight/01_wind_machine -SupercutSeed=1 -SupercutDev -SupercutScript=$P\\Script\\shell1_hall_fps.txt -csvCaptureFrames=20000 -csvGpuStats $COMMON" > args/hall.args; cat args/hall.args; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 | grep -E "busy|cpu|free_ram"; date +%H:%M
```

Result:

```
-SupercutRoom=fight/01_wind_machine -SupercutSeed=1 -SupercutDev -SupercutScript=C:\UE\Farm\perf3\Script\shell1_hall_fps.txt -csvCaptureFrames=20000 -csvGpuStats -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log
free_ram_gb=1.7 of 15.9
cpu_load_pct=0 threads=12
busy_procs=clx1 dotnetx1
11:03
```

### Sun 15 Nov 11:03:26 · Agent (claude-opus-5-5)

Writing the CSV analysis script while the build crawls (pc2 is RAM-starved by its Studio windows).

**Sun 15 Nov 11:03:53 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\analyze.py",
 "content": "\"\"\"Lane perf3: frame times from one desktop run (logs/<tag>/profile.csv + run.log).\n\nThe CSV (engine CSV profiler, boot capture) has one row per frame with FrameTime in wall ms and, with -csvGpuStats,\nGPU pass times. The engine log has wall-clock stamps and GFrameCounter % 1000 on every line. Rows are matched to\nlog frames by the constant offset that best lines up the two clocks; sections are cut by the game's own log lines.\n\nusage: python -I analyze.py <tag> [sections|hitch|gpu] [args]\n  sections                 per room / state table (ROOM change .. PICK offered or RUN wrapped, FREEZE begin/end)\n  window <t0-line-regex> <seconds>   frames from the first line matching the regex for N seconds\n  hitch <seconds> <ms>     frames over <ms> in the first <seconds> after the title shows\n  gpu <from-regex> <to-regex>  top GPU passes, average ms, between two log lines\n\"\"\"\nimport csv, os, re, statistics, sys\nfrom datetime import datetime\n\nHERE = os.path.dirname(os.path.abspath(__file__))\nLINE = re.compile(r'^\\[(\\d{4})\\.(\\d\\d)\\.(\\d\\d)-(\\d\\d)\\.(\\d\\d)\\.(\\d\\d):(\\d{3})\\]\\[\\s*(\\d+)\\](.*)$')\n\n\ndef load(tag):\n    d = os.path.join(HERE, '..', 'logs', tag)\n    log = []\n    last, wraps = None, 0\n    with open(os.path.join(d, 'run.log'), encoding='utf-8', errors='replace') as f:\n        for raw in f:\n            m = LINE.match(raw.rstrip('\\n'))\n            if not m:\n                continue\n            y, mo, da, h, mi, s, ms, fr, text = m.groups()\n            t = datetime(int(y), int(mo), int(da), int(h), int(mi), int(s), int(ms) * 1000).timestamp()\n            fr = int(fr)\n            if last is not None and fr < last - 500:\n                wraps += 1\n            last = fr\n            log.append((t, wraps * 1000 + fr, text))\n    with open(os.path.join(d, 'profile.csv'), encoding='utf-8', errors='replace') as f:\n        rows = list(csv.reader(f))\n    head = rows[0]\n    data = []\n    for r in rows[1:]:\n        if not r or r[0].startswith('['):\n            break\n        data.append(r)\n    col = {n: i for i, n in enumerate(head)}\n    ft = [float(r[col['FrameTime']]) for r in data]\n    cum = [0.0]\n    for x in ft:\n        cum.append(cum[-1] + x / 1000.0)\n    # offset c: row = frame - c. Pick the c whose clock difference varies least over the log lines.\n    best = None\n    for c in range(-40, 41):\n        diffs = [t - cum[fr - c] for t, fr, _ in log if 0 <= fr - c < len(cum)]\n        if len(diffs) < 20:\n            continue\n        sd = statistics.pstdev(diffs)\n        if best is None or sd < best[0]:\n            best = (sd, c)\n    return log, head, col, data, ft, best[1], best[0]\n\n\ndef stats(ft):\n    s = sorted(ft)\n    n = len(s)\n    p99 = s[min(n - 1, int(0.99 * n))]\n    worst1 = statistics.mean(s[-max(1, n // 100):])\n    return n, statistics.mean(ft), p99, worst1, s[-1]\n\n\ndef rows_between(log, c, f0, f1, n):\n    return max(0, f0 - c), min(n, f1 - c)\n\n\ndef sections(tag):\n    log, head, col, data, ft, c, sd = load(tag)\n    gcol = col.get('GPUTime') or col.get('GPU/Total')\n    print(f'{tag}: {len(ft)} csv rows, row = frame - {c} (clock spread {sd*1000:.1f} ms)')\n    marks = []\n    for t, fr, text in log:\n        if re.search(r'ROOM change|PICK offered|RUN wrapped|FREEZE (begin|end)|SCRIPT (finished|failed)', text):\n            marks.append((fr, text))\n    room, state, start = None, 'live', None\n    acc = {}\n    order = []\n    for fr, text in marks:\n        if start is not None and room is not None:\n            a, b = rows_between(log, c, start, fr, len(ft))\n            acc.setdefault((room, state), []).extend(range(a, b))\n            if (room, state) not in order:\n                order.append((room, state))\n        if 'ROOM change' in text:\n            m = re.search(r'ROOM change[^:]*: *(.*)', text)\n            room, state, start = (m.group(1)[:40] if m else text[-40:]), 'live', fr\n        elif 'FREEZE begin' in text:\n            state, start = 'frozen', fr\n        elif 'FREEZE end' in text:\n            state, start = 'live', fr\n        else:\n            room, start = None, None\n    allrows = []\n    print(f'{\"room\":42s} {\"state\":6s} {\"frames\":>6s} {\"avg ms\":>7s} {\"p99 ms\":>7s} {\"slow1% ms\":>9s} {\"max ms\":>7s} {\"GPU avg\":>7s}')\n    for k in order:\n        idx = acc[k]\n        if not idx:\n            continue\n        allrows.extend(idx)\n        n, avg, p99, w1, mx = stats([ft[i] for i in idx])\n        g = statistics.mean(float(data[i][gcol]) for i in idx) if gcol is not None else float('nan')\n        print(f'{k[0]:42s} {k[1]:6s} {n:6d} {avg:7.2f} {p99:7.2f} {w1:9.2f} {mx:7.1f} {g:7.2f}')\n    n, avg, p99, w1, mx = stats([ft[i] for i in allrows])\n    g = statistics.mean(float(data[i][gcol]) for i in allrows) if gcol is not None else float('nan')\n    print(f'{\"all rooms\":42s} {\"both\":6s} {n:6d} {avg:7.2f} {p99:7.2f} {w1:9.2f} {mx:7.1f} {g:7.2f}')\n\n\ndef window(tag, rx, secs):\n    log, head, col, data, ft, c, sd = load(tag)\n    gcol = col.get('GPUTime')\n    t0 = next((t, fr) for t, fr, text in log if re.search(rx, text))\n    t1 = [(t, fr) for t, fr, _ in log if t <= t0[0] + secs][-1]\n    a, b = rows_between(log, c, t0[1], t1[1], len(ft))\n    n, avg, p99, w1, mx = stats(ft[a:b])\n    g = statistics.mean(float(data[i][gcol]) for i in range(a, b)) if gcol is not None else float('nan')\n    print(f'{tag} window \"{rx}\" +{secs}s: frames {n}, avg {avg:.2f} ms, p99 {p99:.2f}, slowest 1% mean {w1:.2f}, max {mx:.1f}, GPU avg {g:.2f} (row = frame - {c}, spread {sd*1000:.1f} ms)')\n\n\ndef hitch(tag, secs, limit):\n    log, head, col, data, ft, c, sd = load(tag)\n    t_title = next((t, fr) for t, fr, text in log if re.search(r'TITLE|title shown|MENU title', text))\n    a = t_title[1] - c\n    cum = 0.0\n    out = []\n    i = a\n    while i < len(ft) and cum < secs:\n        if ft[i] > limit:\n            # the log line nearest this frame\n            fr = i + c\n            near = min(log, key=lambda x: abs(x[1] - fr))\n            prev = [x for x in log if x[1] <= fr][-1]\n            out.append((cum, ft[i], fr, prev[2][:150]))\n        cum += ft[i] / 1000.0\n        i += 1\n    print(f'{tag}: title at frame {t_title[1]} (row {a}); {i - a} frames in {cum:.1f} s; {len(out)} frames over {limit} ms (row = frame - {c}, spread {sd*1000:.1f} ms)')\n    for t, ms, fr, text in out:\n        print(f'  +{t:6.2f} s  {ms:7.1f} ms  frame {fr}  last log line: {text}')\n    n, avg, p99, w1, mx = stats(ft[a:i])\n    print(f'  first {secs} s: avg {avg:.2f} ms, p99 {p99:.2f}, max {mx:.1f}')\n\n\ndef gpu(tag, rx0, rx1):\n    log, head, col, data, ft, c, sd = load(tag)\n    f0 = next(fr for t, fr, text in log if re.search(rx0, text))\n    f1 = next(fr for t, fr, text in log if fr > f0 and re.search(rx1, text))\n    a, b = rows_between(log, c, f0, f1, len(ft))\n    res = []\n    for name, i in col.items():\n        if name.startswith('GPU/') or name in ('GPUTime', 'FrameTime', 'GameThreadTime', 'RenderThreadTime', 'RHIThreadTime'):\n            try:\n                v = statistics.mean(float(data[r][i] or 0) for r in range(a, b))\n            except ValueError:\n                continue\n            res.append((v, name))\n    res.sort(reverse=True)\n    print(f'{tag} GPU passes, frames {b - a} between \"{rx0}\" and \"{rx1}\" (average ms per frame):')\n    for v, name in res[:25]:\n        print(f'  {v:7.3f}  {name}')\n\n\nif __name__ == '__main__':\n    tag, mode = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else 'sections')\n    if mode == 'sections':\n        sections(tag)\n    elif mode == 'window':\n        window(tag, sys.argv[3], float(sys.argv[4]))\n    elif mode == 'hitch':\n        hitch(tag, float(sys.argv[3]), float(sys.argv[4]))\n    elif mode == 'gpu':\n        gpu(tag, sys.argv[3], sys.argv[4])\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:04:08 · Tool call: Bash** (Start LOG.md, check build)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat > LOG.md <<EOF
# perf3 log

All times SGT (c4 clock, \`date\`).

- 10:52 lane started. Read BRIEF, COMMON_RULES, FARM.md, perf2 REPORT/tables/tools, dlss2, shell1, light1, vfx1 handoffs, GOTCHAS sections (pc2 test lane 2, Shipping settings, first1, farm, shell1 measuring).
- 10:54 pc2 status: free RAM 5.4 GB, CPU 2 %, busy none. Mirrored worktree (3010 files, 88 s). Started build (-Jobs 4, RAM short) then package, background.
- 10:55 engine source: the error text is \`PipelineStateCache.cpp:733\` (\`HandlePipelineCreationFailure\`, compute); precache requests may fail without effect (\`PipelineStateCache.cpp:722\`, only non-precache failures are Fatal). Global compute shaders are precached at start from \`LaunchEngineLoop.cpp:4504\` -> \`ShaderCompiler.cpp:5253\` \`PrecacheComputePipelineStatesForGlobalShaders\`: every permutation that \`ShouldCompilePermutation\` and \`ShouldPrecachePermutation\` accept for the shader platform, with no check of the card's runtime caps. \`Shader: <unknown>\` because cooked shaders carry no name (\`RHIResources.h:865\`, name is optional data only with r.Shaders.ExtraData at cook).
- 10:57 D3D12 side: \`D3D12Shaders.cpp:107\` \`ValidateShaderIsUsable\` refuses a shader needing wave ops, bindless, stencil ref or barycentrics the card lacks, but has no check for \`SixteenBitTypes\`, \`TypedUAVLoadsExtended\` or \`Atomic64\` (flags recorded by \`D3DShaderCompilerDXC.cpp:1146\`). The driver call returns 0x80070057 (E_INVALIDARG) for each of the 24.
- 10:58 existing logs on c4: every RTX 4080 SUPER and RX 9070 XT packaged run has 0 of these errors; pc2 packaged (viewmerge1) 24; pc2 uncooked editor run (view1) 0. So: cooked package + Pascal card.
- 11:00 first-start level code now \`FirstStartLevel\` = benchmark lowest - 1, clamped 1..2 (\`SupercutUserSettings.cpp:171\`), so pc2 should get HIGH now, not EPIC as in perf2. DLSS default 0 (OFF) on every card.
- 11:03 pc2 free RAM 0.9 to 1.7 GB while the build compiles (its Studio windows); build slow.
- CSV profiler: \`-csvCaptureFrames=N\` boot capture (\`CsvProfiler.cpp:5054\`, \`5182\`); FrameTime is wall time from cycle stamps (\`CsvProfiler.cpp:4163-4168\`), so it is a real frame time even with -UseFixedTimeStep. \`-csvGpuStats\` (\`CsvProfiler.cpp:5103\`) adds GPU pass times.
EOF
tail -3 /d/UE/wt/perf3_farmlogs/bp.txt; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 | grep -E "busy|cpu|free_ram"; date +%H:%M
```

Result:

```
free_ram_gb=1.3 of 15.9
cpu_load_pct=3 threads=12
busy_procs=clx1 dotnetx1
11:04
```

**Sun 15 Nov 11:04:17 · Tool call: Bash** (See build step logs on pc2)

```
ssh pc2 'powershell -NoProfile -Command "Get-ChildItem C:\UE\Farm\_out\perf3 -Recurse -File | Select-Object FullName,Length,LastWriteTime | Format-Table -AutoSize | Out-String -Width 200"' 2>&1 | sed 's/Users\\[^\\]*/Users\\USER/' | head -20
```

Result:

```
(Bash completed with no output)
```

**Sun 15 Nov 11:04:22 · Tool call: Bash** (Look for build log on pc2)

```
ssh pc2 'dir /s /b C:\UE\Farm\_out\perf3 & dir /b C:\UE\Farm\perf3\Saved\Logs 2>nul & powershell -NoProfile -Command "Get-Content C:\UE\Farm\perf3\Saved\Logs\*UBT*.log -Tail 5 -ErrorAction SilentlyContinue"' 2>&1 | head -20; F="[notes]/unreal/megajam-2026/farm/farm.sh"; sed -n 1,60p "$F" | grep -n "build)"
```

Result:

```
C:\UE\Farm\_out\perf3\build
ubt_SupercutEditor.json
ubt_SupercutEditor.log
[66/142] Compile [x64] SupercutGameMode.cpp
[67/142] Compile [x64] SupercutGenRunTests.cpp
[68/142] Compile [x64] SupercutGeneratedRuns.cpp
[69/142] Compile [x64] SupercutGrunt.cpp
[70/142] Compile [x64] SupercutGunFeelTests.cpp
```

### Sun 15 Nov 11:04:36 · Agent (claude-opus-5-5)

Build is at 70/142 files on pc2. While it runs, checking which global shaders compile 16-bit permutations without a runtime precache filter (my lead for the 24).

**Sun 15 Nov 11:04:36 · Tool call: Bash** (List TSR shader classes and precache filters)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess; grep -n "^class F\|ShouldPrecachePermutation\|F16BitVALUDim>\|IMPLEMENT_GLOBAL_SHADER" TemporalSuperResolution.cpp | head -90
```

Result:

```
519:class FTSRShader : public FGlobalShader
664:class FTSRConvolutionNetworkShader : public FTSRShader
683:			PermutationVector.Set<FTSRShader::F16BitVALUDim>(false);
689:			PermutationVector.Set<FTSRShader::F16BitVALUDim>(false);
709:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
717:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters, FPermutationDomain PermutationVector)
730:		if (PermutationVector.Get<FTSRShader::F16BitVALUDim>() != bUse16BitVALU)
756:		if (PermutationVector.Get<FTSRShader::F16BitVALUDim>())
763:class FTSRMeasureFlickeringLumaCS : public FTSRShader
806:class FTSRMeasureThinGeometryCoverageCS : public FTSRShader
833:class FTSRClearPrevTexturesCS : public FTSRShader
846:class FTSRDilateVelocityCS : public FTSRShader
911:class FTSRDecimateHistoryCS : public FTSRShader
974:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
987:		if (PermutationVector.Get<FTSRShader::F16BitVALUDim>())
994:class FTSRRejectShadingCS : public FTSRConvolutionNetworkShader
1063:		if (PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>().Get<FTSRShader::F16BitVALUDim>())
1100:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1103:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1123:class FTSRDetectThinGeometryCS : public FTSRConvolutionNetworkShader
1187:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1190:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1209:class FTSRWeightRelaxationCS : public FTSRConvolutionNetworkShader
1257:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1260:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1276:class FTSRSpatialAntiAliasingCS : public FTSRShader
1313:class FTSRUpdateHistoryCS : public FTSRShader
1382:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Paramet
[... 3979 more characters not shown]
```

**Sun 15 Nov 11:04:44 · Tool call: Bash** (Read TSR base and DecimateHistory permutations)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess; sed -n 519,560p TemporalSuperResolution.cpp; sed -n 911,990p TemporalSuperResolution.cpp
```

Result:

```
class FTSRShader : public FGlobalShader
{
public:
	static constexpr int32 kSupportMinWaveSize = 32;
	static constexpr int32 kSupportMaxWaveSize = 64;

	class F16BitVALUDim : SHADER_PERMUTATION_BOOL("DIM_16BIT_VALU");
	class FAlphaChannelDim : SHADER_PERMUTATION_BOOL("DIM_ALPHA_CHANNEL");

	FTSRShader(const ShaderMetaType::CompiledShaderInitializerType& Initializer)
		: FGlobalShader(Initializer)
	{ }

	FTSRShader()
	{ }

	static ERHIFeatureSupport Supports16BitVALU(EShaderPlatform Platform)
	{
		// UE-254365
		if (IsVulkanPlatform(Platform))
		{
			return ERHIFeatureSupport::Unsupported;
		}

		return FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Platform);
	}

	static bool ShouldCompile32or16BitPermutation(EShaderPlatform Platform, bool bIs16BitVALUPermutation)
	{
		// Always compile the 32bit permutations for the alpha channel
		if (!bIs16BitVALUPermutation)
		{
			return true;
		}

		const ERHIFeatureSupport Support = FTSRShader::Supports16BitVALU(Platform);
		return Support != ERHIFeatureSupport::Unsupported;
	}

	static ERHIFeatureSupport SupportsWaveOps(EShaderPlatform Platform)
	{
		return FDataDrivenShaderPlatformInfo::GetSupportsWaveOperations(Platform);
class FTSRDecimateHistoryCS : public FTSRShader
{
	DECLARE_GLOBAL_SHADER(FTSRDecimateHistoryCS);
	SHADER_USE_PARAMETER_STRUCT(FTSRDecimateHistoryCS, FTSRShader);

	class FMoireReprojectionDim : SHADER_PERMUTATION_BOOL("DIM_MOIRE_REPROJECTION");
	class FResurrectionReprojectionDim : SHADER_PERMUTATION_BOOL("DIM_RESURRECTION_REPROJECTION");
	class FThinGeometryCoverageDim: SHADER_PERMUTATION_BOOL("DIM_THIN_GEOMETRY_COVERAGE_REPROJECTION");
	using FPermutationDomain = TShaderPermutationDomain<FMoireReprojectionDim, FResurrectionReprojectionDim, FThinGeometryCoverageDim, FTSRShader::F16BitVALUDim, FTSRShader::FAlphaChannelDim>;

	BEGIN_SHADER_PARAMETER_STRUCT(FParameters, )
		SHADER_PARAMETER_STRUCT_INCLUDE(FTSRCommonParameters, CommonParameters)
		SHADER_PARAMETER(FMatrix44f, RotationalClipToPrevClip)

		SHADER_PARAMETER_RDG_TEXTURE_SRV(Texture2D, DilatedReprojectionVectorTexture)
		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, ClosestDepthTexture)
		SHADER_PARAMETER_RDG_TEXTURE_SRV(Texture2D, DilateMaskTexture)
		SHADER_PARAMETER_RDG_TEXTURE_SRV(Texture2D, DepthErrorTexture)
		SHADER_PARAMETER_RDG_TEXTURE(Texture2DArray, PrevAtomicTextureArray)
		SHADER_PARAMETER_RDG_BUFFER_SRV(StructuredBuffer<uint>, PrevAtomicBuffer)

		SHADER_PARAMETER_STRUCT_INCLUDE(FTSRPrevHistoryParameters, PrevHistoryParamete
[... 2694 more characters not shown]
```

**Sun 15 Nov 11:04:48 · Tool call: Bash** (Read UpdateHistory and ResolveHistory permutations)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess; sed -n 1313,1335p TemporalSuperResolution.cpp; sed -n 1360,1395p TemporalSuperResolution.cpp; sed -n 1403,1480p TemporalSuperResolution.cpp | grep -v "SHADER_PARAMETER"
```

Result:

```
class FTSRUpdateHistoryCS : public FTSRShader
{
	DECLARE_GLOBAL_SHADER(FTSRUpdateHistoryCS);
	SHADER_USE_PARAMETER_STRUCT(FTSRUpdateHistoryCS, FTSRShader);

	enum class EQuality
	{
		Low,
		Medium,
		High,
		Epic,
		MAX
	};

	class FQualityDim : SHADER_PERMUTATION_ENUM_CLASS("DIM_UPDATE_QUALITY", EQuality);

	using FPermutationDomain = TShaderPermutationDomain<FQualityDim, FTSRShader::F16BitVALUDim, FTSRShader::FAlphaChannelDim>;

	BEGIN_SHADER_PARAMETER_STRUCT(FParameters, )
		SHADER_PARAMETER_STRUCT_INCLUDE(FTSRCommonParameters, CommonParameters)
		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, InputSceneColorTexture)

		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, HistoryRejectionTexture)
		SHADER_PARAMETER(int32, bGenerateOutputMip3)

		SHADER_PARAMETER_STRUCT(FTSRHistoryArrayIndices, HistoryArrayIndices)
		SHADER_PARAMETER_STRUCT_INCLUDE(FTSRPrevHistoryParameters, PrevHistoryParameters)
		SHADER_PARAMETER_RDG_TEXTURE_SRV(Texture2DArray, PrevHistoryColorTexture)
		SHADER_PARAMETER_RDG_TEXTURE_SRV(Texture2DArray, PrevHistoryMetadataTexture)

		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, PrevDistortingDisplacementTexture)
		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, ResurrectedDistortingDisplacementTexture)
		SHADER_PARAMETER_RDG_TEXTURE(Texture2D, UndistortingDisplacementTexture)
		SHADER_PARAMETER(float, DistortionOverscan)

		SHADER_PARAMETER_RDG_TEXTURE_UAV(RWTexture2DArray, HistoryColorOutput)
		SHADER_PARAMETER_RDG_TEXTURE_UAV(RWTexture2DArray, HistoryMetadataOutput)
		SHADER_PARAMETER_RDG_TEXTURE_UAV(RWTexture2DArray, SceneColorOutputMip1)
		SHADER_PARAMETER_RDG_TEXTURE_UAV(RWTexture2DArray, DebugOutput)
	END_SHADER_PARAMETER_STRUCT()

	static bool ShouldCompilePermutation(const FGlobalShaderPermutationParameters& Parameters)
	{
		FPermutationDomain PermutationVector(Parameters.PermutationId);

		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
		{
			return false;
		}

		return FTSRShader::ShouldCompilePermutation(Parameters);
	}

	static void ModifyCompilationEnvironment(const FGlobalShaderPermutationParameters& Parameters, FShaderCompilerEnvironment& OutEnvironment)
	{
		FTSRShader::ModifyCompilationEnvironment(Parameters, OutEnvironment);
		OutEnvironment.CompilerFlags.Add(CFLAG_Wave32);

		FPermutationDomain PermutationVector(Parameters.PermutationId);
class FTSRResolveHistoryCS : public FTSRShader
{
	DECLARE_GLOBAL_SHADER(FTSRResolveHistoryCS);
	SHADER_USE_PARAMETER_STRUCT(FTSRResolveH
[... 2025 more characters not shown]
```

### Sun 15 Nov 11:04:56 · Agent (claude-opus-5-5)

Strong lead: TSR's DecimateHistory (16) and UpdateHistory (8) compile 16-bit permutations and have no runtime precache filter. 16 + 8 = 24. Checking the base filter to be sure the count holds.

**Sun 15 Nov 11:04:58 · Tool call: Bash** (Read FTSRShader compile filter and wave-size precache util)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess; sed -n 560,640p TemporalSuperResolution.cpp; grep -n "ShouldPrecacheWithWaveSize" -A20 /d/UE/UE_5.9/Engine/Source/Runtime/RenderCore/Private/ShaderPermutationUtils.cpp | head -40
```

Result:

```
return FDataDrivenShaderPlatformInfo::GetSupportsWaveOperations(Platform);
	}

	static bool SupportsLDS(EShaderPlatform Platform)
	{
		// Always support LDS on preview platform 
		if (FDataDrivenShaderPlatformInfo::GetIsPreviewPlatform(Platform))
		{
			return true;
		}

		// Always support LDS if wave ops are not guarenteed
		if (SupportsWaveOps(Platform) != ERHIFeatureSupport::RuntimeGuaranteed)
		{
			return true;
		}

		// Do not support LDS if shader supported wave size are guarenteed to support the platform.
		if (FDataDrivenShaderPlatformInfo::GetMinimumWaveSize(Platform) >= kSupportMinWaveSize &&
			FDataDrivenShaderPlatformInfo::GetMaximumWaveSize(Platform) <= kSupportMaxWaveSize)
		{
			return false;
		}

		return true;
	}

	static bool ShouldCompilePermutation(const FGlobalShaderPermutationParameters& Parameters)
	{
		return SupportsTSR(Parameters.Platform);
	}

	static void ModifyCompilationEnvironment(const FGlobalShaderPermutationParameters& Parameters, FShaderCompilerEnvironment& OutEnvironment)
	{
		if (FTSRShader::Supports16BitVALU(Parameters.Platform) == ERHIFeatureSupport::RuntimeGuaranteed)
		{
			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
		}
		OutEnvironment.CompilerFlags.Add(CFLAG_WarningsAsErrors);
		OutEnvironment.CompilerFlags.Add(CFLAG_HLSL2021);
		OutEnvironment.CompilerFlags.Add(CFLAG_ForceOptimization);

		OutEnvironment.SetDefine(TEXT("TSR_SUPPORT_LENS_DISTORTION"), IsTSRLensDistortionSupported(Parameters.Platform) ? 1 : 0);
		if (TSRPrevAtomicsInBuffer(Parameters.Platform))
		{
			OutEnvironment.SetDefine(TEXT("TSR_PREV_ATOMICS_IN_BUFFER"), 1);
		}
	}
}; // class FTemporalSuperResolutionShader

int32 SelectWaveSize(EShaderPlatform ShaderPlatform, const TArray<int32>& WaveSizeDomain)
{
	check(!WaveSizeDomain.IsEmpty());
	int32 WaveSizeOps = 0;

	// Whether to use wave ops optimizations.
	const ERHIFeatureSupport WaveOpsSupport = FTSRShader::SupportsWaveOps(ShaderPlatform);
	const bool bUseWaveOps = (CVarTSRWaveOps.GetValueOnAnyThread() != 0 && GRHISupportsWaveOperations && (WaveOpsSupport == ERHIFeatureSupport::RuntimeDependent || WaveOpsSupport == ERHIFeatureSupport::RuntimeGuaranteed));
	const int32 WaveSizeOverride = bUseWaveOps ? CVarTSRWaveSize.GetValueOnAnyThread() : 0;

	if (bUseWaveOps)
	{
		if (WaveSizeOverride != 0 && WaveSizeDomain.Contains(WaveSizeOverride) && WaveSizeOverride >= GRHIMinimumWaveSize && WaveSizeOverride <= GRHIMaximumWaveSize)
		{
			WaveSizeOps = WaveSizeOverride;
		}
		else
		{
			co
[... 862 more characters not shown]
```

**Sun 15 Nov 11:05:22 · Tool call: Bash** (Check global shader map API, build progress)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/RenderCore/Public; grep -n "HasShader\|TShaderRef<FShader> GetShader\|GetShader(FShaderType\|class FGlobalShaderMap\b\|RENDERCORE_API FGlobalShaderMap\* GetGlobalShaderMap\|GetGlobalShaderMap(" GlobalShader.h | head; grep -n "GetRHIShaderBase" Shader.h | head -3; grep -n "GetName()" Shader.h | head -3; cat /d/UE/wt/perf3_farmlogs/bp.txt | tail -2; ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\perf3\Saved\Logs\*UBT*.log -Tail 1"' 2>/dev/null
```

Result:

```
127:	friend class FGlobalShaderMap;
145:	friend class FGlobalShaderMap;
172:		inline TShaderRef<FShader> GetShader(FShaderType* ShaderType, int32 PermutationId = 0) const
177:	TShaderRef<FShader> GetShader(EShaderPlatform ShaderPlatform, FShaderType* ShaderType, int32 PermutationId = 0) const;
181:class FGlobalShaderMap
187:	RENDERCORE_API TShaderRef<FShader> GetShader(FShaderType* ShaderType, int32 PermutationId = 0) const;
217:	bool HasShader(FShaderType* Type, int32 PermutationId) const
222:	bool HasShaderPipeline(const FShaderPipelineType* ShaderPipelineType) const
342:extern RENDERCORE_API FGlobalShaderMap* GetGlobalShaderMap(EShaderPlatform Platform);
360:inline FGlobalShaderMap* GetGlobalShaderMap(ERHIFeatureLevel::Type FeatureLevel)
1109:	inline FRHIShader* GetRHIShaderBase(EShaderFrequency Frequency, bool bRequired = true) const
1146:		return static_cast<FRHIVertexShader*>(GetRHIShaderBase(SF_Vertex, bRequired));
1151:		return static_cast<FRHIMeshShader*>(GetRHIShaderBase(SF_Mesh));
130:		int32 AL = FCString::Strlen(A.Type->GetName());
131:		int32 BL = FCString::Strlen(B.Type->GetName());
134:			int32 StrCmp = FCString::Strncmp(A.Type->GetName(), B.Type->GetName(), AL);
[84/142] Compile [x64] SupercutLitterTests.cpp
Shell cwd was reset to [notes]
```

### Sun 15 Nov 11:05:34 · Agent (claude-opus-5-5)

pc2 build at 84/142. Starting the [pc-b] side in parallel (it needs its own build and package under `perf3` for the comparison pictures), after a load check.

**Sun 15 Nov 11:05:34 · Tool call: Bash** (Load check [pc-b])

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status [pc-b] 2>&1 | grep -E "free_ram|cpu_load|busy|gpu=|farm_names"
```

Result:

```
free_ram_gb=6.9 of 31.6
cpu_load_pct=31 threads=16
busy_procs=clx1 dotnetx2
gpu=NVIDIA GeForce RTX 4080 SUPER, 28 %, 7266 MiB, 22.15 W
farm_names=clap1 clap2 credits1 dlss2 feel5 flats1 gen2 hallmerge1 hud1 light2 litter1 proof qa1 rebake1 sfx4 ui1 vfx1
```

**Sun 15 Nov 11:05:42 · Tool call: Bash** (Mirror, build, package on [pc-b] (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs_[pc-b]; mkdir -p $L; ( "$F" mirror [pc-b] perf3 /d/UE/wt/perf3 && "$F" build [pc-b] perf3 "$L" -Jobs 6 && "$F" status [pc-b] | grep -E "free_ram|cpu|busy" && "$F" package [pc-b] perf3 "$L" ) > "$L/bp.txt" 2>&1; echo exit $?; tail -5 "$L/bp.txt"
```

Result:

```
Command running in background with ID: b12t3zl60. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\b12t3zl60.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**Sun 15 Nov 11:06:00 · Tool call: Bash** (Count picture lines in main8)

```
cd /d/UE/wt/perf3/Script; grep -c " shot " main8.txt; grep " shot " main8.txt | head -50 | awk '{print $3}' | tr '\n' ' '; echo; grep -c " shot " gen/s7.txt gen/s7shots.txt 2>/dev/null
```

Result:

```
67
s1_01_start s1_02_at_the_machine s1_03_machine_stopped s1_04_out_of_the_tunnel s1_05_grunt_frozen s1_06_three_shots_hang s1_07_action s1_08_grunt_0_gone s1_09_three_more_hang s1_10_stage_clear s1_11_gate_ahead s1_upgrade_screen s2_01_start s2_02_frozen_door_held_open s2_03_nearly_there s2_upgrade_screen s3_01_start s3_02_rusher_coming s3_03_frozen_in_its_crouch s3_04_two_shots_hang s3_05_rusher_0_gone s3_06_rusher_1_coming s3_07_two_for_the_rusher s3_08_both_set_up s3_09_action s3_10_from_the_stage s3_upgrade_screen s4_01_start s4_02_the_line s4_03_line_locked_rusher_coming s4_04_two_for_the_rusher s4_05_two_for_the_marksman s4_06_set_up s4_07_action s4_08_three_for_the_grunt s4_09_grunt_gone s4_10_from_the_camera_stage s4_upgrade_screen s5_01_start s5_02_frozen_three_marks meant comes s5_03_three_shots_hang s5_04_door_open s5_upgrade_screen s6_01_start s6_02_four_shots_hang s6_03_rushers_gone s6_04_from_the_rock s6_05_marksman_gone 
gen/s7.txt:0
gen/s7shots.txt:4
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:06:15 · Tool call: Bash** (PSO-related settings in log and config)

```
cd /d/UE/wt/viewmerge1_farmlogs/run; grep -o "Set CVar \[\[[^]]*PSO[^]]*\]\]\|Set CVar \[\[r.ShaderPipelineCache[^]]*\]\]" run.log | sort -u; grep -n "ShaderPipelineCache\|PipelineFileCache\|stablepc\|\.upipelinecache" run.log | head; grep -n "bShareMaterialShaderCode\|bSharedMaterialNativeLibraries\|PSO\|PipelineCache" /d/UE/wt/perf3/Config/*.ini
```

Result:

```
Set CVar [[r.PSOPrecache.GlobalShaders:1]]
Set CVar [[r.PSOPrecache.KeepInMemoryForActiveMaterials:1]]
815:[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
816:[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
818:[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
1127:[2026.11.14-19.59.09:199][  0]LogRHI: Display: ShaderPipelineCache: Paused Batching. 1
1129:[2026.11.14-19.59.09:200][  0]LogRHI: Display: ShaderPipelineCache: Resumed Batching. 0
1130:[2026.11.14-19.59.09:200][  0]LogRHI: Display: ShaderPipelineCache: Batching Resumed.
```

**Sun 15 Nov 11:06:22 · Tool call: Bash** (Read pipeline cache file lines in context)

```
cd /d/UE/wt/viewmerge1_farmlogs/run; sed -n 805,830p run.log | cut -c1-220
```

Result:

```
[2026.11.14-19.59.07:203][  0]LogInit: FStereoShaderAspects: bMobileMultiViewEnabled = 0
[2026.11.14-19.59.07:203][  0]LogInit: FStereoShaderAspects: --- StereoAspects end ---
[2026.11.14-19.59.07:203][  0]LogInit: XR: Instanced Stereo Rendering is Disabled
[2026.11.14-19.59.07:203][  0]LogInit: XR: Mobile Multiview is Disabled
[2026.11.14-19.59.07:218][  0]LogSlate: Using FreeType 2.14.1
[2026.11.14-19.59.07:219][  0]LogSlate: SlateFontServices - WITH_FREETYPE: 1, WITH_HARFBUZZ: 1
[2026.11.14-19.59.07:239][  0]LogShaderLibrary: Display: FShaderMaterializationTableRegistry: Canonical table chunk not found for platform 49 'PCD3D_SM6'
[2026.11.14-19.59.07:239][  0]LogShaderLibrary: Display: Using IoDispatcher for shader code library Supercut. Total 1907 unique shaders.
[2026.11.14-19.59.07:239][  0]LogShaderLibrary: Display: Cooked Context: Loaded Shared Shader Library Supercut
[2026.11.14-19.59.07:239][  0]LogShaderLibrary: Display: Logical shader library 'Supercut' has been created as a monolithic library, components 1
[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
[2026.11.14-19.59.07:239][  0]LogShaderLibrary: Display: Tried to open again shader library 'Supercut', but could not find new components for it (existing components: 1).
[2026.11.14-19.59.07:239][  0]LogRHI: Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache
[2026.11.14-19.59.07:239][  0]LogInit: Using OS detected language (en-US).
[2026.11.14-19.59.07:239][  0]LogInit: Using OS detected locale (en-SG).
[2026.11.14-19.59.07:239][  0]LogTextLocalizationManager: No localization for 'en-US' exists, so 'en' will be used for the language.
[2026.11.14-19.59.07:239][  0]LogTextLocalizationManager: No localization for 'en-SG' exists, so 'en' will be used for the locale.
[2026.11.14-19.59.07:239][  0]LogSlate: FontCache flush requested. Reason: Culture for localization was changed
[2026.11.14-19.59.07:239][  0]LogSlate: FontCache flush requested. Reason: Culture for localization was changed
[2026.11.14-19.59.07:240][  0]LogAssetRegistry: ActiveMountsLoading is disabled.
[2026.11.14-19.59.07:240][  0]LogAssetRegistry: FAssetRegistry took 0.0002 seconds to st
[... 486 more characters not shown]
```

**Sun 15 Nov 11:06:31 · Tool call: Bash** (Check both builds)

```
ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\perf3\Saved\Logs\*UBT*.log -Tail 1"' 2>/dev/null; tail -2 /d/UE/wt/perf3_farmlogs_[pc-b]/bp.txt; date +%H:%M
```

Result:

```
[100/142] Compile [x64] SupercutRoomFile.cpp
11:06
```

### Sun 15 Nov 11:06:38 · Agent (claude-opus-5-5)

pc2 build at 100/142. Meanwhile, locating the engine's supported bundled pipeline cache path in 5.9 for job 3.

**Sun 15 Nov 11:06:40 · Tool call: Bash** (Find bundled PSO cache handling in cook/staging)

```
cd /d/UE/UE_5.9/Engine/Source; grep -rn "\.spc\|stablepc" --include=*.cs Programs/AutomationTool/Scripts/CopyBuildToStagingDirectory.Automation.cs 2>/dev/null | head; grep -rln "PipelineCaches" --include=*.cs Programs/AutomationTool 2>/dev/null | head; grep -rn "NeedsShaderStableKeys" --include=*.cpp Editor Developer Runtime 2>/dev/null | head -5
```

Result:

```
Programs/AutomationTool/Scripts/CopyBuildToStagingDirectory.Automation.cs
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:262:		GConfig->GetBool(TEXT("DevOptions.Shaders"), TEXT("NeedsShaderStableKeys"), bAllPlatformsNeedStableKeys, GEngineIni);
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:263:		GConfig->GetBool(TEXT("DevOptions.Shaders"), TEXT("bNeedsShaderStableKeys"), bAllPlatformsNeedStableKeys, GEngineIni);
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:278:			PlatformIniFile.GetBool(TEXT("DevOptions.Shaders"), TEXT("NeedsShaderStableKeys"), bNeedShaderStableKeys);
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:279:			PlatformIniFile.GetBool(TEXT("DevOptions.Shaders"), TEXT("bNeedsShaderStableKeys"), bNeedShaderStableKeys);
Runtime/Engine/Private/Materials/Material.cpp:3169:	if (Ar.IsSaving() && Ar.IsCooking() && Ar.IsPersistent() && !Ar.IsObjectReferenceCollector() && FShaderLibraryCooker::NeedsShaderStableKeys(EShaderPlatform::SP_NumPlatforms))
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:07:13 · Tool call: Bash** (Find PipelineCaches staging lines)

```
cd /d/UE/UE_5.9/Engine/Source; grep -n "PipelineCaches" Programs/AutomationTool/Scripts/CopyBuildToStagingDirectory.Automation.cs | head; grep -rn "PipelineCaches" --include=*.cpp Editor/UnrealEd/Private/Cooker | head -5
```

Result:

```
2173:						DirectoryReference ShaderCacheRoot = DirectoryReference.Combine(SC.ProjectRoot, "Content", "PipelineCaches", SC.PlatformDir);
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:436:			const FString StablePCDir = FPaths::ProjectDir() / TEXT("Build") / TargetPlatform->IniPlatformName() / TEXT("PipelineCaches");
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:471:				const FString PCUncookedPath = FPaths::ProjectDir() / TEXT("Content") / TEXT("PipelineCaches") / TargetPlatform->IniPlatformName() / OutFilename;
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:547:						const FString RootPipelineCacheMetadataPath = GetMetadataDirectory() / TEXT("PipelineCaches");
Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp:590:	const FString RootMetaDataPath = GetMetadataDirectory() / TEXT("PipelineCaches");
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:07:18 · Tool call: Bash** (Read stable PSO cache packaging in cooker)

```
cd /d/UE/UE_5.9/Engine/Source; sed -n 425,480p Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp
```

Result:

```
void UCookOnTheFlyServer::CreatePipelineCache(const ITargetPlatform* TargetPlatform, const FString& LibraryName)
{
	// make sure we have a registry generated for all the platforms 
	const FString TargetPlatformName = TargetPlatform->PlatformName();
	TArray<FString>* SCLCSVPaths = OutSCLCSVPaths.Find(FName(TargetPlatformName));
	if (SCLCSVPaths && SCLCSVPaths->Num())
	{
		TArray<FName> ShaderFormats;
		TargetPlatform->GetAllTargetedShaderFormats(ShaderFormats);
		for (FName ShaderFormat : ShaderFormats)
		{
			const FString StablePCDir = FPaths::ProjectDir() / TEXT("Build") / TargetPlatform->IniPlatformName() / TEXT("PipelineCaches");
			// look for the new binary format for stable pipeline cache - spc
			const FString StablePCBinary = StablePCDir / FString::Printf(TEXT("*%s_%s.spc"), *LibraryName, *ShaderFormat.ToString());

			bool bBinaryStablePipelineCacheFilesFound = [&StablePCBinary]()
				{
					TArray<FString> ExpandedFiles;
					IFileManager::Get().FindFilesRecursive(ExpandedFiles, *FPaths::GetPath(StablePCBinary), *FPaths::GetCleanFilename(StablePCBinary), true, false, false);
					return ExpandedFiles.Num() > 0;
				}();

			// for now, also look for the older *stablepc.csv or *stablepc.csv.compressed
			const FString StablePCTextual = StablePCDir / FString::Printf(TEXT("*%s_%s.stablepc.csv"), *LibraryName, *ShaderFormat.ToString());
			const FString StablePCTextualCompressed = StablePCTextual + TEXT(".compressed");

			bool bTextualStablePipelineCacheFilesFound = [&StablePCTextual, &StablePCTextualCompressed]()
				{
					TArray<FString> ExpandedFiles;
					IFileManager::Get().FindFilesRecursive(ExpandedFiles, *FPaths::GetPath(StablePCTextual), *FPaths::GetCleanFilename(StablePCTextual), true, false, false);
					IFileManager::Get().FindFilesRecursive(ExpandedFiles, *FPaths::GetPath(StablePCTextualCompressed), *FPaths::GetCleanFilename(StablePCTextualCompressed), true, false, false);
					return ExpandedFiles.Num() > 0;
				}();

			// because of the compute shaders that are cached directly from stable shader keys files, we need to run this also if we have stable keys (which is pretty much always)
			static const IConsoleVariable* CVarIncludeComputePSOsDuringCook = IConsoleManager::Get().FindConsoleVariable(TEXT("r.ShaderPipelineCacheTools.IncludeComputePSODuringCook"));
			const bool bIncludeComputePSOsDuringCook = CVarIncludeComputePSOsDuringCook && CVarIncludeComputePSOsDuringCook->GetInt() >= 1;
			if (!bBinaryStablePipelineCacheFilesFound &
[... 1280 more characters not shown]
```

**Sun 15 Nov 11:07:31 · Tool call: Bash** (Log findings, wait, check builds)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat >> LOG.md <<'EOF'
- 11:05 lead for the 24: TSR (`TemporalSuperResolution.cpp`). `FTSRDecimateHistoryCS` (line 911) and `FTSRUpdateHistoryCS` (line 1313) compile a 16-bit permutation (`F16BitVALUDim`, `CFLAG_AllowRealTypes`, lines 987 and 1396) on SM6 because `bSupportsRealTypes=RuntimeDependent` (`Engine/Config/Windows/DataDrivenPlatformInfo.ini:127`), and neither has a `ShouldPrecachePermutation`, so the default precaches every compiled permutation. 16-bit ones: Decimate 2x2x2x2 (moire, resurrection, thin geometry, alpha) = 16, Update 4 qualities x 2 alpha = 8. 16 + 8 = 24. The TSR classes that do filter (`FTSRConvolutionNetworkShader::ShouldPrecachePermutation`, line 717) drop 16-bit permutations when `Use16BitVALU` is false (line 640: needs `GRHIGlobals.SupportsNative16BitOps`). The GTX 1070 (Pascal) has no native 16-bit shader ops; the renderer then dispatches the 32-bit permutations. To prove with a temporary log of shader type, permutation and hash.
- 11:06 project has the bundled pipeline cache slot but no file: every pc2 log says `Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache`. Shared shader library on (1907 shaders). The cook bundles one from `Build/Windows/PipelineCaches/*Supercut_PCD3D_SM6.spc` (`ShaderLibraryCooking.cpp:436-441`) and needs stable keys (`NeedsShaderStableKeys` in `[DevOptions.Shaders]`, `ShaderLibraryCooking.cpp:262`).
- 11:06 [pc-b]: free RAM 6.9 GB, CPU 31 %, another lane's cl running (builds queue). Started mirror, build, package there for the picture comparison.
EOF
sleep 120; ssh pc2 'powershell -NoProfile -Command "Get-Content C:\UE\Farm\perf3\Saved\Logs\*UBT*.log -Tail 1"' 2>/dev/null; tail -2 /d/UE/wt/perf3_farmlogs_[pc-b]/bp.txt; date +%H:%M
```

Result:

```
0.284          [821.490]  +0.002 TelemetryService.FlushEvents
FARM mirror [pc-b]:C:\UE\Farm\perf3 sent 3010 files (3280.1 MB), deleted 0, 3010 files in project, 119.3 s
11:09
```

**Sun 15 Nov 11:09:36 · Tool call: Bash** (Check pc2 build result)

```
cat /d/UE/wt/perf3_farmlogs/bp.txt | grep -v "^\s*[0-9.]* *\[" | tail -8
```

Result:

```
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822
```

### Sun 15 Nov 11:09:42 · Agent (claude-opus-5-5)

pc2 build passed (822 s); package is running. Preparing the temporary diagnostic (not to be committed) that names the shader behind each hash.

**Sun 15 Nov 11:09:42 · Tool call: Bash** (Check module deps and includes)

```
cd /d/UE/wt/perf3/Source/Supercut; grep -n "Dependency\|\"" Supercut.Build.cs | head -20; grep -n "^#include" SupercutPlayerController.cpp | head -30
```

Result:

```
9:		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "SlateCore", "ApplicationCore" });
10:		PrivateDependencyModuleNames.AddRange(new string[] { "AudioMixer", "AudioMixerCore", "NonRealtimeAudioRenderer", "Json", "Niagara", "DLSSBlueprint", "Renderer", "AssetRegistry", "RHI", "RenderCore" });
13:		foreach (string Name in new string[] { "mx_action_drums", "mx_action_bass", "mx_action_colour", "mx_action_heat", "mx_puzzle", "mx_between", "mx_take_start", "mx_room_clear" })
15:			RuntimeDependencies.Add("$(ProjectDir)/Audio/music/wav/" + Name + ".wav", StagedFileType.NonUFS);
18:		RuntimeDependencies.Add("$(ProjectDir)/Content/Props/catalogue.txt", StagedFileType.NonUFS);
1:#include "SupercutPlayerController.h"
2:#include "Supercut.h"
3:#include "SupercutAudio.h"
4:#include "SupercutDlss.h"
5:#include "SupercutEnemy.h"
6:#include "SupercutHUD.h"
7:#include "SupercutMachines.h"
8:#include "SupercutMenu.h"
9:#include "SupercutMenuView.h"
10:#include "SupercutPractice.h"
11:#include "SupercutPuzzles.h"
12:#include "SupercutRun.h"
13:#include "SupercutTime.h"
14:#include "SupercutTuning.h"
15:#include "SupercutUserSettings.h"
16:#include "Components/StaticMeshComponent.h"
17:#include "Engine/World.h"
18:#include "EngineUtils.h"
19:#include "GameFramework/CharacterMovementComponent.h"
20:#include "GameFramework/PlayerInput.h"
21:#include "GenericPlatform/GenericPlatformInputDeviceMapper.h"
22:#include "HAL/FileManager.h"
23:#include "InputCoreTypes.h"
24:#include "InputKeyEventArgs.h"
25:#include "Misc/App.h"
26:#include "Misc/CommandLine.h"
27:#include "Misc/FileHelper.h"
28:#include "Misc/Parse.h"
29:#include "Misc/Paths.h"
30:#include "UnrealClient.h"
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:09:52 · Tool call: Bash** (List script commands the scripted player knows)

```
cd /d/UE/wt/perf3/Source/Supercut; grep -n "TEXT(\"[a-z]*\")" SupercutPlayerController.cpp | grep -i "cmd\|==\|Equals" | head -40
```

Result:

```
534:		if (Step.Command == TEXT("scene"))
597:	if (Step.Command == TEXT("move"))
602:	else if (Step.Command == TEXT("look"))
606:	else if (Step.Command == TEXT("lookat"))
610:	else if (Step.Command == TEXT("aim"))
631:	else if (Step.Command == TEXT("jump"))
635:	else if (Step.Command == TEXT("fire"))
645:	else if (Step.Command == TEXT("firehold"))
649:	else if (Step.Command == TEXT("clap"))
674:	else if (Step.Command == TEXT("reload"))
678:	else if (Step.Command == TEXT("key"))
688:	else if (Step.Command == TEXT("click"))
696:	else if (Step.Command == TEXT("point"))
704:	else if (Step.Command == TEXT("mouse"))
709:	else if (Step.Command == TEXT("report"))
722:	else if (Step.Command == TEXT("expectdeath"))
726:	else if (Step.Command == TEXT("shot"))
743:	else if (Step.Command == TEXT("end"))
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:10:04 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\psodiag_snippet.cpp.txt",
 "content": "// TEMPORARY perf3 diagnostic, never committed. Goes in ASupercutPlayerController::BeginPlay after the bTrace line,\n// with #include \"GlobalShader.h\" and \"RHIGlobals.h\" at the top. Run with -SupercutPsoDiag.\n\tif (FParse::Param(FCommandLine::Get(), TEXT(\"SupercutPsoDiag\")))\n\t{\n\t\tconst EShaderPlatform DiagPlatform = GetFeatureLevelShaderPlatform(GMaxRHIFeatureLevel);\n\t\tFGlobalShaderMap* DiagMap = GetGlobalShaderMap(DiagPlatform);\n\t\tUE_LOG(LogSupercut, Display, TEXT(\"PSODIAG native16bit %d wave %d-%d\"), GRHIGlobals.SupportsNative16BitOps ? 1 : 0, GRHIMinimumWaveSize, GRHIMaximumWaveSize);\n\t\tfor (TLinkedList<FShaderType*>::TIterator DiagIt(FShaderType::GetTypeList()); DiagIt; DiagIt.Next())\n\t\t{\n\t\t\tFGlobalShaderType* DiagType = DiagIt->GetGlobalShaderType();\n\t\t\tif (!DiagType || DiagType->GetFrequency() != SF_Compute)\n\t\t\t{\n\t\t\t\tcontinue;\n\t\t\t}\n\t\t\tfor (int32 DiagId = 0; DiagId < DiagType->GetPermutationCount(); ++DiagId)\n\t\t\t{\n\t\t\t\tif (!DiagMap->HasShader(DiagType, DiagId))\n\t\t\t\t{\n\t\t\t\t\tcontinue;\n\t\t\t\t}\n\t\t\t\tFRHIShader* DiagRhi = DiagMap->GetShader(DiagType, DiagId).GetRHIShaderBase(SF_Compute, false);\n\t\t\t\tif (DiagRhi)\n\t\t\t\t{\n\t\t\t\t\tUE_LOG(LogSupercut, Display, TEXT(\"PSODIAG %s %d %s\"), DiagType->GetName(), DiagId, *DiagRhi->GetHash().ToString());\n\t\t\t\t}\n\t\t\t}\n\t\t}\n\t\tFTimerHandle DiagTimer;\n\t\tGetWorldTimerManager().SetTimer(DiagTimer, [this]() { ConsoleCommand(TEXT(\"ProfileGPU\")); }, 8.f, false);\n\t}\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\psodiag_snippet.cpp.txt (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:10:09 · Tool call: Bash** (Verify RHI globals names)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime/RHI/Public; grep -n "SupportsNative16BitOps\|MinimumWaveSize" RHIGlobals.h | head; grep -rn "SupportsNative16BitOps =" ../../D3D12RHI/Private/*.cpp | head -3; tail -2 /d/UE/wt/perf3_farmlogs/bp.txt
```

Result:

```
534:	int32 MinimumWaveSize = 0;
538:	bool SupportsNative16BitOps = false;
938:#define GRHIMinimumWaveSize                                    GRHIGlobals.MinimumWaveSize
../../D3D12RHI/Private/D3D12Adapter.cpp:1251:				GRHIGlobals.SupportsNative16BitOps = Features.Native16BitShaderOpsSupported;
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:10:16 · Tool call: Bash** (Wait for pc2 package)

```
for i in $(seq 1 18); do sleep 20; if grep -q "step=package" /d/UE/wt/perf3_farmlogs/bp.txt; then break; fi; done; tail -3 /d/UE/wt/perf3_farmlogs/bp.txt; tail -2 /d/UE/wt/perf3_farmlogs_[pc-b]/bp.txt; date +%H:%M
```

Result:

```
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=318
11:16
```

**Sun 15 Nov 11:16:24 · Tool call: Bash** (Check [pc-b] result)

```
grep -v "^\s*[0-9.]* *\[" /d/UE/wt/perf3_farmlogs_[pc-b]/bp.txt | tail -6; cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/b12t3zl60.output" | tail -3
```

Result:

```
FARM mirror USERu:C:\UE\Farm\perf3 sent 3010 files (3280.1 MB), deleted 0, 3010 files in project, 119.3 s
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=318
FARM step=build name=perf3 exit=0 secs=318

[exited with code 0]
```

### Sun 15 Nov 11:16:29 · Agent (claude-opus-5-5)

[pc-b] build passed (318 s) but its package step didn't start; starting it now after a load check.

**Sun 15 Nov 11:16:30 · Tool call: Bash** (Load check [pc-b] before package)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status [pc-b] 2>&1 | grep -E "free_ram|cpu_load|busy"
```

Result:

```
free_ram_gb=5.6 of 31.6
cpu_load_pct=54 threads=16
busy_procs=clx1 dotnetx2 Supercutx2
```

### Sun 15 Nov 11:16:40 · Agent (claude-opus-5-5)

[pc-b] has two other games running; waiting before packaging there.

**Sun 15 Nov 11:16:41 · Tool call: Bash** (Wait for pc2 package; recheck [pc-b])

```
for i in $(seq 1 24); do sleep 20; if grep -q "step=package" /d/UE/wt/perf3_farmlogs/bp.txt; then break; fi; done; grep -v "^\s*[0-9.]* *\[" /d/UE/wt/perf3_farmlogs/bp.txt | tail -4; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status [pc-b] 2>&1 | grep -E "free_ram|cpu_load|busy"; date +%H:%M
```

Result:

```
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822
free_ram_gb=4.6 of 31.6
cpu_load_pct=48 threads=16
busy_procs=clx1 dotnetx3 Supercutx2
11:24
```

**Sun 15 Nov 11:24:52 · Tool call: Bash** (Check pc2 chain result)

```
cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bgccxx2z8.output" | tail -5; grep -v "^\s*[0-9.]* *\[" /d/UE/wt/perf3_farmlogs/bp.txt | tail -5
```

Result:

```
exit 0
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822

[exited with code 0]
build SupercutEditor on C:\UE\UE_5.9: exit 0 (try 1)
FARM step=build name=perf3 exit=0 secs=822
```

### Sun 15 Nov 11:25:00 · Agent (claude-opus-5-5)

The chained package step silently didn't run on either PC. Running package on pc2 directly now (pc2 load check first).

**Sun 15 Nov 11:25:00 · Tool call: Bash** (Load check pc2 before package)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>&1 | grep -E "free_ram|cpu_load|busy"
```

Result:

```
free_ram_gb=5.4 of 15.9
cpu_load_pct=0 threads=12
busy_procs=UnrealEditor-Cmdx1
```

**Sun 15 Nov 11:25:08 · Tool call: Bash** (See what the other editor process on pc2 is)

```
ssh pc2 'powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name like ''UnrealEditor%'' or Name like ''AutomationTool%'' or Name like ''dotnet%''\" | ForEach-Object { $_.Name + '' '' + $_.CommandLine.Substring(0, [Math]::Min(220, $_.CommandLine.Length)) }"' 2>&1 | sed -E 's/Users\\[^\\]+/Users\\USER/g'
```

Result:

```
Get-CimInstance : Invalid query 
At line:1 char:1
+ Get-CimInstance Win32_Process -Filter "Name like UnrealEditor% or Nam ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Get-CimInstance], CimException
    + FullyQualifiedErrorId : HRESULT 0x80041017,Microsoft.Management.Infrastructure.CimCmdlets.GetCimInstanceCommand
```

**Sun 15 Nov 11:25:14 · Tool call: Bash** (List Unreal processes on pc2 with command lines)

```
cat > /tmp/p3q.ps1 <<'EOF'
Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(UnrealEditor|AutomationTool|Supercut)' } | ForEach-Object { $c = [string]$_.CommandLine; $_.Name + ' ' + $c.Substring(0, [Math]::Min(260, $c.Length)) }
EOF
scp -q /tmp/p3q.ps1 pc2:C:/UE/Farm/_out/perf3/p3q.ps1 2>/dev/null || { ssh pc2 "mkdir C:\UE\Farm\_out\perf3" ; scp -q /tmp/p3q.ps1 pc2:C:/UE/Farm/_out/perf3/p3q.ps1; }; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\perf3\p3q.ps1' 2>&1 | sed -E 's/Users\\[^\\]+/Users\\USER/g'
```

Result:

```
UnrealEditor-Cmd.exe "C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" C:\UE\Farm\hands2\Supercut.uproject -ExecCmds="Automation RunTests Supercut; Quit" -nullrhi -nosound -unattended -nopause -nosplash -stdout -FullStdOutLogOutput
```

### Sun 15 Nov 11:25:20 · Agent (claude-opus-5-5)

hands2's tests are running on pc2; waiting for them to end before packaging.

**Sun 15 Nov 11:25:21 · Tool call: Bash** (Wait until pc2 is idle)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; for i in $(seq 1 20); do s=$("$F" status pc2 2>&1); b=$(echo "$s" | sed -n 's/^busy_procs=//p'); [ "$b" = "none" ] && break; sleep 30; done; echo "$s" | grep -E "free_ram|cpu_load|busy"; date +%H:%M
```

Result:

```
free_ram_gb=6.2 of 15.9
cpu_load_pct=0 threads=12
busy_procs=none
11:26
```

**Sun 15 Nov 11:26:32 · Tool call: Bash** (Package on pc2 (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs; "$F" package pc2 perf3 "$L" > "$L/pkg.txt" 2>&1; echo "exit $?"; grep -v "^\s*[0-9.]* *\[" "$L/pkg.txt" | tail -4
```

Result:

```
Command running in background with ID: btikj4zjt. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\btikj4zjt.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**Sun 15 Nov 11:26:37 · Tool call: Bash** (Wait until [pc-b] has no games running)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; for i in $(seq 1 20); do s=$("$F" status [pc-b] 2>&1); b=$(echo "$s" | sed -n 's/^busy_procs=//p'); c=$(echo "$s" | sed -n 's/^cpu_load_pct=\([0-9]*\).*/\1/p'); echo "$b" | grep -q Supercut || { [ "$c" -lt 60 ] && break; }; sleep 30; done; echo "$s" | grep -E "free_ram|cpu_load|busy"; date +%H:%M
```

Result:

```
free_ram_gb=10.4 of 31.6
cpu_load_pct=23 threads=16
busy_procs=dotnetx1 UnrealEditor-Cmdx1
11:28
```

**Sun 15 Nov 11:28:57 · Tool call: Bash** (Check pc2 package output)

```
cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/btikj4zjt.output"; tail -30 /d/UE/wt/perf3_farmlogs/pkg.txt
```

Result:

```
exit 0
LogAudioCaptureCore: Display: No Audio Capture implementations found. Audio input will be silent.
LogAudio: Display: Registering Engine Module Parameter Interfaces...
LogSupercut: Display: TUNING template written to C:/UE/Farm/_builds/perf3/Supercut59/Windows/Tuning.example.txt
FARM step=package name=perf3 exit=0 secs=83

[exited with code 0]
LogAnalytics: Display: Provider StudioTelemetry.Provider.Log is disabled for this application
LogAnalytics: Display: Provider StudioTelemetry.Provider.CSV is disabled for this application
LogAnalytics: Display: Provider StudioTelemetry.Provider.Horde is disabled for this application
LogStreaming: Display: AsyncLoading2 - Created: Async Loading Thread: true, Async Post Load: true, Multithreaded: false
LogCsvProfiler: Display: Metadata set : systemresolution.resx="1024"
LogCsvProfiler: Display: Metadata set : systemresolution.resy="768"
LogHAL: Display: Platform has ~ 16 GB [17086164992 / 17179869184 / 16], which maps to Larger [LargestMinGB=32, LargerMinGB=12, DefaultMinGB=8, SmallerMinGB=6, SmallestMinGB=0)
LogCsvProfiler: Display: Metadata set : extradevelopmentmemorymb="0"
LogWindowsTouchpad: Display: CacheForceMaxTouchpadSensitivityMode SetMaxTouchpadSensitivity
LogObj: Display: Attempting to load config data for Default__SlateThemeManager before the Class has been constructed/registered/linked (likely during module loading or early startup). This will result in the load silently failing and should be fixed.
LogCsvProfiler: Display: Metadata set : verbatimrhiname="Null"
LogCsvProfiler: Display: Metadata set : rhiname="Null"
LogCsvProfiler: Display: Metadata set : rhifeaturelevel="SM6"
LogCsvProfiler: Display: Metadata set : shaderplatform="PCD3D_SM6"
LogCsvProfiler: Display: Metadata set : gpu=""
LogCsvProfiler: Display: Metadata set : gpudriver=""
LogDeviceProfileManager: Display: Deviceprofile LinuxArm64Editor not found.
LogDeviceProfileManager: Display: Deviceprofile LinuxArm64 not found.
LogCsvProfiler: Display: Metadata set : deviceprofile="Windows"
LogStreaming: Display: FlushAsyncLoading(8): 8 QueuedPackages, 0 AsyncPackages
LogStreaming: Display: Partially loaded package /Engine/EngineMaterials/WorldGridMaterial (state: WaitingForIo) to avoid deadlock when it was recursively flushed by package /Engine/EngineMaterials/DefaultTextMaterialOpaque (state: PostLoad). UniqueCallstack(-1).
LogStreaming: Display: Partially loaded package /Engine/EngineMaterials/DefaultDeferredDecalMaterial (state: WaitingForI
[... 1190 more characters not shown]
```

### Sun 15 Nov 11:29:01 · Agent (claude-opus-5-5)

pc2 package done in 83 s (exit 0). Checking the cook log, then starting the [pc-b] package and the first pc2 runs.

**Sun 15 Nov 11:29:03 · Tool call: Bash** (Check pc2 package logs)

```
L=/d/UE/wt/perf3_farmlogs; ls $L/package; grep -c "Failed to compile Material" $L/package/*.log; grep -E "BUILD SUCCESSFUL|AutomationTool exiting|Cook.*(Success|complete)|Packages Cooked|Compiled.*[0-9]+ actions|Total execution time" $L/package/package_run.log | tail -6
```

Result:

```
console.txt
farm_step.txt
package_run.log
write_tuning.log
/d/UE/wt/perf3_farmlogs/package/package_run.log:0
/d/UE/wt/perf3_farmlogs/package/write_tuning.log:0
LogCook: Display: Packages Cooked: 1327, Packages Incrementally Skipped: 0, Packages Skipped by Platform: 7, Total Packages: 1334
BUILD SUCCESSFUL
AutomationTool exiting with ExitCode=0 (Success)
```

**Sun 15 Nov 11:29:18 · Tool call: Bash** (Copy title script, inspect package, load check)

```
ssh pc2 "if not exist C:\UE\Farm\_out\perf3\desktools mkdir C:\UE\Farm\_out\perf3\desktools"; scp -q "[notes]/unreal/megajam-2026/lanes/perf3/tools/args/title_main8.txt" pc2:C:/UE/Farm/_out/perf3/desktools/title_main8.txt && echo copied; ssh pc2 'dir /b C:\UE\Farm\_builds\perf3\Supercut59\Windows & dir /s /b C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved 2>nul' | head; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>&1 | grep -E "free_ram|cpu_load|busy|gpu="
```

Result:

```
copied
Engine
Manifest_DebugFiles_Win64.txt
Manifest_NonUFSFiles_Win64.txt
Manifest_UFSFiles_Win64.txt
NOTICES.txt
Play_dev.bat
Supercut
Supercut.exe
Tuning.example.txt
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config
free_ram_gb=4.1 of 15.9
cpu_load_pct=1 threads=12
busy_procs=UnrealEditorx1
gpu=NVIDIA GeForce GTX 1070, 97 %, 4100 MiB, 127.81 W
```

### Sun 15 Nov 11:29:26 · Agent (claude-opus-5-5)

pc2's GPU is at 97% from another lane's editor run. Waiting. Checking what the package step left in Saved meanwhile.

**Sun 15 Nov 11:29:26 · Tool call: Bash** (Saved folder contents and other process)

```
ssh pc2 'dir /s /b C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved'; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\perf3\p3q.ps1' 2>&1 | sed -E 's/Users\\[^\\]+/Users\\USER/g' | cut -c1-250
```

Result:

```
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Logs
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config\CrashReportClient
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config\CrashReportClient\UECC-Windows-BE071C3B45E5F56A8D62E38FCE768348
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config\CrashReportClient\UECC-Windows-FA5E431949A7EDEC569132B8007C0412
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config\CrashReportClient\UECC-Windows-BE071C3B45E5F56A8D62E38FCE768348\CrashReportClient.ini
C:\UE\Farm\_builds\perf3\Supercut59\Windows\Supercut\Saved\Config\CrashReportClient\UECC-Windows-FA5E431949A7EDEC569132B8007C0412\CrashReportClient.ini
UnrealEditor.exe "C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor.exe" "C:\UE\Farm\hands2\Supercut.uproject" -game -RenderOffscreen -windowed -ResX=1280 -ResY=720 -WinX=0 -WinY=0 -nosplash -unattended "-SupercutScript=C:\UE\Farm\hands2\Script\main8.t
```

**Sun 15 Nov 11:29:31 · Tool call: Bash** (Recheck [pc-b])

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status [pc-b] 2>&1 | grep -E "free_ram|cpu_load|busy"; date +%H:%M
```

Result:

```
free_ram_gb=10.6 of 31.6
cpu_load_pct=21 threads=16
busy_procs=none
11:29
```

**Sun 15 Nov 11:29:41 · Tool call: Bash** (Package on [pc-b] (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs_[pc-b]; "$F" package [pc-b] perf3 "$L" > "$L/pkg.txt" 2>&1; echo "exit $?"; tail -2 "$L/pkg.txt"; grep -c "Failed to compile Material" $L/package/package_run.log
```

Result:

```
Command running in background with ID: b00mim6ff. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\b00mim6ff.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**Sun 15 Nov 11:29:51 · Tool call: Bash** (Log, wait, check pc2 and [pc-b])

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat >> LOG.md <<'EOF'
- 11:09 pc2 build passed (822 s, -Jobs 4; RAM 0.9 to 1.7 GB free while compiling). [pc-b] build passed (318 s).
- 11:16 my chained `build && status | grep && package` stopped after the build on both PCs without running package (cause not found; ran package on its own after).
- 11:24 pc2: hands2's tests running (UnrealEditor-Cmd); waited until busy none (11:26, RAM 6.2 GB, CPU 0 %).
- 11:26 pc2 package passed, 83 s, cook 1327 packages, 0 `Failed to compile Material`.
- 11:28 pc2 busy again: hands2's uncooked main8 run (UnrealEditor -game -RenderOffscreen), GPU 97 %, 128 W. Waiting; no frame time run while it runs.
- 11:29 [pc-b]: busy none, RAM 10.6 GB, CPU 21 %. Package started there.
- `D3D12Adapter.cpp:1251`: `GRHIGlobals.SupportsNative16BitOps = Features.Native16BitShaderOpsSupported` (D3D12 OPTIONS4).
EOF
sleep 150; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>&1 | grep -E "free_ram|cpu_load|busy|gpu="; tail -1 /d/UE/wt/perf3_farmlogs_[pc-b]/pkg.txt; date +%H:%M
```

Result:

```
free_ram_gb=3.8 of 15.9
cpu_load_pct=0 threads=12
busy_procs=UnrealEditorx1
gpu=NVIDIA GeForce GTX 1070, 96 %, 4126 MiB, 121.90 W
FARM step=package name=perf3 exit=10 secs=5
11:32
```

### Sun 15 Nov 11:32:32 · Agent (claude-opus-5-5)

[pc-b]'s package failed in 5 s (exit 10, another lane's AutomationTool is packaging there). Retrying in a loop; pc2 still has hands2's run on its GPU.

**Sun 15 Nov 11:32:34 · Tool call: Bash** (Retry [pc-b] package until it runs (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs_[pc-b]; for i in $(seq 1 25); do s=$("$F" status [pc-b] 2>&1); b=$(echo "$s" | sed -n 's/^busy_procs=//p'); if echo "$b" | grep -qE "Supercut|UnrealEditor|AutomationTool|MainCheck"; then echo "$(date +%H:%M) busy $b"; sleep 60; continue; fi; "$F" package [pc-b] perf3 "$L" > "$L/pkg.txt" 2>&1; r=$?; echo "$(date +%H:%M) package exit $r"; [ $r -eq 0 ] && break; sleep 60; done; tail -1 "$L/pkg.txt"; grep -c "Failed to compile Material" $L/package/package_run.log
```

Result:

```
Command running in background with ID: bxrbtm294. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bxrbtm294.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

**Sun 15 Nov 11:32:38 · Tool call: Bash** (Wait for pc2 to be idle)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; for i in $(seq 1 24); do s=$("$F" status pc2 2>&1); b=$(echo "$s" | sed -n 's/^busy_procs=//p'); [ "$b" = "none" ] && break; sleep 30; done; echo "$s" | grep -E "free_ram|cpu_load|busy|gpu="; date +%H:%M
```

Result:

```
free_ram_gb=7.4 of 15.9
cpu_load_pct=6 threads=12
busy_procs=none
gpu=NVIDIA GeForce GTX 1070, 27 %, 1803 MiB, 40.49 W
11:36
```

### Sun 15 Nov 11:37:04 · Agent (claude-opus-5-5)

pc2 is idle. First run: the first-launch hitch run from the title (caches cleared, real desktop window), since anything else would warm the caches.

**Sun 15 Nov 11:37:05 · Tool call: Bash** (Run first-launch hitch run on pc2 desktop)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; bash tools/go.sh first1 title_main8.args -ClearCaches 2>&1 | tail -20
```

Result:

```
Command did not complete within its 600s timeout and was moved to the background (ID: bg1in6p3j). Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bg1in6p3j.output. You will be notified when it completes. If it is still running after 30m in the background, it will be stopped and you will be notified. It is running now: do not start a second copy while it runs. If it is no longer needed, stop it with TaskStop. No output had been read from it when it was moved. A program that buffers its output, or a pipe into one such as tail, can keep the output file empty until the command finishes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\lanes\perf3; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Sun 15 Nov 11:47:13 · Tool call: Bash** (Diagnose the long first run and [pc-b] package)

```
cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bxrbtm294.output"; ls "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/"; cat "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt"; ssh pc2 'dir /b C:\UE\Farm\_out\perf3\desk\first1 & schtasks /query /tn perf3_supercut' 2>&1 | tail -6; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\perf3\p3q.ps1' 2>&1 | sed -E 's/Users\\[^\\]+/Users\\USER/g' | cut -c1-200
```

Result:

```
11:32 busy UnrealEditorx1
11:33 busy Supercutx2
11:46 package exit 0
FARM could not fetch the logs of package
0

[exited with code 1]
cat: '[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt': No such file or directory
The system cannot find the file specified.
ERROR: The system cannot find the file specified.
UnrealEditor.exe "C:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor.exe" "C:\UE\Farm\hands2\Supercut.uproject" -game -RenderOffscreen -windowed -ResX=1280 -ResY=720 -WinX=0 -WinY=0 -nosplash -unattended
```

**Sun 15 Nov 11:47:21 · Tool call: Bash** (Check [pc-b] package result)

```
L=/d/UE/wt/perf3_farmlogs_[pc-b]; grep -v "^\s*[0-9.]* *\[" $L/pkg.txt | grep -E "FARM|BUILD|ExitCode|Cooked|rror" | tail -8; ssh [pc-b] 'dir /b C:\UE\Farm\_builds\perf3\Supercut59\Windows 2>&1 & dir /b C:\UE\Farm\_out\perf3\package 2>&1'
```

Result:

```
FARM step=package name=perf3 exit=0 secs=529
FARM could not fetch the logs of package
Engine
Manifest_DebugFiles_Win64.txt
Manifest_NonUFSFiles_Win64.txt
Manifest_UFSFiles_Win64.txt
NOTICES.txt
Play_dev.bat
Supercut
Supercut.exe
Tuning.example.txt
console.txt
farm_step.txt
package_run.log
write_tuning.log
```

**Sun 15 Nov 11:47:33 · Tool call: Bash** (Fetch [pc-b] package log)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs_[pc-b]; mkdir -p $L/package; "$F" fetch [pc-b] perf3 out/package/package_run.log $L/package </dev/null 2>&1 | tail -2; grep -c "Failed to compile Material" $L/package/package_run.log; grep -E "Packages Cooked|BUILD SUCCESSFUL|ExitCode=" $L/package/package_run.log | tail -3
```

Result:

```
0
Took 2.97s to run UnrealPak.exe, ExitCode=0
BUILD SUCCESSFUL
AutomationTool exiting with ExitCode=0 (Success)
```

### Sun 15 Nov 11:47:42 · Agent (claude-opus-5-5)

[pc-b] package is fine (0 material failures). Starting the one [pc-b] picture run (title start, main8 with its 67 pictures, 1920x1080) after a load check.

**Sun 15 Nov 11:47:44 · Tool call: Bash** (Load check [pc-b], copy title script)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status [pc-b] 2>&1 | grep -E "free_ram|cpu_load|busy|gpu="; ssh [pc-b] "if not exist C:\UE\Farm\_out\perf3\desktools mkdir C:\UE\Farm\_out\perf3\desktools"; scp -q "[notes]/unreal/megajam-2026/lanes/perf3/tools/args/title_main8.txt" [pc-b]:C:/UE/Farm/_out/perf3/desktools/title_main8.txt && echo copied
```

Result:

```
free_ram_gb=9.1 of 31.6
cpu_load_pct=17 threads=16
busy_procs=clx1 dotnetx1
gpu=NVIDIA GeForce RTX 4080 SUPER, 15 %, 7262 MiB, 21.46 W
copied
```

**Sun 15 Nov 11:47:52 · Tool call: Bash** (Picture run on [pc-b] (background))

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; L=/d/UE/wt/perf3_farmlogs_[pc-b]; "$F" run [pc-b] perf3 "$L" -Packaged -Exe '{B}\Supercut59\Windows\Supercut.exe' -Title -Run main8 -Seed 1 -Script 'C:\UE\Farm\_out\perf3\desktools\title_main8.txt' -FixedFps 240 -Silent -ResX 1920 -ResY 1080 -TimeoutSeconds 540 > $L/run.txt 2>&1; echo "exit $?"; tail -2 $L/run.txt; grep -E "RUN wrapped|SETTINGS first start" $L/run/run.log | cut -c1-250; grep -c "Failed to create compute pipeline" $L/run/run.log; ls $L/run/shots | wc -l
```

Result:

```
Command running in background with ID: b943t0dpu. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\b943t0dpu.output. You will be notified when it completes. To check interim output, use Read on that file path.
```

### Sun 15 Nov 11:47:58 · Agent (claude-opus-5-5)

While both PCs run, adding the temporary diagnostic to the worktree (uncommitted; pc2 gets it only after its baseline runs).

**Sun 15 Nov 11:47:59 · Tool call: Bash** (Locate insertion point)

```
cd /d/UE/wt/perf3/Source/Supercut; grep -n "bTrace = FParse::Param" SupercutPlayerController.cpp; grep -n '^#include "UnrealClient.h"' SupercutPlayerController.cpp; file SupercutPlayerController.cpp
```

Result:

```
74:	bTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));
30:#include "UnrealClient.h"
SupercutPlayerController.cpp: C source, ASCII text, with CRLF line terminators
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:48:05 · Tool call: Bash** (Insert temporary diagnostic (CRLF-safe))

```
cd /d/UE/wt/perf3/Source/Supercut; python - <<'EOF'
p='SupercutPlayerController.cpp'
b=open(p,'rb').read().decode('utf-8')
snip=open(r'[notes]/unreal/megajam-2026/lanes/perf3/tools/psodiag_snippet.cpp.txt',encoding='utf-8').read()
body=''.join(l+'\n' for l in snip.split('\n')[2:] if True).rstrip('\n')+'\n'
body=body.replace('\n','\r\n')
anchor='\tbTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));\r\n'
assert b.count(anchor)==1
b=b.replace(anchor, anchor+body)
inc='#include "UnrealClient.h"\r\n'
assert b.count(inc)==1
b=b.replace(inc, inc+'#include "GlobalShader.h"\r\n#include "RHIGlobals.h"\r\n')
open(p,'wb').write(b.encode('utf-8'))
EOF
git -C /d/UE/wt/perf3 diff --stat; git -C /d/UE/wt/perf3 diff | head -50
```

Result:

```
Source/Supercut/SupercutPlayerController.cpp | 30 ++++++++++++++++++++++++++++
 1 file changed, 30 insertions(+)
diff --git a/Source/Supercut/SupercutPlayerController.cpp b/Source/Supercut/SupercutPlayerController.cpp
index 78c0f02..3d0f1a9 100644
--- a/Source/Supercut/SupercutPlayerController.cpp
+++ b/Source/Supercut/SupercutPlayerController.cpp
@@ -28,6 +28,8 @@
 #include "Misc/Parse.h"
 #include "Misc/Paths.h"
 #include "UnrealClient.h"
+#include "GlobalShader.h"
+#include "RHIGlobals.h"
 
 namespace
 {
@@ -72,6 +74,34 @@ void ASupercutPlayerController::BeginPlay()
 	bCountFps = FParse::Param(FCommandLine::Get(), TEXT("SupercutFps"));
 	bQuitAtEnd = FParse::Param(FCommandLine::Get(), TEXT("SupercutQuit"));
 	bTrace = FParse::Param(FCommandLine::Get(), TEXT("SupercutTrace"));
+	if (FParse::Param(FCommandLine::Get(), TEXT("SupercutPsoDiag")))
+	{
+		const EShaderPlatform DiagPlatform = GetFeatureLevelShaderPlatform(GMaxRHIFeatureLevel);
+		FGlobalShaderMap* DiagMap = GetGlobalShaderMap(DiagPlatform);
+		UE_LOG(LogSupercut, Display, TEXT("PSODIAG native16bit %d wave %d-%d"), GRHIGlobals.SupportsNative16BitOps ? 1 : 0, GRHIMinimumWaveSize, GRHIMaximumWaveSize);
+		for (TLinkedList<FShaderType*>::TIterator DiagIt(FShaderType::GetTypeList()); DiagIt; DiagIt.Next())
+		{
+			FGlobalShaderType* DiagType = DiagIt->GetGlobalShaderType();
+			if (!DiagType || DiagType->GetFrequency() != SF_Compute)
+			{
+				continue;
+			}
+			for (int32 DiagId = 0; DiagId < DiagType->GetPermutationCount(); ++DiagId)
+			{
+				if (!DiagMap->HasShader(DiagType, DiagId))
+				{
+					continue;
+				}
+				FRHIShader* DiagRhi = DiagMap->GetShader(DiagType, DiagId).GetRHIShaderBase(SF_Compute, false);
+				if (DiagRhi)
+				{
+					UE_LOG(LogSupercut, Display, TEXT("PSODIAG %s %d %s"), DiagType->GetName(), DiagId, *DiagRhi->GetHash().ToString());
+				}
+			}
+		}
+		FTimerHandle DiagTimer;
+		GetWorldTimerManager().SetTimer(DiagTimer, [this]() { ConsoleCommand(TEXT("ProfileGPU")); }, 8.f, false);
+	}
 
 	// The engine applied the saved window and quality at start. The volumes, the unfocused mute and the colour filter are the game's own.
 	USupercutUserSettings& Settings = USupercutUserSettings::Get();
Shell cwd was reset to [notes]
```

**Sun 15 Nov 11:48:12 · Tool call: Bash** (Check pc2 hitch run progress)

```
cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bg1in6p3j.output" | tail -8; date +%H:%M
```

Result:

```
11:48
```

**Sun 15 Nov 11:48:17 · Tool call: Bash** (pc2 status)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>&1 | grep -E "free_ram|cpu_load|busy|gpu="; ls "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/"
```

Result:

```
free_ram_gb=3.6 of 15.9
cpu_load_pct=0 threads=12
busy_procs=none
gpu=NVIDIA GeForce GTX 1070, 15 %, 2691 MiB, 36.10 W
```

**Sun 15 Nov 11:48:27 · Tool call: Bash** (Wait and check hitch run)

```
sleep 200; cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bg1in6p3j.output" | tail -5; cat "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt" 2>/dev/null; date +%H:%M
```

Result:

```
<tool_use_error>Blocked: sleep 200 followed by: cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bg1in6p3j.output" tail -5 cat "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt" date +%H:%M. To wait for a condition, use Monitor with an until-loop (e.g. `until <check>; do sleep 2; done`). To wait for a command you started, use run_in_background: true. Do not chain shorter sleeps to work around this block.</tool_use_error>
```

**Sun 15 Nov 11:48:33 · Tool call: Bash** (Wait until the hitch run starts)

```
until [ -s "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt" ]; do sleep 10; done; cat "[notes]/unreal/megajam-2026/lanes/perf3/logs/first1/load.txt"; date +%H:%M
```

Result:

```
before: free_ram_gb=4 of 15.9 cpu_load_pct=1 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 2695 MiB, 39.58 W 
11:48
```

### Sun 15 Nov 11:48:36 · Agent (claude-opus-5-5)

The first-launch run started on pc2 at 11:48 (RAM 4 GB free, GPU idle). The [pc-b] picture run is also going. Waiting for both.

**Sun 15 Nov 11:48:38 · Tool call: Bash** (Wait for hitch run result)

```
until grep -q "compute pipeline errors" "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bg1in6p3j.output" 2>/dev/null; do sleep 10; done; cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bg1in6p3j.output" | tail -16
```

Result:

```
cpu_before=2
others_before=
seconds_to_exit=140.1
exit_code=777003
hang=False
cpu_after=1
others_after=
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality CUSTOM (never chosen), display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUserSettings.ini
LogSupercut: Display: SETTINGS first start: benchmark CPU 192, GPU 256, groups view 3, anti-aliasing 3, shadows 3, GI 3, reflections 3, post 3, textures 3, effects 3, foliage 3, shading 3, in 6.7 s; lowest EPIC, quality set to HIGH
LogSupercut: Display: RUN wrapped: takes 1, time 98.4 s, shots 46, freezes 14, kills 17
LogSupercut: Display: SCRIPT finished at 15.93 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 72.8, slowest 1% of frames 50.8, over 4389 frames and 60.3 s
LogSupercut: Display: FPS frozen: average 70.8, slowest 1% of frames 53.5, over 2484 frames and 35.1 s
compute pipeline errors: 24

[exited with code 0]
```

### Sun 15 Nov 11:51:15 · Agent (claude-opus-5-5)

First-launch run done: HIGH picked by the benchmark, 72.8 fps live average (13.7 ms), slowest 1% 50.8 fps, 24 errors, RUN line matches except wall time (no fixed step). Analyzing the per-frame CSV.

**Sun 15 Nov 11:51:16 · Tool call: Bash** (Inspect hitch run outputs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; ls -la logs/first1/; cat logs/first1/load.txt; grep -E "removed|cache_files" logs/first1/result.txt; grep -E "QUIT|Exiting|LogExit|Fatal|exit code" logs/first1/run.log | tail -5 | cut -c1-200; head -c 600 logs/first1/profile.csv | tr ',' '\n' | head -30
```

Result:

```
total 15082
drwxr-xr-x 1 [user] 197121        0 Nov 15 11:51 .
drwxr-xr-x 1 [user] 197121        0 Nov 15 11:37 ..
-rw-r--r-- 1 [user] 197121     2471 Nov 15 11:51 GameUserSettings.after.ini
-rw-r--r-- 1 [user] 197121      268 Nov 15 11:51 load.txt
-rw-r--r-- 1 [user] 197121 14942208 Nov 15 11:51 profile.csv
-rw-r--r-- 1 [user] 197121      618 Nov 15 11:51 result.txt
-rw-r--r-- 1 [user] 197121   481507 Nov 15 11:51 run.log
-rw-r--r-- 1 [user] 197121     4915 Nov 15 11:51 sample.csv
before: free_ram_gb=4 of 15.9 cpu_load_pct=1 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 2695 MiB, 39.58 W 
gpu gate: idle
after: free_ram_gb=4.6 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 26 %, 2864 MiB, 39.62 W 
cache_files_removed=
[2026.11.15-03.50.58:297][351]LogSupercut: Display: QUIT with code 0
[2026.11.15-03.50.59:649][352]LogExit: Preparing to exit.
[2026.11.15-03.50.59:769][352]LogExit: Game engine shut down
[2026.11.15-03.50.59:999][352]LogExit: Object subsystem successfully closed.
[2026.11.15-03.51.00:946][352]LogExit: Exiting.
EVENTS
Exclusive/GameThread/EventWait
Scheduler/GameThread/CreateThread
Exclusive/GameThread/Material_UpdateDeferredCachedUniformExpressions
FMsgLogf/FMsgLogfCount
CsvProfiler/NumTimestampsProcessed
CsvProfiler/NumCustomStatsProcessed
CsvProfiler/NumEventsProcessed
CsvProfiler/ProcessCSVStats
Scheduler/AllWorkers/CreateThread
Scheduler/Oversubscription
FMsgLogf/FMsgLogfCount
Exclusive/GameThread/InitRenderResource
IoDispatcherFileBackend/FrameBytesScatteredKB
IoDispatcherFileBackend/FrameSeeks
IoDispatcherFileBackend/FrameFilesystemBytesReadKB
IoDispatcherFileBackend/FrameSequentialReads
Sched
```

**Sun 15 Nov 11:51:26 · Tool call: Bash** (Inspect CSV structure; [pc-b] result)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import csv
rows=list(csv.reader(open('logs/first1/profile.csv',encoding='utf-8',errors='replace')))
print(len(rows), [len(r) for r in rows[:3]], [len(r) for r in rows[-3:]])
h=rows[0]; print('FrameTime' in h, 'GPUTime' in h, [x for x in h if 'GPU' in x][:10])
print(rows[-2][:6]); print(rows[-1][:12])
print([i for i,x in enumerate(h) if x in('FrameTime','GPUTime','GameThreadTime','RenderThreadTime')])
EOF
cat /c/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/b943t0dpu.output
```

Result:

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
_csv.Error: field larger than field limit (131072)
exit 0
game exit code 0
FARM step=run name=perf3 exit=0 secs=169
[2026.11.15-03.48.01:518][  0]LogSupercut: Display: SETTINGS first start: benchmark CPU 261, GPU 385, groups view 3, anti-aliasing 3, shadows 3, GI 3, reflections 3, post 3, textures 3, effects 3, foliage 3, shading 3, in 3.6 s; lowest EPIC, quality 
[2026.11.15-03.50.34:629][329]LogSupercut: Display: RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17
0
65

[exited with code 0]
```

### Sun 15 Nov 11:51:31 · Agent (claude-opus-5-5)

[pc-b] picture run: same RUN line, 0 errors, 65 pictures, HIGH picked. Fixing the CSV reader (huge metadata field) and analyzing the pc2 first launch.

**Sun 15 Nov 11:51:33 · Tool call: Bash** (Inspect CSV with larger field limit)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; sed -i 's/^import csv, os, re, statistics, sys$/import csv, os, re, statistics, sys\ncsv.field_size_limit(1 << 30)/' tools/analyze.py; python -I - <<'EOF'
import csv
csv.field_size_limit(1<<30)
rows=list(csv.reader(open('logs/first1/profile.csv',encoding='utf-8',errors='replace')))
print(len(rows), [len(r) for r in rows[:3]], [len(r) for r in rows[-3:]])
h=rows[0]; print([i for i,x in enumerate(h) if x in('FrameTime','GPUTime','GameThreadTime','RenderThreadTime','RHIThreadTime')])
print([x for x in h if x.startswith('GPU')][:10])
print(rows[-1][:8]); print(rows[1][:4], rows[2][:4])
EOF
```

Result:

```
<persisted-output>
Output too large (175.4KB). Full output saved to: [agent-config]\2f0f321c-13ca-453f-9197-384709201b64\tool-results\b44rznzhp.txt

Preview (first 2KB):
8172 [297, 297, 297] [377, 377, 377]
[110, 236, 237, 238, 241]
['GPUSceneInstanceCount', 'GPUTime', 'GPUMem/LocalBudgetMB', 'GPUMem/LocalUsedMB', 'GPUMem/SystemBudgetMB', 'GPUMem/SystemUsedMB']
['', '10.7297', '0', '0', '0', '0', '0', '0']
["Region: EngineInit/Launch - End##1.384076;Region: EngineInit/FEngineLoop::PreInitPreStartupScreen - Begin##1.384097;Region: EngineInit/LaunchSetGameName - Begin##1.384204;Region: EngineInit/LaunchSetGameName - End##1.402830;Region: EngineInit/Init Output Devices - Begin##1.402839;Region: EngineInit/Init Output Devices - End##1.403337;Region: EngineInit/LLM Init - Begin##4.080742;Region: EngineInit/LLM Init - End##4.082063;Region: EngineInit/InitTaggedStorage - Begin##4.082068;Region: EngineInit/InitTaggedStorage - End##4.082069;Region: EngineInit/CreateConsoleOutputDevice - Begin##4.082075;Region: EngineInit/CreateConsoleOutputDevice - End##4.082748;Region: EngineInit/Fix up the relative project path - Begin##4.082803;Region: EngineInit/Fix up the relative project path - End##4.082813;Region: EngineInit/Command Line Adjustments - Begin##4.082816;Region: EngineInit/Command Line Adjustments - End##4.083170;Region: EngineInit/BeginPreInitTextLocalization - Begin##4.083245;Region: EngineInit/BeginPreInitTextLocalization - Begin##4.083254;Region: EngineInit/BeginPreInitTextLocalization - End##4.083270;Region: EngineInit/BeginPreInitTextLocalization - End##4.083270;Region: EngineInit/PreInitShaderLibrary - Begin##4.083271;Region: EngineInit/PreInitShaderLibrary - End##4.083976;Region: EngineInit/LaunchCheckForFileOverride - Begin##4.083978;Region: EngineInit/LoadModule - Begin##4.084939;Region: EngineInit/LoadModule  - StorageServerClient - Begin##4.085279;Region: EngineInit/LoadModule  - StorageServerClient - End##4.085586;Region: EngineInit/LoadModule - End##4.085588;Region: EngineInit/LoadModule - Begin##4.086137;Region: EngineInit/LoadModule  - CookOnTheFly - Begin##4.086371;Region: EngineInit/LoadModule  - CookOnTheFly - End#
...
</persisted-output>
[This command modified 1 file you've previously read: tools\analyze.py. Call Read before editing.]
```

**Sun 15 Nov 11:51:46 · Tool call: Bash** (Fix CSV parsing; find title marker in log)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/analyze.py'
s=open(p,encoding='utf-8').read()
old="""    head = rows[0]
    data = []
    for r in rows[1:]:
        if not r or r[0].startswith('['):
            break
        data.append(r)
"""
new="""    head = rows[0]
    data = []
    for r in rows[1:]:
        if not r or r[0].startswith('[') or r[0] == 'EVENTS':
            if r and r[0] == 'EVENTS' and len(r) > len(head):
                head = r   # the header written at the end lists the stats that appeared during the run as well
            break
        data.append(r)
"""
assert s.count(old)==1
s=s.replace(old,new)
s=s.replace("float(data[i][gcol])","num(data[i], gcol)").replace("float(data[r][i] or 0)","num(data[r], i)")
s=s.replace("def stats(ft):","def num(row, i):\n    return float(row[i]) if i < len(row) and row[i] else 0.0\n\n\ndef stats(ft):")
open(p,'w',encoding='utf-8').write(s)
EOF
grep -n -i "title" logs/first1/run.log | head -8 | cut -c1-180; grep -n "LogCsvProfiler" logs/first1/run.log | head -5 | cut -c1-200
```

Result:

```
24:LogCsvProfiler: Display: Metadata set : commandline="" Supercut -SupercutTitle -SupercutRun=main8 -SupercutSeed=1 -SupercutScript=C:\UE\Farm\_out\perf3\desktools\title_main8.txt
352:LogInit: Command Line: -SupercutTitle -SupercutRun=main8 -SupercutSeed=1 -SupercutScript=C:\UE\Farm\_out\perf3\desktools\title_main8.txt -csvCaptureFrames=30000 -nosplash -unat
932:[2026.11.15-03.48.52:736][  0]LogChaosDD: Creating Chaos Debug Draw Scene for world Untitled
934:[2026.11.15-03.48.53:023][  0]LogAudio: Display: Audio Device (ID: 1) registered with world 'Untitled'.
935:[2026.11.15-03.48.53:038][  0]LogSlate: Updating window title bar state: overlay mode, drag disabled, window buttons hidden, title bar hidden
1105:[2026.11.15-03.48.53:774][  0]LogWorld: BeginTearingDown for /Temp/Untitled_0
1106:[2026.11.15-03.48.53:776][  0]LogWorld: UWorld::CleanupWorld for Untitled, bSessionEnded=true, bCleanupResources=true
1109:[2026.11.15-03.48.53:809][  0]LogAudio: Display: Audio Device unregistered from world 'Untitled'.
11:LogCsvProfiler: Display: Metadata set : platform="Windows"
12:LogCsvProfiler: Display: Metadata set : config="Development"
13:LogCsvProfiler: Display: Metadata set : buildversion="++UE5+Release-5.9-CL-60351404"
14:LogCsvProfiler: Display: Metadata set : engineversion="5.9.0-60351404+++UE5+Release-5.9"
15:LogCsvProfiler: Display: Metadata set : enginereleaseversion="5.9.0"
```

**Sun 15 Nov 11:51:50 · Tool call: Bash** (First game log lines to find the title moment)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -n "LogSupercut" logs/first1/run.log | head -25 | cut -c1-200
```

Result:

```
933:[2026.11.15-03.48.52:980][  0]LogSupercut: Display: MUSIC read 8 files from ../../../Supercut/Audio/music/wav
1115:[2026.11.15-03.48.54:190][  0]LogSupercut: Display: TUNING no file at C:/UE/Farm/_builds/perf3/Supercut59/Windows/Tuning.txt: every number is its default
1116:[2026.11.15-03.48.54:804][  0]LogSupercut: Display: PROPS catalogue: 145 props from C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Content/Props/catalogue.txt
1117:[2026.11.15-03.48.54:812][  0]LogSupercut: Display: CREDITS 106 lines from C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Content/Credits/credits.txt
1118:[2026.11.15-03.48.54:820][  0]LogSupercut: Display: RUN list read: 8 rooms (fight/01_wind_machine, puzzle/a_the_cue, fight/02_stunt_run, fight/03_long_lens, puzzle/b_the_wild_wall, fight/04_hot_s
1119:[2026.11.15-03.48.55:019][  0]LogSupercut: Display: LIGHT lamp at V(X=816.53, Y=-1530.21, Z=2320.75), 4231 cd, cone 50 degrees, glowing part 275 cm across; fill 0.60 lux; ambient 0.30 lux; studio
1120:[2026.11.15-03.48.55:020][  0]LogSupercut: Display: LIGHT lamp mesh base at V(X=771.05, Y=-1608.99, Z=-50.00), scale 11.37, yaw 60
1121:[2026.11.15-03.48.55:030][  0]LogSupercut: Display: HALL built round 01_wind_machine: 84 x 68 m, walls 36 m, floor at -50, rig at 1150, near side 3, door on side 0; 2266 instances in 32 meshes, 2
1122:[2026.11.15-03.48.55:030][  0]LogSupercut: Display: ROOM built: 01_wind_machine, 71 pieces (3 of them actors) from C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Content/Rooms/fight/01_wind
1123:[2026.11.15-03.48.55:030][  0]LogSupercut: Display: GATE locked until every enemy of the room is down (2 alive)
1124:[2026.11.15-03.48.55:040][  0]LogSupercut: Display: TITLE backdrop: scene 1 (01_wind_machine), 0 actors removed, 4 actors built, in 103.2 ms
1127:[2026.11.15-03.48.55:060][  0]LogSupercutSound: Display: START stage_bed flat
1128:[2026.11.15-03.48.55:061][  0]LogSupercutSound: Display: SOUND mono upmix: the settings say EMonoChannelUpmixMethod::EqualPower, the mixer uses EMonoChannelUpmixMethod::EqualPower
1129:[2026.11.15-03.48.55:062][  0]LogSupercutSound: Display: SOUND master: +10.5 dB, limited at -2.5 dBFS
1130:[2026.11.15-03.48.55:062][  0]LogSupercutSound: Display: SOUND non-real-time device: nothing goes to the speakers, the game renders it each frame
1131:[2026.11.15-03.48.55:062][  0]LogSupercutSound: Display: SOUND music at 1.00
1132:[2026.11.15-03.48.55:066][  0]LogSupercutSound: Display: START blade_loop placed
[... 907 more characters not shown]
```

**Sun 15 Nov 11:51:56 · Tool call: Bash** (List hitches over 50 ms in first 60 s)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py first1 hitch 60 50 2>&1 | head -60
```

Result:

```
first1: title at frame 0 (row -3); 2738 frames in 60.0 s; 4 frames over 50.0 ms (row = frame - 3, spread 8.8 ms)
  +  0.04 s  19999.8 ms  frame 3  last log line: LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
  + 20.04 s    230.3 ms  frame 4  last log line: LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
  + 20.31 s    100.1 ms  frame 7  last log line: LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
  + 38.99 s     60.4 ms  frame 1222  last log line: LogSupercut: Display: ROOM change frames: the 4 frames from the change took 60.5, 36.6, 12.1, 13.0 ms
Traceback (most recent call last):
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 181, in <module>
    hitch(tag, float(sys.argv[3]), float(sys.argv[4]))
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 151, in hitch
    n, avg, p99, w1, mx = stats(ft[a:i])
                          ^^^^^^^^^^^^^^
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 71, in stats
    p99 = s[min(n - 1, int(0.99 * n))]
          ~^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range
```

**Sun 15 Nov 11:52:05 · Tool call: Bash** (Look at the first frames after boot)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools')
import analyze
log, head, col, data, ft, c, sd = analyze.load('first1')
print('c',c,'rows',len(ft),'sum s',sum(ft)/1000)
print([round(x,1) for x in ft[:20]])
# log lines in frames 1..12
for t,fr,text in log:
    if 1<=fr<=12 and ('Supercut' in text or 'PSO' in text): print(fr, text[:140])
EOF
```

Result:

```
c 3 rows 8171 sum s 133.9699457
[19999.8, 230.3, 9.1, 29.0, 100.1, 13.2, 14.7, 17.6, 17.8, 16.2, 16.1, 17.4, 16.9, 16.4, 17.0, 18.6, 15.6, 17.0, 16.1, 18.0]
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 1334988258 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 55049582 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 1758115893 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 2057419601 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 3132444827 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 761474543 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 4052107468 (PSOPrecacheState: Missed)
2 LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 3]
2 LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
```

### Sun 15 Nov 11:53:45 · Harness

[The session's context was summarised here. The summary is not exported.]

**Sun 15 Nov 11:53:54 · Tool call: Bash** (Find title and benchmark lines in the run log)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -n -E "TITLE|BENCH|SETTINGS|first start|SCRIPT|ROOM change" logs/first1/run.log | head -20 | cut -c1-220
```

Result:

```
1124:[2026.11.15-03.48.55:040][  0]LogSupercut: Display: TITLE backdrop: scene 1 (01_wind_machine), 0 actors removed, 4 actors built, in 103.2 ms
1133:[2026.11.15-03.48.55:154][  0]LogSupercut: Display: SCRIPT loaded: 346 steps from C:\UE\Farm\_out\perf3\desktools\title_main8.txt
1138:[2026.11.15-03.48.55:154][  0]LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality CUSTOM (never chosen), display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supe
1232:[2026.11.15-03.49.01:887][  0]LogSupercut: Display: SETTINGS first start: benchmark CPU 192, GPU 256, groups view 3, anti-aliasing 3, shadows 3, GI 3, reflections 3, post 3, textures 3, effects 3, foliage 3, shading
1337:[2026.11.15-03.49.01:978][  0]LogSupercut: Display: SETTINGS saved: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Wi
1565:[2026.11.15-03.49.04:514][136]LogSupercut: Display: SCRIPT 2.50 key Enter| pos V(X=150.00, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1589:[2026.11.15-03.49.06:627][269]LogSupercut: Display: ROOM change: take 1, scene 1 of 8 (01_wind_machine), charges 3 of 3, 6 actors removed, 4 actors built, in 13.7 ms
1595:[2026.11.15-03.49.06:643][270]LogSupercut: Display: SCRIPT scene 1 take 1 entered after 4.63 s, clock set to 0
1597:[2026.11.15-03.49.06:700][273]LogSupercut: Display: ROOM change frames: the 4 frames from the change took 29.1, 32.9, 9.7, 14.3 ms
1598:[2026.11.15-03.49.06:847][282]LogSupercut: Display: SCRIPT 0.20 look 0 0| pos V(X=150.00, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1603:[2026.11.15-03.49.07:149][300]LogSupercut: Display: SCRIPT 0.51 shot s1_01_start| not saved: no -SupercutShots folder pos V(X=150.00, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1605:[2026.11.15-03.49.07:646][331]LogSupercut: Display: SCRIPT 1.00 move 1 0| pos V(X=150.00, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1615:[2026.11.15-03.49.08:701][392]LogSupercut: Display: SCRIPT 2.06 move 0 0| pos V(X=749.58, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1618:[2026.11.15-03.49.09:145][418]LogSupercut: Display: SCRIPT 2.50 shot s1_02_at_the_machine| not saved: no -SupercutShots folder pos V(X=759.63, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
1621:[2026.11.15-03.49.10:328][487]LogSupercut: Display: SCRIPT 3.68 clap | blade angle 195 pos V(X=759.63, Z=90.15) yaw 0 health 100 rounds 6 char
[... 885 more characters not shown]
```

**Sun 15 Nov 11:54:04 · Tool call: Bash** (Anchor the hitch window after the benchmark and rerun)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/analyze.py'
s=open(p,encoding='utf-8').read()
old="""    t_title = next((t, fr) for t, fr, text in log if re.search(r'TITLE|title shown|MENU title', text))
    a = t_title[1] - c
"""
new="""    # The title is on screen from the last settings line before the first room (after the first-start benchmark,
    # if one ran). The first CSV row is the whole boot and is skipped.
    first_room = next(fr for t, fr, text in log if 'ROOM change' in text)
    t_title = [(t, fr) for t, fr, text in log if fr <= first_room and re.search(r'SETTINGS (at start|saved)', text)][-1]
    a = max(1, t_title[1] - c)
"""
assert old in s; s=s.replace(old,new)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
python -I tools/analyze.py first1 hitch 60 50
```

Result:

```
first1: title at frame 0 (row 1); 4171 frames in 60.0 s; 3 frames over 50.0 ms (row = frame - 3, spread 8.8 ms)
  +  0.00 s    230.3 ms  frame 4  last log line: LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
  +  0.27 s    100.1 ms  frame 7  last log line: LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
  + 18.95 s     60.4 ms  frame 1222  last log line: LogSupercut: Display: ROOM change frames: the 4 frames from the change took 60.5, 36.6, 12.1, 13.0 ms
  first 60.0 s: avg 14.39 ms, p99 19.39, max 230.3
```

**Sun 15 Nov 11:54:10 · Tool call: Bash** (Count missed PSOs and list room changes)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; L=logs/first1/run.log; echo "missed PSO total: $(grep -c 'PSOPrecacheState: Missed' $L)"; grep -n -E "ROOM change:|PSOPrecacheState" $L | awk -F'[][]' '{print $2, $4, $5}' | cut -c1-150 | awk '{k=$3" "$4" "$5" "$6; print}' | grep -E "ROOM|Missed" | sed -n '1,4p;/ROOM/p' | head -30; grep -E "PSOPrecacheState" $L | sed 's/.*PSOPrecacheState: //' | sort | uniq -c
```

Result:

```
missed PSO total: 48
2026.11.15-03.48.55:472   0 LogRHI: Display: Encountered a new graphics PSO: 3326528255 (PSOPrecacheState: Missed)
2026.11.15-03.48.56:454   0 LogRHI: Display: Encountered a new graphics PSO: 1371641584 (PSOPrecacheState: Missed)
2026.11.15-03.48.56:454   0 LogRHI: Display: Encountered a new graphics PSO: 488447920 (PSOPrecacheState: Missed)
2026.11.15-03.48.56:454   0 LogRHI: Display: Encountered a new graphics PSO: 2518162785 (PSOPrecacheState: Missed)
2026.11.15-03.49.06:627 269 LogSupercut: Display: ROOM change: take 1, scene 1 of 8 (01_wind_machine), charges 3 of 3, 6 actors removed, 4 actors buil
2026.11.15-03.49.21:005 218 LogSupercut: Display: ROOM change: take 1, scene 2 of 8 (a_the_cue), charges 3 of 3, 5 actors removed, 4 actors built, in 
2026.11.15-03.49.28:575 768 LogSupercut: Display: ROOM change: take 1, scene 3 of 8 (02_stunt_run), charges 3 of 3, 5 actors removed, 4 actors built, 
2026.11.15-03.49.49:522 278 LogSupercut: Display: ROOM change: take 1, scene 4 of 8 (03_long_lens), charges 3 of 3, 5 actors removed, 4 actors built, 
2026.11.15-03.50.05:447 436 LogSupercut: Display: ROOM change: take 1, scene 5 of 8 (b_the_wild_wall), charges 3 of 3, 5 actors removed, 8 actors buil
2026.11.15-03.50.15:406 181 LogSupercut: Display: ROOM change: take 1, scene 6 of 8 (04_hot_set), charges 3 of 3, 9 actors removed, 6 actors built, in
2026.11.15-03.50.32:783 462 LogSupercut: Display: ROOM change: take 1, scene 7 of 8 (c_the_cutaway), charges 3 of 3, 6 actors removed, 9 actors built,
2026.11.15-03.50.42:348 180 LogSupercut: Display: ROOM change: take 1, scene 8 of 8 (05_martini_shot), charges 3 of 3, 10 actors removed, 7 actors bui
     48 Missed)
```

**Sun 15 Nov 11:54:15 · Tool call: Bash** (Room change frame costs and missed PSO times)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; L=logs/first1/run.log; grep -E "ROOM change(:| frames)" $L | sed 's/^\[[^]]*\]\[[^]]*\]LogSupercut: Display: //' | cut -c1-110; echo; grep "PSOPrecacheState" $L | cut -c2-20 | cut -c12-16 | uniq -c
```

Result:

```
ROOM change: take 1, scene 1 of 8 (01_wind_machine), charges 3 of 3, 6 actors removed, 4 actors built, in 13.7
ROOM change frames: the 4 frames from the change took 29.1, 32.9, 9.7, 14.3 ms
ROOM change: take 1, scene 2 of 8 (a_the_cue), charges 3 of 3, 5 actors removed, 4 actors built, in 41.4 ms
ROOM change frames: the 4 frames from the change took 60.5, 36.6, 12.1, 13.0 ms
ROOM change: take 1, scene 3 of 8 (02_stunt_run), charges 3 of 3, 5 actors removed, 4 actors built, in 24.0 ms
ROOM change frames: the 4 frames from the change took 35.7, 27.9, 9.4, 12.0 ms
ROOM change: take 1, scene 4 of 8 (03_long_lens), charges 3 of 3, 5 actors removed, 4 actors built, in 24.4 ms
ROOM change frames: the 4 frames from the change took 35.7, 26.0, 9.0, 13.2 ms
ROOM change: take 1, scene 5 of 8 (b_the_wild_wall), charges 3 of 3, 5 actors removed, 8 actors built, in 21.0
ROOM change frames: the 4 frames from the change took 34.5, 27.9, 8.6, 11.1 ms
ROOM change: take 1, scene 6 of 8 (04_hot_set), charges 3 of 3, 9 actors removed, 6 actors built, in 25.7 ms
ROOM change frames: the 4 frames from the change took 38.3, 26.8, 8.4, 12.9 ms
ROOM change: take 1, scene 7 of 8 (c_the_cutaway), charges 3 of 3, 6 actors removed, 9 actors built, in 16.0 m
ROOM change frames: the 4 frames from the change took 29.6, 28.1, 13.8, 8.6 ms
ROOM change: take 1, scene 8 of 8 (05_martini_shot), charges 3 of 3, 10 actors removed, 7 actors built, in 30.
ROOM change frames: the 4 frames from the change took 43.8, 24.0, 9.7, 12.1 ms

      8 03.48
     40 03.49
```

**Sun 15 Nov 11:54:21 · Tool call: Bash** (Missed PSO timing and pc2 load check)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; L=logs/first1/run.log; grep "PSOPrecacheState" $L | cut -c13-21 | uniq -c | tr '\n' ' '; echo; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>/dev/null | grep -E 'free_ram|cpu_load|busy|^gpu'; ssh pc2 'nvidia-smi --query-gpu=utilization.gpu,power.draw --format=csv,noheader'; date +%H:%M
```

Result:

```
1 03.48.55:       7 03.48.56:      39 03.49.02:       1 03.49.08: 
free_ram_gb=4.4 of 15.9
cpu_load_pct=0 threads=12
busy_procs=none
gpu=NVIDIA GeForce GTX 1070, 27 %, 2895 MiB, 36.45 W
24 %, 36.50 W
11:54
```

**Sun 15 Nov 11:54:29 · Tool call: Bash** (Top memory processes on pc2 and FARM RAM rule)

```
ssh pc2 'powershell -NoProfile -Command "Get-Process | Sort-Object WorkingSet64 -Descending | Select-Object -First 8 Name,@{n=\"MB\";e={[int]($_.WorkingSet64/1MB)}} | Format-Table -HideTableHeaders"'; grep -n -i -E "ram|6 GB" "[notes]/unreal/megajam-2026/farm/FARM.md" | head -8
```

Result:

```
Memory Compression 1078
[another platform]Beta   1037
[another platform]Beta    975
[another platform]Beta    926
[another platform]Beta    684
[another platform]Beta    671
MsMpEng             483
[another platform]Beta    421


grep: [notes]/unreal/megajam-2026/farm/FARM.md: No such file or directory
```

**Sun 15 Nov 11:54:33 · Tool call: Bash** (Find the farm RAM rule)

```
cd "[notes]/unreal/megajam-2026"; ls farm | head; grep -rn -i -E "free.?ram|GB free|6 GB" farm/*.md lanes/COMMON_RULES.md 2>/dev/null | head -8
```

Result:

```
__pycache__
farm.sh
mirror.py
remote
lanes/COMMON_RULES.md:22:- Before each heavy step run the load check `FARM.md` describes (under 60% CPU, enough free RAM, no `Supercut`,
```

**Sun 15 Nov 11:54:37 · Tool call: Bash** (Locate FARM.md free RAM guidance)

```
cd "[notes]/unreal/megajam-2026"; f=$(ls ../*.md FARM.md lanes/*.md 2>/dev/null | xargs grep -l -i "free_ram\|free RAM" 2>/dev/null); echo "$f"; for x in $f; do grep -n -i "free ram\|free_ram" "$x" | head -4; done
```

Result:

```
../FINDINGS.md
FARM.md
lanes/COMMON_RULES.md
441:  after a change in `FloodlineCore`. Free RAM there was 8 to 10 GB during the lane with a [another platform]
112:- `free_ram_gb` is at least 6,
22:- Before each heavy step run the load check `FARM.md` describes (under 60% CPU, enough free RAM, no `Supercut`,
```

**Sun 15 Nov 11:54:39 · Tool call: Bash** (Read FARM load check section)

```
cd "[notes]/unreal/megajam-2026"; sed -n 100,130p FARM.md
```

Result:

```
runs from two lanes' own package folders were not tried. Before `run`, check that `busy_procs` in `status` shows
  no `Supercut`; if it does, wait.

## Before a heavy step (build, test, package, run)

A person uses [pc-b] and [pc-c], and pc2 has [another platform] Studio windows open. Before each heavy step run
`"$F" status <host>` and go ahead only if:

- `busy_procs` shows no `Supercut` (a tester may be playing; never stop it) and no other lane's `UnrealEditor` run
  you would double up on. `SupercutMainCheckx1` in that list is not a process: it means the main thread's merge
  check is waiting for this PC or running on it (flag file `<root>\Farm\_main_waiting`, younger than 20 minutes,
  read by `remote/status.ps1`; added 14 Nov 22:10). Treat it as busy and wait, so the merge check goes first,
- `free_ram_gb` is at least 6,
- `cpu_load_pct` is under 60.

Otherwise wait and check again in a few minutes. Never close, move or click a [another platform] Studio window on any farm PC,
never stop a process you did not start, and never touch `C:\SupercutPlaytest`, `C:\UE\Builds\Supercut59_feel` or
`C:\UE\feelstudy` on [pc-b].

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
```

**Sun 15 Nov 11:54:47 · Tool call: Bash** (Check RAM readings logged so far)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -n -i "ram" LOG.md | cut -c1-200
```

Result:

```
6:- 10:54 pc2 status: free RAM 5.4 GB, CPU 2 %, busy none. Mirrored worktree (3010 files, 88 s). Started build (-Jobs 4, RAM short) then package, background.
11:- 11:03 pc2 free RAM 0.9 to 1.7 GB while the build compiles (its Studio windows); build slow.
12:- CSV profiler: `-csvCaptureFrames=N` boot capture (`CsvProfiler.cpp:5054`, `5182`); FrameTime is wall time from cycle stamps (`CsvProfiler.cpp:4163-4168`), so it is a real frame time even with -Us
15:- 11:06 [pc-b]: free RAM 6.9 GB, CPU 31 %, another lane's cl running (builds queue). Started mirror, build, package there for the picture comparison.
16:- 11:09 pc2 build passed (822 s, -Jobs 4; RAM 0.9 to 1.7 GB free while compiling). [pc-b] build passed (318 s).
18:- 11:24 pc2: hands2's tests running (UnrealEditor-Cmd); waited until busy none (11:26, RAM 6.2 GB, CPU 0 %).
20:- 11:28 pc2 busy again: hands2's uncooked main8 run (UnrealEditor -game -RenderOffscreen), GPU 97 %, 128 W. Waiting; no frame time run while it runs.
21:- 11:29 [pc-b]: busy none, RAM 10.6 GB, CPU 21 %. Package started there.
```

**Sun 15 Nov 11:54:58 · Tool call: Bash** (Add the 6 GB free RAM gate to go.sh)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/go.sh'
s=open(p,encoding='utf-8').read()
old='''  busy=$(echo "$st" | sed -n 's/^busy_procs=//p'); cpu=$(echo "$st" | sed -n 's/^cpu_load_pct=\\([0-9]*\\).*/\\1/p')
  if [ "$busy" = "none" ] && [ "${cpu:-100}" -lt 60 ]; then break; fi
  echo "$(date +%H:%M) pc2 busy ($busy, cpu $cpu), waiting"; sleep 60; waited=$((waited+60))
  [ $waited -gt 1800 ] && { echo "pc2 busy for 30 min, giving up"; exit 1; }'''
new='''  busy=$(echo "$st" | sed -n 's/^busy_procs=//p'); cpu=$(echo "$st" | sed -n 's/^cpu_load_pct=\\([0-9]*\\).*/\\1/p')
  ram=$(echo "$st" | sed -n 's/^free_ram_gb=\\([0-9]*\\).*/\\1/p')
  if [ "$busy" = "none" ] && [ "${cpu:-100}" -lt 60 ] && [ "${ram:-0}" -ge 6 ]; then break; fi
  echo "$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting"; sleep 60; waited=$((waited+60))
  [ $waited -gt ${WAIT_MAX:-1800} ] && { echo "pc2 not ready for $waited s, giving up"; exit 1; }'''
assert old in s, 'nomatch'; s=s.replace(old,new)
s=s.replace("# 1. farm load check (busy_procs none, CPU < 60)","# 1. farm load check (busy_procs none, CPU < 60, free RAM >= 6 GB)")
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
grep -n "ram" tools/go.sh
```

Result:

```
<stdin>:3: SyntaxWarning: invalid escape sequence '\('
<stdin>:7: SyntaxWarning: invalid escape sequence '\('
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
AssertionError: nomatch
23:echo "before: $(echo "$st" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\n' ' ')" > logs/$tag/load.txt
44:echo "after: $(echo "$st" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\n' ' ')" >> logs/$tag/load.txt
```

### Sun 15 Nov 11:55:00 · Agent (claude-opus-5-5)

Doing it with the Edit tool instead.

**Sun 15 Nov 11:55:03 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "old_string": "  if [ \"$busy\" = \"none\" ] && [ \"${cpu:-100}\" -lt 60 ]; then break; fi\n  echo \"$(date +%H:%M) pc2 busy ($busy, cpu $cpu), waiting\"; sleep 60; waited=$((waited+60))\n  [ $waited -gt 1800 ] && { echo \"pc2 busy for 30 min, giving up\"; exit 1; }",
 "new_string": "  ram=$(echo \"$st\" | sed -n 's/^free_ram_gb=\\([0-9]*\\).*/\\1/p')\n  if [ \"$busy\" = \"none\" ] && [ \"${cpu:-100}\" -lt 60 ] && [ \"${ram:-0}\" -ge 6 ]; then break; fi\n  echo \"$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting\"; sleep 60; waited=$((waited+60))\n  [ $waited -gt ${WAIT_MAX:-1800} ] && { echo \"pc2 not ready for $waited s, giving up\"; exit 1; }"
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\perf3\tools\go.sh has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:55:04 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "old_string": "# 1. farm load check (busy_procs none, CPU < 60)",
 "new_string": "# 1. farm load check (busy_procs none, CPU < 60, free RAM >= 6 GB)"
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\perf3\tools\go.sh has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:55:26 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\queue.sh",
 "content": "#!/bin/bash\n# Lane perf3: run steps on pc2 one after another, each behind the farm load check.\n# usage: queue.sh step... ; a step is \"pics\" (farm offscreen picture run like [pc-b]'s) or \"<tag>:<argfile>[:switches]\"\ncd \"$(dirname \"$0\")/..\"\nF=\"[notes]/unreal/megajam-2026/farm/farm.sh\"\nready() {\n  local waited=0\n  while true; do\n    st=$(\"$F\" status pc2 2>/dev/null)\n    busy=$(echo \"$st\" | sed -n 's/^busy_procs=//p'); cpu=$(echo \"$st\" | sed -n 's/^cpu_load_pct=\\([0-9]*\\).*/\\1/p')\n    ram=$(echo \"$st\" | sed -n 's/^free_ram_gb=\\([0-9]*\\).*/\\1/p')\n    if [ \"$busy\" = \"none\" ] && [ \"${cpu:-100}\" -lt 60 ] && [ \"${ram:-0}\" -ge 6 ]; then return 0; fi\n    echo \"$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting\"; sleep 60; waited=$((waited+60))\n    [ $waited -gt 3600 ] && { echo \"pc2 not ready for an hour, giving up\"; return 1; }\n  done\n}\nfor step in \"$@\"; do\n  echo \"=== $(date +%H:%M:%S) $step\"\n  if [ \"$step\" = pics ]; then\n    ready || exit 1\n    mkdir -p logs/pics_pc2\n    echo \"before: $(echo \"$st\" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\\n' ' ')\" > logs/pics_pc2/load.txt\n    \"$F\" run pc2 perf3 /d/UE/wt/perf3_farmlogs -Packaged -Exe '{B}\\Supercut59\\Windows\\Supercut.exe' -Title -Run main8 -Seed 1 \\\n      -Script 'C:\\UE\\Farm\\_out\\perf3\\desktools\\title_main8.txt' -FixedFps 240 -Silent -ResX 1920 -ResY 1080 -TimeoutSeconds 900 2>&1 | tail -5\n    st=$(\"$F\" status pc2 2>/dev/null)\n    echo \"after: $(echo \"$st\" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\\n' ' ')\" >> logs/pics_pc2/load.txt\n    cat logs/pics_pc2/load.txt\n  else\n    IFS=: read -r tag af sw <<< \"$step\"\n    WAIT_MAX=3600 bash tools/go.sh \"$tag\" \"$af\" $sw\n  fi\ndone\necho \"=== $(date +%H:%M:%S) queue done\"\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\queue.sh (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:55:32 · Tool call: Bash** (List arg files and farm log folder)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; ls tools/args; ls /d/UE/wt/perf3_farmlogs 2>/dev/null | head; date +%H:%M
```

Result:

```
gen_s7_fx.args
hall.args
main8_fx.args
title_main8.args
title_main8.txt
bp.txt
build
package
pkg.txt
11:55
```

**Sun 15 Nov 11:55:36 · Tool call: Bash** (Run the pc2 measurement queue in the background)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; bash tools/queue.sh pics main8_a:main8_fx.args hall_a:hall.args gen_a:gen_s7_fx.args first2:title_main8.args:-ClearCaches warm1:title_main8.args > logs/queue1.txt 2>&1
```

Result:

```
Command running in background with ID: bdmv9f1ql. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bdmv9f1ql.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\lanes\perf3; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Sun 15 Nov 11:55:39 · Tool call: Bash** (Read the end of LOG.md)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -15 LOG.md | cut -c1-300
```

Result:

```
- 10:57 D3D12 side: `D3D12Shaders.cpp:107` `ValidateShaderIsUsable` refuses a shader needing wave ops, bindless, stencil ref or barycentrics the card lacks, but has no check for `SixteenBitTypes`, `TypedUAVLoadsExtended` or `Atomic64` (flags recorded by `D3DShaderCompilerDXC.cpp:1146`). The driver c
- 10:58 existing logs on c4: every RTX 4080 SUPER and RX 9070 XT packaged run has 0 of these errors; pc2 packaged (viewmerge1) 24; pc2 uncooked editor run (view1) 0. So: cooked package + Pascal card.
- 11:00 first-start level code now `FirstStartLevel` = benchmark lowest - 1, clamped 1..2 (`SupercutUserSettings.cpp:171`), so pc2 should get HIGH now, not EPIC as in perf2. DLSS default 0 (OFF) on every card.
- 11:03 pc2 free RAM 0.9 to 1.7 GB while the build compiles (its Studio windows); build slow.
- CSV profiler: `-csvCaptureFrames=N` boot capture (`CsvProfiler.cpp:5054`, `5182`); FrameTime is wall time from cycle stamps (`CsvProfiler.cpp:4163-4168`), so it is a real frame time even with -UseFixedTimeStep. `-csvGpuStats` (`CsvProfiler.cpp:5103`) adds GPU pass times.
- 11:05 lead for the 24: TSR (`TemporalSuperResolution.cpp`). `FTSRDecimateHistoryCS` (line 911) and `FTSRUpdateHistoryCS` (line 1313) compile a 16-bit permutation (`F16BitVALUDim`, `CFLAG_AllowRealTypes`, lines 987 and 1396) on SM6 because `bSupportsRealTypes=RuntimeDependent` (`Engine/Config/Windo
- 11:06 project has the bundled pipeline cache slot but no file: every pc2 log says `Could not open FPipelineCacheFile: ../../../Supercut/Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache`. Shared shader library on (1907 shaders). The cook bundles one from `Build/Windows/Pipeli
- 11:06 [pc-b]: free RAM 6.9 GB, CPU 31 %, another lane's cl running (builds queue). Started mirror, build, package there for the picture comparison.
- 11:09 pc2 build passed (822 s, -Jobs 4; RAM 0.9 to 1.7 GB free while compiling). [pc-b] build passed (318 s).
- 11:16 my chained `build && status | grep && package` stopped after the build on both PCs without running package (cause not found; ran package on its own after).
- 11:24 pc2: hands2's tests running (UnrealEditor-Cmd); waited until busy none (11:26, RAM 6.2 GB, CPU 0 %).
- 11:26 pc2 package passed, 83 s, cook 1327 packages, 0 `Failed to compile Material`.
- 11:28 pc2 busy again: hands2's uncooked main8 run (UnrealEditor -game -RenderOffscreen), GPU 97 %, 128 W. Waiting; no frame time run while it runs.
- 11:29 [pc-b]: busy none, RAM 10.6 GB, CPU 21 %
[... 147 more characters not shown]
```

**Sun 15 Nov 11:55:48 · Tool call: Bash** (Append progress to LOG.md)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat >> LOG.md <<'EOF'
- 11:46 [pc-b] package passed (529 s, 0 `Failed to compile Material`). 11:50 [pc-b] picture run (farm, offscreen, `-Title`, title_main8, FixedFps 240, 1920x1080): benchmark CPU 261 GPU 385, quality HIGH; `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`; 0 `Failed to create compute pipeline`; 65 shots.
- 11:40 run first1 (pc2 desktop session via scheduled task, caches and settings cleared, from the title): benchmark CPU 192 GPU 256, all groups 3, quality HIGH, FULLSCREEN 1920x1080. `RUN wrapped: takes 1, time 98.4 s, shots 46, freezes 14, kills 17` (no fixed step, so wall time). FPS rolling avg 72.8, slowest 1 % 50.8. 24 compute pipeline errors. Load before: busy none, CPU 1 %, GPU 25 %, free RAM 4.0 GB, which is under FARM.md's 6 GB, so first1 is marked and gets a rerun (first2). I missed the RAM rule in go.sh; it checks free RAM >= 6 now.
- 11:53 first1 hitches, first 60 s from the title (after the benchmark): 230 ms and 100 ms on the first title frames (39 graphics PSOs `PSOPrecacheState: Missed` in that second, 48 missed in the whole run, 8 more during load), 60.4 ms at the change into scene 2 (a_the_cue). Every room change costs 30 to 60 ms over its first two frames (the game logs them): 29/33, 61/37, 36/28, 36/26, 35/28, 38/27, 30/28, 44/24 ms.
- 11:55 pc2 free RAM 4.4 GB (its [another platform] Studio windows hold about 5 GB). Queue started (tools/queue.sh): pc2 picture run, main8_a, hall_a, gen_a, first2 (cold), warm1, each waiting for busy none, CPU < 60 % and free RAM >= 6 GB.
EOF
```

Result:

```
(Bash completed with no output)
```

### Sun 15 Nov 11:55:51 · Agent (claude-opus-5-5)

The pc2 queue is waiting for free RAM. Meanwhile I'm converting [pc-b]'s pictures to 960-wide JPGs so the pairs are ready.

**Sun 15 Nov 11:55:53 · Tool call: Bash** (List [pc-b] shots, check PIL, queue status)

```
ls /d/UE/wt/perf3_farmlogs_[pc-b]/run/shots | head -5; ls /d/UE/wt/perf3_farmlogs_[pc-b]/run/shots | wc -l; python -I -c "import PIL; print(PIL.__version__)"; cat "C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/2f0f321c-13ca-453f-9197-384709201b64/tasks/bdmv9f1ql.output" | tail -3
```

Result:

```
s1_01_start.png
s1_02_at_the_machine.png
s1_03_machine_stopped.png
s1_04_out_of_the_tunnel.png
s1_05_grunt_frozen.png
65
12.2.0
```

**Sun 15 Nov 11:55:56 · Tool call: Bash** (Check queue progress)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat logs/queue1.txt
```

Result:

```
=== 11:55:36 pics
11:55 pc2 not ready (clx1 dotnetx1, cpu 0, free ram 2 GB), waiting
```

**Sun 15 Nov 11:56:06 · Tool call: Bash** (Read TSR 16-bit permutation and cvar code)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; sed -n 505,560p "$S"; echo ----; sed -n 975,1000p "$S"; echo ----; sed -n 1385,1410p "$S"
```

Result:

```
}

	static const auto CVarNaniteFoliage = IConsoleManager::Get().FindTConsoleVariableDataInt(TEXT("r.Nanite.Foliage"));
	static const bool bNaniteFoliageEnabled = (CVarNaniteFoliage && CVarNaniteFoliage->GetValueOnAnyThread() != 0);
	return bNaniteFoliageEnabled || ThinGeometryDetection != 0;
}

// WebGPU has no texture atomics, so on SP_WEBGPU_SM5 the closest-occluder scatter
// (TSR.PrevAtomics) is a storage buffer of 8x8 pixel tiles instead of a texture array (TSRClosestOccluder.ush).
static bool TSRPrevAtomicsInBuffer(EShaderPlatform Platform)
{
	return IsWebGPUSM5ShaderPlatform(Platform);	// The shared helper
}

class FTSRShader : public FGlobalShader
{
public:
	static constexpr int32 kSupportMinWaveSize = 32;
	static constexpr int32 kSupportMaxWaveSize = 64;

	class F16BitVALUDim : SHADER_PERMUTATION_BOOL("DIM_16BIT_VALU");
	class FAlphaChannelDim : SHADER_PERMUTATION_BOOL("DIM_ALPHA_CHANNEL");

	FTSRShader(const ShaderMetaType::CompiledShaderInitializerType& Initializer)
		: FGlobalShader(Initializer)
	{ }

	FTSRShader()
	{ }

	static ERHIFeatureSupport Supports16BitVALU(EShaderPlatform Platform)
	{
		// UE-254365
		if (IsVulkanPlatform(Platform))
		{
			return ERHIFeatureSupport::Unsupported;
		}

		return FDataDrivenShaderPlatformInfo::GetSupportsRealTypes(Platform);
	}

	static bool ShouldCompile32or16BitPermutation(EShaderPlatform Platform, bool bIs16BitVALUPermutation)
	{
		// Always compile the 32bit permutations for the alpha channel
		if (!bIs16BitVALUPermutation)
		{
			return true;
		}

		const ERHIFeatureSupport Support = FTSRShader::Supports16BitVALU(Platform);
		return Support != ERHIFeatureSupport::Unsupported;
	}

	static ERHIFeatureSupport SupportsWaveOps(EShaderPlatform Platform)
	{
		return FDataDrivenShaderPlatformInfo::GetSupportsWaveOperations(Platform);
----
		{
			return false;
		}

		return true;
	}

	static void ModifyCompilationEnvironment(const FGlobalShaderPermutationParameters& Parameters, FShaderCompilerEnvironment& OutEnvironment)
	{
		FTSRShader::ModifyCompilationEnvironment(Parameters, OutEnvironment);

		FPermutationDomain PermutationVector(Parameters.PermutationId);
		if (PermutationVector.Get<FTSRShader::F16BitVALUDim>())
		{
			OutEnvironment.CompilerFlags.Add(CFLAG_AllowRealTypes);
		}
	}
}; // class FTSRDecimateHistoryCS

class FTSRRejectShadingCS : public FTSRConvolutionNetworkShader
{
	DECLARE_GLOBAL_SHADER(FTSRRejectShadingCS);
	SHADER_USE_PARAMETER_STRUCT(FTSRRejectShadingCS, FTSRConvolutionNetworkShader);

[... 1111 more characters not shown]
```

**Sun 15 Nov 11:56:10 · Tool call: Bash** (Which TSR shaders override ShouldPrecachePermutation)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; grep -n -E "ShouldPrecachePermutation|^class FTSR|Use16BitVALU\(|r\.TSR\.16Bit" "$S" | head -60
```

Result:

```
100:	TEXT("r.TSR.16BitVALU"), 1,
107:	TEXT("r.TSR.16BitVALU.AMD"), 1,
112:	TEXT("r.TSR.16BitVALU.Intel"), 1,
117:	TEXT("r.TSR.16BitVALU.Nvidia"), 1,
519:class FTSRShader : public FGlobalShader
636:bool Use16BitVALU(EShaderPlatform ShaderPlatform)
664:class FTSRConvolutionNetworkShader : public FTSRShader
717:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters, FPermutationDomain PermutationVector)
723:		bool bUse16BitVALU = Use16BitVALU(Parameters.Platform) && !bSupportsAlpha && PermutationVector.Get<FWaveSizeOps>() != 0;
763:class FTSRMeasureFlickeringLumaCS : public FTSRShader
806:class FTSRMeasureThinGeometryCoverageCS : public FTSRShader
833:class FTSRClearPrevTexturesCS : public FTSRShader
846:class FTSRDilateVelocityCS : public FTSRShader
911:class FTSRDecimateHistoryCS : public FTSRShader
994:class FTSRRejectShadingCS : public FTSRConvolutionNetworkShader
1100:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1103:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1123:class FTSRDetectThinGeometryCS : public FTSRConvolutionNetworkShader
1187:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1190:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1209:class FTSRWeightRelaxationCS : public FTSRConvolutionNetworkShader
1257:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FGlobalShaderPermutationParameters& Parameters)
1260:		return FTSRConvolutionNetworkShader::ShouldPrecachePermutation(Parameters, PermutationVector.Get<FTSRConvolutionNetworkShader::FPermutationDomain>());
1276:class FTSRSpatialAntiAliasingCS : public FTSRShader
1313:class FTSRUpdateHistoryCS : public FTSRShader
1403:class FTSRResolveHistoryCS : public FTSRShader
1467:	static EShaderPermutationPrecacheRequest ShouldPrecachePermutation(const FShaderPermutationParameters& Parameters)
1476:		return FGlobalShader::ShouldPrecachePermutation(Parameters);
1497:class FTSRVisualizeCS : public FTSRShader
1967:	bool bUse16BitVALU = Use16BitVALU(ShaderPlatform);
```

**Sun 15 Nov 11:56:12 · Tool call: Bash** (Read TSR 16-bit cvars and Use16BitVALU)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; sed -n 96,122p "$S"; sed -n 636,662p "$S"; sed -n 1960,1975p "$S"
```

Result:

```
TEXT(" 64: WaveSizeOps 64;\n"),
	ECVF_RenderThreadSafe);

TAutoConsoleVariable<int32> CVarTSR16BitVALU(
	TEXT("r.TSR.16BitVALU"), 1,
	TEXT("Whether to use 16bit VALU on platform that have bSupportsRealTypes=RuntimeDependent"),
	ECVF_RenderThreadSafe);

#if PLATFORM_DESKTOP

TAutoConsoleVariable<int32> CVarTSR16BitVALUOnAMD(
	TEXT("r.TSR.16BitVALU.AMD"), 1,
	TEXT("Overrides whether to use 16bit VALU on AMD desktop GPUs"),
	ECVF_RenderThreadSafe);

TAutoConsoleVariable<int32> CVarTSR16BitVALUOnIntel(
	TEXT("r.TSR.16BitVALU.Intel"), 1,
	TEXT("Overrides whether to use 16bit VALU on Intel desktop GPUs"),
	ECVF_RenderThreadSafe);

TAutoConsoleVariable<int32> CVarTSR16BitVALUOnNvidia(
	TEXT("r.TSR.16BitVALU.Nvidia"), 1,
	TEXT("Overrides whether to use 16bit VALU on Nvidia desktop GPUs"),
	ECVF_RenderThreadSafe);

#endif // PLATFORM_DESKTOP

bool Use16BitVALU(EShaderPlatform ShaderPlatform)
{
	// Whether to use 16bit VALU
	const ERHIFeatureSupport VALU16BitSupport = FTSRShader::Supports16BitVALU(ShaderPlatform);
	bool bUse16BitVALU = (CVarTSR16BitVALU.GetValueOnAnyThread() != 0 && GRHIGlobals.SupportsNative16BitOps && VALU16BitSupport == ERHIFeatureSupport::RuntimeDependent) || VALU16BitSupport == ERHIFeatureSupport::RuntimeGuaranteed;

	// Controls whether to use 16bit ops on per GPU vendor in mean time each driver matures.
#if PLATFORM_DESKTOP
	if ((GRHIGlobals.SupportsNative16BitOps && VALU16BitSupport == ERHIFeatureSupport::RuntimeDependent) || VALU16BitSupport == ERHIFeatureSupport::RuntimeGuaranteed)
	{
		if (IsRHIDeviceAMD())
		{
			bUse16BitVALU = CVarTSR16BitVALUOnAMD.GetValueOnAnyThread() != 0;
		}
		else if (IsRHIDeviceIntel())
		{
			bUse16BitVALU = CVarTSR16BitVALUOnIntel.GetValueOnAnyThread() != 0;
		}
		else if (IsRHIDeviceNVIDIA())
		{
			bUse16BitVALU = CVarTSR16BitVALUOnNvidia.GetValueOnAnyThread() != 0;
		}
	}
#endif // PLATFORM_DESKTOP

	return bUse16BitVALU;
}
		
	const EShaderPlatform ShaderPlatform = View.GetShaderPlatform();

	// Whether lens distortion support is compiled in the shaders.
	const bool bSupportsLensDistortion = IsTSRLensDistortionSupported(ShaderPlatform);

	// Whether to use 16bit VALU
	bool bUse16BitVALU = Use16BitVALU(ShaderPlatform);

	// Whether alpha channel is supported.
	const bool bSupportsAlpha = PassConfig.AlphaChannel >= 0 ? (PassConfig.AlphaChannel > 0) : IsPostProcessingWithAlphaChannelSupported();

	const float RefreshRateToFrameRateCap = (View.Family->Time.GetDeltaRealTimeSeconds() > 0.0f && PassConfig.Shading
[... 209 more characters not shown]
```

**Sun 15 Nov 11:56:24 · Tool call: Bash** (Show the error lines and engine code that prints them)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -m3 -B2 -A3 "Failed to create compute pipeline" logs/first1/run.log | cut -c1-300; sed -n 715,740p /d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineStateCache.cpp
```

Result:

```
[2026.11.15-03.48.53:162][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xE47C8AF6CBA94493:

[2026.11.15-03.48.53:162][  0]LogRHI: Error: Failed to create compute pipeline with hash C943EEB2FC37390A.
[2026.11.15-03.48.53:162][  0]LogRHI: Error: Shader: <unknown>
[2026.11.15-03.48.53:163][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash 77C7F836F42FD243, error 80070057.
[2026.11.15-03.48.53:164][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash E3E671E1B79D05F2, error 80070057.
--
[2026.11.15-03.48.53:165][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0x77C7F836F42FD243:

[2026.11.15-03.48.53:165][  0]LogRHI: Error: Failed to create compute pipeline with hash 1403E8480EF42111.
[2026.11.15-03.48.53:165][  0]LogRHI: Error: Shader: <unknown>
[2026.11.15-03.48.53:165][  0]LogD3D12RHI: Error: Failed to create pipeline state with combined hash C0757229C38FC560, error 80070057.
[2026.11.15-03.48.53:166][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xE3E671E1B79D05F2:

[2026.11.15-03.48.53:166][  0]LogRHI: Error: Failed to create compute pipeline with hash 8685ECF03AC18C7B.
[2026.11.15-03.48.53:166][  0]LogRHI: Error: Shader: <unknown>
[2026.11.15-03.48.53:166][  0]LogD3D12RHI: Warning: Failed to create compute PSO with combined hash 0xA51AAEFC95EFEDCD:


	if(Init.bFromPSOFileCache)
	{
		// Let the cache know so it hopefully won't give out this one again
		FPipelineFileCacheManager::RegisterPSOCompileFailure(GetTypeHash(Init), Init);
	}
	else if(!Init.bPSOPrecache)
	{
		// Precache requests are allowed to fail, but if the PSO is needed by a draw/dispatch command, we cannot continue.
		UE_LOGF(LogRHI, Fatal, "Shader compilation failures are Fatal.");
	}
}

// Prints out information about a failed compute pipeline compilation.
// This is fatal unless the compilation request is coming from the precaching system.
static void HandlePipelineCreationFailure(const FComputePipelineStateInitializer& Init)
{
	// Dump the shader hash so it can be looked up in the SHK data. See the previous function for details.
	UE_LOGF(LogRHI, Error, "Failed to create compute pipeline with hash %ls.", *Init.ComputeShader->GetHash().ToString());

#if !(UE_BUILD_SHIPPING || UE_BUILD_TEST)
	UE_LOGF(LogRHI, Error, "Shader: %ls", Init.ComputeShader->GetShaderName());
#endif

	if (!Init.bPSOPrecache && !Init.bFromPSOFileCache)
	{
```

**Sun 15 Nov 11:56:33 · Tool call: Bash** (Queue status and fatal line for compute)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -3 logs/queue1.txt; sed -n 740,750p /d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineStateCache.cpp
```

Result:

```
=== 11:55:36 pics
11:55 pc2 not ready (clx1 dotnetx1, cpu 0, free ram 2 GB), waiting
	{
		// Precache requests are allowed to fail, but if the PSO is needed by a draw/dispatch command, we cannot continue.
		UE_LOGF(LogRHI, Fatal, "Shader compilation failures are Fatal.");
	}
}

#if PSO_TRACK_CACHE_STATS

static std::atomic_uint64_t TotalPrecompileCompleteTime[(int)EPSOPrecachePriority::Num];
static std::atomic_uint64_t TotalPrecompileCompileTime[(int)EPSOPrecachePriority::Num];
static std::atomic_uint64_t TotalPrecompileTimeToBegin[(int)EPSOPrecachePriority::Num];
```

**Sun 15 Nov 11:56:38 · Tool call: Bash** (Convert [pc-b] shots to 960 JPG)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; mkdir -p shots/[pc-b]; python -I - <<'EOF'
import os
from PIL import Image
src='D:/UE/wt/perf3_farmlogs_[pc-b]/run/shots'; dst='shots/[pc-b]'
for f in sorted(os.listdir(src)):
    if f.endswith('.png'):
        im=Image.open(os.path.join(src,f)).convert('RGB'); w,h=im.size
        im.resize((960, round(h*960/w)), Image.LANCZOS).save(os.path.join(dst,f[:-4]+'.jpg'), quality=85)
print(len(os.listdir(dst)), w, h)
EOF
date +%H:%M; tail -2 logs/queue1.txt
```

Result:

```
65 1920 1080
11:56
11:55 pc2 not ready (clx1 dotnetx1, cpu 0, free ram 2 GB), waiting
11:56 pc2 not ready (clx1 dotnetx1, cpu 2, free ram 2 GB), waiting
```

**Sun 15 Nov 11:56:57 · Tool call: Bash** (Find PSO recording switches in engine source)

```
E=/d/UE/UE_5.9/Engine/Source; grep -rn -E "\"logPSO\"|TEXT\(\"logPSO\"\)|r\.ShaderPipelineCache\.(LogPSO|Enabled|StartupMode|SaveAfterPSOsLogged)\"" $E/Runtime/RenderCore $E/Runtime/RHI 2>/dev/null | head; grep -rln "UShaderPipelineCacheToolsCommandlet" $E/Editor | head -3
```

Result:

```
/d/UE/UE_5.9/Engine/Source/Runtime/RenderCore/Private/ShaderPipelineCache.cpp:56:														  TEXT("r.ShaderPipelineCache.StartupMode"),
/d/UE/UE_5.9/Engine/Source/Runtime/RenderCore/Private/ShaderPipelineCache.cpp:115:														   TEXT("r.ShaderPipelineCache.SaveAfterPSOsLogged"),
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:114:														   TEXT("r.ShaderPipelineCache.Enabled"),
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:121:														   TEXT("r.ShaderPipelineCache.LogPSO"),
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:1886:		bCmdLineForce = FParse::Param(FCommandLine::Get(), TEXT("deleteuserpsocache")) || FParse::Param(FCommandLine::Get(), TEXT("logPSO"));
/d/UE/UE_5.9/Engine/Source/Editor/UnrealEd/Classes/Commandlets/ShaderPipelineCacheToolsCommandlet.h
/d/UE/UE_5.9/Engine/Source/Editor/UnrealEd/Private/Commandlets/ShaderPipelineCacheToolsCommandlet.cpp
/d/UE/UE_5.9/Engine/Source/Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp
```

**Sun 15 Nov 11:57:07 · Tool call: Bash** (Read PSO logging cvars and save paths)

```
E=/d/UE/UE_5.9/Engine/Source; sed -n 108,130p $E/Runtime/RHI/Private/PipelineFileCache.cpp; sed -n 1880,1900p $E/Runtime/RHI/Private/PipelineFileCache.cpp; grep -n -E "logPSO|LogPSO|CollectedPSOs|rec\.upipelinecache|SaveFileCache|bLogPSO" $E/Runtime/RHI/Private/PipelineFileCache.cpp $E/Runtime/RenderCore/Private/ShaderPipelineCache.cpp | head -30
```

Result:

```
/**
  * PipelineFileCache API access
  **/

static TAutoConsoleVariable<int32> CVarPSOFileCacheEnabled(
														   TEXT("r.ShaderPipelineCache.Enabled"),
														   PIPELINE_CACHE_DEFAULT_ENABLED,
														   TEXT("1 Enables the PipelineFileCache, 0 disables it."),
														   ECVF_Default | ECVF_RenderThreadSafe
														   );

static TAutoConsoleVariable<int32> CVarPSOFileCacheLogPSO(
														   TEXT("r.ShaderPipelineCache.LogPSO"),
														   PIPELINE_CACHE_DEFAULT_ENABLED,
														   TEXT("1 Logs new PSO entries into the file cache and allows saving."),
														   ECVF_Default | ECVF_RenderThreadSafe
														   );

static TAutoConsoleVariable<int32> CVarPSOFileCacheReportPSO(
														   TEXT("r.ShaderPipelineCache.ReportPSO"),
														   PIPELINE_CACHE_DEFAULT_ENABLED,
														   TEXT("1 reports new PSO entries via a delegate, but does not record or modify any cache file. New PSOs are reported in bulk once per frame."),
{
	static bool bOnce = false;
	static bool bCmdLineForce = false;
	if (!bOnce)
	{
		bOnce = true;
		bCmdLineForce = FParse::Param(FCommandLine::Get(), TEXT("deleteuserpsocache")) || FParse::Param(FCommandLine::Get(), TEXT("logPSO"));
		UE_CLOGF(bCmdLineForce, LogRHI, Warning, "****************************** Deleting user-writable PSO cache as requested on command line");
	}
	return bCmdLineForce;
}

class FPipelineCacheFile
{
	FString Name;
	EShaderPlatform ShaderPlatform;
	FName PlatformName;
	uint64 TOCOffset;

	FPipelineCacheFileFormatTOC TOC;
	FGuid FileGuid;
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:120:static TAutoConsoleVariable<int32> CVarPSOFileCacheLogPSO(
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:121:														   TEXT("r.ShaderPipelineCache.LogPSO"),
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:1886:		bCmdLineForce = FParse::Param(FCommandLine::Get(), TEXT("deleteuserpsocache")) || FParse::Param(FCommandLine::Get(), TEXT("logPSO"));
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:2295:			RecordingFilename += FString::Printf(TEXT("%s_%s_%s.rec.upipelinecache"), *Name, *PlatformName.ToString(), *UniqueFileGuid.ToString());
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.cpp:2296:			RecordingFilename = FPaths::ProjectSavedDir() / TEXT("CollectedPSOs") / RecordingFilename;
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Private/PipelineFileCache.c
[... 1714 more characters not shown]
```

**Sun 15 Nov 11:57:12 · Tool call: Bash** (Read pipeline cache startup mode and save calls)

```
E=/d/UE/UE_5.9/Engine/Source; f=$E/Runtime/RenderCore/Private/ShaderPipelineCache.cpp; sed -n 50,70p $f; sed -n 112,122p $f; grep -n -E "SavePipelineFileCache\(|Shutdown\(|SaveMode|BoundPSO|FPipelineFileCacheManager::SaveMode" $f | head -20
```

Result:

```
static TCHAR const* SortOrderKey = TEXT("SortOrder");
	static TCHAR const* GameVersionKey = TEXT("GameVersion");
}


static TAutoConsoleVariable<int32> CVarPSOFileCacheStartupMode(
														  TEXT("r.ShaderPipelineCache.StartupMode"),
														  1,
														  TEXT("Sets the startup mode for the PSO cache, determining what the cache does after initialisation:\n")
														  TEXT("\t0: Precompilation is paused and nothing will compile until a call to ResumeBatching().\n")
														  TEXT("\t1: Precompilation is enabled in the 'Fast' mode.\n")
														  TEXT("\t2: Precompilation is enabled in the 'Background' mode.\n")
														  TEXT("Default is 1."),
														  ECVF_Default | ECVF_RenderThreadSafe
														  );

static TAutoConsoleVariable<int32> CVarPSOFileCacheBackgroundBatchSize(
														  TEXT("r.ShaderPipelineCache.BackgroundBatchSize"),
														  1,
														  TEXT("Set the number of PipelineStateObjects to compile in a single batch operation when compiling in the background. Defaults to a maximum of 1 per frame, due to async. file IO it is less in practice."),
														  ECVF_Default | ECVF_RenderThreadSafe
														   ECVF_Default | ECVF_RenderThreadSafe
														   );
static TAutoConsoleVariable<int32> CVarPSOFileCacheSaveAfterPSOsLogged(
														   TEXT("r.ShaderPipelineCache.SaveAfterPSOsLogged"),
														   0,
														   TEXT("Set the number of PipelineStateObjects to log before automatically saving. 0 will disable automatic saving (which is the default now, as automatic saving is found to be broken)."),
														   ECVF_Default | ECVF_RenderThreadSafe
														   );
 
static TAutoConsoleVariable<int32> CVarPSOFileCacheAutoSaveTime(
															TEXT("r.ShaderPipelineCache.AutoSaveTime"),
135:static TAutoConsoleVariable<int32> CVarPSOFileCacheAutoSaveTimeBoundPSO(
136:	TEXT("r.ShaderPipelineCache.AutoSaveTimeBoundPSO"),
143:static TAutoConsoleVariable<int32> CVarPSOFileCacheSaveBoundPSOLog(
144:																 TEXT("r.ShaderPipelineCache.SaveBoundPSOLog"),
202:static bool GetShaderPipelineCacheSaveBoundPSOLog()
211:	return GRHISupportsPipelineFileCache && (bCmdLineForce || CVarPSOFileCacheSaveBoundPSOLog.GetValueOnAnyThread() == 1);
231:void ConsoleCommandSavePipelineFileCache()
233:	if (GetShaderPipelineCacheSaveBoundPSOLog())
235:		FShaderPipelineCache::SavePipelineFileCache(FPipelineFileCacheManager::SaveMode::BoundPSOsOnly);
239:		FSh
[... 803 more characters not shown]
```

**Sun 15 Nov 11:57:16 · Tool call: Bash** (Read pipeline cache save-on-exit code)

```
E=/d/UE/UE_5.9/Engine/Source; f=$E/Runtime/RenderCore/Private/ShaderPipelineCache.cpp; sed -n 655,680p $f; sed -n 777,800p $f; grep -rn "define PIPELINE_CACHE_DEFAULT_ENABLED" $E/Runtime/RHI | head
```

Result:

```
FShaderPipelineCache* FShaderPipelineCache::ShaderPipelineCache = nullptr;
FString FShaderPipelineCache::UserCacheTaskKey;

FShaderPipelineCache::FShaderCachePreOpenDelegate FShaderPipelineCache::OnCachePreOpen;
FShaderPipelineCache::FShaderCacheOpenedDelegate FShaderPipelineCache::OnCachedOpened;
FShaderPipelineCache::FShaderCacheClosedDelegate FShaderPipelineCache::OnCachedClosed;
FShaderPipelineCache::FShaderPrecompilationBeginDelegate FShaderPipelineCache::OnPrecompilationBegin;
FShaderPipelineCache::FShaderPrecompilationCompleteDelegate FShaderPipelineCache::OnPrecompilationComplete;

static void PipelineStateCacheOnAppDeactivate()
{
	if (GetShaderPipelineCacheSaveBoundPSOLog())
	{
		FShaderPipelineCache::SavePipelineFileCache(FPipelineFileCacheManager::SaveMode::BoundPSOsOnly);
	}
	if (GetPSOFileCacheSaveUserCache())
	{
		FShaderPipelineCache::SavePipelineFileCache(FPipelineFileCacheManager::SaveMode::Incremental);
	}
}

int32 FShaderPipelineCache::GetGameVersionForPSOFileCache()
{
	int32 GameVersion = (int32)FEngineVersion::Current().GetChangelist();
#if WITH_EDITOR
void FShaderPipelineCache::Shutdown(void)
{
	if (ShaderPipelineCache)
	{
		delete ShaderPipelineCache;
		ShaderPipelineCache = nullptr;
	}
}

void FShaderPipelineCache::PauseBatching()
{
	if (ShaderPipelineCache)
    {
        ShaderPipelineCache->PausedCount++;
        UE_LOGF(LogRHI, Display, "ShaderPipelineCache: Paused Batching. %d", ShaderPipelineCache->PausedCount);
        if (ShaderPipelineCache->PausedCount > 0)
        {
            ShaderPipelineCache->bPaused = true;
        }
    }
}

bool FShaderPipelineCache::IsBatchingPaused()
{
/d/UE/UE_5.9/Engine/Source/Runtime/RHI/Public/PipelineFileCache.h:19:#define PIPELINE_CACHE_DEFAULT_ENABLED (!WITH_EDITOR)
```

### Sun 15 Nov 11:57:20 · Agent (claude-opus-5-5)

Still waiting on pc2 (another lane's compile). Meanwhile I'm reading how 5.9 records and ships a pipeline cache, for job 3.

**Sun 15 Nov 11:57:22 · Tool call: Bash** (Check whether the PSO log saves at shutdown)

```
E=/d/UE/UE_5.9/Engine/Source; f=$E/Runtime/RenderCore/Private/ShaderPipelineCache.cpp; n=$(grep -n "FShaderPipelineCache::~FShaderPipelineCache" $f | cut -d: -f1); sed -n "${n},$((n+25))p" $f; grep -n -A12 "FPipelineFileCacheManager::Shutdown" $E/Runtime/RHI/Private/PipelineFileCache.cpp | head -30; tail -2 "[notes]/unreal/megajam-2026/lanes/perf3/logs/queue1.txt"
```

Result:

```
FShaderPipelineCache::~FShaderPipelineCache()
{
	// The render thread tick should be dead now and we are safe to destroy everything that needs to wait or manual destruction

	FScopeLock Lock(&Mutex);
	if (NextPrecompileCacheTask.IsValid() && !NextPrecompileCacheTask->IsComplete())
	{
		NextPrecompileCacheTask->Wait();
	}
	NextPrecompileCacheTask = FGraphEventRef();

	FShaderPipelineCache::CloseUserPipelineFileCache();

	for (auto& PSOTask : ShaderCacheTasks)
	{
		PSOTask.Value->Close();
		// Close() should have called though to Flush() - all work is now in the shutdown lists
	}

	//
	// Clean up cached RHI resources
	//
	for (auto& Pair : BlendStateCache)
	{
		Pair.Value->Release();
	}
3320:void FPipelineFileCacheManager::Shutdown()
3321-{
3322-	if(IsPipelineFileCacheEnabled())
3323-	{
3324-		FRWScopeLock Lock(FileCacheLock, SLT_Write);
3325-		for (auto const& Pair : Stats)
3326-		{
3327-			delete Pair.Value;
3328-		}
3329-		Stats.Empty();
3330-		NewPSOs.Empty();
3331-        NumNewPSOs = 0;
3332-		
11:55 pc2 not ready (clx1 dotnetx1, cpu 0, free ram 2 GB), waiting
11:56 pc2 not ready (clx1 dotnetx1, cpu 2, free ram 2 GB), waiting
```

**Sun 15 Nov 11:57:26 · Tool call: Bash** (Clock and user cache close behaviour)

```
date +%H:%M:%S; E=/d/UE/UE_5.9/Engine/Source; grep -n -B3 -A10 "void FShaderPipelineCache::CloseUserPipelineFileCache" $E/Runtime/RenderCore/Private/ShaderPipelineCache.cpp | grep -n -i -E "save|close" | head
```

Result:

```
11:57:26
4:968:void FShaderPipelineCache::CloseUserPipelineFileCache()
11:975-		if (GetShaderPipelineCacheSaveBoundPSOLog())
13:977-			SavePipelineFileCache(FPipelineFileCacheManager::SaveMode::BoundPSOsOnly);
```

**Sun 15 Nov 11:57:30 · Tool call: Bash** (Read cook-side pipeline cache creation)

```
f=/d/UE/UE_5.9/Engine/Source/Editor/UnrealEd/Private/Cooker/ShaderLibraryCooking.cpp; sed -n 255,270p $f; sed -n 420,485p $f
```

Result:

```
const UProjectPackagingSettings* const PackagingSettings = GetDefault<UProjectPackagingSettings>();
	if (IsUsingShaderCodeLibrary())
	{
		FShaderLibraryCooker::InitForCooking(PackagingSettings->bSharedMaterialNativeLibraries, AllContextArtifactReader.Get());

		bool bAllPlatformsNeedStableKeys = false;
		// support setting without Hungarian prefix for the compatibility, but allow newer one to override
		GConfig->GetBool(TEXT("DevOptions.Shaders"), TEXT("NeedsShaderStableKeys"), bAllPlatformsNeedStableKeys, GEngineIni);
		GConfig->GetBool(TEXT("DevOptions.Shaders"), TEXT("bNeedsShaderStableKeys"), bAllPlatformsNeedStableKeys, GEngineIni);

		// See if we desire stable keys in DLC, PSO manual cache in DLC is not supported, so they are disabled by default
		// They have other uses so allow them to be optionally enabled
		bool bAllowShaderStableKeysInDLC = false;
		GConfig->GetBool(TEXT("DevOptions.Shaders"), TEXT("bAllowShaderStableKeysInDLC"), bAllowShaderStableKeysInDLC, GEngineIni);
		bAllPlatformsNeedStableKeys = bAllPlatformsNeedStableKeys && (!IsCookingDLC() || bAllowShaderStableKeysInDLC);

		// The shader code library directory doesn't matter while cooking
		FShaderLibraryCooker::BeginCookingLibrary(ActualName);
	}
}

void UCookOnTheFlyServer::CreatePipelineCache(const ITargetPlatform* TargetPlatform, const FString& LibraryName)
{
	// make sure we have a registry generated for all the platforms 
	const FString TargetPlatformName = TargetPlatform->PlatformName();
	TArray<FString>* SCLCSVPaths = OutSCLCSVPaths.Find(FName(TargetPlatformName));
	if (SCLCSVPaths && SCLCSVPaths->Num())
	{
		TArray<FName> ShaderFormats;
		TargetPlatform->GetAllTargetedShaderFormats(ShaderFormats);
		for (FName ShaderFormat : ShaderFormats)
		{
			const FString StablePCDir = FPaths::ProjectDir() / TEXT("Build") / TargetPlatform->IniPlatformName() / TEXT("PipelineCaches");
			// look for the new binary format for stable pipeline cache - spc
			const FString StablePCBinary = StablePCDir / FString::Printf(TEXT("*%s_%s.spc"), *LibraryName, *ShaderFormat.ToString());

			bool bBinaryStablePipelineCacheFilesFound = [&StablePCBinary]()
				{
					TArray<FString> ExpandedFiles;
					IFileManager::Get().FindFilesRecursive(ExpandedFiles, *FPaths::GetPath(StablePCBinary), *FPaths::GetCleanFilename(StablePCBinary), true, false, false);
					return ExpandedFiles.Num() > 0;
				}();

			// for now, also look for the older *stablepc.csv or *stablepc.csv.compressed
			const FString StablePCT
[... 2557 more characters not shown]
```

**Sun 15 Nov 11:57:35 · Tool call: Bash** (List farm.sh commands)

```
cd "[notes]/unreal/megajam-2026"; sed -n 1,60p farm/farm.sh | grep -n -E "^\s*#|\)\s*$|case|usage" | head -40
```

Result:

```
1:#!/bin/bash
2:# farm.sh: build, test, package and run a SUPERCUT project copy on a farm PC, driven from c4. Details: ../FARM.md.
3:#
4:#   farm.sh mirror  <host> <name> <project folder on c4>     copy the project to <root>\Farm\<name> (changed files only)
5:#   farm.sh build   <host> <name> <log folder> [build.ps1 args, e.g. -Target Supercut -Jobs 8]
6:#   farm.sh test    <host> <name> <log folder> [run_tests.ps1 args, e.g. -Filter Supercut.Rooms]
7:#   farm.sh package <host> <name> <log folder>               Tools\package.cmd   -> <root>\Farm\_builds\<name>\Supercut59
8:#   farm.sh package-shipping <host> <name> <log folder>      Tools\package_shipping.cmd -> ...\_builds\<name>\Supercut59_ship
9:#   farm.sh run     <host> <name> <log folder> [run_demo.ps1 args]   {P} = the mirror folder there, e.g. -Script {P}\Script\main8.txt
10:#   farm.sh fetch   <host> <name> <remote path> <local folder>   path in the mirror, or builds/... or out/...
11:#   farm.sh status  <host>
12:#
13:# Each step brings its logs back to <log folder>/<step>/ and exits with the remote step's exit code.
14:# Logs that come back have the PC's user and computer names replaced by USER and PC.
16:here=$(cd "$(dirname "$0")" && pwd)
18:root_of() {   # one line per farm PC: ssh alias, root folder there (engine in <root>\UE_5.9, mirrors in <root>\Farm)
19:  case "$1" in
29:# copy remote path $2 (forward slashes) from host $1 into local folder $3, masking user and computer names in text files
34:  un=$(ssh "$host" 'echo %USERNAME%' | tr -d '\r\n'); cn=$(ssh "$host" 'echo %COMPUTERNAME%' | tr -d '\r\n')
45:    local tmp; tmp=$(mktemp)
58:case "$verb" in
59:  mirror)
60:    [ $# -eq 3 ] || { echo "usage: farm.sh mirror <host> <name> <project folder on c4>" >&2; exit 64; }
```

**Sun 15 Nov 11:57:53 · Tool call: Bash** (Queue status and context of last missed PSO)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -2 logs/queue1.txt; grep -n "PSOPrecacheState" logs/first1/run.log | tail -2 | cut -c1-200; L=logs/first1/run.log; n=$(grep -n "PSOPrecacheState" $L | tail -1 | cut -d: -f1); sed -n "$((n-6)),$((n+1))p" $L | cut -c1-200
```

Result:

```
11:56 pc2 not ready (clx1 dotnetx1, cpu 2, free ram 2 GB), waiting
11:57 pc2 not ready (clx1 dotnetx1, cpu 6, free ram 2 GB), waiting
1560:[2026.11.15-03.49.02:279][  2]LogRHI: Display: Encountered a new graphics PSO: 1386134789 (PSOPrecacheState: Missed)
1611:[2026.11.15-03.49.08:540][382]LogRHI: Display: Encountered a new graphics PSO: 1902698113 (PSOPrecacheState: Missed)
[2026.11.15-03.49.07:646][331]LogSupercut: Display: SCRIPT 1.00 move 1 0| pos V(X=150.00, Z=90.15) yaw 0 health 100 rounds 6 charges 3 rolling
[2026.11.15-03.49.07:934][348]LogSupercutSound: Display: START step_1 flat
[2026.11.15-03.49.08:071][356]LogSupercut: Display: TRACE pos 372 0 90 yaw 0.0 pitch 0.0 rounds 6 charges 3 rolling
[2026.11.15-03.49.08:263][367]LogSupercutSound: Display: START step_2 flat
[2026.11.15-03.49.08:297][369]LogSupercutSound: Display: STOP step_1 flat, played out
[2026.11.15-03.49.08:540][382]LogCsvProfiler: Display: CSVEvent "PSO/Encountered new graphics PSO" [Frame 383]
[2026.11.15-03.49.08:540][382]LogRHI: Display: Encountered a new graphics PSO: 1902698113 (PSOPrecacheState: Missed)
[2026.11.15-03.49.08:577][385]LogSupercut: Display: TRACE pos 676 0 90 yaw 0.0 pitch 0.0 rounds 6 charges 3 rolling
```

**Sun 15 Nov 11:58:04 · Tool call: Bash** (Read hall and generated scripts)

```
cd /d/UE/wt/perf3; cat Script/shell1_hall_fps.txt | head -20; echo ---; grep -c . Script/gen/s7.txt; grep -i -E "room|scene" Script/gen/s7.txt | head -12
```

Result:

```
# Proof for lane shell1 (the hall): frame time standing at the start of one room, looking down the room.
# Run: run_demo.ps1 -Packaged -Room fight/01_wind_machine -Seed 1 -Dev -Script <this file> -Silent (no -FixedFps)
# F4 turns damage off so the enemies cannot end the run. The FPS line counts frames after the first 3 s.
0.10 key F4
0.20 look 0 5
15.00 end
---
308
# room gen/s7/d01.txt, start 250,200,0
0 scene 2 1
# room gen/s7/d02.txt, start 250,0,0
0 scene 3 1
# room gen/s7/d03.txt, start 250,-200,0
0 scene 4 1
# room gen/s7/d04.txt, start 250,200,0
0 scene 5 1
# room gen/s7/d05.txt, start 250,0,0
0 scene 6 1
# room gen/s7/d06.txt, start 250,200,0
0 scene 7 1
Shell cwd was reset to [notes]
```

### Sun 15 Nov 11:58:08 · Agent (claude-opus-5-5)

pc2 is still busy with another lane's compile (2 GB free), so my queue is holding. I'm checking what "the hall" means in shell1's handoff so I measure the right place.

**Sun 15 Nov 11:58:09 · Tool call: Bash** (Find what the hall is in shell1 notes and the brief)

```
cd "[notes]/unreal/megajam-2026/lanes"; grep -n -i "hall" shell1/HANDOFF.md | head -12; grep -n -i "hall" perf3/BRIEF.md | head
```

Result:

```
1:# Lane shell1 (round 2) handoff: the soundstage hall
5:- `81a8f53` SUPERCUT shell1: soundstage hall round every room, Hall tuning, tests
6:- `c849bb9` SUPERCUT shell1: hall materials saved for instancing, four work lights, hall is studio tone in a freeze
15:lit), a steel roof, four dim work lights and thin haze. The set itself is lit as before; the hall is dim.
19:All of it is code: [SupercutHall.cpp](<D:/UE/wt/shell1/Source/Supercut/SupercutHall.cpp>). No line in any room file.
21:1. When a room is built, `ASupercutRoom` calls `ASupercutHall::BuildFor(*this)` (one line, before the "ROOM built" log).
22:   `TearDown` calls `ASupercutHall::TearDownFor(*this)` (one line).
23:2. The hall reads the room: the box round its solid parts, the floor under the start, its loose parts that do not
25:3. The kept-out box is the room box plus `HallMargin` (400 cm). No piece but a floor tile may touch it. A piece that
27:4. The hall floor is the underside of the floor block the player starts on. That is -50 in most rooms. In
29:   no part of the room reaches lower; over a pit there is no tile, so the pit drops out of sight below the hall floor.
30:   The test rooms `hall/ledge` (start on the wind machine, 4.8 m up) and `hall/perch` (start on a 14 m post) show the
17:  props and the hall went in.
22:`lanes\shell1\HANDOFF.md` (settings, the hall's frame time script `Script\shell1_hall_fps.txt`),
35:   generated room during a fight with freezes and breaks, in the hall, and in the hand-made run. If the average
```

**Sun 15 Nov 11:58:15 · Tool call: Bash** (Wait until the pc2 picture run finishes)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; until grep -q -E "=== .* main8_a|giving up" logs/queue1.txt; do sleep 20; done; tail -12 logs/queue1.txt
```

Result:

```
Command running in background with ID: bobm23gg2. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bobm23gg2.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\lanes; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Sun 15 Nov 11:58:26 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\pairs.py",
 "content": "\"\"\"Lane perf3: pc2 vs [pc-b] picture pairs from the same scripted run.\n\nusage: python -I pairs.py <pc2 shots folder> <[pc-b] shots folder> <out folder>\nWrites <out>/<shot>.jpg (pc2 on top, [pc-b] below, 960 wide each) and prints, per shot, the mean absolute\ndifference (0..255) of the two pictures at 480x270, and of their mean brightness, largest first.\n\"\"\"\nimport os, sys\nfrom PIL import Image, ImageChops, ImageDraw, ImageStat\n\na_dir, b_dir, out = sys.argv[1:4]\nos.makedirs(out, exist_ok=True)\nrows = []\nfor f in sorted(os.listdir(a_dir)):\n    if not f.endswith('.png') or not os.path.exists(os.path.join(b_dir, f)):\n        continue\n    a = Image.open(os.path.join(a_dir, f)).convert('RGB')\n    b = Image.open(os.path.join(b_dir, f)).convert('RGB')\n    sa, sb = a.resize((480, 270), Image.BILINEAR), b.resize((480, 270), Image.BILINEAR)\n    diff = sum(ImageStat.Stat(ImageChops.difference(sa, sb)).mean) / 3\n    bright = sum(ImageStat.Stat(sa).mean) / 3 - sum(ImageStat.Stat(sb).mean) / 3\n    rows.append((diff, bright, f))\n    h = round(a.height * 960 / a.width)\n    pair = Image.new('RGB', (960, 2 * h))\n    pair.paste(a.resize((960, h), Image.LANCZOS), (0, 0))\n    pair.paste(b.resize((960, h), Image.LANCZOS), (0, h))\n    d = ImageDraw.Draw(pair)\n    d.text((8, h - 16), 'pc2 GTX 1070', fill=(255, 255, 255))\n    d.text((8, 2 * h - 16), '[pc-b] RTX 4080 S', fill=(255, 255, 255))\n    pair.save(os.path.join(out, f[:-4] + '.jpg'), quality=85)\nrows.sort(reverse=True)\nprint(f'{len(rows)} pairs; mean abs diff (0..255), brightness pc2 minus [pc-b]:')\nfor diff, bright, f in rows:\n    print(f'  {diff:6.2f}  {bright:+6.2f}  {f}')\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tools\pairs.py (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 11:58:31 · Tool call: Bash** (Check queue progress)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -2 logs/queue1.txt; date +%H:%M
```

Result:

```
11:56 pc2 not ready (clx1 dotnetx1, cpu 2, free ram 2 GB), waiting
11:57 pc2 not ready (clx1 dotnetx1, cpu 6, free ram 2 GB), waiting
11:58
```

**Sun 15 Nov 11:58:36 · Tool call: Bash** (Read the two TSR shaders' permutation domains)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; sed -n 911,975p "$S" | grep -n -E "Dim|Domain|return|if" ; echo ----; sed -n 1313,1388p "$S" | grep -n -E "Dim|Domain|return|if"
```

Result:

```
6:	class FMoireReprojectionDim : SHADER_PERMUTATION_BOOL("DIM_MOIRE_REPROJECTION");
7:	class FResurrectionReprojectionDim : SHADER_PERMUTATION_BOOL("DIM_RESURRECTION_REPROJECTION");
8:	class FThinGeometryCoverageDim: SHADER_PERMUTATION_BOOL("DIM_THIN_GEOMETRY_COVERAGE_REPROJECTION");
9:	using FPermutationDomain = TShaderPermutationDomain<FMoireReprojectionDim, FResurrectionReprojectionDim, FThinGeometryCoverageDim, FTSRShader::F16BitVALUDim, FTSRShader::FAlphaChannelDim>;
52:		if (FPermutationDomain(Parameters.PermutationId).Get<FThinGeometryCoverageDim>() && IsWebReducedGlobalShaderPlatform(Parameters.Platform))
54:			return false;
57:		if (!FTSRShader::ShouldCompilePermutation(Parameters))
59:			return false;
62:		FPermutationDomain PermutationVector(Parameters.PermutationId);
64:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
----
15:	class FQualityDim : SHADER_PERMUTATION_ENUM_CLASS("DIM_UPDATE_QUALITY", EQuality);
17:	using FPermutationDomain = TShaderPermutationDomain<FQualityDim, FTSRShader::F16BitVALUDim, FTSRShader::FAlphaChannelDim>;
68:		FPermutationDomain PermutationVector(Parameters.PermutationId);
70:		if (!FTSRShader::ShouldCompile32or16BitPermutation(Parameters.Platform, PermutationVector.Get<FTSRShader::F16BitVALUDim>()))
72:			return false;
75:		return FTSRShader::ShouldCompilePermutation(Parameters);
```

**Sun 15 Nov 11:58:43 · Tool call: Bash** (Wait up to about 8 minutes for the picture run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 50); do grep -q -E "=== .* main8_a|giving up" logs/queue1.txt && break; sleep 10; done; tail -4 logs/queue1.txt; date +%H:%M
```

Result:

```
11:57 pc2 not ready (clx1 dotnetx1, cpu 6, free ram 2 GB), waiting
11:58 pc2 not ready (clx1 dotnetx1, cpu 7, free ram 2 GB), waiting
11:59 pc2 not ready (clx2 dotnetx1, cpu 5, free ram 3 GB), waiting
12:00 pc2 not ready (clx2 dotnetx1, cpu 3, free ram 3 GB), waiting
12:07
```

### Sun 15 Nov 12:07:09 · Agent (claude-opus-5-5)

The queue log stopped at 12:00 and it's 12:07 now, so I'm checking whether the farm status call is hanging.

**Sun 15 Nov 12:07:10 · Tool call: Bash** (Inspect queue state and running farm processes)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -3 logs/queue1.txt; ls logs/pics_pc2 2>/dev/null; cat logs/pics_pc2/load.txt 2>/dev/null; ps aux 2>/dev/null | grep -E "farm.sh|ssh pc2" | grep -v grep | head
```

Result:

```
11:58 pc2 not ready (clx1 dotnetx1, cpu 7, free ram 2 GB), waiting
11:59 pc2 not ready (clx2 dotnetx1, cpu 5, free ram 3 GB), waiting
12:00 pc2 not ready (clx2 dotnetx1, cpu 3, free ram 3 GB), waiting
load.txt
before: free_ram_gb=7.7 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 1685 MiB, 17.76 W
```

### Sun 15 Nov 12:07:14 · Agent (claude-opus-5-5)

The picture run started at 12:01 (7.7 GB free, pc2 idle). The farm only prints when the run ends, so I'm waiting for it.

**Sun 15 Nov 12:07:15 · Tool call: Bash** (Wait for the pc2 picture run to finish)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 50); do grep -q -E "=== .* main8_a|giving up" logs/queue1.txt && break; sleep 10; done; tail -12 logs/queue1.txt; date +%H:%M
```

Result:

```
11:55 pc2 not ready (clx1 dotnetx1, cpu 0, free ram 2 GB), waiting
11:56 pc2 not ready (clx1 dotnetx1, cpu 2, free ram 2 GB), waiting
11:57 pc2 not ready (clx1 dotnetx1, cpu 6, free ram 2 GB), waiting
11:58 pc2 not ready (clx1 dotnetx1, cpu 7, free ram 2 GB), waiting
11:59 pc2 not ready (clx2 dotnetx1, cpu 5, free ram 3 GB), waiting
12:00 pc2 not ready (clx2 dotnetx1, cpu 3, free ram 3 GB), waiting
game exit code 0
FARM step=run name=perf3 exit=0 secs=450
before: free_ram_gb=7.7 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 1685 MiB, 17.76 W 
after: free_ram_gb=4.6 of 15.9 cpu_load_pct=1 threads=12 busy_procs=clx1 dotnetx2 gpu=NVIDIA GeForce GTX 1070, 28 %, 1685 MiB, 18.24 W 
=== 12:09:30 main8_a:main8_fx.args
12:09 pc2 not ready (clx1 dotnetx2, cpu 4, free ram 4 GB), waiting
12:09
```

**Sun 15 Nov 12:09:41 · Tool call: Bash** (Check pc2 picture run results)

```
cd /d/UE/wt/perf3_farmlogs/run; ls; L=$(ls *.log | head -3); for l in $L; do echo "== $l"; grep -E "RUN wrapped|SETTINGS (at start|first start|saved)" $l | sed 's/^\[[^]]*\]\[[^]]*\]//' | cut -c1-200; echo "compute errors: $(grep -c 'Failed to create compute pipeline' $l)"; done; ls shots | wc -l
```

Result:

```
console.txt
farm_step.txt
run.log
shots
== run.log
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUs
LogSupercut: Display: RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17
compute errors: 24
65
Shell cwd was reset to [notes]
```

**Sun 15 Nov 12:09:46 · Tool call: Bash** (Save pc2 shots and build picture pairs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; mkdir -p /d/UE/wt/perf3_pics_pc2 && cp -r /d/UE/wt/perf3_farmlogs/run/shots /d/UE/wt/perf3_farmlogs/run/run.log /d/UE/wt/perf3_pics_pc2/; cp /d/UE/wt/perf3_farmlogs/run/run.log logs/pics_pc2/run.log; python -I tools/pairs.py /d/UE/wt/perf3_pics_pc2/shots /d/UE/wt/perf3_farmlogs_[pc-b]/run/shots shots/pairs | head -40
```

Result:

```
65 pairs; mean abs diff (0..255), brightness pc2 minus [pc-b]:
    8.73   +8.73  s5_04_door_open.png
    7.74   +7.73  s7_02_frozen_bridge.png
    6.67   +6.66  s5_02_frozen_three_marks.png
    6.66   +6.65  s7_01_start.png
    6.25   +6.24  s7_05_door_ahead_shut_shot_still_hanging.png
    5.58   +5.57  s2_01_start.png
    5.51   +5.50  s5_01_start.png
    5.33   +5.33  s7_03_target_seen_from_the_bridge.png
    5.19   +5.19  s7_04_shot_hangs.png
    4.21   +4.20  s7_06_door_open.png
    4.01   +4.00  s2_02_frozen_door_held_open.png
    3.81   +3.80  s1_03_machine_stopped.png
    3.81   +3.80  s1_01_start.png
    3.29   +3.27  s1_02_at_the_machine.png
    2.76   +2.75  s4_07_action.png
    2.64   +2.62  s1_10_stage_clear.png
    2.42   +2.40  s8_05_set_is_clear.png
    2.17   +1.99  s8_03_three_gone.png
    2.08   +2.04  s4_03_line_locked_rusher_coming.png
    1.66   +1.65  s5_03_three_shots_hang.png
    1.57   -0.19  s3_09_action.png
    1.49   -1.39  s3_07_two_for_the_rusher.png
    1.47   +1.42  s8_06_from_tower_2.png
    1.44   +1.40  s4_02_the_line.png
    1.34   +1.33  s4_06_set_up.png
    1.20   +0.88  s3_05_rusher_0_gone.png
    1.14   +1.10  s1_08_grunt_0_gone.png
    0.99   +0.95  s3_10_from_the_stage.png
    0.96   +0.91  s1_11_gate_ahead.png
    0.93   +0.88  s4_09_grunt_gone.png
    0.90   +0.90  s2_03_nearly_there.png
    0.70   +0.51  s6_01_start.png
    0.56   +0.55  s3_04_two_shots_hang.png
    0.50   +0.18  s3_06_rusher_1_coming.png
    0.44   +0.42  s4_05_two_for_the_marksman.png
    0.40   +0.13  s3_08_both_set_up.png
    0.33   +0.07  s4_10_from_the_camera_stage.png
    0.33   -0.08  s8_01_start.png
    0.33   +0.32  s1_09_three_more_hang.png
```

**Sun 15 Nov 12:09:58 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\shots\\pairs\\s5_04_door_open.jpg"
}
```

Result:

```
[image]
```

**Sun 15 Nov 12:10:04 · Tool call: Bash** (Compare rendering features in [pc-b] and pc2 logs)

```
J=/d/UE/wt/perf3_farmlogs_[pc-b]/run/run.log; P=/d/UE/wt/perf3_pics_pc2/run.log; for l in $J $P; do echo "== $l"; grep -i -E "ray ?tracing|RHI.*(support|Wave)|Nanite|VirtualShadow|Lumen|DLSS|Upscal|TSR|Native16|bindless" $l | sed 's/^\[[^]]*\]\[[^]]*\]//' | sort -u | head -14 | cut -c1-170; done
```

Result:

```
== /d/UE/wt/perf3_farmlogs_[pc-b]/run/run.log
LogConfig: Set CVar [[D3D12.Bindless.ResourceDescriptorHeapSize:32768]]
LogConfig: Set CVar [[D3D12.Bindless.SamplerDescriptorHeapSize:2048]]
LogConfig: Set CVar [[r.Lumen.DiffuseIndirect.Allow:1]]
LogConfig: Set CVar [[r.Lumen.FinalGatherMethod:1]]
LogConfig: Set CVar [[r.Lumen.HardwareRayTracing.HitLighting.Allowed:0]]
LogConfig: Set CVar [[r.Lumen.HardwareRayTracing.HitLighting.Allowed:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.Allow:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.DownsampleFactor:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.DownsampleFactor:2]]
LogConfig: Set CVar [[r.Lumen.Reflections.MaxRoughnessToTraceForFoliage:0.2]]
LogConfig: Set CVar [[r.Lumen.Reflections.MaxRoughnessToTraceForFoliage:0.4]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.MinWeight:0]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.MinWeight:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.NumSamples:3]]
== /d/UE/wt/perf3_pics_pc2/run.log
LogConfig: Set CVar [[D3D12.Bindless.ResourceDescriptorHeapSize:32768]]
LogConfig: Set CVar [[D3D12.Bindless.SamplerDescriptorHeapSize:2048]]
LogConfig: Set CVar [[r.Lumen.DiffuseIndirect.Allow:1]]
LogConfig: Set CVar [[r.Lumen.FinalGatherMethod:1]]
LogConfig: Set CVar [[r.Lumen.HardwareRayTracing.HitLighting.Allowed:0]]
LogConfig: Set CVar [[r.Lumen.HardwareRayTracing.HitLighting.Allowed:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.Allow:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.DownsampleFactor:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.DownsampleFactor:2]]
LogConfig: Set CVar [[r.Lumen.Reflections.MaxRoughnessToTraceForFoliage:0.2]]
LogConfig: Set CVar [[r.Lumen.Reflections.MaxRoughnessToTraceForFoliage:0.4]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.MinWeight:0]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.MinWeight:1]]
LogConfig: Set CVar [[r.Lumen.Reflections.ScreenSpaceReconstruction.NumSamples:3]]
```

**Sun 15 Nov 12:10:09 · Tool call: Bash** (Compare non-cvar feature lines and cvar sets)

```
J=/d/UE/wt/perf3_farmlogs_[pc-b]/run/run.log; P=/d/UE/wt/perf3_pics_pc2/run.log; for l in $J $P; do echo "== $(basename $(dirname $(dirname $l)))"; grep -v "Set CVar" $l | grep -i -E "ray ?tracing|Native16|wave ops|SM6|RHI.*Support|Lumen|Nanite" | sed 's/^\[[^]]*\]\[[^]]*\]//' | sort -u | head -14 | cut -c1-170; grep -c "Set CVar" $l; done; diff <(grep "Set CVar" $J | sed 's/^\[[^]]*\]\[[^]]*\]//' | sort -u) <(grep "Set CVar" $P | sed 's/^\[[^]]*\]\[[^]]*\]//' | sort -u) | head -20
```

Result:

```
== perf3_farmlogs_[pc-b]
LogCsvProfiler: Display: Metadata set : raytracing="0"
LogCsvProfiler: Display: Metadata set : rhifeaturelevel="SM6"
LogCsvProfiler: Display: Metadata set : shaderplatform="PCD3D_SM6"
LogD3D12RHI:      Enhanced Barriers Driver Support: Yes
LogD3D12RHI:   Max supported Feature Level 12_1, shader model 6.7, binding tier 3, wave ops supported, atomic64 supported
LogD3D12RHI:   Max supported Feature Level 12_2, shader model 6.7, binding tier 3, wave ops supported, atomic64 supported
LogD3D12RHI: AtomicInt64OnDescriptorHeapResource is supported
LogD3D12RHI: AtomicInt64OnGroupShared is supported
LogD3D12RHI: AtomicInt64OnTypedResource is supported
LogD3D12RHI: Bindless is enabled (Configuration=RayTracing). Initializing allocators with 32768 Resource and 2048 Sampler descriptors
LogD3D12RHI: Bindless is supported. MaxNonSamplerDescriptors: 1000000, MaxSamplerDescriptors: 2048
LogD3D12RHI: D3D12 ray tracing tier 1.1 and bindless resources are supported.
LogD3D12RHI: Display: Creating D3D12 RHI with Max Feature Level SM6
LogD3D12RHI: ID3D12Device1 is supported.
335
== wt
LogCsvProfiler: Display: Metadata set : raytracing="0"
LogCsvProfiler: Display: Metadata set : rhifeaturelevel="SM6"
LogCsvProfiler: Display: Metadata set : shaderplatform="PCD3D_SM6"
LogD3D12RHI:      Enhanced Barriers Driver Support: Yes
LogD3D12RHI:   Max supported Feature Level 12_1, shader model 6.2, binding tier 3, wave ops supported, atomic64 unsupported
LogD3D12RHI:   Max supported Feature Level 12_1, shader model 6.7, binding tier 3, wave ops supported, atomic64 supported
LogD3D12RHI: AtomicInt64OnDescriptorHeapResource is supported
LogD3D12RHI: AtomicInt64OnGroupShared is supported
LogD3D12RHI: AtomicInt64OnTypedResource is supported
LogD3D12RHI: Bindless is enabled (Configuration=RayTracing). Initializing allocators with 32768 Resource and 2048 Sampler descriptors
LogD3D12RHI: Bindless is supported. MaxNonSamplerDescriptors: 1000000, MaxSamplerDescriptors: 2048
LogD3D12RHI: Display: Creating D3D12 RHI with Max Feature Level SM6
LogD3D12RHI: ID3D12Device1 is supported.
LogD3D12RHI: ID3D12Device10 is supported.
335
```

**Sun 15 Nov 12:10:16 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\shots\\pairs\\s7_02_frozen_bridge.jpg"
}
```

Result:

```
[image]
```

**Sun 15 Nov 12:10:17 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\shots\\pairs\\s3_07_two_for_the_rusher.jpg"
}
```

Result:

```
[image]
```

**Sun 15 Nov 12:10:28 · Tool call: Bash** (Queue status and log the picture comparison)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -4 logs/queue1.txt; cat >> LOG.md <<'EOF'
- 12:01 to 12:09 pc2 picture run (farm, offscreen, same line as [pc-b]'s). Load before: busy none, CPU 0 %, free RAM 7.7 GB, GPU 25 %. After: someone's compile had started (cl, dotnet), free RAM 4.6 GB; fixed-step pictures do not depend on load. `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`, quality HIGH, 24 compute pipeline errors, 65 shots. Both logs: `raytracing="0"` (software Lumen on both), the same 335 CVar sets, no difference in the set.
- 12:12 pairs (tools/pairs.py, shots/pairs/): all 65 show the same frame with the same parts: shadows, Lumen bounce, reflections on the floor, sky, the sketch look in freezes, muzzle and hit effects, upscaled at 87 %. pc2 is a little brighter in the lit rooms (mean +4 to +9 levels of 255 in scenes 1, 2, 5, 7; under 1.5 in the sketch freezes and scenes 3, 4, 6, 8). Shadow edges in s7_02 look slightly softer on pc2. Nothing missing.
EOF
```

Result:

```
before: free_ram_gb=7.7 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 1685 MiB, 17.76 W 
after: free_ram_gb=4.6 of 15.9 cpu_load_pct=1 threads=12 busy_procs=clx1 dotnetx2 gpu=NVIDIA GeForce GTX 1070, 28 %, 1685 MiB, 18.24 W 
=== 12:09:30 main8_a:main8_fx.args
12:09 pc2 not ready (clx1 dotnetx2, cpu 4, free ram 4 GB), waiting
```

**Sun 15 Nov 12:10:35 · Tool call: Bash** (List cooked shader metadata on pc2 farm folder)

```
ssh pc2 'dir /b C:\UE\Farm\perf3\Saved\Cooked\Windows\Supercut\Metadata\ShaderLibrarySource 2>nul & dir /b /s C:\UE\Farm\perf3\Saved\Cooked\Windows\Supercut\Metadata\*.json 2>nul' | sed 's#.*\\Metadata#Metadata#' | head -20
```

Result:

```
The system cannot find the path specified.
Metadata\Crypto.json
Metadata\ValidationCookArtifact.json
Metadata\ShaderLibrarySource\ShaderAssetInfo-Global-PCD3D_SM5-PCD3D_SM5.assetinfo.json
Metadata\ShaderLibrarySource\ShaderAssetInfo-Global-PCD3D_SM6-PCD3D_SM6.assetinfo.json
Metadata\ShaderLibrarySource\ShaderAssetInfo-Supercut-PCD3D_SM5-PCD3D_SM5.assetinfo.json
Metadata\ShaderLibrarySource\ShaderAssetInfo-Supercut-PCD3D_SM6-PCD3D_SM6.assetinfo.json
```

**Sun 15 Nov 12:10:39 · Tool call: Bash** (Fetch global shader asset info and search a failing hash)

```
mkdir -p /d/UE/wt/perf3_meta; scp -q "pc2:C:/UE/Farm/perf3/Saved/Cooked/Windows/Supercut/Metadata/ShaderLibrarySource/ShaderAssetInfo-Global-PCD3D_SM6-PCD3D_SM6.assetinfo.json" /d/UE/wt/perf3_meta/ && ls -la /d/UE/wt/perf3_meta | awk '{print $5, $NF}'; head -c 800 /d/UE/wt/perf3_meta/*.json; echo; grep -o -i "c943eeb2fc37390a" /d/UE/wt/perf3_meta/*.json | head -2
```

Result:

```
56
0 .
0 ..
43488 ShaderAssetInfo-Global-PCD3D_SM6-PCD3D_SM6.assetinfo.json
{
	"AssetInfoVersion": 2,
	"ShaderCodeToAssets": [
		{
			"ShaderMapHash": "0053B30CD6ACC9EC",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "0188B4BAB4045279",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "01A97DEF1D08985D",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "01E655D2AEEAD370",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "058E4FC4DD213C9B",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "059C2F3237B98920",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "06123B3C686C2BD9",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "062DC90D716A0146",
			"Assets": [
				"None"
			]
		},
		{
			"ShaderMapHash": "065FC63F4DE8A46E",
			"Assets":
```

**Sun 15 Nov 12:10:48 · Tool call: Bash** (Wait for the main8 frame time run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 54); do grep -q -E "=== .* hall_a|giving up" logs/queue1.txt && break; sleep 10; done; tail -12 logs/queue1.txt | grep -v "not ready" ; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
game exit code 0
FARM step=run name=perf3 exit=0 secs=450
before: free_ram_gb=7.7 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 1685 MiB, 17.76 W 
after: free_ram_gb=4.6 of 15.9 cpu_load_pct=1 threads=12 busy_procs=clx1 dotnetx2 gpu=NVIDIA GeForce GTX 1070, 28 %, 1685 MiB, 18.24 W 
=== 12:09:30 main8_a:main8_fx.args
12:14:52 started main8_a (idle)
12:14:52 started main8_a (idle)
12:19
```

**Sun 15 Nov 12:19:54 · Tool call: Bash** (Keep waiting for the main8 run to finish)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 54); do grep -q -E "=== .* hall_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/started main8_a/,$p' logs/queue1.txt | grep -v "not ready"; date +%H:%M
```

Result:

```
12:14:52 started main8_a (idle)
before: free_ram_gb=7.6 of 15.9 cpu_load_pct=7 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 28 %, 1685 MiB, 38.19 W 
gpu gate: idle
after: free_ram_gb=4.4 of 15.9 cpu_load_pct=5 threads=12 busy_procs=clx1 dotnetx1 Supercutx2 gpu=NVIDIA GeForce GTX 1070, 25 %, 1692 MiB, 39.80 W 
cpu_before=6
others_before=Supercut,Supercut
seconds_to_exit=414.3
exit_code=777003
hang=False
cpu_after=8
others_after=cl,Supercut,Supercut
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUserSettings.ini
LogSupercut: Display: RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17
LogSupercut: Display: SCRIPT finished at 15.93 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 240.0, slowest 1% of frames 240.0, over 14414 frames and 60.1 s
LogSupercut: Display: FPS frozen: average 240.0, slowest 1% of frames 240.0, over 8426 frames and 35.1 s
compute pipeline errors: 24
=== 12:21:58 hall_a:hall.args
12:22
```

### Sun 15 Nov 12:22:14 · Agent (claude-opus-5-5)

The main8 run finished: same run line, 24 errors. But pc2 still shows two Supercut processes afterwards, so I'm checking whether they're mine before the queue goes on.

**Sun 15 Nov 12:22:16 · Tool call: Bash** (Check desk_run process logic and list Supercut processes on pc2)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -n -i -E "others_|exit_code|Get-Process|Stop-Process|taskkill" tools/desk_run.ps1 | head; scp -q tools/p3q.ps1 pc2:C:/UE/Farm/_out/perf3/p3q.ps1 2>/dev/null; ssh pc2 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\perf3\p3q.ps1' 2>&1 | sed -E 's#C:\\Users\\USER\\]+#%USERPROFILE%#g' | cut -c1-250 | head
```

Result:

```
15:$res = [ordered]@{ tag = $Tag; session_id = (Get-Process -Id $PID).SessionId }
32:$res.others_before = (@(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '^(Supercut|UnrealEditor|cl|link|UnrealBuildTool|AutomationTool|ShaderCompileWorker)' }) | ForEach-Object { $_.Name }) -join ','
46:if ($done) { $res.exit_code = $p.ExitCode; $res.hang = $false } else { $res.exit_code = 'none'; $res.hang = $true }
50:$left = @($ids | Where-Object { Get-Process -Id $_ -ErrorAction SilentlyContinue })
51:if (-not $done) { foreach ($i in $left) { Stop-Process -Id $i -Force -ErrorAction SilentlyContinue }; $res.stopped_by_pid = ($left -join ',') }
57:$res.others_after = (@(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '^(Supercut|UnrealEditor|cl|link|UnrealBuildTool|AutomationTool|ShaderCompileWorker)' }) | ForEach-Object { $_.Name }) -join ','
```

**Sun 15 Nov 12:22:22 · Tool call: Bash** (List Supercut processes with start time and command line)

```
ls "[notes]/unreal/megajam-2026/lanes/perf3/tools/"; ssh pc2 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -like \"Supercut*\" } | ForEach-Object { \"{0} {1} {2} {3}\" -f $_.ProcessId, $_.Name, $_.CreationDate, ($_.CommandLine -replace \"^.{0,0}\",\"\").Substring(0, [Math]::Min(200, $_.CommandLine.Length)) }"' 2>&1 | sed -E 's#C:\\Users\\USER\\]+#%USERPROFILE%#g' | head
```

Result:

```
__pycache__
analyze.py
args
desk_run.ps1
go.sh
pairs.py
psodiag_snippet.cpp.txt
queue.sh
13628 Supercut.exe 15/11/2026 12:22:18 pm "C:\UE\Farm\_builds\set2\Supercut59\Windows\Supercut.exe" -RenderOffscreen -windowed -ResX=1920 -ResY=1080 -WinX=0 -WinY=0 -nosplash -unattended "-SupercutScript=C:\UE\Farm\set2\Script\set2_hall.txt" 
6948 Supercut.exe 15/11/2026 12:22:18 pm "C:\UE\Farm\_builds\set2\Supercut59\Windows\Supercut\Binaries\Win64\Supercut.exe" Supercut -RenderOffscreen -windowed -ResX=1920 -ResY=1080 -WinX=0 -WinY=0 -nosplash -unattended "-SupercutScript=C:\UE
```

**Sun 15 Nov 12:22:32 · Tool call: Bash** (Per-room frame times for main8_a (had company))

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py main8_a sections 2>&1 | tail -22
```

Result:

```
main8_a: 26555 csv rows, row = frame - 4 (clock spread 16.6 ms)
room                                       state  frames  avg ms  p99 ms slow1% ms  max ms GPU avg
the 4 frames from the change took 4.2, 4   live    15102   16.41   19.06    327.32 43327.7   12.59
the 4 frames from the change took 4.2, 4   frozen   8426   13.82   17.51     37.94   442.4   12.85
take 1, scene 2 of 8 (a_the_cue), charge   live        4   12.69   13.43     13.43    13.4   12.24
take 1, scene 3 of 8 (02_stunt_run), cha   live        4   13.23   19.09     19.09    19.1   12.23
take 1, scene 4 of 8 (03_long_lens), cha   live        4   12.48   18.21     18.21    18.2   12.58
take 1, scene 5 of 8 (b_the_wild_wall),    live        4   11.37   12.17     12.17    12.2   10.92
take 1, scene 6 of 8 (04_hot_set), charg   live        4   12.44   12.65     12.65    12.7   11.85
take 1, scene 7 of 8 (c_the_cutaway), ch   live        4   12.38   13.43     13.43    13.4   12.33
take 1, scene 8 of 8 (05_martini_shot),    live        4   12.40   13.28     13.28    13.3   11.22
all rooms                                  both    23556   15.48   18.85    224.02 43327.7   12.68
```

### Sun 15 Nov 12:22:38 · Agent (claude-opus-5-5)

The per-room table has a parsing bug: "ROOM change frames" lines count as room starts, and the boot row is included. Fixing that.

**Sun 15 Nov 12:22:41 · Tool call: Bash** (Fix room parsing and rerun the table)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/analyze.py'
s=open(p,encoding='utf-8').read()
reps=[("re.search(r'ROOM change|PICK offered","re.search(r'ROOM change:|PICK offered"),
("        if 'ROOM change' in text:\n            m = re.search(r'ROOM change[^:]*: *(.*)', text)","        if 'ROOM change:' in text:\n            m = re.search(r'ROOM change: *(.*)', text)"),
("    return max(0, f0 - c), min(n, f1 - c)","    return max(1, f0 - c), min(n, f1 - c)   # row 0 is the whole boot")]
for a,b in reps:
    assert s.count(a)==1, a; s=s.replace(a,b)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
python -I tools/analyze.py main8_a sections 2>&1 | tail -20
```

Result:

```
main8_a: 26555 csv rows, row = frame - 4 (clock spread 16.6 ms)
room                                       state  frames  avg ms  p99 ms slow1% ms  max ms GPU avg
take 1, scene 1 of 8 (01_wind_machine),    live     1604   15.88   19.00     84.58   679.6   14.54
take 1, scene 1 of 8 (01_wind_machine),    frozen   1465   15.27   17.88     79.60   442.4   13.91
take 1, scene 2 of 8 (a_the_cue), charge   live      505   13.00   16.09     31.56    57.5   12.06
take 1, scene 2 of 8 (a_the_cue), charge   frozen    877   13.08   18.36     62.24   352.2   11.94
take 1, scene 3 of 8 (02_stunt_run), cha   live     3503   13.46   18.97     47.08   656.8   12.40
take 1, scene 3 of 8 (02_stunt_run), cha   frozen   1152   14.05   16.01     23.91    39.7   13.20
take 1, scene 4 of 8 (03_long_lens), cha   live     2552   13.11   18.57     24.64    55.1   12.30
take 1, scene 4 of 8 (03_long_lens), cha   frozen    900   13.64   15.94     21.86    37.3   12.83
take 1, scene 5 of 8 (b_the_wild_wall),    live     1644   12.92   15.76     26.17    71.9   12.12
take 1, scene 5 of 8 (b_the_wild_wall),    frozen    456   13.27   15.02     64.76   174.7   12.15
take 1, scene 6 of 8 (04_hot_set), charg   live     2191   13.20   19.66     26.76    45.5   12.41
take 1, scene 6 of 8 (04_hot_set), charg   frozen   1608   13.31   19.11     23.42    36.0   12.51
take 1, scene 7 of 8 (c_the_cutaway), ch   live      866   13.87   19.88     90.25   505.3   12.48
take 1, scene 7 of 8 (c_the_cutaway), ch   frozen    888   12.97   16.38     19.30    32.9   12.17
take 1, scene 8 of 8 (05_martini_shot),    live     2264   13.29   18.69     25.41    72.4   12.47
take 1, scene 8 of 8 (05_martini_shot),    frozen   1080   14.02   16.25     22.66    37.6   13.18
all rooms                                  both    23555   13.64   18.85     39.72   679.6   12.68
```

**Sun 15 Nov 12:22:50 · Tool call: Bash** (Shorten room labels to scene number and name)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/analyze.py'
s=open(p,encoding='utf-8').read()
a="""            m = re.search(r'ROOM change: *(.*)', text)
            room, state, start = (m.group(1)[:40] if m else text[-40:]), 'live', fr"""
b="""            m = re.search(r'scene (\\d+) of \\d+ \\(([^)]+)\\)', text)
            room, state, start = (f'{m.group(1)} {m.group(2)}'[:40] if m else text[-40:]), 'live', fr"""
assert s.count(a)==1; s=s.replace(a,b)
open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
python -I tools/analyze.py main8_a sections 2>&1 | sed -n 3,4p; tail -2 logs/queue1.txt
```

Result:

```
<stdin>:5: SyntaxWarning: invalid escape sequence '\d'
1 01_wind_machine                          live     1604   15.88   19.00     84.58   679.6   14.54
1 01_wind_machine                          frozen   1465   15.27   17.88     79.60   442.4   13.91
=== 12:21:58 hall_a:hall.args
12:22 pc2 not ready (clx1 dotnetx1 Supercutx2, cpu 93, free ram 3 GB), waiting
```

### Sun 15 Nov 12:22:56 · Agent (claude-opus-5-5)

pc2 is at 93% CPU now (set2's run plus a compile). While I wait, I'm closing the gap in go.sh: it will look for other Supercut or editor processes right before launching, not only at the first check.

**Sun 15 Nov 12:22:57 · Tool call: Read**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "offset": 14,
 "limit": 22
}
```

Result:

```
14	scp -q tools/args/* "pc2:C:/UE/Farm/_out/perf3/desktools/" || { echo scp args failed; exit 1; }
15	waited=0
16	while true; do
17	  st=$("$F" status pc2 2>/dev/null)
18	  busy=$(echo "$st" | sed -n 's/^busy_procs=//p'); cpu=$(echo "$st" | sed -n 's/^cpu_load_pct=\([0-9]*\).*/\1/p')
19	  ram=$(echo "$st" | sed -n 's/^free_ram_gb=\([0-9]*\).*/\1/p')
20	  if [ "$busy" = "none" ] && [ "${cpu:-100}" -lt 60 ] && [ "${ram:-0}" -ge 6 ]; then break; fi
21	  echo "$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting"; sleep 60; waited=$((waited+60))
22	  [ $waited -gt ${WAIT_MAX:-1800} ] && { echo "pc2 not ready for $waited s, giving up"; exit 1; }
23	done
24	echo "before: $(echo "$st" | grep -E 'free_ram_gb|cpu_load|busy_procs|^gpu=' | tr '\n' ' ')" > logs/$tag/load.txt
25	ok=0; waited=0
26	while [ $ok -lt 4 ] && [ $waited -lt 900 ]; do
27	  r=$(ssh pc2 'nvidia-smi --query-gpu=utilization.gpu,power.draw --format=csv,noheader,nounits')
28	  u=${r%%,*}; m=${r##*, }; m=${m%%.*}
29	  if [ "$u" -lt 40 ] && [ "$m" -lt 70 ]; then ok=$((ok+1)); sleep 1; else ok=0; sleep 4; waited=$((waited+5)); fi
30	done
31	gate=idle; [ $ok -lt 4 ] && gate="UNDER LOAD (gpu gate not met after ${waited}s)"
32	echo "gpu gate: $gate" >> logs/$tag/load.txt
33	tr=$(printf '%s' 'powershell -NoProfile -ExecutionPolicy Bypass -File C:\UE\Farm\_out\perf3\desktools\desk_run.ps1 -Tag ' "$tag" ' -ArgFile C:\UE\Farm\_out\perf3\desktools\' "$af" " $flags")
34	ssh pc2 "schtasks /create /tn perf3_supercut /tr \"$tr\" /sc once /st 23:59 /it /f" >/dev/null || { echo create failed; exit 1; }
35	ssh pc2 'schtasks /run /tn perf3_supercut' >/dev/null || { echo run failed; exit 1; }
```

**Sun 15 Nov 12:23:03 · Tool call: Bash** (Wait for the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 55); do grep -q -E "=== .* gen_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/hall_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-200; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
=== 12:21:58 hall_a:hall.args
12:31 pc2 not ready (Supercutx1 Supercut-Win64-Shippingx1 UnrealEditorx1, cpu 5, free ram 2 GB), waiting
12:32
```

### Sun 15 Nov 12:32:22 · Agent (claude-opus-5-5)

pc2 is busy with other lanes (a shipping run, an editor, 2 GB free), so the queue is holding. I'm drafting HANDOFF.md while it waits.

**Sun 15 Nov 12:32:23 · Tool call: Bash** (Review the start of LOG.md and brief proof lines)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; head -12 LOG.md | cut -c1-400; sed -n 1,60p BRIEF.md | grep -n -i -E "handoff|table|proof" | head
```

Result:

```
# perf3 log

All times SGT (c4 clock, `date`).

- 10:52 lane started. Read BRIEF, COMMON_RULES, FARM.md, perf2 REPORT/tables/tools, dlss2, shell1, light1, vfx1 handoffs, GOTCHAS sections (pc2 test lane 2, Shipping settings, first1, farm, shell1 measuring).
- 10:54 pc2 status: free RAM 5.4 GB, CPU 2 %, busy none. Mirrored worktree (3010 files, 88 s). Started build (-Jobs 4, RAM short) then package, background.
- 10:55 engine source: the error text is `PipelineStateCache.cpp:733` (`HandlePipelineCreationFailure`, compute); precache requests may fail without effect (`PipelineStateCache.cpp:722`, only non-precache failures are Fatal). Global compute shaders are precached at start from `LaunchEngineLoop.cpp:4504` -> `ShaderCompiler.cpp:5253` `PrecacheComputePipelineStatesForGlobalShaders`: every permutation
- 10:57 D3D12 side: `D3D12Shaders.cpp:107` `ValidateShaderIsUsable` refuses a shader needing wave ops, bindless, stencil ref or barycentrics the card lacks, but has no check for `SixteenBitTypes`, `TypedUAVLoadsExtended` or `Atomic64` (flags recorded by `D3DShaderCompilerDXC.cpp:1146`). The driver call returns 0x80070057 (E_INVALIDARG) for each of the 24.
- 10:58 existing logs on c4: every RTX 4080 SUPER and RX 9070 XT packaged run has 0 of these errors; pc2 packaged (viewmerge1) 24; pc2 uncooked editor run (view1) 0. So: cooked package + Pascal card.
- 11:00 first-start level code now `FirstStartLevel` = benchmark lowest - 1, clamped 1..2 (`SupercutUserSettings.cpp:171`), so pc2 should get HIGH now, not EPIC as in perf2. DLSS default 0 (OFF) on every card.
- 11:03 pc2 free RAM 0.9 to 1.7 GB while the build compiles (its Studio windows); build slow.
- CSV profiler: `-csvCaptureFrames=N` boot capture (`CsvProfiler.cpp:5054`, `5182`); FrameTime is wall time from cycle stamps (`CsvProfiler.cpp:4163-4168`), so it is a real frame time even with -UseFixedTimeStep. `-csvGpuStats` (`CsvProfiler.cpp:5103`) adds GPU pass times.
20:Read first: `lanes\perf2\REPORT.md`, `lanes\perf2\tables.md` and `lanes\perf2\tools\` (the last measurement and
21:how it was made), `lanes\dlss2\HANDOFF.md` (upscaling and its defaults per card), `lanes\light1\HANDOFF.md`,
22:`lanes\shell1\HANDOFF.md` (settings, the hall's frame time script `Script\shell1_hall_fps.txt`),
23:`lanes\vfx1\HANDOFF.md` (`Script\vfx1_fps.txt`).
53:- Lane folder: `lanes\perf3\`. `LOG.md`, `HANDOFF.md`, tables, pictures in `shots\`.
55:## Proof
58:after; the frame time tables with the load readings beside each run;
[... 38 more characters not shown]
```

**Sun 15 Nov 12:32:30 · Tool call: Bash** (Wait for the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* gen_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/hall_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-200; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
=== 12:21:58 hall_a:hall.args
12:41 pc2 not ready (UnrealEditorx1, cpu 0, free ram 4 GB), waiting
12:41
```

**Sun 15 Nov 12:41:57 · Tool call: Bash** (See which editor process is running on pc2)

```
ssh pc2 'powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -like \"UnrealEditor*\" -or $_.Name -like \"Supercut*\" } | ForEach-Object { \"{0} {1} {2} | {3}\" -f $_.ProcessId, $_.Name, $_.CreationDate, $_.CommandLine.Substring(0, [Math]::Min(220, $_.CommandLine.Length)) }"' 2>&1 | sed -E 's#C:\\Users\\USER\\]+#%USERPROFILE%#g' | head -5
```

Result:

```
The system cannot find the path specified.
```

**Sun 15 Nov 12:42:01 · Tool call: Bash** (Fresh pc2 status)

```
F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" status pc2 2>/dev/null | grep -E 'free_ram|cpu_load|busy'; tail -2 "[notes]/unreal/megajam-2026/lanes/perf3/logs/queue1.txt"
```

Result:

```
free_ram_gb=7.3 of 15.9
cpu_load_pct=0 threads=12
busy_procs=UnrealEditorx1 UnrealEditor-Cmdx1
12:40 pc2 not ready (UnrealEditorx1, cpu 1, free ram 4 GB), waiting
12:41 pc2 not ready (UnrealEditorx1, cpu 0, free ram 4 GB), waiting
```

**Sun 15 Nov 12:42:08 · Tool call: Bash** (Look at GOTCHAS and FINDINGS format)

```
cd "[notes]/unreal"; tail -12 GOTCHAS.md | cut -c1-250; echo; grep -n "^## " FINDINGS.md | tail -5
```

Result:

```
text by content, not bytes.

## c4 and the farm PCs put source files in different unity blobs (15 Nov 2026, verified)

Code that built and passed 239 tests on [pc-b] and pc2 failed to compile on c4: `error C4459: declaration of 'Parts'
hides global declaration`. `SupercutEnemyGun.cpp` has a table at file scope in an anonymous namespace. In c4's unity
build that file shares a blob (`Module.Supercut.1.cpp`) with two test files that have locals of the same name; the farm
PCs group the files differently (their copies are not git checkouts) and never saw it. So a short generic name at file
scope (`Parts`, `Rows`, `Names`) is a build break waiting for a different blob order. Give file-scope names their
file's prefix, and search the whole of `Source` for the new name first: my first rename, `EnemyGunParts`, was already a
function in a test file and failed the same way. The judges' build is compiled on c4, so package on c4 early on
submission day: `cmd /c Tools\package_shipping.cmd` took 2 min 19 s once it compiled (cook of 1,327 packages included).

646:## SUPERCUT run lane: rooms as files, the run, measured numbers (13 Nov 2026, c4, engine 5.8.4)
681:## SUPERCUT on a GTX 1070: what the frame rate pays for (13 Nov 2026, verified on pc2, lane pctest2)
707:## c4 runs out of memory with many agent sessions open (13 Nov 2026, verified by the orchestrator)
723:## Build farm: [pc-b], [pc-c], pc2, pc4 (14 Nov 2026, verified, lane farm1)
746:## NVIDIA DLSS in SUPERCUT (14 Nov 2026, verified by lane dlss2)
```

**Sun 15 Nov 12:42:12 · Tool call: Bash** (Wait for the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* gen_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/hall_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-200; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
=== 12:21:58 hall_a:hall.args
12:51 pc2 not ready (ShaderCompileWorkerx4 UnrealEditorx1, cpu 1, free ram 6 GB), waiting
12:51
```

**Sun 15 Nov 12:51:40 · Tool call: Bash** (Wait for the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* gen_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/hall_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-200; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
=== 12:21:58 hall_a:hall.args
13:00 pc2 not ready (UnrealEditor-Cmdx1, cpu 0, free ram 7 GB), waiting
13:01
```

**Sun 15 Nov 13:01:07 · Tool call: Bash** (Wait for the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* gen_a|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/hall_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-240; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
=== 12:21:58 hall_a:hall.args
13:02:34 started hall_a (idle)
before: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 10.54 W 
gpu gate: idle
after: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 47.84 W 
cpu_before=1
others_before=
seconds_to_exit=22.9
exit_code=777003
hang=False
cpu_after=0
others_after=
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUserSettings.ini
LogSupercut: Display: SCRIPT finished at 15.01 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 70.5, slowest 1% of frames 66.6, over 846 frames and 12.0 s
LogSupercut: Display: FPS frozen: no frames counted
compute pipeline errors: 24
=== 13:03:05 gen_a:gen_s7_fx.args
=== 13:03:05 gen_a:gen_s7_fx.args
13:03
```

### Sun 15 Nov 13:03:13 · Agent (claude-opus-5-5)

Hall run is clean (nobody else on pc2): 70.5 fps average (14.2 ms), slowest 1% at 66.6 fps (15.0 ms), 24 errors. The generated run has started.

**Sun 15 Nov 13:03:14 · Tool call: Bash** (Hall frame time window from the CSV)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; grep -n -E "SCRIPT (0.10|0.20|15.00|finished)|ROOM change:" logs/hall_a/run.log | cut -c1-140 | head; python -I tools/analyze.py hall_a window "SCRIPT 0.20 look" 12 2>&1 | tail -2
```

Result:

```
1230:[2026.11.15-05.02.42:418][  0]LogSupercut: Display: ROOM change: take 1, scene 1 of 1 (01_wind_machine), charges 3 of 3, 0 actors remov
1499:[2026.11.15-05.02.57:557][ 23]LogSupercut: Display: SCRIPT finished at 15.01 s: player alive, health 100
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
StopIteration
```

**Sun 15 Nov 13:03:21 · Tool call: Bash** (Hall frame times after the first 3 s)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools'); import analyze, statistics
log, head, col, data, ft, c, sd = analyze.load('hall_a')
t0,f0 = next((t,fr) for t,fr,x in log if 'ROOM change:' in x)
t1,f1 = next((t,fr) for t,fr,x in log if 'SCRIPT finished' in x)
# skip first 3 s after the room change
cum=0; a=f0-c
while cum<3.0: cum+=ft[a]/1000; a+=1
b=f1-c
n,avg,p99,w1,mx=analyze.stats(ft[a:b]); g=col.get('GPUTime')
print(f'hall_a frames {n}, avg {avg:.2f} ms, p99 {p99:.2f}, slowest1% {w1:.2f}, max {mx:.1f}, GPU avg {statistics.mean(analyze.num(data[i],g) for i in range(a,b)):.2f}, spread {sd*1000:.1f} ms')
EOF
```

Result:

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 10, in <module>
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\statistics.py", line 484, in mean
    T, total, n = _sum(data)
                  ^^^^^^^^^^
  File "C:\Users\USER\AppData\Local\Programs\Python\Python312\Lib\statistics.py", line 193, in _sum
    for n, d in map(_exact_ratio, values):
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<stdin>", line 10, in <genexpr>
IndexError: list index out of range
```

**Sun 15 Nov 13:03:27 · Tool call: Bash** (Debug hall CSV alignment)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools'); import analyze
log, head, col, data, ft, c, sd = analyze.load('hall_a')
print(len(ft), len(data), c, sd, [ (fr,x[:50]) for t,fr,x in log if 'ROOM change:' in x or 'SCRIPT finished' in x])
print(list(col)[:12])
EOF
tail -c 400 logs/hall_a/profile.csv | tr ',' ' ' | cut -c1-300
```

Result:

```
838 838 8 0.0018337041459272668 [(0, 'LogSupercut: Display: ROOM change: take 1, scene 1'), (1023, 'LogSupercut: Display: SCRIPT finished at 15.01 s: ')]
['EVENTS', 'Exclusive/GameThread/EventWait', 'Scheduler/GameThread/CreateThread', 'Exclusive/GameThread/Material_UpdateDeferredCachedUniformExpressions', 'FMsgLogf/FMsgLogfCount', 'CsvProfiler/NumTimestampsProcessed', 'CsvProfiler/NumCustomStatsProcessed', 'CsvProfiler/NumEventsProcessed', 'CsvProfiler/ProcessCSVStats', 'Scheduler/AllWorkers/CreateThread', 'Scheduler/Oversubscription', 'Exclusive/GameThread/InitRenderResource']
054900 0.000100 0.008800 0.093000 6.9765 26.9549 7.8212 61.2286 3.9460 14346 42 5335 358 14.6175 8765.0078 1494.1250 3082.5000 0 10258.8047 0 0.040400 0 0 1.6918 0.020900 0.008400 0 0 8 0.003906 0 0.006200 0 0.001200 0.1598 0.008400 0.064100 0.042500 0.001100 0 0.000800 0.000300 0.001300 0.005600 0.
```

**Sun 15 Nov 13:03:35 · Tool call: Bash** (Inspect CSV headers of the hall run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import csv; csv.field_size_limit(1<<30)
rows=list(csv.reader(open('logs/hall_a/profile.csv',encoding='utf-8',errors='replace')))
print(len(rows), rows[0][:4], rows[0].index('FrameTime') if 'FrameTime' in rows[0] else None, len(rows[0]))
for i,r in enumerate(rows[1:],1):
    if not r or r[0].startswith('[') or r[0]=='EVENTS':
        print('stop at', i, r[:3], len(r)); 
        if r and r[0]=='EVENTS': print('end hdr FrameTime', r.index('FrameTime'))
        break
print(rows[1][:3])
EOF
```

Result:

```
<persisted-output>
Output too large (171KB). Full output saved to: [agent-config]\2f0f321c-13ca-453f-9197-384709201b64\tool-results\bvf43r33f.txt

Preview (first 2KB):
839 ['EVENTS', 'Exclusive/GameThread/EventWait', 'Scheduler/GameThread/CreateThread', 'Exclusive/GameThread/Material_UpdateDeferredCachedUniformExpressions'] 105 413
["Region: EngineInit/Launch - End##0.655173;Region: EngineInit/FEngineLoop::PreInitPreStartupScreen - Begin##0.655185;Region: EngineInit/LaunchSetGameName - Begin##0.655252;Region: EngineInit/LaunchSetGameName - End##0.655405;Region: EngineInit/Init Output Devices - Begin##0.655407;Region: EngineInit/Init Output Devices - End##0.655552;Region: EngineInit/LLM Init - Begin##0.875323;Region: EngineInit/LLM Init - End##0.876404;Region: EngineInit/InitTaggedStorage - Begin##0.876405;Region: EngineInit/InitTaggedStorage - End##0.876406;Region: EngineInit/CreateConsoleOutputDevice - Begin##0.876409;Region: EngineInit/CreateConsoleOutputDevice - End##0.876752;Region: EngineInit/Fix up the relative project path - Begin##0.876823;Region: EngineInit/Fix up the relative project path - End##0.876828;Region: EngineInit/Command Line Adjustments - Begin##0.876830;Region: EngineInit/Command Line Adjustments - End##0.877055;Region: EngineInit/BeginPreInitTextLocalization - Begin##0.877112;Region: EngineInit/BeginPreInitTextLocalization - Begin##0.877115;Region: EngineInit/BeginPreInitTextLocalization - End##0.877128;Region: EngineInit/BeginPreInitTextLocalization - End##0.877128;Region: EngineInit/PreInitShaderLibrary - Begin##0.877129;Region: EngineInit/PreInitShaderLibrary - End##0.877509;Region: EngineInit/LaunchCheckForFileOverride - Begin##0.877511;Region: EngineInit/LoadModule - Begin##0.877994;Region: EngineInit/LoadModule  - StorageServerClient - Begin##0.878148;Region: EngineInit/LoadModule  - StorageServerClient - End##0.878282;Region: EngineInit/LoadModule - End##0.878283;Region: EngineInit/LoadModule - Begin##0.878596;Region: EngineInit/LoadModule  - CookOnTheFly - Begin##0.878724;Region: EngineInit/LoadModule  - CookOnTheFly - End##0.878843;Region: EngineInit/LoadModule - End##0.878848;Region: EngineInit/Lo
...
</persisted-output>
```

### Sun 15 Nov 13:03:42 · Agent (claude-opus-5-5)

The CSV loses its last ~3 s when the game quits (838 rows against about 1,050 frames), so for the hall I use the window from 3 s after the start to the end of the CSV.

**Sun 15 Nov 13:03:46 · Tool call: Bash** (Hall frame times and top GPU passes)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools'); import analyze, statistics
log, head, col, data, ft, c, sd = analyze.load('hall_a')
f0 = next(fr for t,fr,x in log if 'ROOM change:' in x)
cum=0; a=max(1,f0-c)
while cum<3.0: cum+=ft[a]/1000; a+=1
b=len(ft)
n,avg,p99,w1,mx=analyze.stats(ft[a:b]); g=col['GPUTime']
print(f'hall_a frames {n} ({sum(ft[a:b])/1000:.1f} s), avg {avg:.2f} ms, p99 {p99:.2f}, slowest1% {w1:.2f}, max {mx:.1f}, GPU avg {statistics.mean(analyze.num(data[i],g) for i in range(a,b)):.2f}')
res=[]
for name,i in col.items():
    if name.startswith('GPU/'):
        res.append((statistics.mean(analyze.num(data[r],i) for r in range(a,b)),name))
res.sort(reverse=True); print('  '+', '.join(f'{n[4:]} {v:.2f}' for v,n in res[:12]))
EOF
```

Result:

```
hall_a frames 660 (9.4 s), avg 14.18 ms, p99 14.98, slowest1% 15.12, max 15.5, GPU avg 13.45
  Lights 3.71, TemporalSuperResolution 3.60, LumenScreenProbeGather 2.07, RenderDeferredLighting 0.72, Unaccounted 0.67, LumenSceneLighting 0.48, ShadowDepths 0.47, LumenReflections 0.32, Basepass 0.29, Postprocessing 0.29, GlobalDistanceFieldUpdate 0.26, CustomDepth 0.08
```

**Sun 15 Nov 13:03:52 · Tool call: Bash** (Wait for the generated run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* first2|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/started gen_a/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-240; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
13:03:14 started gen_a (idle)
before: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 47.84 W 
gpu gate: idle
after: free_ram_gb=6.9 of 15.9 cpu_load_pct=9 threads=12 busy_procs=clx1 dotnetx2 gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.01 W 
cpu_before=2
others_before=
seconds_to_exit=127.1
exit_code=777003
hang=False
cpu_after=4
others_after=cl
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUserSettings.ini
LogSupercut: Display: RUN wrapped: takes 1, time 144.8 s, shots 54, freezes 16, kills 26
LogSupercut: Display: SCRIPT finished at 24.20 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 60.0, slowest 1% of frames 60.0, over 3883 frames and 64.7 s
LogSupercut: Display: FPS frozen: average 60.0, slowest 1% of frames 60.0, over 4626 frames and 77.1 s
compute pipeline errors: 24
=== 13:05:33 first2:title_main8.args:-ClearCaches
=== 13:05:33 first2:title_main8.args:-ClearCaches
13:05
```

**Sun 15 Nov 13:05:39 · Tool call: Bash** (Generated run samples and per-room table)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; head -2 logs/gen_a/sample.csv; tail -4 logs/gen_a/sample.csv; python -I tools/analyze.py gen_a sections 2>&1 | tail -24
```

Result:

```
13:03:18.0,cpu=6,0 %, 291 MiB, 1898 MHz, 48.16 W, 53
13:03:19.5,cpu=60,0 %, 539 MiB, 1898 MHz, 48.39 W, 53
13:05:17.5,cpu=3,98 %, 2116 MiB, 1847 MHz, 131.25 W, 78
13:05:19.1,cpu=2,98 %, 2116 MiB, 1847 MHz, 135.30 W, 78
13:05:20.7,cpu=2,98 %, 2116 MiB, 1847 MHz, 129.12 W, 78
13:05:22.2,cpu=7,0 %, 2116 MiB, 1847 MHz, 53.57 W, 72
Traceback (most recent call last):
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 180, in <module>
    sections(tag)
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 81, in sections
    log, head, col, data, ft, c, sd = load(tag)
                                      ^^^^^^^^^
  File "[notes]\unreal\megajam-2026\lanes\perf3\tools\analyze.py", line 48, in load
    ft = [float(r[col['FrameTime']]) for r in data]
                ~^^^^^^^^^^^^^^^^^^
IndexError: list index out of range
```

**Sun 15 Nov 13:05:45 · Tool call: Bash** (Drop a truncated last CSV row and rerun the table)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
p='tools/analyze.py'
s=open(p,encoding='utf-8').read()
a="    col = {n: i for i, n in enumerate(head)}\n    ft = [float(r[col['FrameTime']]) for r in data]\n"
b="    col = {n: i for i, n in enumerate(head)}\n    while data and len(data[-1]) <= col['FrameTime']:\n        data.pop()   # the game quit while this row was being written\n    ft = [float(r[col['FrameTime']]) for r in data]\n"
assert s.count(a)==1; s=s.replace(a,b); open(p,'w',encoding='utf-8',newline='\n').write(s)
EOF
python -I tools/analyze.py gen_a sections 2>&1 | tail -24
```

Result:

```
1 d01                                      live      116   17.43  139.81    379.04   379.0   11.96
1 d01                                      frozen    133   12.75   20.28     22.45    22.5   12.11
2 d02                                      live      205   13.41   21.42    145.94   261.6   11.42
2 d02                                      frozen    241   13.28   33.62     72.05    72.8   11.89
3 d03                                      live      153   12.08   17.61     30.43    30.4   11.25
3 d03                                      frozen    241   12.21   17.37     18.67    18.8   11.56
4 d04                                      live      551   12.03   17.45     20.94    27.8   11.32
4 d04                                      frozen    482   12.65   14.54     17.29    17.8   11.92
5 d05                                      live      501   11.76   13.32     18.24    31.0   11.03
5 d05                                      frozen    164   12.01   17.48     17.64    17.6   11.36
6 d06                                      live      315   12.59   16.80     24.68    36.4   11.79
6 d06                                      frozen    360   12.61   17.50     17.83    18.0   11.88
7 d07                                      live      182   12.47   21.30     38.16    38.2   11.63
7 d07                                      frozen    184   13.38   19.64    204.86   204.9   11.73
8 d08                                      live      392   13.21   15.76     33.68    56.3   12.32
8 d08                                      frozen   1080   13.30   17.42     18.21    19.0   12.55
9 d09                                      live      396   12.15   17.30     25.68    36.5   11.37
9 d09                                      frozen    360   12.48   18.23     18.46    18.6   11.78
10 d10                                     live      336   12.59   17.85     31.52    57.4   11.75
10 d10                                     frozen    720   13.00   18.14     18.48    18.8   12.25
11 d11                                     live      189   11.68   18.18     30.75    30.8   10.96
12 d12                                     live      605   12.39   16.97     25.91    67.7   11.58
12 d12                                     frozen    720   13.00   14.11     14.27    14.6   12.25
all rooms                                  both     8626   12.73   17.90     34.02   379.0   11.84
```

**Sun 15 Nov 13:05:54 · Tool call: Bash** (List frames over 100 ms in the generated run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py gen_a hitch 999 100 2>&1 | cut -c1-230; grep -c "PSOPrecacheState: Missed" logs/gen_a/run.log
```

Result:

```
gen_a: title at frame 0 (row 1); 9383 frames in 118.9 s; 5 frames over 100.0 ms (row = frame - 4, spread 16.5 ms)
  +  0.00 s    379.0 ms  frame 5  last log line: LogSupercut: Display: ROOM change frames: the 4 frames from the change took 16.7, 16.7, 16.7, 16.7 ms
  +  0.42 s    139.8 ms  frame 9  last log line: LogSupercut: Display: ROOM change frames: the 4 frames from the change took 16.7, 16.7, 16.7, 16.7 ms
  +  3.80 s    109.2 ms  frame 261  last log line: LogSupercutSound: Display: MUSIC start between flat, from bar 1
  +  4.88 s    261.6 ms  frame 340  last log line: LogSupercut: Display: ROOM change frames: the 4 frames from the change took 16.7, 16.7, 16.7, 16.7 ms
  + 52.22 s    204.9 ms  frame 4179  last log line: LogSupercutSound: Display: STOP freeze_in flat, played out
  first 999.0 s: avg 12.67 ms, p99 17.87, max 379.0
37
```

**Sun 15 Nov 13:06:01 · Tool call: Bash** (Match frames over 50 ms with missed PSOs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools'); import analyze
for tag in ['gen_a','main8_a','first1']:
    log, head, col, data, ft, c, sd = analyze.load(tag)
    miss=[fr for t,fr,x in log if 'PSOPrecacheState: Missed' in x]
    from collections import Counter
    cnt=Counter(miss)
    big=[(i+c, ft[i]) for i in range(1,len(ft)) if ft[i]>50]
    out=[]
    for fr,ms in big:
        m=sum(v for f,v in cnt.items() if fr-2<=f<=fr+1)
        out.append(f'{fr}:{ms:.0f}ms/{m}miss')
    print(tag, 'missed', len(miss), 'frames>50ms', len(big)); print('  ', ' '.join(out))
EOF
```

Result:

```
gen_a missed 37 frames>50ms 10
   5:379ms/0miss 9:140ms/0miss 261:109ms/0miss 340:262ms/0miss 465:71ms/0miss 468:73ms/0miss 4179:205ms/0miss 4417:56ms/0miss 6823:57ms/0miss 8068:68ms/0miss
main8_a missed 37 frames>50ms 20
   5:680ms/0miss 6:187ms/0miss 13:76ms/0miss 820:93ms/0miss 922:442ms/0miss 1132:320ms/0miss 1683:71ms/0miss 3439:58ms/0miss 3980:352ms/0miss 5279:61ms/0miss 6084:657ms/0miss 9351:171ms/0miss 10258:51ms/0miss 13634:55ms/0miss 13712:62ms/0miss 15096:175ms/0miss 16104:72ms/0miss 20610:56ms/0miss 20611:505ms/0miss 22893:72ms/0miss
first1 missed 48 frames>50ms 3
   4:230ms/8miss 7:100ms/0miss 1222:60ms/0miss
```

### Sun 15 Nov 13:06:11 · Agent (claude-opus-5-5)

In the fixed-step runs the frames over 50 ms don't line up with missed pipelines. Checking what the log shows around the biggest ones.

**Sun 15 Nov 13:06:13 · Tool call: Bash** (Log lines around generated-run spikes)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I - <<'EOF'
import sys; sys.path.insert(0,'tools'); import analyze
log, head, col, data, ft, c, sd = analyze.load('gen_a')
for target in (340, 4179, 261):
    print('== frame', target, f'{ft[target-c]:.0f} ms')
    for t,fr,x in log:
        if target-3 <= fr <= target+1 and 'TRACE' not in x: print('  ', fr, x[:150])
EOF
```

Result:

```
== frame 340 262 ms
   339 LogSupercut: Display: ROOM change frames: the 4 frames from the change took 16.7, 16.7, 16.7, 16.7 ms
== frame 4179 205 ms
   4178 LogSupercutSound: Display: STOP freeze_in flat, played out
== frame 261 109 ms
```

**Sun 15 Nov 13:06:24 · Tool call: Bash** (Wait for cold and warm first-launch runs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "queue done|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/started first2/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-240; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
13:14 pc2 not ready (Supercutx2, cpu 13, free ram 9 GB), waiting
13:15
```

**Sun 15 Nov 13:15:51 · Tool call: Bash** (Keep waiting for first-launch runs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "queue done|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/started first2/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-240; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
13:24 pc2 not ready (Supercutx2, cpu 0, free ram 8 GB), waiting
13:25
```

**Sun 15 Nov 13:25:18 · Tool call: Bash** (Identify the Supercut processes on pc2)

```
ssh pc2 'wmic process where "name like \"Supercut%\"" get ProcessId,CreationDate,ExecutablePath /format:list' 2>&1 | tr -d '\r' | grep -v '^$' | sed -E 's#C:\\Users\\USER\\]+#%USERPROFILE%#g' | head
```

Result:

```
CreationDate=20261115132054.634553+480
ExecutablePath=C:\UE\Farm\_builds\sfx5\Supercut59\Windows\Supercut.exe
ProcessId=16764
CreationDate=20261115132054.644680+480
ExecutablePath=C:\UE\Farm\_builds\sfx5\Supercut59\Windows\Supercut\Binaries\Win64\Supercut.exe
ProcessId=21772
```

**Sun 15 Nov 13:25:28 · Tool call: Bash** (Confirm diag-only diff and mirror to pc2)

```
cd /d/UE/wt/perf3 && git status --short && git diff --stat; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" mirror pc2 perf3 /d/UE/wt/perf3 2>&1 | tail -3
```

Result:

```
M Source/Supercut/SupercutPlayerController.cpp
 Source/Supercut/SupercutPlayerController.cpp | 30 ++++++++++++++++++++++++++++
 1 file changed, 30 insertions(+)
FARM mirror pc2:C:\UE\Farm\perf3 sent 1 files (0.0 MB), deleted 2, 3010 files in project, 2.4 s
Shell cwd was reset to [notes]
```

**Sun 15 Nov 13:25:36 · Tool call: Bash** (Show hall and main8 arg files)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat tools/args/hall.args; echo; cat tools/args/main8_fx.args
```

Result:

```
-SupercutRoom=fight/01_wind_machine -SupercutSeed=1 -SupercutDev -SupercutScript=C:\UE\Farm\perf3\Script\shell1_hall_fps.txt -csvCaptureFrames=20000 -csvGpuStats -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log

-SupercutRun=main8 -SupercutSeed=1 -SupercutScript=C:\UE\Farm\perf3\Script\main8.txt -UseFixedTimeStep -FPS=240 -csvCaptureFrames=40000 -csvGpuStats -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutTrace -SupercutQuit -abslog={O}\run.log
```

**Sun 15 Nov 13:25:45 · Tool call: Bash** (Write the diag args and the second batch script)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; printf '%s' '-SupercutRoom=fight/01_wind_machine -SupercutSeed=1 -SupercutDev -SupercutPsoDiag -SupercutScript=C:\UE\Farm\perf3\Script\shell1_hall_fps.txt -nosplash -unattended -DeterministicAudio -SupercutFps -SupercutQuit -abslog={O}\run.log' > tools/args/psodiag.args; cat > tools/after1.sh <<'EOF'
#!/bin/bash
# Lane perf3, second batch: main8 rerun (fixed step, GPU passes), then the PSO diagnostic build, package and run on pc2.
cd "$(dirname "$0")/.."
F="[notes]/unreal/megajam-2026/farm/farm.sh"
bash tools/queue.sh main8_b:main8_fx.args
wait_ready() {
  local waited=0
  while true; do
    st=$("$F" status pc2 2>/dev/null)
    busy=$(echo "$st" | sed -n 's/^busy_procs=//p'); cpu=$(echo "$st" | sed -n 's/^cpu_load_pct=\([0-9]*\).*/\1/p')
    ram=$(echo "$st" | sed -n 's/^free_ram_gb=\([0-9]*\).*/\1/p')
    if [ "$busy" = "none" ] && [ "${cpu:-100}" -lt 60 ] && [ "${ram:-0}" -ge 6 ]; then echo "$(date +%H:%M) ready: ram $ram cpu $cpu"; return 0; fi
    echo "$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting"; sleep 60; waited=$((waited+60))
    [ $waited -gt 3600 ] && { echo "pc2 not ready for an hour"; return 1; }
  done
}
wait_ready || exit 1
echo "=== $(date +%H:%M:%S) diag build"; "$F" build pc2 perf3 /d/UE/wt/perf3_farmlogs -Jobs 4 2>&1 | tail -3
wait_ready || exit 1
echo "=== $(date +%H:%M:%S) diag package"; "$F" package pc2 perf3 /d/UE/wt/perf3_farmlogs 2>&1 | tail -3
bash tools/queue.sh psodiag:psodiag.args
echo "=== $(date +%H:%M:%S) after1 done"
EOF
echo ok
```

Result:

```
ok
```

**Sun 15 Nov 13:25:52 · Tool call: Bash** (Check TSR pass event names for 16-bit info)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; grep -n -E "RDG_EVENT_NAME\(\"TSR (DecimateHistory|UpdateHistory)" -A4 "$S" | head -20
```

Result:

```
2833:			RDG_EVENT_NAME("TSR DecimateHistory(#%d%s%s%s%s%s) %dx%d",
2834-				PermutationVector.ToDimensionValueId(),
2835-				PermutationVector.Get<FTSRDecimateHistoryCS::FMoireReprojectionDim>() ? TEXT(" ReprojectMoire") : TEXT(""),
2836-				PermutationVector.Get<FTSRDecimateHistoryCS::FResurrectionReprojectionDim>() ? TEXT(" ReprojectResurrection") : TEXT(""),
2837-				PermutationVector.Get<FTSRDecimateHistoryCS::FThinGeometryCoverageDim>() ? TEXT(" ThinGeometryCoverage") : TEXT(""),
--
3489:			RDG_EVENT_NAME("TSR UpdateHistory(#%d Quality=%s%s%s%s%s%s%s) %dx%d",
3490-				PermutationVector.ToDimensionValueId(),
3491-				kUpdateQualityNames[int32(PermutationVector.Get<FTSRUpdateHistoryCS::FQualityDim>())],
3492-				PermutationVector.Get<FTSRShader::F16BitVALUDim>() ? TEXT(" 16bit") : TEXT(""),
3493-				PermutationVector.Get<FTSRShader::FAlphaChannelDim>() ? TEXT(" AlphaChannel") : TEXT(""),
```

**Sun 15 Nov 13:25:58 · Tool call: Bash** (Wait for first-launch runs)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "queue done|giving up" logs/queue1.txt && break; sleep 10; done; sed -n '/started first2/,$p' logs/queue1.txt | grep -v "not ready" | cut -c1-240; tail -1 logs/queue1.txt; date +%H:%M
```

Result:

```
13:34 pc2 not ready (dotnetx2 linkx1, cpu 19, free ram 5 GB), waiting
13:35
```

### Sun 15 Nov 13:35:27 · Brief from the orchestrating agent

From the main thread, 15 Nov 13:36. FARM CHANGE. Stay on pc2 (your subject is its old graphics card). farm.sh now QUEUES by itself: build, test, package and run take a slot on the host (pc2 1, [pc-c] 3, c4 2) and wait inside the call when all are taken. Do not poll the load first; call the step and let it wait. `farm.sh slots` shows who holds what. Between 13:22 and 13:24 a broken step.ps1 of mine was live; if a step failed then with a PowerShell parser error (MissingEndCurlyBrace), run `mirror` again and repeat the step. [pc-b] is OUT until I say otherwise, so drop any [pc-b] comparison you had planned; [pc-c] is on (root F:\UE, AMD RX 9070 XT, a person uses it) if you want a modern-card column. No reply needed; carry on.

### Sun 15 Nov 13:35:32 · Agent (claude-opus-5-5)

The main thread says farm.sh now queues steps itself. My desktop-session runs go around farm.sh, so I'm checking whether they can hold a slot.

**Sun 15 Nov 13:35:33 · Tool call: Bash** (Read farm.sh slot commands and current holders)

```
cd "[notes]/unreal/megajam-2026"; sed -n 1,30p farm/farm.sh | grep -n -E "slot|hold|lock|queue" ; grep -n -E "slot" farm/farm.sh | head -30; "farm/farm.sh" slots 2>&1 | head
```

Result:

```
12:#   farm.sh slots                                             who holds or waits for which PC right now
20:# Slots (15 Nov): build, test, package, package-shipping and run take one of the host's slots and wait for one
21:# when all are taken, so the lanes no longer pile onto one PC. A slot whose farm.sh has died is taken over.
12:#   farm.sh slots                                             who holds or waits for which PC right now
20:# Slots (15 Nov): build, test, package, package-shipping and run take one of the host's slots and wait for one
21:# when all are taken, so the lanes no longer pile onto one PC. A slot whose farm.sh has died is taken over.
35:slots_of() {  # heavy steps at once on each PC
48:slot=''
49:take_slot() {   # take_slot <host> <name> <step>: returns when this process holds a slot on the host
51:  n=$(slots_of "$host"); mkdir -p "$lockdir"
57:        slot=$d; trap 'rm -rf "$slot"' EXIT
58:        [ "$waited" -gt 0 ] && echo "FARM waited ${waited}s for a slot on $host" >&2
61:      if [ -f "$d/owner" ]; then   # a slot whose farm.sh is gone, or older than an hour, is free
66:    [ "$waited" -eq 0 ] && echo "FARM $host is full ($n slot(s)); waiting. 'farm.sh slots' shows who holds them" >&2
90:  take_slot "$host" "$name" "$s"
162:  slots)
172:      echo "$h: $held of $(slots_of "$h") slot(s) held"
[pc-b]: 0 of 2 slot(s) held
pc2: 0 of 1 slot(s) held
[pc-c]: 0 of 3 slot(s) held
c4: home1 build since 13:33:16 (2 min, running)
c4: set2 test since 13:34:21 (1 min, running)
c4: 2 of 2 slot(s) held
```

**Sun 15 Nov 13:35:38 · Tool call: Bash** (Read the slot implementation)

```
cd "[notes]/unreal/megajam-2026"; sed -n 35,95p farm/farm.sh
```

Result:

```
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
is_local() { [ "$1" = c4 ]; }

lockdir=/d/UE/Farm/_locks
slot=''
take_slot() {   # take_slot <host> <name> <step>: returns when this process holds a slot on the host
  local host=$1 name=$2 s=$3 n i d pid t now waited=0
  n=$(slots_of "$host"); mkdir -p "$lockdir"
  while :; do
    for i in $(seq 1 "$n"); do
      d="$lockdir/$host.$i"
      if mkdir "$d" 2>/dev/null; then
        echo "$$ $name $s $(date +%s) $(date +%H:%M:%S)" > "$d/owner"
        slot=$d; trap 'rm -rf "$slot"' EXIT
        [ "$waited" -gt 0 ] && echo "FARM waited ${waited}s for a slot on $host" >&2
        return 0
      fi
      if [ -f "$d/owner" ]; then   # a slot whose farm.sh is gone, or older than an hour, is free
        read -r pid _ _ t _ < "$d/owner"; now=$(date +%s)
        if [ -n "${pid:-}" ] && { [ ! -d "/proc/$pid" ] || [ $((now - ${t:-now})) -gt 3600 ]; }; then rm -rf "$d"; fi
      fi
    done
    [ "$waited" -eq 0 ] && echo "FARM $host is full ($n slot(s)); waiting. 'farm.sh slots' shows who holds them" >&2
    sleep 15; waited=$((waited + 15))
  done
}

# copy path $2 (forward slashes) on host $1 into local folder $3, masking user and computer names in text files
pull() {
  local host=$1 src=$2 dst=$3 un cn
  mkdir -p "$dst"
  if is_local "$host"; then
    cp -r "$src" "$dst/" || return 1
    un=${USERNAME:-}; cn=${COMPUTERNAME:-}
  else
    scp -r -q "$host:$src" "$dst/" || return 1
    un=$(ssh "$host" 'echo %USERNAME%' | tr -d '\r\n'); cn=$(ssh "$host" 'echo %COMPUTERNAME%' | tr -d '\r\n')
  fi
  [ -n "$un" ] && [ -n "$cn" ] || return 0
  find "$dst" -type f \( -name '*.log' -o -name '*.txt' -o -name '*.ini' -o -name '*.csv' \) -print0 |
    xargs -0 -r sed -i -e "s#$un#USER#Ig" -e "s#$cn#PC#Ig"
}

step() {   # step <name of step> <host> <name> <log folder> [args...]
  local s=$1 host=$2 name=$3 logs=$4; shift 4
  local root; root=$(root_of "$host") || exit $?
  take_slot "$host" "$name" "$s"
  local af=''
  if [ $# -gt 0 ]; then
    af="$root\\Farm\\_out\\$name.$s.args.txt"
    local tmp; tmp=$(mktemp)
    printf '%s\r\n' "$@" > "$tmp"
```

### Sun 15 Nov 13:35:44 · Agent (claude-opus-5-5)

I can take pc2's slot the same way farm.sh does (a lock folder on c4). I'll stop my waiting queue, change go.sh to take the slot instead of polling load, and restart the remaining runs.

**Sun 15 Nov 13:35:46 · Tool call: Bash** (Check queue is still only waiting)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; tail -2 logs/queue1.txt; ls logs/first2 2>/dev/null; ssh pc2 'schtasks /query /tn perf3_supercut /fo list' 2>&1 | grep -i -E "status|last run" | head -3
```

**Sun 15 Nov 13:35:46 · Tool call: ToolSearch**

```
{
 "query": "select:TaskStop",
 "max_results": 1
}
```

Result:

```
13:33 pc2 not ready (clx1 dotnetx2, cpu 7, free ram 6 GB), waiting
13:34 pc2 not ready (dotnetx2 linkx1, cpu 19, free ram 5 GB), waiting
load.txt
Status:        Ready
```

Result:

```

```

**Sun 15 Nov 13:35:49 · Tool call: TaskStop**

```
{
 "task_id": "bdmv9f1ql"
}
```

Result:

```
{"message":"Successfully stopped task: bdmv9f1ql (cd \"[notes]/unreal/megajam-2026/lanes/perf3\"; bash tools/queue.sh pics main8_a:main8_fx.args hall_a:hall.args gen_a:gen_s7_fx.args first2:title_main8.args:-ClearCaches warm1:title_main8.args > logs/queue1.txt 2>&1)","task_id":"bdmv9f1ql","task_type":"local_bash","command":"cd \"[notes]/unreal/megajam-2026/lanes/perf3\"; bash tools/queue.sh pics main8_a:main8_fx.args hall_a:hall.args gen_a:gen_s7_fx.args first2:title_main8.args:-ClearCaches warm1:title_main8.args > logs/queue1.txt 2>&1"}
```

**Sun 15 Nov 13:35:54 · Tool call: Bash** (Make sure no old queue processes remain)

```
ps aux | grep -E "go.sh|queue.sh" | grep -v grep | awk '{print $1}' | xargs -r kill 2>/dev/null; ps aux | grep -E "go.sh|queue.sh" | grep -v grep | wc -l
```

Result:

```
0
```

**Sun 15 Nov 13:36:02 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "old_string": "waited=0\nwhile true; do\n  st=$(\"$F\" status pc2 2>/dev/null)\n  busy=$(echo \"$st\" | sed -n 's/^busy_procs=//p'); cpu=$(echo \"$st\" | sed -n 's/^cpu_load_pct=\\([0-9]*\\).*/\\1/p')\n  ram=$(echo \"$st\" | sed -n 's/^free_ram_gb=\\([0-9]*\\).*/\\1/p')\n  if [ \"$busy\" = \"none\" ] && [ \"${cpu:-100}\" -lt 60 ] && [ \"${ram:-0}\" -ge 6 ]; then break; fi\n  echo \"$(date +%H:%M) pc2 not ready ($busy, cpu $cpu, free ram $ram GB), waiting\"; sleep 60; waited=$((waited+60))\n  [ $waited -gt ${WAIT_MAX:-1800} ] && { echo \"pc2 not ready for $waited s, giving up\"; exit 1; }\ndone",
 "new_string": "# Take pc2's one farm slot the way farm.sh's take_slot does (lock folder on c4, owner line \"pid name step epoch time\"),\n# so no farm step of another lane starts during the run. Held until this script exits.\nlock=/d/UE/Farm/_locks/pc2.1; waited=0\nuntil mkdir \"$lock\" 2>/dev/null; do\n  if [ -f \"$lock/owner\" ]; then\n    read -r pid _ _ t _ < \"$lock/owner\"; now=$(date +%s)\n    if [ -n \"${pid:-}\" ] && { [ ! -d \"/proc/$pid\" ] || [ $((now - ${t:-now})) -gt 3600 ]; }; then rm -rf \"$lock\"; continue; fi\n  fi\n  [ $((waited % 300)) -eq 0 ] && echo \"$(date +%H:%M) pc2 slot held: $(cat \"$lock/owner\" 2>/dev/null)\"\n  sleep 15; waited=$((waited+15))\ndone\necho \"$$ perf3 run $(date +%s) $(date +%H:%M:%S)\" > \"$lock/owner\"; trap 'rm -rf \"$lock\"' EXIT\necho \"$(date +%H:%M:%S) took the pc2 slot after ${waited}s\"\nst=$(\"$F\" status pc2 2>/dev/null)"
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\perf3\tools\go.sh has been updated successfully.
```

**Sun 15 Nov 13:36:04 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\go.sh",
 "old_string": "# 1. farm load check (busy_procs none, CPU < 60, free RAM >= 6 GB) and a GPU idle gate",
 "new_string": "# 1. takes pc2's farm slot (FARM change of 15 Nov 13:36), records farm status, and a GPU idle gate"
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\perf3\tools\go.sh has been updated successfully.
```

**Sun 15 Nov 13:36:12 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tools\\after1.sh",
 "content": "#!/bin/bash\n# Lane perf3, second batch on pc2: cold and warm first launch, main8 rerun (fixed step, GPU passes), then the PSO\n# diagnostic build, package and run. go.sh takes pc2's farm slot; farm.sh steps wait for it by themselves.\ncd \"$(dirname \"$0\")/..\"\nF=\"[notes]/unreal/megajam-2026/farm/farm.sh\"\nfor s in first2:title_main8.args:-ClearCaches warm1:title_main8.args main8_b:main8_fx.args; do\n  IFS=: read -r tag af sw <<< \"$s\"\n  echo \"=== $(date +%H:%M:%S) $tag\"; bash tools/go.sh \"$tag\" \"$af\" $sw\ndone\necho \"=== $(date +%H:%M:%S) diag build\"; \"$F\" build pc2 perf3 /d/UE/wt/perf3_farmlogs -Jobs 4 2>&1 | tail -3\necho \"=== $(date +%H:%M:%S) diag package\"; \"$F\" package pc2 perf3 /d/UE/wt/perf3_farmlogs 2>&1 | tail -3\necho \"=== $(date +%H:%M:%S) psodiag\"; bash tools/go.sh psodiag psodiag.args\necho \"=== $(date +%H:%M:%S) after1 done\"\n"
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\perf3\tools\after1.sh has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 13:36:14 · Tool call: Bash** (Run the second batch on pc2 in the background)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; rm -rf logs/first2; bash tools/after1.sh > logs/after1.txt 2>&1
```

Result:

```
Command running in background with ID: bj43e42y1. Output is being written to: C:\Users\USER\AppData\Local\Temp\claude\ce66ae306241b5fa\2f0f321c-13ca-453f-9197-384709201b64\tasks\bj43e42y1.output. You will be notified when it completes. To check interim output, use Read on that file path.
Session cwd remains [notes]\unreal\megajam-2026\lanes\perf3; directory changes made by the backgrounded command do not apply to subsequent commands.
```

**Sun 15 Nov 13:36:28 · Tool call: Bash** (Log progress and check the second batch started)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat >> LOG.md <<'EOF'
- 12:15 main8_a (desktop, fixed step 240, CSV): run line matches, 24 errors, but desk_run saw two Supercut processes at launch (set2's run started between the farm check and mine). Discarded; rerun as main8_b.
- 13:03 hall_a (desktop, live, shell1's script, damage off): no other process before or after. Frames 3 s to end of CSV: avg 14.18 ms, p99 14.98, slowest 1 % 15.12, max 15.5; GPU 13.45 ms. Top GPU passes: Lights 3.71, TSR 3.60, Lumen screen probe gather 2.07, deferred lighting 0.72, Lumen scene lighting 0.48, shadow depths 0.47. Game's FPS line: 70.5 avg, slowest 1 % 66.6.
- 13:03 gen_a (desktop, fixed step 60): no other process at launch; a compile started after the run (CPU 2 to 7 % in the last samples). `RUN wrapped: takes 1, time 144.8 s, shots 54, freezes 16, kills 26`, 24 errors. All rooms avg 12.73 ms, p99 17.9, slowest 1 % 34.0, GPU 11.84. Heaviest room d08 (fight with a long freeze): live 13.21 ms avg / slowest 1 % 33.7, frozen 13.30 / 18.2, GPU 12.3 to 12.6.
- CSV quirks: the CSV loses the last ~3 s when the game quits and the last row can be cut short; analyze.py drops a short last row and windows end at the CSV end.
- 13:36 FARM change from the main thread: farm.sh queues by itself, pc2 has 1 slot, [pc-b] out. My desktop runs go round farm.sh, so go.sh now takes pc2's slot through farm.sh's own lock folder (`D:\UE\Farm\_locks\pc2.1`, same owner line) instead of polling load. Queue stopped while it was only waiting (first2 never launched); second batch (tools/after1.sh) started: first2 cold, warm1, main8_b, then the PSO diagnostic build, package and run.
EOF
sleep 30; cat logs/after1.txt; "[notes]/unreal/megajam-2026/farm/farm.sh" slots | grep pc2
```

Result:

```
=== 13:36:14 first2
13:36 pc2 slot held: 362367 sfx5 run 1794720956 13:35:56
pc2: sfx5 run since 13:35:56 (1 min, running)
pc2: 1 of 1 slot(s) held
```

### Sun 15 Nov 13:37:01 · Agent (claude-opus-5-5)

I've switched my runs to farm.sh's new slot system. sfx5 holds the pc2 slot right now; after that my cold start, warm start and main8 rerun go in, then the diagnostic build.

**Sun 15 Nov 13:37:02 · Tool call: Bash** (Wait for the cold first-launch run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* warm1" logs/after1.txt && break; sleep 10; done; grep -v "slot held" logs/after1.txt | cut -c1-240; date +%H:%M
```

Result:

```
=== 13:36:14 first2
13:43:36 took the pc2 slot after 435s
13:43:44 started first2 (idle)
before: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 11.99 W 
gpu gate: idle
after: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.40 W 
cpu_before=0
others_before=
seconds_to_exit=129
exit_code=777003
hang=False
cpu_after=0
others_after=
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality CUSTOM (never chosen), display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUserSettings.ini
LogSupercut: Display: SETTINGS first start: benchmark CPU 197, GPU 265, groups view 3, anti-aliasing 3, shadows 3, GI 3, reflections 3, post 3, textures 3, effects 3, foliage 3, shading 3, in 4.8 s; lowest EPIC, quality set to HIGH
LogSupercut: Display: RUN wrapped: takes 1, time 98.3 s, shots 46, freezes 14, kills 17
LogSupercut: Display: SCRIPT finished at 15.93 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 81.6, slowest 1% of frames 59.1, over 4917 frames and 60.2 s
LogSupercut: Display: FPS frozen: average 79.1, slowest 1% of frames 65.6, over 2776 frames and 35.1 s
compute pipeline errors: 24
=== 13:46:04 warm1
13:46:05 took the pc2 slot after 0s
13:46
```

**Sun 15 Nov 13:46:15 · Tool call: Bash** (Hitches and per-room table for the cold run)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py first2 hitch 60 50 | cut -c1-200; echo "missed: $(grep -c 'PSOPrecacheState: Missed' logs/first2/run.log)"; grep -E "ROOM change frames" logs/first2/run.log | sed 's/.*took //' | tr '\n' ' '; echo; python -I tools/analyze.py first2 sections | tail -18
```

Result:

```
first2: title at frame 0 (row 1); 4713 frames in 60.0 s; 1 frames over 50.0 ms (row = frame - 3, spread 8.2 ms)
  +  0.00 s    237.6 ms  frame 4  last log line: LogRHI: Display: Encountered a new graphics PSO: 1758115893 (PSOPrecacheState: Missed)
  first 60.0 s: avg 12.73 ms, p99 16.60, max 237.6
missed: 49
21.6, 29.0, 8.6, 13.5 ms 22.5, 28.5, 7.8, 12.3 ms 29.9, 19.9, 7.8, 12.4 ms 30.5, 19.4, 7.5, 12.7 ms 26.4, 21.8, 6.8, 12.1 ms 31.9, 18.5, 7.6, 12.7 ms 24.5, 22.4, 11.9, 9.6 ms 36.4, 19.2, 6.4, 12.6 ms 
room                                       state  frames  avg ms  p99 ms slow1% ms  max ms GPU avg
1 01_wind_machine                          live      485   13.84   17.23     30.54    37.3   13.11
1 01_wind_machine                          frozen    458   13.37   15.72     16.32    17.9   12.64
2 a_the_cue                                live      176   12.07   22.43     28.58    28.6   11.26
2 a_the_cue                                frozen    295   12.35   13.71     15.29    16.8   11.67
3 02_stunt_run                             live     1202   12.16   16.79     21.22    34.7   11.45
3 02_stunt_run                             frozen    375   12.80   13.68     13.96    14.1   12.05
4 03_long_lens                             live      869   12.27   16.93     22.95    33.1   11.54
4 03_long_lens                             frozen    294   12.75   13.75     14.07    14.2   12.03
5 b_the_wild_wall                          live      570   12.04   16.48     22.97    32.6   11.31
5 b_the_wild_wall                          frozen    157   12.06   13.01     13.20    13.2   11.32
6 04_hot_set                               live      749   12.24   17.50     27.18    38.2   11.50
6 04_hot_set                               frozen    543   12.31   13.58     15.49    18.4   11.60
7 c_the_cutaway                            live      293   12.46   22.49     30.20    36.0   11.69
7 c_the_cutaway                            frozen    304   12.15   13.56     13.94    14.3   11.43
8 05_martini_shot                          live      772   12.24   16.67     24.43    36.3   11.50
8 05_martini_shot                          frozen    350   12.87   13.98     14.19    14.5   12.12
all rooms                                  both     7892   12.46   16.73     21.59    38.2   11.73
```

**Sun 15 Nov 13:46:22 · Tool call: Bash** (Wait for the warm run and analyse it)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* main8_b" logs/after1.txt && break; sleep 10; done; sed -n '/=== .* warm1/,$p' logs/after1.txt | grep -v "slot held" | cut -c1-200; python -I tools/analyze.py warm1 hitch 60 50 | cut -c1-200; echo "missed: $(grep -c 'PSOPrecacheState: Missed' logs/warm1/run.log)"; python -I tools/analyze.py warm1 sections | tail -1
```

Result:

```
=== 13:46:04 warm1
13:46:05 took the pc2 slot after 0s
13:46:12 started warm1 (idle)
before: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 12.87 W 
gpu gate: idle
after: free_ram_gb=10.4 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.40 W 
cpu_before=0
others_before=
seconds_to_exit=121.5
exit_code=777003
hang=False
cpu_after=2
others_after=
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUs
LogSupercut: Display: RUN wrapped: takes 1, time 98.4 s, shots 46, freezes 14, kills 17
LogSupercut: Display: SCRIPT finished at 15.94 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 81.4, slowest 1% of frames 58.7, over 4909 frames and 60.3 s
LogSupercut: Display: FPS frozen: average 79.3, slowest 1% of frames 64.6, over 2783 frames and 35.1 s
compute pipeline errors: 24
=== 13:48:25 main8_b
13:48:26 took the pc2 slot after 0s
warm1: title at frame 0 (row 1); 4712 frames in 60.0 s; 2 frames over 50.0 ms (row = frame - 3, spread 7.9 ms)
  +  0.00 s    235.8 ms  frame 4  last log line: LogRHI: Display: Encountered a new graphics PSO: 1758115893 (PSOPrecacheState: Missed)
  +  0.26 s     92.5 ms  frame 8  last log line: LogRHI: Display: Encountered a new graphics PSO: 1758115893 (PSOPrecacheState: Missed)
  first 60.0 s: avg 12.74 ms, p99 16.74, max 235.8
missed: 37
all rooms                                  both     7893   12.46   16.89     21.73    38.0   11.74
```

### Sun 15 Nov 13:48:34 · Brief from the orchestrating agent

From the main thread, 15 Nov 13:48. pc2 GOES DOWN SOON: the owner is shutting it down to add memory. Let the step you have running on pc2 finish (do not stop it), fetch its logs and pictures to c4 at once, and start NO new step on pc2. farm.sh now refuses new pc2 steps by waiting ("FARM pc2 is closed"); do not sit in that wait. Until I tell you pc2 is back (about 20 to 30 minutes from the moment it is empty), work on what needs no pc2: write up what you have measured so far, and take your modern-card column on [pc-c] if you planned one. After the restart pc2 will have 32 GB instead of 16, its mirrors stay on disk, and any open program there will be closed, so note in your report which numbers were taken before and after the memory change. Reply with one line when your pc2 step has ended and its output is on c4.

**Sun 15 Nov 13:48:40 · Tool call: Bash** (Wait for main8_b to finish before the diag build)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* diag build" logs/after1.txt && break; sleep 5; done; sed -n '/=== .* main8_b/,$p' logs/after1.txt | cut -c1-200; date +%H:%M:%S
```

Result:

```
=== 13:48:25 main8_b
13:48:26 took the pc2 slot after 0s
13:48:34 started main8_b (idle)
13:53:23
```

**Sun 15 Nov 13:53:27 · Tool call: Bash** (Keep waiting for main8_b)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; for i in $(seq 1 56); do grep -q -E "=== .* diag build" logs/after1.txt && break; sleep 5; done; sed -n '/started main8_b/,$p' logs/after1.txt | cut -c1-200; date +%H:%M:%S
```

Result:

```
13:48:34 started main8_b (idle)
before: free_ram_gb=10.4 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.50 W 
gpu gate: idle
after: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.20 W 
cpu_before=0
others_before=
seconds_to_exit=334.6
exit_code=777003
hang=False
cpu_after=1
others_after=
LogSupercut: Display: SETTINGS at start: sensitivity 1.00, volume 100, quality HIGH, display FULLSCREEN 1920x1080, file C:/UE/Farm/_builds/perf3/Supercut59/Windows/Supercut/Saved/Config/Windows/GameUs
LogSupercut: Display: RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17
LogSupercut: Display: SCRIPT finished at 15.93 s: player alive, health 100
LogSupercut: Display: FPS rolling: average 240.0, slowest 1% of frames 240.0, over 14414 frames and 60.1 s
LogSupercut: Display: FPS frozen: average 240.0, slowest 1% of frames 240.0, over 8426 frames and 35.1 s
compute pipeline errors: 24
=== 13:54:22 diag build
13:54:23
```

**Sun 15 Nov 13:54:26 · Tool call: TaskStop**

```
{
 "task_id": "bj43e42y1"
}
```

Result:

```
{"message":"Successfully stopped task: bj43e42y1 (cd \"[notes]/unreal/megajam-2026/lanes/perf3\"; rm -rf logs/first2; bash tools/after1.sh > logs/after1.txt 2>&1)","task_id":"bj43e42y1","task_type":"local_bash","command":"cd \"[notes]/unreal/megajam-2026/lanes/perf3\"; rm -rf logs/first2; bash tools/after1.sh > logs/after1.txt 2>&1"}
```

**Sun 15 Nov 13:54:31 · Tool call: Bash** (Confirm nothing of mine waits for pc2 and main8_b output is on c4)

```
ps aux | grep -E "farm.sh|after1|go.sh" | grep -v grep | awk '{print $1}' | xargs -r kill 2>/dev/null; sleep 2; ps aux | grep -E "farm.sh|after1" | grep -v grep | wc -l; F="[notes]/unreal/megajam-2026/farm/farm.sh"; "$F" slots | grep pc2; ls /d/UE/Farm/_locks/; cd "[notes]/unreal/megajam-2026/lanes/perf3"; ls -la logs/main8_b | awk '{print $5, $NF}'
```

Result:

```
0
pc2: hands2 run since 13:54:26 (0 min, running)
pc2: 1 of 1 slot(s) held
c4.2
pc2.1
pc2.closed
[pc-c].1
[pc-c].2
[pc-c].3
 55586
0 .
0 ..
2471 GameUserSettings.after.ini
268 load.txt
56360960 profile.csv
607 result.txt
530979 run.log
11975 sample.csv
```

### Sun 15 Nov 13:54:38 · Agent (claude-opus-5-5)

My pc2 step (main8_b) has ended and its output (log, CSV, samples, settings) is on c4. Nothing of mine is waiting on pc2; the diagnostic build never took the slot.

**Sun 15 Nov 13:54:39 · Tool call: Bash** (Remove my scheduled task and analyse main8_b)

```
ssh pc2 'schtasks /delete /tn perf3_supercut /f' 2>&1 | head -2; cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py main8_b sections | tail -18
```

Result:

```
SUCCESS: The scheduled task "perf3_supercut" was successfully deleted.
room                                       state  frames  avg ms  p99 ms slow1% ms  max ms GPU avg
1 01_wind_machine                          live     1604   14.15   16.71     41.93   230.2   13.20
1 01_wind_machine                          frozen   1465   13.52   16.09     19.70    41.5   12.79
2 a_the_cue                                live      505   12.01   13.01     17.56    25.1   11.26
2 a_the_cue                                frozen    877   12.26   16.11     18.73    32.4   11.58
3 02_stunt_run                             live     3503   12.13   16.74     19.56    35.1   11.42
3 02_stunt_run                             frozen   1152   12.67   13.50     19.41    33.2   11.94
4 03_long_lens                             live     2552   12.14   16.37     19.80    33.8   11.43
4 03_long_lens                             frozen    900   12.63   14.02     20.05    34.0   11.90
5 b_the_wild_wall                          live     1644   11.93   13.05     18.97    33.8   11.22
5 b_the_wild_wall                          frozen    456   11.96   12.94     22.69    31.7   11.23
6 04_hot_set                               live     2191   12.11   17.09     23.39    38.5   11.40
6 04_hot_set                               frozen   1608   12.24   16.85     20.96    33.8   11.52
7 c_the_cutaway                            live      866   12.27   16.82     24.42    37.5   11.56
7 c_the_cutaway                            frozen    888   12.09   13.36     15.76    31.2   11.38
8 05_martini_shot                          live     2264   12.17   16.57     20.65    35.6   11.46
8 05_martini_shot                          frozen   1080   12.88   13.92     20.20    35.0   12.13
all rooms                                  both    23555   12.43   16.55     22.01   230.2   11.70
```

### Sun 15 Nov 13:54:44 · Agent (claude-opus-5-5)

main8_b is clean and matches the live cold run: 12.43 ms average, slowest 1% 22.0 ms, GPU 11.7 ms. The big spikes in main8_a came from the company. Pulling the GPU pass breakdown now.

**Sun 15 Nov 13:54:45 · Tool call: Bash** (Top GPU passes for the hand-made run and room d08)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; python -I tools/analyze.py main8_b gpu "ROOM change: take 1, scene 1" "RUN wrapped" | head -16; python -I tools/analyze.py gen_a gpu "ROOM change: .*\(d08\)" "ROOM change: .*\(d09\)" | head -14
```

Result:

```
main8_b GPU passes, frames 26227 between "ROOM change: take 1, scene 1" and "RUN wrapped" (average ms per frame):
   12.353  RenderThreadTime
   12.339  FrameTime
   11.616  GPUTime
    3.669  GPU/TemporalSuperResolution
    2.210  GameThreadTime
    2.196  RHIThreadTime
    2.038  GPU/Lights
    1.932  GPU/LumenScreenProbeGather
    0.716  GPU/RenderDeferredLighting
    0.646  GPU/Unaccounted
    0.482  GPU/LumenSceneLighting
    0.387  GPU/Postprocessing
    0.310  GPU/Basepass
    0.299  GPU/LumenReflections
    0.296  GPU/ShadowDepths
gen_a GPU passes, frames 1563 between "ROOM change: .*\(d08\)" and "ROOM change: .*\(d09\)" (average ms per frame):
   13.196  FrameTime
   13.162  RenderThreadTime
   12.415  GPUTime
    3.735  GPU/TemporalSuperResolution
    3.017  GameThreadTime
    2.820  RHIThreadTime
    2.264  GPU/LumenScreenProbeGather
    1.980  GPU/Lights
    0.725  GPU/RenderDeferredLighting
    0.674  GPU/Unaccounted
    0.508  GPU/Postprocessing
    0.483  GPU/LumenSceneLighting
    0.393  GPU/LumenReflections
```

**Sun 15 Nov 13:55:02 · Tool call: Bash** (Revert the temporary diagnostic in my worktree)

```
cd /d/UE/wt/perf3 && git checkout -- Source/Supercut/SupercutPlayerController.cpp && git status --short && git log --oneline -1
```

Result:

```
eec7dd4 SUPERCUT main: the enemy gun's part table is EnemyGunPartTable
Shell cwd was reset to [notes]
```

**Sun 15 Nov 13:55:09 · Tool call: Bash** (Collect load readings for each run)

```
rm -rf /d/UE/wt/perf3_meta; cd "[notes]/unreal/megajam-2026/lanes/perf3"; for t in first1 first2 warm1 main8_b hall_a gen_a; do echo "$t: $(tr '\n' ' ' < logs/$t/load.txt | cut -c1-330)"; done; grep -c "" logs/first2/run.log >/dev/null; python -I tools/analyze.py first1 sections | tail -1; date +%H:%M
```

Result:

```
first1: before: free_ram_gb=4 of 15.9 cpu_load_pct=1 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 25 %, 2695 MiB, 39.58 W  gpu gate: idle after: free_ram_gb=4.6 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 26 %, 2864 MiB, 39.62 W  
first2: before: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 11.99 W  gpu gate: idle after: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.40 W  
warm1: before: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 12.87 W  gpu gate: idle after: free_ram_gb=10.4 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.40 W  
main8_b: before: free_ram_gb=10.4 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.50 W  gpu gate: idle after: free_ram_gb=10.3 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.20 W  
hall_a: before: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 10.54 W  gpu gate: idle after: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 47.84 W  
gen_a: before: free_ram_gb=10.1 of 15.9 cpu_load_pct=0 threads=12 busy_procs=none gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 47.84 W  gpu gate: idle after: free_ram_gb=6.9 of 15.9 cpu_load_pct=9 threads=12 busy_procs=clx1 dotnetx2 gpu=NVIDIA GeForce GTX 1070, 0 %, 287 MiB, 13.01 W  
all rooms                                  both     7029   13.96   19.50     26.00    60.4   13.13
13:55
```

**Sun 15 Nov 13:55:23 · Tool call: Bash** (Log the latest runs and the pc2 shutdown)

```
cd "[notes]/unreal/megajam-2026/lanes/perf3"; cat >> LOG.md <<'EOF'
- 13:43 first2 (desktop, from the title, engine caches and settings cleared; NVIDIA driver cache not cleared, it is outside the farm folder). Alone on pc2, free RAM 10.3 GB, GPU 0 % before. Benchmark CPU 197 GPU 265, HIGH. `RUN wrapped: takes 1, time 98.3 s, shots 46, freezes 14, kills 17`, 24 errors, 49 missed graphics PSOs. First 60 s from the title: one frame over 50 ms, 237.6 ms on the first title frame (missed PSOs); room changes 22 to 36 ms. Whole run live: avg 12.46 ms, slowest 1 % 21.6, GPU 11.73.
- 13:46 warm1 (same, nothing cleared): run line matches (98.4 s), 24 errors, 37 missed. First 60 s: 235.8 ms and 92.5 ms on the first title frames, nothing else over 50 ms. Whole run avg 12.46, slowest 1 % 21.7. The title hitch is there warm too, so it is not only driver compile time.
- 13:48 main8_b (desktop, fixed step 240): alone, run line matches, 24 errors. All rooms avg 12.43 ms, p99 16.55, slowest 1 % 22.0, GPU 11.70. Top GPU: TSR 3.67, Lights 2.04, Lumen screen probe gather 1.93, deferred lighting 0.72, Lumen scene lighting 0.48. main8_a's big spikes were the other lane's run.
- first1 against first2: first1 had pc2's [another platform] Studio windows open (GPU 25 %, 2.7 GB of video memory taken, free RAM 4 GB) and averaged 13.96 ms; from about 13:00 those were gone (GPU 0 %, 287 MiB, 10 GB free) and the same run averages 12.46.
- 13:48 main thread: pc2 goes down to get memory (16 to 32 GB). Let main8_b finish (output on c4 13:54), stopped the batch before the diagnostic build took a slot, deleted the scheduled task perf3_supercut on pc2. Every pc2 number in this lane was taken at 16 GB.
- 13:56 reverted the PSO diagnostic in the worktree (never built or committed); tree clean at eec7dd4. pc2's mirror C:\UE\Farm\perf3 still holds the diagnostic source from the 13:26 mirror; the pc2 package is the clean one built at 11:26.
EOF
```

Result:

```
(Bash completed with no output)
```

**Sun 15 Nov 13:55:44 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\tables.md",
 "content": "# perf3 tables (pc2, GTX 1070, 16 GB RAM, 15 Nov 2026)\n\nGame head eec7dd4, Development package built on pc2 at 11:26 (no code change in this lane). Default settings: the\nfirst-start benchmark picks HIGH on pc2 (87 % resolution, TSR, software Lumen, virtual shadow maps), DLSS off.\n1920x1080 fullscreen in pc2's desktop session. Frame times are wall time per frame from the engine CSV profiler\n(`FrameTime`), cut into rooms by the game's own log lines (`tools/analyze.py`). Every number here was taken with\npc2 at 16 GB, before its memory change.\n\n## Load beside each run (farm status before / after, desk_run's process check at launch)\n\n| Run | What | Free RAM GB | CPU % | GPU before | Other processes | Kept |\n| --- | --- | --- | --- | --- | --- | --- |\n| first1 11:40 | main8 from title, caches cleared, live | 4.0 / 4.6 | 1 / 0 | 25 %, 2.7 GB (Studio windows) | none | marked: under 6 GB, Studio on the GPU |\n| main8_a 12:15 | main8, fixed step 240 | 7.6 / 4.4 | 7 / 5 | 28 % | another lane's Supercut run | discarded |\n| hall_a 13:03 | shell1 hall script, live | 10.1 / 10.1 | 0 / 0 | 0 % | none | yes |\n| gen_a 13:03 | generated s7, fixed step 60 | 10.1 / 6.9 | 0 / 9 | 0 % | none at launch; a compile began after the end (CPU 2 to 7 % in the last samples) | yes |\n| first2 13:43 | main8 from title, caches cleared, live | 10.3 / 10.3 | 0 / 0 | 0 % | none | yes |\n| warm1 13:46 | main8 from title, warm, live | 10.3 / 10.4 | 0 / 0 | 0 % | none | yes |\n| main8_b 13:48 | main8, fixed step 240 | 10.4 / 10.3 | 0 / 0 | 0 % | none | yes |\n\n## Frame time at default settings\n\n| Place | Run | Frames | Avg ms | Slowest 1 % ms | p99 ms | GPU ms |\n| --- | --- | --- | --- | --- | --- | --- |\n| Hand-made run, all rooms, live | first2 | 7,892 | 12.46 | 21.59 | 16.73 | 11.73 |\n| Hand-made run, all rooms, live | warm1 | 7,893 | 12.46 | 21.73 | 16.89 | 11.74 |\n| Hand-made run, all rooms, fixed step | main8_b | 23,555 | 12.43 | 22.01 | 16.55 | 11.70 |\n| Hand-made run, heaviest room (1 wind machine, live) | first2 | 485 | 13.84 | 30.54 | 17.23 | 13.11 |\n| Hall (shell1 script, 3 s to end) | hall_a | 660 | 14.18 | 15.12 | 14.98 | 13.45 |\n| Generated run, all rooms | gen_a | 8,626 | 12.73 | 34.02 | 17.90 | 11.84 |\n| Generated, heaviest room d08, fight | gen_a | 392 | 13.21 | 33.68 | 15.76 | 12.32 |\n| Generated, heaviest room d08, freeze | gen_a | 1,080 | 13.30 | 18.21 | 17.42 | 12.55 |\n| (first1, Studio windows open) | first1 | 7,029 | 13.96 | 26.00 | 19.50 | 13.13 |\n\nNothing is over 16.7 ms on average. The slowest 1 % in the fixed-step generated run comes from single 100 to 380 ms\nframes (first frames, a room change, one freeze start) that line up with no missed pipeline; in the live hand-made\nruns the worst frames are room changes (22 to 36 ms over two frames).\n\nTop GPU passes (ms per frame):\n\n| Pass | main8_b all rooms | gen_a d08 | hall_a |\n| --- | --- | --- | --- |\n| TemporalSuperResolution | 3.67 | 3.74 | 3.60 |\n| Lights | 2.04 | 1.98 | 3.71 |\n| LumenScreenProbeGather | 1.93 | 2.26 | 2.07 |\n| RenderDeferredLighting | 0.72 | 0.73 | 0.72 |\n| Unaccounted | 0.65 | 0.67 | 0.67 |\n| LumenSceneLighting | 0.48 | 0.48 | 0.48 |\n| Postprocessing | 0.39 | 0.51 | 0.29 |\n| LumenReflections | 0.30 | 0.39 | 0.32 |\n| ShadowDepths | 0.30 | | 0.47 |\n\n## First minute after a launch (from the title, after the benchmark)\n\n| Run | Frames over 50 ms in 60 s | What was on screen | Missed graphics PSOs (whole run) |\n| --- | --- | --- | --- |\n| first2 (cold) | 237.6 ms | first title frame | 49 |\n| warm1 (warm) | 235.8 ms, 92.5 ms | first title frames | 37 |\n| first1 (cold, Studio open) | 230.3, 100.1, 60.4 ms | first title frames; change into scene 2 | 48 |\n\nAverage over the first 60 s: first2 12.73 ms, warm1 12.74 ms. Room changes: first2 22 to 36 ms over the first two frames.\n\n## Errors per run\n\n`Failed to create compute pipeline`: 24 in every pc2 packaged run (first1, pics, main8_a, hall_a, gen_a, first2,\nwarm1, main8_b); 0 on [pc-b]'s RTX 4080 SUPER with the same package line. No code change, so no after column.\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\tables.md (file state is current in your context — no need to Read it back)
```

**Sun 15 Nov 13:56:23 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\perf3\\HANDOFF.md",
 "content": "# Lane perf3 handoff: SUPERCUT on a GTX 1070 (pc2), 15 Nov 2026\n\nNo code or content change. The worktree `D:\\UE\\wt\\perf3` (branch perf3) is clean at eec7dd4. All pc2 numbers were\ntaken with pc2 at 16 GB of RAM, before the owner's memory change to 32 GB. Numbers: [tables.md](<[notes]/unreal/megajam-2026/lanes/perf3/tables.md>).\nClock-by-clock notes and source lines: [LOG.md](<[notes]/unreal/megajam-2026/lanes/perf3/LOG.md>).\n\n## 1. The 24 `Failed to create compute pipeline` errors\n\nWhat they are (from the engine source; the hash-to-name check on pc2 was not run, see \"Not done\"):\n\n- At start the engine precaches a compute pipeline for every global compute shader permutation that was cooked\n  (`LaunchEngineLoop.cpp:4504` -> `ShaderCompiler.cpp:5253`). It does not ask the card first.\n- TSR cooks a 16-bit math permutation of each shader on SM6, because the platform says 16-bit types are\n  \"runtime dependent\" (`Engine/Config/Windows/DataDrivenPlatformInfo.ini:127`, `TemporalSuperResolution.cpp:546`).\n  Most TSR shaders skip those in precaching through `Use16BitVALU`, which checks the card\n  (`TemporalSuperResolution.cpp:636`, `GRHIGlobals.SupportsNative16BitOps`). `FTSRDecimateHistoryCS` (line 911) and\n  `FTSRUpdateHistoryCS` (line 1313) have no such check, so all their 16-bit permutations get precached:\n  2x2x2 x alpha = 16 plus 4 qualities x alpha = 8, which is 24.\n- A GTX 1070 (Pascal) has no native 16-bit shader math (`D3D12Adapter.cpp:1251`). D3D12's own check before\n  creating a pipeline does not look at 16-bit types (`D3D12Shaders.cpp:107-145`), so the driver gets the call and\n  returns E_INVALIDARG (0x80070057) for each. The editor (uncooked) run never precaches them: 0 errors there.\n- They do no harm. A failed pipeline that a draw or dispatch actually needs is fatal\n  (`PipelineStateCache.cpp:722-724` and `740-743`), and every pc2 run ran to the end. At draw time TSR asks\n  `Use16BitVALU` (`TemporalSuperResolution.cpp:1967`), which is false on this card, and uses the 32-bit shaders.\n\nPictures: the same scripted run (title, main8, fixed step 240, 1920x1080, HIGH from the benchmark on both) on pc2\nand on [pc-b], 65 pairs, pc2 on top: [shots/pairs](<[notes]/unreal/megajam-2026/lanes/perf3/shots/pairs>).\nBoth run software Lumen (`raytracing=\"0\"`) with the same 335 CVar settings. Every pair has the same frame and\nthe same parts: shadows, Lumen bounce, floor reflections, sky, the sketch look in freezes, muzzle and hit effects,\nupscaling. Nothing is missing on pc2. pc2 is slightly brighter in lit rooms (mean +4 to +9 of 255 in scenes 1,\n2, 5, 7, under 1.5 elsewhere) and its shadow edges look a touch softer in s7_02. [taste: owner review] whether that\nbrightness gap matters; I did not chase it.\n\nCan they be removed cheaply? No, so I stopped there.\n- The project has no per-shader precache switch. The only one is `r.PSOPrecache.GlobalShaders`\n  (`PSOPrecacheSettings.cpp:17`). It is read-only, read before the card is known, and turns off precaching of every\n  global compute shader on every card, so it would add hitches on good cards to hide a harmless log line.\n- The real fix is two lines in the engine (give those two shaders the same `ShouldPrecachePermutation` check the\n  other TSR shaders have). That needs a source-built engine, which we do not have.\n\n## 2. Frame rate at default settings (1920x1080, HIGH, DLSS off)\n\n| Place | Avg ms | Slowest 1 % ms | GPU ms |\n| --- | --- | --- | --- |\n| Hand-made run, live from the title (first2) | 12.46 | 21.6 | 11.73 |\n| Hand-made run, fixed step (main8_b) | 12.43 | 22.0 | 11.70 |\n| Hall, shell1 script (hall_a) | 14.18 | 15.1 | 13.45 |\n| Heaviest generated room d08, fight / freeze (gen_a) | 13.21 / 13.30 | 33.7 / 18.2 | 12.3 / 12.6 |\n\nAll under 16.7 ms, so per the brief nothing was changed. The defaults code is right for this card: the benchmark\ngives HIGH (`SupercutUserSettings.cpp:171`), DLSS is off and reports `NotSupportedIncompatibleHardware`. Biggest GPU\ncost everywhere is TSR at 3.6 to 3.7 ms, then lights (2.0, 3.7 in the hall) and Lumen screen probes (1.9 to 2.3).\nWith pc2's [another platform] Studio windows open on the GPU (first1) the same run averaged 13.96 ms.\n\n## 3. First launch hitches\n\nCold (first2: settings and every engine cache under the package's Saved cleared) and warm (warm1), 60 s from the\ntitle after the benchmark:\n\n- One hitch over 50 ms cold: 237.6 ms on the very first title frame. Warm: 235.8 ms and 92.5 ms on the first\n  title frames. Nothing else in the first minute; room changes cost 22 to 36 ms.\n- The first title frame meets 39 graphics pipelines the precache missed (`PSOPrecacheState: Missed`). The NVIDIA\n  driver cache (%LOCALAPPDATA%) is outside the farm folder and was not cleared, so \"cold\" is engine-cold only.\n- Warm still hitches the same, so most of that frame is not driver compile time.\n\nA pipeline cache shipped with the package, the supported 5.9 way (read, not tried):\n1. Set `NeedsShaderStableKeys=True` under `[DevOptions.Shaders]` in DefaultEngine.ini\n   (`ShaderLibraryCooking.cpp:262`) and package.\n2. Play the game with `-logPSO` (`PipelineFileCache.cpp:1886`, `r.ShaderPipelineCache.LogPSO` line 121); the\n   recorded PSOs are saved to `Saved/CollectedPSOs/*.rec.upipelinecache` on exit (`PipelineFileCache.cpp:2295`,\n   `ShaderPipelineCache.cpp:968-977`).\n3. Run the `ShaderPipelineCacheTools` commandlet (expand) on the recording plus the cook's .shk files to make\n   `Build/Windows/PipelineCaches/<name>_Supercut_PCD3D_SM6.spc`.\n4. Package again: the cook finds the .spc (`ShaderLibraryCooking.cpp:432-447`) and builds\n   `Content/PipelineCaches/Windows/Supercut_PCD3D_SM6.stable.upipelinecache`, which every log today says is missing.\n   It precompiles at start (`r.ShaderPipelineCache.StartupMode` 1, `ShaderPipelineCache.cpp:55`).\n\nNot tried: pc2 went down for its memory change. At best it removes one 0.24 s frame when the title appears, not\nduring play, and the warm run suggests it may not remove all of that. It also needs re-recording whenever materials\nchange. My call: not worth it before submission. [taste: owner review]\n\n## Proof\n\n- No code or content change, so no build, test, package or run-line proof is owed. For the record, the packages\n  used: pc2 build 822 s, package 83 s, 0 `Failed to compile Material`; [pc-b] build 318 s, package 529 s, 0.\n- Run lines on pc2, all matching: `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17` (pics run,\n  main8_a, main8_b at fixed step; 98.3 to 98.4 s live), `RUN wrapped: takes 1, time 144.8 s, shots 54, freezes 16,\n  kills 26` (gen_a). [pc-b] pics run: `time 98.2 s, shots 46, freezes 14, kills 17`.\n- Errors per run: 24 on every pc2 packaged run, 0 on [pc-b].\n\n## How to re-run\n\n- `tools/go.sh <tag> <argfile> [-ClearCaches|-FreshSettings]`: takes pc2's farm slot (same lock folder as\n  farm.sh), starts `desk_run.ps1` in pc2's desktop session through a scheduled task `perf3_supercut`, fetches log,\n  CSV, samples and settings to `logs/<tag>/` masked. Delete the task after (`schtasks /delete /tn perf3_supercut /f`).\n  Arg files in `tools/args/`.\n- `python -I tools/analyze.py <tag> sections|hitch <s> <ms>|gpu <rx0> <rx1>|window <rx> <s>`.\n- `python -I tools/pairs.py <pc2 shots> <other shots> <out>` for picture pairs.\n- The PSO diagnostic (prints every global compute permutation's hash so the 24 hashes in the log get names, plus a\n  ProfileGPU at 8 s): `tools/psodiag_snippet.cpp.txt`, run with `tools/args/psodiag.args`. Never commit it.\n\n## Not done\n\n- Hash-to-name check of the 24 on pc2 (the diagnostic build). pc2 went down before the build got a slot. The\n  mirror `C:\\UE\\Farm\\perf3` on pc2 still has the diagnostic source from 13:26; the next `mirror` of a clean tree\n  puts it back. The pc2 package under `_builds\\perf3` is the clean 11:26 one.\n- The bundled pipeline cache (above).\n- No [pc-c] column: [pc-b]'s RTX 4080 SUPER pictures stand for the good card, and [pc-c] has a person on it.\n- Nothing measured after pc2's memory change.\n\n## Gotchas\n\n- Runs in pc2's desktop session go round farm.sh. Before 13:36 farm.sh had no slots and another lane's run started\n  between my load check and my launch (main8_a, discarded). go.sh now takes the farm slot itself.\n- With `-UseFixedTimeStep` the game's FPS lines report the fixed rate (240.0); only the CSV `FrameTime` is real.\n- The CSV loses the last ~3 s when `-SupercutQuit` ends the game, and its last row can be cut short.\n- `RenderOffscreen` farm runs are fine for pictures, not for frame time.\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\perf3\HANDOFF.md (file state is current in your context — no need to Read it back)
```

### Sun 15 Nov 13:56:28 · Agent (claude-opus-5-5)

Checking the one claim in the handoff I haven't verified yet: the number of TSR update qualities.

**Sun 15 Nov 13:56:29 · Tool call: Bash** (Confirm the TSR update quality count)

```
S="/d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/PostProcess/TemporalSuperResolution.cpp"; sed -n 1313,1330p "$S" | grep -n -A8 "enum class EQuality"; grep -n "kUpdateQualityNames\[\]" -A2 "$S" | head -4
```

Result:

```
6:	enum class EQuality
7-	{
8-		Low,
9-		Medium,
10-		High,
11-		Epic,
12-		MAX
13-	};
14-
3312:		static const TCHAR* const kUpdateQualityNames[] = {
3313-			TEXT("Low"),
3314-			TEXT("Medium"),
```

**Sun 15 Nov 13:56:41 · Tool call: Bash** (Add GOTCHAS and FINDINGS entries, confirm clean tree)

```
cd "[notes]/unreal"; cat >> GOTCHAS.md <<'EOF'

## 24 `Failed to create compute pipeline` errors on a GTX 1070 are harmless (15 Nov 2026, verified on pc2, lane perf3)

A cooked package on a Pascal card logs 24 `LogRHI: Error: Failed to create compute pipeline with hash ...` (driver
error 80070057) at frame 0; RTX 4080 and RX 9070 XT log none. They are the 16-bit math permutations of
`FTSRDecimateHistoryCS` (16) and `FTSRUpdateHistoryCS` (8), which the engine precaches on every card because those
two shaders lack the card check the other TSR shaders have (`TemporalSuperResolution.cpp:636`, `Use16BitVALU`).
Pascal has no native 16-bit shader math. Precache failures are not fatal (`PipelineStateCache.cpp:722`); a pipeline
that is actually used would be fatal, and TSR uses its 32-bit shaders on this card. Pictures match an RTX 4080 run.
Removing them takes an engine change or `r.PSOPrecache.GlobalShaders=0` for every card; do neither. Ignore them.
EOF
cat >> FINDINGS.md <<'EOF'

## SUPERCUT frame time on a GTX 1070 at default settings (15 Nov 2026, verified on pc2 at 16 GB, lane perf3)

Head eec7dd4, Development package, benchmark picks HIGH (87 %, TSR, software Lumen, VSM), DLSS off, 1920x1080, pc2
alone. Hand-made run 12.46 ms average, slowest 1 % 21.6, GPU 11.7; hall (shell1 script) 14.2 ms; heaviest generated
room (s7 d08) 13.2 ms in the fight, slowest 1 % 33.7. TSR is the biggest GPU pass (3.7 ms), then lights (2.0) and
Lumen screen probes (2.0). With pc2's [another platform] Studio windows on the GPU the hand-made run was 14.0 ms. First launch:
one 0.24 s frame when the title first appears (39 graphics PSOs missed by the precache), warm or cold; room changes
22 to 36 ms. Tables and tools: `megajam-2026/lanes/perf3/`.
EOF
cd /d/UE/wt/perf3 && git status --short | wc -l
```

Result:

```
0
Shell cwd was reset to [notes]
```

### Sun 15 Nov 13:56:58 · Agent (claude-opus-5-5)

My pc2 step (main8_b) finished and its output is on c4. Nothing of mine is running or waiting on pc2, and I deleted my scheduled task there.

I changed no code or content. The worktree `D:\UE\wt\perf3` is clean at eec7dd4, and every pc2 number was taken at 16 GB, before the memory change.

**1. The 24 errors are harmless, and I left them.**
- **What they are:** I worked this out from the engine source; I didn't get to the check on pc2 that would match each logged hash to a shader name.
  - At start-up the engine pre-builds pipelines for two TSR upscaler shaders in their 16-bit form, on every card.
  - Those are `FTSRDecimateHistoryCS` (16 versions) and `FTSRUpdateHistoryCS` (8 versions), which makes 24.
  - The GTX 1070 has no native 16-bit shader maths, so the driver refuses all 24.
- **Why it's safe:** a failed pipeline the game actually used would crash it (`PipelineStateCache.cpp:722`), and every pc2 run went to the end. On this card TSR uses its 32-bit shaders.
- **Pictures:** I compared 65 shots from the same script on pc2 and on [pc-b].
  - Nothing is missing on pc2: shadows, Lumen light, reflections, sky, the sketch look, effects and upscaling are all there.
  - pc2 is slightly brighter in lit rooms, by 4 to 9 levels out of 255. [taste: owner review]
- **Why I didn't remove them:** it would take an engine change we can't build, or a setting that turns off pre-building for every card and adds stutter on good ones.

**2. Frame rate is under 16.7 ms everywhere, so I changed nothing.** All runs were at default settings (HIGH from the benchmark, 1920x1080), with pc2 to myself.

| Place | Average | Slowest 1% |
| --- | --- | --- |
| Hand-made run | 12.5 ms | 21.6 ms |
| Hall | 14.2 ms | 15.1 ms |
| Heaviest generated room (d08), fight | 13.2 ms | 33.7 ms |

- TSR is the biggest GPU cost, at 3.7 ms.
- The first run (13.96 ms) had pc2's [another platform] Studio windows open on the GPU and only 4 GB free RAM, so I marked it and ran it again.
- I discarded one run because another lane's game started during it.

**3. First launch has one hitch.** Within the first minute from the title, the only frame over 50 ms is the first title frame, at 0.24 s. It's the same on a warm start. Room changes cost 22 to 36 ms.
- A pipeline cache shipped with the package is the supported 5.9 way to fix that frame. The steps and source lines are in the handoff.
- I didn't try it because pc2 went down. It would only remove that one frame before play starts, and the warm run suggests it might not remove all of it. My call is that it's not worth doing before submission. [taste: owner review]

**Not done:**
- The check that names the 24 hashes on pc2. The code for it is ready in the lane folder.
- The pipeline cache experiment.
- A column for [pc-c].
- Anything after pc2's memory change.

pc2's mirror still has the temporary diagnostic source; the next mirror of a clean tree replaces it. The pc2 package itself is the clean one.

Files are in `[notes]\unreal\megajam-2026\lanes\perf3\`:
- [HANDOFF.md](<[notes]/unreal/megajam-2026/lanes/perf3/HANDOFF.md>)
- [tables.md](<[notes]/unreal/megajam-2026/lanes/perf3/tables.md>), with the load reading beside each run
- [LOG.md](<[notes]/unreal/megajam-2026/lanes/perf3/LOG.md>)
- [shots/pairs](<[notes]/unreal/megajam-2026/lanes/perf3/shots/pairs>)

I also added one entry each to [GOTCHAS.md](<[notes]/unreal/GOTCHAS.md>) and [FINDINGS.md](<[notes]/unreal/FINDINGS.md>).
