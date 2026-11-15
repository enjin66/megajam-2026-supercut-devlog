# Dev log

Times are Singapore time. The agent sessions behind each entry are in `transcripts/`.

## Fri 13 Nov 2026

### 05:41. Starting again

The first day of the jam went to a different game: a flood-night dispatch game with the working
title Floodline. It reached a packaged build that played a full night. At 05:41 the owner called
it off. They have a clearer idea of what they want to make, and we start from scratch.

Nothing from Floodline goes into the new game: no code, no art, no sound, no data. Its project,
builds and sound files were moved into a folder named `_scrapped_floodline` on both PCs, so no
agent can copy from them by accident. What we keep is what we learned about the engine: how to
build from the command line, how to package, which traps cost us time.

### 05:42. Logging everything

The owner's instruction: log everything from this point so the entry can go in for Glass Box.

What we set up in the next twenty minutes:

- This repo. It is private. Only the owner decides who else sees it.
- A script that exports every agent session into `transcripts/`: what the owner typed, what the
  agent answered, every tool call and its result. The raw session files hold the studio's
  private notes on other projects, so the script strips those and replaces emails, IP addresses,
  account names and the jam's registered-only codes with tags. The README lists every cut.
- A rule for helper agents: every brief carries a marker line, and the export picks up any
  session whose first prompt has it. No helper's work can go unlogged because someone forgot
  to list it.

First thing the export caught: the agent's own inspection commands had listed the names of
unrelated work threads on this PC. Those results are now withheld too.

Not yet covered: sessions run by models from other providers (GPT, Gemini). Their briefs and
final reports already appear in the orchestrator's transcript. Their own step-by-step sessions
get an exporter the first time one is used on this game.

### 06:03. The game is SUPERCUT

The owner's pitch, in their words: "a roguelite puzzle FPS game ... you have guns and a clapperboard
with limited charges. every time you use your clapperboard, you can freeze time for X amount of
seconds." Light puzzles sit beside the fights: freeze a giant turbine to get past it, or find glyphs
that only show in frozen time. Then they asked the agent a straight question: is this a good idea?

The agent's answer was yes, with three changes it argued for:

- **The freeze has to be more than a pause button.** If frozen enemies cannot hurt you and you can
  shoot them freely, every fight is solved the same way. The agent's proposal: shots fired in frozen
  time hang in the air a metre from the gun and all fly when time resumes. You stop the scene, set
  up the shot, and let it play. That is also the theme said out loud: the director stages the take.
- **Keep the roguelite part thin.** A judge plays for about ten minutes. So: one run of about eight
  hand-built rooms, pick one of three upgrades between rooms, death restarts the run as the next
  take. No progress between runs and no generated rooms.
- **Three puzzle ideas, each used twice.** Stop the machine, glyphs that show only in frozen time,
  and stand on what you froze.

These are written into the spec as the agent's picks, each marked so the owner can overrule it.

A name check found one small student jam game called SUPERCUT on itch.io from 2022 and no Steam
listing. Good enough for a jam.

### 06:06. First helper agent: the core

One helper agent starts on the part that every version of this game needs: a new Unreal project,
first-person movement, the clapperboard freeze, a revolver whose shots hang in frozen time, one
enemy that fires slow shots, and a test room with a spinning blade to freeze and walk past. Its
brief is in the orchestrator's transcript, word for word. Room design, art and sound wait until the
freeze is proven to feel right.

### 06:15. Should we be on the 5.9 preview?

The owner had watched Epic's kickoff stream and came away thinking we should be on the Unreal Engine
5.9 MegaJam Preview, with some tools switched on that the stream talks about. We build on 5.8.4.

The agent read the stream's captions for the setup half (minutes 28 to 45), pulled frames to read
the plugin names off the presenter's screen, and compared them with the engine installed here.

- The presenter ticks two plugins, Unreal MCP and MCP Client Toolset, and names a third, All
  Toolsets. All three ship in our 5.8.4 install.
- What 5.9 has that 5.8.4 lacks: a project setting holding instructions the agent reads on connect,
  an assistant panel inside the editor, and two "Unreal Canvas" plugins the presenter left off.
  Our agents already get their instructions from files and briefs, and they work from outside the
  editor.
- Neither the stream nor the official rules require 5.9. The rules name no engine version.

The agent's advice: stay on 5.8.4. Epic's own post says the preview had about a week of development
and a short test pass, our build, test and package commands are proven on 5.8.4, and a helper agent
is already building the core there. The one reason to switch would be a web build, which only the
preview supports.

### 06:40. The owner pushes back, and is right to

The agent's summary of the stream had one line it had not checked: the presenter says more of the
editor can be scripted from Python in 5.9. The owner quoted that line back: isn't this the
important part?

It is. How far an agent can reach inside the editor decides how good the levels, materials and
effects can get in three days. So the agent measured instead of arguing:

- Epic's preview post claims "expanded Python APIs covering audio, MetaSounds, modeling, physics,
  Niagara, materials, PCG, networking, and UI", and new toolsets for geometry, audio, level creation
  and gameplay testing. The 5.9 docs give agents a tool to run their own Python inside the editor.
- A listing of our 5.8.4 install shows Python toolsets for Blueprints, materials, assets, meshes,
  scenes and Niagara. It shows no tool for running Python through the agent connection, and no
  geometry or audio toolsets.

So the gap is real, and the agent's first answer ("stay on 5.8.4") rested on a claim it had not
tested. What is still unknown is whether the preview is stable enough to ship from. Epic says it
had a week of development and a short test pass.

Decision: install 5.9 beside 5.8.4 now, list both sets of tools side by side, and package the core
of the game on both. Move only if the preview packages cleanly. A second helper agent is driving
the Epic Games Launcher to do the install; it stops at any licence prompt for a person to click.

### 07:20. The preview is installed, and the two engines differ more than expected

The install took fifteen minutes once it started in the right place. The first attempt began
downloading into the wrong folder before the helper agent had set a location; it cancelled, cleaned
up 5 GB of partial download and started again. No licence prompt appeared. It did click through
Epic's own warning that the preview "has not been fully tested and may be unstable".

With both engines on disk the agent compared their folders. The preview has 65 plugins for agent
tools against 35 in 5.8.4. The new ones are close to a shopping list for this game: geometry,
navigation mesh, input, MetaSound, scene capture, console. One thing went the other way. The
ready-made Python tools shrank from about 600 to about 130, and a new module lets the agent run
its own Python in the editor. So 5.9 seems to trade a long menu of fixed tools for one open door.

Counting files does not tell us whether that door works, or whether the preview can package a game
on this PC. A third helper agent is finding out on two throwaway projects: build and package a C++
project on 5.9, list every tool in both engines, and try real jobs through the Python route (build
a room, make a material, start the game and take a picture). The game itself stays on 5.8.4 until
that report is in.

### 07:30. The log nearly leaked an account name

Before sending the last entry to GitHub the agent read the new transcript by eye. The automatic
scan had passed it. Line 818 held the signed-in Epic account's display name.

How it got there: the helper that installed the preview had read the Epic Games Launcher's own log
file to see why a download stalled, and the Launcher writes pieces of its interface into that log,
account name included. The scan only knows words on its list, and nobody had put that name on it.

The commit was still local, so nothing had left the PC. Three fixes, in order of how much they matter:

- The exporter now withholds the result of any call that reads the Launcher's saved files, the same
  way it withholds results from the studio's private notes.
- It also withholds the result of every call that reads the screen (89 of them in that one
  transcript). A screen dump can hold anything, and no word list can know it in advance. The call
  itself stays in the transcript, so a reader still sees where the agent looked and clicked.
- The name went on the word list, and the local commit was thrown away and rebuilt.

The agent's first guess at the cause was wrong. It assumed the name came from a screen dump and
fixed that first. Tracing the hit back to its tool call showed it came from a log file read with
an ordinary shell command, which the screen fix would not have caught.

### 07:45. The freeze works

The first helper agent reported after an hour and forty minutes: a new C++ project, 3,200 lines,
three commits, a packaged Windows build. It claimed five proofs. The orchestrating agent does not
take a helper's word for it, so it re-ran two of them and looked at the pictures itself.

- Seven of seven automated tests pass, run again by the orchestrator. They cover the rules that
  matter: charges go 3, 2, 1, 0; a freeze ends at four seconds or on a second press; a frozen enemy
  shot holds still and cannot hurt; shots fired in frozen time hang, then fly and hit; the blade
  kills while spinning and not while frozen.
- The packaged game, run again with a scripted player, wrote this to its own log: six shots "hang
  100.0 cm from the muzzle", the freeze ends, six shots "fly on at 9000 cm/s", three enemies die.
  During the freeze the most any frozen thing moved was 0.0000 cm.
- The pictures show it. Start of the room in colour:

  ![The test room in colour](pictures/core/00_start.png)

  Frozen, with enemy shots stopped in the air:

  ![Frozen: the room goes grey, enemy shots hang](pictures/core/02_frozen_enemy_shots.png)

  Frozen, with six of the player's own shots placed and waiting:

  ![Six player shots hanging in frozen time](pictures/core/03_own_shots_hanging.png)

What the helper learned the hard way, in its words: "The freeze itself was the easy part." Stopping
time is one number per actor in Unreal. Making it look stopped took three tries. Draining colour
from the whole screen made the glowing shots go pale with everything else, and those shots are the
point of the game. Grading by brightness failed because a lit floor is as bright as a small glow.
What worked was turning walls and floors grey at the material and leaving the glows alone.

What is not proven: no person has played it. The helper is plain about that: "I can show that the
freeze is instant and that nothing moves during it, and I cannot yet say that it feels good." The
build is waiting for the owner to play. The helper also listed 37 judgement calls it made, each
with the option it turned down, for the owner to overrule.

One number to watch: the packaged folder is 1,001 MB and the jam's limit is a 1 GB zip. 348 MB of
that is a debug file that does not ship, so there is room, but not for carelessness.

### 07:55. Next helper: the run, and how rooms get made

With the freeze proven, the next question was how eight rooms get built in two and a half days.
The agent's call: a room is a text file. The game reads it when the room starts and builds the
walls, enemies and machines from it. Two reasons. An agent can write a room and test it without
compiling anything or opening the editor. And a scripted player can then prove that every room can
be finished, which matters for a game with puzzles in it. The choice also does not depend on which
engine version we end up on.

A fourth helper agent has that job, plus the rest of the run: going from room to room, a film can
that gives back one clapperboard charge, a pick of one from three upgrades between rooms, and death
sending you back to scene one as the next take. Its brief asks for nine upgrades that change how
you play and lean on what is special here (frozen time, hanging shots, charges), and for a page
called "How to write a room" that the room-building agents will work from.

Only one helper compiles at a time for now. This PC has 31 GB of memory and 2 GB free, and an
earlier compile already died from that.

### 08:45. The engine question is settled: we move to the 5.9 preview

The third helper agent came back with a 230-line report and a verdict: move, and move now, on a
copy. Its three reasons, each one tested and not read off a web page:

- 5.9 built, tested, packaged and ran a C++ project on this PC.
- Through the editor's agent connection, 5.9 lets an agent run its own Python, press keys in a
  running game and take a picture of what the player sees. 5.8.4 can do none of the three. The
  helper ran the same seven jobs on both engines: 5.9 finished all seven in about 30 calls, 5.8.4
  needed 61 and could not finish three (no sound import, no navigation mesh, no input to the game).
- The move is one way. The older editor refuses any file saved by the newer one.

A report on a throwaway project is not our game, so the orchestrating agent ran the real test: take
the proven core, copy it, point it at 5.9, and run the same checks as this morning.

It did not go smoothly. The first build died with the compiler crashing on every file. So did the
second attempt. So did the package step. The helper's report had described this exact failure and a
cure (delete one 2 GB file and build one file at a time). The cure worked once and then failed
again, which meant the helper's explanation was incomplete. Six of these files were written this
morning and four came out bad, with one job or several, with memory free or not. Then the agent
found the same crash, same compiler file and line, in the notes from the 5.8.4 build earlier. So it
is not the preview engine. It is this PC's compiler and a very large file, and the cause is still
not found. What we have is a build script that spots the crash, deletes the bad file and tries
again. A workaround, written down as one.

One wrong turn on the way: the agent tried switching off the engine's build accelerator to see if
that was the cause. The build passed. The log showed the switch had been ignored, so the pass
proved nothing. It would have been easy to write "fixed" at that point.

Once it compiled, the result was clean:

- Seven of seven tests pass on 5.9.
- The package step ends with zero errors and zero warnings.
- The packaged game's log matches the 5.8.4 one line for line: six shots hang, six fly, the player
  reaches the end. 268 frames a second.

  ![The same frozen moment, built with 5.9](pictures/ue59/03_own_shots_hanging_ue59.png)

One thing to carry forward. The very first launch of the fresh build stalled for about 17 seconds
while it compiled shaders, and then hung on exit. The second launch was perfect. A judge's first
launch is a first launch, so the game will need a warm-up screen before play starts.

Decision: SUPERCUT moves to 5.9. The port is three small files and the same source still builds on
5.8.4, which stays as the way back for as long as every asset is made by a script. The agent's
advice at 06:15 was to stay on 5.8.4. The owner's question at 06:40 is why that got tested, and the
test says the owner was right.

### 09:15. "Works on my machine" lasted twenty minutes

Right after the engine decision the agent sent a helper to run the 5.9 build on two other PCs in
the studio, one with a GTX 1070 and one with an RTX 2060. We had only ever run the game on the
PC that built it. The helper's report:

- **On both PCs the game never started.** The small launcher at the top of the build showed a box
  asking to install the Visual C++ runtime and waited for an answer. No log, no window, no game.
  The build PC has a newer runtime than the two test PCs, so it never showed the box. A judge who
  double-clicks the game and sees an "Error" box may not click Yes.
- **Started directly, the game ran on the GTX 1070, slowly.** 27 frames a second on the first run
  and 51 on the second, for a room made of grey boxes. The build PC does 268. The log also shows
  24 graphics programs failing to build on that card.
- **The RTX 2060 PC could not show anything.** Its graphics driver reports the card as lost until a
  restart. That is the PC's problem, not the game's, and restarting it is the owner's call because
  other work runs there.
- A trap for our own tests: a game that fails to open a graphics device still exits with code 0.

None of this showed up in seven passing tests and a clean run on the build PC. Fixes so far: the
build is repackaged with the runtime files placed beside the game and no installer. A second
helper is back on the GTX 1070 PC to check that the box is gone, and to switch the engine's costly
lighting features off one at a time to find what the frame rate is paying for.

### 09:45. The game has a run: three rooms, upgrades, a wrap screen

The second helper (Claude Fable 5.2, lane `run`) reported at 09:10 after about 75 minutes. What it
built, on top of the core:

- **Rooms are text files.** One file per room, one line per piece: a box, a lamp, a Grunt, a
  spinning blade, a moving platform, a strip of lava, a film can, the gate. The game reads the file
  when the room starts. A bad line stops the game with the file name, the line number and what is
  wrong. An agent can write a room and test it with no compile and no editor.
- **Room to room.** Reach the gate and the game pauses and offers 3 of 9 upgrades. Pick with a key
  or a click, then the next room is built in the same world (1 to 9 ms). After the last room, a
  wrap screen with takes, time, shots, freezes and kills.
- **Death is the next take.** Die and the run starts again at scene 1 as take 2, with no upgrades.
- **Nine upgrades**, each one entry in a table and each with a test: LONG TAKE, EXTRA REEL, SLOW
  BURN, DOUBLE EXPOSURE, STUNT DOUBLE, QUICK CHANGE, THROUGH LINE, REVERSE SHOT, ENCORE.
- **A film can pickup** that gives one clapperboard charge.

The helper worked on the 5.8.4 project because the engine decision came while it was mid-task. The
orchestrating agent merged its commits onto the 5.9 branch and ran the proofs again there itself:
the editor target builds, 24 of 24 tests pass, the package builds with the new command (runtime
files beside the game, no installer), and the packaged game plays the scripted three-room run to
the wrap screen: 6 kills, 5 freezes, 19 shots, two upgrades picked (one by key, one by click),
exit code 0, no error lines, 288 frames a second on the build PC. The numbers match the helper's
own run on 5.8.4.

![The upgrade screen after scene 1](pictures/run/18_upgrade_screen_1.png)
![Scene 2, frozen: the film can ahead, lava behind it, a Grunt at the gate](pictures/run/21_film_can_from_the_start.png)
![The wrap screen](pictures/run/38_wrap_screen.png)

What the helper says is not done, in its own words: "No person has played it." Every run so far
was a scripted player. The three rooms prove the flow and are not designed levels. Upgrade
strengths are first guesses. It also made calls the owner has not seen yet: health and revolver
rounds carry from room to room, lava kills in frozen time too, a held upgrade is never offered
again, and the upgrade screen has no heading.

Next: two more enemy kinds (a Rusher that runs at you, a Marksman that shows an aim line before one
fast shot), then the puzzle pieces, then the real rooms.

### 09:50. Two helpers at once: enemies, and sound made by code

The build PC can compile one thing at a time (it has 2 to 7 GB of memory free), so only one helper
may touch the C++. To use the waiting time, the second helper got a job that needs no compiler.

- **Lane `enemies`** (Claude Opus 5.5, high). The Rusher and the Marksman, with numbers from the
  orchestrating agent's brief: the Rusher runs faster than the player walks, stops at 4.5 m, crouches
  for 0.45 s, then lunges in a straight line it cannot change; the Marksman stands still, follows the
  player with a red line for 1.2 s, locks the line for 0.4 s, then fires one fast shot along it. Both
  are dodged the same way a person would guess: step sideways after the tell. The brief also asks for
  one shared enemy base first, with the old 24 tests proving the Grunt did not change, so that shots
  and upgrades stop knowing the Grunt by name.
- **Lane `sound`** (Claude Opus 5.5, high). About 45 sound effects as WAV files, every sample
  synthesised by Python code the helper writes: the clapperboard snap, the freeze and the resume, a
  bed for frozen time, the revolver, the three enemies, steps, screens. No sample packs, no
  recordings, no audio model, no paid service. `[agent's pick]` The owner had not chosen a sound tool;
  this choice keeps every sound made in the jam window by something we can show line by line. An
  agent cannot hear, so the brief makes it measure each file (attack time, where the energy sits,
  loudness against the other files, a click-free loop join) and say which sounds came out weak.

Model choice: the studio's rule sends motion and feel work to Fable and work with a clear spec to
Opus. Enemy behaviour sits between the two. The agent wrote the spec down to the numbers and sent
it to Opus, because the Fable allowance for the week is half gone and the look of the game, which
has no spec yet, needs it more.

### 10:05. The owner kept getting security prompts

The owner, back at the PC: Windows kept asking for permission "regarding Unreal" on two PCs, and
they did not want to keep clicking. The agent first assumed nothing and looked for the asker. The
firewall's own event log named it: each prompt was Windows Firewall asking about a new program
that had opened a listening port, and the programs were the engine's tools and every new copy of
our packaged game. Starting the game and listing its open ports showed one: TCP 1985, the engine's
trace control port, which every non-Shipping Unreal program opens. Each new build folder is a new
program path to Windows, so each test build raised a new prompt.

Two results. On the studio's PCs the firewall's prompt for new programs is now off (the firewall
itself stays on). For the jam: a Development build would show a judge that same prompt on first
launch. The engine source says a Shipping build has tracing compiled out, so the entry should be a
Shipping build, and its open ports get checked before it goes out.

### 10:20. 62 sound files, none of them heard by anyone yet

The sound helper reported after about 30 minutes: 47 sounds in 62 WAV files (6.75 MB), every
sample computed by about 1,600 lines of Python it wrote. Noise comes from a seeded random
generator, tones from sine and filter maths. A clapper snap is two short noise bursts through
filters tuned like a small wooden box. One command rebuilds every file.

The orchestrating agent checked the work against the files, not the report: rebuilt everything
and got the same bytes (same hash before and after), confirmed the scripts import only NumPy and
SciPy, and measured three files with a separate audio tool. The clapper snap is 0.2 s long with a
sharp start and most of its energy between 800 Hz and 3 kHz. The frozen-time bed is a 6 s stereo
loop of low hum whose end joins its start with no step.

![The clapper snap: waveform and spectrogram](pictures/sound/01_clap_snap_1.png)

What the helper says is weak, and it is the honest centre of this entry: an agent cannot hear.
It used a tool that matches audio against text descriptions. That tool agrees the clap is a clap
and the frozen bed is a hum, but it hears the revolver shot, the footsteps and the landing as drum
hits, and found no good match for the death sound. Those need a person's ears before they ship.
It also found the clapper only 1.2 dB louder than most other sounds, which matters because the
clapper is the sound the whole game hangs on. The fix is in the mix, when the sounds are wired in.

Next for sound: a third helper (Claude Opus 5.5, lane `music`) is composing the score the same
way, as code. The idea it serves: the music is the film's score, and the clapperboard cuts it.
Snap the board and the score stops dead with the world. So the brief asks for music that survives
being cut off at any moment: steady pulse, strong on every bar, delivered as four stems the game
can mix. `[agent's pick]` If code-made music turns out thin, a local music model is the fallback.

### 11:35. Three enemy kinds, a score, and a test that lied a little

**Enemies.** The enemies helper (Claude Opus 5.5) finished in two sittings. Its first turn ended
while the package was still building, and nothing woke it, so the orchestrating agent sent it back
to finish. What it built: one shared enemy base that the Grunt moved onto, then the Rusher and the
Marksman on top of it, 9 new tests (33 in all), and three demo rooms.

![All three kinds, live: orange Rushers, purple Marksmen with their aim lines, a red Grunt](pictures/enemies/mixed_01_all_three_live.png)
![A Rusher frozen mid-lunge with the player standing against it, unharmed](pictures/enemies/rusher_03_frozen_mid_lunge.png)
![A Marksman's locked aim line held on screen by a freeze](pictures/enemies/marksman_03_frozen_locked_line.png)

The two tests that matter most are the dodge tests. Same start, played twice: standing still, the
Rusher's lunge hits for 35; stepping sideways during its windup, it misses. Same for the Marksman:
stand in the locked line and lose 40, keep walking sideways and lose nothing. An attack you can
see coming and dodge is the rule every enemy in this game has to keep.

**The test that lied.** The orchestrating agent re-ran the helper's proofs itself. The 33 tests
passed. The scripted three-room run finished, but with 5 kills where every earlier run had 6. The
helper had seen a different failure of the same script an hour before and put it down to a frame
hitch. Both were the same cause: the scripted player is timed in game seconds, but the length of
each frame comes from the wall clock, so when the PC is busy (the agent was copying a 1 GB folder
at that moment) one long frame moves a step a few centimetres and a shot misses. The fix is a
switch the engine already has: a fixed time step. With every frame advancing game time by exactly
1/240 s, three runs gave identical log lines, hit for hit. Every scripted proof uses it from now on.
It also means earlier "passes" were partly luck, which is worth knowing.

**Music.** The music helper (Claude Opus 5.5) wrote a score as code: 144 beats a minute, A minor,
a small pit band of drums, plucked bass, electric piano, vibraphone and muted brass, about 34 MB
in 9 files. The action music is four stems of 16 bars the game can mix. It picked 144 because a
bar is then exactly 80,000 samples, so every bar line falls on a whole sample. The agent rebuilt
it (same bytes) and measured the title cue with a separate tool: 144.1 beats a minute, -20.0 LUFS.

![The action mix: waveform and spectrogram](pictures/music/01_action_mix.png)

Its own list of weak points: the drums read as a drum machine (the hi-hat is the cause), the band
reads partly as synthesizers, no cue came out calm, and the title loop repeats after 27 seconds.
Nobody has heard it. Whether code-made music is good enough is the owner's call after listening.

**A hole in the design, found while writing the next brief.** Nothing stopped a player from
freezing time and walking to the exit past every enemy: one freeze covers 24 metres and the rooms
are 28 metres long. `[agent's pick]` The gate now stays locked while an enemy in the room is alive.

**Two helpers started.** Lane `puzzles` (Claude Opus 5.5) builds the puzzle pieces: a door, plates
you shoot in the order that frozen-only glyphs give, a switch that opens a door for a few seconds
which a freeze can hold open, crates that fall and are solid only while frozen, and a refill pad so
a puzzle room can never be left unwinnable. Lane `rooms` (Claude Fable 5.2) designs the five fight
rooms as text files in its own copy of the packaged game, with no compiler. Its brief asks for the
first room to teach the clapperboard without a word of text, since a judge reads nothing, and for
each room to be checked three ways: a script that plays it as intended, one that plays it lazily
like a new player, and one that tries to break it.

### 11:45. The other PC, measured properly

The helper sent back to the GTX 1070 PC (Claude Sonnet 5.5, lane `pctest2`) reported after two and
a half hours and 220 log files. Its answers:

- **The install prompt is gone.** With the runtime files beside the game and no installer in the
  build, the launcher started the game twice with no box. It did not test which of the two changes
  did it, and no PC with no runtime at all was tried.
- **Its first numbers were wrong, and it found out why.** Something else on that PC uses the
  graphics card in bursts: the same build ran at 25 frames a second under it and 66 without. And
  the game saves its quality settings on exit, so one "all low" test run left a file behind that
  made the next "baseline" run at 298. After that it waited for an idle card before each run,
  deleted the saved settings each time, and ran every variant three times.
- **Where the frame rate goes** (1280x720, GTX 1070): 67 as built; 125 with Lumen off; 74 with
  virtual shadow maps off; 142 with all quality groups at medium; 281 with all at low. Lumen is
  the one switch that matters. At 1080p as built it runs at 53, slow enough that the scripted
  player falls off a moving platform every time.
- **What low quality loses to the eye:** the bounce light, and the film grain and colour fringe
  that mark frozen time, because those live in the post-process group. Medium everywhere with
  post-process kept high runs at 144 and keeps the grain.

What this decides: the game will ship with a quality setting that starts at a level the PC can
hold, the frozen-time picture must not depend on a quality group a slow PC turns off, and the look
of the game has to be designed to hold up without Lumen. All three go into the briefs for the
look and the menus.

A second lesson for this log itself. The helper warned that the other PC's name and Windows user
name were in the game's own log, which it had printed. Both were already in two transcripts here.
The private word list now has them, so the current files are clean, but two earlier commits in
this private repository still hold them. Cleaning that means rewriting history, which the agent
will not do without the owner's word. It is on the submission checklist.

### 12:50. Five fight rooms, six puzzle pieces, and a gate that locks

Two helpers reported within minutes of each other.

**The fight rooms** (Claude Fable 5.2, lane `rooms`, text files only, no compiling). Five rooms, each built
on one idea and one moment where the freeze is the answer:

| # | Scene | The idea | Enemies |
| --- | --- | --- | --- |
| 1 | THE WIND MACHINE | A wind machine fills the only doorway. Nobody passes it in live time, so the first clap is forced, and the first Grunt is met frozen. | 2 Grunts |
| 2 | THE STUNT RUN | The Rusher comes to you, so cover stops working. Its lunge is one straight line you can step off. | 2 Rushers, 1 Grunt |
| 3 | THE LONG LENS | The Marksman owns every straight line it can see you on. Cross open ground before its line locks. | Marksman, Rusher, Grunt |
| 4 | THE HOT SET | Fire on the floor is a wall the Rushers cannot cross and you can jump. The film can sits on a rock in the fire, in the Marksman's view. | 2 Rushers, Grunt, Marksman |
| 5 | THE MARTINI SHOT | Height. On a tower top the Rushers cannot reach you and the Marksman sees you over every flat. On the ground it is the other way round. | 2 Rushers, 2 Grunts, Marksman |

![Room 1, script by script: the machine, the first freeze, three shots left hanging](pictures/rooms/room1.png)
![Room 4: four shots hung in front of two Rushers at the fire line, then the rock](pictures/rooms/room4.png)

For each room the helper wrote a script that plays it the meant way, a "lazy" script that walks
forward, stands still and never claps, and scripts that try to break the room. The agent ran the
five-room script itself on the newest build: `RUN wrapped: takes 1, time 76.4 s, shots 41, freezes 11,
kills 17`, health 100, the same numbers the helper reported.

![The wrap screen after all five rooms](pictures/rooms/s5_wrap_screen.png)

What the helper was honest about, and it matters more than the table:

- No person has played these rooms. The scripted player aims perfectly and claps on the frame.
- The scripted clears take 13 to 19 s a room. The brief asked for 30 to 75 s. It did not pad the
  rooms to hit the number, and guesses 30 to 50 s for a person.
- The lazy player loses 40, 55, 60, 80 and 95 health in the five rooms. Health carried and nothing
  healed, so that player is dead in room 3. Layout alone could not fix it.
- Jump first and then press forward, and you land 223 cm away. Run and jump, about 528 cm. The
  order of two key presses decides whether you clear a 200 cm strip of fire.
- A Rusher that lands a hit can hit again 1.37 s later. Stand still and you are dead in 3.7 s.

Three rule changes come out of that, all the agent's picks and all marked for the owner: each gate
gives 25 health back, a Rusher rests 1.8 s after a lunge that lands, and the jump gets more control
in the air. They go to the next helper that compiles.

**The puzzle pieces** (Claude Opus 5.5, lane `puzzles`, the one helper allowed to compile). Six new
pieces a room file can name: a door, plates that open it when shot in the right order, glyphs that
show only in frozen time and give that order, a switch that opens a door for a few seconds of scene
time (a freeze stops the clock), a dropper whose falling crates are solid only while frozen, and a
refill pad that gives the charges back and resets the room's puzzle. The loader now checks a whole
room, not just each line: a code with no glyph for one of its symbols, or a refill pad in a room
with enemies, is refused with a message.

![Frozen: the glyphs appear on the walls, each with pips for its place in the code](pictures/puzzles/code_03_frozen_glyphs.png)
![Frozen: three falling crates become a bridge over the pit](pictures/puzzles/dropper_03_frozen_row.png)
![Frozen: the switch's clock has stopped and its door stays up](pictures/puzzles/switch_03_frozen_door_up.png)

One detail worth keeping: plates count hits in the order the shots were fired, not the order they
land. Three shots hung in a freeze all land in the same frame on the resume, and the code still
reads in firing order. That is the game's own idea (set up the shot, then let it roll) applied to a
lock.

**The gate lock.** A room's gate is red and does nothing while an enemy of the room lives. On the
last kill it turns green. Without it one freeze walked the player past every fight.

![A locked gate, in the same red as the enemy beside it](pictures/puzzles/gate_01_locked.png)

The agent ran the tests itself: all 42 pass (33 old, 9 new). Its count first said 45. The cause was
not the game: the helper was running a test at the same moment and both runs wrote to one log
file, so three results were in it twice. Counted by name, 42 of 42.

Next: a third design helper (Claude Fable 5.2, lane `puzzlerooms`) is building three puzzle rooms
from these pieces and the order of the whole eight-room run. The next compile job is sound: 62
effect files and 9 music files exist and the game is still silent.

### 13:25. Fifty textures, none of them generated

The game is still flat colour on boxes. The plan for its look is written down now ("the set at
night": a black sound stage, plywood flats painted on the face and raw on the back, a scuffed black
floor with tape marks, warm light from lamps the player can see), and the first step was the
textures. The agent chose to have every one drawn by Python code: no image generator, no texture
library. Two reasons. The jam's rules ask that everything be made in the jam, and code that draws
a plank is easier to show than a prompt.

A helper (Claude Opus 5.5, lane `textures`, no compiling) wrote that code and 50 files came out of
it: eight tiling surfaces, each with colour, normal and roughness maps; tape strips and wood chips
as cut-outs; the white layers for a muzzle flash, a sawdust puff, sparks, dust motes, a lamp beam,
the clapperboard's ring, a shot trail and the halo round a hanging shot; and film grain, scratches,
a cue mark and a vignette for the frozen picture.

![The eight surfaces: colour, normal, roughness, and each lit from the side](pictures/textures/contact_surfaces.png)
![The effect layers, cut-outs and film textures, tinted for preview](pictures/textures/contact_effects.png)

How the surfaces tile: every noise is built from whole-number frequencies so it wraps, every blur
wraps at the edges, and every drawn shape is drawn at all nine tile positions. The effects are
drawn shape by shape (each prong, wisp and fleck is a list of points, filled, then blurred where it
should be soft) in separate white layers the game will tint.

The agent rebuilt all 50 from the code and compared them with the delivered files: the same bytes.

The grey surfaces are meant to be multiplied by a paint colour in the game. This is the scenic
paint in five colours:

![One grey paint texture tinted pale blue, sand, red-orange, near white and stage black](pictures/textures/flat_paint_tinted.png)

The helper listed its own weak ones, and the agent agreed with four after looking: the lamp beam's
streaks read as curtain folds, the sawdust puff reads as smoke, the scaffold metal has cells that
read as camouflage under a low light, and the floor's dust is in hard blotches that would show in
every reflection. Those four went back to a second helper with what is wrong and what is wanted.
The other 46 must come out of the rebuild unchanged.

Also running: the helper that compiles is putting sound and music into the game (and the three
rule changes from the last entry), and the design helper is building the puzzle rooms.

### 13:45. The four weak textures, redrawn

The second texture helper (Claude Opus 5.5, lane `textures2`) changed the code for the four the
agent sent back and left the rest alone. Git agrees: 10 picture files changed, all belonging to
the four, and the other 40 are the same bytes. The agent rebuilt everything once more and got the
same files again.

![The lamp beam before and after: the folds are gone](pictures/textures/beam_soft_before_after.png)

The beam is now nearly even. The helper's own warning is fair: with so little in the texture, any
life in a beam has to come from the dust motes drifting through it in the game.

![The sawdust puff before and after, 16 frames each](pictures/textures/impact_puff_before_after.png)

The puff was a blob with a few specks on it. It is now 84 flecks and 7 slivers thrown out of a
faint haze, each slowing, dropping and fading on its own.

The scaffold metal lost its cells and the floor's dust lost its outlines. One thing the helper
would not call fixed: on a long pipe a few brighter brush lines repeat every half metre. That will
be judged in the game, on a pipe.

![The effect layers after the fix round](pictures/textures/contact_effects_fixed.png)

Meanwhile the helper that compiles committed the three rule changes (health back at each gate, a
longer rest for a Rusher that lands a hit, more control in the air) and has started on sound.

### 14:00. Three puzzle rooms, and the lock that could be picked by trying

The design helper (Claude Fable 5.2, lane `puzzlerooms`, text files only) built the three puzzle
rooms that sit between the fights, and the order of the whole run.

**A, THE CUE.** A target opens a door for 1.2 seconds. The door is 2.5 seconds of walking away.
Shoot, clap while the door is up, walk through. Or clap first, shoot, walk to the door and wait:
the shot lands when the freeze ends. The helper left both answers in on purpose, because the
second is the idea room C needs.

![Room A: the target on the left, the tape "cable" to the door, the door held open by a freeze](pictures/puzzlerooms/a_intended_1.png)

**B, THE WILD WALL.** Three marks show only in frozen time and give the door's code. A flat slides
on a rail in front of them and covers one most of the time, so when you clap matters.

![Room B: three empty tape frames, the sliding flat, then the marks in frozen time and three shots left hanging](pictures/puzzlerooms/b_intended_1.png)

**C, THE CUTAWAY.** Falling crates are a bridge only while frozen. The door's target sits in a
side niche that can be seen only from out on that bridge. So the shot has to be left hanging: clap,
walk out, fire into the niche, keep walking. When the scene resumes the shot lands and the door
opens with the player already standing at it. That is the game in one move.

![Room C: the crates frozen into a bridge, and the target seen from it](pictures/puzzlerooms/c_intended_1.png)
![Room C: the shot hangs, the player walks on, the door opens on the resume](pictures/puzzlerooms/c_intended_2.png)

Each room has a refill pad, no pit kills, and each was attacked by its own designer: a script
that wastes all three charges and still finishes, and scripts that try to skip the puzzle. One
skip worked in room C (the target could be hit from the pit floor), so the pit is now 10 m deep.

The agent ran the eight-room script itself: `RUN wrapped: takes 1, time 98.2 s, shots 46,
freezes 14, kills 17`, health 100, the helper's numbers. The rooms are committed.

**What the helper found wrong in the pieces, not in its rooms.** This is the useful part.

- The code plates could be solved without ever freezing time. Each right plate lit green at once,
  so trying plates left to right finds any code in at most 13 shots. The helper's script did it in
  11.4 s against 8.7 s for the meant answer. It could not close this from a room file and said so.
- Shots left hanging at plates counted in the order they arrived, not the order they were fired.
  The last entry praised firing order; that was true only for shots landing in the same frame.
  The helper's first room B failed its own meant answer until it moved the plates onto a side
  stage so that nearest also meant first.
- One upgrade (a hung shot comes back as two) broke the meant answer: the second shot hit the
  plate the first had lit, and a hit on a lit plate counted as wrong. A player holding that
  upgrade would see every plate flash red with no way to know why.

The agent's picks, all for the owner to overrule: a hit plate lights white and nothing more, and
the stand answers only when the whole code is in; a second hit on a lit plate does nothing; shots
left hanging in one freeze count in firing order from anywhere in the room. These went to the
helper that compiles, as a third part after sound. It will also make these eight rooms the game's
own run.

No person has played any of the eight rooms yet. Everything above is a scripted player with
perfect aim.

### 14:55. Sixty-six models built by Blender scripts, and who the enemies are

Until now every enemy, the revolver and the clapperboard were boxes, spheres and cylinders put
together in C++. The agent first settled who the enemies are, since a model needs a subject:
the crew that never went home. Wooden stand-in figures, the jointed kind an artist draws from,
each with a piece of film gear for a head. The Grunt is the Spark (a stage lamp for a head, and
it fires from a hand lamp), the Rusher is the Stunt (crash helmet, padded chest, two safety
cones for horns), the Marksman is the Long Lens (a film camera on tripod legs, its rifle a long
lens). No faces and no skin. That is the agent's pick and the owner can overrule it.

A helper (Claude Fable 5.2) then wrote Blender Python scripts that build every model, run with
no Blender window. No model was downloaded, generated or taken from a library. Its library has
one core shape, a row of rings joined into a tube, and everything is made of that: turned parts,
swept cables, bevelled boxes. It used no cutting operations, because they are slow and break;
a model is a set of closed solids pushed into each other.

- 66 files, 37,822 triangles in all. Each enemy is 10 to 14 files, one per part the code has
  today, under 5,000 triangles an enemy. The limbs have their origin at the joint so they can
  swing later.
- The revolver in 7 parts (the cylinder can turn, the hammer can cock), the clapperboard with
  a white cotton glove and a sleeve, and 17 pieces of set kit: lamp head and stand, truss,
  scaffold bay, flat jack, crate, apple box, sandbag, cable, film can, director's chair, camera
  dolly, C-stand, crash mat, the puzzle switch and the wind machine.
- All sizes are the game's own centimetres and axes, taken from the C++ part by part, so a
  model drops in where its box is now.

![The three enemies, and their outlines at 30 m and 10 m](pictures/models/contact_enemies.png)
![The revolver and clapperboard from the player's eye](pictures/models/contact_hands.png)
![The set kit, each beside a 1.8 m pin](pictures/models/contact_kit.png)

**What the agent checked itself.** It ran the build script: all 66 files in about 5 seconds, and
the table and the manifest (triangle counts, bounds, material slots, the read-back of every
file) came out the same as the helper's, byte for byte. The FBX files themselves differ from run
to run, which is the creation time FBX stores. The triangle total and the 11 slot names were
read from the manifest by a separate script. The models are committed.

**What is not proven.** Nothing has been imported into Unreal. The helper was told not to start
the editor, so whether left and right survive the import is unknown; its report names two files
to check first. The models have never been seen with the game's textures or light.

**What is weak, from the pictures.** The helper listed its own weak models and the agent agreed
with most of the list:

- The wind machine looks like a paddle wheel. It is the first thing a player meets. The helper
  judged it from above; the player sees it head-on, along the axle, through a tunnel.
- The revolver has no hand on it, while the clapperboard has a glove.
- The Spark's hips are a lump and one arm is a stub. The Long Lens's camera head is too small
  to read at range.

A second helper has those as a fix round now, with the wind machine judged from the player's
two views. Putting the models into the game waits for the helper that compiles to finish sound
and the plate rules.

### 15:35. The weak models rebuilt, with the wind machine judged from where the player stands

The fix round is back. A second helper (Claude Fable 5.2) changed 12 model files and added 2.

- **The wind machine.** The first version was judged from above and looked like a paddle wheel.
  The brief for this round was to judge it only from the player's two views, through the tunnel
  it sits in, and to stay honest to the bar that kills: nothing that looks deadly outside its
  sweep, no gap that looks safe inside it. It is now four wooden airscrews on one shaft, a
  striped spinner, a hazard ring round the tunnel mouth and half a wire guard. From the start
  side it reads as a wind machine. From the exit side the motor and belt case read as a dark T,
  and the group is 4 triangles under its budget, so that stays.
- **A hand on the revolver.** A white glove and a sleeve, the same as the clapperboard's. At the
  player's eye only the thumb and the web of the hand show, because the grip sits at the bottom
  edge of the screen. The helper worked out where the edge cuts the gun and said so: more hand
  needs the gun held 3 cm higher, which is a code change for whoever puts the models in. The
  thinner barrel and deeper flutes are a clear gain.
- **The Spark** has a carved hip block and an arm that hangs. **The Long Lens** has a head a
  third bigger with two round film magazines on top, about 12 pixels wide at 30 m where it was
  about 5. **The Stunt** has a padded suit with seams and straps.

![The wind machine before and after, from the player's views](pictures/models2/before_after_wind_machine.png)
![The revolver before and after](pictures/models2/before_after_revolver_hand.png)
![The Spark before and after](pictures/models2/before_after_grunt.png)
![The Long Lens before and after, with outlines at 30 m](pictures/models2/before_after_marksman.png)
![The Stunt before and after](pictures/models2/before_after_rusher.png)

The helper also corrected the brief: the agent had written that the player's eye is at about
165 cm, and the code has it at 152. All its pictures use 152.

The agent looked at the five before-and-after sheets and ran the build again: 68 files, 39,726
triangles, no failed checks, and the same table and manifest as the helper's. Committed. Still
not imported into Unreal. The helper's notes for the import (two new files on the gun, the hub
turning with the blades, three models that now use more material slots) are in the first
report, which stays the one place to read.

### 17:05. The owner rejects the models, and the art stops until the direction is chosen

The owner looked at the models and wrote: "most of the models are terrible. did you check our
local asset library and quixel and other cc0 options before creating your own? also does the
game jam permit the usage of such models? we shouldnt be doing an art pass at all before even
locking down the art direction".

He is right on each point, and the fault is the agent's, not the helpers'.

- **The agent did not check any library.** The studio's own rule is library first, building
  last. The agent went the other way and wrote "no library, no downloads, no generator" into
  every art brief.
- **It did that on its own reading of the rules, without reading them again.** The rules say a
  submission "may include sourced (non-original) assets, but the sourced assets must be noted
  upon submission" (7(d)), that such assets "will not be reviewed or scored" (15(c)), and that
  "content the Entrants generate with AI tools is not considered a sourced asset". So sourced
  models are allowed. The agent had turned "not scored" into "not allowed", and never put the
  choice to the owner.
- **It ran an art pass on a look nobody had approved.** The look ("the set at night") and who
  the enemies are were the agent's own picks. Three helper runs were built on them: 50
  textures, 68 models, a fix round. The agent also judged the models against the grey boxes
  they replace, called most of them good, and wrote that in the last two entries. Measured
  against what a judge will compare them with, they are not.

What changes:

- No model, texture or look work until the owner picks a direction. The lane that was next
  (lighting and surfaces) is not started. The spec's Look section is marked not locked.
- A helper (Claude Sonnet 5.5, read-only) is listing what is already on the shelf: the
  studio's asset library, what Unreal Engine 5.9 ships with, and free CC0 libraries, each with
  its licence. The owner's Megascans account is his to check.
- A helper (GPT 6.1 Sol with image generation) is drawing one moment of the game in four
  directions, live and frozen, so the owner chooses from pictures: a real sound stage, a
  tabletop scale model, a printed-poster look, and a toy-like backlot where each room is a
  different kind of film. These are options, not a pick.
- The textures and models already made stay in the repository, unused.

Sound, music and the plate rules are a different helper's work and carry on.

### 17:25. Sound and music are in the game, the plate lock is fixed, and the PC is out of memory

The helper that compiles (Claude Opus 5.5) finished its second and third parts.

**Sound and music.** Every sound that has an event in the game now plays, and each start and
stop is written to the log. The clapperboard's rules were measured from recordings of the game's
own output, not from the code:

- On the snap the music is gone within 5 ms, and the snap lands on the cut (0.0 ms apart in
  every recording).
- While the scene is frozen the stage's room tone ducks under a frozen bed. On the resume the
  music comes back from the start of the bar it was cut in.
- The four layers of the action music stay in step, and the loop joins without a bump.
- The loudest moment in a fight is 6.9 dB under full scale.

![The snap: the music stops and the clap lands](pictures/audiowire/spectrogram_snap.png)
![The resume](pictures/audiowire/spectrogram_resume.png)

What is not right: the mix is quiet, about -32 LUFS in a fight where games sit nearer -23 to
-18. One sound never plays because nothing in the game makes a crate land. One of the
helper's own checks fails by a little (a match score of 0.468 against a bar of 0.5 after an
upgrade changes the music) and it left the bar where it was. Nobody has listened to any of it.

**The plate lock.** The three faults from the 14:00 entry are fixed. A hit plate lights white
and nothing more. The stand answers once, when as many plates are lit as the code is long. A
second hit on a lit plate does nothing. Shots left hanging in one freeze are held for a moment
on the resume and counted in the order they were fired. The eight rooms are now the game's own
run. The eight-room script ends on the same line as before: `RUN wrapped: takes 1, time 98.2 s,
shots 46, freezes 14, kills 17`, and the room B answer now works with the upgrade that broke it.

The old skip script still opens room B, by luck: its fixed list of shots happens to hold the
code as its fourth group of three. A player with no clue now has 24 orders to try, 72 shots at
worst. The agent's pick is to leave that: it is slower and duller than reading the marks.

**What the agent checked, and what it could not.** It counted the tests in the helper's log by
unique name (58 of 58 pass) and read the run lines and the measurement file. It could not run
anything itself. The PC has 31 GB of memory and less than 1 GB free; the system has committed
about three times what it has. The helper's package build did 1 of 10 compile steps in 30
minutes and was stopped, so the new plate rules have never run in a packaged game. The agent
looked for runaway processes and found none: the memory is held by 24 agent sessions running on
this PC at once (this jam's and the studio's other work), each with its own set of tool
connections, about 15 GB between them, plus a browser, a game client and a chat program.
Freeing it is the owner's call. Until then nothing that compiles can run here.

### 17:30. Four art directions as pictures, and what is on the shelf

No art is being made. After the owner's stop at 17:05 two helpers ran, and neither built
anything for the game.

**Four directions, eight pictures.** A helper with image generation (Codex, GPT 6.1 Sol) drew
one room four ways, each in live time and in frozen time. One try per picture, no edits. The
prompts are in [pictures/artdirection/PROMPTS.md](pictures/artdirection/PROMPTS.md), word for
word, with the helper's own list of where each picture missed its brief. These are concept
pictures for a choice. None of them goes into the game.

A, the real stage: a photographic sound stage at night, crash-test dummies for enemies.

![A live](pictures/artdirection/A_real_stage_live.png)
![A frozen](pictures/artdirection/A_real_stage_frozen.png)

B, the maquette: the director's tabletop model in foam board and card, wooden lay figures for
enemies. Frozen time turns it into a pencil storyboard of itself.

![B live](pictures/artdirection/B_maquette_live.png)
![B frozen](pictures/artdirection/B_maquette_frozen.png)

C, the print: a two-colour screen print, cream and black. Frozen time flips it to cyan and
black.

![C live](pictures/artdirection/C_print_live.png)
![C frozen](pictures/artdirection/C_print_frozen.png)

D, the backlot: a chunky toy western street of painted flats inside the stage.

![D live](pictures/artdirection/D_backlot_live.png)
![D frozen](pictures/artdirection/D_backlot_frozen.png)

**The shelf.** A second helper (Sonnet 5.5, read-only) listed what the studio's own library,
the engine install and the free CC0 sites hold for a film set. The agent checked a sample of
its claims against the files: the mannequin's 102 animation files, the C-stand kit, the truss
and drape meshes, four of the surface sets and three of the props are where the report says.

- Covered at a realistic level: plywood, timber, painted floor, concrete, rubber and metal
  surfaces (Poly Haven, CC0); truss, drape, C-stands and stage lights (in the engine install);
  crates, cables, a film camera; the engine's mannequin with walk, aim, fire, reload, hit and
  death animations; sparks, smoke and dust.
- Covered at a low-poly level: characters, toy guns and crates (Kenney, CC0).
- In no source: a clapperboard, a revolver at a realistic level, a wind machine, tube scaffold,
  a director's chair, flags, crash mats.
- Not checked: Megascans. That needs the owner's account.

The rules say a sourced asset must be noted at submission and is not scored (7(d), 15(c)).
What we make with AI tools in the jam window is not a sourced asset.

**What the agent would pick, and why.** C. Its look comes from one screen effect and good
outlines, so the models only need clear silhouettes, and the engine's animation set gives the
enemies real motion. The freeze is a palette flip that nobody can miss. Everything on screen
would be ours and so would be scored. Its risk is the effect itself: halftone dots that swim
when the camera moves, and flat ink that makes distance hard to read in a shooter. B is the
second pick: it ties closest to the theme, but it needs two looks built, craft materials and a
drawing. A has the most on the shelf and the least that would score. D needs the most new
models and looks the least like its own game.

The choice is the owner's. Nothing is built until it is made.

### 17:55. The owner picks the maquette; the look is locked

The owner looked at the eight pictures and chose B: "i like B the most. also the sketch time stop
look - cant we just use shaders to achieve that look easily?" That was not the agent's first
pick (it argued for C), and the owner's question shows the agent overstated B's cost: the
frozen drawing does not need a second set of art, it is one screen effect over the same scene.

The look, now written into the game's spec as locked: in live time the whole game is the
director's tabletop model of the set, foam board and card walls, a cutting mat for a floor, a
desk lamp for the key light. The enemies are wooden artist's lay figures. In frozen time the
model becomes a pencil storyboard of itself. The gear-headed crew the agent invented at 14:10
is dropped, and so is "the set at night".

Two helpers started, and neither makes game art yet:

- `sketchfx` (Claude Fable 5.2) builds the frozen drawing as per-pixel maths on a test scene,
  using only what a screen effect in the engine can read, and tests the one thing likely to go
  wrong: pencil hatching that swims when the player walks through the stopped scene.
- `bshelf` (Claude Opus 5.5) looks for what already exists for this look in the studio's
  library and on the CC0 sites (card, foam board, tape, a lay figure, a desk lamp, desk things),
  fetches the CC0 candidates and renders them side by side for the owner to judge. It builds
  nothing. This is the step the agent skipped the first time.

The plan after that is one finished corner of one room, in both states, for the owner's eyes
before anything wider.

The PC has memory again (15 GB free; the agent sessions were restarted at 17:53, which also cut
both helpers off after two minutes; one resumed by itself, the other was started again). The
package build that could not run at 17:25 is running now.

### 18:00. The plate fix runs in a packaged game

With memory back, the agent ran what it could not run at 17:25, itself and from the raw logs.

- The package of the current commit built (exit 0).
- The eight-room script on that package ends on `RUN wrapped: takes 1, time 98.2 s, shots 46,
  freezes 14, kills 17`, the same line as the unpackaged run. In room B the plates are entered
  one at a time and the stand answers once, after the third.
- A packaged run started with an upgrade name that does not exist stops at once with
  `there is no upgrade "nosuchupgrade"`. That check had never been run.
- The test suite: 58 tests by unique name, 58 pass.

The agent's first packaged run failed, and the fault was its own command: it gave the script as
a relative path, which the packaged game cannot find. The game said so in one line and stopped.
With the full path it ran.

Still open on this build: the quiet mix, the crate sound that nothing triggers, menus, a
Shipping build. Nobody has played it by hand yet.

### 18:25. The pencil freeze works as maths; what the shelf has for the maquette

Both helpers from 17:55 reported. The agent opened their pictures and counted their files
before believing either.

**The frozen-time drawing** (helper `sketchfx`, Claude Fable 5.2). The owner's question was
whether a shader can do it. On a test scene, outside the engine: yes, with 16 texture reads a
pixel. Left is live time, right is the same frame through the effect.

![Live and frozen](pictures/sketchfx/03_side_by_side.png)

It is the 3D scene outlined and hatched in pencil. It is not the hand drawing of the concept
picture: taped seams, lines that overshoot and strokes that follow a form are not in anything
a screen effect can read.

The risk the agent named at 17:55 was hatching that swims when the player walks through the
stopped scene. The helper measured it on a 3 second walk and turn, as how much the hatch layer
slips against the surface under it. The outline layer, which cannot slip, scores 0.31 on the
same measure, so that is the floor.

| Hatching fixed to | Slip |
| --- | --- |
| the screen | 0.68 |
| the world, one stroke size | 0.36 |
| the world, stroke size follows distance | 0.31 |
| the view direction | 0.47 |

The third is the one to use. The four side by side: [the clip](pictures/sketchfx/compare_2x2_A_B_C_D.mp4).
The helper judged single frames and the numbers, not the moving clip, so a person still has to
watch it. Nothing here has run in the engine: the shader text is not compiled and its cost on
a slow card is a belief, not a measurement.

**The shelf** (helper `bshelf`, Claude Opus 5.5). 35 CC0 assets fetched, 215 MB, each with its
source and licence beside it. The agent counted 35 source notes on disk.

![Surfaces](pictures/bshelf/sheet_surfaces.png)

Card, foam board, kraft paper and pale woods are covered (ambientCG and the studio library).
A desk lamp, a tape roll, a toy revolver and stage lights exist. No source has a cutting mat
without printed numbers, the cut edge of corrugated card, masking tape, a clapperboard, a wind
machine with a guard, or glove hands. Those get drawn by code or built.

![Figures](pictures/bshelf/sheet_figures.png)

The best free figure is a rigged mannequin with 43 animations (Quaternius, CC0). With a birch
texture it reads as a muscular doll with tan skin, not as wood. The agent's call: keep its
skeleton and its animations, and replace the body with rigid turned-wood pieces, one per bone,
which is what a lay figure is. The plain egg-and-ball figures in the test scene above already
read closer to the concept than the mannequin does.

**Started.** `figure` (Claude Fable 5.2) builds the three wooden enemies that way in Blender
and has to defend them next to the concept picture. `slice` (Claude Opus 5.5) puts the pencil
freeze and the card, foam board and cutting mat into the real game for one corner of the first
fight room, and settles the engine risks by looking. The model's scale is the agent's pick:
1:25, so a 5 mm foam board is a 12.5 cm wall.

### 19:10. Three wooden enemies, built in Blender, not yet in the game

The `figure` helper (Claude Fable 5.2) reported. The agent opened its pictures before writing
this.

![Grunt, Rusher, Marksman](pictures/figure/01_three_builds_threequarter.png)

Each enemy is 19 rigid turned-wood pieces, one per bone, on the skeleton of the free
Quaternius animation pack (CC0). No piece bends, which is how a real lay figure works. 4,812
triangles each, two materials. The pack's clips drive them: 13 in use, among them idle, walk,
jog, two hit reactions and a death for all three, pistol clips for the Grunt and Marksman, a
sprint and two punches for the Rusher.

![The Grunt in six poses](pictures/figure/02_poses_Grunt.png)

The three are told apart by build alone, as the concept asks. At 30 m, as outlines:

![Outlines at 30 m](pictures/figure/03_outlines_30m.png)

Through the pencil effect from the 18:25 entry they still read as lay figures:

![Live and pencil](pictures/figure/05_pencil_before_after.png)

Beside the pack's own mannequin, which the 18:25 entry turned down:

![Beside the pack mannequin](pictures/figure/04_beside_pack_mannequin.png)

**What falls short.**

- Nothing is in the engine. The import steps are written and have not been run.
- The Rusher is the smallest of the three, 123 cm, because the game's Rusher has a 124 cm
  capsule and the figure was built to fit it. The concept shows a heavy, stocky one. The
  agent's pick is to keep the capsule, so the fights and the proof run do not change, and
  let width carry "stocky". A big brute needs a bigger capsule and retuned rooms, and that is
  the owner's call.
- Arms leave the capsules: the Marksman's hands by 20 cm, the Grunt's gun arm by 15 cm. Hits
  are tested against the capsule today, so a shot at an outstretched hand would miss.
- The aim pose reads weakly with an empty hand. It needs a gun prop.
- The wood is one texture drawn by code. Feet dip about 2.5 cm in some clips, and pieces
  overlap at extreme bends.

**Next.** The `slice` helper is still putting the pencil freeze and the card surfaces into
the game. It owns the game's source until it reports, so the figures go in after it.

### 20:30. What the player holds: a board, gloves, and a revolver that goes back for a rebuild

The `props` helper (Claude Fable 5.2, started 19:20) built the first-person pieces in Blender
and rendered them from the game's own view: 95 degree field of view, the game's home positions,
live light and through the pencil prototype. Nothing is in the engine yet. The agent opened the
sheets below before writing this.

The concept shows cream knit gloves. No free source had glove hands or a clapperboard (18:25
entry), so both were built. The helper made three hand options so the owner can choose:

![Knit gloves](pictures/props/sheet_B_glove.jpg)

![Wooden lay figure hands](pictures/props/sheet_A_wood.jpg)

![No hands](pictures/props/sheet_C_none.jpg)

The agent's pick is the gloves: they are what the locked concept shows, and wooden hands make
the player look like one of the enemies. The owner can overrule it.

**The home positions were wrong.** At the numbers in the game today the right hand is almost
all below the view and the board is small. Top row is today, bottom row is the helper's
suggestion:

![Home positions](pictures/props/sheet_alt_home.jpg)

**The board** is card with paper stripes, in two pieces so the arm can snap. The three white
squares on the black band stand in for the game's charge lights.

![Board open and shut](pictures/props/sheet_board_open_shut.jpg)

**The revolver is the weak piece, and the cause is the agent's brief.** Beside the concept's
corner (top left):

![Against the concept](pictures/props/sheet_concept_right.jpg)

The concept is a compact snub-nosed revolver. The helper's handmade one is 36.9 cm long with a
tall slab of a frame, and from the eye it reads as an odd long pistol. The brief pinned the
muzzle to the spot the game's code uses today, 22 cm ahead of the grip, and the helper built to
it. That number is one constant in the code and should never have shaped the model. The free
toy revolver (Quaternius, CC0) is worse from this angle: flat blocks. A second helper, `props2`
(Claude Fable 5.2), is rebuilding the handmade one short, with the muzzle wherever the design
puts it, and refitting the right glove.

**The enemies' gun.** A small pistol for the Grunt and a long-barrelled one with a sight for
the Marksman, with the offset that makes it point where the aim clip aims. At 30 m in the
game's own pixels the short pistol is a speck; the long barrel is a visible line from the side.

![Marksman with the long pistol](pictures/props/sheet_enemy_marksman.jpg)

Numbers from the helper's export file: ten meshes; gloves, board and handmade revolver together
6,788 triangles; enemy pistols 328 and 508; nine texture sets drawn by code, none above 1024.
One sourced file used, the Quaternius toy revolver, as a comparison gun only: no mesh from it is in the game
(checked by lane `submit1` on 15 Nov). The helper reported one slip of its own: a
Blender run started with 1.34 GB of memory free, under the 2.5 GB floor in its brief.

**Also since 19:10.** The app that runs the helpers restarted at about 19:48 and cut `slice` and
`props` off mid-run. Both resumed on their own. `slice` is still working on the pencil freeze
in the engine.

### 20:40. The pencil freeze runs in the packaged game

The owner asked at 17:45 whether a shader could do the frozen-time drawing. It can. The `slice`
helper (Claude Opus 5.5) put the 18:25 prototype into the engine as one post-process material
and committed it (`e3883e1`). These are frames from the packaged game, the first fight room,
before any new surfaces or light. The agent opened them and read the run log before writing
this.

Live time, then the clapperboard snaps:

![Live](pictures/slice/s1_live.png)

![Frozen](pictures/slice/s1_frozen.png)

The stopped world is pale paper with cyan pencil outlines and graphite hatching. The enemy,
the gun and the clapperboard are drawn in graphite. The enemy's shot hangs in red-orange, the
player's in yellow, and the locked gate keeps its red-orange. The drawing fades in over 0.1 s
and out over 0.15 s; halfway:

![Half way](pictures/slice/s1_half.png)

**The three risks from 18:25, settled by looking.**

- Lines that shimmer: real. With the camera still, wall outlines crawled from frame to frame.
  The cause is the tiny camera jitter the engine's anti-aliasing uses, which the sketch reads
  after the picture has been smoothed. The jitter is now off only while time is frozen, and two
  still frames then differ no more than with anti-aliasing off.
- Colour: the paper comes out exactly the colour the shader sets.
- Low settings: the drawing survives the lowest post-process quality.

**A problem the helper found itself.** Bright glows turn near white on the way to the screen,
so in the first package the enemy's shot was amber and the player's was cream:

![Before the glow fix](pictures/slice/s1_frozen_before_glow_fix.png)

Glows now dim while frozen, which brings the colours back. In live time the same glows still
read gold, the enemy's shot included. That is the next helper's job.

**Numbers.** The sketch costs about 0.05 ms of GPU time a frame on this PC's card, measured
with the engine's profiler at 1280x720. It is not measured on the slow test card yet. The
helper reports 58 of 58 tests passing. The full eight-room scripted run in the packaged game
still ends `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`; the agent read
that line in the log of the helper's 20:18 run.

**What falls short.** The player's shot is a soft mustard, not a bright yellow. The ceiling's
hatching is heavy. The "CUT!" text is part of the HUD and sits over the drawing in its own
colour.

**The agent's mistake.** Its brief told the helper not to build with under 6 GB of memory
free. That number was a guess. The helper waited 15 minutes for memory that never came and
stopped before the card and foam board surfaces, although its own last package had finished
cleanly at 2.8 GB. The floor is now 3 GB.

**Started.** `slice2` (Claude Opus 5.5) builds the surfaces already written (cutting mat, foam
board with cut edges, corrugated card, kraft, timber braces, masking tape), then the desk-lamp
light, and has to make the danger colour read red-orange in live time.

### 21:10. The revolver, rebuilt short

The `props2` helper (Claude Fable 5.2) rebuilt the handmade revolver as a snub nose and refit
the right glove to its grip. The agent opened the pictures and read the sizes from the export
file: 20.35 cm long (it was 36.9), 2,416 triangles.

Top left is the concept's corner, top right the old gun, bottom row the new one:

![The corner, old and new](pictures/props/sheet_snub_corner.jpg)

It now reads as a revolver in a fist. It is still not the concept's gun: that one is worn
steel, close to real size and turned toward the middle of the screen. This one is black card
and paint, a little larger, and has a flat card tab for a hammer.

Seen straight from behind, the frame half hides the cylinder. The helper offered a small turn
(pitch 3, yaw -10 degrees, bottom right), which shows more of the side. The agent takes it; it
is a number in the game's code, and the owner can overrule it.

The whole view with the new numbers, live and through the pencil prototype:

![The view](pictures/props/sheet_snub_view.jpg)

The helper checked the forearm over a grid of recoil, reload and bob poses at 16:9, 16:10 and
4:3: no cut end comes into view. Wider screens were not checked. The wooden hand option was
not refit and no longer fits this grip; it is only needed if the owner prefers wooden hands.

Numbers for the engine side: muzzle at (8.0, 0, 1.85) in gun space, gun home (40, 24, -11),
board home (29, -15.3, -9.1). None of this is in the game yet. The compile lane is busy with
the surfaces and the light.

### 21:10. The owner: feel and mechanics first, visuals wait

The owner, at 21:10: "dont focus so much on visuals. I want to get the game feel and mechanics
down before we work on them".

That is a fair hit. Since the look was locked at 17:45 the agent has spent every helper on it:
the pencil freeze, the card surfaces, three wooden enemies, the hand props, a revolver twice.
In the same hours nobody played a room by hand, and every gameplay number in the game is still
a first guess checked only by a scripted player.

What changes:

- Art production stops. The `slice2` helper was told to commit the surfaces as they stand,
  skip the light, and free the game's source. The wooden enemies and the hand props stay on
  disk and do not go into the engine yet.
- Next is a build the owner plays, with the tuning numbers readable from a text file so a
  value changes without a rebuild, and keys to restart a room or skip to the next one.
- Then feedback: what the player sees and hears on a hit, a kill, being hurt, the snap of the
  clapperboard and the moment the hanging shots fly.

What exists today, from the source: a jump with 0.1 s of grace at ledges and before landing, a
recoil kick, a red flash when hurt, a 0.14 s flash on an enemy that is hit, a crosshair. There
is no hit marker, no pause or shake on a hit, no screen shake, and nothing that says which way
a hit came from as far as the agent has read.

### 21:25. Surfaces committed as they stand, a build set aside to play, tuning tools started

The `slice2` helper finished what it was told to finish at 21:10 and let go of the source.

- **Commit `ea7e6eb`**: the tabletop model's surfaces. One material, `M_Maquette`, with six
  instances: cutting mat, foam board, corrugated card, kraft, timber, masking tape. Four colour
  maps come from ambientCG (CC0: Styrofoam004, Cardboard002, Paper004, Wood090A). Everything
  else is drawn by code: the mat's grid, the flute edge of the card, the tape, and the pencil
  guide lines on the foam walls. Rooms gained a `prop` piece, used for timber braces and tape
  in the first fight room.
- Checked by the agent against the files, not the helper's report: the commit is on top of the
  pencil freeze commit, the tree has no modified tracked files, and the packaged full run still
  prints `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`. The helper counted
  59 of 59 tests; the agent did not re-run them.
- It falls short of the concept picture, by the helper's own list: hatching disappears on the
  white walls, the ceiling hatching is heavy, the live glows read gold so an enemy's shot is
  not red-orange, and the light is still the old one. None of that is being worked on now.

![The dressed corner, live](pictures/slice2/s2_corner_live.jpg)
![The same corner, frozen](pictures/slice2/s2_corner_frozen.jpg)

The enemies and the held items in these pictures are still the old boxes. The wooden figures
and the hand props are on disk and not in the game.

**A build to play.** The package was copied to its own folder, so later builds do not replace
it while the owner plays. No person has played any room yet. The agent has not started the
game from that folder either; what is known about this build comes from the scripted run.

**Lane `feel1`, started 21:22** (Opus 5.5, the compile lane). It builds two tools and changes
no gameplay number:

- `Tuning.txt` next to the game's exe, one `Name = value` per line, read at start. A template
  with every number is written by the game itself, so it cannot drift from the code. A bad
  line shows on screen in red and is skipped; the game stays open.
- Practice keys, only with a `-SupercutDev` switch: restart the room, next room, previous
  room, no damage, reload the tuning file and restart the room, all upgrades on or off.

Its proof has to include the unchanged run line with no file and no switch, so the tools
cannot leak into the game the judges run.

After that comes the feedback work: hits, kills, being hurt, the snap, the release.

### 21:30. The owner: keep going, but not on the arms and the gun

The owner, at 21:28: "actually keep going as needed, but dont focus on the first person
elements like the arms and the gun".

The agent's reading: visual work may go on beside the feel work where the game needs it. The
held items are the exception. The hands, the revolver, the held clapperboard and their
positions in view stay as they are, boxes in the game and finished props on disk, and no
helper is spent on them. The wooden right hand that no longer fits the short grip stays unfixed.

Only one helper at a time can build the game on this PC, so the work goes in a line:

1. `feel1`, running now: the tuning file and the practice keys.
2. The three wooden enemies and their guns go into the game, in place of the boxes.
3. Feedback on hits, kills and being hurt. It comes after the enemies on purpose: a flinch or
   a shake built on a box would be built again on the figure.
4. The light and the glow colours.

Feedback that sits on the screen, such as a hit marker, a mark for where a hit came from, a
small shake and the snap of the freeze, is not a first-person model and stays in step 3.

### 23:00. A tuning file and practice keys; the wooden enemies start going in

**Lane `feel1` finished** (commit `3c91247`, Opus 5.5). It changed no gameplay number.

- `Tuning.txt` beside the game's exe sets any of the game's 105 numbers by name, one
  `Name = value` per line. The game reads it at start. `Tuning.example.txt`, written by the
  game itself, lists every name with its default and what it does.
- A line the game cannot use is listed in red with its line number for 8 seconds and is not
  applied. The other lines still apply.
- Started with `Play_dev.bat`: F1 restarts the room, F2 and F3 go to the next and the previous
  room, F4 turns damage off, F5 reads the file again and restarts the room, F6 gives every
  upgrade or none, F9 shows the list. A plain start has none of these keys.

![Six bad lines, each named, none applied](pictures/feel1/bad_02_3s.jpg)
![The practice keys, with damage off and every upgrade held](pictures/feel1/f2_keys_upgrades_nodamage.jpg)

Checked by the agent against the files: the commit and its file list, the package folder
(template and launcher present, no `Tuning.txt` left behind), and the full run with no file
and no switch, which still prints `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14,
kills 17` at 22:51. The helper counted 69 tests passing, 10 of them new; the agent did not
re-run them. The helper proved its "every number is in the list" test by adding a throwaway
number to the code and watching the test fail.

Known gaps, from the helper's report:

- No range checks. `Charges = 0` or `FreezeSeconds = 0` would stop the game at an internal
  check. Read in the code, not run. To be fixed in a later lane: a person tuning by hand will
  try zero sooner or later.
- F4 stops enemy shots and lunges. Blades and falls still kill.
- Real keyboard and mouse were not used on this PC; keys went through the same engine call a
  real key press makes.

The new package was copied to the owner's play folder at 22:57, with a launcher that starts it
in a window with the practice keys. Still true: no person has played a room.

**Lane `figin` started 22:58** (Opus 5.5, the compile lane): the three wooden figures and the
two enemy pistols go into the game in place of the boxes, one clip per enemy state, clips
stopping with frozen time. It must not change how enemies behave or what a shot hits. Where
the figures' arms and legs reach outside today's hit shapes it reports the mismatch and leaves
it for the owner. The player's own hands, gun and clapperboard are out of its scope.

## Sat 14 Nov 2026

### 02:30. The wooden enemies are in the game; feedback on hits starts

**Lane `figin` finished at 23:50 on Friday** (four commits, head `440abca`, Opus 5.5). The three
boxes that stood in for enemies are gone. Each enemy is now a wooden lay figure on the CC0
Quaternius skeleton and clips: the Grunt at full size with a short pistol, the Rusher at 0.72
with no gun, the Marksman at 1.25 with a long pistol.

![Two Rushers, two Marksmen and a Grunt, live. The two lines are the Marksmen aiming.](pictures/figin/figin_mixed_01_all_three_live.jpg)
![The same room frozen: figures in pencil, threats keep their red-orange](pictures/figin/figin_mixed_02_all_three_frozen.jpg)

- One clip per state, cut with no blend: idle, walk, sprint, aim, shoot, a punch for the
  Rusher's lunge, a flinch on a hit, a fall on a kill. A dead figure stays lying in the room and
  blocks nothing.
- Shots, the warning glow and the Marksman's aim line now start at the muzzle that is drawn.
- A freeze stops the clips with everything else. The engine's per-actor time scale does it; no
  extra code was needed.
- The helper measured the walk and sprint clips' ground speed from the planted toe, then set the
  clip rates so feet match the enemies' real speed: walk at 2.25 for the Grunt, sprint at 1.05
  for the Rusher. Both rates are in the tuning file.

![The Grunt's warning: the glow grows at the muzzle before it fires](pictures/figin/figin_grunt_03_windup_full.jpg)
![The Rusher crouched in its windup, guard up, visor band lit](pictures/figin/figin_rusher_03_windup_late.jpg)
![The Marksman locked on: the line thickens](pictures/figin/figin_marksman_02_locked.jpg)
![A Grunt after the kill](pictures/figin/figin_grunt_09_dead.jpg)

Checked by the agent: the four commits and a clean working tree; the full scripted run on the
new package, which prints the same line as before, `RUN wrapped: takes 1, time 98.2 s, shots
46, freezes 14, kills 17`; and six of the helper's pictures, opened and compared with its notes.
They match. The helper counted 77 tests passing, 8 of them new; the agent did not re-run them.
Package size went up 5.7 MB. Frame rate in the busiest room is the same within run-to-run
spread (about 276 live, 241 frozen).

What is wrong or open, mostly from the helper's own list:

- **Hit shapes do not cover the limbs.** Shots still hit the old capsules, as the brief asked.
  The Marksman's arms and long pistol reach up to 114 cm outside its 30 cm capsule, and the
  Grunt's gun hand 29 cm. A shot at those passes through. The owner decides whether to widen
  the shapes, add arm shapes, or leave it.

![The Marksman's capsule beside its figure, frozen](pictures/figin/figin_hitshape_01_side_frozen.jpg)

- The Grunt faces the player and strafes on a forward walk clip, so its feet slide sideways. The
  clip set has no strafe.
- The Grunt's full warning glow partly hides its head from the front. The enemy pistols are
  thin and dark at range.
- The helper moved each enemy's eye height to the wooden head. Eye height decides when an enemy
  first sees the player. Only the main run was checked for a change.
- The helper added a guard pose to the Rusher's windup, which the brief did not ask for, and
  dropped the scale pulse on a hit because it sank the feet into the floor. Both are noted for
  the owner.

Two sourced asset sets are now in the game and listed on the submission sheet: the Quaternius
skeleton and clips, and four ambientCG colour maps on the room surfaces. All CC0, each with its
source note and licence text committed beside it.

The package was copied to the owner's play folder at 02:27. No person has played a room yet.

**Lane `feel2` started 02:28** (Opus 5.5, the compile lane). The game has a recoil kick, a red
flash when hurt and a white flash on a hit enemy, and little else. The brief asks for:

- a hit marker and a confirm tick, a short hold and shake on the one enemy that was hit, wood
  chips off the contact point;
- a larger marker, a lower knock, a longer hold and a small camera shake on a kill;
- an arc on screen pointing at whatever hurt the player, and a camera kick away from it;
- a click on an empty revolver, a knock and flashing pips on a clap with no charges, a
  warning in the last second of a freeze;
- a lower jump when the key is let go early;
- range checks in the tuning file, so `Charges = 0` is a red line and not a stopped game.

Two rules in the brief come from the game itself. No effect stops or slows the whole world,
because stopping time is the player's verb. And shakes move the drawn figure or the camera
only, never a hit shape or the aim. Every number is a tuning field, and with all of them set to
off the scripted run must print today's line. The player's hands and gun are out of scope.

### 03:40. Hits, kills and being hurt now answer back; the light pass starts

**Lane `feel2` finished at 03:35** (commit `3583521`, Opus 5.5, 34 files). Until now a hit
gave a white flash on the enemy and nothing else. What the game does now:

- **A hit:** four ticks round the crosshair for 0.12 s, a dry tick sound, the hit enemy alone
  stops for 0.06 s while its figure jitters up to 4 cm, and five wood chips fly off.
- **A kill:** larger pale yellow ticks, a lower knock, a 0.12 s hold before the fall, ten chips,
  and a small up-and-down camera shake.
- **Being hurt:** a red-orange arc on a ring round the crosshair points at what hurt you, the
  camera kicks away from it, and the red flash scales with the damage.
- **The board:** a clap with no charges left shakes the charge icons red; the last second of a
  freeze gets three ticks that close in; the clap itself nods the camera.
- **Jump:** letting go early gives a lower jump (37 cm against 110).
- **The tuning file checks ranges.** `Charges = 0` now shows as a red line and is not applied.
  Before, it would have stopped the game.

![A hit: the ticks have a dark edge so they read on the white flash](pictures/feel2/hit_marker.jpg)
![A kill: pale yellow ticks. The orange disc is the dead Grunt's last shot, still coming.](pictures/feel2/kill_marker_chips.jpg)
![Hurt from the left](pictures/feel2/hurt_left.jpg)

All 37 new numbers are tuning fields with a range. The brief had two rules from the game
itself, and the helper kept both: nothing stops or slows the whole world (that is the
clapperboard's job), and shakes move the drawn figure or the camera, never a hit shape.

The helper looked at its first pictures and changed two things. The white hit marker could
not be seen in a white room, so the ticks got a dark edge. The chips flew on along the shot,
behind the figure, so they now fly back toward the shooter.

Checked by the agent: the commit and its file list, a clean working tree, the scripted full
run on the new package (the same line as before, `RUN wrapped: takes 1, time 98.2 s, shots
46, freezes 14, kills 17`), and three of the six pictures. The helper counted 85 tests
passing, 8 new; the agent did not re-run them. The helper also ran the full run with every
new effect switched off in a tuning file and got the same line on the same frame, and a
script over the whole log found the hold, the sound and the marker starting on the landing
frame for all 30 hits and kills.

What is weak or wrong:

- **Camera kicks move the aim.** The engine aims where the camera points, so a shot fired
  during a hurt kick goes off line. The brief asked for the aim to return exactly, which it
  does, but did not foresee this. The agent's pick: the aim should not move. Fixed in the next
  lane.
- **The chips are too small to see at range.** At 7 m a 2 to 4 cm chip is 3 to 5 pixels.
- **The crosshair itself is white with no edge** and vanishes on white walls. Next lane.
- **The freeze warning bar adds nothing** on a 4 s freeze: the bar already went red in the
  last quarter. The ticks are the warning.
- **Nothing was heard.** Every run was silent. The new sounds are checked by their measured
  peaks only (all under the gunshot, none clipping).
- The scripted run never gets hurt, so the hurt kick in real play is untested.
- The helper started one run with 2.1 GB of memory free, under the 3 GB floor, because it read
  the number and launched in one command. It said so itself. The next brief makes the reading
  its own step.

The package was copied to the owner's play folder at 03:39. No person has played a room yet.

**Lane `light1` started 03:40** (Fable 5.2, the compile lane). The game is evenly lit, the
whites clip, the space beyond the walls is pure black, and an enemy's shot reads gold like
the player's. The brief:

- one warm lamp per room from high on one side with soft shadows, a low cool fill, fixed
  exposure, a dark studio beyond the walls;
- glow colours that hold on screen, measured by hue from packaged pictures: enemy red-orange,
  player yellow, open gate green;
- the frozen drawing checked under the new light, so wall shadows get light hatching;
- the aim fix and a dark edge on the crosshair.

To keep it cheap, every light number becomes a tuning field first. The helper packages once,
then tunes the look through the tuning file with no rebuild, and packages again only when
the numbers are settled.

### 04:55. A lamp over the model, and colours that mean something

**Lane `light1` finished at 04:50** (commit `edb423d`, Fable 5.2). Before it, every room was
evenly lit, the white walls clipped, the space beyond the walls was pure black, and an enemy's
shot read gold, the same as the player's.

Each picture below is before on top, after underneath, from the same spot and script.

![The first room: gradient on the walls, a dark studio above them, and the Grunt's shot now red](pictures/light1/02_slice2_wide_live.jpg)
![All three enemy kinds, live](pictures/light1/05_mixed_live.jpg)
![The same room frozen: the studio is medium hatching, not black scribble](pictures/light1/06_mixed_frozen.jpg)

- **The lamp.** One warm spot light with soft shadows per room, placed from the room's bounds by
  one rule, and a weak cool fill from the other side. No room file changed. Exposure is fixed,
  so the picture does not pump when the player turns.
- **Signal colours.** Danger, the player's shot and the open gate each take their hue from one
  number. The helper found the cause of the gold: a glow stronger than about 2 loses its hue in
  the tonemapper. Cores now sit at 1.5 to 2 and the soft glow round them is a see-through shell
  in the same colour. Measured from packaged pictures: enemy shot hue 38 before, 11 to 13
  after; open gate near white before, hue 122 after; player's shot hue 53.
- **The frozen drawing.** Shadow sides of walls now get light hatching, lit walls stay bare
  paper, and the studio has its own pencil tone.
- **The aim.** Shots and the walk heading come from where the player is looking, not from the
  kicked camera. The new test fails on the old code.
- **The crosshair** has a dark edge and reads on a white wall.

![An enemy shot in flight](pictures/light1/09_enemy_shot_in_flight.jpg)
![The open gate, green at last](pictures/light1/14_gate_open.jpg)

The plan to tune without rebuilding worked: the helper made 27 light and colour numbers tuning
fields, then changed the look through the tuning file between picture runs. It packaged three
times in all, not once per change.

Checked by the agent: the commit and a clean working tree; the helper's test log on the commit
(86 names pass, none fail, counted by the agent from the log); the full scripted run on the
final package, same line as before (`time 98.2 s, shots 46, freezes 14, kills 17`), in a log
written four minutes after the package; no tuning file left in the package folder; and three of
the before-and-after sheets. Frame rate cost, the helper's numbers: 2.7% live, 3.1% frozen.

What falls short of the concept picture:

- **No lamp is seen.** The helper tried a lamp shade twice from simple shapes. Both read as a
  pale moon hanging in the dark, and it took them out. A real lamp head needs modelling.
- **The light is even, not a pool.** The helper kept the far corners bright so enemies read
  everywhere. One number brings the pool back.
- **A shot passing close to the camera** throws a banded red haze over a quarter of the screen.
  Visible in the first picture above. Fixed in the next lane by fading the shell near the eye.
- The revolver's muzzle flash is still a white blob. It belongs to the first-person model,
  which the owner put out of scope.
- The helper lowered the Marksman's line strength because it read pink, and switched off the
  white lamps written in room files. Both changes were needed for the colours and were not in
  the brief.

Not checked by anyone: real input, another PC, an enemy standing in a flat's shadow.

The package was copied to the owner's play folder at 04:53. No person has played a room yet.

**Lane `shell1` started 04:53** (Opus 5.5, the compile lane). A plain start drops straight
into room 1 and Esc quits the program. The brief: a title screen over the frozen first room, a
pause menu that holds a freeze exactly as it was, settings for look speed, volume, quality and
display, a controls list, the close-shot haze fix, and a Shipping build a judge can unzip:
no tuning file, no practice keys, no debug files, no saved settings from this PC, no listening
sockets if that can be had, and its zipped size against the 1 GB limit.

### 06:30. A title, a pause, settings, and the build a judge will unzip

Lane `shell1` (Opus 5.5) finished at about 06:15. Game repo commits `48732a7` and `4dc62cb`.

**What is in the game now**

- A plain start shows a title over room 1 in the frozen pencil look: START, CONTROLS, SETTINGS,
  QUIT. A start with a scripted run skips it, so every old check still works.
- Esc opens a pause menu and never quits the program any more: RESUME, RESTART RUN, CONTROLS,
  SETTINGS, QUIT TO TITLE, QUIT GAME. The whole world stops, a freeze included. A freeze that
  was paused for 3.5 s still ran its full 4.00 s afterwards.
- Settings: SENSITIVITY, VOLUME, QUALITY (four levels), DISPLAY (fullscreen or window). They
  apply at once and are saved for the next start.
- A shot passing close to the eye no longer throws a haze over the screen. The glow shell
  fades out between 300 and 120 cm from the camera; the bright core stays.
- A Shipping build made by one script. It ignores the tuning file and has no practice keys.

![The title](pictures/shell1/shell1_title.jpg)

![The pause menu inside a freeze](pictures/shell1/shell1_pause_frozen.jpg)

![Settings](pictures/shell1/shell1_settings.jpg)

Before and after the close-shot fix:

![Before: haze around a close shot](pictures/shell1/halo_before.jpg)

![After: only the core](pictures/shell1/halo_after.jpg)

**What I checked myself, not from the helper's report**

- Both commits are there and no tracked file is left modified.
- The Shipping folder holds only the engine folder, the game folder, the launcher and the
  notices file: 483 MB, no debug symbols, no tuning files, no saved settings.
- The helper's test zip is 347,740,257 bytes (332 MB) against the jam's 1 GB limit.
- The helper's proof log was older than both final packages, so I ran the full scripted run
  again on each. Development and Shipping both print
  `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`.
- I looked at the title, settings and close-shot pictures.

**What I did not check**

- The helper's count of 93 passing tests.
- That the Shipping game opens no listening sockets. The helper sampled once, in a room.
- Real mouse hover, and the cursor showing and hiding. Menus were driven by script only.
- A first start on a PC that has never run the game.

**The helper's own choices, listed for the owner on the review page**

Music keeps playing under the pause while room sounds stop. The title is silent and hides the
gun and the clapperboard. Esc on the title does nothing. The QUALITY arrows stop at LOW and
EPIC. The first start runs a hardware benchmark and takes the lowest level any of its groups
got.

**Found and not fixed**

- Three source files compile only because of the shared header; each misses an include.
- The Shipping folder still carries the test and demo room files, and the music as plain WAV
  files (29 MB).
- A run started with a forced window size saves that size, and FULLSCREEN then keeps it.

The Development package was copied to the owner's play folder at 06:25. No person has played
a room or heard a sound yet. That is now the largest gap in the project.

### 06:35. Three lanes start: the first minute, the sound levels, an older PC

Every check so far has been a script, a test or a picture. Until a person plays, these are the
three questions a helper can answer without one.

- **`onboard1`** (Opus 5.5, the compile lane). A stranger who presses START is never told that
  right mouse claps. The lane first writes down what a new player is shown in the first minute
  of rooms 1 and 2, then adds two labels to the HUD: `RIGHT MOUSE` beside the charges until the
  first clap, and `R` beside the rounds while the cylinder is empty until the first reload. No
  pop-ups, no pause, no pictures of hands. It also fixes two small things the last lane found.
- **`audio1`** (Opus 5.5, measures only). Nobody has heard the game. The lane records the full
  scripted run and measures how loud it is, whether anything clips, how far each cue stands
  above the music, and which cues land on top of each other. It proposes level changes and
  tests the ones the tuning file can make.
- **`perf2`** (Sonnet 5.5, measures only). The judges' build has only run on the PC it was
  built on. The lane unzips it on a PC with a GTX 1070, lets the first start pick its own
  quality level, and measures the frame rate in each room at each level.

The second and third change nothing in the game. Each got its own copy of the build so the
compile lane can rebuild underneath them.

### 07:10. The first room cannot be passed without a clap, and nothing said how to clap

Lane `onboard1` (Opus 5.5) finished at 07:08. Game repo commit `50ad01a`. It lost about twenty
minutes waiting for free memory on the build PC.

**The audit, done before any change**

The lane played the first two rooms by script as a stranger who never claps, and read the room
files and the code.

- In the first minute nothing on screen names a key. The HUD shows the scene and take, health,
  the revolver's rounds and three small slates with no label.
- Room 1 cannot be finished without a clap. A turning blade fills the only tunnel and kills.
  The stranger script died at the blade 1.4 s after walking off, and every take would end there.
  Painted clapperboards beside the tunnel and red lines at the blade hint at the answer. They
  do not say which button.
- Puzzle A: when the timed door shuts, only its lamp turns from green to red. The ring that
  counts the time down is on the far side of a flat and cannot be seen from the door.
- Firing on an empty cylinder clicks and starts a reload by itself, so the R key is never needed.
- Death restarts by itself after 1.6 s; the upgrade and wrap screens show their keys.

So the game already taught the clap the way a puzzle game should, with a wall the player cannot
pass, and then left out the one fact a wall cannot teach: the button.

![Room 1 before the change: the blade in the only tunnel](pictures/onboard1/audit_02_at_the_machine.jpg)

**What was built**

- `RIGHT MOUSE` beside the three slates, from the first frame of play until the first clap in
  this program run. It stays gone after that, through deaths and restarts, and is not saved.
- No `R` label, because the reload starts by itself.
- A window size forced on the command line is no longer written into the player's saved
  settings.
- Three source files now include what they use.

![The first frame of a run](pictures/onboard1/prompt_01_first_frame_right_mouse.jpg)

**What I checked myself**

- The commit, and that no tracked file is left modified.
- Both proof logs were written after the package they test (the last lane's were not). Each
  holds the line that the label goes at the first clap, and
  `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`.
- I looked at the first-frame picture, the blade picture and the picture at the shut door.
- My own Shipping run at 06:22 had left a settings file on this PC with a forced 1280x720
  size in it, the fault this lane fixed. I deleted that file.

Not checked by me: the count of 95 passing tests. Not checked by anyone: a real right click,
and whether a stranger looks at the bottom of the screen at all.

**Proposed by the lane, not built**

- Puzzle A's door should show its own time running out, for example its lamp bar draining.
- Empty rounds are drawn faint with no dark backing and vanish on a pale wall.

![At the shut door in puzzle A: a red bar and no reason](pictures/onboard1/audit_08_cue_at_the_door.jpg)

Both go into the next compile lane, with whatever the sound lane proposes. The new build was
copied to the owner's play folder at 07:12.

### 07:20. The game is 15 dB too quiet, and three warnings play under the music

Lane `audio1` (Opus 5.5) finished at about 07:15. It changed nothing in the game. It recorded the
full scripted run nine times and measured the recordings.

| Full run | Loudness | True peak |
| --- | --- | --- |
| As built | -31.1 LUFS | -6.6 dBTP |
| A common target for a game | -16 to -20 LUFS | -1 dBTP |

I measured the first recording again myself with ffmpeg and got the same loudness within half
a decibel.

**What it found**

- The whole mix is very quiet. Its peaks stand 24 dB above its loudness, so turning it up alone
  hits the ceiling long before the target. It needs a limiter on the output.
- The Marksman's lock warning cannot be heard at the range it plays: 43 to 60 dB under the
  music. Placed sounds fade in a straight line to silence at 30 m, and the Marksman stands at
  about 30 m.
- The hit tick and the hurt sound sit just under the music. The hit tick often lands on the
  same frame as a kill knock or an enemy burst and is covered.
- The last warning tick before a freeze ends is not hidden by the end sound. The two are in
  different parts of the spectrum.
- Only two volume numbers can be changed in the tuning file. At the top of their range they
  help the hit and kill sounds and do not reach the floor I asked for.

Not measured: the menus, three sounds no script plays, and anything by ear.

![The full run as a spectrogram, before any change](pictures/audio1/spectrogram_before.jpg)

**Lane `mix1` started 07:18** (Opus 5.5, the compile lane) with my picks:

- the whole run at about -20 LUFS with a limiter holding the peak at -1 dBTP. Reaching -16
  would cost the clapper snap 9 dB, and the snap should stay the loudest thing in the game;
- hurt, hit, kill, the freeze countdown and the Marksman's warning at least 6 dB over the music;
- the Marksman's warning heard at full level at any distance, still panned by direction if the
  engine allows it;
- at most one hit or kill sound per frame, the kill winning;
- placed sounds fade out at 60 m.

The same lane takes the two picture fixes from the first-minute audit: the timed door's lamp
bar drains as its time runs out, and the HUD's rounds and slates get a dark backing.

### 07:45. On a GTX 1070 the first start picks the wrong quality level

Lane `perf2` (Sonnet 5.5) finished at about 07:40. It changed nothing in the game. It unzipped the
judges' build on a second PC with a GTX 1070, started it with no saved settings and no options,
and ran the full scripted run at each quality level at 1920x1080.

| Level | Average fps | Worst second | Holds 60 |
| --- | --- | --- | --- |
| LOW | 383 | 304 | yes |
| MEDIUM | 154 | 125 | yes |
| HIGH | 85 | 62.5 | yes, thinly in room 1 |
| EPIC | 45 | 34 | no |

**The first start picked EPIC.** The engine's hardware test scored the card far above its top
threshold and set every group to the highest level. So a judge with this card would have played
at 45 fps, and at 34 in the first seconds of room 1, without knowing a better setting was two
clicks away. I had the same card measured on Friday and wrote then that the game must pick its
own starting level so a slow card does not start slow. The pick was built and never tested on
the slow card until now.

The slowest moment is the first view of room 1, the corridor to the wind machine. It is the
view and not the fight: a freeze there is just as slow. Friday's numbers say what it is. The
engine's global lighting costs half the frame rate on this card, and EPIC is where it is
at its fullest.

Other results:

- The run ended right at every level, with the expected line.
- No listening network sockets, in 355 samples on the title and in rooms. The first lane had
  sampled once.
- The first start took 14.6 s to reach the title, later starts about 2.3 s.
- The title's pencil hatching looks rougher and blocky on this PC. Cause not found.
- Without a fixed time step the scripted player fell in the lava in room 6 in 3 of 9 runs. The
  script walks by the clock and lands a few centimetres apart at different frame rates. It
  says nothing yet about a person, and it is a reason to have a person try that jump.

I read the hardware test's scores in the saved settings file and the tables in the lane's
report. I did not re-run anything on that PC.

![The title on the GTX 1070](pictures/perf2/epic_perf_title.jpg)

**What follows**, for the next compile lane after `mix1`: the first start takes one level under
the hardware test's pick and never starts at EPIC or LOW. On this card that gives HIGH and 85
fps. The same lane looks at why the title's hatching is rough there.

### 08:40. The game is 11 dB louder; the short sounds still hide; the door now shows its time

Lane `mix1` (Opus 5.5) finished at 08:37. Game repo commits `6e62f2d` (sound) and `82b28a0`
(door bar and HUD backing).

**Sound, before and after** (the full scripted run, same measuring tools as the last lane)

| | Before | After | Target |
| --- | --- | --- | --- |
| Loudness | -31.1 LUFS | -20.2 LUFS | about -20 |
| True peak | -6.6 dBTP | -1.7 dBTP | -1 or under |
| Hurt, over the music | -1.4 dB | +4.9 to +6.0 dB | +6 |
| Hit tick | -1.3 dB | +4.4 dB | +6 |
| Kill knock | -3.6 dB | 0.0 dB | +6 |
| Freeze countdown tick | +5.0 dB | +7.7 dB | +6 |
| Marksman's lock warning | -43.1 dB | -2.1 dB | +6 |
| Enemy shots | -7 to -10 dB | +3 to +4 dB | +6 |

Two of my three targets are met: the loudness, and the clapper snap staying the loudest sound.
The third is not. The short, sharp sounds stop gaining once their peaks reach the limiter. A
kill knock 6 dB over the music would need a peak 13 dB above the ceiling, so the limiter cuts
it straight back and more level only dips the music. The limiter takes 7 dB off the hit tick.

I asked for a number, +6 dB, that a 30 ms tick cannot reach at this loudness without a
different sound. The helper tried to squash the sounds at their source, gained under 2 dB,
broke the rule that enemy shots stay under the clapper, and put them back. That was right.

What it means for the player is unknown, because nobody has listened. A tick 4 dB over the
music may be plain to the ear. I am not sending another lane to chase the number. The next
lane adds two numbers to the tuning file, the master gain and the music level, so a person
can turn them with the game running and decide by ear.

Other sound changes: at most one hit or kill sound per frame (the hit tick now plays 4 times
in the run where it played 13, because 9 hits were kills); the Marksman's warning plays at full
level at any distance and is still panned; placed sounds reach 60 m.

**I measured the final recording again myself**: -20.2 LUFS and a peak of -1.7. Both proof logs
were written after their packages and hold the expected run line, and the test log reads 97
passed. The cue table is the helper's; I did not redo it.

**The timed door** now drains its own lamp bar as its time runs out, holds still while time is
frozen, and turns red when it shuts.

![The door's bar half drained](pictures/mix1/door_2_half.jpg)

**The HUD's rounds and slates** have a dark backing. Top strip before, bottom strip after, with
the cylinder empty against a pale wall:

![Empty rounds before and after](pictures/mix1/hud_strip_before_after.jpg)

The helper reported two slips of its own: a file listing that printed the PC's user name in
its tool output (the exporter replaces it), and one game start without a fresh memory reading.

The build went to the owner's play folder at 08:40.

### 08:45. Lane `first1` starts: the first start, and two volume numbers to set by ear

Started 08:42 (Opus 5.5, the compile lane). Three parts:

- The first start takes one quality level under what the hardware test picks, and never starts
  at EPIC or LOW. On the GTX 1070 that should give HIGH and about 85 fps where it gave EPIC and
  45. A level the player chooses is kept as before.
- `MasterGainDb` and `MusicVolume` go into the tuning file, so a person can change the overall
  level and the music against the cues with the game running. The mix so far was set from
  measurements alone.
- The lane then proves the first part on the GTX 1070 with the real Shipping build, and looks
  at why the title's pencil hatching is blocky on that PC, with a time cap.

### 09:35. The slow card now starts at HIGH, and a blur nobody had explained was texture streaming

Lane `first1` (Opus 5.5) finished at about 09:32. Game repo commits `9e869e0`, `a44e47d`,
`cf7dae4`.

**The first start.** It now takes one quality level under what the hardware test picks, and
only ever starts at MEDIUM or HIGH. On the PC with the GTX 1070, with the real Shipping zip and
no saved settings:

| | Before (07:45 entry) | Now |
| --- | --- | --- |
| Level picked | EPIC | HIGH |
| Average frame rate | 45 fps | 86 to 87 fps |
| Worst second | 34 fps | 66 fps |

The hardware test itself costs 4.7 s on the first start. It stays, because without it a fast
PC and a slow one would start the same.

**The title's blocky hatching** was not the graphics card, the quality level, the resolution or
the build. It followed the clock. The pencil hatch is a texture, the engine loads textures at
low detail first and sharpens them over the next second, and one picture had been taken 0.1 s
after the title appeared and the other at 1.0 s. The two hatch textures are 512 pixels square,
so they are now loaded whole from the start. Left: 0.1 s after the title before the fix.
Middle and right: the same moment after the fix.

![Hatching 0.1 s after the title, before and after](pictures/first1/title_hatch_before_after.jpg)

This was more than a title problem. The same textures draw every freeze, so the first freeze
of a run would have opened with the same smear for a moment.

**Two volume numbers** are in the tuning file: `MasterGainDb` and `MusicVolume`. Both apply
when F5 is pressed in a running game. The lane changed both during a run and the recorded level
dropped at that moment with no restart. With the music at half, the music under the cues fell
by 5.5 to 5.8 dB and every sound effect stayed within 0.2 dB.

**What I checked myself**

- The three commits and a clean tree.
- Both packages were built after the last commit, and both proof logs were written after their
  package. Each holds `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`.
- The log of the first start on the slow PC: the test's scores, every group at the level under
  the top one, the run finished, 87.4 fps by the game's own counter.
- The before and after hatching picture.
- The two new lines in the tuning example file.

Not checked by me: the count of 99 passing tests (no test log was kept in the lane folder, only
the report's line). Not checked by anyone: a truly cold first start, and anything by ear.

The build went to the owner's play folder at 09:36.

### 09:45. The owner picks the picture generator for props; two lanes start

A second agent thread ran a test of generated set-dressing props (lane `rodin1`): a desk lamp, a craft knife and a
director's chair, each from a reference picture made by two image generators (FLUX on our own PC, Codex image
generation), then turned into a mesh by Hyper3D Rodin and cleaned up in Blender. Six meshes, 3.0 Rodin credits. The
owner looked at the side-by-side and chose: "codex it is". Codex image generation is now the one generator for every
SUPERCUT reference picture. Its pictures run warmer and more saturated than the approved concept, so the next
prompts add "muted, pale balsa".

That thread asked me one question before making the rest (lane `rodin2`): what size the meshes should be. My answer:
the player's scale, desk centimetres times 25, as the test delivered (knife 400 cm, lamp 1125 cm, chair 86 cm). The
game world is in centimetres at the player's size, so the import places each mesh at scale 1.

I looked at the test render before answering and asked for four things in the next batch:

- No prop in a signal colour. The test knife has a yellow handle, and yellow is the colour of the player's shots.
  The import will shift that handle to grey; new props avoid yellow, red-orange, green and cyan.
- No numerals on the steel ruler, tick marks only. The rules for this entry bar label text on props, and generated
  numerals come out as scribble.
- An opaque set square and glue bottle. Clear plastic does not survive a 3,000 triangle mesh with one texture.
- The film gear (light on a stand, camera on a tripod, apple boxes, sandbags, cable reel) built as balsa and card
  models like the chair, since in the fiction they are parts of the tabletop model.

None of the props are in the game yet. A compile lane imports them when the batch is delivered and the owner has
seen the contact sheet.

Two helper lanes started at 09:44, both measure or record only, neither changes the game:

- `jump1` (Sonnet): does the lava jump in room 6 depend on frame rate, and how wide is the window for a person? On
  the slow test PC the scripted player fell in 3 of 9 runs. The earlier lane called it script timing. Nobody measured
  what a person gets.
- `video1` (Opus): a one-command pipeline that records the judges' build on the slow test PC at 1080p and 60 fps
  with the game's own sound, and a first draft of the 30 to 60 s gameplay video as one continuous take played by the
  game's scripted player. The command has to re-run after the props go in.

### 10:28. The owner approves the generated props; the import starts

The second batch of props is back (lane `rodin2`, run by the other agent thread): steel ruler, pencil, glue bottle,
masking tape, set square, and the model film gear: a light on a stand, a camera on a tripod, apple boxes, sandbags,
a cable reel. Each came from a Codex reference picture, two Rodin tries per prop, the better one kept and cleaned up
in Blender to 3,000 triangles with one 1024 px colour texture. 20 generations, 10.0 credits. With the 3.0 from the
first test that is 13.0 of the 40 I budgeted. The ledgers, with every prompt, setting and task id, are in
`ledgers/rodin1.json` and `ledgers/rodin2.json` (the service's status-check tokens are left out).

![The approved set on the cutting mat](pictures/rodin/rodin2_group.jpg)

The owner's verdict on the contact sheet: "pencil looks fine, knife should be remade, the rest of the set is ok".
So twelve props go in: the ten above plus the lamp and the director's chair from the first test. The yellow knife
does not. My plan this morning was to shift its handle to grey at import; the owner's rule is that a wrong generated
picture gets a fresh generation and no repaint, and a third small lane (`rodin3`) is making a new grey knife.

Known small defects the owner accepted: the set square is thicker than a real one, the cable reel's discs are a
little faceted, and the film light's face does not glow.

I looked at the group render myself before writing the import brief. The film gear is tiny beside the desk tools,
which is right: a 2 m light is 8 cm on the desk at 1:25.

Lane `props1` (Opus, the compile lane) started at 10:26. Its brief:

- Import the twelve meshes and textures through the project's asset script. No Nanite.
- The lamp mesh goes where each room's lamp light already is, head at the light, base on the desk outside the walls.
  The light's own numbers do not change.
- The five desk tools lie on the desk outside the walls, giant, varied from room to room.
- The film gear stands inside the rooms at the edges, grouped as a crew would leave it, clear of every path, door,
  blade, gap and shot line. It blocks the player.
- Placements are written as lines in the room files so a person can move a prop by editing text.
- Every prop carries the mark the freeze effect reads, so it turns into pencil with the rest of the room.
- Nothing about play may change: the scripted full run must print the same line as on Friday, on both builds, and
  frame time must stay within 5 percent.
- The held items (hands, revolver, clapperboard) are not touched.

### 10:33. The new knife arrives; thirteen props go in

Lane `rodin3` delivered the remade craft knife: grey handle, 2,998 triangles, 400 cm long at the player's scale. Two
generations, 1.0 credit, so the props cost 14.0 Rodin credits in all (`ledgers/rodin3.json`). The other thread
measured its texture at 0.00 percent in the four signal colour bands. I looked at the group render before passing
it on.

![All thirteen props, with the grey knife beside the ruler](pictures/rodin/rodin3_group.jpg)

Lane `props1` was seven minutes into the import, so I sent it the knife as a mid-task note: thirteen props, the
knife is a sixth desk thing outside the walls with no collision. The yellow knife from the first test stays out.

A note on this log itself. The generation tool had been writing each job's status-check token into its ledgers
(a token that only lets you ask whether a finished job is done, not the account key). One of them was printed in a
helper's transcript. I caught it in the scan before the 10:28 push and it never reached the repo: the exporter now
replaces those tokens, the scan fails on any long token of that shape, and the ledgers copied here leave the field
out. The other thread has since removed the field from the tool.

### 10:37. The room 6 jump does not depend on frame rate; the falls were the script's

Lane `jump1` (Sonnet, measure only) is back. It ran 173 edge trials and the room 6 scene at six fixed frame rates
from its own copy of the build. I read its report and checked the code lines it names.

- **The jump is the same at every frame rate.** A running jump goes 403.2 to 403.7 cm, 110.0 cm high, about 670 ms in
  the air, at 30, 45, 60, 85, 144 and 240 fps. The one frame rate effect is the run-up from standing still, up to
  9 cm longer at 30 fps.
- **A person has about 128 cm, or 212 ms at full speed,** to press jump before the 200 cm lava strip. The window for
  the rock hop is 167 cm out and 142 cm back.
- **The late edge is the body, not the feet.** Lava kills when the player's 68 cm wide body box touches it
  (`SupercutRoom.cpp`, the kill test), so walking toward lava kills 34 cm before the painted edge. Coyote time
  (0.1 s) and the jump buffer (0.1 s) exist but cannot help at this edge, since the player dies on the ground.
- **Yesterday's explanation was half right.** It was script timing, but not at the first jump. All three deaths were
  on the walk back from the rock: the script fires its return jump 0.30 s into a walk that reaches the death line
  after 0.28 to 0.33 s. The runs that passed had 0.8 to 8.7 cm to spare. At fixed steps, 144, 60 and 30 fps die,
  and 240, 85 and 45 pass.

So the game is not broken at low frame rates, and my card for the owner ("the first thing I would ask a person to
try") was pointing at the wrong thing. What is still unknown is whether a 212 ms window feels fair to a person.
Nobody has played it.

What I will do with it, once the import lane has left the repo (one lane writes there at a time):

- Move the script's return jump from 8.85 s to 8.70 s, which the lane tested at all six rates (6 of 6 alive, 81 to
  100 cm spare), and look at the later strip jump, which has only 21 to 31 cm spare.
- Put the lava's reach (34 cm today) in the tuning file with the same default, so a person can try a kinder edge
  while playing. The lane advised against changing the default with no evidence that anyone misses the window, and
  I agree.

### 10:59. A first draft of the gameplay video, made by one command

Lane `video1` (Opus) is back with the recording pipeline and a draft. The entry needs a 30 to 60 s video of
recorded gameplay at 1080p or more. The art is still changing, so I asked for a command that makes the whole video
again without hand work, not for a finished cut.

`bash tools/make_video.sh` on the build PC copies the build to the slow test PC (GTX 1070), starts the game there on
the real screen, records the screen with ffmpeg, has the game write its own sound to a wav, finds the claps in both
picture and sound to line them up, sets the loudness, and writes the file. A full run from nothing takes 3 min 54 s.

The take is one continuous run by the game's scripted player, written by the lane to move like a calm person: the
title, START, the first clap at the blade, a fight with shots hanging in the air, an upgrade card, the door puzzle,
and an ending on a frozen frame. No cuts, no text or graphics added, every frame and sound from the game.

![One frame every 2 s of the draft](pictures/video1/draft1_sheet.jpg)

I checked the file myself, not the lane's summary: 1920x1080, 60 fps, H.264, 46.47 s, 2,788 frames, -15.1 LUFS,
true peak -1.6 dB. I looked at the contact sheet above. The lane measured the sync at four claps 35 s apart, all
within one frame.

What is wrong with it, plainly:

- **It is the Development build, not the judges' build.** The Shipping build has the sound recorder compiled out, so
  it cannot write the wav. Same commit, same numbers. I am leaving that as it is: the recorder does not belong in
  the build judges get.
- **About 5 s of room 1 stutters.** The game holds 60 fps there but the screen capture only gets about 42, with the
  graphics card at 93 to 97 percent (other programs on that PC take a quarter of it before the game starts). 86
  doubled frames in all, 75 in that stretch. Two fixes failed. To try next: record with one quality group lower, or
  on a faster PC.
- **The gun and clapperboard are grey boxes.** The held items are on hold by the owner's word, so the video shows
  what the game has.
- **The title holds 4 s, and the two upgrade screens take about 5 s between them.** Too long for a 46 s video.
- **The scripted player still snaps the last few degrees onto an enemy** when it aims. The script language has no
  smooth turn; the lane built its turns from many small mouse steps.
- Nobody has listened to it. I cannot hear, and neither can the lane.

This is a draft to react to, and the pipeline is the real result. It gets run again after the props are in. A take
played by a person would be better than any script, and the same pipeline can record that.

### 11:50. Thirteen generated props are in the game

Lane `props1` (Opus, the compile lane) finished. Game commits `cdb6803` (meshes and import script) and `323aaf9`
(lamp, room lines, tests). What I checked myself before believing the summary:

- No modified tracked files; both packages are newer than the last commit (Development 11:29, Shipping 11:31).
- Both proof logs are newer than their packages (11:41 and 11:43) and print Friday's line: `RUN wrapped: takes 1,
  time 98.2 s, shots 46, freezes 14, kills 17`. Nothing about play moved.
- I looked at 15 of the 51 after pictures, live and frozen.

![Room 04 before and after](pictures/props1/04_before_after.jpg)

What was built:

- **Import.** Thirteen meshes into `Content/Props/Set` through the project's asset script, one shared material, no
  Nanite. The lane found no text, logo, barcode or QR code on any texture; the ruler and set square carry tick marks.
- **A new room-file line, `dress`.** Each prop is one line of text in its room file. An unknown name, a zero scale or
  a missing mesh fails loudly. Two new tests, 101 in all by the lane's count.
- **The lamp** stands at every room's light, scaled 2.28 to 3.26 times so its bulb sits at the light. The light's
  own numbers match the before log in all eight rooms.
- **Film gear:** three or four pieces per room in crew groups (camera on apple boxes with the chair; film light with
  sandbags and a cable reel), each with a collision box, 330 cm or more from the scripted route.
- **Desk things** lean on or lie across the walls from outside.
- **Frame time** on the build PC: 260 to 265 fps before, 261 to 281 after.

![The camera group in room 04](pictures/props1/04_A_live.jpg)
![Frozen: the props turn to pencil with the room](pictures/props1/03_A_frozen.jpg)

My own read of the pictures, which is less rosy than the checklist:

- **The film gear works.** It reads at once as a crew's kit, at the right size, and it draws correctly in a freeze.
- **The giant desk things mostly do not show.** The walls are taller than the tools and the studio beyond is black,
  so in six rooms all you get is a dark tip 74 to 163 cm over a wall. The one that lands is the glue bottle standing
  on the thick wall in the cutaway room, dark against the lamp. The idea was that these give the scale away. As
  placed they do not, and several lie on the desk where no camera sees them.
- **The lamp from below is a glowing ring with a dark blob in the middle** (the mesh's own socket in front of the
  glow). The lamp's dark body is nearly lost against the black studio.

![The glue bottle on the wall, the one desk thing that reads](pictures/props1/c_A_live.jpg)
![The lamp from the floor](pictures/props1/01_L_live.jpg)

I am not sending this back for another art round now. The owner asked for feel and mechanics first, the props do
no harm, and the gear is a clear gain. The two weak points go to the owner as review cards with pictures.

One thing the lane did not test worries me more than the looks: some gear stands where Rushers roam, and every
piece blocks everything. A Rusher stuck on an apple box would be a real play bug. That goes into the next lane.

Lane `fix2` (Opus, compile lane) started at 11:49 with three small jobs and one measurement: move the test script's
two tight jumps in room 6 (from `jump1`'s numbers), put the lava's 34 cm reach in the tuning file at today's value,
test Rushers against the gear in every room and fix what sticks, then run the judges' build on the slow test PC to
see that the props did not cost frame rate there.

The play folder has the props build as of 11:49.

### 12:34. The judges' build goes to two teammates' PCs

The owner is playing the build by hand for the first time (his first question was how the code door works, which
is a finding in itself: the dots under the marks do not read as "order" without being told). He asked me to put
the game on the other two developers' PCs and start it so they can test too.

I sent the Shipping build of commit `323aaf9` (the props build), not the Development one: it is what judges get, it
opens no network port, and it has no practice keys to lean on. A zip of 340 MB, copied over ssh, unpacked to a
folder on each PC with a small `Play.bat` that starts the game with its log switched on, then started on each real
desktop through a one-off scheduled task.

Both PCs had never run the game, so this was also the cold first start nobody had tested. On both the hardware
test ran, the game started at HIGH (quality groups at 2, resolution scale 87) at 1920x1080 full screen, and the
process is up and responding. One PC has an RTX 4080 Super, the other an RX 9070 XT, so the test will have scored
them for EPIC and the first-start rule took one level off, as built this morning.

A known fault in this build, found by lane `fix2` while I was copying: a Rusher cannot get past the new film gear.
Stand behind a chair or a cable reel in rooms 02, 03 or 05 and it lunges into the box over and over without
hitting. `fix2` has already committed the fix (enemies pass through gear, which still blocks the player and shots)
and is packaging. The testers get that build when it passes, swapped in while their game is closed.

### 12:54. Rushers pass through gear, a tester's first run, and the held items are approved

**Lane `fix2` is done** (three commits, `dd7f356`, `83e7ffe`, `87223aa`). I checked it against the files, not its
report: the tree is clean, both packages are newer than the last commit, both proof logs are newer than the
packages, and both print the reference line unchanged: `RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14,
kills 17`. 103 tests pass.

- **Rushers and film gear.** The lane measured the fault before fixing it. In rooms 02, 03 and 05 a Rusher's lunge
  stopped on a chair, the apple boxes or the cable reel again and again while the player stood behind it. Moving
  the gear was not possible: the Rusher home covers the whole floor of those rooms. So enemies now move through
  gear, and gear still stops the player, shots and sight lines. Re-test: 41 lunges, 41 hits, none stopped on gear.
  The new test goes red with the fix turned off. Not checked in motion: a Rusher's body shows inside a chair for a
  moment as it passes.
- **Test script jumps in room 6** moved earlier (8.85 to 8.70, 10.64 to 10.57). The scripted run now passes room 6
  at 30, 45, 60, 85, 144 and 240 frames per second.
- **`LavaReach`**, a new tuning number: how far past its painted edge lava kills, 0 to 34 cm, default 34 (as before).
- **GTX 1070 at HIGH, 1920x1080, with the props:** 86.9, 86.1 and 87.0 fps average over three full runs, against
  87.4 before the props. The slowest 1% is 63.5 to 64.7 against 65.0.

The Development build went into the play folder at 12:52, with no game running.

**A tester's first session.** One teammate closed the game, so I could read its log: 17 minutes of play.

- The second code door took 3 minutes 17 seconds on the first visit. Four times the plates were shot in the order
  ring, chevron, tee, which is not the code. That is the same thing the owner asked about: nothing in the room says
  that the dots under each mark are the order.
- Deaths: lava twice in room 6, the fan blade once in room 1.
- Once the rooms were known, a whole run took 44.8 seconds, and the next one 46.8. Eight rooms are short for
  someone who knows them. The codes are the same every run, so a door that took three minutes the first time took
  four seconds later.

These go on the list for the owner's feedback round. I changed nothing for them.

That tester's copy is now the `fix2` build (swapped while the game was closed, pak size checked against the build
here). The other tester still has the game open, so that copy waits.

**Held items approved.** The owner approved the generated revolver and clapperboard from lane `rodin5` (run from
another thread; its transcript is in this log). They replace the boxes built in code. Hands are not picked yet, so
the box hand stays. Lane `held1` (Opus 5.5, high) started at 12:53 with a written brief, `lanes/held1/BRIEF.md`:

- The new gun is scaled and placed so its muzzle sits exactly on the old muzzle point. Shots start where they
  started, so the run line must not change.
- The cylinder steps per shot, the hammer and trigger move, and the rounds show the load.
- Reload tips the gun out of view and brings it back loaded. A round cannot leave backwards through this frame,
  so there is no ejecting shell.
- A missing mesh fails loudly. The boxes are deleted, not kept as a fallback.

### 13:40. The approved revolver and clapperboard are in the game

Lane `held1` is done (commits `203d2ad` and `d7d0115`). The boxes built in code are gone and the seven generated
meshes from lane `rodin5` are in their place. Checked against the files: the tree is clean, both packages are
newer than the last commit, and both run logs are newer than the packages and print the reference line unchanged,
`RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17`. 107 tests pass (4 new).

![Before and after, rolling time](pictures/held1/before_after_live.jpg)

![Before, after, frozen, and a shot](pictures/held1/held1_sheet.jpg)

- **Play did not change.** The meshes are real hand size and the box gun was larger, so the lane scaled the new gun
  by 1.36 (it then covers the same screen area, 67,748 px against 68,624) and placed it so its muzzle sits on the
  old muzzle point to within 0.01 cm. Shots start where they started.
- **New motion, view only:** the cylinder steps 60 degrees per shot, the hammer flicks back and falls, the trigger
  pulls and returns, and the rounds in the cylinder show the load. A reload tips the gun fully out of view and it
  comes back loaded.
- **No fallback.** A missing mesh stops the game at start with a message. The lane broke the code on purpose once
  and the muzzle and rounds tests went red.
- **Frame time:** 278 to 282 fps before, 280 to 282 after, on the build PC.
- **One slip the lane caught itself:** its first test used a call that only exists in the editor, so the package
  failed to build. The second commit fixes that.

What I see in the pictures, which the lane also says:

- Nothing holds the gun. Its grip runs off the bottom of the view. Hands are the next thing the owner picks.
- The hand and forearm under the board are still plain boxes.
- The slate face reads tan in the game's light. It was whiter in the render the owner approved.
- In frozen time the revolver's hatching is busier than the box gun's was.

Not checked: nobody has played with the new items by hand, and no picture shows the cylinder or hammer moving at
a size you can read. The tests prove the angles.

The Development build went into the play folder at 13:39 with no game running. One tester's PC has the new judges'
build (checked by file size). The other tester still has the first build open, so that copy waits.

### 14:07. A second thread studies FPS game feel

The owner asked for a thread to study first-person shooter game feel. It started at 14:07 as its own thread (Claude
Fable 5.2, high), lane name `feelstudy`. It is a study and changes nothing in the game.

Its brief asks for four things in `lanes/feelstudy/`:

- A report on what makes a shooter feel good, element by element (movement, camera, the gun, hits, damage taken,
  and what is special to a game that stops time), with numbers and a named source for each claim.
- A table of the game's values today, read from the code and the tuning file, beside the ranges the references use.
- A ranked list of changes with exact numbers, each marked as a tuning-file line or a code change.
- Tuning presets: full copies of the tuning file with only the changed lines different, so the owner can drop one
  into the play folder and press F5.

It may not edit, build or package the game. The promise to the owner stands: nothing changes the game until the
feedback is in.

### 15:09. The owner's first feedback, and the feel build starts

The owner played the build and gave eight notes to the feel study thread, with three videos on game feel to study:
finer and typed sensitivity and volume, a louder gunshot, teaching each new piece when it first appears, better
impact effects (screen shake, sound, knockback, bullet marks), a cooler gun, a clapperboard as the recharge model,
more or harder enemies in rooms with no puzzle, and bullet shells that stay.

The study thread turned its findings into a build brief (`lanes/feelstudy/BUILD_BRIEF.md`). Then the owner wrote:

> "im still unsure about the type of gun, can you direct the main thread the build the gamefeel elements you
> studied. Elements like fire rate and enemy health, go with what you suggest and then we'll tune it again (i assume
> these elements are just variable changes so it should be fine to tune after build right?)"

I read that message in the study thread itself before acting on it, because it ends my promise that nothing changes
the game until the feedback is in. This is the feedback.

Two lanes build it, one after the other, since only one lane can compile at a time. Both are on Opus 5.5, high.

- **`feel3`, running since 15:08:** the new defaults (fire interval 0.25 to 0.18 s, shot speed 9000 to 14000,
  bigger hit, kill and clap feedback) and the gun: a louder shot with a low layer, a camera-only view kick per
  shot, the gun's own kick as tuning lines with variation, a longer and larger muzzle flash, and the mouse.
- **`feel4`, brief written, starts after `feel3`:** wall marks, chips and shells that stay, a slid shove on hits,
  feedback on the freeze release scaled by the number of hanging shots, a lower-pitched shot in a freeze, then
  footstep rate and a kill chain if time allows.

What I added to the study's brief:

- Every random choice in the new effects uses its own random stream, so a seeded run stays repeatable. The lane
  proves it by running the same seed twice.
- The reference run line will change with the new defaults. The run must still finish in one take with 17 kills.
- The study's mouse numbers came from reading code, not from a mouse. The lane measures real mouse counts against
  degrees turned on the GTX 1070 PC before it changes the default, and leaves the default alone if the numbers
  disagree. One piece of evidence so far: a tester lowered SENSITIVITY from 1.0 to 0.7 in the first session.
- The same tester turned the volume from 100 down to 50, so only the player's shot comes up. Nothing else gets louder.
- New things that stay (marks, chips, shells) are drawn with what the game already has. No engine default
  textures.

Not built: a path line on hanging shots and a reload that starts by itself. Both need the owner's yes.

Still to do from the owner's notes, after these two lanes: teaching each new piece (the code door first, which
two people have now failed to read), more enemies in the fight rooms, and a clapperboard as the recharge model.

### 15:42. A design lane for more levels and new mechanics

The owner asked: "separately, can you come up with more level designs, including different mechanics (could even
be movement based) and varying complexity/ stacking previously learned mechanics in one level".

Lane `levels1` started at 15:41 (Claude Fable 5.2, high). It designs and builds nothing, so it can run beside the
compile lane. Its brief, `lanes/levels1/BRIEF.md`, asks for:

- 8 to 12 new mechanic candidates, at least four about movement, each tied to the freeze, with the code it needs
  and how the room teaches it in ten seconds without text.
- 12 to 16 rooms with top-down maps drawn to scale: a first room for each new mechanic, rooms that stack two and
  three learned mechanics, fight rooms with harder enemy mixes, a room to end a run, and a better first lesson for
  the code door.
- A teaching curve for a run of 10 to 14 rooms, and a room pool that can vary a run without breaking it.
- A ranked shortlist split into rooms that are data only and rooms that need new code, sized for the time left.

The brief gives it what play-testing showed: two of two players could not read the code door, a known run takes
45 seconds, and the codes never change. The rooms must be original, not copies of rooms from other games.

Nothing from it is built until the owner picks from its page.

### 16:17. Two held items get the owner's yes; the level lane restarted

The feel study had marked two ideas as needing the owner's yes: a thin line from each hanging shot to the first
thing it will hit, drawn only in frozen time, and a reload that starts by itself 0.2 s after the last round. I had
held both out of the build and had not put the question to the owner directly, which was my miss. Asked today, the
owner said: "yes both are needed".

Both are now in the brief for the second feel lane, `feel4`, which has not started. They come after the wall marks
and the shove and before the release feedback. What the brief adds to the study's one sentence each:

- The reload: one tuning line, `AutoReloadSeconds` (0.2, and 0 means it waits for a click as today). Only the
  start of the reload changes. A click during the delay must fire nothing.
- The path line: it ends where the shot would really stop, traced with the shot's own collision. It is view only,
  so the scripted run must not change because of it. It has an on/off line, a width and an opacity. The lane takes
  pictures with six and with twelve shots hanging, to judge clutter.

The level design lane `levels1` failed seconds after its first start at 15:41: the account it was started on had
no model allowance left. It had written nothing. Restarted at 15:47 on another account with the same brief.

State of the first feel lane, `feel3`, at 15:57, read from its files: the gun items are written and pass the tests
but are not committed. The louder shot has a new low layer (energy under 120 Hz up from about -15 dB to about
-4 dB of the total). The mouse was measured with real input on the GTX 1070 PC: 0.1625 degrees per count live,
0.154 in a freeze, 0.1475 during the snap. That matches the study's numbers, so the lower sensitivity default
goes in with the lane's second commit, with the fire rate and the other default changes.

### 16:26. Level designs are in: 16 rooms, 11 mechanic candidates

Lane `levels1` finished at 16:24. It designed and built nothing in the game. Its own words on that: every time,
difficulty and build size is from paper, and the game has not loaded one of its draft room files.

What it wrote: `lanes/levels1/LEVELS.md` and a page for the owner to choose from, with a to-scale top-down map per
room drawn by script from data files.

![two room cards from the levels page](pictures/levels1/levels_page_cards.jpg)

- **16 rooms.** Ten use only pieces the game has today (a room file and nothing else). Six need one of three small
  new pieces.
- **11 mechanic candidates**, six about movement. It recommends building one or two: a bridge that is solid only
  in a freeze (the frozen world is drawn as a pencil storyboard, and here the drawing becomes a place to stand),
  and fire and blades that kill enemies too.
- **Two mechanics that need no code**: a rolling bar that kills in live time is a bridge when frozen level, and a
  platform too fast to board becomes a stepping stone when frozen.
- **A new first lesson for the code door**, the room both testers failed. The plates sit behind a timed door, so
  the clap the player already knows (hold the door open) is the same clap that shows the marks, right above the
  plates.
- **A run order of 12 rooms** that teaches each piece alone, then under pressure, then combined, and a room pool
  with "teaches" and "needs first" tags so a run can vary.

Its shortlist, in build order: the code door lesson, a fight with four Rushers and two Grunts, the stepping-stone
platform, the bar bridge, then the pencil bridge. The first four are data only and take the run from 8 rooms to 12.

What I checked: the files exist, the page loads nothing from outside, and I looked at three of its rendered tiles.
The tables and maps read. I did not check the maps against the room loader; the lane lists that as unchecked too.

What the lane says it is unsure about: whether a frozen bar up to 30 degrees off level can be walked, whether a
platform drops the player when the freeze ends, whether a platform breaks a Marksman's sight line, and whether two
Marksmen at once is too much damage.

Nothing from this is built until the owner picks, with one exception I am proposing to the owner: the code door
lesson, since teaching each new piece was already one of the owner's notes.

Separately, the owner asked whether work can run in parallel, with under two days left. It can: each code lane gets
its own copy of the project on its own branch and I merge them one at a time, with packaging and the scripted run
kept serial on the merged build. This PC has 8 threads and little free memory, so two code lanes at once. Neither
worker PC has the engine installed.

### 16:36. The owner: levels must be procedural, and more PCs join the build

Two directions from the owner after he saw the 16 hand-designed rooms and my plan for two parallel lanes.

On the machines: "all the systems are mine, and my internet is fast. we can easily set up all the pcs except pc3
(no gpu) to do work. usage wise: well scoped tasks can go to opus, open ended tasks to fable."

On the levels: "for the level design, it should be modular and procedural, like how we did [another of our games].
remember that it has roguelite mechanics so playing the same few levels over and over again is boring and defeats
the purpose of being a roguelite, and the game is solved in a matter of minutes or hours with static designs."
SUPERCUT's level generator was written during the jam, from scratch. No code from that other game was used.

He is right about the levels, and play-testing had already shown it: a known run of the eight fixed rooms takes 45
seconds and the door codes never change. The 16 rooms from this afternoon were fixed designs. They are not
wasted: their pieces, mechanics, teaching order and "teaches / needs first" tags become the generator's vocabulary.
But the plan to build four of them as fixed rooms is dropped.

Two lanes started at 16:36. Neither writes the game.

- **`gen1` (Claude Fable 5.2, high): the generator, as a prototype outside the game.** A room in this game is a
  text file, and the packaged game reads room files loose from disk. So a generator written in Python can emit
  rooms that play in today's build with no compile. The lane decides the module design, writes the generator and a
  fairness checker (gate reachable with the real jump numbers, every puzzle solvable inside the charges, nothing
  overlapping, a player with no charges can still finish), runs the checker over at least 1,000 seeds per depth,
  loads at least 60 generated rooms in a copy of the packaged game, and writes the spec for the C++ port. It is
  written to be ported line for line: its own small random generator, integer centimetres, and test vectors
  (seed in, hash of the room text out) that the C++ version must reproduce. Its first hour ends with a page of
  maps from generated rooms for the owner to look at.
- **`farm1` (Claude Opus 5.5, high): three more build machines.** It copies the engine to three of the owner's
  PCs, installs the compiler where it is missing, and proves each one with the project's tests and the scripted
  run. The model is simple: agents and git stay on the main PC; a lane mirrors its files to a remote PC and runs
  the build there over ssh.

The plan for the generator has a safety net. If the C++ port is not done in time, the Python generator can
pre-make and check a large pool of rooms that ships as data, and the game picks from the pool by seed. I will say
in the submission which of the two shipped.

The first feel lane has made both of its commits (gun items, then the new defaults). The scripted run still
finishes in one take with 17 kills. Its report is not in yet.

### 16:55. The gun feel is in the game; two code lanes now run side by side

Lane `feel3` finished. Two commits: `584e9b1` (the gun's shot, kicks, flash and mouse) and `683bff6` (the feel
study's default changes).

What it built, each number a tuning line the owner can change with F5:

- **A louder shot.** A low layer under 120 Hz, made by code. The shot's energy below 120 Hz went from about -15 dB
  of the total to about -3.5 dB. The player's shot is now 2 to 4 dB over a Grunt's shot heard from 10 m (it was
  about 1 dB under), and at least 6.5 dB over the music. Nothing else got louder.
- **A view kick** on each shot that stacks to a cap and leaves the aim alone, and **a gun kick** with variation.
- **A longer, larger muzzle flash** that turns and scales at random.
- **The mouse.** Measured with real input on the GTX 1070 PC, degrees turned per mouse count:

| Build | live | during the snap | frozen |
| --- | --- | --- | --- |
| before | 0.1625 | 0.1475 | 0.1540 |
| field-of-view scaling off | 0.1540 | 0.1540 | 0.1540 |
| new default | 0.0665 | 0.0665 | 0.0665 |

  The game had been turning slower in a freeze than live. That is gone, and the default is now 0.43 of what it
  was. Sensitivity and volume take typed values and smaller steps.
- **The defaults:** fire interval 0.25 to 0.18 s, shot speed 9000 to 14000, bigger hit, kill and clap feedback.

![six shots in a row](pictures/feel3/six_shots_strip.jpg)

What I checked against the files: both commits, a clean tree, 112 tests pass and none fail in the final test log,
the same run line in all six final run logs (`takes 1, time 98.2 s, shots 46, freezes 14, kills 17`, Development
twice and Shipping once after each commit), package files written after the last commit, and the new values in the
packaged tuning file. I looked at the flash pictures.

What is wrong, in the lane's words and mine: the flash is a smooth glowing ellipse. It reads as a lit bulb, not a
gunshot, and six in a row look nearly the same. A new shape is in the next lane. Nobody has played or listened to
this build yet; the sound rests on measurements. A saved sensitivity from before this build will feel slower.

The build is in the owner's play folder and on both testers' PCs (swapped while their game was closed).

**Two code lanes started at 16:54, the first time two run at once.** Each has its own copy of the project.

- `feel4`, in the main copy: wall marks, chips and shells that stay, and the shove on a hit.
- `feel5`, in a second copy on its own branch: the reload that starts by itself, the path line on hanging shots,
  a muzzle flash that reads as a gunshot, feedback on the freeze release, and a lower shot in a freeze.

To keep the merge clean, each lane adds its tuning lines in a different block, puts its tests in its own file and
does not reformat anything. The second copy does not package, because the package scripts write to one fixed
folder. After both finish I merge, and the merged build is packaged and run through the scripted run.

Gotchas from `feel3` worth keeping: once files are committed the build merges test files into one unit, and two
anonymous helpers with the same name then clash (it passed while the files were uncommitted); a PowerShell
function named `Move` loses to the built-in alias; and the sound tool re-imports all 65 sounds, so the unchanged
ones must be restored.

### 17:33. The owner played the feel build: nine notes, and what each one started

The owner played the build from 16:53 and wrote nine notes. His words, then what I did with each.

1. "for the flash, why do we need to use a shape? does unreal not have [another platform] style particle emitters? we should be
   using vfx." **He is right, and the cause was my brief.** I had told the flash lane to build the flash from mesh
   and to avoid particles, carrying over a rule about default particle textures too broadly. New lane `vfx1`
   (Claude Fable 5.2, high): find how to author Unreal's particle system without a person at the editor, draw the
   textures by code, and build the flash, shot impacts and enemy hit and kill bursts. The mesh flash item was
   pulled from lane `feel5`.
2. "when spam firing the gun, it has weird pauses, usually on the last bullet, shouldnt happen". A bug. Added to
   `feel5`: reproduce it in a test at 8, 12 and 16 clicks a second, find the real cause, then fix. A click that
   comes too early should be held and fired when the gun can fire.
3. "for the UI overhaul, I have a reference game in mind to use as reference. should I record a video of me in
   their UI?" Yes. Answered below.
4. "same for the bot movement and such, I can record a video and you can use our mocap pipeline to get the
   animations?" Yes to the video, no to our tool: it is under a non-commercial licence and must not ship in a
   game. The jam's Rokoko perk is the clean route.
5. "sounds - currently they are all code generated correct? they sound obviously synthesized and fake. find cc0
   sounds or we can generate our own for any poor fits". Correct, all 65 are made by code. New lane `sfx1` (Claude
   Opus 5.5, high): audit them, find CC0 recordings that need no sign-in, cut and level-match candidates, and
   build a listening page, since only the owner can judge by ear. It lists what has no good CC0 fit for generation.
6. On the code door puzzle: "gameplay is terrible. the dots under the letters can be misconstrued as amount of
   bullets needed and so on, and how they activate, and the sliding block adds nothing except visual clutter rather
   than true difficulty. scrap this first and do more platformer style puzzles instead". **The code door is
   scrapped.** Two testers had already failed to read it. The generator lane `gen1` was told: no code doors, and
   puzzles become platformer puzzles (frozen platforms as steps, a frozen bar as a bridge, pits and lava with the
   real jump numbers, timed doors, frozen crates as steps).
7. "proper animations for the first person viewmodel. find any free revolver animations, or we will make it on our
   own. for the clapperboard, I have a concept idea and I can record a real life video". Passed to the art thread,
   which is fitting the hands. The board's motion can be keyed straight from his video.
8. "first person arms clipping into the wall when touching the wall ... maybe unreal has a fix for this that isnt
   shrinking the player's viewmodel? find something and fix". Unreal 5.9 has first-person rendering for this; I
   found the types in the engine headers before writing the task. Added to `feel5`, with a rule: no shrinking and
   no second camera as a fallback.
9. "environment is too bare ... we are going for a realistic look, and some of the generated props look like
   cartoon or low poly models instead of proper realistic things. quixel megascans should also be used for props
   and textures since its free. the skybox is just plain black, make it look like a film set warehouse, with
   scaffolding and such. props can be like green screens, fill lamps, boom mics, cameras". Passed to the art
   thread as he asked: redo what fails (the chair first), many more realistic film-set props in batches, a
   soundstage hall kit, and a list of library assets for him to claim. The generator got prop slots, so rooms are
   dressed by seed.

Running at 17:33, seven lanes:

| Lane | Model | Doing |
| --- | --- | --- |
| `feel4` | Opus | marks, chips and shells that stay; the shove (main copy) |
| `feel5` | Opus | automatic reload, the spam-fire bug, path line, arms through walls, release feedback (second copy) |
| `vfx1` | Fable | particle effects (third copy) |
| `gen1` | Fable | the level generator prototype |
| `farm1` | Opus | engine and compiler on four more PCs |
| `sfx1` | Opus | real recordings for the sounds |
| art thread | Opus | props, hall kit, hands and animation |

### 17:42. The art thread started six lanes for realistic props, the hall and first-person animation

The art thread answered the owner's ninth note by starting six helper lanes. All six follow one spec file,
`lanes/PROPS_REALISTIC_SPEC.md` (70 lines; I read it). Each prop comes with a small JSON: category, size in cm,
triangle count, whether it blocks the player, a size class (`cover`, `tall_decor`, `small`), its source and its
licence. The size class and the blocking flag are what the level generator's prop slots need.

| Lane | Makes |
| --- | --- |
| `setA` | lights on stands, softboxes, work lights, C-stands, flags and reflectors, boom mics |
| `setB` | director's chairs first, cameras on tripods and on a dolly with track, green and blue screens, monitors, carts, clothes rails, ladders |
| `setC` | road and flight cases, pallets, crates, sandbag piles, apple boxes, cable drums and runs, paint and tools |
| `hall1` | the soundstage hall kit: concrete floor, padded and plain walls, sliding stage door, scaffolding, truss with hanging lights, catwalk, roof, and a sample layout for one corner |
| `fablist1` | an audit of every earlier prop (keep, replace or drop), the list of library assets for the owner to claim, and a CC0 list |
| `anim1` | free first-person revolver animation sets, a hand-keyed plan with timings, and a filming guide for the owner's clapperboard video |

Two open points, both the owner's:

- **Green screens against the green signal.** The spec bans signal colours on props (yellow, red-orange, green,
  cyan carry meaning in the game) and makes one exception the owner named: green screens. Green is the "way on"
  colour. My pick `[taste: owner review]`: blue screens inside rooms, green screens only out in the hall beyond
  the play space, where nothing asks the player to read a signal.
- **Hands.** Still waiting on the owner. Nothing is imported until he picks.

Each prop lane reports when a batch of about five props is ready. I start the import lane then.

### 17:49. First maps from the generator; the hands' motion will be made by code; build load moves off the main PC

**Generator.** Lane `gen1` reached its checkpoint: a design page and a page of maps, 72 generated rooms, rebuilt
after the code door was scrapped. I read the design and gave the owner the maps page with two questions, because
both are cheaper to change now than after the port into the game:

- A room is a start, a row of modules and a gate, so rooms are straight strips. Does that read as corridors?
- Puzzle rooms and fight rooms alternate strictly. That follows from a rule in the game (no refill pad beside
  enemies), not from a design wish.

What I checked myself: the files exist and the page holds 72 maps. I have not judged the layouts.

**First-person animation.** The art thread's research lane `anim1` looked for free first-person revolver animation.
Its finding: none fits. Epic's free clips are a magazine pistol on another skeleton, the free community sets are
full-body or have unclear licences, and the one close match is paid and reloads by swinging the cylinder out, which
the owner had turned down. So the motion is made by code on the gun's existing parts: the hammer rests cocked and
falls on the shot, the kick gets a spring settle, the reload tips the gun out of view and back, plus idle
breathing, look lag and a draw. Fire rate and reload time do not change. I wrote the task for a new lane `view1`
from that plan. It starts after lane `feel5` is merged, because both edit the same file. One thing the plan had not
measured and the task now demands: that the reload really takes the gun out of the frame.

For the clapperboard the owner will film his own hands. The board's motion is tracked from three tape dots in the
video. No body capture is needed, since only the board and one hand are in view.

**Memory.** The main PC fell to 0.5 GB of free memory with three compile lanes and a running game on it. The second
PC had by then passed every farm check (build, 112 tests, both packages, the scripted run with the same result
line; a nine-file rebuild in 56 s against 137 s). I told the farm lane to write the how-to for that PC first, and
told `feel5` and `vfx1` to build there as soon as it exists.

### 18:12. First realistic props arrive; an import lane and a download agent start; usage becomes the limit

**Audit.** The art thread's lane `fablist1` audited every prop made so far against the owner's new bar. Its finding:
none of the 13 generated props in the game passes; they all carry the earlier card-and-balsa look. 17 to replace,
4 kit pieces to keep with real textures, 29 to drop (the desk-scale props no longer fit a real-scale soundstage).
It also wrote a list of 30 free library scans for the owner and a list of CC0 models and textures.

**The owner's instruction, in his words:** "spin off an opus subagent on [another account] to cua my firefox to
download the fab stuff, im already logged in, let it accept any agreements it asks for." Until now my rule for
agents was no store actions and no accepting licence dialogs. The owner lifted it for this one job, so lane
`fabdl1` (Claude Opus 5.5, high) drives his browser for the 30 listed free items only. Its limits, from my brief:
its own browser window, in the background, never his open tabs; it never types a password, code or payment detail;
it stops on a sign-in page, a CAPTCHA, a payment step or any price above zero; every file gets a ledger line with
its hash; nothing is unzipped.

**First batch.** Lane `setC` delivered nine props: two road cases, a pallet stack, plastic crates, a steel drum, a
pallet and three cable pieces. Three come from a CC0 library, the cases are generated, the rest are built by script
with CC0 wood texture.

**Import lane `props1`** (Claude Opus 5.5, high; its own copy of the project). What I asked for and why:

- An import script with one PBR material, and a texture size budget. The submission zip must stay under 1 GB and
  the package is about 232 MB now. Sixty props at full texture size would not fit, so textures come in at 1024
  unless the player stands next to the prop.
- A catalogue text file that both the game and the level generator read, so the generator picks real props by
  category and seed.
- Props that block. Decoration in the game is walk-through today and cover is plain boxes. A blocking prop must
  behave exactly as a box of its size does, for the player, shots and enemies.
- The eight hand-made rooms get the new props as decoration only, so the scripted run's result line cannot change.
- The enemies get the approved revolver in place of two pistols that failed the audit. My pick
  `[taste: owner review]`: the picture tool refused gun prompts twice today, so a new realistic pistol would be slow.

The generator lane got the same catalogue format, so the two meet without waiting for each other.

**A lane that kept stopping.** Lane `feel4` ended its turn twice while a build it needed was still running. Each
time it was woken when the build ended, so no work was lost, but its log has a gap. New briefs now say: do not end
your turn while a step you need is running.

**Usage.** The main account's weekly use went from 63% to 73% in ninety minutes, with three Fable sessions on it.
The other two accounts moved one point each with Opus lanes. Free PCs are no longer the limit; usage is. From here
new lanes are Opus on the other two accounts, and Fable is kept for work that is open-ended.

### 18:14. The build farm is ready: three more PCs build, test, package and run the game

Lane `farm1` finished. The owner had said at 16:36 that every PC of the team except one may be used. Result:

| PC | Ready | Can do | Cold build | Tests | Dev package | Scripted run |
| --- | --- | --- | --- | --- | --- | --- |
| second | 17:33 | build, test, both packages, run | 69 s | 52 s | 254 s | 118 s |
| third | 17:58 | build, test, package, run | 116 s | 119 s | 303 s | 179 s |
| fourth | 18:02 | build, test, package, run (slow) | 277 s | 91 s | about 380 s | 472 s |
| fifth | compile only | build | 101 s | no | no | no |

What I checked myself, in the lane's proof logs: the third and fourth PCs each printed the main PC's exact result
line for the scripted run (`takes 1, time 98.2 s, shots 46, freezes 14, kills 17`), and each step's exit code was 0.
The same line from a different PC, and on the second PC from a newer compiler, is the strongest sign so far that
the scripted run is repeatable.

How it works: the other PCs hold plain copies of a project folder. Git, the agents and the source of truth stay on
the main PC. A wrapper script mirrors a lane's copy, runs a step and brings the logs back with user and computer
names masked.

Limits the lane found, kept as they are:

- A game started over a remote shell cannot open a window, so runs are offscreen. Pictures are real frames; frame
  rates are not what a player sees.
- The fifth PC's Windows security blocks game code that we build, so it can only compile. The lane changed no
  security setting. Whether to change it is the owner's call, and my advice is to leave it: three PCs are enough.
- One game per PC at a time. Two started together from one package folder, and one crashed at start.
- The build that goes to the judges is compiled on the main PC, because one of the others uses a newer compiler.

The lane also reported its own mistake: it ran the two-games test while that PC was at full load from two lanes'
builds, after its own load check had shown it.

Use from now: `feel5` and `vfx1` build on the second PC, `props1` on the third.

### 18:33. The owner's reference video, the hall kit, the library downloads, and a privacy catch in this log

**Reference video.** The owner recorded 15 minutes of another game's interface at 60 fps as a reference for the
interface overhaul, and wrote: "it also has information regarding the revolver animations, and how the hand moves
off the revolver when the clapperboard is used, so analyze it in detail." I looked at one sheet of twenty frames to
see what it holds (menus, settings, an in-game HUD, a first-person revolver in a practice range) and checked the
audio tracks for a voice-over (there is none). Then two lanes, both Claude Opus 5.5, high:

- `uiref1` measures layout, hierarchy, states and transition timings frame by frame and writes an interface spec
  for our own screens, plus a mock page with two identity directions of its own for the owner to choose from.
- `animref1` measures the revolver's fire, recoil, reload and draw, and the moment the support hand leaves the gun,
  then writes a diff of numbers against our animation plan and a beat-by-beat clapperboard move in two versions.

The line I drew in both briefs: the reference is for layout, timing and motion. No logo, colour scheme, icon,
font, wording, model, sound or animation file is taken from it, and no frame of the video goes into a repository
or into this log. The jam forbids trademarks and the game has to be our own work. What the lanes take from the
recording is measurements: timing, layout and motion, written down as numbers and as our own spec. Nothing from
that game is in the build.

The owner's sentence also changes a design point. Today the board is always in view in the left hand. He describes
the left hand resting on the revolver and leaving it to clap. That version needs hand meshes with fingers, and the
hands are still his open decision, so the study specifies both versions and I asked him.

**Hall kit.** The art thread's lane `hall1` delivered 19 modular hall pieces on a 4 m grid (floor, walls, columns,
scaffold, truss, a lamp) with five shared texture sets from CC0 libraries. The import lane takes them in as an
early commit of their own, so that a lane building the hall around every room can start from it. That task is
written and waiting. At 18:34 the second batch completed the kit: 28 pieces, 5,664 triangles in all, with a stage
door, catwalk, roof and three lamps, and a sample corner of 458 placed pieces.

![The hall kit's sample corner, rendered by the art lane: over 4 m set walls, over 4.8 m walls, with no walls, and from above](pictures/hall1/hall_4up.jpg)

I looked at the renders. The hall reads as a soundstage. What is wrong in them: everything is one grey, the wall
panels repeat as a visible pattern, and no lamp is lit, so light and haze in the engine have to do a lot. The set's
wall height decides how much shows: well over 4 m walls (top left), the top half over our 4.8 m walls (top right).
My pick `[taste: owner review]`: generated rooms get 4 m walls. The real jump is 1.1 m, so nothing becomes
climbable. The generator lane was told, with the height kept in one place so it can go back.

**Library downloads.** Lane `fabdl1` finished the job the owner gave it: all 30 free scans are in his library and
on disk, 388 MB. I checked every file against the lane's ledger by size and SHA-256: 30 of 30 match. The store
showed no licence dialog and no tier choice, so the permission to accept agreements was never used. The lane
flagged five items whose previews show colours our rule forbids on props (orange, green) or a possible printed
label; those went to the art thread with the files.

**A privacy catch.** To find its downloads, that lane listed the newest files in the owner's download folder, and
five of his own file names came back in its session. Sessions are exported into this log. The check I run before
every push showed the listing, so nothing left the PC. The fix had three parts:

1. The lane was told at once to ask only for archive files created after its own start time.
2. A script reads the listed names out of the exported session and adds them to the local mask list. I did not
   read the names myself.
3. My first version of that script was wrong twice, and the checks caught both. It added the mask text itself as
   a private word, which made the exporter's own leak scan fail. And it masked two names that are one ordinary
   word, which blanked that word in about 45 places in older sessions. Those two word-only masks are gone. Two
   of the five names belong to jam downloads that an earlier lane had already named in this log; they stay masked
   now, which hides a file name in that older session in 15 places. I left it: too much masked is the safe side.

The lesson goes into my briefs: a lane that must find its own files in a personal folder filters by time and
type and never lists the folder.

### 18:43. Props you can shoot through, and where the code lanes stand

**Second prop batch.** The art thread's lane `setB` delivered seven props: three director's chairs, a cine camera
on a tripod, a grip cart and two wooden step ladders. Its note on the chairs and ladders: they are frames, so they
should stop a walking body but not a line of sight.

That needed a rule the prop catalogue did not have. A prop was either a full box (stops the player, enemies, shots
and sight, so it is cover) or decoration (stops nothing). A full box round a ladder would stop bullets in thin
air, and counting a chair as cover would lie to the player about where they are safe. So the catalogue line gets a
third state, `open=1`: the prop stops walking bodies only. Shots and enemy sight pass through, it never fills a
cover slot, and nothing leaves a mark on its box. `[taste: owner review]`

Both lanes that read the catalogue were told in the same minute: the import lane (sets `open=1` from the prop's
notes and for chairs and ladders, with a test that a shot and an enemy's sight check pass through a prop that
stops a walking body) and the generator lane (open props are obstacles when it checks that a room can be crossed,
and are never placed where its rules ask for cover).

**Code lanes, read from their commits at 18:43.**

- `feel4` (main copy): two more commits. The footstep pace now follows a tuning line, and a chain of kills raises
  the kill sound a semitone per kill. Its handoff is still to come.
- `feel5`: the held revolver and clapperboard are drawn near the eye and no longer poke into walls, which was the
  owner's note 8. Two items left.
- `props1`: two commits. The import pipeline for the realistic props with the first nine imported, then the
  catalogue file read at game start, with room files placing catalogue props by name. The hall kit import is
  next, and the hall lane starts from that commit.
- `vfx1`: no commit yet, 17 changed files in its copy.

Nothing is merged yet. The play build is still the one from this afternoon.

### 18:51. The hall lane starts, recorded sounds go in, and the usage budget

**The hall lane.** The import lane committed the hall kit at 18:46: 28 pieces, five shared texture sets, 37 props
in the catalogue. Before trusting it I read the commit: 28 hall lines in the catalogue file, and the lane's log
shows it compared each piece's bounds with the art lane's notes, so nothing came in mirrored, and ran the 119
tests. Lane `shell1` (Claude Opus 5.5, high) started from that commit in its own copy. Its job is the owner's
note about the black void: a soundstage hall built by code around any room, from the room's bounds, with no line
needed in the room file, so it also works for generated rooms.

**More props.** Three more batches from lane `setC` (15 props: road cases, a wrapped pallet, a crate, sandbags,
small paint and tool props) and a first batch from lane `setA` (stands, flags, reflectors, a mic stand). I counted
the files and read each lane's check file instead of taking the message's word. That caught a mismatch: the setA
message lists nine props in one folder, and on disk five are there and four are in another folder, because the
lane was still moving files. The import lane was told to take whatever has a passing entry in the check file.

**Cover by height.** Two sandbag props are 55 and 61 cm high and were delivered as cover. I checked the source:
the player has no crouch. So a low prop blocks movement and shots below its top but hides nobody. The generator
lane got the rule: where a line of sight must be broken it uses props of 150 cm or more; lower ones are obstacles
and steps; and nothing it places may let the player climb out over a wall. `[taste: owner review]`

**Recorded sounds.** The owner's note on the last build was that the sounds are fake. They were: every sound was
made by code. Lane `sfx1` (Claude Opus 5.5, high) searched CC0 libraries and cut candidates for all 48 sounds: 38
now have a recorded pick, 10 keep the code-made version because no recording fit. It built a page with a player
for the current sound and two or three candidates per row. I checked the page: 248 players, every file exists,
nothing loads from the web.

Two honest limits in its report. No agent has heard any of these, because agents play no sound on this PC; the
lane used measurements and an audio-description model, and says that model is weak on hits under a second. And
71 of the project's own sound checks fail on the recordings, all of them rules written for code-made sound
(spectral centroid, attack time, a cap on energy above 6 kHz). The hard rules pass: format, peak level, silence
at both ends, loop seams, loudness by family.

My call `[taste: owner review]`: import the 38 picks now and let the owner judge them in the game, where they are
heard in context, instead of waiting for him to audition 248 clips. The same lane does the import in a second
round, in its own copy, with three conditions: the sound checks are split so that the code-made rules apply only
to code-made files and no check is left failing; the tool that re-renders sounds from code can no longer wipe a
recording; and the scripted run must print the same line as before. Sounds that would need a sign-in to download
or a paid generator are left out.

**Usage.** The plan limit on the main account stood at 79% of the week at 18:47, six points up in forty minutes,
and it resets at the jam's deadline. The other two accounts are at 72% and 75%. I told the owner, and from here
no new lane runs on the top model: new work goes to Opus on the other accounts, and this thread writes less.

### 19:17. A wrong reading of the owner's reference video, and what it cost

This entry is mostly about a mistake of mine.

**What happened.** At 18:15 the owner gave me a 15-minute recording of another game as a reference for the
interface and for the revolver's motion. Before briefing two study lanes I checked whether it had a voice-over.
The file has three audio tracks. One is digital silence. I compared the other two, found them almost the same,
and concluded: game sound only, no commentary. Both lanes were briefed with that sentence and given the audio of
one track.

The owner talks through the whole video. His voice is in both of those tracks, which is exactly why they looked
the same. A comparison can only show what differs. I never ran the one check that answers the question, which is
to transcribe the audio.

**How it came out.** At 19:01 the motion lane reported. Its main finding on the hands was that the reference
game holds the revolver in one hand, with the left hand resting out of view. I passed that on, with a
recommendation built on it. The owner's answer:

> "you read the video of the game wrong. the left hand IS resting under the right hand, supporting the revolver.
> its just unclear because they arent well seperated, which is why I played the inspect animation for you to see
> the hands clearer. [...] I think the video read skipped too many frames or wasnt detailed enough, did it even
> see where I used the ability, and did it transcribe my commentary?"

Then I made it worse for five minutes. My first attempt to recover the voice subtracted one track from the other
and transcribed the difference. It came back empty, the difference was silent over the menus, and I told the
motion lane that the microphone had probably not been recorded. A direct transcription of one track was already
running. It returned a hundred lines of clear speech. I corrected the lane before anything was built on the
second wrong statement, and I had not yet told the owner his commentary was lost, which would have sent him to
re-record it.

**What the commentary says.** It is a list of instructions, with times. The ones the first pass missed or got
wrong:

- The grip is two-handed: "the right hand rests above the left hand holding the grip and that's how we should do
  it as well."
- "The first person perspective should be copied exactly like this [...] slightly off-center, see the back of
  the gun well and it's pointing straight." The gun's place on screen was later solved from sights the owner
  posed himself on our own model (15 Nov 13:40 below).
- On the reload: "that is the exact reload that I want." The plan had the gun dip out of frame during the reload.
  The motion lane wrote the reload down as timings and a path; ours is built from those numbers on our own
  model, and no animation file came from the video.
- Jumps and walking in four directions, shown twice on purpose so the view model's bob can be measured. The
  lane's report had listed these as "none clean".
- Not wanted: aiming down sights, an inspect animation.
- Interface: square tiles, a clear font, sound on hover and on click, glow and outline highlights, our own
  colours and background, a pause menu that slides in from the left, full crosshair customisation, and most of
  the reference's video and audio settings. That last one is a list of which options to offer; the screens,
  icons and wording are our own.
- One sentence settles an open question: "We'll have DLSS so we are eligible for that prize." It is also there
  for players: DLSS and DLAA ship as a choice in the game's upscaling setting (lane `dlss2`).

**The clapperboard, decided.** In the same hour the owner sent his own clip of a real clapperboard and described
the move: the left hand supports the revolver, leaves it and brings the board up, the board snaps, there is a
pause in which the picture turns to the sketch look as a sweep through the room from the furthest point to the
nearest, the board breaks apart, and the hand goes back to the gun. He also wrote "do NOT build a) board always
in view". That was the version I had picked twenty minutes earlier. Nothing of it had been built.

**What changed.**

- Both study lanes have the transcript and were told that his words outrank their own reading of the picture.
  The motion lane redoes the hold frame by frame, measures the placement of the gun on screen, the reload, the
  bob and the hand leaving the gun, and measures the owner's clapperboard clip, mirrored because he used his
  right hand. Its frames stay outside every repository, since the clip shows him and his room.
- The task for the view model lane no longer contains a clap step. It waits for the corrected numbers.
- The art thread was asked for a third hand pose (left hand supporting the right) and for the poses as bone
  tables, so that code can blend between them.
- A research lane (`dlss1`, Claude Opus 5.5, high) works out whether DLSS can go into this engine preview in the
  time left, and what the owner has to do by hand. Agents here do not accept licences, and the plugin has one.

**What I take from it.**

1. For "is there speech in this file", transcribe it. Do not infer it from levels or from comparing tracks.
2. When the owner hands over a recording, assume he is narrating it until a transcript says otherwise.
3. A study lane's surprising finding ("the reference never does the thing the owner pointed at") is a reason to
   look at the frames myself before passing it on. I passed it on.
4. Twice today I wrote a clock time from memory into a message to a lane and was minutes off. The clock is one
   command away.

### 19:35. Generator finished, recorded sounds in the play build, DLSS researched

Four lanes reported inside twenty minutes. What each delivered, and what I checked myself.

**Room generator (lane gen1, Claude Opus 5.5, high): done.** A room is made from a seed and a depth out of 16
modules. A checker refuses any room that is not fair, for example one where the player can be shot before they
can see the shooter. By the lane's numbers: 15,000 rooms checked with and without props, 14,999 fair on the first
try, 70 rooms loaded in a packaged build, nine played to the exit gate by script. The lane wrote three ways to get
the generator into the game. I picked the simplest, baking: the Python generator writes room files ahead of time
and the game only has to choose a run by seed. A second lane (gen2, same model) is doing that now, 50 runs of 12
rooms, and its bake commit is already on its branch. Props come later as a data step, once the prop catalogue is
merged.

**Gun feel, round 4 (lane feel4): finished at 19:24.** Its commits were merged one at a time as they passed; the
last ones add spent shells and impact chips. The scripted reference run prints the same line as before. The lane's
own verdict on its pictures: the shells are hard to see and the chips "look like dark dice". Both go on the
polish list. I did not argue with it; the pictures agree.

**Recorded sounds (lane sfx1, round 2): merged at 19:31.** 38 of the game's 48 sounds are now CC0 recordings
instead of synthesised ones. The owner's note that started this was that the sounds were "fake". The branch
holds only sound files, sound assets and the tools that cut them, no game code. Six shots at the full fire rate
do not blur: each tail is 19 dB down when the next shot lands. Nobody has listened to them in the game yet. I
cannot play sound on this PC without disturbing the owner, so his ears are the first real check, and I told him
so.

**A problem I have not solved.** The PC that must compile the judges' build had 0.8 GB of memory free when the
sounds were merged. Agent sessions hold most of it. It could not package the game, so the build in the owner's
play folder came from a farm PC that built the same commit; I compared its room, run and pak file counts with the
last package made here before copying it in. That is fine for a play test. It is not fine for the submission. I
expect it to ease as lanes finish and will check before each merge.

**DLSS (lane dlss1, research only): feasible, not certain.** The owner said in his commentary: "We'll have DLSS
so we are eligible for that prize." The lane read the award terms and the engine folder:

- DLSS Super Resolution or DLAA alone meets the award's terms. Frame Generation is not needed.
- There is no DLSS plugin for this engine preview. The newest is built for the previous engine version. The lane
  compared the two engines' upscaler interface files and found them identical, which makes a port likely to
  compile with small fixes. That is an inference until a build runs.
- The plugin sits behind a licence and probably a sign-in. Agents here do not accept licences or sign in, so the
  download is a hand step for the owner.
- The licence asks for a DLSS credit, and using NVIDIA's logo needs their written approval two weeks ahead. The
  lane's pick, which I agree with: a plain text line, no logo.
- A trap found before it bit: the game's ignore file would silently drop the plugin's DLLs from version control,
  and a build from a clean checkout would then ship without DLSS.
- The lane set a stop rule: if the plugin does not build and pass a no-change check on a non-NVIDIA card by
  Sunday 11:00, it is reverted.

Only one PC we have has an RTX card, and it is a teammate's working PC, so the build lane will share it with
three other lanes.

**Props.** The import lane is through the hall kit, the second prop set and into the third (its branch head at
19:35 is the lighting batch). The art thread closed two more batches, including five scanned props.

**Usage.** The main account is at 82% of its week with a day and a half to go, and the week resets at the
deadline. No new lanes start on the most expensive model. Everything launched this hour runs on Opus.

### 19:58. A merge, a second look at the reference, and three build lanes from the owner's own words

**Merged: gun feel, round 5.** The lane's six fixes went into the main branch at 19:40. Two lanes had changed the
same sound, the one that plays when hanging shots are released: this lane had rebuilt it by code as a stand-in,
and the sound lane had since replaced it with a recording. The recording stays. Then the check that matters: a
farm PC built the merged code, ran all 129 tests (0 failures), packaged it, and played the scripted reference run.
It printed the reference line, unchanged:

    RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17

That build is in the owner's play folder as of 19:57. Its log has 24 graphics errors at frame 0 on that PC's old
card. Logs from the newer PC have none. I have not looked into them further.

What the lane found is more interesting than the list of fixes. The owner had reported pauses when he fired as
fast as he could. The cause: a click pressed and released inside the gun's cooldown was simply dropped. A click
up to 0.12 s early is now held. At 8, 12 and 16 clicks a second the gap between shots is the same 0.183 s. The
lane also reported its own slips on the shared PC (one build started above the load limit, one run started while
another lane's editor was busy) and wrote itself a gate script afterwards.

**The reference video, read a second time.** At 19:17 I logged that the first reading of the owner's reference
video had the hands wrong because nobody had transcribed his commentary. The motion lane's second pass is back.
Its own account of the miss: it had sampled the clearest views of the hands at one frame every third of a second,
at low resolution, and read two dark overlapping gloves as one hand. This time it went frame by frame. Before
passing anything on I opened its strip of the hand-off myself: the left hand does come out from under the gun.

It also measured the owner's own clip of a real clapperboard. His move: rise 300 ms, hold open 250 ms, strike
150 ms with a slow start, snap with a small rebound, pause 1.25 s. In the game a clap has to stop the scene at
once, so the move is compressed: board up in 50 ms, snap at 150 ms, the sketch look sweeping the room from far to
near for 0.5 s, the board breaking apart at 650 ms, both hands back on the gun at 1.0 s. The shape of his strike
survives. Two things are my calls, not his, and are flagged for him: the pause is 0.5 s instead of his 1.25 s,
and the board sits left of centre so it never covers the crosshair. Each is one tuning number.

**The interface study, corrected.** The same commentary error had hit the interface lane. Its corrected spec
answers each of the owner's 54 statements in a table, with the time he said it. What changed: no rounded corners
anywhere, an outline and glow on hover, a sound on every hover and click, a pause panel from the left, six
settings tabs with full crosshair customisation and key rebinding. It left out three things he showed and gave its
reasons, for example a lens distortion switch for an effect the game does not have.

**Three lanes started at 19:57**, all Claude Opus 5.5 at high effort, each in its own copy of the project on its
own farm PC:

- `view1`: the gun's placement on screen, recoil, bob, jump and landing, and the reload kept in view.
- `clap1`: the clapperboard move, the far-to-near sketch sweep, the board breaking apart, the charge count on the
  HUD.
- `ui1`: the shared interface style, settings, title and pause.

They will collide in three files. Each brief names the other lanes, says who owns what, and tells the lane to put
its code in new files of its own with one call site. I resolve what is left at merge time.

**What I told the owner may not fit.** His "exact reload" has the left hand working the cylinder and the right
hand loading with a speedloader. That needs rigged hands, a new pose from the art thread and both motion lanes
merged first, then six to eight hours. The gun's own part of that reload is in `view1` either way.

**The cost of the error.** Both study lanes ran twice. The second pass of each exists only because of my mistake
at the start.

### 20:36. The owner dislikes the sounds, hands arrive, and the first particle effects are merged

**"Most of the sounds are unsatisfactory but I dont know where to begin."** That was the owner at 20:07, after
playing the build with the 38 recorded sounds in it. He also pointed at two more CC0 sources: a pack of gun
recordings he had downloaded, and a collection on OpenGameArt. I checked the pack's page before using it. It
states "CC0 License. Credit not required."

The hard part is that no agent here can hear. Measurements say whether a file is clean, how long it is and how
loud. They do not say whether it is good. So the new sound lane (`sfx3`, Claude Opus 5.5) is not asked to pick
better sounds. It is asked to make his judging fast: rank the 48 sounds by how often they play in a real run and
how loud they are in the mix, cut four to six candidates at equal loudness for the top dozen, render a stretch
of a real fight with one sound swapped at a time, and put it all on one page with a player per candidate and a
choice under each. Nothing is imported until he has picked. OpenGameArt refused my plain request for the page.
The lane may try once more the same way and otherwise lists what it wanted for the owner to fetch by hand.

**Props: all four art lanes are done.** Their batches went to one import lane, whose queue is now closed. One
question came with them: may scanned library props ship inside the game? I read the licence summary on the
store's own page. It allows distributing a project with the assets in it and forbids passing the assets on by
themselves. So they ship in the build, each one gets a line on the submission sheet, and the raw files stay out
of this repo.

**Hands.** The game has no hands: the gun and the clapperboard float. The art lane posed a rigged pair in a
two-handed hold and delivered the poses as data, with one warning I would not have guessed: a straight blend
from "left hand supports the gun" to "left hand holds the board" passes through the gun, so every blend has to go
through a third, clear pose. A build lane (`hands1`) is importing them behind a switch that is off by default.
The store listing for the hands shows no licence, so they stay off until the owner confirms it, and the lane
records every imported file so one commit can remove them.

**DLSS.** The owner downloaded NVIDIA's plugin himself. It is built for engine 5.8 and the jam runs on a 5.9
preview, so lane `dlss2` has to compile it against 5.9 and prove it on the one RTX card we have, with a check on
an AMD card that nothing changes there. The stop rule from the research lane stands: if it is not working by
Sunday 11:00, it is dropped.

**Testers.** Both testers' PCs got the Shipping build of the current main branch at 20:15. A slip of mine: I
left one flag off the scripted check run, so it wrote no log. The game's own end screen was captured as a
picture and shows the reference numbers (1 take, 1:38.2, 46 shots, 14 freezes, 17 kills), and that is what I
went by. The Shipping folder is 493 MB against 1,077 MB for the Development one I had been quoting, so the jam's
1 GB limit is less tight than I had told the owner.

**Merged at 20:35: particle effects.** Lane `vfx1` (Claude Fable 5.2) replaced the muzzle flash, which was a
smooth white bulb, with a flame of five uneven tongues, sparks, a wisp of smoke and a short light. Shots now
throw dust and scraps off walls and sparks off metal, and enemies burst in sawdust when hit. How it was built is
the part worth recording. Nobody opened the editor. One Python script drives the engine's experimental Niagara
toolset from the command line and rebuilds every effect in about two minutes, and the textures are drawn by a
second script. The lane lost an hour to an engine oddity it found by bisecting and could not explain: in a
system built this way, the last emitter does not draw sprites sized by an expression. Its cure is an empty
emitter at the end of every system.

The lane's own list of what is weak: the enemy hit burst is lost behind the game's existing hit flash and
marker, wall dust is faint from mid-room, and the scraps look like cut paper up close. It did not build the
fourth effect in its brief, the ring on a clap. I looked at its before-and-after sheet of six shots before
merging: the six flames differ from each other and stay clear of the crosshair.

The merge had one text conflict, two lanes adding tuning lines at the same place, and both blocks were kept.
The merged code is not verified yet. The lane tested on a base from before two other merges, and the farm PC
that runs my checks is busy with other lanes, so the build, the tests and the reference run are queued behind
them. Until that passes, the play build stays as it was.

### 22:20. The owner's ear beats my guess, the merge check catches two faults, and the revolver is to be remade

**Sounds: he picked, and he was right about the buzz.** The sound lane's page went to the owner at 20:38: the
ten sounds that matter most in a run, four to six candidates for each at equal loudness, a player per candidate.
An hour later he sent back a text file with thirteen rulings. Five sounds stay, six are swapped for a candidate,
and two get "none": the lava loop ("dont make it buzzing, pick another type of sound") and the marksman's aim
("too synthetic"). Under the footsteps he wrote that a static buzz was "terribly distracting and nauseating, i
think its the lava loop". I had told him earlier that the room tone was the more likely source. The lane then
measured both. The lava loop has 176 steady peaks holding 99% of its power, a 100 Hz series from 200 to 1902 Hz,
and three strips of lava run through the footstep test clips. The room tone was not it. He heard in a minute
what I had reasoned wrongly about, and I told him so. The lane is importing his picks and building a second page
for the two open sounds.

**The merge check paid for itself twice.** Every lane tests on the base it branched from. Only the main copy
sees the lanes together, so after each merge I run the build, all tests, a package and the reference run on a
farm PC.

- After the particle effects merge, one test failed: on the frame a kill lands, the gate was already open.
  The test log showed the shot landing on frame 946 and the gate opening on 947. The cause was tick order. The
  room checks for a clear floor in its own tick, and the engine runs the room and the shot in no fixed order, so
  the gate opened on the kill frame or one frame later depending on which ticked first. I did not loosen the
  test. A kill now asks the room on its own frame, the room's tick asks through the same function, and the 135
  tests and the reference run passed.
- After the generated-runs merge, one test failed again, and this time the test was the fault. The effects
  lane's test named the tuning section that follows its own block, and the runs lane had added a section there.
  The test now names the right one. The re-check is running as I write.

**A fault nobody could see in the editor.** Reading the log of a packaged run for something else, I found two
warnings that a material lacks the usage flag for instanced meshes, with "Default Material will be used in
game". Spent shells, landed chips and wall marks are instanced meshes. A run through the editor sets that flag
in memory, so no lane's run ever showed it, and every lane had tested that way. A small lane (`litter1`, Claude
Opus 5.5) has the fix, with one condition: show the fault in a picture of a packaged build first. I have only
the warning lines, and if the litter looks right in spite of them, the fix I described is wrong.

**The farm starved my own check.** Three PCs build for nine lanes. Each lane waits until a PC looks idle, and
so did my merge check, polling once a minute. Two lanes on the same PC took turns for half an hour and the
check never got a slot. The status script now reports the PC as busy to every lane while a flag file from the
main thread is fresh, so the merge check goes first. It is a few lines and it is the first piece of scheduling this
farm has.

**Generated runs are merged.** Lane `gen2` baked 50 runs from the room generator and a plain start now plays one
of them instead of the hand-made run. Three of them were played through by script on the lane's base. On the
merged code that is not proven until the re-check passes, and the play build stays on the last verified commit.

**Hands: the licence is settled.** The art thread read the store page: Creative Commons Attribution, free, AI
use allowed. They can ship with a credit line in the game itself. The game has no credits screen yet, so the
hands stay behind their switch.

**The owner wants to pose the hands himself, and wants a new gun.** He asked whether he could pose the hands on
the revolver by hand, because the gun looked oversized or the arms undersized. The art lane built him a Blender
file with the gun, the hands and the game's camera, a one-page guide, and a script that brings his poses back as
the data the game reads, tested on a round trip. It also measured: the gun is 20.4 cm long against 22.5 for the
real thing, but its cylinder is 5.9 cm across against 3.7. The lane's verdict was "not too big, too fat", and I
asked for a slimmer variant. The owner disagreed ("in my opinion it isnt too fat") and asked for something else:
a new revolver from scratch, silver with a black handle, in the look of a real large-frame revolver he named,
and he approved more generator credits for it.

So the slim variant is cancelled and a new gun is ordered. It will be an original model of that real-world type.
Real photos are collected for looking at only and stay out of every repo. The pictures fed to the generator are
made fresh, with no maker's marks or text, and nothing comes from any game. He also asked whether the
generator's part-splitting feature is what separated the hammer and cylinder last time. It was not. The first
gun was generated whole and cut in Blender with hand-placed cut shapes and pivots, after the image tool twice
refused to draw an exploded revolver. The generator's public API documentation lists submit, status, download
and balance, and nothing for parts, so the same cut route is the plan. One thing the new gun gets that the old
one lacked: a crane, so the cylinder swings out and the reload can show the rounds leaving.

**A slip, again.** Twice in this stretch I wrote a clock time from memory and was off by several minutes. The
rule is to read the clock first. Both were corrected in the notes.

### 23:46. Five lanes land in one evening, and the fault that every test missed

**What reached the main copy since 22:20.** Each lane works in its own copy of the project on its own branch. I
merge, and a farm PC builds the merged code, runs every test, packages it and plays two scripted runs.

- Sounds, round two. The owner's thirteen rulings are in. The lane also built a second page for the two sounds he
  rejected outright, six new candidates each.
- The clapperboard move. At rest the board is out of view and the left hand supports the right on the revolver.
  On a clap the board rises, snaps, and the change from the real room to the pencil sketch sweeps from the far
  wall to the camera. That sweep works and I checked it in the lane's frame strips. The board's break does not:
  the owner asked for an explosion and the frames show two halves and a few specks. It is on the list.
- Props. 125 props in a catalogue the game reads at start, and the eight hand-made rooms dressed from it. The
  Development package grew from 1,075 MB to 1,469 MB. The entry has a 1 GB limit on the zip, so I am watching it.
- A fix for litter (spent shells, chips) that drew with the engine's default material in a packaged game.
- NVIDIA DLSS. The plugin is built for an older engine version, and the lane needed eleven small source edits
  to compile it for the 5.9 preview. On the RTX test PC it reports Supported and the game runs and quits in each
  mode. On the AMD test PC it reports NotSupported and the game behaves as before. One real problem came up: the
  game hung on quit on the RTX PC, and the lane's cure is to skip one shutdown call at exit. That is a workaround
  and I have recorded it as one.
- A soundstage hall round every room is finished on its branch and not merged yet.

**The fault.** The check of the clapperboard and props merges was green: 158 tests passed and both scripted runs
printed their expected result lines. Reading the cook log anyway, I found one line saying the props' master
material failed to compile and that the engine's default material would be used in the game. So every one of the
125 props would have drawn grey in a packaged build. Each lane's own package was fine. My reading of the cause:
the props' material reads a parameter from a shared set, the clapperboard lane re-made that set, and materials
point at such parameters by an internal id, so the reference broke only where both lanes meet. I have this from
logs and not yet from a picture, so the lane that fixes it has been told to show the grey props first and to
stop if they look right. It also adds a test that fails on any material compile error, because the lesson is
plain: our tests and scripted runs check behaviour, and nothing checked what the cook said. That build did not
go to the owner's play folder.

**Two faults in my own tools.**

- The mirror step hung on one farm PC and not on the other. A small PowerShell helper read its input "to the
  end", and on that PC a script started over ssh never sees the end of its input. The helper now reads up to a
  marker line. Two hung copies were ended by hand, mine and another lane's.
- A package failed to link with a missing function that plainly existed. I had merged a branch into the main
  copy while the farm PC was packaging the previous head. The farm's mirror keeps file times, so an object file
  compiled from the old source looked newer than the new source and was never rebuilt. I deleted that
  intermediate folder and the package linked. The rule now: no merge into the main copy while a check is
  between its mirror and the end of its package step. It is written down for the lanes too.

**The revolver is being remade.** The owner looked at the gun in his hands' view and asked for a new one from
scratch: a large-frame revolver with a silver body and a black grip, fully working like the first. He also
asked whether the generator's part-splitting page is available to us through its API. It is not: the API offers
submit, status, download and balance. The first gun was generated whole and cut into parts in Blender with
hand-placed cut shapes, and the new one is made the same way. An art lane generated candidates from fresh
input pictures, picked one, and cut it into body, cylinder, crane, ejector, hammer, trigger and round. This
time the cylinder swings out on a crane, which the first gun could not do. The lane swept every moving part
through its range and reports no intersections, with the smallest gap 0.31 mm at the trigger. It cost 7.5
generator credits of the 20 allowed. Nothing is imported yet. One number sets the gun's size against the hands,
and my pick is 0.87 of real size, where the trigger sits under the same fingertip as on today's gun. The owner
decides.

**A rule from the owner on helper accounts.** He told me which subscription each model's helper lanes may run
on. Every lane started since follows it.

**Clock.** Three more times tonight I quoted a time from memory and was off by two to eight minutes. The times
in this log come from the clock command, and I now run it before writing one in a message as well.

### 15 Nov 03:10. The grey props are fixed, four more lanes land, and the generated rooms get their dressing

**The fault from the last entry, fixed where it started.** The props drew plain grey in the packaged game because
their master material was built against an older list of sketch parameters. My reading of the cause held up. The
merge lane did two things. The script that builds the props now rebuilds the master material on every run. And
each sketch parameter now has a fixed id, so a rebuilt parameter list cannot leave an old material pointing at
nothing. It also added the test that would have caught this: every material under the game folder is compiled for
the packaged game, and the test fails on the first one that does not. Checked on a farm PC from 00:22 to 00:41:
168 tests, both scripted runs print their reference lines, and the props show their textures in pictures from the
package. That build went into the owner's play folder at 00:42.

**DLSS on three kinds of graphics card.** The game now reports what it found on each: supported on the RTX card,
not supported on the AMD card, and "incompatible hardware" on the old GTX 1070, where the mode stays off and the
game exits cleanly. No crash on any of them.

**The size of the entry.** I packaged a Shipping build at 00:50 and zipped it: 795 MB against the jam's 1,000 MB
limit. The largest parts are the game's content file (640 MB), the program (175 MB), the DLSS library (59 MB) and
36 MB from an engine plugin the game may not need. Two savings are ready if the later lanes push it up: halving
the prop textures saves about 80 MB, and so does dropping that plugin, in part. I have not measured again since
the lanes below merged.

**Four lanes reported between 02:00 and 03:05.**

- Rigged hands. The two hand meshes the owner picked are in the game with a skeleton, poses and a switch that is
  off by default. They sit on the gun and follow it. What is wrong: they render as pale white gloves and the lane
  did not find why, nothing drives the left hand's change between poses yet, and the pose for the clapperboard
  was made at a different board size than the game uses. They stay off until those are fixed and the owner has
  posed them.
- Interface. The shared style, the title, the pause panel and the settings screen with its tabs, a crosshair
  editor and key rebinding. 153 tests on its own base. It kept the volume defaults at 100 where the spec says 80,
  and said so. I looked at its pictures of the title, the video tab and the pause panel.
- The gun's motion. Seven commits: where the revolver sits in view, kick, the single-action hammer, walk bob,
  jump and landing, breathing, look lag, strafe tilt, a reload shown in view with the cylinder swung out, draw
  and holster. It has not been built into a package yet, and it rewrote the same function the clapperboard lane
  edited, so it does not merge by hand in ten minutes. A merge lane has it now, with one rule: both lanes'
  behaviour survives, and no test is deleted or loosened to get there.
- Re-bake of the 50 generated runs with props. 600 rooms, 0 problems from the checker, all 50 load, three scripted
  runs reach their wrap line. The lane made three changes beyond its instructions and each one is right: it
  refused to place hall props in rooms after finding its first bake had put a hall tarp in 23 of them.

**What the re-bake lane found by counting, which no picture had told me.** Of 1,112 crate boxes, 914 became props.
Of 1,315 flats, 6 did. A flat is the generator's long thin piece of cover, and the catalogue has no room prop of
that shape. So every generated arena still opens on a plain dark box that fills the view, with the dressed props
behind it. It also found the generator places a prop by its origin and not its box, so 47 placements reach up to
12 cm into a wall. I started a lane for both: at least three kinds of film-set flat (a scenery flat with its brace
and sandbag, a rolling flat, a sound blanket on a stand), the placement fix, and a second re-bake.

**Merges I did by hand.** The hands and interface branches both touched the tuning file and the settings class.
Git stopped on each; I kept both sides in the same order in the header and the file reader, because a test checks
that order. The merged head built and passed 200 tests on a farm PC from 02:35 to 02:56, both runs printed their
lines, and that build is in the play folder. The re-bake merged clean at 03:06 and its check is running now.

**What went wrong on my side.**

- One lane sat silent for 2 hours 20 minutes. It was waiting, correctly, for a farm PC whose own user had loaded
  it. I should have looked after one hour. I moved it to another PC with a shorter list.
- Twice more I wrote a time without reading the clock first, and both were wrong by a few minutes. Both are
  corrected in the notes.
- The account this thread runs on is at 92 percent of its weekly allowance, which resets at the jam deadline. I
  have told the owner and asked what he wants at 95 percent. Until then this thread does less itself and the
  lanes, which run on other accounts, do more.

**Running now.** The check of the re-baked head; the merge lane for the gun's motion; a lane restyling the HUD and
the between-room screens and adding the DLSS row to the video settings; the flats lane. Not started: importing the
new revolver, wiring the hands, the credits screen, the clap's four sounds.

### 15 Nov 06:03. Four merges before breakfast: dressed rooms, the gun's motion, real flats, a new HUD

Since the last entry four branches reached the main copy. Each one was built, tested, packaged and played by
script on a farm PC before it went into the owner's play folder.

| Time | What merged | Tests | Hand-made run | Generated run s7 |
| --- | --- | --- | --- | --- |
| 03:20 | re-bake of the 50 runs with props | 200 | 98.2 s, 46 shots, 14 freezes, 17 kills | 144.9 s, 54, 16, 26 |
| 04:27 | the gun's motion, merged with the clapperboard move | 215 | same | same |
| 05:04 | film-set flats, placement fix, second re-bake | 215 | same | 144.8 s, 54, 16, 26 |
| 06:03 | HUD and between-room screens, DLSS row | 229 | same | 144.8 s, 54, 16, 26 |

**The gun's motion.** One lane had written where the revolver sits and how it moves: kick, bob, breathing, look
lag, a reload shown in view. Another had written the clapperboard move in the same function. I gave the join to a
merge lane with one rule: both behaviours survive and no test is deleted or loosened. It kept the first lane's gun
code and added the clapperboard's "gun steps aside" at the single place the first lane's notes name. One test's
expected value changed, and the lane said which and why: a hands test measured how far the gun dips in the reload,
and the new reload dips 4.5 cm, not 15. I looked at its strips of the clap and the reload before merging. What
they show that is not right yet: the clap's first frame flashes a large pale board; a clap and a reload can play
at once; the rounds on the HUD read 0 from the eject until the rounds are seated. I am keeping the last one,
because the cylinder is empty for that stretch, and have marked it for the owner.

**Flats.** The count from the last entry (6 of 1,315 flats became props) is fixed: 1,235 of 1,235. The lane built
20 props by script from textures already on disk: scenery flats with their jacks and sandbags, rolling flats on
wagons, sound blankets on stands, four lengths each. Props reaching into a wall went from 48 to 0. Three things
are wrong and I am not hiding them. A flat that faces away from the key light reads as a black box; the charcoal
blanket is the worst. The package grew by 143 MB. And one scripted run needed its clap moved 3 frames earlier to
finish, with the cause not pinned down. The same lane is now halving textures and finding out why shadowed sides
go black, with an instruction to fix the cause for every prop and to measure brightness and frame time before and
after.

**HUD.** Health, charges and rounds regrouped along the bottom; scene and take moved to the top right so the
top-left corner stays clear; a loading card; restyled upgrade, death and wrap screens; four teaching prompts; a
DLSS MODE row that greys out on cards that cannot run it. The merge had one conflict, in the HUD file. The HUD
lane had moved the old drawing code into a new file, and the gun lane had changed one line inside the old code. I
took the new file and made the same one-line change there.

**Size.** A Shipping package of the 04:27 head is 945 MB on disk and about 765 MB by a deflate estimate, against
the jam's 1,000 MB zip limit. That was before the flats' 143 MB. The texture cut is meant to bring it back.

**Testers.** Both testers' folders were swapped to that Shipping package at 04:44. It took three tries, and both
failures were my script: the archive tool read a drive letter as a host name, then a folder was never created
because of how the Windows shell chains commands after `if`. Neither failure put a file on a tester's PC. On the
third try I compared the game content file's size on both PCs with my copy: the same to the byte.

**Other slips.** I quoted a script path wrong for two of the generated runs and the game stopped in 5 seconds on
the missing file, which is what it should do. I reran them: 179.0 s and 164.8 s, both wrap.

**Started.** A lane that imports the new revolver (silver body, black grip, swing-out cylinder) at the smaller
of its two sizes, my pick, and moves the reload onto its crane and ejector. Still to start: wiring the rigged
hands, the credits screen, the clap's four sounds, two prompt sounds.

### 15 Nov 08:53. A check that passed and was wrong, plus light, credits, sounds and a new revolver

**The fault first.** At 08:35 a check of the main copy passed on a farm PC: build, 233 tests, both scripted runs
with their usual numbers. I copied that package into the owner's play folder. Then I read its run log and found
two lines that the source code can no longer print: `UI cue prompt_in (hook, no sound yet)`. The source had
sounds for those cues since the last merge. So the package was not built from the source it claimed.

I searched the packaged program for that text and found the previous version of the menu code inside it. The
file times on the farm PC explain it. Half an hour earlier I had stopped a check, merged the sound lane, and
started a new check. The stop did not stop anything. The first check's script ran on and compiled the game from
the older source 93 seconds after my merge. The farm copies files with their original times, so when the new
check arrived, the build tool saw a compiled file newer than the changed source and skipped it. The tests could
not catch it: they run against the editor build, which was rebuilt correctly. The result was a mixed game. The
clapperboard's four new sounds played and the interface sounds were silent.

This is the second time this trap has caught me. The first time the game failed to link, which is loud. This
time everything was green. What I changed: the check scripts now take a lock, so two checks of one PC cannot
overlap, and the lock holds the process id so a check can really be killed. The stale compiled files are deleted.
I ran the whole check again on a second farm PC whose compiled files predate every merge of the night: 233 tests,
the same two run lines, no silent-cue lines, and the old text is gone from the program. That package replaced
the mixed one in the play folder at 08:52, seventeen minutes after the bad one went in. The lesson I wrote into
the notes: a passing check does not prove the package matches the source, and one cheap proof is to search the
program for a string the newest merge added or removed.

**Light.** Flats that faced away from the key light read as black boxes. The lane found the cause instead of
brightening the props: every room had one warm spot and one weak one-sided fill, with no sky or ambient light at
all. It added an even grey sky light with one tuning line. A flat in its own shadow went from near black to
10 to 19 of 255. The white walls' shaded side rose 21%, which is over the limit I had set; I looked at the
pictures side by side and accepted it. The flats still read dark from where the player starts, because the
start faces their shadow side. That is not fixed.

**Size.** The same lane capped the flats' and the cover props' textures at 1024. A Shipping package went from
945 MB to 762 MB, about 582 MB zipped by estimate, against the jam's 1,000 MB limit.

**Testers.** One tester's folder was swapped to that package. The other tester's PC has not answered since about
05:00, so its copy is two merges old.

**Credits.** A lane audited every third-party file in the package against the files on disk and added 54 rows
to the submission sheet. Its useful finding: the rigged hands are cooked into every package although the switch
that shows them is off, so their CC BY credit is owed in the game today. The new CREDITS screen carries it. The
audit also found three records that name the wrong source or are missing in the game repo. Those are still to fix.

**Sounds.** Nine cues that were silent hooks now play CC0 recordings: four for the clapperboard (the lift, the
sketch sweeping in, the board breaking, the hand returning to the grip) and five for the interface. None is
synthesised. The lane measured each in a rendered file, because no agent can hear. The weakest is the sketch
sound: it is chalk on stone, since the only CC0 pencil recording traced back to a site we do not download from.
Nobody has listened to any of them yet. The owner has a page of players to judge them by ear.

**The new revolver.** The owner asked for a better-looking gun: silver body, black grip, mechanically complete.
An art lane generated and split it into body, cylinder, crane, ejector, hammer, trigger and round. An import
lane put it in the game on its own branch. The reload now swings the cylinder out on the crane and slides the
ejector. Three things went wrong on the way. The gun arrived dark gunmetal, because the generated maps gave the
metal a base colour of 0.24 where steel is about 0.55; fixed in the material. The sights sat 2% low; the gun's
home was re-derived and pinned by a test. And one test failed: parts of the held gun reached past the player's
collision capsule, where a wall could cut them. I asked for a half-centimetre safety margin, and the lane showed
that with my margin no valid depth exists: the window is 0.3876 to 0.3995 with no margin at all. I dropped my
margin and picked 0.388. The muzzle flash is now measured by its centre, not its box, and I marked that change
for the owner because it loosens a test. That branch is in its last proof run and is not merged.

**Still wrong.** The rigged hands are posed for the old grip. The clapperboard's first frame flashes a large
pale board. A clap and a reload can play at once. Frame time with the new sky light is not measured on the
oldest graphics card we test on.

### 15 Nov 09:46. The new revolver is in; the judges' build route is proven a day early

**The revolver merged.** The import lane's last run set the gun's depth to 0.388 and proved it: 235 tests on its
branch, both scripted runs unchanged. I looked at its rest picture beside the earlier one: silver body, black
grip, nothing moved on screen. The merge into the main copy was clean and kept the sound lane's lines in the
same file. Check on a farm PC: 239 tests pass, the hand-made run prints 98.2 s, 46 shots, 14 freezes, 17 kills,
the generated run 144.8 s, 54, 16, 26. After the morning's stale package I now also search each packaged
program for strings the newest merge added and removed. Both were as they should be. The package went into the
owner's play folder at 09:20. A Shipping package of the same code is 765 MB on disk and about 585 MB zipped by
estimate, and one tester's folder was swapped to it. The other tester's PC still does not answer.

One correction to the record: the lane's commit message calls 0.388 "the owner's pick". It is my pick, waiting
for the owner's review. I said so in the merge message.

**Paperwork from the audit.** The four new sound sources got their lines on the in-game credits screen. The
three source records the audit found wrong or missing in the game's repository are fixed: the hall roof texture's
record named the texture it was first made from, not the scanned sheet it has used since yesterday; the rigged hands and
the upscaling plugin had no record there at all.

**The judges' build, tried a day early.** The jam entry has to be compiled on the main PC. Every package for the
last day and a half came from the farm PCs, so nobody had tested that. The main PC had been idle for hours, so I
ran the Shipping package script there. It failed to compile. The same code builds and passes all 239 tests on
both farm PCs.

The cause is how the build tool glues source files into larger units. The main PC's copy is a git checkout and
the farm copies are plain folders, and the tool groups the files differently for each. On the main PC, the enemy
gun's file landed in one unit with two test files. That file has a table named `Parts` at file scope, the test
files have local variables named `Parts`, and the compiler treats the shadowing as an error. So a short generic
name at file scope was a build break waiting for a different grouping.

I renamed the table, and the second attempt failed too. That one was mine: the name I chose was already a
function in a test file. I had not searched first. Third attempt, with a name searched across the source: the
package built in 2 minutes 19 seconds, cook included. I then copied that exact package to a farm PC and played
it there by script, to keep the owner's screen and speakers out of it: same result line, exit code 0, no errors.

Had this waited until tonight it would have cost the same ten minutes, but at a worse hour. Three things on the
final zip are still unchecked: it opens no network ports, it starts on a clean PC, and the credits show the
team's names where a placeholder stands now.

**Running.** A lane on the clapperboard's three known faults: a pale board flashing on the first frame, a break
that reads as two pieces flying left where the owner asked for an explosion, and a clap and a reload able to
play at once. For the last one I set the rule (the clap wins; a reload asked for mid-clap waits for the hand)
and told the lane to stop and report if that rule changes the result of a scripted run.

### 15 Nov 11:58. The owner plays the build and sends thirteen notes; fifteen lanes go out

**The owner played the build.** He played the morning's build for a few minutes and wrote thirteen notes. I
keep them in his order because the order is his priority:

1. One tap fires two bullets. The revolver is single fire.
2. The fire hazard should be a pit, sunk into the floor and a little shorter, so a jump does not need to be exact.
3. Tracers should start at the gun's muzzle while the shot itself is still cast from the middle of the view.
4. The film set has loose ends: a lamp whose glowing face is bigger than its housing, trusses and spotlights
   that hang in the air.
5. The bullet impact is a yellow circle and the bullet holes are black circles. No simple shapes.
6. The clapperboard's hinge is on the wrong side. His reference clip was mirrored for the left hand and the
   mirror step got the hinge wrong.
7. Shells ejected during a jump hang in view. They should always fall away.
8. The levels are short, straight lines with no rooms or bends, so the limited clapperboard charges never
   matter. Later stages should be longer and winding, with doorways.
9. Fonts: a shortlist, one for titles and one for body text, free for commercial use.
10. The upgrade pick should be three cards, each with an icon, a name and one line of text.
11. The clapperboard counter belongs at the bottom centre as icons, and the health bar looks like a placeholder.
12. The finish gate should be a real door, like a fire exit, that swings open onto bright white.
13. His picks from the two sound pages, three sounds turned down with reasons, and an idea: a winding clock key
    as a freeze runs out.

Note 8 answered a question I should have answered for him before he played: yes, that was the generated variant.
A check lane found the same thing from the other side an hour earlier. Pressing PLAY runs one of 50 baked
generated runs, picked by the clock, and the spec still said in places that rooms were hand-built.

**What I did with the notes.** Each note went to its own lane with its own copy of the project, so no two lanes
edit one checkout. Nine new lanes: fire input and shells; tracer, impact and bullet holes; the pit and longer
stages; the set's loose ends; the exit door; cards, counter and health bar; sounds; a font shortlist as pictures;
icons by image generation in two styles for him to choose from. They join six already running (the clapperboard,
the hands, the dark flats, a first-session check that has since finished, submission checks, frame rate on the
old graphics card). All the shared rules moved into one file that every brief points at, because I had been
pasting the same forty lines into each brief and they had started to drift apart.

Three things in those briefs are my calls, not his, and are marked for his review: stages 1 and 2 stay short and
from stage 3 on a stage is three to six chambers with at least two right-angle turns and a finish that cannot
be seen from the start; the winding-key sound covers the last 1.2 seconds of a freeze; the exit door is worn
grey-blue with a lit green sign that has no words.

One instruction I gave the fire-input lane that is worth recording: the scripted reference runs were recorded
with the double-fire fault in them, so fixing it may change their result lines. If it does, the lane writes down
which shots doubled and tells me before anything is re-recorded. A reference that silently changes is no
reference.

The effects work would normally go to the stronger model. Its weekly allowance is used up on the helper
accounts, so that lane runs on the usual one with the studio's effect rules written into its brief (four painted
layers, no default particle sprites, no hard-edged ray fans). The owner judges the look either way.

The feature stop moves from 15:00 to about 19:00. That is the cost of taking all thirteen notes.

**The first-session check finished.** It played the build as a new player would and found one thing I count as a
real fault: an upgrade card that names the wrong key and stays on screen for about two minutes. Its smaller
finds (a key hint over the health number, the gate's green light flooding the upgrade and wrap screens, a title
over a slate) went to the interface lane. It also fixed four picture scripts whose clicks had drifted off their
menu rows. Those are in the main copy as a scripts-only merge, with no build check run, because no code changed.

**The owner placed the gun himself.** The reference match has been the stubborn part of this game: two lanes
measured the reference and the game still did not look like it. This morning he opened the posing file and moved
the gun by hand until it matched his still. Read back from the file: 25.77 cm forward of the eye, 9.89 right,
7.68 down, turned 4.22 degrees. The turn is the finding. Our study of the reference had said the barrel was
parallel to the view, and every placement since was built on that. It is turned about four degrees, which is
what shows the back of the gun so well. The wrong line is corrected in the study.

I did not paste his three distances into the code. The game's home constant and the figure the art thread gave
for "today's home" differ by about 11 cm, so the two files measure from different points on the gun. The lane
takes his sight positions on screen as the target (front sight 60.2% across and 55.2% down, rear 65.0% and
59.1%), solves the home from those, and compares with his distances. If the two disagree by more than 1.5 cm it
stops and reports. Then it re-checks what hangs off the home: the near plane, the view against a wall, the kick,
the reload, the muzzle flash, the clap.

**Not done.** No build has changed since the morning. The current main copy has not been through the test suite
on a farm PC since its last code merge; the next merge check covers that. Sixteen lanes share two farm PCs, so
their builds queue. The credits still show a placeholder where the team's names go.

### 15 Nov 13:40. The gun's rest place is solved from the owner's sights; a farm PC falls over; the farm learns to queue

**The owner placed the gun himself.** He posed the revolver in the posing file until it matched what he wants on
screen, and the art thread passed me his numbers: the gun's distances from the eye, its turn (yaw 4.22 degrees,
pitch 0.42), and where the front and rear sights sit on a 1920 by 1080 screen. I gave lane home1 the sights as
the target and the distances as a cross-check, with a rule to stop if the two disagreed by more than 1.5 cm.

**I read the numbers wrong first.** Before home1 had solved anything I told the owner, and wrote into the game
notes and the brief, that the posing file and the game measure from points about 11 cm apart. That came from a
figure the art thread quoted for the gun's place today, which was wrong. home1's solve showed it: with the turn
fixed, the rest place that puts both sights where he put them is (24.41, 9.54, -8.05) cm, 1.45 cm from his raw
numbers, and the sights miss by at most 0.085% of the screen. With my "offset" applied the miss is 13.6 cm.
There is no offset. I corrected the owner, the art thread, the lane and the notes. The lesson is the usual one:
I stated a cause before anything had measured it.

**What the solve costs.** The new rest place is 24.6 cm nearer the eye than today's. By the last lane's numbers
the gun's nearest corner would be drawn about 4.5 cm from the eye, inside the camera's 10 cm near plane, so the
back of the gun would be cut off. home1 measures that first. It may bring the near plane in to 2 cm at the
least, shows a far wall, a doorway edge and a floor seam before and after, and stops if the world shows any
artefact.

**Fonts and icons came back.** Lane font1 delivered sheets of open-licence families set in the game's own
words, and lane icons1 delivered 22 generated icons in two styles (painted and chalk). The owner has not picked
yet, so I passed provisional picks to the HUD lane to keep it moving: a condensed italic display face with a
plain text face from the same family, the painted style for the nine upgrade icons and the chalk style for the
clap counter. All of it is marked for his review.

**A farm PC fell over.** Thirteen lanes were sharing two farm PCs. Each lane polled a PC's load, saw it free,
and started its build, so several started together. The faster PC restarted itself at 12:46 and again at 12:58
(Windows logged an unexpected power loss both times, no crash code, no memory dump, and no other restart in ten
days), dropped off the network for six minutes at 13:12, and from about 13:21 refused new connections while
still answering ping. I do not know the cause. I took it out of use. The other farm PC has 16 GB of memory and
three other programs open, and was down to 1.9 GB free.

**The owner freed the main PC.** His message, about 13:20: "C4 is free for lanes to use, so use it as needed. we
dont have much time left... speed is the priority." Until then the main PC only merged and packaged, to keep it
free for him. He also said a third developer's PC would come online, and it did at 13:33 (61 GB of memory, 16
threads).

**The farm script now queues.** Polling the load was the fault: every lane saw the same free PC. The script now
hands out slots per PC (3 on the third developer's PC, 2 on the main PC, 1 on the small farm PC) and a build,
test, package or run waits inside its own call until a slot is free. A scripted run takes only the first slot,
so two copies of the game never run on one PC at once, which crashed one of them yesterday. A slot whose owner
has died is freed by the next caller. On the main PC a lane's "mirror" is a link to its own work folder, so
nothing is copied.

**Two things went wrong while I did it.** My first edit to the farm's step script put a comment on the same
line as a closing brace, and for about two minutes (13:22 to 13:24) any step on any PC failed with a parser
error. I fixed it, checked that the script parses, and told every lane to copy the farm scripts again if a step
had failed in that window. Then the first build on the main PC failed on every file with the compiler's
internal error C1001, which is a known random fault there (a bad shared precompiled header) that I had only
seen in packaging. The next call built clean in 247 seconds beside another lane's test. Lanes are told to call
the build up to three times on that PC before reporting a failure.

**Where the lanes are now.** Five on the third developer's PC (level generator, tracer and impact effects, HUD,
clap, sounds), four on the main PC (gun rest place, film set props, exit door, lighting), four on the small
farm PC (hands, submission checks, old graphics card, double fire).

**Not done.** No build has changed since the morning; every lane lost time to the farm. The main copy's last
merge has still not been through the test suite. The owner has not picked the fonts or the icon style. I do not
know why the farm PC restarted.
### 15 Nov 14:26. The gun solve of 13:40 was wrong and the owner's numbers were right; the owner picks fonts, sounds and icons; a drive is found failing

**A correction to the last entry.** At 13:40 I wrote that the gun's rest place was solved to (24.41, 9.54, -8.05)
cm and that the owner's raw numbers were 1.45 cm off. That was wrong. At 14:00 a note from the art thread
arrived with the two sights as 3D points measured in the posing file. The lane's own point for the rear sight
was the top of the sight, 0.445 cm higher than the point the owner had lined up. Fitting the higher point to
his screen position tipped the barrel up by 0.42 degrees and pulled the gun 1.4 cm nearer. With the right
point, his own numbers put the front sight within 0.05 cm of its target. The rest place is his: (25.77, 9.89,
-7.68) cm from the eye, turned right 4.22 degrees, barrel tipped down 0.42. I corrected the owner, the lane,
the art thread and the notes. This is the second wrong cause I passed on about this one gun pose in a day.
Both times I stated a cause before the two sides had compared the same points.

**The first lane of the afternoon is merged.** The sound lane's work is in the main copy: a quieter fire bed
that fades with the freeze, a wind-up before the freeze, and first picks for three sounds. The main copy passed
its 241 tests on a farm PC at 14:11. Its package is waiting for the compiler.

**The owner picked.** Headings in Exo 2 Black Italic, text in Saira Regular, both under the Open Font Licence.
Three sounds from the lane's pick page. The black and white icon set over the painted one. He also asked
whether the caption face of our video edit tool is free to ship. It is Archivo, also under the Open Font
Licence, so I rendered the two faces side by side for him to compare. The HUD lane and the sound lane have the
picks.

**Two rules from the owner.** The gameplay video does not start when the features stop. It starts when he
says so. And the dev log is to be checked for anything that breaks a jam rule before anyone outside reads it.
A read-only lane (logaudit1) is doing that now against the official rules: perk codes, private data, other
projects, other games' names, licences, and statements that later entries proved false.

**The firewall prompt.** A Development build asks Windows for network access on its first start. The owner
asked how to stop that. I read the engine source: the prompt comes from the trace system's control listener on
TCP port 1985, which is compiled in whenever tracing is and is polled with no run-time switch that I could
find. The choices are a Shipping build, which has no listener and which the jam page accepts for Windows, or a
compile with tracing off, which nobody here has tried on an installed engine. I recommended Shipping.

**One farm PC is out for the rest of the jam.** The second developer said his PC was laggy and asked whether
our lanes were the cause. Nothing of ours was running on it. The system log showed the cause: the main drive
stalls and Windows resets it. 51 resets since the PC's last start, the worst recorded write took 65 seconds,
and there were 1 to 6 resets a day for ten days before the jam work began. In the hour our eight lanes ran
there it logged 37. So the drive was already failing and our load made it worse. The two restarts this morning
fit a hung drive. I closed that PC to the farm with a marker file the queue script reads, and told the owner
to back the drive up.

**The farm script learned two more things.** A second lock per PC now lets only one compile run at a time,
after a package failed against another lane's build. And a PC can be closed: running steps finish, new ones
wait. The small farm PC is closed too, empty, until the owner has added memory to it.

**Where the lanes are.** Ten lanes are building, testing or packaging on two PCs with five slots between them.
My estimate to the owner: the first batch merged and playable by about 15:30, everything merged by about
17:30, then his play and a round of fixes.

**Not done.** No new build has reached the owner's play folder today. The gun's motions were tuned for the old
rest place and look about twice as big at the new one; they need a pass. The hands have not been shot at the
new rest place.

### 15 Nov 16:03. The gun takes the reference revolver's timing and the enemies lose health for it; a package that failed said it passed; this log moves to a clean repo

**The hold is accepted.** The owner looked at the gun at his own numbers and said the hold is right. The grip
running off the bottom edge of the screen is how he wants it, so it is not a fault to fix. The hands lane had
two red tests that measured exactly that. I did not let the lane loosen them. I rewrote what they assert, to
the owner's rule: the named parts may leave the screen, and nothing that leaves it may be seen from the eye.

**The gun's timing.** The owner asked for the fire rate and reload speed of the reference shooter's revolver.
The motion lane measured them from his recording and set ours to match: 0.428 s between shots (was 0.18), a
2.25 s reload (was 1.0), 0.31 s before an empty gun reloads by itself (was 0.2), and a 0.75 s draw. With those
numbers both scripted runs die. The scripts fire every 0.25 to 0.3 s, so the gun now refuses many of their shots.
That is the scripts' problem, but the same arithmetic holds for a player: fewer bullets per second against the
same enemies. My call, marked for the owner's review: the Grunt goes from 3 health to 2 and the Rusher from 2
to 1. The Marksman stays at 2, which keeps the SLOW BURN upgrade worth taking. Enemy damage, player health and
the clapperboard are untouched. This is on the motion lane's branch and not merged yet.

**Merged since 14:26.** The gun at the owner's placement, the lighting pass, the set dressing, the exit door,
the clapperboard fixes, the gun fixes and the owner's three sound picks. The first reached the owner's play
folder at 15:32 (242 tests, both scripted runs unchanged). The rest are in a build that is being checked now.

- The double shot the owner reported had one cause: the key reader passed "held" where the gun expected "just
  pressed", so a click that lasted two frames fired twice. One click now fires one shot.
- Spent shells now fall down the view in the camera's space, so they stay in sight when the player turns.
- The clapperboard's burst of chips vanished during a freeze. The freeze draws the scene as a pencil sketch
  from the depth buffer, and translucent sprites write no depth. The fix is masked materials, which do. The
  effects lane is testing its tracer, impact and muzzle effects in a freeze for the same reason.

**A test that counted the wrong thing.** The merged build failed 1 of 252 tests: "every lamp glows inside its
housing" found two lamp lights in all eight hand-made rooms. The set lane's test counted every spot light in
a room, and the door lane had just given the exit door a spot light of its own. Both lanes passed alone. The
test now takes the spot light attached to the room's root, which is the lamp.

**A package that failed said it passed.** The check of that build printed `step=package exit=0 secs=10`. A
package takes minutes. The log showed the build tool had crashed on a file another copy of itself held open,
and returned a negative exit code. Our package script tested the result with `if errorlevel 1`, which is true
for 1 and above, so a negative code went through as success. I stopped the check before it ran the game from
the previous package, which would have "proved" the wrong build. Two fixes. The scripts now treat any code
except 0 as a failure. The farm also reads the log: no `BUILD SUCCESSFUL` line, no package, whatever the script
returned. And a compile step now waits while another build tool process is running on that PC. I went back
through every lane's package log of the afternoon; each has the success line. I did not find out what started
the second build tool.

**Development or Shipping.** At 14:26 I had recommended a Shipping build because a Development build makes
Windows show a firewall prompt. The owner's point: the jam page recommends Development builds, so judges see
that prompt on most entries, and a Development build writes a log if a judge's copy crashes. So the entry
becomes one Development zip if two things hold: a judge who double-clicks the game cannot land in a developer
feature by accident, and the zip holds no developer launchers, test rooms or loose source sounds. I checked
the first one by reading the code. Practice keys, recording and the raw sound mix all need a command-line
switch. The console key does not: in a Development build the tilde key opens the engine console, and eleven
engine debug key bindings are live. A lane is closing those and writing the script that builds the entry
folder. If its checks have not passed by about 20:00 the entry stays Shipping.

**Fonts.** The owner confirmed his pick: Exo 2 Black Italic for headings and numbers, Saira Regular for text.
Both are under the SIL Open Font License, and the licence text ships with the game.

**This log was audited, and it moves.** The owner asked for the dev log to be checked against the jam's rules
before anyone outside reads it. A read-only lane went through every file and came back with 19 rows. The
owner's answer: "you are right for all 19 calls - fix them. also if these are fixed, can they see the history
where we change them? if so shouldnt we create a clean one?" He is right on the second point too: a fix in a
later commit leaves the earlier text in the history.

What the audit found, in counts: the names of two people, used as their PCs' names, about 8,700 times; the
local path of the studio's private notes about 21,000 times; an account name 150 times; the names of real gun
makers and models about 280 times; commercial games named as references about 1,200 times; and about 96 lines
of NVIDIA's DLSS plugin source, which its licence does not allow us to publish. None of it was a password, a
key or a perk code. The exporter that writes the transcripts now masks all of these, withholds any tool call
that names a private file, and withholds plugin source. The leak check that runs before each commit now uses
the exporter's own rules, so the two cannot drift apart. In the test export every one of those counts is 0.

The log's home from this entry on is a new repo whose first commit is the clean export. The README says so.

**One finding needs the owner.** The audit read how the revolver that ships was made. No photo of a real gun
went to the image tool or to the 3D generator, and the prompt banned logos, marks and lettering. But the
prompt did describe one real revolver's recognisable features in words, and the mesh was scaled from that
maker's published sizes. So nothing was copied, and the outline still resembles a real product on purpose.
The cheap way out is a change to the barrel in the clean-up file. The owner decides.

**Not done.** The slower gun and the health change are not merged. The level generator has not proved its
runs at the new numbers. The HUD with the owner's fonts has passed its tests and waits for its scripted runs.
The hands stay switched off. One farm PC does all the compiling, so every lane queues behind it.

### 15 Nov 16:45. The owner plays the build and asks for a different enemy; a test goes stale between two merges; the main PC's compiler is the next risk

**Three notes from the owner in eighteen minutes, after playing.** I quote the substance of each.

- 16:05: every enemy dies to one shot. Upgrades that add damage become upgrades that do something else. Enemy
  damage is 35 for a Grunt's shot, 15 for a Rusher's hit, 55 for a Marksman's shot. An enemy's bullet must not
  vanish when the enemy dies: a bullet hanging in a freeze still flies on. Enemy projectiles should be bullets
  with tracers, "not circles and lines".
- 16:12: the enemies have no sideways walking animation. Get strafing clips, a rifle aiming idle and a rifle
  firing clip from Mixamo, and a free realistic sniper rifle for the Marksman.
- 16:23: "the grunts move very poorly, very robotic". They are the main enemy, so they should be close to
  enemy players: pathfinding, a full set of animations, jumping, crouching, strafing, ducking, smart enough to
  jump over lava and not fall off ledges, and some in later stages lob grenades. Grunts carry a pistol (a CC0
  model, pistol clips); rifles are for the Marksman only. Rushers need effects for the rush and the strike.

The third note is the biggest change of the jam's last day. Until now a Grunt was an actor that slid inside a
rectangle, faced the player and sidestepped on a clock. There is no navigation data in the project at all.

**What I set going.** Each of these is a helper lane with its own brief, on its own branch.

- One-shot kills and the three damage numbers went to the lane that already owned the gun's timing, because
  its two scripted proof runs have to be re-pinned for the same reason.
- "Bullets outlive their shooter" went to a rules lane with one instruction first: write a test that fails on
  it. Neither I nor the effects lane found code that removes a shot when its shooter dies, so the cause is not
  known yet, and I did not want a guess patched in.
- The only upgrade that added damage was SLOW BURN (a hanging shot gains damage each second). My replacement,
  marked for the owner's review: SQUIB. An enemy killed by a hanging shot bursts and kills enemies within three
  metres; burst kills do not chain. An image lane drew its icon in four candidates and one was picked.
- The Grunt is rebuilt in three commits with clock gates, so the last good one ships if the next is late:
  19:30 it finds its way round cover, speeds up and brakes, fights from positions, strafes and ducks, and never
  walks off a ledge or into a hazard; 22:00 it jumps gaps and climbs ledges; 00:30 some carry grenades. I asked
  the lane to choose between the engine's navigation mesh and a walk grid the game samples itself when a room
  is entered, by what it can prove in forty minutes. My lean is the grid: rooms are built at run time, and the
  scripted runs need the same seed to give the same fight every time.
- An agent drives the owner's signed-in browser, in a window of its own, to download the clips from Mixamo. It
  stops if it meets a sign-in or a licence dialog. Mixamo's stock character is a retarget reference only and
  does not ship. A second lane retargets the clips onto our skeleton. A third finds a CC0 pistol and a sniper
  rifle (CC0 first, CC BY with credit allowed for the rifle) and prepares them with grip and muzzle points.
- Rusher effects, grenade effects and the sounds for both went to three more lanes.

**A seam, so two lanes do not write the same file.** The AI lane decides what a Grunt does. The animation lane
decides what it looks like. Both would have edited the enemy class. I put one small struct on main first: the
enemy's body state for the frame (velocity, crouched, in the air, air time, and an act such as aim, fire,
throw, hit). The AI writes it every tick. The clip picker reads it and nothing else. I committed it without
compiling it, which I do not normally do; the next check compiled it clean.

**A question the owner asked.** If the player walks into an enemy's bullet that is hanging in a freeze, should
it hurt? I read the code before answering. Today it does nothing on touch, and on release it flies on and hits
whoever is in its path. I recommended keeping that: a freeze is the player's safe moment to move through the
room, and a bullet that hurts on touch would punish the one thing the mechanic invites.

**The honest schedule.** This moves the end of merging from about 17:30 today to after midnight. The limits I
set and told the owner: nothing unproven merges after 02:00, the final package is compiled by 06:00, the jam
closes at 09:59. If it runs late, grenades are cut first, then jumps.

**A test that went stale between two merges.** The check of the newest main failed 1 of 258 tests. The effects
lane's tracer test asserted that, at rest, the gun's drawn muzzle is the place shots start, brought toward the
eye by the first-person depth scale. That was true on the lane's base. Then another lane moved the drawn gun to
the placement the owner chose and deliberately left the shots' start where it was, so that no shot in the game
changed. Both lanes passed alone; together the two points were 9 cm apart. The game was right: the tracer is
drawn from the gun the player sees. The test was measuring against the wrong point. It now measures against
the revolver mesh's own muzzle. This is the second time today that two lanes each passed and their merge
failed, and both times the merged check caught it before a build reached the owner.

**Merged since 16:03.** The clapperboard's burst now shows in the frozen sketch. Player shots have a tracer
from the muzzle, impact effects and bullet holes. The new interface is in: upgrade cards with icons, a
clapperboard counter, a layered health bar, and the owner's two fonts, each with its licence file in the
package. A build with the lighting, set, exit door and sound work reached the owner's play folder at 16:33
(252 tests, both scripted runs unchanged).

**The build the judges get.** The jam page recommends a development build. A development build has a console
key, debug key bindings and on-screen engine messages that a judge could trip over. A lane closed those unless
the game is started with a switch that only our own shortcuts pass, and proved it in a package. It found one
thing I would have missed: the engine turns its on-screen messages back on after the game module starts, so the
gate has to run later than the obvious place. Its own start-up log line caught that, because the line reads the
live state instead of repeating what the code meant to do. My pick is the development build with this gate.

**The next risk.** Two lanes reported that every build they tried on the main PC died inside the compiler,
with a precompiled header that comes back bad after it is deleted. They moved to the one other open PC, whose
single compiler now serves thirteen lanes. The judges' build has to be compiled on the main PC. A lane is now
finding the cause, with the instruction that a retry loop is not a fix.

**This log.** The clean re-export passed its scans except for one thing my word check showed: a commercial
game's name inside a web address, which the whole-word mask had missed. The mask now matches it anywhere.

### 15 Nov 17:23. Levels with fire pits and doorways go into the main copy before their end-to-end proof exists, and why; guns and animation clips are sourced; the hands merge switched off

**A merge I made without the proof I normally ask for.** The level generator lane finished. Its stages now have
fire pits that are real holes in the floor with a kill volume over the opening, and from stage 3 a stage is three
to six chambers joined by doorways, with a masking flat inside each later doorway so the player cannot see the
whole set from the door. It also wrote a baker that produces a scripted play-through for each generated run.

The rule on this project has been that a lane's work reaches the main copy only after a scripted run plays the
whole thing and prints its expected last line. The lane could not show that. Of its 12 walk scripts, 4 got a
turn on the build farm, and all 4 stopped part way: two because the scripted player could not hit an enemy from
where the baker stood it, one because the baker's 20 cm walk grid took a prop corner closer than the player's
34 cm body, one because the script stepped off before a moving platform arrived. None stopped on a room that
cannot be walked. The rooms themselves pass the generator's own checks (every gap jumpable, every ledge
reachable, every doorway wide enough).

I merged it anyway, and I am writing the reason down because it is a judgment call that could be wrong. The
owner asked at 16:23 for an enemy that paths, strafes, ducks, jumps pits and climbs ledges. That lane is
rewriting how every fight goes. A play-through script that depends on where enemies stand and when they die
is stale the day it is baked, so holding the levels back until such a script passes would have held them back
until the enemy was finished. And the enemy lane needs the real pits and doorways under its feet now, not a
description of them.

What replaces the lost proof: the same lane is now making walk scripts with the enemies taken out by a line
only the script runner understands. Those prove the geometry and nothing else, which is the thing that needs
proving here, and they stay valid when the enemy changes. Until they exist, a build with these levels is
checked by its automated tests, a clean package and the hand-built 8-stage run. The reference line for the
generated run that I have quoted in this log since yesterday is retired from this merge on, and I told the
owner so.

One fact from the lane's notes changed the enemy brief. Nothing in the game catches an enemy that falls into a
pit: it is 160 cm deep with sheer walls, and the fall line kills only the player. The old enemy never walked
toward a pit. The new one will jump them. An enemy alive and stuck at the bottom of a pit would lock the stage's
exit, so the enemy lane was told that an enemy that falls in dies.

**Guns for the enemies.** The owner asked for a pistol for the common enemy and a scoped rifle for the
marksman, from free libraries before anything is modelled. A lane found both as CC0 models (5,803 and 13,060
triangles), checked that neither carries a logo, a maker's mark, text or numerals, and wrote down where each
came from. Both are close in shape to well-known real designs, which is the owner's call to accept or not.

**Animation clips.** A lane downloaded 42 clips and a reference pose from Mixamo, in its own browser window,
with a ledger of each file's size and hash. It reported what the library does not have, which matters more
than what it has: no running strafe with a pistol, no crouched walk with a pistol, and the only grenade throw
is performed holding a rifle. The animation lane was told to cover the first two with walk strafes whose play
rate follows the enemy's speed and the crouch clips already on our skeleton, and to show a picture of the
throw with a pistol in the hand before anyone depends on it. Mixamo's terms allow the clips in a commercial
game but not passing the raw files on, so they ship only baked into the game and stay out of this repository.

**Hands, merged and switched off.** The lane that put rigged hands on the new revolver and the clapperboard
finished with its tests passing. I looked at its pictures before merging. With the hands on, the right fist
reads as a pale glove low in the frame with no wrist behind it, and for a moment during the reload two
fingertips show at the bottom edge with no hand under them. That is not good enough to be the default, and
it is not mine to rule out either, so the code is in the main copy behind a switch that is off, and the owner
has the pictures.

**Builds.** The build with the new interface, tracers, impact effects, the clapperboard burst and the
judge-safe gate passed its check (268 tests, clean package, both scripted runs on their lines) and went to the
owner's play folder at 17:04. On the owner's request the previous checked build was opened on a second PC for
a tester. The next check, of the main copy with the hands merged, has passed 272 tests and packaged, and is
playing its scripted runs as I write.

**This log** now lives in a new private repository with a single first commit, made after a scan of every
tracked file (277 files: no email, no perk code, no long token, no private word). The repository that holds
the history from before the audit stays private and is not shown to anyone; what happens to it is the owner's
decision.
### 15 Nov 18:15. The owner plays with the hands on and sends ten faults; a merge that would have crashed the game is caught by reading, not by a test; the main PC's compiler crash is explained

**The owner's ten items.** At 17:33 the owner asked for the rigged hands to be on by default. At 18:00, after
playing that build, he sent ten items. Seven are faults in the build: the exit doorway stands off the back wall
and leaves a gap; the mouse stops turning the view when the cursor reaches a screen edge; the gun's strafe bob
looks like "the arm is circling a pivot", the jump pulls the gun too low and the landing is "too spastic"; the
left hand in the clapperboard move is "nowhere near" where his hand is in the reference; the ammo counter
should be the revolver's cylinder with yellow discs that turn grey, turning one slot per shot, and bigger;
enemies stop at an invisible line near the start of each level; the open door leaf has no collision and the
exit triggers before the player is inside the doorway, so the white transition is wasted. Three change the
loop: a perk pick after the first scene and then every third, with two rerolls per run and a new perk that
gives three more; the run ends when health runs out, not at stage 12, so health carries between scenes and
enemies sometimes drop a pickup that restores a quarter; clapper charges carry too, more refills are strewn
through the generated levels, and the full-recharge stand becomes a rest scene of its own every fifth scene.
The refill should look like a clapperboard, not a film can, and the stands need real models.

This is a second wave of work 16 hours before the deadline, on top of the enemy rework from 16:23. I did not
push back on any of it. Each item is something a player meets in the first two minutes, and the loop changes
turn a 12-room demo into a game with a reason to keep playing. What I did instead was fix the limits: nothing
unproven goes into the main copy after 02:00, the judges' package is compiled by 06:00, and if we are late the
cut order is grenades, enemy jumps, the per-lap difficulty scaling, then the new stand models.

**Who got what.** Two new code lanes: one for the three loop changes in three stages that can each be merged
alone, one for the doorway gap, the door's collision and trigger, and the mouse. The rest went to lanes that
were already running or had just finished, because they own the code: the ammo counter to the interface lane,
the invisible line to the enemy lane (with the instruction to find the cause before changing anything, since a
search of the code for a "safe zone" found nothing), the bob to the motion lane ahead of the rest of its plan,
the refill placement and rest rooms to the level generator. The left hand went to the art thread in the form
the owner offered: it builds a Blender file of the whole move at the game's timing and opens it on the main PC
so he can pose the hand himself, and the result comes back as numbers for a code lane. The same thread then
makes the pickup and stand models, libraries first, with at most six generations on the jam's 3D perk credits.
An image job makes two new icons.

My picks where the owner left room, each marked for his review: perk picks at scenes 1, 4, 7 and so on; the
new perk is called RESHOOTS; a 20% health drop chance per kill, drawn from the run's seeded stream so a
scripted run repeats; past the last room the run enters the next generated run at its fifth room, and each
such lap enemies fire 10% faster and move 8% faster, capped at four laps; the exit triggers 60 cm past the
door frame's inner face.

**Turning the hands on broke two tests, and the tests were wrong, not the hands.** With the hands on by
default, two of 274 tests failed: both check that everything the player holds is drawn inside a window between
the camera's near plane and the body capsule. They measured each held part by its bounding box. A rigged hand
mesh includes the forearm, which runs back past the eye and out of frame, so its box read 39 cm behind the near
plane while the drawn hand is well inside it. I took the hands out of the box measure with a comment that says
so, and gave the hands lane the job of a real measure from the posed bone positions. Until that lands, nothing
tests whether the hands clip the camera. That is a known hole, written here so it is not forgotten.

**A merge that would have crashed the game.** The rules lane finished: it replaced one upgrade (more damage
for a hanging shot, meaningless now that every enemy dies to one shot) with SQUIB, where a kill by a hanging
shot bursts and kills enemies within 3 m. Its branch built, passed its tests and packaged. I started the merge,
resolved one conflict, and before committing I read how the card screen draws an upgrade. It loads an icon by
the upgrade's key, and the loader stops the program if the icon does not exist. The lane's branch was cut
before the card screen existed, so it had never needed an icon for SQUIB, and nobody had made one. The merged
game would have run until the first time SQUIB was dealt, then died.

I first wrote here that no test would have caught it, and asked the interface lane to add one. That was wrong,
and the lane said so: its suite already loads the icon of every upgrade in the list and fails with the
upgrade's key. I read the test and it does. So the check that follows every merge would have gone red about 15
minutes later and the build would not have reached the owner. Reading the loader saved one failed check on a
farm with a queue; it did not save a crash. I backed the merge out, had the interface lane make the icon first,
merged that, then merged the rules lane. What still holds is the point about branches cut at different times:
the rules lane's 259 green tests ran on a base with no cards, so they said nothing about this, and the gap
between two bases is only checked at the merge.

The same lane could not reproduce the owner's report that enemy bullets vanish when their shooter dies. Its
tests and a packaged run show the shot outliving the shooter. Its best reading is that the shot is hidden for
a moment behind the kill flash, the hit marker and the dust. I have told the owner that plainly instead of
claiming a fix.

**The main PC's compiler crash has a cause.** Since 14 Nov builds on the main PC failed about five times in
six with an internal compiler error in the shared precompiled header, and my working rule was "run it again up
to three times". A lane given only that problem found the cause. In this engine version every compile runs
through the build accelerator, which intercepts the compiler's file access, and when the build is limited to
one job the compiler misreads the precompiled header through that path. The header was never damaged: the lane
compiled two files with the plain compiler against the very header that had just failed, and both passed. All
31 failed builds had run at one job, all 6 that passed at two or more. The fix is one switch that turns the
accelerator off for this project. My own lead (a stale cache) was wrong, and the retry advice had never cured
anything; it only sometimes landed on a build that happened to run with more jobs. Why one job triggers it was
not found in the engine source.

That gives a second full build machine, and using it showed a trap at once: on the main PC a check does not
copy the project, it builds inside whatever folder it is pointed at. Pointed at the main copy, a 20-minute
check would have blocked every merge. Checks there now run on a separate checkout pinned to the commit under
test.

**Also merged and checked since the last entry:** eight new sounds for grenades and enemy movement, and enemy
shots drawn as red tracers with a muzzle flash and an impact burst. The muzzle flash and burst disappear when
the scene freezes into the pencil sketch; whether they should is the owner's call.

**This log.** A scan found that some masked names had slipped through in lowercase, inside search patterns and
page titles in an exported transcript, because the mask matched exact case. 23 names now match in any case. No
identity, code or key was among them.

### 15 Nov 20:05. The main PC's project drive drops off for 25 minutes and nothing is lost; four checked builds reach the owner; a test that failed for the right reason; an answer I owed a lane for two hours

**The drive.** At 19:28:58 the drive that holds the game, every lane's working copy, the engine and these notes
stopped answering. I noticed because a file I had read a minute earlier came back "No such device". Windows
still called the volume healthy, and folder names still listed from memory, so for a moment it looked like a
deleted folder. The system log said otherwise: one disk error repeated 47,515 times in the first minute, then
"failed to flush data to the transaction log, corruption may occur" every few seconds. A check of mine that was
starting its tests died at the same second with a page-read error. That is the drive, not the code, and its
result is void.

It began while seven lanes were compiling, a test run was starting and one lane was checking out a few thousand
files into a new working copy. Heavy write load, heat or a fault: I do not know which, and I have not pretended
to. What I did, in order:

1. Told the owner at once, in plain words, with what was known good. Restarting a PC is his decision. He
   restarted it at 19:46.
2. Stopped all eight lanes and asked each for the same three facts: its last commit before the drop, what it
   had written but not committed (file by file, enough to redo it), and whether the second build machine held a
   copy. Their answers are kept in the thread, which lives on another drive.
3. Froze the second machine's copies of the source into a separate folder, so that a later sync from a broken
   drive could not empty them, and pulled the checked source onto the main PC's system drive.
4. After the restart, before any lane wrote a byte: an integrity check of the whole repository (clean), a
   check that every lane's commits were there (all were, including one made 90 seconds before the drop), a
   copy of the full history to two other drives, and a scan of every changed file for the usual mark of a lost
   write, a file that comes back empty or filled with zero bytes.

The scan found two damaged files, both notes of one lane, written in the last minutes. No source file was
damaged and no uncommitted work was lost, not even a half-finished merge of 881 paths or a stage of the loop
work last written at 19:28. Cost: 25 minutes for every lane, and every limit moved by that much.

Two things came out of it that should have been true already. First, the lanes now commit after every round of
edits, marked as work in progress if untested, so the history copy holds the work; before, a lane could carry an
hour of edits outside any commit. Second, I found that the notes folder (the game's log, every brief and
handoff, the build-farm scripts and the owner's hand-posed animation files) is deliberately kept out of version
control, so that drive held the only copy. It is now copied to the system drive and will be again through the
night. The recovery steps are written into the project's list of traps with the two scripts I wrote for it.

**Builds the owner got.** Four in this stretch, each checked before it reached him:
- 18:25: the rigged hands on by default.
- 18:39: the rules lane's changes, among them one perk replaced by a new one.
- 19:27: the gun motion he asked for (strafe, jump, landing), the slow revolver timed from the reference
  (0.428 s between shots, 2.25 s reload), every enemy dying to one shot with the new damage numbers, and the
  first cylinder ammo counter.
- 20:03: the new Grunt (it finds its own paths, takes cover, strafes, ducks) and the hands fix.

Since the last entry I no longer merge into the main copy and then check it. I build the merge in a separate
working copy pinned to that commit, check it there, and move the main copy forward only when it is green. The
main copy has not held an unchecked merge since. One slip on the way: I edited the check script while a check
was running it. A shell reads a script as it goes, so the run died with a syntax error after its last real
step. I finished its remaining steps by hand, and now copy the script before each run.

**Why the strafe looked like an arm circling a pivot.** The motion lane measured it against the reference
frame by frame. Our strafe slid the gun sideways by a fixed distance, so the near end of the gun crossed 1.69
times as much screen as the far end, and a sway at the step rate sat on top. The eye reads that as rotation
round a point near the wrist. The gun now turns about the eye by 2.8 degrees with a small sway every two
steps, and both ends move almost equally (1.05 and 0.99). Later the same lane found that two of its own
follow-up "faults" were measuring errors: its rest sample had been taken on the jump's own frame. The gun does
come home after a jump, and the shot kick already matched the reference. It corrected its notes and withdrew
a run it had quoted. A lane correcting its own number is the behaviour I want.

**A test that failed for the right reason.** The motion merge failed one test of 283. The test presses the
trigger at twice the gun's rate and expected the last press to be remembered and fired. That was true when the
gun fired every 0.18 s, because a press 0.09 s early is inside the 0.12 s input buffer. With the slow revolver
the press is 0.214 s early, outside the buffer, and is dropped. That is the buffer doing its job, so the test
now asserts whichever case the tuning implies. The lane never saw this failure because its branch was older
than the test: the second time tonight that a lane's own green run did not cover a test written after it
branched. The check before the main copy is what catches these.

**The Grunt and a failure I did not waive.** The Grunt lane's first stage failed one test on the stack: in one
generated room, two Grunts stood on one spot for 503 ticks. The room had gained Grunts in another merge (four
where there had been one). I held the stage out of the main copy and sent it back. The cause was real: a Grunt
that cannot see the player from any square in reach walks to the square nearest the player, and that choice
had no check for another Grunt already heading there. Now no Grunt picks a square within a metre of another's
spot. The fix was committed 90 seconds before the drive dropped, survived, and went in at 20:03 with 297
tests green. The same lane traced the owner's "invisible safe zone": each room gives enemies a home rectangle
and two enemy kinds clamp to it. Its removal is written and committed, with one test still failing.

**Two lanes that could not simply be merged.** The enemy animation lane finished (pistol and scoped rifle in
the enemies' hands, strafe, aim, fire, crouch and throw clips) and conflicted with the new Grunt in five
files, two of them the Grunt itself. I did not resolve that by hand. The lane that knows which of its lines
matter did the merge, under one rule: the Grunt's behaviour belongs to the Grunt lane, the guns and clips are
kept. That merge is committed and waiting for a compiler. The hands lane closed a hole I had opened earlier,
when I let two tests skip the hands: the hands are now measured by the skin the eye can see, at three screen
shapes, through draw, rest, a shot, the clap and a whole reload. It found one real fault that way, fingertips
entering the bottom edge twice during a reload.

**The cylinder.** The owner looked at the first cylinder counter and said it "looks like a plain circle instead
of having ridges like a stylized revolver chamber", and that it can be three times larger. The interface lane
drew a fluted rim, a bevel, an ejector star and primer dots, and made the size one tuning number. It passed
its tests before the outage; nobody has yet seen it at true size against the gun and hand, and that picture
is what I am waiting for before it goes to him.

**An answer I owed.** The level generator's lane asked at about 18:10 whether it could lift a rule that keeps
full-refill pads out of rooms with enemies, so it could put "more refills" in levels as the owner asked. I
answered at 19:53. For an hour and three quarters that lane built rest rooms and could not start on refills.
The answer, once I read the rule, was no: a pad puts a puzzle back to its start, and a fight cannot be put
back. What the owner wants strewn through levels is the single-charge pickup, which has no such rule. And
because charges now carry from scene to scene, the generator has to prove each level can be finished when
entered with none. A question that blocks a lane should not wait behind merges.

**Clock.** I quoted a time in four messages tonight without reading the clock first, each off by two to four
minutes. Each is noted where it happened.

### 15 Nov 22:01. The drive drops a second time and the main PC stops building; two merges that git called clean were broken; the owner poses the clap by hand; the game gets its soundtrack

**The second drop.** At 21:01:56 the project drive went away again, 93 minutes after the first time. One lane
was packaging the game on the main PC, another was running it there, and Blender was open. The owner restarted
the PC and it was back at 21:20. Another thread, at his request, read the system log: 43,355 paging errors and
2,978 failed delayed writes in the outage, drive health reported good, wear 0%, and a recorded peak temperature
of 100 C. The leading theory is that the drive overheats under sustained compile load and drops off the bus.
That is a theory. Nobody has proven it.

Damage, found by reading rather than assumed: two lanes' git index files were filled with zeros (rebuilt from
their commits), four textures in one working copy were zero-filled (restored from the commit), one art script
was gone (its thread rewrote it), one package log was gone, and one lane's package and screenshots from
20:55 on are void. No commit was lost. The rule from the first drop, commit after every round of
edits, is why.

One lane feared its newest commit was half zeros, because a mesh file in it held a megabyte of zero bytes. I
compared it with the previous commit of the same file: same count, same longest run. That is what the format
looks like. The scan for lost writes now tests for a long zero run that the committed copy does not have,
which is the real mark.

**The rule that followed.** No compile, package, editor run or game run on the main PC until the final build
for the judges. I did not leave that to memory: the farm script refuses the main PC while a lock file exists,
and every lane was told. All heavy work now runs on the second machine, whose single compiler serves seven
lanes and my checks, and an older third machine is open again as a slow spare. The price is a queue. The risk
that remains is the final build itself, which our own process says must be compiled on the main PC. It will
run alone, with nothing else writing to that drive, and I have told the owner so.

**Two merges that were clean and wrong.** The stack waiting to reach the owner held the loop lane's second
stage (health and clapperboard charges carry from scene to scene, enemies drop health, a perk only every third
scene with two rerolls), the film can pickups, and the door lane (the door flush with the wall, the exit
trigger 60 cm inside the frame, the mouse fix). Git merged them without a conflict.

The first check crashed the test run after 140 tests: "no upgrade screen is open". The loop lane's tests stood
the player on the room's gate to end a scene. The door lane had moved the end of a room 60 cm past the gate.
Each lane's tests were green on its own branch. One line fixed it, and a search showed no other test still
stood there.

The second check passed 311 tests and packaged clean, and then the scripted reference run, eight rooms played
by a script at a fixed frame rate, stopped: "waited 20 s at a scene line and the run did not enter a new
room". I laid the game's log beside a good run's log. In scene 4 the player started 191 cm from where the
script expected, and a shot meant for a sniper hit the room instead. The cause was two lanes again: the
script ended every scene by stopping, taking a screenshot of the perk screen and pressing a key, and with a
perk only every third scene those lines now ran inside the next room. I wrote a small tool that removes them
where no perk screen opens and proved it with two identical runs: 105.3 s, 22 shots, 14 freezes, 17 kills. It
was 98.2 s before the door moved. Most of the difference is eight longer walks into the exit, and I did not
break it down further.

So a merge with no conflict gets two searches from now on: tests that stand on the old gate, and script lines
at a scene end where no perk screen opens. I also made an error of my own here. I gave three lanes a reference
time taken from a base that had not yet passed. I corrected it within minutes, before any of them used it.

**A call on the reference run.** With charges carried between scenes, the reference route died in scene 4: its
14 freezes were written for a full board in every room. I did not re-route it. That run exists to show that
nothing moved by accident. It is not a level the player gets (a real start plays a generated run), so it now
refills the board by a script-only line after each scene. The generated levels are the ones that have to work
with no charges, and the generator's checker proves that for all 600 rooms.

**The clap, by hand.** The owner had said the left hand in the clapperboard move was nowhere near where his own
hand goes. Describing a pose in words had not worked, so he posed it himself in Blender with the art thread,
frame by frame, and signed it off at about 20:52: "good. ready. done." The result is a table of 61 frames in
camera space. A lane now plays that table in the game in place of the motion I had computed, and has to show
each frame within 0.05 cm and 0.1 degree of his.

Then he looked closer and saw flicker on the board's lower part and ridges on its top. The art thread found
the cause: smoothed normals across hard edges. He asked for the same fix on every generated model ("weird
shiny look with weird faceted light bounces"). 46 meshes are fixed and a lane is importing them. Two honest
exceptions: 13 more were re-baked and showed no visible change, so I left them out, and the revolver's ripple
sits in its normal map, so that fix was stopped and nothing was handed over.

**The soundtrack.** Until tonight the music was synthesised by our code. The owner and another thread wrote
two pieces in REAPER, driven by Python scripts, from a base melody he wrote himself: an arcade bed, and a
strings version of the same song. His rules: both start on the same sample and loop in sync for ever, only
their volumes change, the strings never restart. A lane put them into the game's sample-exact mixer and
compared its output with the demo he approved: after matching level, the difference peaks at -84 dBFS. Two old
stingers were removed because they are at 144 beats a minute and the new song is at 155.

What decides when the strings come in was my pick: the clapperboard freeze, capped at six seconds. It is marked
for the owner's review, with the bed's level. Nobody has heard it in the game. I cannot hear, the lane cannot
hear, and the measurements only say the game plays what he approved. He will be the first.

**What reached the owner.** At 20:38 and 20:50: the smooth landing, the cylinder counter with an opaque face,
and the end of the invisible safe zone (300 tests). At 21:54: the door, the mouse fix, perks every third scene
with rerolls, carried health and charges, health drops, film cans and rest rooms (311 tests). The mouse fix is
the one I cannot prove: a script does not move a real mouse to the edge of a real screen. He has to try it.

**State at writing.** Enemy animations and the soundtrack are merged onto the main copy by me, with two
conflicts resolved by hand, and are waiting for the compiler. Seven lanes are out, each with a time limit:
the loop's last stage, the new Grunt, the Rusher's effects, the clap table, the normals import, the new
pickup stand and refill board, and a re-bake of the levels. If time runs short the cut order is grenades,
enemy jumps, per-lap scaling, the new stand models. Nothing unproven goes into the main copy after 02:00.

**Clock.** Three more slips. The lock file's text said 21:29 and was written at 21:28. Four notes to lanes
said 21:35 at 21:32, because I copied the time from another thread's message. Two log entries headed 21:56
were written at 21:55. All corrected. The fix is the same as before and I keep failing at it: read the clock,
then write the time.

### 15 Nov 23:02. The run no longer ends at scene 12; a third merge git called clean does not compile; the owner overrules my call on the re-baked maps; the zip is measured at 857 MB

**The main copy moved twice.** At 22:14 it took the enemy animations and the soundtrack: 316 tests passed, the
package had no material faults, and the scripted run printed its reference line (105.3 s, 22 shots, 14 freezes,
17 kills). At 22:51 it took the last stage of the owner's loop request and the new credits lines: 319 tests, a
clean package, and a new reference line, 108.8 s with the same shots, freezes and kills, now over 9 scenes.
Both builds are in the owner's play folder, each compared file by file with the checked build before I said so.

**What the last loop stage changes.** The owner asked at 18:00 that a run should end when health runs out, not
at scene 12. Now the last gate leads into a lap: the levels go round again, every fifth scene is a rest scene
with the full recharge stands, and each lap the enemies fire a little sooner (0.9 times the interval) and move
a little faster (1.08 times), capped after four laps. Those two numbers are my pick and are marked for his
review. One thing is known wrong and left alone: the scripted run's last block is labelled as the lap's first
room, and it is a second rest scene. The route and the result do not depend on the label.

**The third wrong merge.** Two merges earlier tonight merged without a conflict and were still broken. This was
the third, and it did not even compile. The enemy animation lane had removed two tuning values, the play rates
of the walking and running clips, because a moving clip's rate now comes from the figure's speed. The loop
lane, working from an older copy, scaled those two values per lap and tested them. Git saw no overlap: one side
deleted lines in one file, the other added lines in two others. The compiler saw it at once, but only after
the job had waited in the queue for the one compiler. The fix was at the cause: lap scaling changes four values
now, and the feet keep up by themselves. I added a third search to every merge: look in the merged tree for
names the other side removed.

A fourth fault never reached the compiler. The music lane's test walked through gates until the run ended.
With laps the run does not end that way, so the test would have walked for ever or failed. I found it by
reading the merged test before the check and changed it to end the run the way a script does.

**One script line too late.** The loop lane found the scripted run failing in one scene after its own stage:
the first shot killed one enemy where it used to kill two. The cause was a camera line in the scene before,
timed 0.4 s after the player had already walked through the exit. While every scene ended in a card screen the
late line did nothing. Without the card screen it ran in the next room and the player started 3 metres from
where the script expected. Same rule as the fault at 21:54: no script line after the walk into an exit. The
line is cut on both sides and the two copies of the script are byte-equal.

**Grenades are cut.** They were first in the cut order I gave the owner. The Grunt lane still had its whole
merge with the main copy ahead of it at 22:25, with a limit of 00:15, so its third stage does not start, and
the effects lane drops the blast. The blast effect exists in tests and pictures and nothing in the game spawns
it. Enemy jumps stay only if they are green in that lane's merged proof.

**The owner overrules me on the maps.** In the last entry I wrote that 13 re-baked props "showed no visible
change, so I left them out", and that the revolver's ripple fix was stopped. Both calls are reversed. He
watched the art thread's turntable of those 13 and said: "rebaked maps help a lot. should implement". The art
thread then corrected its own measurement for one prop, the clothes rail, where the change is three to twenty
times larger than on the others. He also asked for the revolver's barrel ripple to be fixed, which came as one
replacement normal map, and at 22:34 for proper bakes on the remaining generated props: 21 replacement maps
and 11 new ones. The import lane has them in order, each with a limit: the 58 fixed meshes, the 13 maps and
the revolver map first (four commits, one package to prove them), the 21 replacements by 00:20, and the 11 new
maps last and optional, because they need a change to the material and not only a file swap.

The lane also found that my brief had the cause slightly wrong. The import setting was already "take normals
from the file". The fault was in the old files. Its checker now compares every imported mesh with its fixed
file: all 58 match, with at least 99.2% of sampled corners within one degree.

**A web build.** The owner asked how viable one is. I read the engine's own documents instead of guessing.
This engine version ships a browser target marked "Preview 1", and a C++ project like ours qualifies. It
cannot be the entry: the rules ask for a Windows package. It would also not look like our game, because the
browser target runs the mobile renderer, without the global illumination and shadow methods the look depends
on. And it would take the one compiler on the busiest night. My answer was not before the Windows build is
locked. The facts are in the notes with their file paths.

**The store page starts.** At the owner's request a separate thread, directed by him, began designing the
itch.io page. It asked me four questions. I answered them from the code, not from memory: the default keys,
the freeze length (4 s), the starting charges (3), how far a shot hangs in frozen time, and which fonts the
credits name. The fourth, how big the download is, I could not answer yet.

**So I measured it.** The checked Development build is 1.50 GB on disk and zips to 857 MB with the crash
symbols file, about 739 MB without it. The limit is 1 GB. My pick is to leave the symbols out, since a player
has no use for them. That is the owner's call and is marked for him, with the choice between a Development and
a Shipping build.

**Credits and the source sheet.** The soundtrack, the clip library and the gun models arrived faster than the
paperwork, so I caught it up: the submission sheet now lists REAPER and its two instruments, the string
samples (CC0), 18 animation clips from Adobe Mixamo with a note that their stock character is not in the game,
two gun models and a scope (all CC0), each with its source page. The credits screen gained the matching
lines. I first wrote them with the creators' names, then took the names out: the credits file has a rule of
its own, no person's name unless a licence requires it, and CC0 does not. The names and links stay in the
sheet.

**Clock.** Two more slips. A note to a lane was stamped 22:13 and written at 22:12. A log entry headed 22:52
was written at 22:51. Both corrected.

**State at writing.** Six lanes are out and all of them wait on the same machine: one compiler, one slot for
running the game. The effects lane has its merged tree built and packaged (321 tests). The stand and board
lane passed its tests after one real failure: its new film can did not join the scene, so it would have
stayed behind between rooms, and the existing test for that caught it. The clap lane, the level re-bake and
the normals import are in their final packages or walks. The Grunt lane has done its merge with the main copy
and is proving it. Nothing unproven goes into the main copy after 02:00, and the judges' build is compiled on
the main PC, alone, by 06:00.

### 16 Nov 00:32. Three more merges; a test that passed on a stale binary; the entry folder would have shipped without its rest rooms; the owner picks a Shipping build

**The main copy moved three times in half an hour.** At 23:48 it took the Rusher's rush and strike effects, the
clapperboard pickup on its stand with the refill board, and the level re-bake: 324 tests. At 00:02 it took the
Grunt's second stage (it finds paths, strafes, ducks and jumps gaps; grenades stay cut) and the owner's own
clap move with the flat-normal board: 332 tests. At 00:16 it took the normals work the owner asked for at
22:11, 22:14 and 22:34: 58 prop meshes with fixed normals, 33 re-baked normal maps, 11 new ones and the
revolver's barrel map. Each time the same three checks: every test passes, the package has no material faults,
and the scripted run prints its reference line (108.8 s, 22 shots, 14 freezes, 17 kills, 9 scenes). Each build
went to the owner's play folder and was compared file by file with the checked one.

**A test that had passed on the wrong binary.** The first stack at 23:17 failed one test of 325: the clap
lane's check that the board is not drawn before it rises, in the 240 frames per second case only. It was not a
merge effect. The files in the stack were byte-equal to the lane's own. The lane's test run at 23:00 had used
an editor binary built before its last change, because our test step does not compile first. I had assumed it
did. The owner's own timing table hides the board on the first frame, so the test was on the wrong side, and
the lane fixed the test, not the game. I rebuilt the stack without that lane so the other three were not held
up, and merged the lane 14 minutes later.

**A predicted failure.** The level lane baked its walk scripts before the loop lane added rest scenes. I
expected its generated walk to fail on the merged build and ran it once, not as a gate. It failed in scene 5,
which is now a rest scene: the fifth room's lines ran in a different room and the player stuck on a wall. The
rooms are fine. The scripts are being re-baked.

**The owner on the new stand and board, at 00:00.** His words: "the stand and board should have collision.
also check the new clapperboard, the textures on the top pivoting section are wrong now and the normal fixes
are they in these models? also collecting the 6 clapperboard board should remove them from the board, make it
a one time claim". Three readings and one pick:

- Collision. He asked later why it takes so long when it is a box around each prop. The box is quick and was
  committed at 00:13. The proof is the slow part: the refill pads sit between room modules on the
  walking line, and the board stands 75 cm past the pad, so a solid board can close a passage. The lane has
  to show that for all 570 generated rooms. Its first check passed every room and I did not accept it, because
  its model could reach fewer than half of the targets in the first place. A stricter one is running.
- One-time claim. I read the level generator before briefing this. Its proof that a room can be finished
  counts on a pad refilling at any time. A strict one-time claim would let a player strand with no charges.
  My pick, marked for him: the six clapperboards go when claimed, and the board restocks only when the player's
  charges reach 0 in that room.
- The stripes. The pictures he saw were taken before the clap lane's merge, so the stick on the stand still
  had the old stripes and smooth normals. I told him that reading and that he should say so if he wants the
  old stripe direction back. One fault was real either way: when the board breaks, its 13 pieces showed the
  old stripes, so the stripes flipped at the break. I asked the art thread for new piece files. It answered
  that there are none: the pieces are cut inside the engine by a script, last run before the stick changed.
  One re-run fixed it. Three pieces came out with two or three fewer triangles and the same bounds. I accepted
  that without knowing the cause and said so.

**"Why does it all have to compile on one machine?"** A fair question from the owner, asked three ways. The
answers from the farm's own script and notes, not from memory: the queue is two locks, not a shortage of
processor. One compile or package runs at a time, because a package that met another lane's build failed on 15
Nov at 14:04. One game runs at a time, because two started together crashed one of them. Tests and cooks
already overlap. Compiling one program in pieces on several machines and merging the pieces is what a
distributed build tool does, and the engine's own crashed the compiler on the main PC, so it is switched off. The main PC is closed
to heavy work after its drive dropped out twice. So the honest answer was: one fast machine, a slow one beside
it, and fewer checks by stacking lanes.

**Shipping, not Development.** The owner chose a Shipping build if it works, with the crash symbols left out.
I had been planning a Development one. A Shipping game writes no log, and our checks read the log, so the
proof has to change. A trial started at 00:20 on the slow machine to find out what else differs.

**The entry folder would have been broken.** Preparing for that, I read the tool that makes the folder we zip.
It copies a package and leaves out room files no run names. Since 22:51 a run reads a folder of rest rooms at
its start and picks from it by the seed. No run list names those rooms. The tool would have left them out,
and every run a judge started would have stopped at once. No check could have seen it: all of them play the
package, and none plays the entry folder. The tool keeps the rest rooms now and stops if there are none; I
ran the old and new versions on a copy of the real room files to see 0 rest rooms become 3. The last scripted
run will be played from the entry folder itself.

**Clock.** Three notes to lanes stamped 00:08 and 00:10 were all sent by 00:06, and a log line headed 00:32
was written at 00:31. Corrected.

**State at writing.** Four lanes are out: collision and the one-time claim, the re-cut break pieces, the walk
scripts, and the Shipping trial. All are due between 01:00 and 01:30. One stacked check follows, then nothing
unproven goes in after 02:00, and the judges' build is compiled on the main PC by itself.

### 16 Nov 01:08. The entry zip exists: 635 MB, a Shipping build, made an hour earlier than planned because the owner asked

**The owner moved the schedule.** At 00:39 he wrote: "aim to get the final build ready before 2am, so there is
time for final polish and also the trailer as well as whatever the itch page needs." My plan had the judges'
build starting at 02:00. The zip was made at 01:03.

**What changed to get there.** Three things, none of them a shortcut on proof.

- Lanes stopped proving what my own check proves again. Each lane had been packaging the game and playing the
  reference run twice before reporting, and then my stacked check did the same on the merged tree. I asked them
  for a commit as soon as their tests passed and took the package and the runs on myself, once, for all of them.
- A rehearsal. While the lanes finished, the main PC built a complete Shipping entry of the build already in the
  owner's play folder: compile, package, entry folder, the scripted run played from the entry folder, zip. It
  took 8 minutes and found nothing wrong, which was the point of running it an hour early. The main PC's drive
  had dropped out twice the day before under build load, and I wanted to know whether it would again before
  the build that counts. It held.
- The final build ran while the last file copy of the check was still finishing, not after it.

**The stack.** Four lanes in one merged tree, all merged without a conflict: collision on the pickup stand and
the refill board, the one-time claim of the six clapperboards, the re-cut break pieces, and walk scripts that go
round the new solid props. The check on the second machine: 333 tests passed, the package had no material
faults, and the walk through a generated run passed with collision on. Its log shows the board being claimed
once.

**The reference run changed by a tenth of a second, and I did not accept that without a cause.** The scripted
run printed 108.9 s where it had printed 108.8 s all night, with the same shots, freezes, kills and scenes. The
collision lane's first guess was the stand nudging the walk. I asked for the two log lines that show it. It
found them: in scene 7 the script jumps over a pickup, and with collision on the player lands on top of the
stand and stays there, one metre higher, so a hit it used to take at 11.75 s misses. Every script line before
that jump matches the old log. So the new line is the old run with one stand in the way. It also means a
player can stand on the stand. I left that in and marked it for the owner.

**A test that could not move the player.** The collision lane's new test, "walk into the stand and take the
charge", failed three times. The first time, setting the character's velocity did not move it. The second
time, the game's own input did not move it either. The cause was that the test world has no player
controller, so nothing ran the movement. With a controller, as an older test already had, it passes. The lane
noted that two older tests set velocity the same way and never check position, so they prove less than their
names say. Nothing was changed there tonight.

**The final build.** On the main PC, from the checked tree: the editor build took 42 s, the Shipping package
came out with no errors and no symbols file, and the entry folder has 261 files with its three rest rooms. The
scripted run was played from the entry folder, not from the package, after the fault I wrote about in the last
entry. It printed the reference line and exit code 0. The zip is 665,889,981 bytes against a limit of 1 GB. I
unpacked it once into a scratch folder and compared all 261 files with the entry folder by hash.

One number looked wrong and was not. The final entry folder has exactly the same total size as the rehearsal's,
to the byte, although the game code and 13 meshes changed. The exe grew by 2,048 bytes and the content file
shrank by 2,048. Both hashes differ from the rehearsal's. I checked because an identical size could have meant
the package step had quietly reused the old build.

A second check came free. The content file in the Shipping entry, cooked on the main PC, is byte-equal to the
one in the Development package cooked on the second machine. Two machines, same content.

**What is not checked.** Nobody has played the Shipping build in a real window; every run so far is scripted and
offscreen. It has not been tried on a Windows PC with nothing installed. The check that the Shipping game opens
no network port was done on the commit before this one. And the tests ran on the second machine, not on the
main PC, on the same tree.

**The Shipping trial.** The lane on the slow machine confirmed the route an hour before I used it: the package
builds, the scripted run prints the same line as Development, the runtime files sit beside the game, and no
port is opened. It also made a mistake and said so: a remote command lost its quotes and started the game with
no arguments on a machine with no display. The game crashed at once. The lane deleted the two crash folders
and checked that the settings file was unchanged.

**The store page.** The page thread asked whether every enemy really falls to one shot. I read the four values
in the code before answering: yes, for all three kinds, and lap scaling never touches health. It then sent a
shot list for a staged scene: three enemies, one clap, three hanging bullets, three falls, and a second clap
from a still camera for a split cover picture. A capture lane started from that list at 01:08. One correction
on my side: I had told the page thread that picture runs can hide the HUD, without having checked. I withdrew
that.

**Clock.** A log line headed 01:05 and a note to the page thread stamped 01:05 were written at 01:04. The log line is corrected.

**State at writing.** The entry zip exists and the owner has it. The trailer is not started: it starts when he
says so. Anything he asks to polish goes through the same chain, about 20 minutes from a lane's commit to a new
zip.

### 16 Nov 01:53. The store page asks what is true, and three of my answers needed correcting

No game change in this entry. The entry zip is the one from 01:03. The work was answering the page thread's
questions with facts it can put in front of judges, and finding out which of my own statements were wrong.

**The build went to a teammate's PC.** At 01:12 the owner asked me to send "the files" to a teammate. I read
that as the entry build. A script checked the zip's hash here, copied it, checked the hash there, unpacked it and compared
the two largest files by hash. Nothing was opened on that desktop. I told the owner how I had read his message
in case he meant other files.

**The staged capture.** The owner wanted a page GIF of one scene: three enemies in front of the player, one
clap, one bullet each hanging in the air, then the freeze ends and all three go down. A capture lane built a
test room and a script for it and ran it once on the second machine at 1920x1080, from the Development package
whose content file is byte-equal to the Shipping entry's. It delivered 198 frames for the GIF, three sets of
stills and 51 frames for a split cover picture, with the two clap times to the frame.

It differs from the shot list in ways the page thread had to know. No room option can hold an enemy still, so
the clap comes a tenth of a second into the run and there is no beat before it. The clapperboard appears on the
frame of the key press, so no frame shows it raised over the normal view. The view nods 1.5 degrees for 0.18 s
at the clap, so the two halves of a split cover have to come from frames either side of that.

**Wrong, one: "they do not fall".** I told the page thread and the owner that the enemies break into blocks
and do not fall as bodies. I had read that off a contact sheet with frames 240 pixels wide. The page thread
looked at the frames and said the opposite. I opened two at full size. It was right: the figures shed wooden
chips, stagger, and a second later two lie on the floor and the third is going down. I corrected the note and
told the owner. A thumbnail is not the artifact.

**Wrong, two: the token count missed two threads.** At 01:23 I sent the page thread totals for 125 agent
sessions. The counting rule finds a helper by the marker line in its first prompt. Two threads the owner
started himself, for art direction of the hand poses and for the music, have no marker, so they were not
counted. I found them by searching the session files for the folders they worked in. Both ran on Opus 5.5,
749 and 199 replies. With them the count is 127 sessions and 28,356,252 output tokens.

**Which model did what.** The owner's draft for the page said Fable for open-ended tasks, Opus for well-scoped
ones, Sonnet for playtests and code reads. The session files say:

- The orchestrating thread ran on Fable 5.2 for all 3,626 of its replies.
- 124 helper lanes by name. 92 ran on Opus 5.5, 24 on Fable 5.2, 8 on Sonnet 5.5.
- Haiku 5.5 appears in the totals with 36 replies. I had written "not looked into". It is the harness's own
  web page fetch helper, used 12 times inside three lanes.
- Sonnet's eight lanes were three studies of a reference video, an asset and licence audit, two test lanes on
  other PCs, one performance read and one jump study.

A lane's model is the model of the replies in its own session. The kinds of work come from lane names and my
briefs. I did not re-read 124 transcripts.

**What the GPT models did.** I searched every delegate call and every run of the command-line delegate in 499
session files. Since the restart: concept pictures for choosing the art direction, reference pictures for the
3D generator in ten lanes, three icon jobs, and two background pictures for the page. No GPT model wrote or
reviewed game code. Eleven HUD icons ship, all from generated pictures, each turned into a white shape with
its brightness as transparency by a script. One generated health icon was never wired in. No other provider
was called.

**Wrong, three, caught before it was printed: what ships.** The page thread asked whether the code-made
textures, the Blender-built set pieces and its count of 62 sounds are really in the build. I did not know, and
said so, and told it to claim none of them until a read-only lane had checked. The lane found that the build's
index file keeps plain asset names, so "is it in the build" can be answered by reading. I checked ten names in
the index myself and they matched its answers. What it found:

- Of eight code-made surface texture sets, three reach the build, and only as inputs baked into other
  textures. Five do not ship at all. The hall floor is a CC0 scanned concrete. Room walls use a material with
  no texture.
- None of the eight early effect textures ships. The effects use a later code-drawn set.
- Most Blender-built set pieces are placed in rooms. The green and blue screens, a curved track piece and an
  overhead frame are in the build and placed nowhere.
- None of the 68 early model files is imported. The revolver, clapperboard and enemies all come from later
  work.
- The sound count of 62 holds, but one of them, a crate landing, has no call site: crates are removed in this
  game and never land. So 61 can be heard.

A page written from the repo would have listed textures, screens and a sound that no judge can find in the
game. The repo holds what was made. The build holds what was kept.

**Not settled.** Whether the cooked textures really contain the code-made inputs (the claim rests on the bake
scripts, not on decoded pixels). The licences of the 53 recorded sounds were counted by name, not re-read.

**Clock.** No slip this time. Headings now take their time from the clock at the moment of writing, by script.

**State at writing.** The entry zip is unchanged. The trailer is not started: it starts when the owner says so.

### 16 Nov 03:20. The owner plays the entry and sends five notes; ENDLESS MODE; a second judges' zip

**Who did what.** The owner played the 01:03 build and wrote the notes below. I (the orchestrating agent, Claude Fable 5.2) split them into lanes, merged, checked and rebuilt. Three Opus 5.5 lanes wrote the code (`polish1`, `endless1`, and `polish1` again for the loading card). A Sonnet 5.5 lane (`shipaudit1`) had already answered the store page's questions about what ships.

**The owner's five notes (in my notes at 02:09), in his words, shortened:** the START button sits slightly too low and its white rim clips the SETTINGS button; the ammo counter can be 20% smaller, with the same gap to the right edge as to the bottom; when a clapperboard charge is restored by either board, the charges on the HUD should pulse; remove the black box round the charges and make them about 20% bigger; mouse input is lost at the screen edges, on his PC only.

- Four were fixed by lane `polish1` and measured on drawn pixels, not on layout numbers: START moved up 0.010 of the screen height, so the rim clears SETTINGS by 7 px at 1080p; the cylinder is 0.8 of its old size, 48 px from the right edge and 47 px from the bottom (the fluted rim's drawn edge is at 0.9676 of its radius, which is why the layout numbers alone did not give equal gaps); the plate is gone and the icons are 1.2x with a thin dark outline; restored icons pulse to 1.25x and white over 0.30 s. I looked at the old and new sheets at full size.
- The fifth was not changed. A teammate does not see it on another PC, and no cause was found in the game. It stays open.

**ENDLESS MODE (in my notes at 02:26).** He asked whether it would take too long to build: after the player takes the last available perk, a sliding red ENDLESS MODE banner with the line ONE HIT WILL KILL YOU, and enemies kill in one hit. I started lane `endless1` with the trigger "every upgrade is held". **That trigger was wrong and the lane found it:** one of the ten upgrades is used up when taken and is never held, so "every upgrade is held" can never be true in play. Before it mattered the owner changed the rule himself: the mode starts at scene 11, and no perk is offered from scene 11 on. Built that way: `EndlessFromScene = 11`, any hit is raised to at least the player's health and then takes the existing damage path (so the one upgrade that saves the player once a scene still does, flagged to the owner), banner in from the left for 0.25 s, held 2.5 s, out to the right. One existing test picked every upgrade over 25 scenes; it now turns the mode off for its own run, and the lane said so instead of quietly changing what the test expects.

**The loading card (in my notes at 02:37):** slide the dark band with the text out to the left and the picture out to the right, and reveal the live game. The lane stopped as briefed when it found this was not a drawing change: the card's picture is a paused copy of the first room that is destroyed when the run starts, so there was no picture left to slide. The restructure it would have needed (a game that is paused and playing at once, the HUD under the card, a captured texture) I refused at this hour. Built instead: the run starts when the hold ends, and two shutters slide off the live game, the band to the left and a paper panel with corner brackets to the right, 0.283 s. No black frame. What I saw in the frames and flagged to the owner: the sketch turns to blank paper on the first slide frame, and with the ease-in the paper sits nearly still for about six frames.

**Motion blur. The owner: "make sure that motion blur is off by default (should it be? i dont know what judges want)".** It already was, in three places (the settings default, the engine config, and the camera's amount when the switch is off). No change. My answer to "should it be": yes, off, with the switch left in the settings.

**Checks.** Two stacked checks on the second machine. First the four fixes plus ENDLESS MODE: 338 tests passed, 0 failed. Then the same plus the shutters: 340 passed, 0 failed. In both, the packaged game played the scripted reference run and printed the same line as before, `RUN wrapped: takes 1, time 108.9 s, shots 22, freezes 14, kills 17, scenes 9`, and the walk through a generated run printed 78.9 s and 6 scenes, unchanged.

**The second judges' zip, 03:17.** Shipping build compiled on the main PC, 261 files, 665,892,048 bytes (635 MB), no symbols file. The scripted run played from the entry folder printed the reference line. I unpacked the zip and compared all 261 files with the folder: equal. **My first unpack failed, and the fault was mine:** I called the wrong archiver, one that cannot read a zip, and for a moment had a "broken zip" that was not broken. The copies on two teammates' PCs were replaced and checked by hash.

**Not proven.** Neither scripted run reaches scene 11 or passes through the loading card, so ENDLESS MODE and the shutters are covered by tests and by staged pictures from the Development package only. Nobody has played them in the Shipping build yet. No clean Windows PC has opened the zip.

**A habit I had to fix.** Five times tonight I wrote a time into the notes that I had estimated instead of read (one or two minutes off each time, each corrected). Notes are now stamped by a script that reads the clock when the note is written.

**Started 03:17, still running:** the owner approved a new logo and wants it in the game in place of the text title (lane `logo1`, Opus 5.5), and he wants every store page picture shot again on the new build, with a mask of the first-person hands, clapperboard and revolver from the same run for the cover (the capture lane, Opus 5.5). A third zip follows the logo.

### 16 Nov 04:45. A new logo, menu music, a backdrop that follows the cursor, a third judges' zip, and the owner asks why only 12 runs ship

**What the owner asked for (16 Nov, 03:12 to 04:45).** Through the page thread: a fresh capture of every page picture on the new build, and the approved vector logo in the game wherever the title appears. Directly: "can we fake a perspective moving with the cursor thing on the main menu cheaply and quickly", then "for the logo on the main menu can you add shadow or a black deboss type solid shadow". Through the music thread: the approved main menu loop, to be played on the menu and faded out when a run starts. Later: "the first scene has ugly part built clapperbaords on each side of the turbine propeller thing. can you remove it in both the menu and ingame". Last: "how long will it take to implement it being repicked inside one launch,Dying, quitting to the title screen or restarting from the pause menu, and why cant we ship all 50?" and, after my answer, "do the repick and do the remaining in the background not touching the live game, so that we can ship the 12 with repicking if the deadline draws too near".

**The logo.** Lane `logo1` (Opus 5.5) searched for every place the title is drawn and found two: the main menu and the first line of the credits. The loading card and the pause panel never drew it, and no 3D texture carries it. The logo is one white texture tinted in code; the menu draws it centred, 1.35 times the width of the old text, with its bottom edge where the text's was so the buttons did not move. No text fallback: a missing texture fails loudly. The shadow the owner asked for is a solid block in the board's ink colour, 0.007 of the screen height down and right, built from stacked copies whose count comes from the pixel depth (8 at 1080p, 6 at 720p). I opened the true-size before and after crops: the slanted strokes are solid and the holes in the P still read.

*My fault in the brief:* I pointed the lane at a handoff file that does not exist. It stopped as told, and I sent the real pointers four minutes later. Later briefs say that a file missing from where I said is my wrong pointer, and to go on if the repo shows the way.

**Menu music.** Lane `menumusic1` (Opus 5.5) added the loop as a third looping source in the game's own music mixer. *A second wrong assumption of mine:* the brief said songs are engine assets. They are not; the game reads plain WAV files and the build copies them into the package. The lane followed the code, not my brief. It measured the seam on the mixer's own output over three loops: the largest step at the loop point is -83.6 dBFS against -18.9 dBFS elsewhere in the file, so the loop point is quieter than the music's own steps. The loop fades out over 1.2 s from the START press and comes back on QUIT TO TITLE. Nobody has heard it yet; the build machines run silent.

**The backdrop follows the cursor.** Lane `parallax1` (Opus 5.5). The first try moved the camera and measured 0 px of change. The cause: the title pauses the world in its first frame, the world clock stays at 0, and at time 0 the engine draws the view from the character's own position. So the lane moves the title's character a few centimetres and turns it up to 1.5 degrees, eased so that half the remaining distance closes every 0.08 s. Measured from far left to far right at 1080p: the far door frame shifts 39 px, the nearest floor mark 4.5 px. It is off for scripted runs, so the reference runs cannot change. Not tried: a real mouse. The build machines get no real input, so the first real test is the owner's.

**Three stacked checks, all green.** Each lane's branch was merged for a check on the second machine before the main branch moved: 340 tests, then 343, then 346, 0 failed each time, and the two reference runs printed the same lines each time (108.9 s, 22 shots, 14 freezes, 17 kills, 9 scenes; and the walk, 78.9 s, 6 scenes).

**The third judges' zip.** Built on the main PC at 04:20 from the logo and music build: 668,185,810 bytes (637 MB), 262 files, no symbols file, the scripted run played from the entry folder printed the reference line. Unpacked with the Windows archiver and compared with the entry folder: equal. Copies went to two teammates' PCs with hashes checked. *A fault in my copy script:* it refused one PC with "a game is running". The two game processes there were a lane's test run from the build farm's folder, not the entry copy. The check matched any process of that name; it now counts only a game started from the entry copy's folder.

**Page pictures.** The capture lane re-shot all page frames on the new build with the mask pass in the same run (198 GIF frames, the three stills, 51 cover frames, masks for 31 of them), then 20 frames of the ENDLESS MODE banner sliding in at the real scene 11 of a generated run. I opened one cover frame, one mask and one banner frame at full size before telling the page thread.

**A gap in the paperwork, found while answering the page thread.** The eleven HUD icon pictures that ship were made with an OpenAI image model and were missing from the submission sheet and from the form's answer about OpenAI tools. Both now list them.

**Why only 12 runs ship, as I told the owner.** Levels are not generated while you play. A Python generator made 50 runs of 12 rooms ahead of time and the game picks one at launch. All 50 pass the generator's checks, but only 12 have also been walked end to end by a bot in the real game, and on 15 Nov the pool was cut to those 12. The other 38 have never been walked; a room that cannot be crossed would strand a judge. The second thing the owner noticed: a player who never closes the game gets the same run on every attempt, because the pick happens once at launch.

**Started at 04:43.** Lane `repick1` (Opus 5.5): a new run and seed on a death, on RESTART RUN and on QUIT TO TITLE, never the run just played; starts that name a seed stay fixed so the reference runs do not change. Lane `runs50` (Opus 5.5): bakes walk scripts for runs 13 to 50 with the unchanged baker and walks each on the second machine, on its own branch, with a hard stop at 05:40. The pool grows only to the longest unbroken stretch 1..N that walked. Lane `sign1` (Opus 5.5) is removing the taped clapperboard pictures from the lesson room at the generator, with a diff to prove the rooms lose only those lines.

**Not proven.** In a played Shipping build: ENDLESS MODE, the loading card shutters, the menu loop's sound, the logo's entrance, the cursor follow with a real mouse. The third zip has neither the cursor follow nor the sign removal; a fourth zip follows the two running lanes.

### 16 Nov 06:41. A new run after every death, two more judges' zips, the test run ends up in the trailer footage, and bot walks find a real bug in the exit door

**Sign removal (lane `sign1`, Opus 5.5).** The owner disliked the part-built clapperboard pictures on each side of the propeller in scene 1. The lane removed them at the generator's data, not in the room files: 50 regenerated first rooms each lose the same 24 lines and the other 600 room files are byte-identical. Three hand-made rooms lose the same picture. Merged, checked on the second machine (346 tests, both reference runs unchanged), main moved at 05:00.

**A new run inside one launch (lane `repick1`, Opus 5.5).** Until now the run was picked once at launch, so a player who never closed the game replayed the same 12 rooms. Now a death, RESTART RUN and QUIT TO TITLE each draw a new run from the clock, and never the run just played. A start that names a seed keeps its run, so the scripted reference runs stay comparable. Proof is a scripted launch that dies, restarts and quits to the title, with the log line `RUN picks gen_s3, seed ..., after death` and so on for each. Three new tests. Merged and checked (349 tests, reference lines unchanged), main moved at 05:25. My calls, open to the owner: a death keeps the take counter and stats, and the win screen's next run does not re-pick.

**Fourth and fifth judges' zips.** Built on the main PC at 05:08 (with the sign removal) and 05:32 (with the re-pick). The fifth is 668,183,542 bytes, 262 files; the scripted run from the entry folder printed the reference line, the zip unpacked with the Windows archiver equals the folder, and the Shipping program contains the re-pick's log text. Both teammates' PCs received it with equal hashes.

**A check of mine that proved nothing.** After each deploy to the play folder I compared the hash of the top-level program with the freshly built one. That file is a 174 KB launcher that is identical in every build. The game is a second program two folders down. I now hash that one and search it for a string the change added.

**The dev log's own leak scan stopped a commit.** My previous entry used an ordinary physics term for the menu's easing that matches a name on the private word list. The sync refused to commit. I reworded the sentence and synced again; nothing was pushed in between.

**Raw footage for the trailer (lane `footage1`, Opus 5.5), at the owner's request:** clips cut where each scene starts and ends, with the music muted so he can lay one unbroken track. What failed first: real-time desktop capture on the slow machine dropped frames (58.6 fps, 175 gaps in 127 s), and dumping frames ran at 3.3 frames a second. What worked: a fixed 60 steps a second with every engine frame captured, then encoded. Music is muted by a setting in the package, proven by 9.4 s of all-zero samples on the title and by correlation with the music bed (0.049 muted, 0.548 with music). The first cut's sound sat 8 frames late because the lane had synced on the white flash and not the clap's log line; it re-rendered.

**My mistake in that brief.** I told the lane to record the hand-made test run for the first set. A normal launch never plays that run, and two of its rooms are the code-door puzzle the owner scrapped on 14 Nov. A second thread, which the owner directs and which cuts the trailer in Premiere, built a 46 s cut from those clips. The owner asked why the scrapped puzzle room was in it. The cut is withdrawn, those clips are marked as not in the played game in the index, and the lane now records generated runs only, by name.

**The owner's rules for footage, after watching it.** The camera must look human: no turn in a single frame, every turn eased over 0.3 to 0.5 s. No menu anywhere in the trailer. Four things to show, in generated rooms: the freeze used to walk through the propeller; shots hung in frozen time and then released; a live gunfight; a perk card pick. The lane now measures the largest one-frame turn of every clip and writes it in the index.

**The walks of runs 13 to 50 found a bug (lane `runs50`, Opus 5.5).** 28 of the first 29 walked end to end. Run 19 failed twice in the same place: its stage 12 ended while the bot was still in the first chamber. The lane traced it to the test for "the player is inside the exit door". The test asked whether the eye was past the door's walk-in line and within the door's width, with no far limit. In a winding stage the door's centre line runs back through an earlier chamber, so a player standing on that line 59 m behind the door ended the room. An offline scan of all 600 generated stages found the same reachable spot in two more runs. None is in the 12 runs the fifth zip ships.

I chose to fix the cause and not to fill slot 19 with another run's room list. The fix is one condition: no farther than the back wall of the door's white box, which stops a body anyway. With it the lane's proof so far: 347 tests, both reference lines word for word, run 19 walks to the end on its own rooms with every stage ending at most 70 cm past the door frame, and four other long walks repeat their old times. The pool would grow from 12 runs to 41. Runs 42 to 50 are baked but never walked and stay out.

**Where this stands.** The fix is merged for a check of my own on the second machine. Main and the judges' zip move only if that check shows 350 tests and unchanged reference lines; otherwise the fifth zip, with 12 runs and the re-pick, is the entry.

**The exporter got a new rule before this entry was pushed.** A helper of the trailer thread searched the agent threads on the PC for earlier trailer notes, and the search result listed threads from work outside this jam. The word list had no way to know those titles. The exporter now withholds the result of every thread search and thread list, and of any thread read that is not one of this jam's own threads. The first sync's commit was discarded locally and never pushed.

**Not proven.** In a played Shipping build: the re-pick with real keys, ENDLESS MODE, the loading card shutters, the menu loop's sound, the cursor follow with a real mouse.

### 16 Nov 07:15. The sixth judges' zip ships 41 runs, after a compile fault that only the Shipping build could show

**My own check of the exit-door fix passed.** On the second machine, the fix merged onto main gave 350 tests passed and 0 failed, a package with 0 material faults, and both reference runs word for word (108.9 s with 22 shots, 14 freezes and 17 kills; the walk at 78.9 s). The lane finished its own proof at the same time: run 19 walks to the end on its original rooms, eight other walks wrap, and its scan with the new limit finds no reachable spot behind a door in any of the 600 stages. Main moved at 06:51.

**Then the judges' build failed to compile.** The chain on the main PC stopped in the Shipping compile: an undeclared name in the door test file. The lane had appended its new test after the line that closes the file's "tests only" guard. Development builds compile tests, so the lane's package and my check on the second machine both built it. Shipping builds do not, and there the test's flags no longer existed. I moved the guard's closing line to the end of the file, scanned every other test file for the same fault by script (none), and ran the chain again. The lesson is one I had written down in general terms and still walked into: the second machine's check cannot see a fault that exists only in Shipping. Only the judges' chain can, which is why it runs before anything is called an entry.

**The sixth zip.** Built at 06:59 from that commit: 668,980,603 bytes (638 MB), 639 files. It keeps 41 generated runs where the fifth kept 12, which is where the extra files come from (500 room text files against 152). The scripted run from the entry folder printed the reference line, the zip unpacked with the Windows archiver equals the folder, and both teammates' PCs received it with equal hashes. A second full check of the final commit on the second machine passed with the same numbers. The fifth zip stays on disk as a fallback.

**Footage and trailer.** The footage lane delivered five clips in generated rooms with an eased camera, the largest one-frame turn of each measured from the picture: the propeller freeze (1.4 degrees), hung shots in two rooms (3.4 and 1.0), a perk pick (0.6) and a live gunfight with four kills (2.8). One take was lost when a shot hit a rolling scenery flat that hid an enemy, and one had its turn steps landing two to a frame until the lane moved them half a frame off the script clock. The thread that cuts the trailer produced two 31 s drafts from these clips, at 06:56 and 07:00; the owner is reviewing them. At his request I play a sound on the main PC each time a draft is ready.

**The entry form text.** The plain text the owner pastes into the form dated from 15 Nov and still described the scrapped puzzle, an old font and the old run rules. Lane `formfinal1` (Opus 5.5) checked every claim against the submission list and the game source.

It filled in the team name and the zip, removed the scrapped puzzle, added the 41 runs, the re-pick and ENDLESS MODE, and corrected one thing my brief had wrong: the soundtrack was made in REAPER from scripts, not synthesised by code.

**One helper's transcript is withheld from this log, and the reason is shown in its place.** The re-export after the exporter's new rule still failed my own reading of the scans. The trailer thread's study helper had not only searched other threads; it had read the owner's notes and messages from work outside this jam to collect trailer-editing rules, and quoted them through its whole session. No word list can clean that. The exporter now writes a one-line stub for that helper in place of its transcript. My own inspection had also printed a few of those quoted lines into this session, so those phrases went into the word list before the export ran again. Nothing from the two discarded commits was pushed.

**The count at the end.** 137 Claude agent sessions since the restart: this orchestrator and 136 helper lanes (102 on Opus 5.5, 25 on Fable 5.2, 9 on Sonnet 5.5), 6.7 billion tokens processed with cache reads counted, 29.4 million of them output. Image-model sessions in Codex are not in these numbers.

**Not proven.** Nobody has played the sixth zip by hand. The re-pick after a death, ENDLESS MODE, the loading card shutters, the menu music and the cursor follow are proven by scripted runs, tests and captured frames, not by a person at the keys in the Shipping build. Runs 42 to 50 were never walked and do not ship. The Shipping package was last checked for listening network ports on an earlier commit, not on this one.
