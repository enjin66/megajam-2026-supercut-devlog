# Transcript: lane-feelstudy-move

Session 9a236f97-4b50-443e-addf-7f677a8b4aff. Exported by `tools/export_transcripts.py`; entries from Fri 13 Nov 2026 05:41 SGT on. Times are Singapore time. See the README for what is removed.

### Sat 14 Nov 14:10:38 · Brief from the orchestrating agent

Act as the research sub-agent for this task.

GLASSBOX-MEGAJAM-2026 lane=feelstudy-move

You are a read-only research helper for a study of first-person shooter game feel. The study is for a small game-jam FPS (Unreal Engine, single player, a revolver, rooms about 20 to 40 m across). You do web research only. Do the work yourself, start no subagents.

## Goal

Collect NUMBERS with a NAMED SOURCE for how well-known first-person games tune player movement and the camera. Return them in your final message (you write no files).

## What to find (use WebSearch and WebFetch)

Movement:
1. [another game] / [another game] III Arena movement constants (speed, accelerate, friction, air accelerate, stop speed, jump velocity, gravity). The source code is public (id-Software GitHub, bg_pmove.c / sv_user.c / pm_ values).
2. Source engine: [another game] 2, [another game], [another game], [another game] (walk and sprint speed in units/s, sv_accelerate, sv_friction, sv_airaccelerate, sv_stopspeed, jump height or jump velocity, gravity). Valve Developer Community wiki pages are the source. Give the unit conversion Valve states (1 unit = 0.75 inch = 1.905 cm) and convert each speed to cm/s and m/s.
3. [another game] (2016) and [another game] Eternal: player speed, any statement by id developers on movement speed, dash numbers. GDC talk "Embracing Push Forward Combat in [another game]" (2018) is one source.
4. [another game] 2 / [another game]: run and sprint speed (units/s, convert), air control statements, slide. Respawn developer talks or the data-mined values on wikis (say which).
5. Halo (any), Destiny, [another game], Unreal Tournament, [other-app]: base move speed in m/s where a developer or an official wiki states it.
6. Unreal Engine CharacterMovementComponent defaults (MaxWalkSpeed 600, MaxAcceleration 2048, BrakingDecelerationWalking 2048, GroundFriction 8, AirControl 0.05 [check], JumpZVelocity 420, GravityScale 1): confirm from Epic's docs or the engine source on the web. And the first-person template's values if stated anywhere.
7. Time to reach top speed and time to stop, wherever a source measures or derives it for any of the above (for [another game]-style friction you can derive: say it is derived and show the formula).
8. Jump: apex height and total air time for [another game], Source, [another game], Halo, [another game] where stated or derivable from jump velocity and gravity (derive and say so). Any developer statement on higher gravity on the way down ("fall multiplier").
9. Coyote time and jump buffer: [another game]'s values (the Player.cs source by Noel Berry / Maddy Thorson is public on GitHub: JumpGraceTime, the jump button buffer), Maddy Thorson's posts on forgiveness mechanics, Game Maker's Toolkit "Platformer Toolkit" defaults, and any FIRST-PERSON game that states it has coyote time or jump buffering ([another game] 2, [another game] Eternal, Dying Light, [another game], [another game], [another game]: only if a developer or the source says so).
10. Air control: what [another game] / Source / UE values mean in practice; any developer statement on why a first-person platforming game wants high air control ([another game], [another game], [another game], [another game] Eternal).

Camera:
11. Field of view: default and range in [another game], [another game] 2, [another game], CS (CS is 90 at 4:3, what is that at 16:9), [another game] 2016 / Eternal, [another game], Apex / [another game] 2 (note their odd scale), [other-app], Halo Infinite, Destiny 2 PC, [another game], [another game]. State for each whether the number is horizontal or vertical and at which aspect ratio, and convert to horizontal at 16:9. Any accessibility guidance on FOV and motion sickness (for example Game Accessibility Guidelines, Microsoft Xbox Accessibility Guidelines).
12. View bob: [another game] cl_bob, cl_bobcycle, cl_bobup values; Source cl_bob values; any developer statement on how much bob, and on offering a head-bob toggle (accessibility guidelines).
13. Camera roll or tilt when strafing: [another game] cl_rollangle and cl_rollspeed; other games that state a value.
14. Landing camera dip, view punch on firing (Source "punchangle", [another game] "kick"), camera shake rules of thumb from developer talks (for example Squirrel Eiserloh's GDC 2016 talk "Math for Game Programmers: Juicing Your Cameras With Math": trauma squared, max angle and offset values he suggests).
15. Mouse input: statements by developers on raw input, no acceleration and no smoothing for first-person aiming.

## Rules for the result

- Only report a number you saw on a page you fetched in this task. Give the page title and URL beside it. If you recall a number but could not confirm it on a page, put it in a separate list headed "Recalled, not confirmed".
- No vague attribution. Not "experts say": the person, talk, article or source file, and the year.
- If a page was blocked or not found, say so in one line and move on. Do not sign in anywhere, do not download game binaries or decompiled code (public source repos by the rights holder are fine to read on the web), install nothing.
- Do not read or print anything under a folder named `memory`, any file named `JAM.md`, files ending in `API.md`, or `.env` files. Do not print account, user or computer names.
- Plain words, short sentences, no em dashes.

## Final message format

A set of tables, one per topic above (movement speed, acceleration and friction, jump, coyote and buffer, air control, FOV, bob, roll, kick and shake, mouse). Columns: Game or source | What | Number as stated | Converted (cm/s, ms, degrees horizontal at 16:9) | Source title and URL. Then the "Recalled, not confirmed" list, then pages that failed. Keep the whole message under about 200 lines. Spend at most about 35 minutes; a good partial answer beats a late full one.

**Sat 14 Nov 14:10:40 · Tool call: ToolSearch**

```
{
 "query": "select:WebFetch,WebSearch",
 "max_results": 5
}
```

Result:

```

```

**Sat 14 Nov 14:10:47 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/bg_local.h",
 "prompt": "List every pm_ constant (pm_stopspeed, pm_duckScale, pm_swimScale, pm_wadeScale, pm_accelerate, pm_airaccelerate, pm_wateraccelerate, pm_flyaccelerate, pm_friction, pm_waterfriction, pm_flightfriction) with exact values and the line they are on. Also JUMP_VELOCITY and STEPSIZE if present."
}
```

**Sat 14 Nov 14:10:48 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/bg_public.h",
 "prompt": "Find JUMP_VELOCITY, DEFAULT_GRAVITY, DEFAULT_VIEWHEIGHT, CROUCH_VIEWHEIGHT, STEPSIZE, MINS/MAXS player bounds and any default speed (g_speed) constants. Quote exact lines."
}
```

**Sat 14 Nov 14:10:50 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/g_active.c",
 "prompt": "Find where g_speed is applied to client speed, where the walking speed scale (64 for walk, usercmd forward/right scaling) and 'g_speed' default are, the fall/landing damage and 'pm_landing'/landing view kick. Quote exact lines."
}
```

**Sat 14 Nov 14:10:51 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/bg_pmove.c",
 "prompt": "Extract: PM_Friction function body (how friction and stopspeed apply), PM_Accelerate body, PM_CmdScale, PM_CheckJump (velocity[2] = JUMP_VELOCITY), PM_AirMove, gravity use (pm->ps->gravity), any view bob / bobCycle / landing 'pm_landtime' / 'landChange' code with numbers. Quote exact numeric lines."
}
```

**Sat 14 Nov 14:10:53 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/cgame/cg_view.c",
 "prompt": "Find CG_OffsetFirstPersonView: bob values (cg_bobup, cg_bobpitch, cg_bobroll, cg_bobyaw), landing dip (LAND_DEFLECT_TIME, LAND_RETURN_TIME, fall deflect), kick (kick_time/damage), step smoothing, default FOV (cg_fov default 90), CG_CalcFov and how horizontal FOV is converted with aspect ratio. Quote exact numbers and line text."
}
```

Result:

```
Of the constants you asked for, four are defined in the page:

- **DEFAULT_GRAVITY:** "#define	DEFAULT_GRAVITY		800"
- **DEFAULT_VIEWHEIGHT:** "#define	DEFAULT_VIEWHEIGHT	26"
- **CROUCH_VIEWHEIGHT:** "#define CROUCH_VIEWHEIGHT	12"
- **MINS_Z:** "#define	MINS_Z				-24" (the page defines only the Z minimum)

The page does not define the following:

- **JUMP_VELOCITY:** not present.
- **STEPSIZE:** not present.
- **MAXS:** no value. The only reference is the declaration "vec3_t		mins, maxs;			// bounding box size" inside `pmove_t`.
- **g_speed or any default speed constant:** not present.
```

Result:

```
The pasted excerpt declares the `pm_` variables as `extern` but does not assign them, so **their values are not given here**. The file only shows their declarations and line numbers, counted from the `/*` on line 1 of the excerpt:

| Constant | Line | Declaration | Value |
|---|---|---|---|
| `pm_stopspeed` | 60 | `extern float pm_stopspeed;` | Not in excerpt |
| `pm_duckScale` | 61 | `extern float pm_duckScale;` | Not in excerpt |
| `pm_swimScale` | 62 | `extern float pm_swimScale;` | Not in excerpt |
| `pm_wadeScale` | 63 | `extern float pm_wadeScale;` | Not in excerpt |
| `pm_accelerate` | 65 | `extern float pm_accelerate;` | Not in excerpt |
| `pm_airaccelerate` | 66 | `extern float pm_airaccelerate;` | Not in excerpt |
| `pm_wateraccelerate` | 67 | `extern float pm_wateraccelerate;` | Not in excerpt |
| `pm_flyaccelerate` | 68 | `extern float pm_flyaccelerate;` | Not in excerpt |
| `pm_friction` | 70 | `extern float pm_friction;` | Not in excerpt |
| `pm_waterfriction` | 71 | `extern float pm_waterfriction;` | Not in excerpt |
| `pm_flightfriction` | 72 | `extern float pm_flightfriction;` | Not in excerpt |

The two other constants are defined in the excerpt:

- `JUMP_VELOCITY`: **270** (line 29, `#define JUMP_VELOCITY	270`)
- `STEPSIZE`: **18** (line 27, `#define STEPSIZE		18`)
```

Result:

```
**g_speed applied to client speed** (`ClientThink_real`):

- `client->ps.speed = g_speed.value;` (preceded by the comment `// set speed`)
- `client->ps.speed *= 1.3;` under `if ( client->ps.powerups[PW_HASTE] ) {`
- A MISSIONPACK-only scout branch multiplies by 1.5.

**Not in this excerpt:** the walking speed scale of 64, the usercmd forward/right scaling, the `g_speed` default value, `pm_landing`, and the landing view kick. These live in the pmove code (bg_pmove) and the cvar table (g_main), which aren't included.

**Fall/landing damage** (`ClientEvents`):

- `if ( g_dmflags.integer & DF_NO_FALLING ) {`
- `if ( event == EV_FALL_FAR ) {` then `damage = 10;`, else `damage = 5;`
- `ent->pain_debounce_time = level.time + 200;	// no normal pain sound`
- `G_Damage (ent, NULL, NULL, NULL, NULL, damage, 0, MOD_FALLING);`

The landing event itself is generated elsewhere. This code only consumes `EV_FALL_MEDIUM` and `EV_FALL_FAR`.
```

Result:

```
**Note:** `pm_landtime` and `landChange` do not appear in this source. Landing uses `legsTimer` and `pm_time`, and `TIMER_LAND` and `JUMP_VELOCITY` are defined outside this excerpt.

**PM_Friction**
- Skips speed-scaled drop when `speed < 1` and zeroes only the horizontal velocity: `vel[0] = 0;`
- Ground friction applies only when walking on a non-slick surface and not knocked back: `control = speed < pm_stopspeed ? pm_stopspeed : speed;`
- Ground drop: `drop += control*pm_friction*pml.frametime;` (`pm_friction = 6.0f`)
- Water drop scales with waterlevel: `drop += speed*pm_waterfriction*pm->waterlevel*pml.frametime;`
- Flight and spectator add their own drops with `pm_flightfriction` (3.0f) and `pm_spectatorfriction` (5.0f).

**PM_Accelerate** (active `#if 1` branch)
- `currentspeed = DotProduct (pm->ps->velocity, wishdir);`
- `addspeed = wishspeed - currentspeed;`
- `accelspeed = accel*pml.frametime*wishspeed;`
- Velocity update: `pm->ps->velocity[i] += accelspeed*wishdir[i];`
- Accel constants: `pm_accelerate = 10.0f`, `pm_airaccelerate = 1.0f`, `pm_wateraccelerate = 4.0f`.

**PM_CmdScale**
- `scale = (float)pm->ps->speed * max / ( 127.0 * total );`
- Normalizes diagonal input so movement isn't about √2 faster.

**PM_CheckJump**
- Jump requires `upmove >= 10`.
- `pm->ps->velocity[2] = JUMP_VELOCITY;` (value not in this excerpt)
- Backward jumps are chosen when `pm->cmd.forwardmove < 0`.

**PM_AirMove**
- Calls friction first, then `PM_Accelerate (wishdir, wishspeed, pm_airaccelerate);`
- Scales wish speed with `wishspeed *= scale;`
- Finishes with `PM_StepSlideMove ( qtrue );`. Gravity for airborne movement is not applied in this function.

**Gravity (`pm->ps->gravity`)**
- Water jump: `pm->ps->velocity[2] -= pm->ps->gravity * pml.frametime;`
- Walking, only on slick surfaces or during knockback: `pm->ps->velocity[2] -= pm->ps->gravity * pml.frametime;`
- Landing calculation: `acc = -pm->ps->gravity;`

**Landing (PM_CrashLand / PM_GroundTrace)**
- `pm->ps->legsTimer = TIMER_LAND;`
- `delta = delta*delta * 0.0001;`
- Crouching doubles damage: `delta *= 2;`
- Water reduces it: `delta *= 0.25;` (waist-deep) and `delta *= 0.5;` (knee-deep)
- Ignored below threshold: `if ( delta < 1 ) {`
- Event thresholds: `if ( delta > 60 ) {`, `} else if ( delta > 40 ) {`, `} else if ( delta > 7 ) {`
- Landing lockout in PM_GroundTrace: `if ( pml.previous_velocity[2] < -200 ) {`, then `pm->ps->pm_time = 250;`

**View bob / bobCycle (PM_Footsteps)**
- Ducked: `bobmove = 0.
[... 183 more characters not shown]
```

Result:

```
## CG_OffsetFirstPersonView and Related Code in cg_view.c

**Bob (view bobbing)**
- Vertical bob is capped: `bob = cg.bobfracsin * cg.xyspeed * cg_bobup.value;` followed by `if (bob > 6) { bob = 6; }`, so the maximum is 6 units.
- Pitch bob uses `delta = cg.bobfracsin * cg_bobpitch.value * speed;`, where `speed = cg.xyspeed > 200 ? cg.xyspeed : 200;` sets a minimum of 200.
- Roll bob uses `delta = cg.bobfracsin * cg_bobroll.value * speed;` and flips sign when `cg.bobcycle & 1` is set.
- While ducked, pitch and roll bob are multiplied by 3 (`delta *= 3;`).
- `cg_bobyaw` does not appear in this file.

**Landing dip**
- Descent phase: `f = delta / LAND_DEFLECT_TIME;` then `cg.refdef.vieworg[2] += cg.landChange * f;`
- Return phase: `f = 1.0 - ( delta / LAND_RETURN_TIME );`, applied the same way.
- The numeric values of `LAND_DEFLECT_TIME`, `LAND_RETURN_TIME`, and `cg.landChange` are not in this excerpt.

**Fall kick**
- The fall-kick block is inside `#if 0`, so it is disabled. It used `FALL_TIME` and `cg.fall_value`.

**Kick (weapon and damage)**
- Weapon kick: `VectorAdd (angles, cg.kick_angles, angles);` and `VectorAdd (origin, cg.kick_origin, origin);`. No `kick_time` variable appears in this file.
- Damage kick ramps in over `DAMAGE_DEFLECT_TIME`, then fades over `DAMAGE_RETURN_TIME`, scaled by `cg.v_dmg_pitch` and `cg.v_dmg_roll`. The constants are not shown.
- The damage blend overlay fades with `ent.shaderRGBA[3] = 200 * ( 1.0 - ((float)t / maxTime) );`, where `maxTime = DAMAGE_TIME`.

**Step smoothing**
- `CG_StepOffset` lowers the view after stair climbs: `cg.refdef.vieworg[2] -= cg.stepChange` with the factor `(STEP_TIME - timeDelta) / STEP_TIME`. The `STEP_TIME` value is not in this excerpt.

**Default FOV**
- The `cg_fov` default (stated as 90 in your request) is not defined in this file. The code clamps it: `if ( fov_x < 1 ) {` and `} else if ( fov_x > 160 ) {`.
- Intermission and `DF_FIXED_FOV` both force `fov_x = 90;`.

**CG_CalcFov and aspect handling**
- Horizontal-to-vertical conversion:
  - `x = cg.refdef.width / tan( fov_x / 360 * M_PI );`
  - `fov_y = atan2( cg.refdef.height, x );`
  - `fov_y = fov_y * 360 / M_PI;`
- No aspect-ratio variable is used. The ratio comes from `cg.refdef.width` and `cg.refdef.height`, which `CG_CalcVrect` derives from `vidWidth` and `vidHeight` scaled by `cg_viewsize` (clamped 30 to 100).
- Underwater warp uses `WAVE_AMPLITUDE 1` and `WAVE_FREQUENCY 0.4`, applying `fov_x += v;` and `fov_y -= v;`.
- Zoom interpo
[... 131 more characters not shown]
```

**Sat 14 Nov 14:11:13 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/bg_pmove.c",
 "prompt": "Quote the lines at the top where pm_stopspeed, pm_duckScale, pm_swimScale, pm_wadeScale, pm_accelerate, pm_airaccelerate, pm_wateraccelerate, pm_flyaccelerate, pm_friction, pm_waterfriction, pm_flightfriction are assigned (e.g. 'float pm_stopspeed = 100.0f;'). Also quote the PM_Friction body text, and in PM_WalkMove / PM_CheckJump any speed scaling for crouch (pm_duckScale) and for backward walking."
}
```

**Sat 14 Nov 14:11:14 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]-III-Arena/master/code/game/g_main.c",
 "prompt": "Quote the cvarTable lines for g_speed, g_gravity, g_knockback (exact default strings, e.g. \"g_speed\", \"320\"). "
}
```

**Sat 14 Nov 14:11:14 · Tool call: WebFetch**

```
{
 "url": "https://developer.valvesoftware.com/wiki/Dimensions",
 "prompt": "Quote the Source engine unit conversion (1 unit = ? inches / cm), player hull size, eye height standing and crouching, and any speed/jump statements. Give exact numbers."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:11:15 · Tool call: WebFetch**

```
{
 "url": "https://developer.valvesoftware.com/wiki/Sv_accelerate",
 "prompt": "Quote default values and descriptions for sv_accelerate, and any mention of sv_friction, sv_airaccelerate, sv_stopspeed, sv_gravity, sv_maxspeed, per-game defaults."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:11:17 · Tool call: WebFetch**

```
{
 "url": "https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/UCharacterMovementComponent",
 "prompt": "Find default values stated for MaxWalkSpeed, MaxAcceleration, BrakingDecelerationWalking, GroundFriction, BrakingFrictionFactor, AirControl, AirControlBoostMultiplier, JumpZVelocity, GravityScale, MaxFallSpeed? Quote exact numbers with the property name."
}
```

Result:

````
The `gameCvarTable` entries are:

```
{ &g_speed, "g_speed", "320", 0, 0, qtrue  },
{ &g_gravity, "g_gravity", "800", 0, 0, qtrue  },
{ &g_knockback, "g_knockback", "1000", 0, 0, qtrue  },
```

These default strings are `"320"`, `"800"`, and `"1000"`. The source is [another game] III Arena code, licensed under the GNU GPL.
````

Result:

```
The web page content you provided doesn't include any default values for those properties. It contains only a "Table of Contents" heading, so I can't find MaxWalkSpeed, MaxAcceleration, BrakingDecelerationWalking, GroundFriction, BrakingFrictionFactor, AirControl, AirControlBoostMultiplier, JumpZVelocity, GravityScale, or MaxFallSpeed in it.

If you share the full page text, I can pull out the stated defaults for you.
```

Result:

```
**Variable declarations (top of file):**

- "float	pm_stopspeed = 100.0f;"
- "float	pm_duckScale = 0.25f;"
- "float	pm_swimScale = 0.50f;"
- "float	pm_wadeScale = 0.70f;"
- "float	pm_accelerate = 10.0f;"
- "float	pm_airaccelerate = 1.0f;"
- "float	pm_wateraccelerate = 4.0f;"
- "float	pm_flyaccelerate = 8.0f;"
- "float	pm_friction = 6.0f;"
- "float	pm_waterfriction = 1.0f;"
- "float	pm_flightfriction = 3.0f;"

**PM_Friction body (excerpts):**

- "if ( pm->waterlevel <= 1 ) {"
- "if ( pml.walking && !(pml.groundTrace.surfaceFlags & SURF_SLICK) ) {"
- "control = speed < pm_stopspeed ? pm_stopspeed : speed;"
- "drop += control*pm_friction*pml.frametime;"
- "drop += speed*pm_waterfriction*pm->waterlevel*pml.frametime;"
- "drop += speed*pm_flightfriction*pml.frametime;"

**Crouch speed scaling (PM_WalkMove):**

- "if ( pm->ps->pm_flags & PMF_DUCKED ) {"
- "if ( wishspeed > pm->ps->speed * pm_duckScale ) {"
- "wishspeed = pm->ps->speed * pm_duckScale;"

**Backward movement:**

- PM_CheckJump does not scale speed for backward movement. It only selects the animation and flag: "PM_ForceLegsAnim( LEGS_JUMPB );" and "pm->ps->pm_flags |= PMF_BACKWARDS_JUMP;"
- PM_WalkMove has no backward speed reduction. PMF_BACKWARDS_RUN affects only the leg animation in PM_Footsteps, as in "PM_ContinueLegsAnim( LEGS_BACK );".

**Note:** pm_wadeScale is declared but does not appear in the code shown. The water speed clamp in PM_WalkMove uses pm_swimScale indirectly through its waterScale calculation.
```

**Sat 14 Nov 14:11:27 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/gamemovement.cpp",
 "prompt": "Quote: ConVar definitions with defaults (sv_friction, sv_stopspeed, sv_gravity, sv_accelerate, sv_airaccelerate, sv_maxspeed, sv_stepsize, sv_bounce, sv_maxvelocity, sv_wateraccelerate, sv_waterfriction, sv_noclipspeed, sv_specaccelerate). Also in CheckJumpButton: the jump velocity formula (sqrt(2*800*45) or similar), the 'flGroundFactor', and the code about 'GetFlags & FL_DUCKING' etc. Also any comment on gravity applied half before and half after movement (StartGravity/FinishGravity). Quote exact lines."
}
```

**Sat 14 Nov 14:11:28 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/hl2/hl_gamemovement.cpp",
 "prompt": "Quote anything about sprint speed, walk speed, ladder, jump height, 'sqrt(2 * 800 * 57.0)' or jump height numbers, and ConVars with defaults. Quote exact lines."
}
```

**Sat 14 Nov 14:11:29 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/hl2/hl2_gamerules.cpp",
 "prompt": "Quote any default movement constants, player speed (hl2_normspeed, hl2_sprintspeed, hl2_walkspeed) if present, and ConVar defaults for movement."
}
```

**Sat 14 Nov 14:11:30 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/server/hl2/hl2_player.cpp",
 "prompt": "Quote defines/ConVars for player speeds: hl2_walkspeed, hl2_normspeed, hl2_sprintspeed (values), sprint, suit power, 'HL2_NORM_SPEED', jump height. Exact lines."
}
```

**Sat 14 Nov 14:11:31 · Tool call: WebSearch**

```
{
 "query": "Source engine sv_accelerate 10 sv_friction 4 sv_airaccelerate sv_stopspeed 100 default values Valve Developer Community",
 "mode": "standard"
}
```

Result:

```
The visible part of the page doesn't include any movement constants or the `hl2_normspeed`, `hl2_sprintspeed`, or `hl2_walkspeed` ConVars. The content is also truncated, so they may appear later in the file.

The nearest player-related defaults shown are not movement settings. For example:

- "ConVar	[secret]		( "[secret]", "30", FCVAR_REPLICATED );" (health drop timer, default 30)
- Similar drop-timer ConVars for grenades, also defaulting to 30.

If you share the rest of the file, I can check it for the movement values you asked about.

[WebFetch note: this page's text is 116198 characters long and the answer above covers only characters 0 to 100000; the final 16198 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```

Result:

```
**Walk, normal, and sprint speeds:**
- "ConVar hl2_walkspeed( "hl2_walkspeed", "150", FCVAR_REPLICATED );"
- "ConVar hl2_normspeed( "hl2_normspeed", "190", FCVAR_REPLICATED );"
- "ConVar hl2_sprintspeed( "hl2_sprintspeed", "320", FCVAR_REPLICATED );"
- "#define HL2_NORM_SPEED hl2_normspeed.GetFloat()"

**Sprint toggle:**
- "ConVar sv_stickysprint("sv_stickysprint", "0", FCVAR_ARCHIVE | FCVAR_ARCHIVE_XBOX);"

**Suit power:**
- "#define SUITPOWER_CHARGE_RATE 12.5" (commented as "100 units in 8 seconds")
- "CSuitPowerDevice SuitDeviceSprint( bits_SUIT_DEVICE_SPRINT, 12.5f );" (non-HL2MP build)

**Jump height:** The provided content doesn't define a jump height setting. The closest match is the autojump hack in `PreThink`, which adds a fixed upward velocity: "vecNewVelocity.z += 250;". It is gated by "ConVar sv_autojump( "sv_autojump", "0" );".

The page content was truncated, so later sections may contain additional definitions.

[WebFetch note: this page's text is 110826 characters long and the answer above covers only characters 0 to 100000; the final 10826 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```

Result:

```
The provided source doesn't mention sprint speed, walk speed, or `sqrt(2 * 800 * 57.0)`. It does contain ladder speed, jump-related values, and ConVars with defaults.

**ConVars with defaults** (descriptions truncated):

- `static ConVar sv_autoladderdismount( "sv_autoladderdismount", "1", FCVAR_REPLICATED, ...`
- `static ConVar sv_ladderautomountdot( "sv_ladderautomountdot", "0.4", FCVAR_REPLICATED, ...`
- `static ConVar sv_ladder_useonly( "sv_ladder_useonly", "0", FCVAR_REPLICATED, ...`

**Ladder speed:**

- `#define USE_DISMOUNT_SPEED 100`
- `float speed = this->MaxSpeed();`
- `mv->m_vecVelocity = MAX_CLIMB_SPEED * factor * ladderUp;`
- `float ladderUnitsPerTick = ( MAX_CLIMB_SPEED * gpGlobals->interval_per_tick );`

**Jump-related values** (no explicit jump height constant appears in this code):

- `VectorScale( jumpDir, MAX_CLIMB_SPEED, mv->m_vecVelocity );`
- `mv->m_vecVelocity.z = mv->m_vecVelocity.z + 50;`

**Max speed (the basis for walk/sprint speed here):**

- `return Min( mv->m_flClientMaxSpeed, mv->m_flMaxSpeed );`
- `return mv->m_flMaxSpeed;`
```

Result:

```
Web search results for query: "Source engine sv_accelerate 10 sv_friction 4 sv_airaccelerate sv_stopspeed 100 default values Valve Developer Community"

Links: [{"title":"Sv friction","url":"https://developer.valvesoftware.com/wiki/Sv_friction"},{"title":"sv airaccelerate","url":"https://csdb.gg/commands/sv_airaccelerate"},{"title":"github.com%2Fmphe%2Ftf2 classicmovement","url":"https://awesome.ecosyste.ms/projects/github.com%2Fmphe%2Ftf2-classicmovement"},{"title":"File: sv_phys.c","url":"https://sources.debian.org/src/ezquake/2.2%2Bgit20150324-1/sv_phys.c"},{"title":"w.atwiki.jp","url":"https://w.atwiki.jp/nmrih/pages/30.html"},{"title":"sv_airaccelerate Command","url":"https://csdb.gg/commands/server/sv_airaccelerate"},{"title":"sv airdecelerate","url":"https://docs.momentum-mod.org/var/sv_airdecelerate/"},{"title":"CS2 & CS:GO sv_airaccelerate Command","url":"https://totalcsgo.com/commands/svairaccelerate"},{"title":"sv_accelerate Command","url":"https://csdb.gg/commands/server/sv_accelerate"},{"title":"Makes the player jump to the exact same height every jump. The height if affected by","url":"https://docs.momentum-mod.org/tags/player/page/4"},{"title":"CS2 & CS:GO sv_accelerate Command","url":"https://totalcsgo.com/commands/svaccelerate"},{"title":"sv_friction Command","url":"https://csdb.gg/commands/server/sv_friction"},{"title":"Last server records","url":"https://kz-rush.ru/page/strafe-physics"},{"title":"remilia.zdoom.org","url":"https://remilia.zdoom.org/wiki/Friction"},{"title":"CS2 & CS:GO sv_friction Command","url":"https://totalcsgo.com/commands/svfriction"},{"title":"QuakeForge  [ip]-815cf","url":"https://[another game].sourceforge.io/doxygen/structmovevars__t.html"},{"title":"CS2 & CS:GO sv_stopspeed Command","url":"https://totalcsgo.com/commands/svstopspeed"},{"title":"CS2 & CS:GO sv_stopspeed Command","url":"https://totalcsgo.com/command/svstopspeed"}]

The search didn't return the Valve Developer Community page for these cvars, but it did turn up defaults from several sources. They differ by game, so the answer depends on which Source-based title you mean.

- **sv_friction 4:** The Valve Developer Community wiki gives 4 for [another game] and [another game]: Source, and 5.2 for [another game]: Global Offensive. By default, it is set to sv_friction 4 ([another game] [another game],[another game]: Source [another game]: Source) and sv_friction 5.2 ([another game]: Global Offensive [another game]: Global Offensive).
- **sv_accelerate 10 and s
[... 1194 more characters not shown]
```

Result:

```
The visible part of the page doesn't include the `sv_*` ConVar definitions you asked about (sv_friction, sv_stopspeed, sv_gravity, sv_accelerate, and the others). The code only references them, so their defaults aren't shown. The text is also truncated, so they may appear later.

**ConVars defined in the visible text**

- "ConVar xc_uncrouch_on_jump( "xc_uncrouch_on_jump", "1", FCVAR_ARCHIVE, "Uncrouch when jump occurs" );" (HL2 builds only)
- "static ConVar diffcheck( "diffcheck", "0", FCVAR_REPLICATED );"
- sv_ladder_dampen defaults to 0.2 and sv_ladder_angle defaults to -0.707. Both are defined only for CSTRIKE_DLL builds.

**Jump velocity**

- Base factor: "float flGroundFactor = 1.0f;", later overwritten by "flGroundFactor = player->m_pSurfaceData->game.jumpFactor;"
- HL2 path: "Assert( GetCurrentGravity() == 600.0f );" followed by "flMul = 160.0f;	// approx. 21 units."
- Other builds: "Assert( GetCurrentGravity() == 800.0f );" followed by "flMul = 268.3281572999747f;"
- When the optimization flag is off, the code computes it instead: "flMul = sqrt(2 * GetCurrentGravity() * GAMEMOVEMENT_JUMP_HEIGHT);"
- Applied as: "mv->m_vecVelocity[2] = flGroundFactor * flMul;  // 2 * gravity * height"
- The derivation comment reads "// v = sqrt( g * 2.0 * 45 )", which describes a jump height of about 45 units.

**Ducking checks**

- "if ( player->m_Local.m_bDucking && (  player->GetFlags() & FL_DUCKING ) )" with the comment "// Cannot jump will in the unduck transition."
- The ducked branch sets the velocity directly, while the standing branch adds to it. The check is "if ( (  player->m_Local.m_bDucking ) || (  player->GetFlags() & FL_DUCKING ) )".

**Gravity split**

- StartGravity applies half a step before movement: "mv->m_vecVelocity[2] -= (ent_gravity * GetCurrentGravity() * 0.5 * gpGlobals->frametime );", preceded by the comment "// yes, this 0.5 looks wrong, but it's not."
- FinishGravity applies the other half after movement: "mv->m_vecVelocity[2] -= (ent_gravity * GetCurrentGravity() * gpGlobals->frametime * 0.5);", preceded by the comment "// Get the correct velocity for the end of the dt ".

[WebFetch note: this page's text is 139215 characters long and the answer above covers only characters 0 to 100000; the final 39215 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```

**Sat 14 Nov 14:11:47 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/shared/movevars_shared.cpp",
 "prompt": "Quote every ConVar/MovementVars default: sv_gravity, sv_stopspeed, sv_maxspeed, sv_accelerate, sv_airaccelerate, sv_wateraccelerate, sv_friction, sv_waterfriction, sv_bounce, sv_stepsize, sv_maxvelocity. Exact definition lines."
}
```

**Sat 14 Nov 14:11:48 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]/master/WinQuake/view.c",
 "prompt": "Quote cvar definitions with defaults: cl_rollspeed, cl_rollangle, cl_bob, cl_bobcycle, cl_bobup, v_kicktime, v_kickroll, v_kickpitch, v_iyaw_cycle etc, scr_fov / fov, v_idlescale. Quote V_CalcBob function and V_CalcRoll function bodies (exact numbers), landing/ 'V_CalcViewRoll' and the view kick logic."
}
```

**Sat 14 Nov 14:11:49 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]/master/WinQuake/sv_phys.c",
 "prompt": "Quote sv_gravity, sv_friction, sv_stopspeed, sv_maxvelocity cvar definitions and defaults; SV_AddGravity; and anything on friction formula. Exact lines."
}
```

**Sat 14 Nov 14:11:51 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]/master/WinQuake/sv_user.c",
 "prompt": "Quote sv_edgefriction, sv_accelerate, sv_idealpitchscale, SV_UserFriction, SV_Accelerate, SV_AirAccelerate (note the 30 wishspeed cap), SV_WaterJump, jump velocity (velocity[2] += 270), and forward/side speed scaling. Exact lines and numbers."
}
```

**Sat 14 Nov 14:11:51 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/id-Software/[another game]/master/WinQuake/host.c",
 "prompt": "Quote sv_maxspeed, host_framerate, sys_ticrate, and sv_aim cvar defaults; maxvelocity; and the default player speed (sv_maxspeed 320). Exact lines."
}
```

Result:

```
The provided source doesn't include `sv_maxspeed`, `sv_aim`, `maxvelocity`, or a default player speed of 320. Those values would be defined elsewhere in the codebase.

The two cvar defaults that do appear in this file are:

`cvar_t	host_framerate = {"host_framerate","0"};	// set for slow motion`

`cvar_t	sys_ticrate = {"sys_ticrate","0.05"};`
```

Result:

````
**cvar definitions and defaults** (sv_phys.c):

```c
cvar_t	sv_friction = {"sv_friction","4",false,true};
cvar_t	sv_stopspeed = {"sv_stopspeed","100"};
cvar_t	sv_gravity = {"sv_gravity","800",false,true};
cvar_t	sv_maxvelocity = {"sv_maxvelocity","2000"};
```

**SV_AddGravity** (non-QUAKE2 branch):

```c
	val = GetEdictFieldValue(ent, "gravity");
	if (val && val->_float)
		ent_gravity = val->_float;
	else
		ent_gravity = 1.0;
#endif
	ent->v.velocity[2] -= ent_gravity * sv_gravity.value * host_frametime;
```

**Friction** (in the QUAKE2 branch of SV_Physics_Step):

```c
					friction = sv_friction.value;

					control = speed < sv_stopspeed.value ? sv_stopspeed.value : speed;
					newspeed = speed - host_frametime*control*friction;

					if (newspeed < 0)
						newspeed = 0;
					newspeed /= speed;

					vel[0] = vel[0] * newspeed;
					vel[1] = vel[1] * newspeed;
```

The non-QUAKE2 version of SV_Physics_Step does not apply this friction code. The source is Copyright (C) 1996-1997 Id Software, Inc., licensed under the GNU GPL v2 or later.
````

Result:

```
**sv_edgefriction** (declared as `cvar_t sv_edgefriction = {"edgefriction", "2"};`): applied when the leading edge is over a dropoff: `"friction = sv_friction.value*sv_edgefriction.value;"`

**sv_accelerate** (declared as `cvar_t sv_accelerate = {"sv_accelerate", "10"};`): used in ground and water acceleration: `"accelspeed = sv_accelerate.value*host_frametime*wishspeed;"`

**sv_idealpitchscale** (declared as `cvar_t sv_idealpitchscale = {"sv_idealpitchscale","0.8"};`): used in `SV_SetIdealPitch`: `"sv_player->v.idealpitch = -dir * sv_idealpitchscale.value;"`

**SV_UserFriction**: `"newspeed = speed - host_frametime*control*friction;"`

**SV_Accelerate**: `"accelspeed = sv_accelerate.value*host_frametime*wishspeed;"`

**SV_AirAccelerate**: The wish speed cap is `"if (wishspd > 30)"` followed by `"wishspd = 30;"`. The acceleration line is `"accelspeed = sv_accelerate.value*wishspeed * host_frametime;"`

**SV_WaterJump**: The jump-exit logic sets horizontal velocity from `movedir`: `"sv_player->v.velocity[0] = sv_player->v.movedir[0];"` and `"sv_player->v.velocity[1] = sv_player->v.movedir[1];"`

**Jump velocity (velocity[2] += 270)**: Not in the provided content.

**Forward/side speed scaling**: Not given as a constant. `SV_AirMove` computes `"wishvel[i] = forward[i]*fmove + right[i]*smove;"`, where fmove and smove come directly from `cmd.forwardmove` and `cmd.sidemove`. The only explicit scaling is the `sv_maxspeed` clamp (`"if (wishspeed > sv_maxspeed.value)"`, with sv_maxspeed = 320) and, in water, `"wishspeed *= 0.7;"`.
```

Result:

```
**Note:** The source doesn't define `scr_fov` or `fov`. It also has no landing-specific logic. The closest match is the stair-step smoothing in `V_CalcRefdef`, which runs when `cl.onground` is true.

**Cvar defaults (from the source)**

- `cl_rollspeed`: "200"
- `cl_rollangle`: "2.0"
- `cl_bob`: "0.02"
- `cl_bobcycle`: "0.6"
- `cl_bobup`: "0.5"
- `v_kicktime`: "0.5"
- `v_kickroll`: "0.6"
- `v_kickpitch`: "0.6"
- `v_iyaw_cycle`: "2"
- `v_iroll_cycle`: "0.5"
- `v_ipitch_cycle`: "1"
- `v_iyaw_level`: "0.3"
- `v_iroll_level`: "0.1"
- `v_ipitch_level`: "0.3"
- `v_idlescale`: "0"

**V_CalcBob (key lines)**

- The cycle is computed from `cl.time` modulo `cl_bobcycle`, then normalized: "cycle /= cl_bobcycle.value;"
- The cycle is split at `cl_bobup`: "cycle = M_PI * cycle / cl_bobup.value;" on the rising part, and "cycle = M_PI + M_PI*(cycle-cl_bobup.value)/(1.0 - cl_bobup.value);" on the falling part.
- Bob scales with horizontal speed: "bob = sqrt(cl.velocity[0]*cl.velocity[0] + cl.velocity[1]*cl.velocity[1]) * cl_bob.value;"
- The waveform blends 30% flat with 70% sine: "bob = bob*0.3 + bob*0.7*sin(cycle);"
- The result is clamped to between -7 and 4.

**V_CalcRoll (key lines)**

- Lateral velocity is taken from the right vector: "side = DotProduct (velocity, right);"
- The sign is kept and the magnitude is made absolute: "side = fabs(side);"
- Below the threshold, roll scales linearly: "side = side * value / cl_rollspeed.value;"
- Above it, roll is capped: "side = value;"
- The sign is restored on return: "return side*sign;"

**V_CalcViewRoll and view kick**

- Movement roll is added first: "side = V_CalcRoll (cl_entities[cl.viewentity].angles, cl.velocity);"
- While a kick is active, roll and pitch are scaled by remaining kick time over `v_kicktime`: "r_refdef.viewangles[ROLL] += v_dmg_time/v_kicktime.value*v_dmg_roll;"
- The kick timer then decreases each frame: "v_dmg_time -= host_frametime;"
- Dead players get a fixed roll of 80.
- `V_ParseDamage` sets the kick. It computes `count` from armor and blood (minimum 10), then projects the damage direction onto the player's right and forward vectors. Each result is multiplied by `count` and its kick cvar (`v_kickroll` or `v_kickpitch`), and the timer is set from `v_kicktime`.
```

Result:

```
**Defaults (from the source):**

- **sv_gravity:** `"600"` for HL2 builds, `"800"` otherwise (via `DEFAULT_GRAVITY_STRING`)
  `ConVar	sv_gravity		( "sv_gravity", DEFAULT_GRAVITY_STRING, FCVAR_NOTIFY | FCVAR_REPLICATED, "World gravity." );`

- **sv_stopspeed:** `"100"`
  `ConVar	sv_stopspeed	( "sv_stopspeed","100", FCVAR_NOTIFY | FCVAR_REPLICATED, "Minimum stopping speed when on ground." );`

- **sv_maxspeed:** `"320"`
  `ConVar	sv_maxspeed		( "sv_maxspeed", "320", FCVAR_NOTIFY | FCVAR_REPLICATED);`

- **sv_accelerate:** `"10"` (Xbox build: `"7"`)
  `ConVar	sv_accelerate	( "sv_accelerate", "10", FCVAR_NOTIFY | FCVAR_REPLICATED);`

- **sv_airaccelerate:** `"10"`
  `ConVar	sv_airaccelerate(  "sv_airaccelerate", "10", FCVAR_NOTIFY | FCVAR_REPLICATED );`

- **sv_wateraccelerate:** `"10"`
  `ConVar	sv_wateraccelerate(  "sv_wateraccelerate", "10", FCVAR_NOTIFY | FCVAR_REPLICATED );`

- **sv_friction:** `"4"`
  `ConVar	sv_friction		( "sv_friction","4", FCVAR_NOTIFY | FCVAR_REPLICATED, "World friction." );`

- **sv_waterfriction:** `"1"`
  `ConVar	sv_waterfriction(  "sv_waterfriction", "1", FCVAR_NOTIFY | FCVAR_REPLICATED );`

- **sv_bounce:** `"0"` (help text truncated to fit the 125-character quote limit)
  `ConVar	sv_bounce		( "sv_bounce","0", FCVAR_NOTIFY | FCVAR_REPLICATED, "Bounce multiplier ..." );`

- **sv_stepsize:** `"18"`
  `ConVar	sv_stepsize		( "sv_stepsize","18", FCVAR_NOTIFY | FCVAR_REPLICATED );`

- **sv_maxvelocity:** `"3500"` (help text truncated to fit the 125-character quote limit)
  `ConVar	sv_maxvelocity	( "sv_maxvelocity","3500", FCVAR_REPLICATED, "Maximum speed ..." );`
```

### Sat 14 Nov 14:12:06 · Agent (claude-sonnet-5-5)

[another game] 1, [another game] 3 and Source SDK constants are confirmed from the public source files. VDC (Valve wiki) returned 403. Next I'm fetching Unreal, [another game], [another game], [another game], FOV and accessibility pages.

**Sat 14 Nov 14:12:07 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/NoelFB/[another game]/master/Source/Player/Player.cs",
 "prompt": "Quote exact constants: JumpGraceTime, JumpSpeed, VarJumpTime, MaxFall, Gravity, HalfGravThreshold, MaxRun, RunAccel, RunReduce, AirMult, the jumpGraceTimer logic, and the jump button buffer (Input.Jump.Pressed / Buffer time, e.g. Input.Jump.BufferTime). Exact lines with their values."
}
```

**Sat 14 Nov 14:12:08 · Tool call: WebSearch**

```
{
 "query": "[another game] Player.cs JumpGraceTime 0.1f VarJumpTime 0.2f github NoelFB [another game] source",
 "mode": "standard"
}
```

**Sat 14 Nov 14:12:09 · Tool call: WebSearch**

```
{
 "query": "Unreal Engine CharacterMovementComponent defaults MaxWalkSpeed 600 MaxAcceleration 2048 GroundFriction 8 JumpZVelocity 420 AirControl 0.05 BrakingDecelerationWalking 2048",
 "mode": "standard"
}
```

**Sat 14 Nov 14:12:09 · Tool call: WebSearch**

```
{
 "query": "GDC 2018 Embracing Push Forward Combat in [another game] Jason O'Donnell player speed movement",
 "mode": "standard"
}
```

**Sat 14 Nov 14:12:09 · Tool call: WebSearch**

```
{
 "query": "Maddy Thorson [another game] and TowerFall physics coyote time jump buffer frames",
 "mode": "standard"
}
```

Result:

```
Web search results for query: "[another game] Player.cs JumpGraceTime 0.1f VarJumpTime 0.2f github NoelFB [another game] source"

Links: [{"title":"I think we won't ever see the full source of this game but they posted this recently:","url":"https://itch.io/post/372783"},{"title":"[another game]: open-source Player class","url":"https://notapixel.itch.io/platformer-test/devlog/729893/[another game]-open-source-player-class"},{"title":"[another game]’s Movement Code Available on GitHub","url":"https://80.lv/articles/[another game]s-movement-code-available-on-github/?amp=1"},{"title":"[another game]s movement code available on github","url":"https://80.lv/articles/[another game]s-movement-code-available-on-github"},{"title":"tcrf.net","url":"https://tcrf.net/[another game]"},{"title":"[another game] Wiki","url":"https://[another game]game.fandom.com/wiki/File:Wave_hyper.gif"},{"title":"Windows [BUG] Coyote Time not working in JunimoKart because of a bug","url":"https://forums.stardewvalley.net/threads/bug-coyote-time-not-working-in-junimokart-because-of-a-bug.20671"},{"title":"itch.io","url":"https://gmtk.itch.io/platformer-toolkit/comments?before=73"},{"title":"See all glossary terms","url":"https://school.gdquest.com/glossary/coyote_time"},{"title":"wildvisualizer.com","url":"https://wildvisualizer.com/conversation/lmsyschat/2bee43dcbfd449a2a784e67a9c376ebd"},{"title":"gmtk.itch.io","url":"https://gmtk.itch.io/platformer-toolkit/comments?after=23"},{"title":"Screen shot courtesy of Matt Makes Games","url":"https://broadly.vice.com/en/article/88a755/how-[another game]-found-success-in-embracing-speedrunners-who-broke-the-game"},{"title":"[another game] & Forgiveness","url":"https://maddymakesgames.com/articles/[another game]_and_forgiveness/"},{"title":"r/gamedev Jul 10 '20","url":"https://redlib.hbubli.cc/r/gamedev/comments/horm1a/ive_started_making_a_teaching_aid_for_people"},{"title":"• [AFK] [another game]@merv.news","url":"https://lemmy.nekusoul.de/post/5890"},{"title":"daytenrose.substack.com","url":"https://daytenrose.substack.com/p/21-coyote-time/comments"},{"title":"[another game] style asymmetric jump godot 4","url":"https://www.vinzius.com/snippets/[another game]-style-asymmetric-jump-godot-4/"}]

The search found the official repository link and context, but not the specific constants you asked about.

- **Repository:** A forum post links to the file at https://github.com/NoelFB/[another game]/blob/master/Source/Player.cs. That is the official NoelFB [another game] repo for Player.cs.
- **Background:** Matt Thorson and Noel Berry posted their 5400-line Player class (C#) from Celest
[... 616 more characters not shown]
```

Result:

````
The page is a truncated excerpt of [another game]'s `Player` class. Here are the requested constants and logic as they appear in the excerpt:

**Constants**
- `private const float JumpGraceTime = 0.1f;`
- `private const float JumpSpeed = -105f;`
- `private const float VarJumpTime = .2f;`
- `public const float MaxFall = 160f;`
- `private const float Gravity = 900f;`
- `private const float HalfGravThreshold = 40f;`
- `public const float MaxRun = 90f;`
- `public const float RunAccel = 1000f;`
- `private const float RunReduce = 400f;`
- `private const float AirMult = .65f;`

**Jump grace timer logic** (in `Update()`, under `//Jump Grace`):
```
if (onGround)
{
    dreamJump = false;
    jumpGraceTimer = JumpGraceTime;
}
else if (jumpGraceTimer > 0)
    jumpGraceTimer -= Engine.DeltaTime;
```

**Jump button buffer:** The excerpt does not include a `BufferTime` value or the `Input.Jump` class definition. It only shows that `Jump()`, `SuperJump()`, `WallJump()`, and `ClimbJump()` call `Input.Jump.ConsumeBuffer();`, which consumes the buffered press. The buffer duration is not in the provided content.

Also, `Gravity`, `HalfGravThreshold`, `RunReduce`, and `AirMult` are declared here, but their usage is in the truncated section (the `NormalUpdate` physics), so I can't confirm how they're applied.

[WebFetch note: this page's text is 186844 characters long and the answer above covers only characters 0 to 100000; the final 86844 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
````

Result:

```
Web search results for query: "GDC 2018 Embracing Push Forward Combat in [another game] Jason O'Donnell player speed movement"

Links: [{"title":"Embracing Push Forward Combat in","url":"https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in"},{"title":"GDC is part of the Informa Tech Division of Informa PLC","url":"https://gdconf.com/news/see-[another game]-devs-break-push-forward-combat-design-gdc-2018"},{"title":"GDC Vault is part of the Informa Tech Division of Informa PLC","url":"https://gdcvault.com/play/1024940/contactUs"},{"title":"www.doomworld.com","url":"https://www.doomworld.com/forum/post/1863462"},{"title":"habr.com","url":"https://habr.com/en/articles/419537"},{"title":"See [another game] devs break down its 'push forward' combat design at GDC 2018","url":"https://www.jikguard.com/news/see-[another game]-devs-break-down-its-push-forward-combat-design-at-gdc-2018"},{"title":"game.watch.impress.co.jp","url":"https://game.watch.impress.co.jp/docs/news/1113403.html"},{"title":"cyber demons the ai of [another game]","url":"https://80.lv/articles/cyber-demons-the-ai-of-[another game]"},{"title":"cyber demons the ai of [another game] 2016","url":"https://www.gamedeveloper.com/design/cyber-demons-the-ai-of-[another game]-2016-"},{"title":"embracing push forward combat in [another game]","url":"https://old.fbpe.org/embracing-push-forward-combat-in-[another game].html"},{"title":"[another game] 2016 official be3 showcase presentation","url":"https://old.fbpe.org/[another game]-2016-official-be3-showcase-presentation.html"},{"title":"Game Developers Conference (GDC) is part of the Informa Tech Division of Informa PLC","url":"https://gdconf.com/news/speaker-qa-kurt-loudy-jake-campbell-break-combat-philosophy-[another game]"},{"title":"Video: The combat design of [another game]","url":"https://www.jikguard.com/news/video-the-combat-design-of-[another game]"},{"title":"How [another game]'s Push Forward Design Cured my Hoarder Syndrome","url":"https://www.gamedeveloper.com/design/how-[another game]-s-push-forward-design-cured-my-hoarder-syndrome"},{"title":"Pushing “Push Forward” Combat With Gameplay","url":"https://game-wisdom.com/?p=27137"},{"title":"How [another game] Cured My Hoarder Syndrome In Videogames","url":"https://game-wisdom.com/critical/[another game]-cured-hoarder-syndrome"},{"title":"The Brutal Gameplay Escalation of ‘[another game] Eternal’","url":"https://www.fandom.com/articles/[another game]-eternal-weapons-gameplay-escalation"},{"title":"pushing push forward combat with gameplay","url":"https://www.gamedeveloper.com/game-platforms/pushing-push-forward-combat-with-gameplay"}]

I found no source naming Jason O'Donnell as a presente
[... 970 more characters not shown]
```

Result:

```
Web search results for query: "Unreal Engine CharacterMovementComponent defaults MaxWalkSpeed 600 MaxAcceleration 2048 GroundFriction 8 JumpZVelocity 420 AirControl 0.05 BrakingDecelerationWalking 2048"

Links: [{"title":"dev.epicgames.com","url":"https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/CharacterMovementComponent"},{"title":"docs.unrealengine.com","url":"https://docs.unrealengine.com/4.26/en-US/PythonAPI/class/CharacterMovementComponent.html"},{"title":"dev.epicgames.com","url":"https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/CharacterMovementComponent.html"},{"title":"dev.epicgames.com","url":"https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/ArchVisCharMovementComponent"},{"title":"unrealengine.com","url":"https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/ArchVisCharMovementComponent.html"},{"title":"unrealengine.com","url":"https://answers.unrealengine.com/questions/814178/view.html"},{"title":"Where is max walk speed stored? (UE5)","url":"https://forums.unrealengine.com/t/where-is-max-walk-speed-stored-ue5/262981"},{"title":"docs.unrealengine.com","url":"https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/CharacterMovementComponent.html"},{"title":"docs.unrealengine.com","url":"https://docs.unrealengine.com/PythonAPI/class/CharacterMovementComponent.html"},{"title":"answers.unrealengine.com","url":"https://answers.unrealengine.com/questions/187524/view.html"},{"title":"UE5 Character Movement Basics: Speed, Jumping, and Gravity in the Character Movement Component","url":"https://uhiyama-lab.com/en/notes/ue/character-movement-component-guide/"},{"title":"docs.unrealengine.com","url":"https://docs.unrealengine.com/4.26/en-US/API/Runtime/Engine/GameFramework/UCharacterMovementComponent/"},{"title":"motion attribute set","url":"https://motioncore.pages.dev/components/motion-attribute-set"},{"title":"answers.unrealengine.com","url":"https://answers.unrealengine.com/questions/555437/view.html"},{"title":"UE 11483","url":"https://issues.unrealengine.com/issue/UE-11483"},{"title":"realdocs.pages.dev","url":"https://realdocs.pages.dev/api/UCharacterMovementComponent.MaxWalkSpeed"},{"title":"Character Movement Component doesn't update in Blueprint component panel","url":"https://answers.unrealengine.com/questions/37930/view.html"},{"title":"🎮 Phaser Game Dev Bundle — 10 complete games with full TypeScript source code.Get it for $19 →","url":"https://generalistpr
[... 1552 more characters not shown]
```

Result:

```
Web search results for query: "Maddy Thorson [another game] and TowerFall physics coyote time jump buffer frames"

Links: [{"title":"Global Sites","url":"https://automaton-media.com/articles/newsjp/20200315-116902/"},{"title":"www.gamespot.com","url":"https://www.gamespot.com/articles/[another game]-dev-explains-how-they-made-their-game-feel/1100-6474775/"},{"title":"20200317 [another game] action feel things","url":"https://gigazine.net/news/20200317-[another game]-action-feel-things"},{"title":"Developer of super-difficult & high-speed masterpiece 2D action game '[another game]' explains 'points about action'","url":"https://wbgsv0a.gigazine.net/gsc_news/en/20200317-[another game]-action-feel-things"},{"title":"Developer of super-difficult & high-speed masterpiece 2D action game '[another game]' explains 'points about action'","url":"https://gigazine.net/gsc_news/en/20200317-[another game]-action-feel-things"},{"title":"[another game] & Forgiveness","url":"https://maddymakesgames.com/articles/[another game]_and_forgiveness/index.html"},{"title":"[another game] & Forgiveness","url":"https://maddymakesgames.com/articles/[another game]_and_forgiveness/"},{"title":"My Authors","url":"https://threadreaderapp.com/thread/1238338574220546049.html"},{"title":"[another game] Wiki","url":"https://[another game]game.fandom.com/wiki/File:Wave_hyper.gif"},{"title":"• [AFK] [another game]@merv.news","url":"https://lemmy.nekusoul.de/post/5890"},{"title":"coyote time input buffering","url":"https://gamejuice.pages.dev/articles/coyote-time-input-buffering"},{"title":"itch.io","url":"https://itch.io/post/3904240"},{"title":"Developers have been subtly cheating to help us win","url":"https://blizzardwatch.com/2020/03/13/[another game]-developer-game-feel/"},{"title":"Coyote Time: What Games Can Teach Us About Forgiveness in Learning  - The Teaching Innovation Blog","url":"https://hn.jakechampion.name/reader/https://blogs.bsu.edu/teaching-innovation/2023/11/15/coyote-time-games-teach-forgiveness-learning"},{"title":"[another game] developer shares the tricks that make tough platforming feel fair","url":"https://rockpapershotgun25.pages.dev/posts/[another game]-developer-shares-the-tricks-that-make-tough-platforming-feel-fair"},{"title":"tasvideos.org","url":"https://tasvideos.org/6555S"},{"title":"Guide to implementing 2D platformers (2012)","url":"https://hn.nuxtjs.org/item/31450218"},{"title":"nagmay.itch.io","url":"https://nagmay.itch.io/a-cat/comments"}]

The search turned up good detail on [another game]'s coyote time and jump buffering, but nothing on TowerFall and no exact jump-buffer frame count for
[... 1474 more characters not shown]
```

**Sat 14 Nov 14:12:23 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/NoelFB/[another game]/master/Source/Input.cs",
 "prompt": "Quote the lines where Jump (VirtualButton) is created with its buffer time (e.g. new VirtualButton(..., 0.08f)), Dash, Grab, and the constant for buffer time. Exact lines."
}
```

**Sat 14 Nov 14:12:24 · Tool call: WebFetch**

```
{
 "url": "https://maddymakesgames.com/articles/[another game]_and_forgiveness/",
 "prompt": "Quote exactly what Maddy Thorson says about coyote time and jump buffering: frame counts, durations, and any other forgiveness values (e.g. half-gravity jump peak, wall jump). Include the author and date."
}
```

Result:

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:12:25 · Tool call: WebFetch**

```
{
 "url": "https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/CharacterMovementComponent",
 "prompt": "Quote the descriptions and any default values for: max_walk_speed, max_acceleration, braking_deceleration_walking, ground_friction, braking_friction_factor, air_control, air_control_boost_multiplier, jump_z_velocity, gravity_scale, braking_friction. Exact quoting with numbers if stated."
}
```

**Sat 14 Nov 14:12:26 · Tool call: WebFetch**

```
{
 "url": "https://uhiyama-lab.com/en/notes/ue/character-movement-component-guide/",
 "prompt": "Quote the default values stated for MaxWalkSpeed, MaxAcceleration, BrakingDecelerationWalking, GroundFriction, AirControl, JumpZVelocity, GravityScale, MaxStepHeight; say if the page claims they are defaults."
}
```

**Sat 14 Nov 14:12:26 · Tool call: WebSearch**

```
{
 "query": "[another game] 2 movement speed units per second run sprint wallrun slide speed Respawn",
 "mode": "standard"
}
```

Result:

```
The page gives no frame counts or exact durations for coyote time or jump buffering. It describes them only as "a short time." Maddy Thorson is the author, but the page shows no publication date.

**Coyote time:**
"You can still jump for a short time after leaving a ledge."

**Jump buffering:**
"If you press and hold the jump button a short time before landing, you will jump on the exact frame that you land."

**Other forgiveness values:**
- **Halved-gravity jump peak:** "the top of your jump has half gravity applied." The article says this gives the player more time to adjust for landing.
- **Wall jump:** "You can actually wall jump 2 pixels from a wall." The article says this is a quarter of a tile in a 320x180 game.
- **Super wall jump:** "I think it's 5 pixels, which is more than half a tile!" (The article's own wording has a curly apostrophe; I've rendered it straight here.)
```

Result:

```
**Descriptions and defaults** (none are stated on the page except where noted)

- **max_walk_speed**: "The maximum ground speed when walking. Also determines maximum lateral speed when falling." Default: not stated.
- **max_acceleration**: "Max Acceleration (rate of change of velocity)". Default: not stated.
- **braking_deceleration_walking**: "Deceleration when walking and not applying acceleration." Default: not stated.
- **ground_friction**: "Setting that affects movement control. Higher values allow faster changes in direction." Default: not stated.
- **braking_friction_factor**: "Factor used to multiply actual value of friction used when braking." Default: the page says "This is 2 by default for historical reasons, a value of 1 gives the true drag equation."
- **air_control**: "When falling, amount of lateral movement control available to the character." Default: not stated.
- **air_control_boost_multiplier**: "When falling, multiplier applied to AirControl when lateral velocity is less than AirControlBoostVelocityThreshold." Default: not stated.
- **jump_z_velocity**: "Initial velocity (instantaneous vertical acceleration) when jumping." Default: not stated.
- **gravity_scale**: "Custom gravity scale. Gravity is multiplied by this amount for the character." Default: not stated.
- **braking_friction**: "Friction (drag) coefficient applied when braking (whenever Acceleration = 0, or if character is exceeding max speed)". Default: not stated.

[WebFetch note: this page's text is 141717 characters long and the answer above covers only characters 0 to 100000; the final 41717 were not read — to read on, call WebFetch again with the same url and offset: 100000.]
```

Result:

```
The page gives values for seven of the eight properties, but none are presented as Unreal Engine defaults. For the first seven, the page lists the values in a "Standardize the starting point for comparison" table and states:

"They are values for this comparison, not the template's defaults."

| Property | Value stated on the page |
|---|---|
| MaxWalkSpeed (Max Walk Speed) | 500 |
| MaxAcceleration (Max Acceleration) | 2048 |
| BrakingDecelerationWalking (Braking Deceleration Walking) | 2000 |
| GroundFriction (Ground Friction) | 8 |
| AirControl (Air Control) | 0.2 |
| JumpZVelocity (Jump Z Velocity) | 700 |
| GravityScale (Gravity Scale) | 1 |
| MaxStepHeight (Max Step Height) | No value given |

The page mentions Max Step Height only as the step height a character can climb, with no number attached.
```

Result:

```
Web search results for query: "[another game] 2 movement speed units per second run sprint wallrun slide speed Respawn"

Links: [{"title":"group2 0.1.0","url":"https://cse125.ucsd.edu/2026/cse125g2/docs/TitanfallConstants_8hpp_source.html"},{"title":"[another game] 2: “Wow” – Dieser Speedrun erstaunt sogar die Entwickler","url":"https://mein-mmo.de/[another game]-2-gauntlet-speedrun/"},{"title":"Watch a speedrunner absolutely fly through [another game] 2","url":"https://www.pcgamer.com/watch-a-speedrunner-absolutely-fly-through-[another game]-2"},{"title":"TitanfallConstants 8hpp","url":"https://cse125.ucsd.edu/2026/cse125g2/docs/TitanfallConstants_8hpp.html"},{"title":"[another game] 2: “Wow” – This speedrun even astonishes the developers","url":"https://mein-mmo.de/en/[another game]-2-gauntlet-speedrun,128728"},{"title":"[another game] 2 multiplayer tips and tricks","url":"https://www.techradar.com/how-to/[another game]-2-multiplayer-tips-and-tricks"},{"title":"Welcome to [another game] 2","url":"https://www.techradar.com/uk/how-to/[another game]-2-multiplayer-tips-and-tricks"},{"title":"• Skip to main content","url":"https://gameranx.com/updates/id/20713/article/[another game]-raw-weapon-stats-decrypted-titan-health-and-speed-revealed/"},{"title":"[another game] 2: “Wow” – This speedrun even astonishes the developers","url":"https://mein-mmo.de/en/[another game]-2-wow-this-speedrun-even-astonishes-the-developers,128728/"},{"title":"[another game] 2 multiplayer tips and tricks","url":"https://www.techradar.com/in/how-to/[another game]-2-multiplayer-tips-and-tricks"},{"title":"Wall Running","url":"https://[another game].wiki.gg/wiki/Wall_Running"},{"title":"Sponsored By","url":"https://www.gamedeveloper.com/design/designer-interview-getting-i-[another game]-i-s-controls-just-right"},{"title":"docs.momentum-mod.org","url":"https://docs.momentum-mod.org/guide/gamemodes/parkour/"},{"title":"[another game] 2: Respawn to speed up movement, improve Titan meter following technical test feedback","url":"https://www.ibtimes.co.uk/[another game]-2-respawn-speed-movement-improve-titan-meter-following-technical-test-feedback-1577954"},{"title":"[another game] Features Tips News Buy Features Tips News Buy","url":"https://careers.ea.com/games/[another game]/[another game]-2/news/tech-test-and-feedback"},{"title":"[another game] 2 Speedrun Glossary","url":"https://tf2sr.github.io/TF2SR-Wiki/docs/knowledge-base/glossary/[another game] 2 Speedrun Glossary"},{"title":"I have some questions about the rule change","url":"https://www.speedrun.com/[another game]_2/forums/5dhnv"},{"title":"[another game] 2","u
[... 2143 more characters not shown]
```

**Sat 14 Nov 14:12:39 · Tool call: WebFetch**

```
{
 "url": "https://github.com/NoelFB/[another game]/tree/master/Source",
 "prompt": "List file names in this directory, especially anything named Input, Settings, Player. Give their paths."
}
```

**Sat 14 Nov 14:12:39 · Tool call: WebFetch**

```
{
 "url": "https://gameranx.com/updates/id/20713/article/[another game]-raw-weapon-stats-decrypted-titan-health-and-speed-revealed/",
 "prompt": "Quote exactly what is stated about Pilot run speed, sprint speed, wall-run speed, jump, double jump, and units. Give the author/date if shown and the exact numbers."
}
```

**Sat 14 Nov 14:12:40 · Tool call: WebFetch**

```
{
 "url": "https://www.gamedeveloper.com/design/designer-interview-getting-i-[another game]-i-s-controls-just-right",
 "prompt": "Quote what the Respawn designer says about movement, speed, air control, sliding, wall running, jump forgiveness/coyote/buffering, and camera. Give interviewee name and date. Exact numbers if any."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:12:41 · Tool call: WebSearch**

```
{
 "query": "[another game] 2 player walk speed 190 sprint 320 units per second jump height 21 units Source units to meters 0.75 inch Valve Developer Community",
 "mode": "standard"
}
```

**Sat 14 Nov 14:12:41 · Tool call: WebSearch**

```
{
 "query": "Game Accessibility Guidelines field of view adjustable motion sickness head bob option first person",
 "mode": "standard"
}
```

Result:

```
The page shows two folders in `Source/`, and no files:

- **Player** (folder): `https://github.com/NoelFB/[another game]/tree/master/Source/Player`
- **PICO-8** (folder): `https://github.com/NoelFB/[another game]/tree/master/Source/PICO-8`

Nothing named Input or Settings appears in this directory listing. The page doesn't show the contents of either folder. A "View all files" link is present, but its target isn't included, so I can't confirm whether it lists more.
```

Result:

```
**Source:** Gameranx, "[another game] Raw Weapon Stats Decrypted; Titan Health and Speed Revealed," by Stephen Daly, March 5, 2014.

- **Run speed:** "The base forward running speed of a Pilot is 180.6 units per second, or about 7.7 MPH"
- **Sprint speed:** "the base Sprint speed of Pilots is 269.85 units per second, or 11.5 MPH"
- **Wall-run speed:** "Consecutive wall running speeds up the player gradually, allowing him to reach a maximum of almost twice his sprint speed." The article then adds: "About 22 to 23 MPH however, using burn cards and wall jumping you can reach 19.63 MPH." It doesn't clearly explain how these figures relate.
- **Jump and double jump:** Not mentioned.
- **Units:** The article gives speeds in "units per second" and converts them to MPH.
```

Result:

```
Web search results for query: "Game Accessibility Guidelines field of view adjustable motion sickness head bob option first person"

Links: [{"title":"devdocs.xbox.com","url":"https://devdocs.xbox.com/gaming/accessibility/xbox-accessibility-guidelines/117"},{"title":"learn.microsoft.com","url":"https://learn.microsoft.com/da-dk/gaming/accessibility/xbox-accessibility-guidelines/117"},{"title":"Xbox Accessibility Guideline 117: Visual distractions and motion settings","url":"https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117"},{"title":"Xbox Accessibility Guidelines - Version History","url":"https://learn.microsoft.com/ar-sa/xbox/accessibility/xag-version-history"},{"title":"Redfall_LargeHero_Accessibility.pngRedfall Standard Edition Box Front","url":"https://bethesda.net/en-US/news/redfall-accessibility-guide"},{"title":"This option is critical if you want to play Avowed in first person perspective. Be sure to check the game settings","url":"https://www.gamepressure.com/newsroom/this-option-is-critical-if-you-want-to-play-avowed-in-first-perso/zd797f"},{"title":"Redfall_LargeHero_Accessibility.pngRedfall Standard Edition Box Front","url":"https://bethesda.net/en-EU/news/redfall-accessibility-guide"},{"title":"Redfall_LargeHero_Accessibility.pngRedfall Standard Edition Box Front","url":"https://bethesda.net/en-AU/news/redfall-accessibility-guide"},{"title":"vr accessibility","url":"https://www.gamedeveloper.com/audio/vr-accessibility"},{"title":"Image via Inflexion","url":"https://vip-develop.destructoid.com/?p=465148"},{"title":"Background by @soberanesMotion Sickness Accessibility in Video Games","url":"https://madelinemiller.dev/blog/motion-sickness-accessibility/"},{"title":"how to reduce motion sickness from fast movement in games","url":"https://macmyths.com/how-to-reduce-motion-sickness-from-fast-movement-in-games/"},{"title":"Forgot password","url":"https://primagames.com/?p=241612"},{"title":"gameaccessibilityguidelines.com","url":"https://gameaccessibilityguidelines.com/?p=21"},{"title":"hn.nuxt.dev","url":"https://hn.nuxt.dev/item/42888538"},{"title":"VR Comfort Settings Checklist & Glossary for Developers and Players Alike","url":"https://www.roadtovr.com/?p=99801"},{"title":"gameaccessibilityguidelines.com","url":"https://gameaccessibilityguidelines.com/?p=3295"}]

The most authoritative match is Microsoft's Xbox Accessibility Guideline 117, which covers visual distractions and motion settings. It recommend
[... 1388 more characters not shown]
```

Result:

```
Web search results for query: "[another game] 2 player walk speed 190 sprint 320 units per second jump height 21 units Source units to meters 0.75 inch Valve Developer Community"

Links: [{"title":"developer.valvesoftware.com","url":"https://developer.valvesoftware.com/wiki/Pl/Dimensions"},{"title":"Dimensions ([another game] 2 and [another game]: Source)","url":"https://developer.valvesoftware.com/wiki/Dimensions_%28[another game]_2_and_[another game]%3A_Source%29"},{"title":"Dimensions ([another game] 2 and [another game]: Source)","url":"https://developer.valvesoftware.com/wiki/Dimensions_([another game]_2_and_[another game]:_Source)"},{"title":"developer.valvesoftware.com","url":"https://developer.valvesoftware.com/wiki/Dimensions?uselang=pl"},{"title":"Speed of Sound","url":"https://developer.valvesoftware.com/wiki/Talk:Dimensions"},{"title":"Mapper%27s Reference","url":"https://developer.valvesoftware.com/wiki/Team_Fortress_2/Mapper%27s_Reference"},{"title":"Team Fortress 2 Mapper%27s Reference","url":"https://developer.valvesoftware.com/wiki/TF2/Team_Fortress_2_Mapper%27s_Reference"},{"title":"[another game] 2: VR Mod","url":"https://steamcommunity.com/app/658920/discussions/0/5057002258663243524"},{"title":"Blog/HL2/🧠Advanced Strategy","url":"https://gamertagmythras.com/blog/[another game]-2/[another game]-2-speedrunning-guide"},{"title":"hl2 player","url":"https://swarm.workshop.perforce.com/files/guest/knut_wikstrom/ValveSDKCodedlls/hl2_dll/hl2_player.cpp"},{"title":"developer.valvesoftware.com","url":"https://developer.valvesoftware.com/wiki/Bunnyhopping"},{"title":"Accelerated Hop","url":"https://wiki.sourceruns.org/en/Source/Accelerated_Hop"},{"title":"[another game] 2","url":"https://steamcommunity.com/app/220/discussions/0/3716062978728218724"},{"title":"Garry's Mod","url":"https://steamcommunity.com/sharedfiles/filedetails/comments/2876378639"},{"title":"[another game] 2","url":"https://steamcommunity.com/app/220/discussions/0/3498761686675982542"},{"title":"developer.valvesoftware.com","url":"https://developer.valvesoftware.com/wiki/Bunnyhop"},{"title":"Player speed variable in HL code Created 7 years ago2017-10-16 10:56:03 UTC by Mr Gnang Mr Gnang","url":"https://twhl.info/thread/view/19366"},{"title":"[another game]: Alyx – Movement Speed Increase","url":"https://naguide.com/?p=15765"}]

The search turned up most of the numbers you asked about, though not all from the Valve Developer Community.

- **Speed:** The Valve wiki's Polish-language Dimensions page lists running at 190 units, with wa
[... 931 more characters not shown]
```

**Sat 14 Nov 14:12:53 · Tool call: WebFetch**

```
{
 "url": "https://developer.valvesoftware.com/wiki/Dimensions_([another game]_2_and_[another game]:_Source)",
 "prompt": "Quote unit conversion statements, player speed numbers (walk, run, sprint, crouch), jump heights, eye height, hull dimensions, with exact numbers."
}
```

**Sat 14 Nov 14:12:53 · Tool call: WebFetch**

```
{
 "url": "https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117",
 "prompt": "Quote what the guideline says about field of view, head bob, camera shake, motion blur, with specific numbers if any (and the guideline title/date)."
}
```

**Sat 14 Nov 14:12:53 · Tool call: WebFetch**

```
{
 "url": "https://gameaccessibilityguidelines.com/?p=21",
 "prompt": "Quote the guideline text on field of view, headbob/weapon bob, and motion sickness. Give the guideline title and level."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

Result:

```
---
layout: Conceptual
title: XBOX Accessibility Guideline 117 - Microsoft Game Dev | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117
uhfHeaderId: MSDocsHeader-Gaming
breadcrumb_path: /gaming/breadcrumb/toc.json
feedback_system: Standard
ms.service: microsoft-game-development-kit
author: edigonzales
ms.author: edigonzales
ms.topic: article
description: XBOX Accessibility Guideline 117.
ms.date: 2026-11-13T00:00:00.0000000Z
locale: en-us
document_id: 80fe8041-2398-07bd-3e0e-666c3ac92cb6
document_version_independent_id: 80fe8041-2398-07bd-3e0e-666c3ac92cb6
updated_at: 2026-11-14T02:19:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/gaming-docs-pr/blob/live/gaming/accessibility/xbox-accessibility-guidelines/117.md
gitcommit: https://github.com/MicrosoftDocs/gaming-docs-pr/blob/6b71c10de53da9c760ebea66bd3ed00fe861ce27/gaming/accessibility/xbox-accessibility-guidelines/117.md
git_commit_id: 6b71c10de53da9c760ebea66bd3ed00fe861ce27
site_name: Docs
depot_name: Learn.gamingdocs
page_type: conceptual
toc_rel: ../../toc.json
feedback_product_url: ''
feedback_help_link_type: ''
feedback_help_link_url: ''
word_count: 1387
asset_id: accessibility/xbox-accessibility-guidelines/117
moniker_range_name: 
monikers: []
item_type: Content
source_path: gaming/accessibility/xbox-accessibility-guidelines/117.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/7fb84634-1717-41ef-acf8-015766493b4a
- https://authoring-docs-microsoft.poolparty.biz/devrel/70117bcd-fc2d-46aa-a329-32b66b3d085f
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/108d8c44-ddc8-4ac8-9e15-4998cc9acea7
- https://authoring-docs-microsoft.poolparty.biz/devrel/156954d1-952a-430e-bdf3-c54bd56edeea
platformId: 46a7c5e8-f0fb-37bf-ed3c-aecb4bbb4d86
---

# XBOX Accessibility Guideline 117 - Microsoft Game Dev | Microsoft Learn

## Goal

The goal of this XBOX Accessibility Guideline (XAG) is to ensure that players can pause or completely stop any content that scrolls, blinks, auto-updates, or otherwise moves. Additionally, players should be able to customize game settings related to field of view, camera movement and sensitivity, and other visual settings related to camera or screen movement. This benefits players who are susceptible to motion sickness, players who are easily distracted by blinking, scrolling, or otherwise moving content, and players who are unable to quickly read text bef
[... 13069 more characters not shown]
```

**Sat 14 Nov 14:12:54 · Tool call: WebSearch**

```
{
 "query": "Squirrel Eiserloh GDC 2016 Math for Game Programmers Juicing Your Cameras With Math trauma max yaw 30 degrees pitch roll offset",
 "mode": "standard"
}
```

Result:

```
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:12:55 · Tool call: WebSearch**

```
{
 "query": "[another game] 2016 player movement speed id Software developer \"Marty Stratton\" OR \"Hugo Martin\" OR \"Tom Willits\" movement fast no sprint units",
 "mode": "standard"
}
```

Result:

```
Web search results for query: "Squirrel Eiserloh GDC 2016 Math for Game Programmers Juicing Your Cameras With Math trauma max yaw 30 degrees pitch roll offset"

Links: [{"title":"Math for Game Programmers Juicing","url":"https://gdcvault.com/play/1023146/Math-for-Game-Programmers-Juicing"},{"title":"Video: Sprucing up cameras with math","url":"https://gamedeveloper.com/programming/video-sprucing-up-cameras-with-math"},{"title":"Reader Brief: In this 2016 GDC session, SMU Guildhall's Squirrel Eiserloh explores the math behind a variety of","url":"https://irc.pcper.com/camera-systems-game-engine-series.html"},{"title":"Context Notes: In this 2016 GDC session, SMU Guildhall's Squirrel Eiserloh explores the math behind a variety of","url":"https://sales.communityimpact.com/camera-controllers-game-engine-series.html"},{"title":"Page Summary: In this 2016 GDC session, SMU Guildhall's Squirrel Eiserloh explores the math behind a variety of","url":"https://baks.verde.ag/6-game-creator-101-cameras.html"},{"title":"Math for Game Programmers: Juicing Your Cameras With Math","url":"https://www.espinoinsurance.com/video/qe-Hs66TjqK/Math-for-Game-Programmers-Juicing-Your-Cameras-With-Math.html"},{"title":"Video: Sprucing up cameras with math","url":"https://www.jikguard.com/news/video-sprucing-up-cameras-with-math"},{"title":"Session Name: | Math for Game Programmers: Juicing Your Cameras With Math |","url":"https://gdcvault.com/play/1023146/contactUs"},{"title":"game engine coding quickies cameras","url":"https://sales.communityimpact.com/game-engine-coding-quickies-cameras.html"},{"title":"gdcvault.com","url":"https://gdcvault.com/play/1023557/contactUs"},{"title":"GDC16 – Day 1","url":"https://blogs.jccc.edu/dpatter/2016/03/15"},{"title":"Squirrel Eiserloh","url":"https://smu.edu/Guildhall/People/Faculty/Squirrel-Eiserloh"},{"title":"Session Name: | Math for Game Programmers: Understanding Homogeneous Coordinates |","url":"https://www.gdcvault.com/play/1022150/contactUs"},{"title":"Math for Game Developers Curves","url":"https://gdcvault.com/play/1025907/Math-for-Game-Developers-Curves"},{"title":"Session Name: | Math for Game Programmers |","url":"https://www.gdcvault.com/play/1018832/contactUs"},{"title":"r/gamedev @Winter_Cell Dec 26 '17","url":"https://axebps-redlib.hf.space/r/gamedev/comments/7m6w0t/math_for_game_programmers_juicing_your_cameras"},{"title":"practical juicing for game devs efe9b06c246b","url":"https://medium.com/@dvdfu/practical-juicing-for-game-
[... 1532 more characters not shown]
```

Result:

```
Web search results for query: "[another game] 2016 player movement speed id Software developer "Marty Stratton" OR "Hugo Martin" OR "Tom Willits" movement fast no sprint units"

Links: [{"title":"inside [another game]'s brutally fast single player campaign","url":"https://bethesda.net/en-EU/news/inside-[another game]'s-brutally-fast-single-player-campaign"},{"title":"[another game] feels like \"Bruce Lee with a shotgun on a skateboard,\" says id","url":"https://www.pcgamer.com/au/[another game]-feels-like-bruce-lee-with-a-shotgun-on-a-skateboard-says-id"},{"title":"inside [another game]'s brutally fast single player campaign","url":"https://bethesda.net/en-NZ/news/inside-[another game]'s-brutally-fast-single-player-campaign"},{"title":"[another game] feels like \"Bruce Lee with a shotgun on a skateboard,\" says id","url":"https://pcgamer.com/[another game]-feels-like-bruce-lee-with-a-shotgun-on-a-skateboard-says-id"},{"title":"inside [another game]'s brutally fast single player campaign","url":"https://bethesda.net/en-AU/news/inside-[another game]'s-brutally-fast-single-player-campaign"},{"title":"new [another game] based on original john romero","url":"https://pcgamesn.com/[another game]/new-[another game]-based-on-original-john-romero"},{"title":"[another game]: The Dark Ages Interview – Medieval Setting, Combat Changes, and More","url":"https://gamingbolt.com/[another game]-the-dark-ages-interview-medieval-setting-combat-changes-and-more"},{"title":"With [another game]: The Dark Ages, id Software is still searching for what made the original great, and I hope it never finds it","url":"https://uk.news.yahoo.com/[another game]-dark-ages-id-software-170805110.html"},{"title":"[another game] guns demons speed","url":"https://www.sector.sk/game-news/117033/[another game]-guns-demons-speed.htm"},{"title":"with [another game] the dark ages id software is still searching for what made the original great and i hope it never finds it","url":"https://www.pcgamer.com/games/fps/with-[another game]-the-dark-ages-id-software-is-still-searching-for-what-made-the-original-great-and-i-hope-it-never-finds-it"},{"title":"[another game] Eternal: Aggression solves every problem","url":"https://game.info.intel.com/gaming-access/[another game]-eternal-aggression-solves-every-problem"},{"title":"[another game] Eternal director explains why the 2016 game's mechanics weren't working for this sequel","url":"https://gonintendo.com/stories/353237-[another game]-eternal-director-explains-why-the-2016-game-s-mechanics-were"},{"title":"Sponsored By","url":"https://gamedeveloper.com/design/q-a-evolving-the-combat-design-of-id-software-s-i-[another game]-eternal-i-"},{"title":"[another game] E3 2015 - Cyberdemon 2","url":"https://gamesbeat.com/?p=122494"},{"titl
[... 2459 more characters not shown]
```

**Sat 14 Nov 14:13:08 · Tool call: WebFetch**

```
{
 "url": "https://en.wikipedia.org/wiki/Field_of_view_in_video_games",
 "prompt": "Quote the defaults and ranges of FOV given for named games ([another game], [another game] 2, [another game], [another game], Apex, [another game] etc.), whether horizontal or vertical, and the conversion formula between horizontal and vertical FOV with aspect ratio. Exact numbers."
}
```

**Sat 14 Nov 14:13:08 · Tool call: WebFetch**

```
{
 "url": "https://www.pcgamingwiki.com/wiki/Glossary:Field_of_view_(FOV)",
 "prompt": "Quote the explanation of horizontal vs vertical FOV, the conversion formula, the 4:3 90 degrees to 16:9 conversion, recommended FOV values, and any table of common FOV values."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:13:09 · Tool call: WebFetch**

```
{
 "url": "https://www.pcgamingwiki.com/wiki/[another game]_Eternal",
 "prompt": "Quote the Field of view (FOV) row in video settings: default, range, horizontal/vertical, plus mouse acceleration/raw input and head bob / camera shake options."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:13:10 · Tool call: WebFetch**

```
{
 "url": "https://www.pcgamingwiki.com/wiki/[another game]",
 "prompt": "Quote the Field of view (FOV) row: default, range, notes about horizontal/vertical or 4:3; and mouse acceleration / raw input row."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:13:10 · Tool call: WebFetch**

```
{
 "url": "https://www.pcgamingwiki.com/wiki/[another game]",
 "prompt": "Quote the Field of view (FOV) row: default, range, scale notes (e.g. 70-110, 4:3 vs 16:9, FOV scale), and mouse raw input row."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

Result:

```
The article doesn't give defaults or ranges for any named game ([another game], [another game] 2, [another game], [another game], Apex, [another game], or others), so I can't provide exact numbers for them.

It does give these general figures, without saying whether they are horizontal or vertical:

- Console: "a narrow FOV of around 60 degrees is used for console games"
- PC: a FOV "of 90 to 100 degrees is usually set for PC games"
- Average human visual field, including peripheral vision: approximately 170–180 degrees

**Conversion between horizontal and vertical FOV**

Where *r* is the aspect ratio, *w* and *h* are width and height, and *H* and *V* are the horizontal and vertical FOV:

- r = w/h = tan(H/2) / tan(V/2)
- H = 2 × arctan(tan(V/2) × (w/h))
- V = 2 × arctan(tan(H/2) × (h/w))
```

**Sat 14 Nov 14:13:15 · Tool call: WebSearch**

```
{
 "query": "[another game] default FOV 90 4:3 horizontal equals 106.26 at 16:9 Source engine fov_desired [another game] 2 default 75",
 "mode": "standard"
}
```

**Sat 14 Nov 14:13:15 · Tool call: WebSearch**

```
{
 "query": "[another game] default FOV 103 vertical horizontal 16:9 range 80 103 Blizzard; [another game] FOV 70 110 slider horizontal 4:3",
 "mode": "standard"
}
```

**Sat 14 Nov 14:13:16 · Tool call: WebSearch**

```
{
 "query": "[another game] Eternal FOV slider range 90 to 120 default horizontal; [another game] 2016 FOV 80 to 130 default 90 PCGamingWiki",
 "mode": "standard"
}
```

**Sat 14 Nov 14:13:17 · Tool call: WebSearch**

```
{
 "query": "[other-app] FOV fixed 103 horizontal; Halo Infinite FOV default 100 range 80-120; Destiny 2 PC FOV 105 default range 70 120 vertical",
 "mode": "standard"
}
```

**Sat 14 Nov 14:13:17 · Tool call: WebSearch**

```
{
 "query": "[another game] default FOV 90 horizontal cl_bob cl_bobcycle cl_rollangle default values [another game] console variables",
 "mode": "standard"
}
```

Result:

```
Web search results for query: "[another game] default FOV 103 vertical horizontal 16:9 range 80 103 Blizzard; [another game] FOV 70 110 slider horizontal 4:3"

Links: [{"title":"[another game] gets an FOV slider after all","url":"https://www.pcgamer.com/[another game]-gets-an-fov-slider-after-all"},{"title":"[another game] gets an FOV slider after all","url":"https://www.pcgamer.com/uk/[another game]-gets-an-fov-slider-after-all"},{"title":"[another game] gets an FOV slider after all","url":"https://www.pcgamer.com/au/[another game]-gets-an-fov-slider-after-all"},{"title":"[another game] FOV","url":"https://www.pcgamesn.com/[another game]/dont-worry-[another game]-no-longer-has-a-fixed-fov"},{"title":"Increase Maximum Allowed FOV","url":"https://us.forums.blizzard.com/en/[another game]/t/increase-maximum-allowed-fov/756468"},{"title":"The best FoV (Field of View) for [another game]","url":"https://www.esportstales.com/[another game]/the-best-fov-field-of-view"},{"title":"[another game] 2 Best Pro Settings For PC","url":"https://gamersdecide.com/articles/[another game]-2-best-pro-settings-pc"},{"title":"It's 2022, and FoV Settings Are Still So Limited","url":"https://us.forums.blizzard.com/en/[another game]/t/its-2022-and-fov-settings-are-still-so-limited/661118"},{"title":"2015 09 07 blizzard restores fov slider in latest [another game] build","url":"https://www.gamewatcher.com/2015-09-07-blizzard-restores-fov-slider-in-latest-[another game]-build"},{"title":"• Skip to main content","url":"https://gameranx.com/?p=29102"},{"title":"Best FOV Settings In [another game] 2","url":"https://exputer.com/?p=112034"},{"title":"[another game] 2 fov calculator","url":"https://fovcalculator.netlify.app/games/[another game]-2-fov-calculator"},{"title":"[another game] | Blizzard Confirms FOV Slider","url":"https://redgamingtech.com/[another game]-blizzard-confirms-fov-slider/"},{"title":"How to Change FOV in [another game] 2 - SarkariResult","url":"https://roller.rock-up.co.uk/cnn/how-to-change-fov-in-[another game]-2-sarkariresult.html"},{"title":"[another game] 2 best pro settings pc","url":"https://gamersdecide.dev.weebpal.com/articles/[another game]-2-best-pro-settings-pc"},{"title":"r/Blizzard 8d ago","url":"https://lr.in.psf.lt/r/Blizzard/comments/1k6s4y4/add_fov_slider_to_console/mouhp0u/?context=3"}]

I ran one search. It covered [another game] only, so I have nothing on [another game]' FOV range or its horizontal 4:3 figures.

**[another game] (mostly [another game] 2, plus original [another game] history):**
- **Range and default:** Sources say OW2's FOV slider runs 80 to 103 and is vertical, not horizontal. One calc
[... 1081 more characters not shown]
```

Result:

```
Web search results for query: "[another game] Eternal FOV slider range 90 to 120 default horizontal; [another game] 2016 FOV 80 to 130 default 90 PCGamingWiki"

Links: [{"title":"[another game] Eternal console commands: FOV, change run speed, and more","url":"https://www.tweaktown.com/news/71641/[another game]-eternal-console-commands-fov-change-run-speed-and-more/index.html"},{"title":"TRENDING: [another game] 6 release date confirmed by Take-Two","url":"https://www.tweaktown.com/news/71641/about/news/gaming/newsletter/index.html"},{"title":"Why low FOV in first-person games can make you feel nauseous","url":"https://pcgamer.com/why-low-fov-in-first-person-games-can-make-you-feel-nauseous"},{"title":"[another game] Eternal","url":"https://steamcommunity.com/app/782330/discussions/0/4032474174136132872"},{"title":"[another game] pc features revealed fov slider chromatic aberration option ultra wide monitor support","url":"https://www.dsogaming.com/news/[another game]-pc-features-revealed-fov-slider-chromatic-aberration-option-ultra-wide-monitor-support/"},{"title":"www.tweaktown.com","url":"https://www.tweaktown.com/news/71641/about/index.html"},{"title":"www.dsogaming.com","url":"https://www.dsogaming.com/?p=87340"},{"title":"[another game] Eternal","url":"https://steamcommunity.com/app/782330/discussions/0/2263565217519893716/?l=russian"},{"title":"[another game] Eternal","url":"https://steamcommunity.com/app/782330/discussions/0/2263565217519893716"},{"title":"dsogaming.com","url":"https://dsogaming.com/?p=87925"},{"title":"Forgot password","url":"https://pcinvasion.com/?p=128284"},{"title":"[another game]: Vanguard has a full-fat FOV slider on console","url":"https://gamesradar.com/[another game]-vanguard-has-a-full-fat-fov-slider-on-console"},{"title":"[another game]: Warzone console players are clamoring for an FOV slider that PC players have had since day one","url":"https://www.pcgamer.com/[another game]-warzone-console-players-are-clamoring-for-an-fov-slider-that-pc-players-have-had-since-day-one"},{"title":"[another game]: Graphics options for PC known – “PC gaming is in our DNA”","url":"https://mein-mmo.de/en/[another game]-grafik-optionen-pc,75458/"},{"title":"gameranx.com","url":"https://gameranx.com/?p=49370"},{"title":"eteknix.com","url":"https://eteknix.com/[another game]-advanced-graphics-options-revealed/amp"},{"title":"[another game] Eternal","url":"https://gamecytus.netlify.app/host-https-www.pcgamingwiki.com/wiki/[another game]_Eternal"},{"title":"r/PS5 Oct 06 '21","url":"https://reddit.rtrace.io/r/PS5/comments/q2vfws/whats_your_opinion_regarding_the_fov_i_hope_a/"},{"title":"DO
[... 1370 more characters not shown]
```

Result:

```
Web search results for query: "[another game] default FOV 90 4:3 horizontal equals 106.26 at 16:9 Source engine fov_desired [another game] 2 default 75"

Links: [{"title":"DEV Community","url":"https://dev.to/keyboard-testerclick/why-the-same-fov-feels-different-across-games-hfov-vs-vfov-2blf"},{"title":"steamcommunity.com","url":"https://steamcommunity.com/app/673130/discussions/0/1629665087685108857"},{"title":"cs2 fov calculator","url":"https://fovcalculator.netlify.app/games/cs2-fov-calculator"},{"title":"What Does FOV Mean in FPS Games?","url":"https://fovcalculator.netlify.app/blog/what-is-fov"},{"title":"[another game] 2","url":"https://steamcommunity.com/app/730/discussions/0/541907867770099391"},{"title":"steamcommunity.com","url":"https://steamcommunity.com/app/673130/discussions/2/1698293703770638297"},{"title":"www.mouse-sensitivity.com","url":"https://www.mouse-sensitivity.com/forums/topic/24-[another game]-2-prev-[another game]-global-offensive/page/4/"},{"title":"the 16 9 vs 4 3 aspect ratio argument 667bd771b342","url":"https://medium.com/@lurppis/the-16-9-vs-4-3-aspect-ratio-argument-667bd771b342"},{"title":"github.com","url":"https://www.github.com/redeclipse/base/pull/1322"},{"title":"Please make FOV a client setting","url":"https://forums.unknownworlds.com/discussion/116308"},{"title":"Horizontal FOV Calculator: Find Your Perfect Field of View","url":"https://west-games.com/?p=29170"},{"title":"16:9 in CSGO is totally f'ed","url":"https://forums.blurbusters.com/viewtopic.php?p=6823"},{"title":"[another game] 2","url":"https://steamcommunity.com/app/730/discussions/0/3881597531965154309"},{"title":"CalculatorGame Calculators FOV DemoFAQBlog CS2 Calculator [other-app] Calculator Apex Calculator","url":"https://fovcalculator.netlify.app/"},{"title":"Vertical FOV Calculator – Find Your Exact Field of View","url":"https://west-games.com/vertical-fov-calculator/"},{"title":"КС2 Калькулятор разрешения и соотношения сторон","url":"https://csdb.gg/ru/resolution-calculator/"},{"title":"8759 43 to 169 csgo","url":"https://www.mouse-sensitivity.com/forums/topic/8759-43-to-169-csgo/"}]

The math checks out, and several sources agree on the core numbers. I did not find a source confirming the [another game] 2 default of 75.

- **The conversion is consistent across sources.** A 90° horizontal FOV at 4:3 becomes about 106.26° at 16:9, as 90 H at 4:3 = 73.74 V = 106.26 H at 16:9 in the DEV Community article. Using the standard formula, I get the same result: the 4:3
[... 1077 more characters not shown]
```

Result:

```
Web search results for query: "[other-app] FOV fixed 103 horizontal; Halo Infinite FOV default 100 range 80-120; Destiny 2 PC FOV 105 default range 70 120 vertical"

Links: [{"title":"support.halowaypoint.com","url":"https://support.halowaypoint.com/hc/en-us/articles/4408359189652"},{"title":"See Destiny 2's FOV at its highest and lowest settings","url":"https://www.pcgamer.com/see-destiny-2s-fov-at-its-highest-and-lowest-settings"},{"title":"Best [other-app] Field of View (FOV) Settings And How To Change It","url":"https://www.gfinityesports.com/[other-app]/best-[other-app]-field-of-view-fov-settings-and-how-to-change-it/"},{"title":"How to change your FOV in [other-app]","url":"https://www.ggrecon.com/guides/how-to-change-[other-app]-fov/"},{"title":"Best [other-app] Field of View (FoV) Settings?","url":"https://primagames.com/tips/best-[other-app]-field-of-view-fov-settings"},{"title":"How to change your FOV in [other-app]","url":"https://www.ggrecon.com/guides/how-to-change-your-fov-in-[other-app]/"},{"title":"The best [other-app] field of view (FOV) settings","url":"https://vip-develop.gamepur.com/?p=281906"},{"title":"Best [other-app] Field of View (FoV) Settings? - Prima Games","url":"https://primagames.com/?p=53971"},{"title":"Forgot password","url":"https://gamepur.com/?p=281906"},{"title":"How to Adjust FOV in [other-app] to Improve Your Gameplay","url":"https://bo3.gg/[other-app]/articles/how-to-change-fov-in-[other-app]"},{"title":"is it possible to change the fov in [other-app]","url":"https://www.fragster.com/is-it-possible-to-change-the-fov-in-[other-app]/"},{"title":"Best FOV settings for Halo Infinite","url":"https://vip-develop.gamepur.com/?p=211263"},{"title":"[other-app] FoV guide: The best screen settings for the shooter in 2023","url":"https://sportskeeda.com/[other-app]/[other-app]-fov-guide-the-best-screen-settings-shooter-2023"},{"title":"The best FoV (Field of View) for Destiny 2","url":"https://www.esportstales.com/destiny/the-best-fov-field-of-view"},{"title":"How to change FOV in [other-app]","url":"https://afkgaming.com/esports/guide/can-you-change-fov-in-[other-app]"},{"title":"What is the Best FOV for Halo Infinite? - Answered - Prima Games","url":"https://primagames.com/?p=52399"},{"title":"halo infinite best fov","url":"https://gamersdecide.dev.weebpal.com/articles/halo-infinite-best-fov"}]

The search partly confirms the [other-app] figure but contradicts the other two.

- **[other-app]:** Confirmed as fixed. Unlike other FPS games, [other-app] doesn't have a FOV slider and is locked in at a hig
[... 1022 more characters not shown]
```

Result:

```
Web search results for query: "[another game] default FOV 90 horizontal cl_bob cl_bobcycle cl_rollangle default values [another game] console variables"

Links: [{"title":"[another game] Wiki","url":"https://[another game].fandom.com/wiki/Console_Commands_(Q1)"},{"title":"gist.github.com","url":"https://gist.github.com/disco0/6759b83a62a3915b7d6764842e603d96"},{"title":"Pace of movement and other useful c-vars","url":"https://discuss.quaddicted.com/t/pace-of-movement-and-other-useful-c-vars/2803"},{"title":"quakeworld-docs.pages.dev","url":"https://quakeworld-docs.pages.dev/qwcl/cvar"},{"title":"#1 2021-05-25 10:59:27","url":"https://www.quaddicted.com/forum/viewtopic.php?id=882"},{"title":"[another game]: KEX Enhanced: CVAR and Command List Guide","url":"https://gamepretty.com/[another game]-kex-enhanced-cvar-and-command-list-guide/"},{"title":"[another game] KEX Enhanced: CVAR & Command list","url":"https://gamepretty.com/[another game]-kex-enhanced-cvar-command-list/"},{"title":"[another game]: KEX Enhanced: CVAR and Command List Guide","url":"https://gamepretty.com/?p=47040"},{"title":"freeslave.github.io","url":"https://freeslave.github.io/[another game]-featureful/docs/configuration/cvars/"},{"title":"icculus.org","url":"https://icculus.org/twilight/darkplaces/readme.html"},{"title":"From Valve Developer Community","url":"https://developer.valvesoftware.com/wiki/HL_cvars"},{"title":"quakewiki.org","url":"https://quakewiki.org/wiki/fov"},{"title":"14 3 console commands","url":"https://www.ludo.guide/guide/[another game]/14-3-console-commands"},{"title":"List of [another game] console commands and variables","url":"https://developer.valvesoftware.com/wiki/List_of_[another game]_console_commands_and_variables"},{"title":"Module darkplaces: Change committed","url":"https://icculus.org/pipermail/twilight-commits/2007-March/004986.html"},{"title":"File: 040_cvarlist.md","url":"https://sources.debian.org/src/yquake2/8.20%2Bctf1.09%2Bdfsg-1/doc/040_cvarlist.md"},{"title":"Console Commands and Variables","url":"https://github.com/dghost/quake2vr/wiki/Console-Commands-and-Variables"},{"title":"[another game] useful console commands","url":"https://re-actor.net/[another game]-useful-console-commands"},{"title":"www.cryengine.com","url":"https://www.cryengine.com/docs/static/engines/cryengine-3/categories/9895942/pages/9215947"},{"title":"040 cvarlist","url":"https://www.github.com/0lvin/heretic2/blob/master/doc/040_cvarlist.md"}]

The search turned up consistent defaults for the [another game] 1 variables, but the FOV source conflicts with the "horizontal" premise.

- **cl_bob:** The default
[... 1463 more characters not shown]
```

### Sat 14 Nov 14:13:31 · Agent (claude-sonnet-5-5)

Constants for [another game] 1, [another game] 3, Source SDK and [another game] are confirmed from source files. Now doing a final batch on Halo FOV, Source bob, mouse input and first-person coyote time, then writing up.

**Sat 14 Nov 14:13:31 · Tool call: WebFetch**

```
{
 "url": "https://support.halowaypoint.com/hc/en-us/articles/4408359189652",
 "prompt": "Quote what is stated about field of view default, minimum, maximum and whether it is horizontal or vertical, and any aspect ratio statement."
}
```

Result:

```
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

**Sat 14 Nov 14:13:32 · Tool call: WebFetch**

```
{
 "url": "https://www.pcgamer.com/[another game]-gets-an-fov-slider-after-all",
 "prompt": "Quote exact FOV numbers: range, default, horizontal or vertical, aspect ratio, and who at Blizzard said it and the date."
}
```

**Sat 14 Nov 14:13:33 · Tool call: WebFetch**

```
{
 "url": "https://raw.githubusercontent.com/ValveSoftware/source-sdk-2013/master/src/game/client/in_mouse.cpp",
 "prompt": "Quote ConVar definitions with defaults: m_rawinput, m_filter, m_customaccel, m_mouseaccel1, sensitivity, m_pitch, m_yaw, and comments about raw input."
}
```

**Sat 14 Nov 14:13:34 · Tool call: WebSearch**

```
{
 "query": "Source SDK cl_bob cl_bobcycle cl_bobup default 0.002 0.8 0.5 viewmodel bob c_baseviewmodel OR view_scene",
 "mode": "standard"
}
```

**Sat 14 Nov 14:13:34 · Tool call: WebSearch**

```
{
 "query": "first person game developer coyote time jump buffering \"[another game] 2\" OR \"[another game]\" OR \"[another game]\" OR \"[another game]\" OR \"[another game] Eternal\" developer says coyote time",
 "mode": "standard"
}
```

Result:

```
The provided content is truncated after the headline, so I can't find the FOV range, default value, horizontal or vertical orientation, aspect ratio, or the Blizzard speaker and date.

The only visible text is the headline: "[another game] gets an FOV slider after all," from PC Gamer. That confirms an FOV slider was added but gives no specifics.

If you share the full article text, I can pull out those details.
```

Result:

```
Web search results for query: "Source SDK cl_bob cl_bobcycle cl_bobup default 0.002 0.8 0.5 viewmodel bob c_baseviewmodel OR view_scene"

Links: [{"title":"Last active","url":"https://gist.github.com/kyokyoknutt/8e6607d78409637fa9ac069c482eb303"},{"title":"Blackmesa viewmodel","url":"https://developer.valvesoftware.com/wiki/Blackmesa_viewmodel"},{"title":"cl bobcycle","url":"https://csdb.gg/command/cl-bobcycle/"},{"title":"cl bobcycle","url":"https://csdb.gg/pl/command/cl-bobcycle/"},{"title":"cl bobcycle","url":"https://csdb.gg/de/command/cl-bobcycle/"},{"title":"CS:GO cl_bobup Command","url":"https://totalcsgo.com/command/clbobup"},{"title":"cl bobcycle","url":"https://csdb.gg/es/command/cl-bobcycle/"},{"title":"CS:GO cl_bobup Command","url":"https://totalcsgo.com/commands/clbobup"},{"title":"Create an account","url":"https://forums.xonotic.org/showthread.php?tid=2129"},{"title":"- calculates the number that is used to 'push' the viewmodel forward in [another game]V_CalcRoll","url":"https://twhl.info/wiki/page/Tutorial:_View_bobbing:_Part_1"},{"title":"Cl bob","url":"https://wiki.sourceruns.org:443/wiki/Cl_bob"},{"title":"Cl bob","url":"https://wiki.sourceruns.org/Cl-bob.html"},{"title":"Install Steam","url":"https://steamcommunity.com/groups/ohackedteam"},{"title":"cl bobamt vert","url":"https://csdb.gg/de/command/cl-bobamt-vert/"},{"title":"cl bob lower amt","url":"https://csdb.gg/es/command/cl-bob-lower-amt/"},{"title":"cl bobamt vert","url":"https://csdb.gg/command/cl-bobamt-vert/"},{"title":"cl bob lower amt","url":"https://csdb.gg/pl/command/cl-bob-lower-amt/"}]

The search didn't confirm the defaults in your query. The values I found differ by game and engine, and I found nothing on `c_baseviewmodel` or `view_scene`.

- **Source SDK 2013 (multiplayer):** A community gist of the bob code declares `cl_bob` at 1, `cl_bobup` at 0.5, and `cl_bobcyclemax` at 0.45. It uses `cl_bob` as an on/off-style check when bobbing the viewmodel angles. static ConVar cl_bobcyclemin( "cl_bobcyclemin","1.5" ); static ConVar cl_bobcyclemax("cl_bobcyclemax", "0.45"); static ConVar cl_bob( "cl_bob","1" ); ... static ConVar cl_bobup( "cl_bobup","0.5" );. This is a secondary source, so check it against the SDK's own `view_scene`/viewmodel code if you need exact values.
- **[another game]/GoldSrc:** The SourceRuns wiki lists cl_bob with a default of 0.01 for GoldSrc games, which doesn't match your 0.002.
- **Black Mesa:** The Valve wiki lists cl_bobcycle at 0.01 and cl_bobup at 1.
- *
[... 710 more characters not shown]
```

Result:

```
**Raw input and related ConVars**

- **m_rawinput**: default `"1"`, help text: "Use Raw Input for mouse input."
- **m_filter**: default `"0"`, help text: "Mouse filtering (set this to 1 to average the mouse over 2 frames)."
- **m_customaccel**: default `"0"`, help text begins "Custom mouse acceleration:" and includes "0: custom accelaration disabled"
- **m_mouseaccel1**: default `"0"`, help text: "Windows mouse acceleration initial threshold (2x movement)."
- **sensitivity**: default `"3"`, help text: "Mouse sensitivity."
- **m_pitch**: default `"0.022"`, help text: "Mouse pitch factor."
- **m_yaw**: default `"0.022"`, help text: "Mouse yaw factor."

**Raw input comments**

The only comment about raw input is the `m_rawinput` help text. The code also checks `m_rawinput` in `GetAccumulatedMouseDeltasAndResetAccumulators()` and `AccumulateMouse()`, but those functions have no explanatory comments. A one-time startup system (`CRawInputConvarOnetimeReset`) forces `m_rawinput` to `1` once, though it has no comment.
```

Result:

```
Web search results for query: "first person game developer coyote time jump buffering "[another game] 2" OR "[another game]" OR "[another game]" OR "[another game]" OR "[another game] Eternal" developer says coyote time"

Links: [{"title":"Credit: Luckshot Games","url":"https://www.austinchronicle.com/arts/locally-made-video-game-big-hops-embraces-coyote-time"},{"title":"coyote time and input buffering explained","url":"https://bugnet.io/blog/coyote-time-and-input-buffering-explained"},{"title":"itch.io","url":"https://itch.io/post/10767229"},{"title":"How to Use Coyote Time to Make Your Levels More Challenging ;)","url":"https://skechyarcade-studios.itch.io/adventurous-night/devlog/782892/how-to-use-coyote-time-to-make-your-levels-more-challenging-"},{"title":"www.gamespot.com","url":"https://www.gamespot.com/articles/[another game]-dev-explains-how-they-made-their-game-feel/1100-6474775/"},{"title":"itch.io","url":"https://itch.io/post/10766350"},{"title":"4298 your players hate missed jump inputs heres why","url":"https://gamedev.net/news/4298-your-players-hate-missed-jump-inputs-heres-why/"},{"title":"Flynn: Advanced Jump Mechanics","url":"https://gamemaker.io/fr/blog/flynn-advanced-jump-mechanics"},{"title":"Input Buffering, Action Canceling, and also Forbidden Knowledge","url":"https://medium.com/@yosispring/input-buffering-action-canceling-and-also-forbidden-knowledge-47a3f8a95151"},{"title":"www.casadellibro.com.co","url":"https://www.casadellibro.com.co/libros-ebooks/matthew-harris/5078"},{"title":"itch.io","url":"https://itch.io/post/16915600"},{"title":"10 Genius Hidden Mechanics In Video Games","url":"https://whatculture.com/amp/gaming/10-genius-hidden-mechanics-in-video-games?page=2"},{"title":"Input Buffering, Coyote Time, and Game Feel","url":"https://kindatechnical.com/game-development/input-buffering-coyote-time-and-game-feel.html"},{"title":"fix godot input pick buffered press jump","url":"https://bugnet.io/blog/fix-godot-input-pick-buffered-press-jump"},{"title":"itch.io","url":"https://itch.io/post/3955704"},{"title":"Game Devlog - #0","url":"https://website-dos.pages.dev/posts/gamedev/4-21-2025"},{"title":"Idiomdrottning’s homepage","url":"https://idiomdrottning.org/coyote-time"},{"title":"itch.io","url":"https://itch.io/post/3904240"},{"title":"r/gamedev Hobbyist Sep 03 '17","url":"https://reddit.birdcat.cafe/r/gamedev/comments/6xtn68/video_game_developers_confess_their_hidden_tricks/dmifykz/?context=3"}]

The search didn't turn up any first-person developer stateme
[... 1425 more characters not shown]
```

**Sat 14 Nov 14:14:03 · Tool call: WebFetch**

```
{
 "url": "https://realdocs.pages.dev/api/UCharacterMovementComponent.MaxWalkSpeed",
 "prompt": "Quote the default value stated for MaxWalkSpeed and its description, and the page's source attribution."
}
```

**Sat 14 Nov 14:14:03 · Tool call: WebFetch**

```
{
 "url": "https://realdocs.pages.dev/api/UCharacterMovementComponent.JumpZVelocity",
 "prompt": "Quote the default value stated for JumpZVelocity and its description."
}
```

**Sat 14 Nov 14:14:03 · Tool call: WebFetch**

```
{
 "url": "https://realdocs.pages.dev/api/UCharacterMovementComponent.AirControl",
 "prompt": "Quote the default value stated for AirControl and its description."
}
```

**Sat 14 Nov 14:14:03 · Tool call: WebFetch**

```
{
 "url": "https://web.archive.org/web/2023/https://developer.valvesoftware.com/wiki/Dimensions",
 "prompt": "Quote the unit conversion (1 unit = ? inches / cm), player speed numbers for running/walking/crouching/sprinting, jump heights, player hull height and eye height."
}
```

Result:

```
Claude Code is unable to fetch from web.archive.org
```

**Sat 14 Nov 14:14:04 · Tool call: WebFetch**

```
{
 "url": "https://realdocs.pages.dev/api/UCharacterMovementComponent.GroundFriction",
 "prompt": "Quote the default value stated for GroundFriction and its description."
}
```

Result:

```
**Default value:** "Default value is 600 cm/s. Unreal units are centimetres — 600 is roughly 6 m/s."

**Description:** "The maximum ground speed in cm/s when walking. Also caps lateral movement speed while the character is airborne (falling)."

**Source attribution:** "RealDocs is an independent community resource and is not affiliated with or endorsed by Epic Games."
```

Result:

```
The default is **0.05**. The page says it is "Default is 0.05 in the stock Character Movement Component" and describes the value as a small amount of control, not zero.

The description reads: "Amount of lateral movement control available while falling, from 0 (no control) to 1 (full control at MaxWalkSpeed)."
```

Result:

```
**Default value:** "Default is 420 cm/s."

**Description:** "The instantaneous vertical velocity applied to the character when a jump begins. Higher values produce higher jumps."
```

Result:

```
The page doesn't state a default value for `GroundFriction`. Its description reads: "Friction applied while walking on the ground".
```

### Sat 14 Nov 14:15:19 · Agent (claude-sonnet-5-5)

# Feel study: movement and camera numbers with sources

[another game] 1, [another game] 3, Source SDK and [another game] constants come from the rights holders' public source files, which I read on GitHub. Only some of the UE, [another game], FOV and accessibility numbers could be confirmed, and no [another game] or Halo speeds. Search-snippet-only items are in the "Recalled" list at the end.

Unit note: Valve's 1 unit = 1.905 cm is the ratio you gave me. I could not confirm it on a fetched page (the Valve wiki returned 403). The [another game] article's own mph figures work out to the same ratio, about 1.906 cm per unit. Every cm/s figure below uses 1.905, including [another game] 3, whose unit scale no page states.

## 1. Movement speed

| Game or source | What | Number as stated | Converted | Source |
|---|---|---|---|---|
| [another game] 3, id 1999 | g_speed default | 320 u/s | 609.6 cm/s, 6.1 m/s | g_main.c, [id-Software/[another game]-III-Arena](https://github.com/id-Software/[another game]-III-Arena) |
| [another game] 3 | Crouch speed scale pm_duckScale | 0.25 | 80 u/s, 152 cm/s | bg_pmove.c, same repo |
| [another game] 3 | Swim and wade scale | 0.50 and 0.70 | | bg_pmove.c |
| [another game] 3 | Haste multiplier | speed *= 1.3 | 416 u/s | g_active.c |
| [another game] 1 | sv_maxspeed | 320 | 6.1 m/s | sv_user.c, [id-Software/[another game]](https://github.com/id-Software/[another game]) WinQuake |
| Source SDK 2013 | sv_maxspeed default | 320 | 6.1 m/s | movevars_shared.cpp, [ValveSoftware/source-sdk-2013](https://github.com/ValveSoftware/source-sdk-2013) |
| [another game] 2 | hl2_walkspeed | 150 | 285.8 cm/s, 2.86 m/s | hl2_player.cpp, same repo |
| [another game] 2 | hl2_normspeed (run) | 190 | 362 cm/s, 3.62 m/s | same |
| [another game] 2 | hl2_sprintspeed | 320 | 609.6 cm/s, 6.1 m/s | same |
| [another game] 1 (2014, not TF2) | Pilot run | 180.6 u/s, "about 7.7 MPH" | 344 cm/s, 3.44 m/s | Stephen Daly, [[another game] Raw Weapon Stats Decrypted](https://gameranx.com/updates/id/20713/article/[another game]-raw-weapon-stats-decrypted-titan-health-and-speed-revealed/), Gameranx, 5 Mar 2014 |
| [another game] 1 | Pilot sprint | 269.85 u/s, "11.5 MPH" | 514 cm/s, 5.14 m/s | same |
| [another game] 1 | Wall run max | "almost twice his sprint speed", "22 to 23 MPH" | about 10 m/s | same. The article says its own figures are unclear |
| Unreal Engine | MaxWalkSpeed default | 600 cm/s | 6.0 m/s | [RealDocs](https://realdocs.pages.dev/api/UCharacterMovementComponent.MaxWalkSpeed). This is an independent community site, not Epic |

For your rooms: [another game] and Source sprint of 6.1 m/s crosses a 30 m room in about 5 s. HL2 run of 3.6 m/s takes about 8 s.

## 2. Acceleration, friction, stopping

| Game or source | What | Number as stated | Converted or derived | Source |
|---|---|---|---|---|
| [another game] 3 | pm_accelerate, pm_airaccelerate | 10 and 1 | | bg_pmove.c |
| [another game] 3 | pm_friction, pm_stopspeed | 6 and 100 | | bg_pmove.c |
| [another game] 3 | Friction rule | `control = speed < pm_stopspeed ? pm_stopspeed : speed; drop += control*pm_friction*frametime` | | bg_pmove.c |
| [another game] 3 | Accel rule | `accelspeed = accel*frametime*wishspeed`, capped at `addspeed` | | bg_pmove.c |
| [another game] 3 | Other | water 4, fly 8, waterfriction 1, flightfriction 3, spectator 5 | | bg_pmove.c |
| [another game] 1 | sv_accelerate, sv_friction, sv_stopspeed | 10, 4, 100 | | sv_user.c, sv_phys.c |
| [another game] 1 | Air accel | same formula, wishspeed capped at 30 | | sv_user.c |
| [another game] 1 | sv_edgefriction | 2 | | sv_user.c |
| Source SDK 2013 | sv_accelerate, sv_airaccelerate | 10 and 10 (Xbox build accelerate 7) | | movevars_shared.cpp |
| Source SDK 2013 | sv_friction, sv_stopspeed | 4 and 100 | | movevars_shared.cpp |
| Source SDK 2013 | sv_wateraccelerate, sv_waterfriction | 10 and 1 | | movevars_shared.cpp |
| Source SDK 2013 | sv_stepsize | 18 | | movevars_shared.cpp |
| Unreal Engine | BrakingFrictionFactor | "2 by default for historical reasons, a value of 1 gives the true drag equation" | | [Epic Python API, CharacterMovementComponent](https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/CharacterMovementComponent) |
| [another game] | RunAccel, RunReduce, AirMult, MaxRun | 1000, 400, 0.65, 90 (pixels/s, px/s²) | Time to top speed 90/1000 = 0.09 s | Player.cs, [NoelFB/[another game]](https://github.com/NoelFB/[another game]) |

I derived the following from the formulas above:

- **[another game] 3 time to full speed (320 u/s), with friction running:** from dv/dt = 3200 - 6v, it is -ln(1 - 0.6)/6 = 0.153 s. Without friction it is 0.1 s.
- **[another game] 3 time to stop from 320 u/s:**
  - Above stopspeed, speed decays at 6 per second. From 320 down to 100 takes ln(3.2)/6 = 0.194 s.
  - Below stopspeed, speed drops linearly at 600 u/s². The last 100 takes 0.167 s.
  - Total is about 0.36 s, over about 45 u (86 cm).
- **Source (accel 10, friction 4, stopspeed 100), assuming Source uses the same friction formula:**
  - Reaching 190 u/s takes 0.128 s.
  - Stopping from 190 takes 0.41 s. Stopping from 320 takes 0.54 s.
  - I did not read Source's Friction() body, so this assumption is untested.

## 3. Jump and gravity

| Game or source | What | Number as stated | Derived | Source |
|---|---|---|---|---|
| [another game] 3 | JUMP_VELOCITY, DEFAULT_GRAVITY | 270 and 800 | Apex 45.6 u = 86.8 cm. Air time 2v/g = 0.675 s | bg_local.h, bg_public.h |
| [another game] 3 | Viewheight stand and crouch | 26 and 12 | 49.5 cm and 22.9 cm | bg_public.h |
| [another game] 3 | Step size | 18 | 34 cm | bg_local.h |
| [another game] 3 | Landing lock | `pm_time = 250` ms when previous vz < -200 | | bg_pmove.c |
| [another game] 3 | Landing damage | `delta*delta*0.0001`; events at delta > 7, 40, 60 | | bg_pmove.c |
| [another game] 3 | Fall damage | 5, or 10 for a far fall | | g_active.c |
| Source SDK, HL2 build | sv_gravity 600. Jump `flMul = 160.0` with comment "approx. 21 units" | | Apex 21.3 u = 40.6 cm. Air time 0.533 s | gamemovement.cpp, movevars_shared.cpp |
| Source SDK, other builds | sv_gravity 800. Jump `flMul = 268.328`, comment `v = sqrt(g * 2.0 * 45)` | | Apex 45 u = 85.7 cm. Air time 0.671 s | same |
| Source | Gravity split | Half applied before the move, half after. Comment: "yes, this 0.5 looks wrong, but it's not." | | gamemovement.cpp |
| Unreal Engine | JumpZVelocity default | 420 cm/s | With gravity 980 (recalled): apex 90 cm, air time 0.86 s | [RealDocs](https://realdocs.pages.dev/api/UCharacterMovementComponent.JumpZVelocity), community site |
| [another game] | Gravity, JumpSpeed, VarJumpTime | 900, -105 (px/s², px/s), 0.2 s | | Player.cs |
| [another game] | MaxFall, HalfGravThreshold | 160 and 40 | | Player.cs |
| [another game] | Half gravity at apex | "the top of your jump has half gravity applied" | | Maddy Thorson, [[another game] & Forgiveness](https://maddymakesgames.com/articles/[another game]_and_forgiveness/) (no date on page) |

Fall multiplier: I found no developer statement on higher gravity on the way down. [another game] goes the other way, with lower gravity at the apex.

## 4. Coyote time and jump buffer

| Game or source | What | Number as stated | Converted | Source |
|---|---|---|---|---|
| [another game] | JumpGraceTime (coyote) | 0.1 s, `const float JumpGraceTime = 0.1f`. Timer resets to the full value every frame on the ground | 100 ms, 6 frames at 60 fps | Player.cs |
| [another game] | Jump buffer | Code calls `Input.Jump.ConsumeBuffer()`. The buffer length is set in Input.cs, which is not in the public repo | not found | [NoelFB/[another game], Source folder](https://github.com/NoelFB/[another game]/tree/master/Source) |
| Maddy Thorson | Coyote | "You can still jump for a short time after leaving a ledge." No number | | [[another game] & Forgiveness](https://maddymakesgames.com/articles/[another game]_and_forgiveness/) |
| Maddy Thorson | Buffer | "If you press and hold the jump button a short time before landing, you will jump on the exact frame that you land." No number | | same |
| Maddy Thorson | Wall jump | "You can actually wall jump 2 pixels from a wall" (a quarter tile in a 320x180 game) | | same |
| First-person games | Developer statement of coyote or buffer | None found for [another game] 2, [another game] Eternal, Dying Light, [another game], [another game] or [another game] | | |

GMTK Platformer Toolkit defaults: not found.

## 5. Air control

| Game or source | What | Number as stated | Meaning in practice | Source |
|---|---|---|---|---|
| [another game] 3 | pm_airaccelerate | 1 | Air accel is 1/10 of ground. At wishspeed 320 that is 320 u/s², so 1 s to add one full run speed | bg_pmove.c, derived |
| [another game] 1 | Air wishspeed cap | 30 u/s with accel 10 | [another game]-style strafe turning, not forward thrust. This is derived from the code, not stated by id | sv_user.c |
| Source SDK 2013 | sv_airaccelerate | 10 | Same rule as ground accel, so air control is high. Whether Source also caps wishspeed at 30 was not read | movevars_shared.cpp |
| Unreal Engine | AirControl | 0.05, "from 0 (no control) to 1 (full control at MaxWalkSpeed)" | Weak air steering by default | [RealDocs](https://realdocs.pages.dev/api/UCharacterMovementComponent.AirControl), community site |
| [another game] | AirMult | 0.65 | Air accel is 65% of ground accel | Player.cs |

I found no developer statement on why a first-person platformer wants high air control.

## 6. FOV

| Game or source | What | Number as stated | Horizontal at 16:9 | Source |
|---|---|---|---|---|
| Formula | H = 2·atan(tan(V/2)·w/h) | | | [Wikipedia, Field of view in video games](https://en.wikipedia.org/wiki/Field_of_view_in_video_games) |
| [another game] (derived) | 90° horizontal at 4:3 | | V = 73.74°, H at 16:9 = 106.26° | derived from the formula |
| [another game] 3 | `cg_fov` is horizontal (fov_x). Clamped 1 to 160. `DF_FIXED_FOV` forces 90. Vertical is derived from the viewport size | | | cg_view.c |
| Console and PC rule of thumb | "around 60" for console, "90 to 100" for PC | not labelled horizontal or vertical | | Wikipedia page above |
| Halo Infinite | Settings screenshot shows FOV set to 97° | | | [Xbox Accessibility Guideline 117](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117) |
| [another game] | FOV slider max 110° | | | same |
| Xbox guideline | "Provide adjustable field of view settings." Low FOV "can help reduce feelings of motion sickness". Halo's own wording says higher angles give a "fishbowl" effect | | | same |

Other FOV defaults and ranges: not confirmed (see Recalled).

## 7. Bob

| Game or source | What | Number as stated | Derived | Source |
|---|---|---|---|---|
| [another game] 1 | cl_bob, cl_bobcycle, cl_bobup | 0.02, 0.6, 0.5 | Cycle length 0.6 s | view.c |
| [another game] 1 | Bob formula | `bob = speed*cl_bob`, then `bob*0.3 + bob*0.7*sin(cycle)`, clamped to -7..4 | At 320 u/s, 6.4 raw gives -2.6 to +4 u (-5 to +7.6 cm) | view.c |
| [another game] 3 | Vertical bob cap | 6 units (`bob > 6`) | 11.4 cm | cg_view.c |
| [another game] 3 | Pitch and roll bob | Use speed with a floor of 200. Roll sign flips each half cycle. Crouched, pitch and roll bob are ×3 | | cg_view.c |
| [another game] 3 | bobmove per ms | 0.3 walk, 0.4 run, 0.5 duck. bobCycle wraps at 256 | At run, 256/0.4 = 640 ms per wrap (derived) | bg_pmove.c |
| Xbox guideline | "Avoid any repetitive side-to-side or up-and-down on-screen movement, except that which is core to game play." Offer an option to turn off camera shake and bob | | | [XAG 117](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117) |
| Xbox guideline examples | Elder Scrolls Online head-bob slider. Halo Infinite per-effect sliders 0 to 100% (radial blur, screen shake, speed lines). Cyberpunk 2077 "additive camera motions" | | | same |

## 8. Roll when strafing

| Game or source | What | Number as stated | Derived | Source |
|---|---|---|---|---|
| [another game] 1 | cl_rollangle, cl_rollspeed | 2.0° and 200 | Roll scales linearly with side speed up to 200 u/s, then holds at 2.0° | view.c |
| [another game] 1 | Damage view kick | v_kicktime 0.5 s, v_kickroll 0.6, v_kickpitch 0.6 | | view.c |
| [another game] 1 | Idle sway | v_idlescale 0 | Off by default | view.c |

## 9. Landing dip, kick, shake

| Game or source | What | Number as stated | Source |
|---|---|---|---|
| [another game] 3 | Landing dip | Eased down over LAND_DEFLECT_TIME, back over LAND_RETURN_TIME (values not on the page I read). The old fall-kick code is disabled (`#if 0`) | cg_view.c |
| [another game] 3 | Damage kick | Ramps in over DAMAGE_DEFLECT_TIME, fades over DAMAGE_RETURN_TIME. Screen blend alpha 200 fading to 0 | cg_view.c |
| [another game] 3 | Stair step smoothing | Eased over STEP_TIME | cg_view.c |
| Source SDK | Jump ledge rule | Cannot jump during the unduck transition | gamemovement.cpp |
| Squirrel Eiserloh, GDC 2016, "Math for Game Programmers: Juicing Your Cameras With Math" | Trauma-squared and max angle values | Not found. A blog recap says use rotational shake in 3D and rotation plus translation in 2D | [GDC Vault listing](https://gdcvault.com/play/1023146/Math-for-Game-Programmers-Juicing) (listing only, talk not read) |

## 10. Mouse

| Game or source | What | Number as stated | Source |
|---|---|---|---|
| Source SDK 2013 | m_rawinput default | 1, "Use Raw Input for mouse input." A one-time reset forces it to 1 | in_mouse.cpp |
| Source SDK 2013 | m_filter, m_customaccel, m_mouseaccel1 | 0, 0, 0. m_filter averages the mouse over 2 frames when set to 1 | in_mouse.cpp |
| Source SDK 2013 | sensitivity, m_yaw, m_pitch | 3, 0.022, 0.022 | in_mouse.cpp |
| Xbox guideline | Players should be able to adjust horizontal and vertical look sensitivity and turn off auto camera movement | | [XAG 117](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117) |
| Xbox guideline, linked article | "Avoid (or provide option to disable) any difference between controller movement and camera movement, such as weapon/walk bobbing or mouse smoothing" | | linked from XAG 117, article itself not read |

Derived: sensitivity 3 × 0.022 = 0.066° per count. At 400 counts per inch (my assumption) a full 360° turn takes about 13.6 inches of mouse travel.

No developer statements on "no acceleration and no smoothing" were found beyond the Source defaults above.

## Recalled, not confirmed on a fetched page

These appeared only in search-result summaries, or are from memory.

- **[another game] FOV:** the slider runs 80 to 103 and is vertical, with 103 possibly the default (PC Gamer and a Blizzard forum thread, via search summary). One guide says it is fixed at 90. The sources conflict, so I computed no 16:9 value.
- **Halo Infinite FOV:** default 78, range 65 to 120 (gaming-news guides, via search). I did not confirm this against an official source.
- **Destiny 2 PC FOV:** horizontal, range 55 to 105, default 85 (a fan survey site, via search).
- **[other-app] FOV:** fixed at 103 (several guides, via search). I did not confirm whether it is horizontal.
- **[another game] 1 and [another game] 3 default fov:** 90, which I recalled. A [another game] wiki snippet suggests [another game] 1 shows about 120 at 16:9 (unclear and unverified).
- **[another game] coyote:** "5 frames" per a [another game] wiki snippet. That conflicts with the 0.1 s (6 frames) in Player.cs, which I trust more.
- **[another game] 1 jump:** velocity z += 270 from memory. `sv_user.c` did not contain it.
- **Valve units:** 1 unit = 0.75 inch = 1.905 cm.
- **[another game] 2 FOV:** fov_desired default 75, which I recalled. A search found nothing to confirm it.
- **CS FOV:** a Steam thread disputes whether CS2 keeps 106.26° at 16:9.
- **Source `cl_bob` values:** a community gist lists `cl_bob` 1, `cl_bobup` 0.5, `cl_bobcyclemax` 0.45 for SDK 2013 multiplayer. GoldSrc `cl_bob` is 0.01 and `cl_bobcycle` 0.8 per a speedrun wiki snippet. I confirmed none against the SDK source.
- **UE defaults:** I could not confirm these on any page: MaxAcceleration 2048, BrakingDecelerationWalking 2048, GroundFriction 8, GravityScale 1, and world gravity -980. The Epic page states none of them, and a tutorial page uses its own values (500, 2048, 2000, 8, 0.2, 700).
- **[another game] 2016:** Marty Stratton said you "generally move faster, or as fast, as the enemies" (via search). CTO Robert Duffy said development began by taking the RAGE movement framework and doubling it (PC Gamer, via search). No speed number was found. I did not locate the GDC 2018 talk "Embracing Push Forward Combat in [another game]", given by Jake Campbell and Kurt Loudy, not Jason O'Donnell (see the [GDC Vault listing](https://gdcvault.com/play/1024940/Embracing-Push-Forward-Combat-in)).
- **[another game] 2 and Apex:** no real speed table found. A student fan project lists slide boost 180 to 380, but that is its own tuning, not Respawn's.
- **Not searched:** [another game] and [another game] speeds, Halo and [another game] base speeds in m/s, the UE first-person template values, and [another game], [another game] and [another game].

## Pages that failed

- developer.valvesoftware.com (Dimensions, Dimensions for HL2 and CS:S, Sv_accelerate): 403.
- pcgamingwiki.com (glossary FOV, [another game] Eternal, [another game], [another game]): 403.
- support.halowaypoint.com FOV article: 403.
- gamedeveloper.com [another game] designer interview: 403.
- web.archive.org: blocked in this tool.
- pcgamer.com [another game] FOV slider: only the headline came back.
- Epic C++ API page for UCharacterMovementComponent: no content returned. The Python API page was readable but gives no defaults except BrakingFrictionFactor.
- gameaccessibilityguidelines.com `?p=21`: 404.
- [another game] `Source/Input.cs`: 404 (the repo has only Player and PICO-8 folders).
- Q3 `bg_pmove.c` summary: the fetch summarizer cut some numbers, so the Q3 constants above come from my targeted follow-up fetches of the same file.
