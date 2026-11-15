# Transcript: lane-dlss1

Session 680a7dbf-7ec3-4ad2-888f-a07720c19df4. Exported by `tools/export_transcripts.py`; entries from Fri 13 Nov 2026 05:41 SGT on. Times are Singapore time. See the README for what is removed.

### Sat 14 Nov 19:17:56 · Brief from the orchestrating agent

Act as the research sub-agent for this task.

GLASSBOX-MEGAJAM-2026 lane=dlss1

You find out how to put NVIDIA DLSS into the jam game SUPERCUT (Unreal Engine 5.9 MegaJam Preview, a C++ project) and write the plan. This round is research and a plan: you change nothing in the game. Do the work yourself; start no subagents.

## Why

The game is an entry in the 2026 Epic AI MegaJam (deadline Monday 16 Nov 2026, 09:59 Singapore time; feature stop Sunday afternoon). One prize, the "Render Royalty: NVIDIA RTX Award", goes to an Unreal entry "using an NvRTX feature, DLSS 4.5 or NVIDIA ACE", and the entry form has NVIDIA questions to answer. The owner said today, while showing a reference game's video settings: "We'll have DLSS so we are eligible for that prize." Public starting point: https://developer.nvidia.com/game-engines/unreal-engine

## Facts about our setup

- Engine: `D:\UE\UE_5.9` on this PC (an installed build of the 5.9 MegaJam Preview, not a source build). Project: `D:\UE\Projects\Supercut59` (read only for you). The project builds from the command line with `Tools\build.ps1` and packages with `Tools\package.cmd`; there is no hand-edited map, the game builds its rooms by code.
- This PC has an AMD card (RX 9070 XT). The only PC of ours with an NVIDIA RTX card is the build-farm PC "[pc-b]" (RTX 4080 Super); `unreal\megajam-2026\FARM.md` in `[notes]\` describes how lanes build, package and run there. Read it; do not run anything there in this round.
- The judges' PC is unknown. The game must start and run exactly as today on a PC without an NVIDIA card. DLSS is an option the player can turn on where it is supported.
- The game has a post-process look that matters: when the player claps a clapperboard, the scene freezes and turns into a pencil-sketch look (a post-process material with outlines and hatching). Read `unreal\megajam-2026\lanes\feel2\HANDOFF.md` and the post-process code under `D:\UE\Projects\Supercut59\Source\Supercut` to see how it is made.
- Lighting: every light is movable; read the project's `Config\DefaultEngine.ini` for the renderer settings in use (Lumen or not, anti-aliasing method, Nanite, ray tracing).
- A settings menu is being designed by another lane; it will need a DLSS mode row.

## Job: write `unreal\megajam-2026\lanes\dlss1\PLAN.md`

1. **What counts for the award.** From NVIDIA's and Epic's public pages for this jam: the exact wording, what "DLSS 4.5" covers (Super Resolution, DLAA, Frame Generation, Multi Frame Generation, Ray Reconstruction, Reflex), whether Super Resolution alone qualifies, and what the NVIDIA questions on the form ask if that is public. Quote and link each source. Say what you could not find.
2. **Is there a DLSS plugin that works with Unreal 5.9 Preview.** Which plugin versions exist, which engine versions each supports, whether one is built for 5.9 or the jam's preview, and if not whether the newest one's source compiles against an installed 5.9 (look at how the plugin gates engine versions in its `.uplugin` and `Build.cs`, from public documentation, release notes, forum posts and public repositories). Check what the engine folder already ships: look under `D:\UE\UE_5.9\Engine\Plugins` for anything named DLSS, NGX, Streamline, NVIDIA or Reflex, and read those `.uplugin` files. State what is verified on our disk and what is only read on the web.
3. **What a person has to do by hand.** Getting the plugin means accepting NVIDIA's licence, which agents here never do. Give the owner the exact page, the exact file to download, and the folder to save it in (`D:\UE\dl\dlss\`), and anything else only a person can do (an NVIDIA developer sign-in, an application ID request, driver version on [pc-b]). If no download is needed because the engine ships it, say so. Also read the licence's terms that touch a free jam entry (redistribution of the DLLs, the logo and attribution requirements, any debug watermark) from the public licence text, and list what we would have to do.
4. **The integration, step by step**, for a C++ project built by scripts: where the plugin goes (engine or project `Plugins\`), the `.uproject` and `Build.cs` changes, which settings and console variables switch DLSS modes at run time (names checked against the plugin's own documentation or headers, not from memory: these change between versions), how the game asks at run time whether DLSS is supported and why not, what happens on an AMD or Intel card (the option hidden or greyed, no crash, no missing DLL at start), what it adds to the package size (the zip limit is 1 GB, the package is about 250 MB), and which of our build farm PCs can compile it.
5. **Our sketch look and DLSS.** A temporal upscaler changes where post-process materials run and at what resolution. Say where our sketch material sits in the post-process chain, what an upscaler does to thin outlines and hatching (shimmer, softness, ghosting when the frozen scene is still and the player moves), and what to set to keep it clean (screen percentage, the material's blendable location, DLAA instead of upscaling, sharpening).
6. **How we prove it on [pc-b]**: the command line to start the packaged game with DLSS on, the log line or stat that shows DLSS is active and in which mode, a screenshot pair (off, on) with frame times from the game's scripted run (`Tools\run_demo.ps1`, described in FARM.md), and the check that the scripted run prints the same result line with DLSS on as off.
7. **Cost and risk**: hours for the smallest version that qualifies (a DLSS mode option: off, DLAA, quality, balanced, performance), hours for Frame Generation and Reflex on top, the ways this can break the build in the last day, and your recommendation: do it, do the smallest version only, or skip.
8. A ready-to-use brief for a build lane, as `BUILD_BRIEF.md`, written so that an agent with no other context can do the integration in its own git worktree once the owner has done the hand steps.

## Rules

- Write only in `[notes]\unreal\megajam-2026\lanes\dlss1\` (`PLAN.md`, `BUILD_BRIEF.md`, `LOG.md` with clock times from `date`, `HANDOFF.md`).
- Web reading is fine. **No downloads of plugins, SDKs or installers, no sign-in anywhere, no licence or terms accepted, no forms submitted.** If a page asks for any of those, stop there and write down what it asks.
- Do not edit, build or run the game or the engine. No git command that writes anywhere under `D:\UE`. Nothing on any other PC in this round.
- Unreal 5.9 and current DLSS are newer than your training: a plugin name, setting or console variable is a guess until you have seen it in current documentation or in a file on disk. Mark each as "seen in <source>" or "not verified".
- Do not read or print: anything under a `memory` folder, a file named `JAM.md`, files ending in `API.md`, `.env` files, the Epic Games Launcher logs or settings, other projects' folders. Do not print account, user or computer names or emails (no `ls -l`, `dir /q`, `whoami`, `hostname`), and never list folders under the user profile.
- No sound aloud, no real keyboard or mouse input, no installs, no admin prompts.
- Do not end your turn while a step you need is still running.
- Final report: can we qualify and with what, what the owner must do by hand (numbered, with links), hours for the smallest version, the three biggest risks, your recommendation, and what you could not verify. Plain words, short sentences, no em dashes. Link local files as markdown links with the full path in angle brackets.

**Sat 14 Nov 19:18:01 · Tool call: Bash** (Show date and list jam folders)

```
date; ls "[notes]/unreal/megajam-2026/"; ls "[notes]/unreal/megajam-2026/lanes/" ; ls "[notes]/unreal/megajam-2026/lanes/dlss1" 2>&1
```

Result:

```
Exit code 2
Sat Nov 14 19:18:03 MPST 2026
FARM.md
GAME.md
JAM.md
SUBMISSION.md
_scrapped_floodline
farm
lanes
review_14nov.html
rules
PROPS_REALISTIC_SPEC.md
anim1
animref1
arms1
arms2
arms3
artdirection
assetaudit
audio1
audiowire
bshelf
core
enemies
fabdl1
fablist1
farm1
feel1
feel2
feel3
feel4
feel5
feelstudy
figin
figure
first1
fix2
gen1
hall1
held1
jump1
levels1
light1
mega1
mix1
models
models2
music
onboard1
pctest
pctest2
perf2
probe59
props
props1
props2
puzzlerooms
puzzles
rodin1
rodin2
rodin3
rodin4
rodin5
rooms
run
setA
setB
setC
sfx1
shell1
sketchfx
slice
slice2
sound
textures
uiref1
vfx1
video1
view1
ls: cannot access '[notes]/unreal/megajam-2026/lanes/dlss1': No such file or directory
```

**Sat 14 Nov 19:18:07 · Tool call: Bash** (Create lane folder, size key docs, list engine plugins)

```
mkdir -p "[notes]/unreal/megajam-2026/lanes/dlss1"; cd "[notes]/unreal/megajam-2026"; wc -l FARM.md lanes/feel2/HANDOFF.md SUBMISSION.md; ls /d/UE/UE_5.9/Engine/Plugins;
```

Result:

```
154 FARM.md
  237 lanes/feel2/HANDOFF.md
  102 SUBMISSION.md
  493 total
2D
AI
Animation
AudioGameplay
AudioGameplayVolume
AudioInsights
AudioInsightsRuntime
AudioModulationInsights
AutomationControllerRpc
BaseMaterial
BlueprintFileUtils
Bridge
Cameras
ChaosCloth
ChaosClothAsset
ChaosClothAssetDataflowNodes
ChaosClothAssetEditor
ChaosClothAssetEditorCore
ChaosClothAssetUsdDataflowNodes
ChaosInsights
ChaosOutfitAsset
ChaosVD
Chooser
CmdLinkServer
Compositing
Compression
Dataflow
DataflowVolumetricPlugin
DerivedDataBuildController
Developer
DiscoveryBeaconReceiver
Editor
EnginePlugin_A
EnhancedInput
Enterprise
Experimental
FX
Fab
FastBuildController
GameInputWindows
GaussianSplat
Importers
Interchange
IoStoreInsights
JsonBlueprintUtilities
LightWeightInstancesEditor
MassInsights
Media
MegascansPlugin
MemoryUsageQueries
MeshPainting
Messaging
MetaHuman
ModularTestFramework
ModularTestResolver
MovieScene
Mutable
NNE
NetcodeUnitTest
Online
PCG
PCGInterops
Performance
[another game]
Protocols
RPCBase
RenderGraphInsights
RenderTraceInsights
Runtime
ScriptGeneratorPlugin
ScriptPlugin
Slate
SubtitlesAndClosedCaptions
Tests
TextureGraph
TraceUtilities
UbaController
VirtualProduction
Web
WorldMetrics
WorldStreamingInsights
XGEController
```

**Sat 14 Nov 19:18:14 · Tool call: Bash** (Search engine folder for NVIDIA plugins)

```
cd /d/UE/UE_5.9/Engine; echo "--- name search"; find Plugins Binaries/ThirdParty Source/ThirdParty -maxdepth 4 -iname "*dlss*" -o -maxdepth 4 -iname "*ngx*" -o -maxdepth 4 -iname "*streamline*" -o -maxdepth 4 -iname "*nvidia*" -o -maxdepth 4 -iname "*reflex*" -o -maxdepth 4 -iname "*nvapi*" 2>/dev/null | head -50; echo "--- uplugin search"; find Plugins -name "*.uplugin" | grep -iE "dlss|ngx|streamline|nvidia|reflex|nv|fsr|xess|upscal" | head; echo "--- build version"; cat Build/Build.version
```

Result:

```
--- name search
Plugins/Runtime/Nvidia
Plugins/Runtime/Nvidia/Reflex
Plugins/Runtime/Nvidia/Reflex/Reflex.uplugin
Binaries/ThirdParty/NVIDIA
Binaries/ThirdParty/nvTextureTools/NVIDIAnvDXT.tps
Binaries/ThirdParty/PhysX3/NVIDIAPhysXRedistributables.tps
Source/ThirdParty/Licenses/NVAPI_v615.license
Source/ThirdParty/Licenses/NVIDIA Aftermath SDK_v2025.5.0.251114 (a5c10ac5-23d6-4a87-9630-a522f9e02023).license
Source/ThirdParty/Licenses/NVIDIA-RIVERMAX_License.txt
Source/ThirdParty/Licenses/NvidiaGameworks_License.docx
Source/ThirdParty/Licenses/nvidia_cutlass_v3.1.0.license
Source/ThirdParty/Licenses/nvidia_cutlass_v3.5.1.license
Source/ThirdParty/Licenses/Nvidia_Geforce_NOW_SDK_License.txt
Source/ThirdParty/Licenses/nvidia_sdk_download.license
Source/ThirdParty/Licenses/nvidia_sdk_download_v12.2.1.license
Source/ThirdParty/Licenses/nvidia_sdk_download_v3.11.0.license
Source/ThirdParty/NVIDIA
Source/ThirdParty/NVIDIA/GeForceNOW/Nvidia_Geforce_NOW_SDK_LICENSE.tps
Source/ThirdParty/NVIDIA/NVaftermath/NVIDIA Aftermath SDK_v2025.5.0.251114 (e2e87085-29ce-4eef-9a5c-7496689bcf5b).tps
Source/ThirdParty/NVIDIA/nvapi
Source/ThirdParty/NVIDIA/nvapi/aarch64/nvapia64.lib
Source/ThirdParty/NVIDIA/nvapi/amd64/nvapi64.lib
Source/ThirdParty/NVIDIA/nvapi/NVAPI.Build.cs
Source/ThirdParty/NVIDIA/nvapi/nvapi.h
Source/ThirdParty/NVIDIA/nvapi/NvApiDriverSettings.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_interface.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_common.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_d3dext.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_salend.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_salstart.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_sli.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_stereo.h
Source/ThirdParty/NVIDIA/nvapi/nvapi_lite_surround.h
Source/ThirdParty/NVIDIA/nvapi/NVAPI_v615 .tps
Source/ThirdParty/NVIDIA/nvDecode/NVIDIAVideoCodecSDK.tps
Source/ThirdParty/NVIDIA/nvEncode/NVIDIAVideoCodecSDK.tps
Source/ThirdParty/nvTextureTools/NVIDIAnvDXT.tps
Source/ThirdParty/nvTriStrip/NVIDIAnvTriStrip.tps
--- uplugin search
Plugins/AI/EnvironmentQueryEditor/EnvironmentQueryEditor.uplugin
Plugins/Developer/UnrealCanvas/UnrealCanvasAnnotations/UnrealCanvasAnnotations.uplugin
Plugins/Developer/UnrealCanvas/UnrealCanvasBridge/UnrealCanvasBridge.uplugin
Plugins/Developer/UnrealCanvas/UnrealCanvasGraph/UnrealCanvasGraph.uplugin
Plugins/Experimental/AVCodecs/NVCodecs/NVCodecs.uplugin
Plugins/Experimental/CommonConversation/CommonConversation.uplugin
Plugins/Experimental/Liv
[... 530 more characters not shown]
```

**Sat 14 Nov 19:18:27 · Tool call: Bash** (Read engine Reflex plugin and NVIDIA binaries)

```
cd /d/UE/UE_5.9/Engine; cat Plugins/Runtime/Nvidia/Reflex/Reflex.uplugin; find Plugins/Runtime/Nvidia -type f | grep -v Intermediate | head -40; echo ---; find Binaries/ThirdParty/NVIDIA -maxdepth 3 | head -30; echo; grep -rli "dlss\|streamline\|ngx" Plugins/Runtime/Nvidia --include=*.h --include=*.cs --include=*.cpp 2>/dev/null | head
```

Result:

```
{
	"FileVersion" : 3,
	
	"FriendlyName" : "Reflex",
	"Version" : 1,
	"VersionName" : "1.6",
	"Description" : "NVIDIA Reflex Latency Tracking and Tick Rate Handling",
	"Category" : "Performance",
	"CreatedBy" : "Epic Games, Inc.",
	"CreatedByURL" : "https://epicgames.com",
	"EnabledByDefault" : false,
	
	"Modules" :
	[
		{
			"Name" : "Reflex",
			"Type" : "ClientOnly",
			"PlatformAllowList" : [ "Win64" ],
			"PlatformArchitectureDenyList" :
			[
				"Win64:arm64",
				"Win64:arm64ec"
			]
		}
	]
}
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Binaries/Win64/UnrealEditor-GeForceNOWWrapper.dll
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Binaries/Win64/UnrealEditor.modules
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Binaries/Win64/UnrealEditor.uclasses
Plugins/Runtime/Nvidia/GeForceNOWWrapper/GeForceNOWWrapper.uplugin
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/GeForceNOWWrapper.Build.cs
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Private/GeForceNOWActionZoneProcessor.cpp
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Private/GeForceNOWWrapper.cpp
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Private/GeForceNOWWrapperModule.cpp
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Private/GeForceNOWWrapperPrivate.h
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Public/GeForceNOWActionZoneProcessor.h
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Public/GeForceNOWWrapper.h
Plugins/Runtime/Nvidia/GeForceNOWWrapper/Source/Public/IGeForceNOWWrapperModule.h
Plugins/Runtime/Nvidia/Reflex/Binaries/Win64/UnrealEditor-Reflex.dll
Plugins/Runtime/Nvidia/Reflex/Binaries/Win64/UnrealEditor.modules
Plugins/Runtime/Nvidia/Reflex/Binaries/Win64/UnrealEditor.uclasses
Plugins/Runtime/Nvidia/Reflex/Reflex.uplugin
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexBlueprint.cpp
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexLatencyMarkers.cpp
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexMaxTickRateHandler.cpp
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexModule.cpp
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexModule.h
Plugins/Runtime/Nvidia/Reflex/Source/Private/ReflexStatsLatencyMarkers.cpp
Plugins/Runtime/Nvidia/Reflex/Source/Public/ReflexBlueprint.h
Plugins/Runtime/Nvidia/Reflex/Source/Public/ReflexLatencyMarkers.h
Plugins/Runtime/Nvidia/Reflex/Source/Public/ReflexMaxTickRateHandler.h
Plugins/Runtime/Nvidia/Reflex/Source/Public/ReflexStatsLatencyMarkers.h
Plugins/Runtime/Nvidia/Reflex/Source/Reflex.Build.cs
Plugins/Runtime/Nvidia/Re
[... 657 more characters not shown]
```

**Sat 14 Nov 19:18:32 · Tool call: Bash** (Read Reflex plugin build file and cvars)

```
cd /d/UE/UE_5.9/Engine/Plugins/Runtime/Nvidia/Reflex/Source; cat Reflex.Build.cs; grep -n "TEXT(\"[a-z]\.\|AutoConsoleVariable\|SetSleepMode\|NvAPI_D3D_Sleep\|bLowLatency\|UFUNCTION" -r . | head -40
```

Result:

```
// Copyright Epic Games, Inc. All Rights Reserved.

using System.IO;

namespace UnrealBuildTool.Rules
{
	public class Reflex : ModuleRules
	{
		public Reflex(ReadOnlyTargetRules Target) : base(Target)
		{
			PublicDependencyModuleNames.AddRange([
				"Core",
				"Engine",
				"RHI",
				"CoreUObject",
				"SlateCore",
				"Slate"
			]);

			PrivateIncludePathModuleNames.AddRange([
				"D3D11RHI",
				"D3D12RHI"
			]);

			// Grab NVAPI
			AddEngineThirdPartyPrivateStaticDependencies(Target, "NVAPI");

			// Grab ReflexStat
			PrivateIncludePaths.Add(Path.Combine(ModuleDirectory, "ThirdParty"));
		}
	}
}
./Private/ReflexLatencyMarkers.cpp:25:static FAutoConsoleVariableRef CVarDisableLatencyMarkers(
./Private/ReflexLatencyMarkers.cpp:26:	TEXT("t.DisableLatencyMarkers"),
./Private/ReflexMaxTickRateHandler.cpp:24:static FAutoConsoleVariableRef CVarDisableCustomTickRateHandler(
./Private/ReflexMaxTickRateHandler.cpp:25:	TEXT("t.DisableCustomTickRateHandler"),
./Private/ReflexMaxTickRateHandler.cpp:31:static FAutoConsoleVariableRef CVarDisableLatencyMarkerOptimize(
./Private/ReflexMaxTickRateHandler.cpp:32:	TEXT("t.DisableLatencyMarkerOptimize"),
./Private/ReflexMaxTickRateHandler.cpp:38:static FAutoConsoleVariableRef CVarEnableReflexInEditor(
./Private/ReflexMaxTickRateHandler.cpp:39:	TEXT("t.EnableReflexInEditor"),
./Private/ReflexMaxTickRateHandler.cpp:104:				params.bLowLatencyMode = bLowLatencyMode;
./Private/ReflexMaxTickRateHandler.cpp:105:				params.bLowLatencyBoost = bBoost;
./Private/ReflexMaxTickRateHandler.cpp:109:				status = NvAPI_D3D_SetSleepMode(FReflexModule::GetD3DDevice(), &params);
./Private/ReflexMaxTickRateHandler.cpp:112:				if (bLowLatencyMode && (status != NVAPI_OK))
./Private/ReflexMaxTickRateHandler.cpp:117:					bLowLatencyMode = false;
./Private/ReflexMaxTickRateHandler.cpp:128:				StatusSleep = NvAPI_D3D_Sleep(Unknown);
./Private/ReflexMaxTickRateHandler.cpp:135:			// When disabled, if we ever called SetSleepMode, we need to clean up after ourselves
./Private/ReflexMaxTickRateHandler.cpp:141:				params.bLowLatencyMode = false;
./Private/ReflexMaxTickRateHandler.cpp:142:				params.bLowLatencyBoost = false;
./Private/ReflexMaxTickRateHandler.cpp:145:				status = NvAPI_D3D_SetSleepMode(FReflexModule::GetD3DDevice(), &params);
./Private/ReflexMaxTickRateHandler.cpp:146:				UE_LOGF(LogMaxTickRateHandler, Log, "SetSleepMode clean up");
./Private/ReflexMaxTickRateHandler.cpp:152:				bLowLatencyMode = true;
./
[... 1029 more characters not shown]
```

### Sat 14 Nov 19:18:35 · Agent (claude-opus-5-5)

I'm partway in. Found so far: the 5.9 engine ships Epic's own NVIDIA Reflex plugin but no DLSS. Next I'm reading the project config and the jam's NVIDIA award pages.

**Sat 14 Nov 19:18:36 · Tool call: Bash** (Read Reflex blueprint API and module init)

```
cd /d/UE/UE_5.9/Engine/Plugins/Runtime/Nvidia/Reflex/Source; sed -n 1,60p Public/ReflexBlueprint.h; grep -n "Reflex\|LowLatency\|GetEnabled\|Supported\|NvAPI_Initialize\|IsRHIDeviceNVIDIA" Private/ReflexModule.cpp | head -30
```

Result:

```
﻿// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "Kismet/BlueprintFunctionLibrary.h"

#include "ReflexBlueprint.generated.h"

#define UE_API REFLEX_API

UENUM(BlueprintType)
enum class EReflexMode : uint8
{
	Disabled = 0 UMETA(DisplayName="Disabled"),
	Enabled = 1 UMETA(DisplayName="Enabled"),
	EnabledPlusBoost = 3 UMETA(DisplayName="Enabled + Boost")
};


UCLASS(MinimalAPI)
class UReflexBlueprintLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_UCLASS_BODY()

	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API bool GetReflexAvailable();

	UFUNCTION(BlueprintCallable, Category="Reflex")
	static UE_API void SetReflexMode(const EReflexMode Mode);
	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API EReflexMode GetReflexMode();

	UFUNCTION(BlueprintCallable, Category="Reflex")
	static UE_API void SetFlashIndicatorEnabled(const bool bEnabled);
	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API bool GetFlashIndicatorEnabled();
	
	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API float GetGameToRenderLatencyInMs();
	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API float GetGameLatencyInMs();
	UFUNCTION(BlueprintPure, Category="Reflex")
	static UE_API float GetRenderLatencyInMs();
};

#undef UE_API
3:#include "ReflexModule.h"
10:IMPLEMENT_MODULE(FReflexModule, Reflex);
12:void FReflexModule::StartupModule()
14:	ReflexMaxTickRateHandler = MakeUnique<FReflexMaxTickRateHandler>();
15:	if (ReflexMaxTickRateHandler.IsValid())
17:		ReflexMaxTickRateHandler->Initialize();
18:		IModularFeatures::Get().RegisterModularFeature(ReflexMaxTickRateHandler->GetModularFeatureName(), ReflexMaxTickRateHandler.Get());
21:	ReflexLatencyMarker = MakeUnique<FReflexLatencyMarkers>();
22:	if (ReflexLatencyMarker.IsValid())
24:		ReflexLatencyMarker->Initialize();
25:		IModularFeatures::Get().RegisterModularFeature(ReflexLatencyMarker->GetModularFeatureName(), ReflexLatencyMarker.Get());
28:	ReflexStatsLatencyMarker = MakeUnique<FReflexStatsLatencyMarkers>();
29:	if (ReflexStatsLatencyMarker.IsValid())
31:		ReflexStatsLatencyMarker->Initialize();
32:		IModularFeatures::Get().RegisterModularFeature(ReflexStatsLatencyMarker->GetModularFeatureName(), ReflexStatsLatencyMarker.Get());
36:void FReflexModule::ShutdownModule()
38:	if (ReflexMaxTickRateHandler.IsValid())
40:		IModularFeatures::Get().UnregisterModularFeature(ReflexMaxTickRateHandler->GetModularFeatureName(), ReflexMaxTickRateHandler.Get());
43:	if (ReflexLat
[... 428 more characters not shown]
```

### Sat 14 Nov 19:18:39 · Agent (claude-opus-5-5)

Now project config, the post-process code and FARM.md.

**Sat 14 Nov 19:18:41 · Tool call: Bash** (Read uproject and renderer settings)

```
cd /d/UE/Projects/Supercut59; ls; cat *.uproject; echo ----; grep -nE "^\[|r\.|Lumen|AntiAliasing|Nanite|RayTrac|DefaultGraphicsRHI|D3D|ScreenPercentage|TSR|TemporalAA|Upscal|VirtualShadow" Config/DefaultEngine.ini | head -80
```

Result:

```
Art
Audio
Binaries
Build
Config
Content
DerivedDataCache
Intermediate
Saved
Script
Source
Supercut.uproject
Tools
{
	"FileVersion": 3,
	"EngineAssociation": "5.9",
	"Category": "",
	"Description": "SUPERCUT. A first-person shooter where a clapperboard stops the scene.",
	"Modules": [
		{
			"Name": "Supercut",
			"Type": "Runtime",
			"LoadingPhase": "Default"
		}
	],
	"Plugins": [
		{
			"Name": "ModelingToolsEditorMode",
			"Enabled": true,
			"TargetAllowList": [
				"Editor"
			]
		}
	]
}
----
1:[/Script/EngineSettings.GameMapsSettings]
6:[/Script/Engine.RendererSettings]
7:r.AllowStaticLighting=False
8:r.Shadow.Virtual.Enable=1
9:r.DynamicGlobalIlluminationMethod=1
10:r.ReflectionMethod=1
11:r.GenerateMeshDistanceFields=True
12:r.DefaultFeature.MotionBlur=False
14:r.CustomDepth=3
16:[/Script/WindowsTargetPlatform.WindowsTargetSettings]
17:DefaultGraphicsRHI=DefaultGraphicsRHI_DX12
18:-D3D12TargetedShaderFormats=PCD3D_SM5
19:+D3D12TargetedShaderFormats=PCD3D_SM6
20:-D3D11TargetedShaderFormats=PCD3D_SM5
21:+D3D11TargetedShaderFormats=PCD3D_SM5
23:[/Script/AndroidFileServerEditor.AndroidFileServerRuntimeSettings]
37:[/Script/Engine.AudioSettings]
43:[/Script/Engine.Engine]
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:18:42 · Tool call: Bash** (Read build farm doc)

```
cat "[notes]/unreal/megajam-2026/FARM.md"
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
[... 8516 more characters not shown]
````

**Sat 14 Nov 19:18:47 · Tool call: Bash** (Full renderer config and AA references)

```
cd /d/UE/Projects/Supercut59; sed -n 1,50p Config/DefaultEngine.ini; ls Config; grep -rniE "AntiAliasing|ScreenPercentage|TSR|Upscal|DLSS" Config Source Tools 2>/dev/null | head -30
```

Result:

```
[/Script/EngineSettings.GameMapsSettings]
GameDefaultMap=/Game/Maps/Boot.Boot
EditorStartupMap=/Game/Maps/Boot.Boot
GlobalDefaultGameMode=/Script/Supercut.SupercutGameMode

[/Script/Engine.RendererSettings]
r.AllowStaticLighting=False
r.Shadow.Virtual.Enable=1
r.DynamicGlobalIlluminationMethod=1
r.ReflectionMethod=1
r.GenerateMeshDistanceFields=True
r.DefaultFeature.MotionBlur=False
; The frozen-time sketch reads the custom stencil (figures, signals, held things). 3: stencil writes on (SceneUtils.cpp).
r.CustomDepth=3

[/Script/WindowsTargetPlatform.WindowsTargetSettings]
DefaultGraphicsRHI=DefaultGraphicsRHI_DX12
-D3D12TargetedShaderFormats=PCD3D_SM5
+D3D12TargetedShaderFormats=PCD3D_SM6
-D3D11TargetedShaderFormats=PCD3D_SM5
+D3D11TargetedShaderFormats=PCD3D_SM5

[/Script/AndroidFileServerEditor.AndroidFileServerRuntimeSettings]
bEnablePlugin=True
bAllowNetworkConnection=True
SecurityToken=[secret]
bIncludeInShipping=False
bAllowExternalStartInShipping=False
bCompileAFSProject=False
bUseCompression=False
bLogFiles=False
bReportStats=False
ConnectionType=USBOnly
bUseManualIPAddress=False
ManualIPAddress=

[/Script/Engine.AudioSettings]
; A flat mono sound plays 0.707 to each side, so it keeps its file's power next to the stereo music and beds.
; The engine default, Linear (0.5 each side), plays every mono effect 3 dB under the level baked into it.
MonoChannelUpmixMethod=EqualPower


[/Script/Engine.Engine]
; The settings screen keeps its values in the engine's own user settings (GameUserSettings.ini).
GameUserSettingsClassName=/Script/Supercut.SupercutUserSettings
DefaultEngine.ini
DefaultGame.ini
DefaultInput.ini
Source/Supercut/SupercutCharacter.cpp:26:// jittered each frame and drawn after TSR has smoothed the picture, so with jitter its lines crawl on a still camera.
Source/Supercut/SupercutPuzzleTests.cpp:480:IMPLEMENT_SIMPLE_AUTOMATION_TEST(FSupercutPlatesReleaseTest, "Supercut.Puzzles.ShotsReleasedFromOneFreezeCountInFiringOrder", PuzzleTestFlags)
Source/Supercut/SupercutTuningTests.cpp:334:IMPLEMENT_SIMPLE_AUTOMATION_TEST(FSupercutTuningRangeDefaultsTest, "Supercut.Tuning.EveryDefaultIsInsideItsRange", TuningTestFlags)
Source/Supercut/SupercutTuningTests.cpp:357:IMPLEMENT_SIMPLE_AUTOMATION_TEST(FSupercutTuningRangeLinesTest, "Supercut.Tuning.AValueOutsideItsRangeIsABadLine", TuningTestFlags)
Source/Supercut/SupercutUserSettings.cpp:87:		LastCPUBenchmarkResult, LastGPUBenchmarkResult, ScalabilityQuality.ViewDistanceQuality, S
[... 126 more characters not shown]
```

**Sat 14 Nov 19:18:49 · Tool call: Bash** (Search jam notes for DLSS and upscaler mentions)

```
cd "[notes]/unreal"; grep -niE "dlss|nvidia|streamline|reflex|upscal|TSR|screen ?percent" GOTCHAS.md FINDINGS.md megajam-2026/GAME.md megajam-2026/SUBMISSION.md megajam-2026/lanes/*/HANDOFF.md megajam-2026/lanes/*/*.md 2>/dev/null | head -40
```

Result:

```
GOTCHAS.md:507:  pc3). With a lost GPU (`nvidia-smi`: "GPU is lost. Reboot the system to recover this GPU") the log
GOTCHAS.md:512:  GPU as OK in that state, so run `nvidia-smi` as part of "look before you touch".
GOTCHAS.md:640:  to 30 minutes `nvidia-smi` showed 93 to 100% GPU use and 3.4 to 4.3 GB used with no game of ours running.
GOTCHAS.md:642:  `nvidia-smi --query-gpu=utilization.gpu,power.draw` stays under 40% and 70 W for four samples (Studio windows keep
GOTCHAS.md:747:- **A post-process material after tonemapping reads jittered depth and normals** (13 Nov 2026, verified). TSR has
GOTCHAS.md:750:  TSR forces 8 jitter samples whatever `r.TemporalAASamples` says (SceneVisibility.cpp, the TSR branch). The fix that
FINDINGS.md:14:  - DLSS needs an NVIDIA RTX card, so c4 cannot test a DLSS feature.
FINDINGS.md:16:  with an NVIDIA RTX card, so the only one that could test DLSS for the NVIDIA RTX Award.
megajam-2026/GAME.md:257:**14 Nov 19:17. COMMENTARY COMPLETE; DLSS IS A GO; lane dlss1.** Transcript complete (100 lines,
megajam-2026/GAME.md:263:quality, a performance overlay; no FSR; **"We'll have DLSS so we are eligible for that prize"** (answers the open
megajam-2026/GAME.md:264:NVIDIA RTX Award question). CLAP reference: 14:30-15:30, a left-hand ability, once held (charging) from about
megajam-2026/GAME.md:266:pulling out his left hand". Lane dlss1 (Opus high, `claudeAgent_alt`, task id ends
megajam-2026/GAME.md:267:`f71eb297-5ad1-4888-af4d-2b104683b2ad`): research only, `lanes/dlss1/PLAN.md` + `BUILD_BRIEF.md`; the plugin
megajam-2026/SUBMISSION.md:19:| NVIDIA questions | only if we use an NvRTX feature, DLSS 4.5 or ACE |
megajam-2026/lanes/audiowire/HANDOFF.md:372:- `ShotsReleasedFromOneFreezeCountInFiringOrder`: ring at 900 cm, bar at 500, cross at 200, fired in that order
megajam-2026/lanes/feel2/HANDOFF.md:110:- `Supercut.Tuning.EveryDefaultIsInsideItsRange` and `Supercut.Tuning.AValueOutsideItsRangeIsABadLine`.
megajam-2026/lanes/feel3/HANDOFF.md:89:One test changed for Part A: `Supercut.Puzzles.ShotsReleasedFromOneFreezeCountInFiringOrder` waits 0.06 s for shots
megajam-2026/lanes/figin/HANDOFF.md:149:| `figin_mixed_01_crop_side_by_side.jpg` | 2x crop of the same frame: the three kinds side by side | Upscaled, so soft. |
megajam-2026/lanes/light1/HANDOFF.md:107:(`EveryFieldIsListedWithTheHeadersComment`, `EveryDefaultIsInsideItsRange`). I also put the old aim code back for
megajam-2026/lanes/sketchfx/HANDOFF.md:15:read) and in three things 
[... 4125 more characters not shown]
```

**Sat 14 Nov 19:18:55 · Tool call: Bash** (Read TSR jitter gotcha and slice findings)

```
cd "[notes]/unreal"; sed -n 745,760p GOTCHAS.md; echo ----; sed -n 10,18p FINDINGS.md; echo ----; sed -n 70,90p megajam-2026/lanes/slice/HANDOFF.md; echo ---; sed -n 195,205p megajam-2026/lanes/sketchfx/HANDOFF.md
```

Result:

```
asset. Run make_assets with `-AllowCommandletRendering` instead; it stays headless. `recompile_material` only queues
  the compile there: the shaders really compile in the package cook, so read `package_run.log` for material errors.
- **A post-process material after tonemapping reads jittered depth and normals** (13 Nov 2026, verified). TSR has
  smoothed the colour by then, but SceneDepth, WorldNormal and the stencil are this frame's jittered samples, so
  outlines drawn from them crawl by a pixel on a still camera (3.6% of wall pixels changed between two still frames).
  TSR forces 8 jitter samples whatever `r.TemporalAASamples` says (SceneVisibility.cpp, the TSR branch). The fix that
  worked: a `FWorldSceneViewExtension` whose `SetupView` sets `View.bAllowTemporalJitter = false` while the effect is
  on (SetupView runs on the game thread from `ULocalPlayer::CalcSceneView`). After it, still frames differ only as
  much as with anti-aliasing off (1.3%, tone in the hatching).
- **A bright emissive loses its hue in the tonemapper** (13 Nov 2026, verified). An unlit glow at strength 4 to 80
  comes out near white or gold whatever its colour: (1, 0.13, 0.03) x 4 read 255,207,117. Pushing saturation after
  tonemapping cannot bring the hue back. Dim the glow instead (a Material Parameter Collection scalar read by the glow
  material); at strength 1 with manual exposure the same colour read 255,102,0.
- **`unreal.CollectionScalarParameter(parameter_name=...)` raises "call() takes at most 0 arguments"** (13 Nov 2026,
  verified). The struct takes no keyword constructor in Python. Make it empty (its C++ constructor gives it a new Id),
  then `set_editor_property` each field.
----
    (the Launcher lists Fortnite only, no UEFN entry).
  - Visual Studio Build Tools 2022 17.14 installed 12 Nov 2026 16:40 (none before that). Details in
    "Visual Studio on c4" below.
  - GPU: AMD Radeon RX 9070 XT. RAM: 31 GB. Free disk: C 334 GB, D 2362 GB, E 366 GB.
  - DLSS needs an NVIDIA RTX card, so c4 cannot test a DLSS feature.
- **[pc-b]**: RTX 4080 Super (from memory notes, not rechecked today). The only box of ours noted
  with an NVIDIA RTX card, so the only one that could test DLSS for the NVIDIA RTX Award.
- **[pc-b], pc2, pc3, pc4** (12 Nov 2026, verified over ssh): no Epic Launcher install data at
  `C:\ProgramData\Epic\UnrealEngineLauncher\LauncherInstalled.dat`, so no Launcher-installed engine.
----

### Risks settled

1. **TSR shimmer with a still camera.** I com
[... 2622 more characters not shown]
```

**Sat 14 Nov 19:18:57 · Tool call: Bash** (Read post-process and jitter code in game source)

```
cd /d/UE/Projects/Supercut59/Source/Supercut; sed -n 15,60p SupercutCharacter.cpp; grep -n "BlendableLocation\|AddOrUpdateBlendable\|WeightedBlendables\|PostProcess\|TemporalAA\|r\.TemporalAA\|Jitter\|IConsoleManager\|ScreenPercentage\|ExecuteConsole" *.cpp *.h | head -50
```

Result:

```
#include "Engine/StaticMesh.h"
#include "Engine/World.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/Controller.h"
#include "Materials/MaterialInstanceDynamic.h"
#include "Materials/MaterialParameterCollection.h"
#include "Materials/MaterialParameterCollectionInstance.h"
#include "SceneView.h"
#include "SceneViewExtension.h"

// Holds the camera's sub-pixel jitter still while the sketch is on. The sketch reads depth and normals, which are
// jittered each frame and drawn after TSR has smoothed the picture, so with jitter its lines crawl on a still camera.
class FSupercutStillFrame : public FWorldSceneViewExtension
{
public:
	FSupercutStillFrame(const FAutoRegister& AutoRegister, UWorld* World) : FWorldSceneViewExtension(AutoRegister, World) {}
	bool bStill = false;

	virtual void SetupView(FSceneViewFamily& ViewFamily, FSceneView& View) override
	{
		if (bStill)
		{
			View.bAllowTemporalJitter = false;
		}
	}
};

namespace
{
	const float EyeHeight = 64.f;                       // above the capsule centre; the eye is 152 cm off the floor
	const FVector GunHome(38.f, 17.f, -15.f);           // in camera space: forward, right, up
	const FVector ClapHome(36.f, -19.f, -11.3f);
	const float ClapScale = 0.62f;                      // the board is modelled at 18 cm wide, which fills too much of the view
	const FVector MuzzleOffset(22.f, 0.f, 2.f);         // in gun space
	const float ArmOpenDegrees = 30.f;
	const FVector FlashShape(0.8f, 1.f, 0.6f);          // the flash's length, width and height against MuzzleFlashSize: not round, so its random turn shows
	const int32 ViewRandomSeed = 7;                     // ViewRandom's seed: the same view each run, apart from every gameplay stream
	const FLinearColor PipColor(1.f, 0.8f, 0.2f);
	bool bClappedThisProgramRun = false;               // HasClappedThisProgramRun: for the whole process, never saved

	// The held meshes (Art/held, Revolver.json and Clap.json there): real hand size, each on its own pivot.
	const float GunScale = 1.36f;                       // the meshes are hand size; at 1.36 the gun covers the box gun's screen area (1.2% under)
	const FVector MeshMuzzle(8.f, 0.f, 1.85f);          // the muzzle in the revolver meshes' space; it lands on MuzzleOffset
	const int32 Chambers = 6;
	const float ChamberRadius = 1.8f;                   // round seats round the cylinder's axis, 2.675 behind its origin
	const float CylinderStepSeconds = 0.08f;            // one 60 degree step
[... 1412 more characters not shown]
```

**Sat 14 Nov 19:19:03 · Tool call: Bash** (Read sketch blendable setup and material location)

```
cd /d/UE/Projects/Supercut59; sed -n 125,190p Source/Supercut/SupercutCharacter.cpp; grep -rn "blendable_location\|BLL_\|BlendableLocation" Tools Script --include=*.py 2>/dev/null | head; ls Tools
```

Result:

```
Rounds = Tuning.RevolverRounds;

	BuildViewModel();

	Camera->PostProcessBlendWeight = 1.f;
	FPostProcessSettings& Picture = Camera->PostProcessSettings;
	// A fixed exposure: the picture must not drift while the player looks around. ApplyTuning sets its level.
	Picture.bOverride_AutoExposureMethod = true;
	Picture.AutoExposureMethod = AEM_Manual;
	Picture.bOverride_AutoExposureApplyPhysicalCameraExposure = true;
	Picture.AutoExposureApplyPhysicalCameraExposure = false;
	Picture.bOverride_AutoExposureBias = true;
	Picture.bOverride_BloomIntensity = true;
	Picture.bOverride_MotionBlurAmount = true;
	Picture.MotionBlurAmount = 0.f;
	Picture.bOverride_VignetteIntensity = true;
	Picture.VignetteIntensity = 0.3f;

	// The frozen-time sketch. It is drawn only while its weight is above 0 (FSceneView::OverridePostProcessSettings).
	const TCHAR* SketchPath = TEXT("/Game/Materials/M_SketchFreeze.M_SketchFreeze");
	UMaterialInterface* SketchMaterial = LoadObject<UMaterialInterface>(nullptr, SketchPath);
	if (!SketchMaterial)
	{
		UE_LOG(LogSupercut, Fatal, TEXT("Missing asset %s. It is made by Tools/make_assets.py."), SketchPath);
	}
	Sketch = UMaterialInstanceDynamic::Create(SketchMaterial, this);
	Camera->AddOrUpdateBlendable(Sketch, 0.f);
	// The same blend for every material (M_Glow dims its glows with it, so a signal keeps its hue in the sketch).
	const TCHAR* SketchValuesPath = TEXT("/Game/Materials/MPC_Sketch.MPC_Sketch");
	UMaterialParameterCollection* SketchCollection = LoadObject<UMaterialParameterCollection>(nullptr, SketchValuesPath);
	if (!SketchCollection)
	{
		UE_LOG(LogSupercut, Fatal, TEXT("Missing asset %s. It is made by Tools/make_assets.py."), SketchValuesPath);
	}
	SketchValues = GetWorld()->GetParameterCollectionInstance(SketchCollection);
	StillFrame = FSceneViewExtensions::NewExtension<FSupercutStillFrame>(GetWorld());
	ApplyTuning();

	USupercutTime& Time = USupercutTime::Get(this);
	Time.OnFroze.AddUObject(this, &ASupercutCharacter::OnFroze);
	Time.OnResumed.AddUObject(this, &ASupercutCharacter::OnResumed);

	if (bTitleLook)
	{
		ShowTitleLook();
	}
}

void ASupercutCharacter::ShowTitleLook()
{
	bTitleLook = true;
	if (!HasActorBegunPlay())
	{
		return;   // BeginPlay calls this again once the sketch exists
	}
	// The title screen pauses the game, so Tick does not run there: the look is set here in full.
	SketchBlend = 1.f;
	Sketch->SetScalarParameterValue(TEXT("Blend"), 1.f);
	SketchValues->SetScalarParameterValue(TEXT("Blend"), 1.f);
	Stil
[... 584 more characters not shown]
```

**Sat 14 Nov 19:19:04 · Tool call: Bash** (Read Build.cs, targets and user settings header)

```
cd /d/UE/Projects/Supercut59; cat Source/Supercut/Supercut.Build.cs; ls Source; cat Source/*.Target.cs | grep -v "^\s*$" | head -40; sed -n 1,140p Source/Supercut/SupercutUserSettings.h
```

Result:

```
using UnrealBuildTool;

public class Supercut : ModuleRules
{
	public Supercut(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "SlateCore", "ApplicationCore" });
		PrivateDependencyModuleNames.AddRange(new string[] { "AudioMixer", "AudioMixerCore", "NonRealtimeAudioRenderer", "Json" });

		// The music is read from these WAV files at run time (SupercutMusic.cpp), so the build stages them beside the game.
		foreach (string Name in new string[] { "mx_action_drums", "mx_action_bass", "mx_action_colour", "mx_action_heat", "mx_puzzle", "mx_between", "mx_take_start", "mx_room_clear" })
		{
			RuntimeDependencies.Add("$(ProjectDir)/Audio/music/wav/" + Name + ".wav", StagedFileType.NonUFS);
		}
	}
}
Supercut
Supercut.Target.cs
SupercutEditor.Target.cs
using UnrealBuildTool;
using System.Collections.Generic;
public class SupercutTarget : TargetRules
{
	public SupercutTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		// The same source builds on UE 5.9 and on 5.8.4. A 5.9 game target must be V8 or packaging stops in UBT.
#if UE_5_9_OR_LATER
		DefaultBuildSettings = BuildSettingsVersion.V8;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_9;
#else
		DefaultBuildSettings = BuildSettingsVersion.V7;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
#endif
		ExtraModuleNames.Add("Supercut");
	}
}
using UnrealBuildTool;
using System.Collections.Generic;
public class SupercutEditorTarget : TargetRules
{
	public SupercutEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		// The same source builds on UE 5.9 and on 5.8.4. See Supercut.Target.cs.
#if UE_5_9_OR_LATER
		DefaultBuildSettings = BuildSettingsVersion.V8;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_9;
#else
		DefaultBuildSettings = BuildSettingsVersion.V7;
		IncludeOrderVersion = EngineIncludeOrderVersion.Unreal5_8;
#endif
		ExtraModuleNames.Add("Supercut");
	}
}
#pragma once

#include "CoreMinimal.h"
#include "GameFramework/GameUserSettings.h"
#include "Misc/CommandLine.h"
#include "SupercutUserSettings.generated.h"

/**
 * The settings screen's four values. They live in the engine's own user settings: Config/DefaultEngine.ini names this
 * class as the engine's GameUserSettingsClassName, so the engine loads it at start and it saves to the same file
 * (GameUserSetting
[... 4268 more characters not shown]
```

**Sat 14 Nov 19:19:08 · Tool call: Bash** (Read package script and run_demo parameters)

```
cd /d/UE/Projects/Supercut59/Tools; cat package.cmd; sed -n 1,60p run_demo.ps1 | grep -nE "param|\[|\$|ExtraArgs|-ResX|RenderOffscreen|Args" | head -50
```

Result:

```
@echo off
rem Packages the Windows Development build with UE 5.9 to D:\UE\Builds\Supercut59. The log goes to Saved\Logs\package_run.log.
rem The Visual C++ runtime files are staged beside the game (-applocaldirectory) and no runtime installer is
rem shipped (no -prereqs): with the installer, the launcher stops at an install prompt on any PC whose runtime is older.
rem One compile at a time: this PC sometimes writes a bad precompiled header (see Tools\build.ps1).
rem The -ubtargs value holds spaces, so it is quoted as one argument. Typed into PowerShell or bash the quotes get lost: run this file.
rem Usage: cmd /c Tools\package.cmd
set PROJ=%~dp0..
cd /d D:\UE
call D:\UE\UE_5.9\Engine\Build\BatchFiles\RunUAT.bat BuildCookRun -nop4 -utf8output -unattended -nocompileuat -cook -build -project=%PROJ%\Supercut.uproject -unrealexe=D:\UE\UE_5.9\Engine\Binaries\Win64\UnrealEditor-Cmd.exe -platform=Win64 -installed -stage -archive -package -pak -iostore -compressed -applocaldirectory=D:\UE\UE_5.9\Engine\Binaries\ThirdParty\AppLocalDependencies -archivedirectory=D:\UE\Builds\Supercut59 -clientconfig=Development "-ubtargs=-MaxParallelActions=1 -NoHotReloadFromIDE -Log=%PROJ%\Saved\Logs\ubt_package.log" > "%PROJ%\Saved\Logs\package_run.log" 2>&1
if errorlevel 1 exit /b %ERRORLEVEL%
rem Beside Supercut.exe: Tuning.example.txt, written by the packaged game itself so it always matches FSupercutTuning,
rem and Play_dev.bat, which starts the game with the practice keys. A Tuning.txt left in the folder is not touched.
set OUT=D:\UE\Builds\Supercut59\Windows
if exist "%OUT%\Tuning.example.txt" del /q "%OUT%\Tuning.example.txt"
"%OUT%\Supercut.exe" -SupercutWriteTuning -nullrhi -unattended -nosplash "-abslog=%PROJ%\Saved\Logs\write_tuning.log"
if not exist "%OUT%\Tuning.example.txt" (
  echo Tuning.example.txt was not written: see Saved\Logs\write_tuning.log
  exit /b 1
)
copy /y "%PROJ%\Tools\Play_dev.bat" "%OUT%\Play_dev.bat" > nul || exit /b 1
exit /b 0
1:# Runs the scripted player in a real game window and waits for it to quit.
2:# Default: the uncooked project through the editor exe. With -Packaged: the packaged game.
3:# Usage: powershell -File Tools\run_demo.ps1 [-Shots <folder>] [-ResX 1280] [-ResY 720] [-Script <file>]
4:#        [-Room <name>] [-Run <name>] [-Seed <n>] [-Log <file>] [-TimeoutSeconds 240] [-NoQuit] [-Packaged [-Exe <packaged Supercut.exe>]]
5:#        [-FixedFps <n>] [-Silent] [-Record <file.wav>] [-Upgrades <name>,<name>] [-Dev]
[... 3314 more characters not shown]
```

**Sat 14 Nov 19:19:17 · Tool call: Bash** (Check run_demo extra args and fps logging)

```
cd /d/UE/Projects/Supercut59/Tools; sed -n 50,120p run_demo.ps1 | grep -nE "gameArgs|RenderOffscreen|Extra|ExecCmds|dpcvars" ; grep -rn "SupercutFps\|FrameTime\|fps" ../Source/Supercut/*.cpp | grep -i "log\|UE_LOG" | head -8
```

Result:

```
1:if ($Run) { $gameArgs += "-SupercutRun=$Run" }
2:if ($Seed -ge 0) { $gameArgs += "-SupercutSeed=$Seed" }
3:if ($Upgrades) { $gameArgs += "-SupercutUpgrades=$Upgrades" }
4:if ($Dev) { $gameArgs += "-SupercutDev" }
5:if (-not $NoQuit) { $gameArgs += "-SupercutQuit" }
6:if ($FixedFps -gt 0) { $gameArgs += @("-UseFixedTimeStep", "-FPS=$FixedFps") }
10:if ($Silent -or $Record) { $gameArgs += "-DeterministicAudio" }
11:if ($Record) { $gameArgs += "-SupercutRecord=`"$Record`"" }   # quotes after the = so FParse::Value reads a path with spaces
12:$p = Start-Process -FilePath $exe -ArgumentList $gameArgs -PassThru
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:19:22 · Tool call: Bash** (Find what the fps flag logs)

```
cd /d/UE/Projects/Supercut59/Source/Supercut; grep -rn "SupercutFps" *.cpp | head -5; grep -rn "TEXT(\"FPS\|FPS \|ms frame\|frame ms" *.cpp | head -8
```

Result:

```
SupercutPlayerController.cpp:57:	bCountFps = FParse::Param(FCommandLine::Get(), TEXT("SupercutFps"));
SupercutPlayerController.cpp:712:			UE_LOG(LogSupercut, Display, TEXT("FPS %s: no frames counted"), Name);
SupercutPlayerController.cpp:722:		UE_LOG(LogSupercut, Display, TEXT("FPS %s: average %.1f, slowest 1%% of frames %.1f, over %d frames and %.1f s"),
Shell cwd was reset to [notes]
```

### Sat 14 Nov 19:19:25 · Agent (claude-opus-5-5)

Local reading is done. Now the web: NVIDIA's Unreal page, the jam's award wording, and the DLSS plugin versions.

**Sat 14 Nov 19:19:26 · Tool call: ToolSearch**

```
{
 "query": "select:WebSearch",
 "max_results": 1
}
```

Result:

```

```

**Sat 14 Nov 19:19:29 · Tool call: WebSearch**

```
{
 "query": "Epic AI MegaJam 2026 \"Render Royalty\" NVIDIA RTX Award DLSS 4.5",
 "mode": "extended"
}
```

**Sat 14 Nov 19:19:29 · Tool call: WebSearch**

```
{
 "query": "NVIDIA DLSS 4.5 Unreal Engine plugin 5.8 5.9 release",
 "mode": "extended"
}
```

Result:

```
Web search results for query: "Epic AI MegaJam 2026 "Render Royalty" NVIDIA RTX Award DLSS 4.5"

Links: [{"title":"2026 Epic AI MegaJam - itch.io","url":"https://itch.io/jam/2026-epic-ai-megajam"},{"title":"Meet the 2026 Epic AI MegaJam partners - Announcements - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/meet-the-2026-epic-ai-megajam-partners/2853549"},{"title":"Epic AI MegaJam 2026: rules, prizes and Unreal MCP setup - DEV Community","url":"https://dev.to/indiebots/epic-ai-megajam-2026-rules-prizes-and-unreal-mcp-setup-291j"},{"title":"Epic promises up to $50,000 for games made with AI","url":"https://renderu.com/en/news/post/28734"},{"title":"Epic Games’ AI MegaJam 2026 Will Let Devs Vibe-Code Games for a $65,000 Cash Prize","url":"https://beebom.com/epic-games-ai-megajam-2026-will-let-devs-vibe-code-games-for-cash-prize/"},{"title":"Epic AI MegaJam 2026: Dates, Rules, Prizes and an AI Prep Checklist","url":"https://vibestackweekly.com/epic-ai-megajam-2026/"},{"title":"Epic AI MegaJam 2026: Dates, Prizes, AI Tools & How to Join","url":"https://www.projprod.com/post/epic-ai-megajam-2026"},{"title":"Epic Games announces AI MegaJam 2026 with prize pool of $65,000","url":"https://www.sportstiger.com/esports/epic-games-announces-ai-megajam-2026-with-prize-pool-of-65000/"},{"title":"Epic AI MegaJam 2026 UEFN: How to Enter, Dates, Teams and Prizes","url":"https://www.theclick.gg/epic-ai-megajam-2026-uefn/"},{"title":"Epic AI MegaJam 2026: AI Is Optional, $65K Cash Prizes and Unreal Engine Submission Rules","url":"https://windowsforum.com/news/epic-ai-megajam-2026-ai-is-optional-65k-cash-prizes-and-unreal-engine-submission-rules.449768/"}]

The NVIDIA RTX Award is a single GeForce RTX 5090 for the top-ranked eligible Render Royalty entry, and DLSS 4.5 qualifies as one of the NVIDIA features.

- **Award structure:** The award goes to the best Render Royalty entry built in Unreal Engine that uses at least one feature from NVIDIA RTX, NVIDIA DLSS, or NVIDIA ACE. The eligible features include RTX Mega Geometry, RTX Direct Illumination, RTX Indirect Illumination, and RTX Path Tracing, which come through the NvRTX branch of Unreal Engine.
- **DLSS 4.5:** The itch.io listing names DLSS 4.5 (Unreal Engine) as a qualifying feature, so an Unreal entry using it can enter the award.
- **Terms:** Epic's judges will determine qualification, with technical assistance from NVIDIA as needed. Entrants also answer the NVIDIA questions when you submi
[... 479 more characters not shown]
```

Result:

```
Web search results for query: "NVIDIA DLSS 4.5 Unreal Engine plugin 5.8 5.9 release"

Links: [{"title":"NVIDIA DLSS","url":"https://developer.nvidia.com/rtx/dlss"},{"title":"NVIDIA DLSS: Unreal Engine Plugin Archive - DLSS - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/nvidia-dlss-unreal-engine-plugin-archive/377564"},{"title":"Official DLSS 5 Neural Rendering plugin access for Unreal Engine 5.8.2 - DLSS - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/official-dlss-5-neural-rendering-plugin-access-for-unreal-engine-5-8-2/382731"},{"title":"DarknessFX on X: \"NVIDIA DLSS 4.5 plugin has been updated today with support for Unreal Engine 5.8, download it at https://t.co/MJTzKDnNi1\" / X","url":"https://x.com/DrkFX/status/2072992551045308848"},{"title":"What’s New for Game Developers in NVIDIA RTX: DLSS 4.5 for UE5 and Multilingual AI Characters","url":"https://developer.nvidia.com/blog/whats-new-for-game-developers-in-nvidia-rtx-dlss-4-5-for-ue5-and-multilingual-ai-characters/"},{"title":"NVIDIA DLSS 4.5 Plugin Brings Dynamic Frame Generation to Unreal Engine","url":"https://en.gamegpu.com/news/igry/plagin-nvidia-dlss-4-5-vnedryaet-dinamicheskuyu-generatsiyu-kadrov-v-unreal-engine"},{"title":"What’s New for Game Developers in NVIDIA RTX: DLSS 4.5 for UE5 and Multilingual AI Characters - GameDev News","url":"https://gamedev.net/news/3584-whats-new-for-game-developers-in-nvidia-rtx-dlss-45-for-ue5-and-multilingual-ai/"},{"title":"Any hero who can compile it for 5.8 - DLSS - NVIDIA Developer Forums","url":"https://forums.developer.nvidia.com/t/any-hero-who-can-compile-it-for-5-8/370193"},{"title":"NVIDIA DLSS 4.5 For Unreal Engine User Manual - Manuals+","url":"https://manuals.plus/nvidia/dlss-4-5-for-unreal-engine-manual"}]

The search found DLSS 4.5 plugin releases for Unreal Engine 5.8, but nothing for UE 5.9.

- **Plugin availability:** NVIDIA's DLSS page lists a UE 5.8 download for the DLSS 4.5 plugin, alongside 5.7, 5.6, and 5.5 builds and notes that the DLSS 4.5 plugin package was last updated in October 2026.
- **Release history:** NVIDIA's plugin archive lists DLSS 4.5 Plugin 8.7.2 for UE 5.8, 5.7, 5.6, and 5.5 on July 21, 2026, with an earlier 8.7.0 build on July 2, 2026 (same engine list).
- **Features:** The plugin brings direct access to dynamic multi-frame generation, a new 6x frame generation mode, and second-generation transformer models for super-resolution.
- **Engine branch:** NVIDIA's RTX branch
[... 840 more characters not shown]
```

**Sat 14 Nov 19:19:39 · Tool call: ToolSearch**

```
{
 "query": "WebFetch fetch url",
 "max_results": 3
}
```

Result:

```

```

**Sat 14 Nov 19:19:44 · Tool call: Bash** (Read NVIDIA award text in official rules)

```
cd "[notes]/unreal/megajam-2026/rules"; ls; grep -n -i -B2 -A12 "nvidia\|render royalty" *.txt | head -120
```

Result:

```
official_rules_2026-11-05.pdf
official_rules_2026-11-05.txt
240-• Solo Driver: For the best game created by a solo developer. 
241-• Best Team: For the best overall game created by a team of two (2) or more Entrants. 
242:• Render Royalty: For the game with the best overall visuals, photoreal or stylized. 
243-• Pocket Powerhouse: For the best mobile game, with one (1) Unreal Engine winner and one (1) 
244-UEFN winner. 
245-• Glass Box: For the best dev log documenting how the Entrant created their Submission. To be 
246-eligible, the dev log must be submitted together with the Submission during the Contest Period. 
247-• Walkie-Talkie: For the best narrative-driven UEFN game featuring large language model 
248-("LLM")-powered non-player characters built with the UEFN conversations feature. 
249-The highest scoring Qualified Submission in each Modifier Prize category that meets the modifier 
250-criteria will be deemed a potential Modifier Prize winner (together with the potential main category 
251-prize winners, the "Winning Entrants"). A potential prize winner can win only one (1) Modifier 
252-Prize category, unless no other eligible potential winner remains for the additional category or 
253-categories. 
254-11. Development Continuation Grants. Following the Contest, Sponsor may, in its sole discretion, 
--
288-• One (1) Solo Driver Modifier Prize: US $2,500 plus Partner Prizes if specified 
289-• One (1) Best Team Modifier Prize: US $5,000 plus Partner Prizes if specified 
290:• One (1) Render Royalty Modifier Prize: US $2,500 plus Partner Prizes if specified 
291-• Two (2) Pocket Powerhouse Modifier Prizes (one (1) Unreal Engine, one (1) UEFN): US 
292-$2,500 each [plus Partner Prizes if specified] 
293-• One (1) Glass Box Modifier Prize: US $2,500 plus Partner Prizes if specified 
294-• One (1) Walkie-Talkie Modifier Prize: US $2,500 plus Partner Prizes if specified 
295-Total cash prizes: US $65,000. 
296-Approximate Retail Value ("ARV") of all cash prizes: US $65,000. The ARV of any Partner Prizes 
297-is not included in this amount, is not known as of the date of these Official Rules, and will be 
298-determined once the Partner Prizes are confirmed. 
299-Prizes are awarded per Submission (that is, per team) and not per Entrant. Each prize (including 
300-each cash prize and any Partner Prize) will be awarded to the Team Owner on behalf of the team, 
301-and the Team Owner is solely responsible for dividing or sharing the prize among the Entran
[... 108 more characters not shown]
```

**Sat 14 Nov 19:19:53 · Tool call: Bash** (Fetch jam and NVIDIA pages as HTML text)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; mkdir -p "$S"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
curl -sL -A "$UA" "https://itch.io/jam/2026-epic-ai-megajam" -o itch.html; curl -sL -A "$UA" "https://forums.unrealengine.com/t/meet-the-2026-epic-ai-megajam-partners/2853549.json" -o partners.json; curl -sL -A "$UA" "https://developer.nvidia.com/game-engines/unreal-engine" -o nv_ue.html; curl -sL -A "$UA" "https://developer.nvidia.com/rtx/dlss" -o nv_dlss.html; ls -la --block-size=K | awk '{print $5,$9}'
python -I -c "
import re,html,sys
t=open('itch.html',encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>','\n',t));t=re.sub(r'\n\s*\n+','\n',t)
i=t.find('NVIDIA');print(len(t));
for m in re.finditer(r'NVIDIA|DLSS|Render Royalty',t):pass
idx=[m.start() for m in re.finditer(r'NVIDIA|DLSS',t)]
print(idx[:20])
print(t[max(0,idx[0]-1500):idx[0]+3000] if idx else t[:3000])
"
```

Result:

```
0K .
0K ..
161K itch.html
37K nv_dlss.html
44K nv_ue.html
84K partners.json
35971
[1173, 10392, 10401, 10442, 10631, 10741, 10748, 10793, 10944, 16013, 16052, 18836, 19081, 19110, 19125, 19167, 21046, 21071, 21268, 21384]

2026 Epic AI MegaJam - itch.io
Skip to main content
itch.io
Browse Games
Game Jams
Upload Game
Developer Logs
Community
Log in
Register
Indie game store
Free games
Fun games
Horror games
Game development
Assets
Comics
Sales
Bundles
Jobs
Tags
Game Engines
2026 Epic AI MegaJam
Hosted by 
epicgamesjams
 � 
#MegaJam
10k
Joined
76
Entries
Overview
Submissions
Submission feed
Submissions open from 
2026-11-12 05:00:00
 to 
2026-11-16 01:59:00
Submissions due in
years
months
days
hours
minutes
seconds
Join jam
This year�s theme: DIRECTOR�S CUT
Your vision, your edits, your final cut. Every developer has that one feature that didn�t quite make it: the mechanic you scoped out at 2 AM, or the idea you shelved and never found a place for. Now�s your chance to finally build it. Using AI agents? You�re directing those too. Set the vision, delegate tasks, and decide what makes the cut.
Vibe your way to $50k
Four days. Up to five humans. As many AI agents as you want. Build a playable game in Unreal Engine or Unreal Editor for Fortnite (UEFN) and compete for cash prizes.
Supported by Claude, Google, OpenAI, SpaceXSI, AMD, Diversion, fal, Hyper3D, Intel, Meshy,
NetApp, NVIDIA, PBRgen, Reallusion, Rokoko, Tripo, and WeLoveIndies.
Dates�
November 12�15, 2026
Prizes
$65,000 in cash prizes, plus Development Continuation Grants of up to $50,000 per team and partner prizes
Perks
Free AI tool credits, version control,
materials, audio, and animation tools for
every jammer. See Partners below.
Tools
Unreal Engine or UEFN, plus any AI tools
Teams
Solo, or up to five people
Where
* Online from anywhere
* In person at Digital Jungle, San Francisco,�Nov 14�15 (
ticket required
)
* At select local�Unreal Engine and UEFN community chapters worldwide.�
Who can enter
Open to developers age 18+ with an�active Epic Games account.� See the 
Official Rules
�for full eligibility details.
Select Join jam 
on this page.�
Joining in person? 
Registration for the San Francisco�event is now�open on 
Eventbrite
. Space is limited.
Set up your tools.
 Install Unreal Engine or UEFN, and get your coding agents and MCP working before kickoff. See 
Get ready
. Watch your inbox on November 10 for cred
[... 2089 more characters not shown]
```

**Sat 14 Nov 19:20:03 · Tool call: Bash** (Extract NVIDIA award text from itch page)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; cat > /c/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/txt.py <<'EOF'
import re,html,sys
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S);t=html.unescape(re.sub(r'<[^>]+>','\n',t));t=re.sub(r'[ \t]+',' ',t);t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[2],'w',encoding='utf8').write(t)
EOF
for f in itch nv_ue nv_dlss; do python -I ../txt.py $f.html $f.txt; done
python -I -c "
t=open('itch.txt',encoding='utf8').read()
for k in ['NVIDIA RTX','NVIDIA question','NVIDIA Q','Render Royalty']:
  i=0
  while True:
    i=t.find(k,i)
    if i<0:break
    print('=====',k,i);print(t[max(0,i-300):i+1200].replace('\n',' | '));i+=len(k)+1200
" | head -80
```

Result:

```
===== NVIDIA RTX 10442
fter the jam get a free session with AWS and NetApp technical experts to deploy the AWS Game Development Toolkit and speed up Horde build pipelines on AWS. Game history for your shelf. Modern infrastructure for your next game.  | linktr.ee/netappgames | NVIDIA:  | NVIDIA supports Unreal Engine 5 with key NVIDIA RTX� technologies. This powerful combination helps developers of all levels get started and propel their games and experiences to the next level. Explore advanced rendering with the NVIDIA RTX Branch of Unreal Engine (NvRTX), boost frame rates while delivering crisp high-quality images with NVIDIA DLSS, and bring game characters to life with NVIDIA ACE. Build with GeForce RTX GPUs and get started with plugins, samples, and developer resources. We can�t wait to see what games you build with NVIDIA RTX!  | developer.nvidia.com | PBRgen:  | PBRgen is an AI tool that generates seamless, tileable PBR materials from a text prompt or reference image. Every material comes with tweakable maps (albedo, normal, roughness, metallic, height, AO, and more) that drop straight into Unreal Engine and UEFN. All 2026 Epic AI MegaJam participants get free access to PBRgen for the duration of the jam, so your team can build the look of your game as fast as you can describe it.  | pbrgen.com | Reallusion:  | Reallusion is proud to partner with Epic Games for the Epic AI MegaJam! Empowering creators to build next-level games in Unreal Engine and UEFN, Reallusion brings industry-leading character creation and 
===== NVIDIA RTX 16013
. | Include:� | Team name, plus each member�s name and the email address linked to their Epic Games account | Game name | Gameplay video link (30�60 seconds) | Dev log link (optional, but required for the Glass Box modifier) | Tools you used (optional, but needed for partner prizes such as Hyper3D�s cash pool) | NVIDIA RTX Award (optional): check the NVIDIA features you used and describe how you used them | OpenAI Awards (optional): which OpenAI models or products you used, and how | UEFN teams | You submit on itch.io. with a private version code. That's a fixed snapshot of your island that can't be changed after you create it.�Follow the  | Fortnite Developer Rules. | 1) Your private version code must be the final, playable build you want judged, and you must create it before the deadline.� | 2) Live island codes and playtest codes aren't accepted, because they can be changed after the jam ends. | Include:� | Team nam
[... 11772 more characters not shown]
```

### Sat 14 Nov 19:20:08 · Agent (claude-opus-5-5)

I have the award wording from the itch.io jam page. Now checking the excluded-countries list, then NVIDIA's DLSS pages.

**Sat 14 Nov 19:20:10 · Tool call: Bash** (Check excluded list and DLSS page text)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; python -I -c "
t=open('itch.txt',encoding='utf8').read()
i=t.find('NVIDIA RTX Award excluded');print(t[i:i+1500].replace('\n',' '))
print('SINGAPORE' , 'Singapore' in t[i:i+1500])
"; echo; grep -n -i "dlss\|download\|5\.8\|5\.9\|plugin" nv_dlss.txt | head -60
```

Result:

```
NVIDIA RTX Award excluded destinations:  Afghanistan; Armenia; Azerbaijan; Bahrain; Belarus; Burma (Myanmar); Cambodia; Central African Republic; China (PRC); Democratic Republic of the Congo; Cuba; Egypt; Eritrea; Georgia; Haiti; Iran; Iraq; Jordan; Kazakhstan; North Korea; Kuwait; Kyrgyzstan; Laos; Lebanon; Libya; Macau; Moldova; Mongolia; Nicaragua; Oman; Pakistan; Qatar; Russia; Saudi Arabia; Somalia; South Sudan; Sudan; Syria; Tajikistan; Turkmenistan; Uzbekistan; Venezuela; Vietnam; Yemen; Zimbabwe. Development Continuation Grants Standout Unreal Engine and UEFN entries can receive Development Continuation Grants of up to $50,000 to keep developing their jam game. Category First place Second place Third place Unreal Engine $50,000 + $1,000 Fab credit $25,000�+ $500 Fab credit� $10,000�+ $250 Fab credit� UEFN $50,000��+ $1,000 Fab credit $25,000�+ $500 Fab credit� $10,000�+ $250 Fab credit� Fab credits go to each winning team�s team lead. Each grant team also gets  one month of Tripo Teams, with up to five seats .� A panel of judges scores each qualified entry from 1 to 5 on: Criterion What judges look for Ambition and innovation Something you couldn�t usually pull off in a four-day jam: a new mechanic, a bold art style, or a bigger scope� Theme A fresh, clever take on the theme Fun factor Gameplay that's fun and satisfying Gameplay Solid, original mechanics that feel good Visuals A strong, consistent look, photoreal or stylized Level design and�game progression Spaces t
SINGAPORE False

2:NVIDIA DLSS | NVIDIA Developer
3:NVIDIA DLSS
4:NVIDIA DLSS is a suite of neural rendering technologies powered by NVIDIA RTX™ Tensor Cores that boosts frame rates while delivering crisp, high-quality images that rival native resolution. DLSS 4 introduced Multi Frame Generation (MFG) and a transformer model for high quality super resolution. DLSS 4.5 introduces Dynamic MFG and a second generation transformer model. 
5:Download Now
8:DLSS AI Technologies
9:DLSS neural rendering technologies include:
10:DLSS Multi Frame Generation
12:DLSS Dynamic Multi Frame Generation
14:DLSS Frame Generation
16:DLSS Ray Reconstruction
17: enhances image quality by using AI to generate additional pixels for intensive ray-traced scenes. DLSS replaces hand-tuned denoisers with an NVIDIA supercomputer-trained AI network that generates higher-quality pixels between sampled rays.
18:DLSS Super Resolution
19: boosts performance by using AI to output higher-resolution frames from a lower-r
[... 2353 more characters not shown]
```

**Sat 14 Nov 19:20:15 · Tool call: Bash** (List DLSS download links and NVIDIA UE page text)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; grep -oiE 'href="[^"]*"[^>]*>[^<]*(Download|Archive|Unreal|DLSS)[^<]*' nv_dlss.html | head -30; echo; grep -n -i "dlss\|reflex\|nvrtx\|plugin\|5\.8\|5\.9" nv_ue.txt | head -50
```

Result:

```
href="#getstarted" class="btn btn-cta me-2 mt-2">Download Now
href="https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/ue-dlss-5.8/8.9.0/2026.10.16_ue5.8_dlss4.5plugin_v8.9.0.zip" data-eula="https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf">Download UE 5.8 DLSS Plugin
href="https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/ue-dlss-5.7/8.9.0/2026.10.16_ue5.7_dlss4.5plugin_v8.9.0.zip" data-eula="https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf">Download UE 5.7 DLSS Plugin
href="https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/ue-dlss-5.6/8.9.0/2026.10.16_ue5.6_dlss4.5plugin_v8.9.0.zip" data-eula="https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf">Download UE 5.6 DLSS Plugin
href="https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/ue-dlss-5.5/8.9.0/2026.10.16_ue5.5_dlss4.5plugin_v8.9.0.zip" data-eula="https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf">Download UE 5.5 DLSS Plugin
href="https://forums.developer.nvidia.com/t/nvidia-dlss-unreal-engine-plugin-archive/377564" id="ibo07r" target="_blank">NVIDIA DLSS: Unreal Engine Plugin Archive
href="https://unity.com/download" id="i7zr2a" target="_blank">Download Unity 
href="#getstarted" class="btn btn-cta">Download

3: Read our latest blog about new Unreal Engine 5 on-device plugins for ACE, announced at Unreal Fest  
12:NVIDIA Plugins for Unreal Engine
13:NVIDIA plugins for Unreal Engine offer a streamlined way to access DLSS 4 and NVIDIA ACE.
14:NVIDIA DLSS 
15:NVIDIA DLSS is a suite of neural rendering technologies powered by GeForce RTX™ Tensor Cores that boosts frame rates while delivering crisp, high-quality images that rival native resolution. The Unreal Engine 5 plugin gives you access to new DLSS Multi Frame Generation, enhanced Ray Reconstruction, Super Resolution, and more.
16:Download DLSS Plugin for Unreal Engine 5 
18:NVIDIA ACE is a suite of digital human technologies that bring game characters and digital assistants to life with generative AI. Plugins for Audio2Face-3D, automatic speech recognition, small language models and text-to-speech samples are now available for Unreal Engine developers looking to bring their MetaHumans to life with generative AI on RTX PCs. 
19:Download NVIDIA ACE Plugin and Samples for Unreal Engine 5 
20:NVIDIA Reflex 
21
[... 959 more characters not shown]
```

**Sat 14 Nov 19:20:27 · Tool call: Bash** (Read NVIDIA DLSS plugin archive forum post)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
curl -sL -A "$UA" "https://forums.developer.nvidia.com/t/nvidia-dlss-unreal-engine-plugin-archive/377564.json" -o archive.json
python -I -c "
import json,re,html
d=json.load(open('archive.json',encoding='utf8'))
for p in d['post_stream']['posts'][:3]:
  t=html.unescape(re.sub(r'<[^>]+>',' ',p['cooked']));t=re.sub(r'\s+',' ',t)
  print(p['created_at'],p.get('updated_at'));print(t[:5000]);print('----')
"
```

Result:

```
2026-07-20T20:51:37.465Z 2026-10-15T18:25:24.116Z
 Access previous NVIDIA DLSS Unreal Engine Plugins Release date Plugin version Download links July 21, 2026 DLSS 4.5 Plugin 8.7.2 Unreal Engine 5.8 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 July 2, 2026 DLSS 4.5 Plugin 8.7.0 Unreal Engine 5.8 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 May 21, 2026 DLSS 4.5 Plugin 8.6.1 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 May 12, 2026 DLSS 4.5 Plugin 8.6.0 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 February 10, 2026 DLSS 4.5 Plugin 8.5.0 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 December 9, 2025 DLSS 4 Plugin 8.4.0 Unreal Engine 5.7 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 September 16, 2025 DLSS 4 Plugin 8.3.0 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 Unreal Engine 5.3 Unreal Engine 5.2 July 31, 2025 DLSS 4 Plugin 8.2.0 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 Unreal Engine 5.3 Unreal Engine 5.2 April 28, 2025 DLSS 4 Plugin 8.1.0 Unreal Engine 5.6 Unreal Engine 5.5 Unreal Engine 5.4 Unreal Engine 5.3 Unreal Engine 5.2 April 16, 2025 DLSS 4 Plugin 4.0.2 Unreal Engine 5.5 Unreal Engine 5.4 Unreal Engine 5.3 Unreal Engine 5.2 
----
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:20:34 · Tool call: WebSearch**

```
{
 "query": "DLSS plugin \"5.9\" Unreal Engine preview compile forums.developer.nvidia.com",
 "mode": "extended"
}
```

**Sat 14 Nov 19:20:35 · Tool call: WebSearch**

```
{
 "query": "MegaJam DLSS plugin Unreal 5.9 Preview NVIDIA jam",
 "mode": "extended"
}
```

Result:

```
Web search results for query: "MegaJam DLSS plugin Unreal 5.9 Preview NVIDIA jam"

Links: [{"title":"2026 Epic AI MegaJam - itch.io","url":"https://itch.io/jam/2026-epic-ai-megajam"},{"title":"アンリアルエンジン on X: \"Unreal Engine 5.9 MegaJam Previewが公開！🔛 注目の新機能はこちら： ・Unreal MCP強化！AIエージェントとの連携がさらに進化 ・Unreal CanvasでAIによる画像・3Dメッシュ生成 ・WebAssembly/WebGPUによるブラウザ実行に実験的対応 ・Lumen・Nanite・アニメーション機能もアップデート！ 詳細はこちらのプレビューロードマップ＆リリースノートより👇 #UnrealEngine #UE5 https://t.co/yl0vF3nugf https://t.co/1fuz6bk… / X","url":"https://x.com/UnrealEngineJP/status/2119973507312607717"},{"title":"John van der Burg on X: \"UE 5.9 preview 1 now ships with a new plugin I worked on called AnimGenOffline (name might change) which allows you to guide animations at high level and use AI to generate the actual frames. This integrates that functionality into Sequencer. As initial plugin into this sy… / X","url":"https://x.com/JohnnyB_222/status/2119878294749225179"},{"title":"Unreal Engine 5.9 MegaJam Preview - Announcements - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840"},{"title":"Unreal Engine 5.9 Preview Is Out & It Was Built With AI","url":"https://80.lv/articles/unreal-engine-5-9-preview-is-out-it-was-built-with-ai"},{"title":"ゲームメーカーズ on X: \"「Unreal Engine 5.9 MegaJam Preview」がリリース。プロジェクトをブラウザで実行可能に、エディタ内でのAIエージェント利用も https://t.co/oHOJrsJNXe ゲームジャム向けに用意されたプレビュー版。 Unreal MCPも更新し、LoreやFabと連携できるようになった\" / X","url":"https://twitter.com/GameMakersJP/status/2119835893431419122"},{"title":"11th November 2026 - EpicMegaJam26 by The Tech Absurdist","url":"https://tech-absurdist.itch.io/epicmegajam26/devlog/1772583/11th-november-2026"},{"title":"Epic AI MegaJam 2026: Dates, Rules, Prizes and an AI Prep Checklist","url":"https://vibestackweekly.com/epic-ai-megajam-2026/"},{"title":"NVIDIA and Unreal Engine 5","url":"https://developer.nvidia.com/UNrealengine"}]

I found no source describing a MegaJam-specific DLSS plugin for the 5.9 Preview. The results cover the Preview and NVIDIA's general Unreal support, so the DLSS details below are general rather than tied to the jam.

- **The Preview:** Epic released the 5.9 MegaJam Preview on November 9, 2026, for the 2026 Epic AI MegaJam, which runs November 12–15. It is described as the first engine release built mainly with agentic workflows, and it is marked as a preview that may be unstable.
- **NVIDIA's role:** The jam's NVIDIA award pages list DLSS 4.5 in Unreal Engine as one way to qua
[... 812 more characters not shown]
```

Result:

```
Web search results for query: "DLSS plugin "5.9" Unreal Engine preview compile forums.developer.nvidia.com"

Links: [{"title":"DLSS - error when building package unreal 5 - Platform & Builds - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/dlss-error-when-building-package-unreal-5/246733"},{"title":"UE5 Compiling Nvidia DLSS - Plugins - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/ue5-compiling-nvidia-dlss/496397"},{"title":"UE5-main and Nvidia DLSS - Pipeline & Plugins - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/ue5-main-and-nvidia-dlss/510307"},{"title":"Nvidia DLSS for UE5.0 Branch or Main - Plugins - Epic Developer Community Forums","url":"https://forums.unrealengine.com/t/nvidia-dlss-for-ue5-0-branch-or-main/496407"},{"title":"Release date for DLSS Unreal Engine 5.0.0 Engine Plugin","url":"https://forums.developer.nvidia.com/t/release-date-for-dlss-unreal-engine-5-0-0-engine-plugin/211240"},{"title":"Unreal Engine 5.5 <> DLSS 3.7.20 compilation error","url":"https://forums.developer.nvidia.com/t/unreal-engine-5-5-dlss-3-7-20-compilation-error/313797/15"},{"title":"Unreal Engine 5.5 <> DLSS 3.7.20 compilation error","url":"https://forums.developer.nvidia.com/t/unreal-engine-5-5-dlss-3-7-20-compilation-error/313797/57"},{"title":"DLSS 3.7.10 for Unreal Engine 5.4 crashes in VR with openXR","url":"https://forums.developer.nvidia.com/t/dlss-3-7-10-for-unreal-engine-5-4-crashes-in-vr-with-openxr/296014"},{"title":"Unreal Engine 5.5 <> DLSS 3.7.20 compilation error","url":"https://forums.developer.nvidia.com/t/unreal-engine-5-5-dlss-3-7-20-compilation-error/313797"},{"title":"UE5 5.6 - DLSS","url":"https://forums.developer.nvidia.com/t/ue5-5-6-dlss/333891?page=2"}]

The search didn't turn up anything about a DLSS plugin for Unreal Engine 5.9 or a preview build of it. The results cover earlier versions, mostly from NVIDIA's developer forums and Epic's forums.

- **UE 5.5 and DLSS 3.7.20:** A thread on NVIDIA's forums covers compile errors. One user worked around them by changing function call parameters, and a community member shared a patched build. A later NVIDIA moderator reply said the plugin had not yet been updated for UE 5.5. The NVIDIA moderator said they could not help because the plugin had not been updated for UE 5.5 yet.
- **UE 5.6:** A later thread notes that there's still no sign of the DLSS plugin for Unreal Engine 5.6. Another user reported that a DLSS 4 b
[... 612 more characters not shown]
```

**Sat 14 Nov 19:20:47 · Tool call: Bash** (Read UE 5.9 MegaJam Preview announcement)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
curl -sL -A "$UA" "https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840.json" -o ue59.json
python -I -c "
import json,re,html
d=json.load(open('ue59.json',encoding='utf8'))
p=d['post_stream']['posts'][0]
t=html.unescape(re.sub(r'<[^>]+>',' ',p['cooked']));t=re.sub(r'\s+',' ',t)
print(len(t));print(t[:2500])
for k in ['pscal','TSR','Temporal','third-party','Third','plugin','Plugin','DLSS','NVIDIA','Reflex','compat','API']:
  for m in re.finditer(k,t):
    print('==',k,':',t[max(0,m.start()-200):m.start()+300])
" | head -60; ls
```

Result:

```
4199
 unreal-engine-5-9-megajam-forum-header 1600�200 224 KB Download Unreal Engine 5.9 MegaJam Preview from the Epic Games Launcher , GitHub , or here for Linux. This isn�t a typical Unreal Engine Preview. We�ve been accumulating changes for rendering and animation in UE5 Main for an eventual 5.9 release next year. However, just a week ago, we decided to start working on a UE 5.9 Preview in time for the 2026 Epic AI MegaJam on November 12�15. This UE 5.9 MegaJam Preview is the first Unreal Engine release built primarily with agentic workflows. A handful of people directed fleets of agents to port the AI tooling from our UE6 development branch and implement Web as a target platform. Agents wrote the web platform code, starting from UE4�s retired HTML5 platform, with engineers directing, reviewing, and testing the work. We�re using this release to learn how to build the engine with multiple people directing swarms of agents working in parallel� and we still have lots to learn. Having said that, we�re already seeing benefits from this approach, and it allows us to deliver more UE5 releases with faster bug fixes and development on targeted features, all without pulling focus from UE6. This Preview had about a week of development and a shorter QA pass than usual. We�re still cleaning up some of the agent-written code, and parts of the web renderer are prototypes we plan to refactor before the full 5.9 release ships. As with all Previews, expect rough edges, missing pieces, and things that break. Test it out during the Epic AI MegaJam or on a copy of your project and tell us what bugs you find: we�ll be fixing issues throughout the preview period, with agents helping us triage and turn reports around quickly. Key feature overview Updates to Unreal MCP (Experimental) Unreal MCP launches automatically with the editor, delivers more reliable connections, and expands its toolsets to support rendering, source control, profiling, debugging, gameplay testing, geometry, audio, UI, and level creation. New integrations with Lore enable AI agents to manage project changes and automate source control workflows, while the new Fab toolset lets agents search the catalog, browse your library, and install free or purchased assets directly into your projects. Unreal Assistant (Experimental) Work with your preferred AI coding agent, including Claude Code, Codex, Cursor, or OpenCode, directly in the in-editor assistant panel in Unreal Editor and connected to Unreal MCP to streaml
[... 1185 more characters not shown]
```

**Sat 14 Nov 19:20:56 · Tool call: Bash** (Find engine versions and upscaler interface in 5.9)

```
ls /d/UE/; cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "class ITemporalUpscaler\|SetTemporalUpscalerInterface\|GetTemporalUpscalerInterface" --include=*.h . | head; grep -rn "class FSceneViewFamily" Engine/Public/SceneView.h | head -2
```

Result:

```
Builds
Projects
UE_5.8
UE_5.9
_farm1
_scrapped_floodline
megajam-2026-devlog
megascans_dl
ref
wt
./Engine/Public/SceneView.h:44:class ITemporalUpscaler;
./Engine/Public/SceneView.h:2694:	inline void SetTemporalUpscalerInterface(UE::Renderer::Private::ITemporalUpscaler* InTemporalUpscalerInterface)
./Engine/Public/SceneView.h:2701:	inline const UE::Renderer::Private::ITemporalUpscaler* GetTemporalUpscalerInterface() const
./Renderer/Private/PostProcess/TemporalAA.h:29:	// Uses third party View.Family->GetTemporalUpscalerInterface()
./Renderer/Private/SceneRendering.h:181:	class ITemporalUpscaler;
./Renderer/Public/TemporalUpscaler.h:12:class ITemporalUpscaler : public ISceneViewFamilyExtention
27:class FSceneViewFamily;
31:class FSceneViewFamily;
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:21:19 · Tool call: Bash** (Diff upscaler-related engine headers 5.8 vs 5.9)

```
A=/d/UE/UE_5.8/Engine; B=/d/UE/UE_5.9/Engine; grep -E "Minor|Patch|Changelist\"" $A/Build/Build.version; for f in Source/Runtime/Renderer/Public/TemporalUpscaler.h Source/Runtime/Engine/Public/SceneViewExtension.h Source/Runtime/D3D12RHI/Public/ID3D12DynamicRHI.h Source/Runtime/D3D11RHI/Public/ID3D11DynamicRHI.h Source/Runtime/VulkanRHI/Public/IVulkanDynamicRHI.h Source/Runtime/Engine/Public/LegacyScreenPercentageDriver.h Source/Runtime/Engine/Public/SceneViewExtensionContext.h Source/Runtime/RHI/Public/DynamicRHI.h Source/Runtime/Renderer/Public/ScreenPass.h Source/Runtime/Renderer/Public/PostProcess/PostProcessInputs.h Source/Runtime/SlateRHIRenderer/Public/Interfaces/ISlateRHIRendererModule.h Source/Runtime/RHICore/Public/RHICoreShader.h; do if [ -f $A/$f ] && [ -f $B/$f ]; then n=$(diff $A/$f $B/$f | grep -c '^[<>]'); echo "$n  $f"; else echo "missing in one: $f ($( [ -f $A/$f ] && echo 58) $( [ -f $B/$f ] && echo 59))"; fi; done
```

Result:

```
"MinorVersion": 8,
	"PatchVersion": 4,
	"Changelist": 58902052,
	"CompatibleChangelist": 55116800,
0  Source/Runtime/Renderer/Public/TemporalUpscaler.h
5  Source/Runtime/Engine/Public/SceneViewExtension.h
0  Source/Runtime/D3D12RHI/Public/ID3D12DynamicRHI.h
missing in one: Source/Runtime/D3D11RHI/Public/ID3D11DynamicRHI.h ( )
1  Source/Runtime/VulkanRHI/Public/IVulkanDynamicRHI.h
0  Source/Runtime/Engine/Public/LegacyScreenPercentageDriver.h
0  Source/Runtime/Engine/Public/SceneViewExtensionContext.h
22  Source/Runtime/RHI/Public/DynamicRHI.h
4  Source/Runtime/Renderer/Public/ScreenPass.h
missing in one: Source/Runtime/Renderer/Public/PostProcess/PostProcessInputs.h ( )
0  Source/Runtime/SlateRHIRenderer/Public/Interfaces/ISlateRHIRendererModule.h
0  Source/Runtime/RHICore/Public/RHICoreShader.h
```

**Sat 14 Nov 19:21:34 · Tool call: Bash** (Show header diffs 5.8 to 5.9)

```
A=/d/UE/UE_5.8/Engine; B=/d/UE/UE_5.9/Engine; for f in Source/Runtime/Engine/Public/SceneViewExtension.h Source/Runtime/VulkanRHI/Public/IVulkanDynamicRHI.h Source/Runtime/RHI/Public/DynamicRHI.h Source/Runtime/Renderer/Public/ScreenPass.h; do echo "=== $f"; diff $A/$f $B/$f | grep '^[<>]' | cut -c1-200; done
```

Result:

```
=== Source/Runtime/Engine/Public/SceneViewExtension.h
> 	 * Called right before translucency is drawn when using the deferred renderer.
> 	 */
> 	virtual void PreRenderTranslucencyDeferred_RenderThread(FRDGBuilder& GraphBuilder, const FSceneView& View) {};
> 
> 	/**
=== Source/Runtime/VulkanRHI/Public/IVulkanDynamicRHI.h
> 	virtual FTextureRHIRef   RHICreateTexture2DFromAndroidHardwareBuffer(AHardwareBuffer* HardwareBuffer, EPixelFormat Format, ETextureCreateFlags Flags) = 0;
=== Source/Runtime/RHI/Public/DynamicRHI.h
> #include "RHIDeviceAnalytics.h"
> 	/**
> 	 * Snapshot of the device-side capability and extension surface this RHI exposes, in a generic RHI-agnostic shape.
> 	 * Users are expected to cache the result, since the payload can be thousands of KV entries.
> 	 */
> 	virtual void RHIGetDeviceAnalytics(FRHIDeviceAnalytics& OutDeviceAnalytics) const
> 	{
> 	}
> 	virtual FRHIOpacityMicromapArraySize RHICalcOpacityMicromapArraySize(const FRHIOpacityMicromapArrayDesc& Initializer)
> 	{
> 		checkNoEntry();
> 		return {};
> 	}
> 
> 
> 	virtual FOpacityMicromapArrayRHIRef RHICreateOpacityMicromapArray(FRHICommandListBase& RHICmdList, const FRHIOpacityMicromapArrayDesc& Initializer)
> 	{
> 		checkNoEntry();
> 		return nullptr;
> 	}
< 	return GDynamicRHI->GetInterfaceType();
> 	return GDynamicRHI ? GDynamicRHI->GetInterfaceType() : ERHIInterfaceType::NotSet;
=== Source/Runtime/Renderer/Public/ScreenPass.h
> 	const EShaderPlatform ShaderPlatform;
> 		, ShaderPlatform(GetFeatureLevelShaderPlatform(InFeatureLevel))
< 	FGlobalShaderMap* ShaderMap = GetGlobalShaderMap(ViewInfo.FeatureLevel);
> 	FGlobalShaderMap* ShaderMap = GetGlobalShaderMap(ViewInfo.ShaderPlatform);
```

**Sat 14 Nov 19:21:46 · Tool call: Bash** (Measure renderer and D3D12 source churn 5.8 to 5.9)

```
A=/d/UE/UE_5.8/Engine/Source/Runtime; B=/d/UE/UE_5.9/Engine/Source/Runtime; for d in Renderer/Private Renderer/Public D3D12RHI/Private D3D12RHI/Public RHI/Public Engine/Public/SceneView.h; do echo "$d: $(diff -rq $A/$d $B/$d 2>/dev/null | wc -l) files differ, $(find $B/$d -type f | wc -l) files in 5.9"; done; ls $B/D3D12RHI/Private | head -5; diff -q $A/Renderer/Private/PostProcess/TemporalAA.h $B/Renderer/Private/PostProcess/TemporalAA.h; diff -q $A/Renderer/Private/SceneTextureParameters.h $B/Renderer/Private/SceneTextureParameters.h; diff -q $A/D3D12RHI/Private/D3D12RHIPrivate.h $B/D3D12RHI/Private/D3D12RHIPrivate.h; diff -q $A/Renderer/Private/ScenePrivate.h $B/Renderer/Private/ScenePrivate.h; diff -q $A/Renderer/Private/SceneRendering.h $B/Renderer/Private/SceneRendering.h
```

Result:

```
Renderer/Private: 321 files differ, 746 files in 5.9
Renderer/Public: 16 files differ, 53 files in 5.9
D3D12RHI/Private: 29 files differ, 107 files in 5.9
D3D12RHI/Public: 1 files differ, 5 files in 5.9
RHI/Public: 19 files differ, 68 files in 5.9
Engine/Public/SceneView.h: 1 files differ, 1 files in 5.9
D3D12Access.h
D3D12Adapter.cpp
D3D12Adapter.h
D3D12Allocation.cpp
D3D12Allocation.h
Files /d/UE/UE_5.8/Engine/Source/Runtime/D3D12RHI/Private/D3D12RHIPrivate.h and /d/UE/UE_5.9/Engine/Source/Runtime/D3D12RHI/Private/D3D12RHIPrivate.h differ
Files /d/UE/UE_5.8/Engine/Source/Runtime/Renderer/Private/ScenePrivate.h and /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/ScenePrivate.h differ
Files /d/UE/UE_5.8/Engine/Source/Runtime/Renderer/Private/SceneRendering.h and /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Private/SceneRendering.h differ
```

**Sat 14 Nov 19:22:03 · Tool call: WebSearch**

```
{
 "query": "\"DLSS.Build.cs\" OR \"DLSSUtility\" OR \"StreamlineCore\" Unreal plugin source \"Renderer/Private\" github",
 "mode": "extended"
}
```

Result:

```
Web search results for query: ""DLSS.Build.cs" OR "DLSSUtility" OR "StreamlineCore" Unreal plugin source "Renderer/Private" github"

Links: [{"title":"Upgrades and builds the DLSS Unreal Engine Plugin from 5.2 to 5.3 · GitHub","url":"https://gist.github.com/coderespawn/16e761a006fedf2e341cc9f17a10971d"},{"title":"GitHub - andrsnn/js-unreal-engine-game-bridge: Run an unchanged three.js browser game inside Unreal Engine 5.8. Build on the web in seconds, ship with Unreal. · GitHub","url":"https://github.com/andrsnn/js-unreal-engine-game-bridge"},{"title":"NVIDIA Unreal Engine DLSS Frame Generation Plugin (Streamline)","url":"https://d29g4g2dyqv443.cloudfront.net/sites/default/files/DLSS_Frame_Generation_Quick_Start_Guide.pdf"},{"title":"NVIDIA Unreal Engine DLSS Frame Generation Plugin (Streamline) Guide","url":"https://manuals.plus/m/470609a57f72ad2dad394f43ff708bcc50c68d1f84310221b0904263230aaa1e"},{"title":"How I Fixed NVIDIA DLSS Plugin Compilation for Unreal Engine 5.8 - A Senior Game Developer's Complete Step-by-Step Guide to Resolving Streamline DLSS Frame Generation Crashes and Build Errors with Proven Patch Workarounds - Dre Dyson","url":"https://dredyson.com/how-i-fixed-nvidia-dlss-plugin-compilation-for-unreal-engine-5-8-a-senior-game-developers-complete-step-by-step-guide-to-resolving-streamline-dlss-frame-generation-crashes-and-build-errors-with-pr/"},{"title":"DLSS 3.7.10 for Unreal Engine 5.4 crashes in VR with openXR","url":"https://forums.developer.nvidia.com/t/dlss-3-7-10-for-unreal-engine-5-4-crashes-in-vr-with-openxr/296014"},{"title":"The Hidden Truth About DLSS Plugin Compilation for Unreal Engine 5.8 - A Complete Definitive Guide to Resolving Epic's Breaking Changes and Community Workarounds - Dre Dyson","url":"https://dredyson.com/the-hidden-truth-about-dlss-plugin-compilation-for-unreal-engine-5-8-a-complete-definitive-guide-to-resolving-epics-breaking-changes-and-community-workarounds/"},{"title":"Content Creation / Rendering","url":"https://developer.nvidia.com/blog/?p=65089"},{"title":"UE5.6 - World Partition HLOD generation fails when StreamlineCore Plugin is enabled (UE5.6 - DLSS4 8.2.0 and 8.3.0)","url":"https://forums.developer.nvidia.com/t/ue5-6-world-partition-hlod-generation-fails-when-streamlinecore-plugin-is-enabled-ue5-6-dlss4-8-2-0-and-8-3-0/345368"}]

The search didn't find a GitHub page containing `DLSS.Build.cs` or `DLSSUtility`, so I couldn't confirm the exact file layout. It did turn up some related material.

- **P
[... 1128 more characters not shown]
```

**Sat 14 Nov 19:22:21 · Tool call: Bash** (Fetch third-party mirror of DLSS 4.5 UE manual)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
curl -sL -A "$UA" "https://manuals.plus/nvidia/dlss-4-5-for-unreal-engine-manual" -o mp45.html; python -I ../txt.py mp45.html mp45.txt; wc -c mp45.txt; grep -n -iE "r\.NGX|r\.Streamline|cvar|console|uplugin|SetDLSSMode|IsDLSS|Supported|Plugins|5\.[4-9]|DLAA|r\.ScreenPercentage|Library" mp45.txt | head -80
```

Result:

```
532 mp45.txt
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:22:33 · Tool call: Bash** (Check manual mirror and fetch NVIDIA FG quick start PDF)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; cat mp45.txt | head -20; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"; mkdir -p pdf; curl -sL -A "$UA" "https://d29g4g2dyqv443.cloudfront.net/sites/default/files/DLSS_Frame_Generation_Quick_Start_Guide.pdf" -o pdf/fg_quickstart.pdf; file pdf/fg_quickstart.pdf; ls -la pdf | awk '{print $5,$9}'
```

Result:

```
Security check | Manuals+
Manuals+
User Manuals Simplified.
A quick safety check
One quick check.
Then back to the manual.
We need to verify this request before allowing access. This helps keep the manuals open to everyone.
Enable JavaScript and cookies to complete the security check.
Enable JavaScript and cookies to continue
Complete the challenge to continue to the requested page.
Back to Manuals+
Ray ID:
 a5a5a35b9deb86a5
Your IP:
 [ip].203.182
Region:
 SG
A little protection for a lot of know-how.
 pdf/fg_quickstart.pdf: PDF document, version 1.4
 
0 .
0 ..
8231041 fg_quickstart.pdf
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:22:43 · Tool call: Bash** (Extract text from FG quick start PDF)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; python -I -c "
import sys
try:
  import pypdf
  r=pypdf.PdfReader('pdf/fg_quickstart.pdf');t='\n'.join(p.extract_text() or '' for p in r.pages)
except ImportError:
  import fitz; d=fitz.open('pdf/fg_quickstart.pdf'); t='\n'.join(p.get_text() for p in d)
open('fg_quickstart.txt','w',encoding='utf8').write(t);print(len(t))
"; head -c 4000 fg_quickstart.txt
```

Result:

```
24137
NVIDIA Unreal Engine DLSS Frame Generation Plugin (Streamline)
DLSS3 and the NVIDIA Unreal Engine DLSS Frame Generation Plugin
The NVIDIA 
DLSS Frame Generation
 plugin is part of a wider suite of related NVIDIA performance and image quality improving technologies and corresponding NVIDIA Unreal Engine plugins:
NVIDIA 
Deep Learning Supersampling Frame Generation (DLSS-FG)
 boosts frame rates by using AI to render additional frames. 
DLSS-FG
 requires a Geforce RTX 40 series graphics card.
NVIDIA 
Deep Learning Supersampling Super Resolution (DLSS-SR)
 boosts frame rates by rendering fewer pixels and using AI to output high resolution frames. 
DLSS-SR
 requires an NVIDIA RTX graphics card.
NVIDIA 
Deep Learning Anti-Aliasing (DLAA)
 is used to improve image quality. 
DLAA
 requires an NVIDIA RTX graphics card.
NVIDIA 
Image Scaling (NIS)
 provides best-in class upscaling and sharpening for non-RTX GPUs, both NVIDIA or 3rd party. Please refer to the NVIDIA 
Image Scaling
 Unreal Engine plugin for further details. NVIDIA
DLSS 3 combines DLSS Super Resolution, DLSS Frame Generation, and NVIDIA Reflex.
The NVIDIA Unreal Engine DLSS Frame Generation plugin (documented here) provides:
DLSS Frame Generation (also called DLSS-G or DLSS-FG)
NVIDIA Reflex
The NVIDIA Unreal Engine DLSS-SR plugin (available separately) provides:
DLSS Super Resolution (DLSS-SR)
Deep Learning Anti-Aliasing (DLAA)
The NVIDIA Unreal Engine NIS plugin (available separately) provides:
NVIDIA Image Scaling
Integration recommendation
The DLSS Frame Generation plugin is supported "out of the box" by Unreal Engine 5.2, including packaged engine releases from Epic.
For 5.1 and earlier engine releases, additional source changes to the engine itself must be made to support the DLSS Frame Generation plugin. We recommend that the integration is done by an engineer who has some understanding of
rebuilding Unreal Engine from source code as well as merging code snippets into the engine code itself.
Quickstart DLSS3 Frame Generation
Note: DLSS Frame Generation and the Reflex implementation are provided together through a "Streamline" library, so the plugin's name is Streamline.
UE 5.2
1
. 
Copy the entire Streamline plugin folder somewhere under the engine's Plugins\Marketplace folder or under your source project's Plugins folder
For a packaged engine release from Epic, copy the plugin somewhere under the engine's Engine\Plugins\Marketplace folder
For 
[... 1561 more characters not shown]
```

**Sat 14 Nov 19:22:51 · Tool call: Bash** (Extract cvars and API names from FG guide)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; tr '\n' ' ' < fg_quickstart.txt | grep -oE "(r|t)\.[A-Za-z]+(\.[A-Za-z0-9]+)+|-sl[a-zA-Z]+|Query[A-Za-z]+|Is[A-Za-z]*Supported|Set[A-Za-z]*Mode|Get[A-Za-z]*Mode|NVIDIA Streamline supported [01]|watermark[^.]*\.|Development[^.]*\.|Shipping[^.]*\." | sort | uniq -c | sort -rn | head -60
```

Result:

```
3 r.Streamline.ClearSceneColorAlpha
      3 NVIDIA Streamline supported 1
      2 t.Streamline.Reflex.HandleMaxTickRate
      2 t.Streamline.Reflex.Auto
      2 r.Streamline.Editor.TagUIColorAlpha
      1 watermarks and are intended to be used for applications shipped to end users.
      1 watermarks and are intended to be used during application development and are a requirement to use the Streamline debugoverlay.
      1 t.Streamline.Reflex.Mode
      1 t.Streamline.Reflex.EnableInEditor
      1 t.Streamline.Reflex.Enable
      1 r.streamline.dlssg.enable
      1 r.Streamline.ViewIdOverride
      1 r.Streamline.UnregisterReflexPlugin
      1 r.Streamline.TagUIColorAlphaThreshold
      1 r.Streamline.TagUIColorAlpha
      1 r.Streamline.TagSceneColorWithoutHUD
      1 r.Streamline.MotionVectorScale
      1 r.Streamline.Editor.TagSceneColorWithoutHUD
      1 r.Streamline.DilateMotionVectors
      1 r.Streamline.DLSSG.Enable
      1 r.Streamline.DLSSG.AdjustMotionBlurTimeScale
      1 r.Streamline.CustomCameraNearPlane
      1 r.Streamline.CustomCameraFarPlane
      1 Shipping builds with the  Plugins -> NVIDIA DLSS Frame   Generation -> Load Debug Overlay  option in Project Settings.
      1 SetReflexMode
      1 SetDLSSGMode
      1 QueryReflexSupport
      1 QueryDLSSGSupport
      1 IsReflexSupported
      1 IsDLSSGSupported
      1 IsDLSSGModeSupported
      1 GetSupportedDLSSGMode
      1 GetReflexMode
      1 GetDefaultReflexMode
      1 GetDefaultDLSSGMode
      1 GetDLSSGMode
      1 Development/Debug builds, but won't appear in Shipping builds.
      1 Development binaries.
      1 Development  and  Streamline\Binaries\ThirdParty\Win64\Debug  paths respectively.
      1 -slnodebugoverlay
      1 -slloglevel
      1 -sllogconsole
      1 -sldebugoverlay
      1 -slbinaries
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:22:55 · Tool call: WebSearch**

```
{
 "query": "\"r.NGX.DLSS.Enable\" OR \"r.NGX.DLAA.Enable\" OR \"UDLSSLibrary\" Unreal DLSS plugin documentation",
 "mode": "standard"
}
```

Result:

```
Web search results for query: ""r.NGX.DLSS.Enable" OR "r.NGX.DLAA.Enable" OR "UDLSSLibrary" Unreal DLSS plugin documentation"

Links: [{"title":"Turning off DLSS by default in Unreal Engine 5.3 and getting current DLSS mode","url":"https://forums.developer.nvidia.com/t/turning-off-dlss-by-default-in-unreal-engine-5-3-and-getting-current-dlss-mode/292520"},{"title":"UE5 5.6 - DLSS","url":"https://forums.developer.nvidia.com/t/ue5-5-6-dlss/333891?page=2"},{"title":"forums.unrealengine.com","url":"https://forums.unrealengine.com/t/i-am-losing-performance-with-dlss/213214"},{"title":"Live FX Documentation","url":"https://assimilate.gitbook.io/live-fx-documentation/unreal-engine/unreal-optimization/dlss"},{"title":"Nvidia dlss on ndisplay ?","url":"https://forums.unrealengine.com/t/nvidia-dlss-on-ndisplay/746163"},{"title":"how to turn off DLSS?","url":"https://forums.unrealengine.com/t/how-to-turn-off-dlss/2481396"},{"title":"Simulation / Modeling / Design","url":"https://developer.nvidia.com/blog/?p=24048"},{"title":"unrealengine.com","url":"https://forums.unrealengine.com/t/has-anyone-got-dlss-working-for-5-1-1-having-lots-of-troubles-with-it/1318731"},{"title":"How to turn off DLSS in unreal engine?","url":"https://forums.developer.nvidia.com/t/how-to-turn-off-dlss-in-unreal-engine/331819"},{"title":"Simulation / Modeling / Design","url":"https://developer.nvidia.com/blog/tips-getting-the-most-out-of-the-dlss-unreal-engine-4-plugin/"},{"title":"NVIDIA DLSS","url":"https://developer.nvidia.com/rtx/dlss?ncid=ref-inor-937552"},{"title":"DLSS 3.5 Plugin - Unreal","url":"https://360igloo.atlassian.net/wiki/x/BIAb1"},{"title":"r.NGX.Automation.Enable Enable automation for NGX DLSS image quality and performance evaluation. (default = 0)","url":"https://pitch-scapula-66c.notion.site/DLSS-Settings-1054d4307e3680e6ac15da36fd9b560a"},{"title":"forums.unrealengine.com","url":"https://forums.unrealengine.com/t/how-to-turn-off-dlss/2481396/6"},{"title":"getting started with nvidia dlss 3.7 for ue 5.0","url":"https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/getting-started-with-nvidia-dlss-3.7-for-ue-5.0.pdf"},{"title":"forums.unrealengine.com","url":"https://forums.unrealengine.com/t/dlss-is-not-working/763228/10"},{"title":"Unable to get DLSS to work in VR","url":"https://forums.developer.nvidia.com/t/unable-to-get-dlss-to-work-in-vr/250211"},{"title":"r/OptimizedGaming • u/TheHybred Verified Optimizer • Dec 29 '23","url":"https://reddit.rtr
[... 1798 more characters not shown]
```

**Sat 14 Nov 19:23:10 · Tool call: Bash** (Read NVIDIA forum thread on DLSS mode control)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
cat > ../forum.py <<'EOF'
import json,re,html,sys
d=json.load(open(sys.argv[1],encoding='utf8'))
for p in d['post_stream']['posts']:
  t=html.unescape(re.sub(r'<[^>]+>',' ',p['cooked']));t=re.sub(r'\s+',' ',t)
  print('['+p['created_at'][:10]+' '+p['username'][:3]+'..]',t[:int(sys.argv[2]) if len(sys.argv)>2 else 1500]);print()
EOF
curl -sL -A "$UA" "https://forums.developer.nvidia.com/t/turning-off-dlss-by-default-in-unreal-engine-5-3-and-getting-current-dlss-mode/292520.json" -o f1.json; python -I ../forum.py f1.json 1800
```

Result:

```
[2024-05-10 pap..]  Hi, Is there a way to turn off DLSS(3.7) by default in Unreal Engine 5.3? It seems like it is turned on by default but I would prefer it to be turned off(and turning it on runtime later). Is there also a way the get the currently used DLSS mode? I can�t find any Blueprint node which would return the current mode used. Kind regards, Szilard 

[2024-05-13 Mar..]  Hello @papp.szilard and welcome to the NVIDIA developer forums. If the DLSS plugin is enabled, then, depending on the screenpercentage used and whether super resolution is enabled in global project settings, it will default to one of the DLSS presets. But all the details on how to enable or disable it, how to integrate DLSS specific blueprints into your project and much more can be found in the extensive documentation that is part of the plugin you downloaded. For example DLSS_Super_Resolution_Quick_Start_Guide.pdf contains all the basic information about the things you asked above. Thanks! 

[2024-05-13 pap..]  Hi Markus, Thank you for the quick response. I guess I would need to add n.NGX.DLSS.Enable 0 to DefaultEngine.ini to disable it by default? I haven�t found a blueprint node that would just tell me which one is the currently used mode to be honest. Kind regards, Szilard 

[2024-05-13 Mar..]  I am afraid r.NGX.DLSS.Enable is read-only. There is a good reason for that, I just can�t find right now what it was exactly. In any case, I am not the UE expert but if I open the sample project that is also part of the DLSS plugin package and do �Find in Blueprints� with the search term DLSS I get a lot of results, some pointing to the blueprints that control the on-screen DLSS stats when you run the demo project. I hope that might help. 

[2024-05-13 pap..]  The DLSS_Super_Resolution_Quick_Start_Guide.pdf only states n.NGX.Enable as read only and does not mention anything about n.NGX.DLSS.Enable. I searched for all the DLSS nodes before, but none of them returns the currently used mode. 

[2024-05-14 Mar..]  You are right regarding r.NGX.enable vs r.NGX.DLSS.enable I guess, not quite sure right now. I�ll see if I can get someone more familiar with these to comment or give advice. Meanwhile, did you check out the Webinar series we have on the different UE features ? Maybe you find some helpful answers there as well. 

[2024-05-14 pap..]  Hi Markus, Thank you for all the help. It seems like adding �n.NGX.DLSS.Enable=0� to the DefaultEngine.ini disables DLSS on start-up. Doi
[... 1968 more characters not shown]
```

**Sat 14 Nov 19:23:25 · Tool call: Bash** (Read forum threads on 5.8 compile and DLSS 5)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"
curl -sL -A "$UA" "https://forums.developer.nvidia.com/t/any-hero-who-can-compile-it-for-5-8/370193.json" -o f2.json; python -I ../forum.py f2.json 1200 | head -60; echo =========; curl -sL -A "$UA" "https://forums.developer.nvidia.com/t/official-dlss-5-neural-rendering-plugin-access-for-unreal-engine-5-8-2/382731.json" -o f3.json; python -I ../forum.py f3.json 1000 | head -30
```

Result: [withheld: it showed NVIDIA plugin source, which the plugin's licence keeps private]

### Sat 14 Nov 19:23:34 · Agent (claude-opus-5-5)

Next: the NVIDIA RTX SDK licence text (public PDF linked from the download buttons), for redistribution, logo and watermark terms.

**Sat 14 Nov 19:23:38 · Tool call: Bash** (Fetch and scan public NVIDIA RTX SDK licence)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"; curl -sL -A "$UA" "https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf" -o pdf/rtx_lic.pdf; file pdf/rtx_lic.pdf; python -I -c "
import pypdf
r=pypdf.PdfReader('pdf/rtx_lic.pdf');t='\n'.join(p.extract_text() or '' for p in r.pages)
open('rtx_lic.txt','w',encoding='utf8').write(t);print(len(t), len(r.pages))
"; grep -n -iE "distribut|attribut|logo|trademark|watermark|notice|credit|free|charge|open source|reverse|developer program|terminat|debug|confidential|audit|report" rtx_lic.txt | head -70
```

Result:

```
pdf/rtx_lic.pdf: PDF document, version 1.7, 7 page(s)
27272 7
19:c. Distribute any software and materials within the SDK, other than developer tools provided for your internal use , as 
20:incorporated in object code format into a software application subject to the distribution requirements indicated in this 
23:2. DISTRIBUTION REQUIREMENTS. These are the distribution requirements for you to exercise the grants above: 
25:b. The following notice shall be included in modifications and derivative works of source code distributed: “This software 
27:c. You agree to distribute the SDK subject to the terms at least as protective as the terms of this license , including (without 
30:d. You agree to notify NVIDIA in writing of any known or suspected distribution or use of the SDK not in compliance with the 
31:requirements of this license, and to enforce the terms of your agreements with respect to the distributed portions of the SDK.  
38:a. You may not reverse engineer, decompile or disassemble, or remove copyright or other proprietary notices from any 
40:b. Except as expressly provided in this license, you may not copy, sell, rent, sublicense, transfer, distribute, modify, or create 
41:derivative works of any portion of the SDK. For clarity, you may not distribute or sublicense the SDK as a stand-alone product. 
46:e. You may not use the SDK in any manner that would cause it to become subject to an open source software license. As 
47:examples, licenses that require as a condition of use, modification, and/or distribution that the SDK be: (i) disclosed or 
48:distributed in source code form; (ii) licensed for the purpose of making derivative works; or (iii) redistributable at no cha rge. 
64:without prior notice to you. Whil e NVIDIA generally maintains compatibility between versions, NVIDIA may in some cases 
72:development and terminate the availability of a pre-release SDK at any time without liability. 
74:7. THIRD-PARTY COMPONENTS. The SDK may include third-party components with separate legal notices or terms as may be 
75:described in proprietary notices accompanying the SDK . If and to the extent there is a conflict between the terms in this 
89:modifications, feature requests or other feedback regarding the SDK. Feedback, even if designated as confidential by you, 
90:shall not create any confidentiality obligation for NVIDIA. If you provide Feedback, you hereby grant NVIDIA, its affiliates and 
91:its designees a non -exclusive, perpetual, irrevo
[... 3727 more characters not shown]
```

**Sat 14 Nov 19:23:44 · Tool call: Bash** (Read licence grant, DLSS supplement and trademark terms)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; sed -n 1,35p rtx_lic.txt; echo .....; sed -n 165,300p rtx_lic.txt
```

Result:

```
NVIDIA RTX SDKs LICENSE 
 
This license is a legal agreement between you and NVIDIA Corporation ("NVIDIA") and governs the use of the NVIDIA RTX 
software development kits, including the DLSS SDK, NGX SDK, RTXGI SDK, RTXDI SDK , RTX Video SDK and/or NRD SDK, if and 
when made available to you under this license (in each case, the “SDK”). 
This license can be accepted only by an adult of legal age of majority in the country in which the SDK is used. If you are under 
the legal age of majority, you must ask your parent or legal guardian to consent to this license. If you are entering this license 
on behalf of a company or other legal entity, you represent that you have legal authority and “you” will mean the entity you 
represent.  
By using the SDK, you affirm that you have reached the legal age of majority , you accept th e terms of th is license, and you 
take legal and financial responsibility for the actions of your permitted users.  
 
You agree to use the SDK only for purposes that are permitted by (a) th is license, and (b) any applicable law, regulation or 
generally accepted practices or guidelines in the relevant jurisdictions. 
1. LICENSE. Subject to the terms of this license  and the terms in the supplement attached,  NVIDIA hereby grants you a non -
exclusive, non-transferable license, without the right to sublicense (except as expressly provided in this license) to:  
a. Install and use the SDK, 
b. Modify and create derivative works of sample source code delivered in the SDK, and 
c. Distribute any software and materials within the SDK, other than developer tools provided for your internal use , as 
incorporated in object code format into a software application subject to the distribution requirements indicated in this 
license. 
 
2. DISTRIBUTION REQUIREMENTS. These are the distribution requirements for you to exercise the grants above: 
a. An application must have material additional functionality, beyond the included portions of the SDK.  
b. The following notice shall be included in modifications and derivative works of source code distributed: “This software 
contains source code provided by NVIDIA Corporation.”  
c. You agree to distribute the SDK subject to the terms at least as protective as the terms of this license , including (without 
limitation) terms relating to the license grant , license restrictions and protection of NVIDIA’s intellectual property rights. 
Additionally, you agree that you will protect the privacy, security a
[... 12514 more characters not shown]
```

**Sat 14 Nov 19:24:00 · Tool call: Bash** (Read watermark and support query passages)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; tr '\n' ' ' < fg_quickstart.txt | sed 's/  */ /g' | grep -oE ".{500}(watermark|slbinaries|won't appear in Shipping).{400}" | head -4; echo; tr '\n' ' ' < fg_quickstart.txt | sed 's/  */ /g' | grep -oE ".{300}(Query[A-Za-z]*Support|QueryDLSSGSupport).{600}" | head -2
```

Result:

```
Options And Console Variables and Commands Note : UE DLSS Frame Generation plugin modules are loaded very early during engine startup, before console variables are available. As such, various debugging settings are exposed via command line options instead of console variables. Selecting Streamline binary flavor By default Streamline uses signed production binaries (e.g.  sl.interposer.dll ,  sl.common.dll ) from the  Streamline\Binaries\ThirdParty\Win64\ path. They have no on-screen watermarks and are intended to be used for applications shipped to end users. They are always packaged by the UE Streamline plugin. For non-shipping UE builds, alternate binaries can be selected via  -slbinaries={development,debug} command line argument, corresponding to the  Streamline\Binaries\ThirdParty\Win64\Development and  Streamline\Binaries\ThirdParty\Win64\Debug paths respectively. They ha
Generation" plugin. Here, toggle the "Load Debug Overlay" option for a fast and convenient way to confirm that DLSS Frame Generation is working, along with real time statistics. 3 .  In this same settings window, ensure the "Allow OTA Update" option is enabled, which will automatically update Streamline as well as DLSS's AI algorithms with the latest improvements. 4 .  Note that the Debug Overlay for Frame Generation will work in the editor and can appear in Development/Debug builds, but won't appear in Shipping builds. 5 .  In the Unreal Editor, Frame Generation only works from a New Editor Window (PIE) or Standalone mode, it doesn't work from the Selected Viewport or while editing. 6 .  We recommend that when Frame Generation is on, Vsync should be off in your application. The DLSS 3 plugin can set Vsync to behave incorrectly when active. Vsync can be disabled with the r.vsync 0 console command.

 the DLSS Frame Generation plugins's modular features by default. Reflex Blueprint library The  Reflex (Streamline) /  UStreamlineLibraryReflex blueprint library is the recommended way to query whether Reflex is supported and also provides functions to configure Reflex IsReflexSupported ,  QueryReflexSupport SetReflexMode ,  GetReflexMode ,  GetDefaultReflexMode GetGameToRenderLatencyInMs ,  GetGameLatencyInMs , GetRenderLatencyInMs Console Variables (low level) It can be configured with the following console variables t.Streamline.Reflex.Enable Enable Streamline Reflex extension. (default = 0) 0: Disabled 1: Enabled t.Streamline.R
[... 1224 more characters not shown]
```

**Sat 14 Nov 19:24:13 · Tool call: Bash** (Inspect D3D12 private and SceneView header diffs)

```
A=/d/UE/UE_5.8/Engine/Source/Runtime; B=/d/UE/UE_5.9/Engine/Source/Runtime; diff $A/D3D12RHI/Private/D3D12RHIPrivate.h $B/D3D12RHI/Private/D3D12RHIPrivate.h | grep '^[<>]' | head -20; echo; diff -rq $A/Renderer/Public $B/Renderer/Public | sed 's|.*Runtime/Renderer/Public/||;s| and .*||' ; diff -q $A/Engine/Public/SceneView.h $B/Engine/Public/SceneView.h && echo same; diff $A/Engine/Public/SceneView.h $B/Engine/Public/SceneView.h | grep '^[<>]' | head -30
```

Result:

```
< #include "D3D12Shader.h"
> #include "D3D12Shaders.h"
> // Forward declare ASDCore's PSDB registration wrapper. Full definition in ASDPSDBRegistration.h
> namespace ASDCore { class FShaderCacheRegistration; }
> 
> 	virtual void RHIGetDeviceAnalytics(FRHIDeviceAnalytics& OutDeviceAnalytics) const override;
> #if D3D12RHI_SUPPORTS_OPACITY_MICROMAPS
> 	virtual FRHIOpacityMicromapArraySize RHICalcOpacityMicromapArraySize(const FRHIOpacityMicromapArrayDesc& Initializer) final override;
> 	virtual FOpacityMicromapArrayRHIRef RHICreateOpacityMicromapArray(FRHICommandListBase& RHICmdList, const FRHIOpacityMicromapArrayDesc& Initializer) final override;
> #endif
> 
> 	ASDCore::FShaderCacheRegistration* GetOrCreateASDShaderCacheRegistration();
> 
> 
> 	ASDCore::FShaderCacheRegistration* ASDShaderCacheRegistration = nullptr;

Only in /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Public: CurveSkinning
FXRenderingUtils.h differ
InstanceCulling/InstanceCullingContext.h differ
MaterialShader.h differ
MeshPassProcessor.h differ
MeshPassProcessor.inl differ
Only in /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Public: MeshPassProcessorPSOValidation.h
PrimitiveSceneInfo.h differ
RayTracingDynamicGeometryUpdateManager.h differ
RayTracingGeometryInstance.h differ
RayTracingInstance.h differ
RayTracingInstanceBufferUtil.h differ
RayTracingMeshDrawCommands.h differ
RendererUtils.h differ
ScreenPass.h differ
Only in /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Public: ShadowDepthCaptureView.h
Files /d/UE/UE_5.8/Engine/Source/Runtime/Engine/Public/SceneView.h and /d/UE/UE_5.9/Engine/Source/Runtime/Engine/Public/SceneView.h differ
< 	
> 
> 	/**
> 	 * Optional explicit ShaderPlatform. When set to a value other than SP_NumPlatforms,
> 	 * FSceneView uses it directly. Otherwise FSceneView falls back to
> 	 * ViewFamily->GetShaderPlatform() (or GMaxRHIShaderPlatform when ViewFamily is null).
> 	 */
> 	EShaderPlatform ShaderPlatform;
> 
> 		, ShaderPlatform(SP_NumPlatforms)
< 	SHADER_PARAMETER(FVector4f, RectLightAtlasSizeAndInvSize)
> 	SHADER_PARAMETER(FVector2f, RectLightAtlasSize)
> 	SHADER_PARAMETER(FUintVector2, RectLightAtlasSizeUint)
< 
< 	/** DEPRECATED all instanced stereo is now what used to be called multi viewport.
< 	 * use IsInstancedStereo() instead.
< 	 * True if mobile multi-viewport is enabled. */
< 	UE_DEPRECATED(5.9, "all instanced stereo is now what used to be called multi viewport. IsInstancedStereo() should be used")
< 	bool bIsMultiViewportEnabled;
< 	/** Feature le
[... 243 more characters not shown]
```

**Sat 14 Nov 19:24:20 · Tool call: Bash** (Check FeatureLevel overloads still exist in 5.9)

```
B=/d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "GetGlobalShaderMap(ERHIFeatureLevel\|inline FGlobalShaderMap\* GetGlobalShaderMap" $B/RenderCore/Public/GlobalShader.h | head; grep -n "FeatureLevel;" $B/Engine/Public/SceneView.h | head -5; grep -n "bIsMultiViewportEnabled" -r $B/Engine/Public | head -3
```

Result:

```
360:inline FGlobalShaderMap* GetGlobalShaderMap(ERHIFeatureLevel::Type FeatureLevel)
1932:	const ERHIFeatureLevel::Type FeatureLevel;
2110:	ERHIFeatureLevel::Type GetFeatureLevel() const { return FeatureLevel; }
```

**Sat 14 Nov 19:24:27 · Tool call: WebSearch**

```
{
 "query": "NVIDIA DLSS Unreal plugin download requires NVIDIA Developer Program login account \"secure\"",
 "mode": "standard"
}
```

Result:

```
Web search results for query: "NVIDIA DLSS Unreal plugin download requires NVIDIA Developer Program login account "secure""

Links: [{"title":"nvidia dlss for unreal engine 2069","url":"https://www.pugetsystems.com/labs/articles/nvidia-dlss-for-unreal-engine-2069/"},{"title":"www.pugetsystems.com","url":"https://www.pugetsystems.com/?p=8257"},{"title":"getting started with nvidia dlss 3.7 for ue 5.1","url":"https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/getting-started-with-nvidia-dlss-3.7-for-ue-5.1.pdf"},{"title":"getting started with nvidia dlss 3.7 for ue 5.0","url":"https://developer.nvidia.com/downloads/assets/gameworks/downloads/secure/dlss/getting-started-with-nvidia-dlss-3.7-for-ue-5.0.pdf"},{"title":"DLSS 3.5 Plugin - Unreal","url":"https://360igloo.atlassian.net/wiki/x/BIAb1"},{"title":"Nvidia releases DLSS 4 plugin for Unreal Engine 5, offering multi frame generation and more","url":"https://www.neowin.net/amp/nvidia-releases-dlss-4-plugin-for-unreal-engine-5-offering-multi-frame-generation-and-more/"},{"title":"Content Creation / Rendering","url":"https://developer.nvidia.com/blog/?p=65089"},{"title":"nvidia introduces official dlss plugin for unreal engine","url":"https://www.guru3d.com/news-story/nvidia-introduces-official-dlss-plugin-for-unreal-engine.html"},{"title":"Nvidia introduces official DLSS plugin for Unreal Engine","url":"https://guru3d.com/story/nvidia-introduces-official-dlss-plugin-for-unreal-engine"},{"title":"nvidia s dlss 4 is now available for unreal engine 5","url":"https://80.lv/articles/nvidia-s-dlss-4-is-now-available-for-unreal-engine-5"},{"title":"NVIDIA DLSS","url":"https://developer.nvidia.com/rtx/dlss?page=1"},{"title":"Nvidia DLSS 3: Jetzt auch für die Unreal Engine 5 erhältlich","url":"https://www.pcgameshardware.de/Deep-Learning-Super-Sampling-Software-277618/News/DLSS-3-fuer-Unreal-Engine-5-1422669/"},{"title":"Official DLSS 5 Neural Rendering plugin access for Unreal Engine 5.8.2","url":"https://forums.developer.nvidia.com/t/official-dlss-5-neural-rendering-plugin-access-for-unreal-engine-5-8-2/382731"},{"title":"Private & Confidential","url":"https://360igloo.atlassian.net/wiki/spaces/IGLOOTOOLS/pages/3558572036/DLSS+3.5+Plugin+-+Unreal"},{"title":"Content Creation / Rendering","url":"https://developer.nvidia.com/blog/now-available-nvidia-dlss-3-for-unreal-engine-5/"},{"title":"Content Creation / Rendering","url":"https://developer.nvidia.com/blog/?p=29474"},{"title":"nvidia dls
[... 2027 more characters not shown]
```

**Sat 14 Nov 19:24:40 · Tool call: Bash** (Read NVIDIA DLSS 4.5 for UE5 blog)

```
S="C:/Users/USER/AppData/Local/Temp/claude/ce66ae306241b5fa/680a7dbf-7ec3-4ad2-888f-a07720c19df4/scratchpad/web"; cd "$S"; UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140 Safari/537.36"; curl -sL -A "$UA" "https://developer.nvidia.com/blog/whats-new-for-game-developers-in-nvidia-rtx-dlss-4-5-for-ue5-and-multilingual-ai-characters/" -o blog45.html; python -I ../txt.py blog45.html blog45.txt; grep -n -iE "driver|RTX 20|RTX 40|RTX 50|5\.[5-9]|super resolution|plugin|preset|model|reflex" blog45.txt | head -40
```

Result:

```
28: adds multilingual AI character capabilities with new models optimized for on-device performance through the NVIGI SDK 1.6 update.
31: arrives as an Unreal Engine plugin with Dynamic Multi Frame Generation, a new 6x mode, and the second-generation transformer model for Super Resolution.
33: 5.7.4 improves stability and compatibility with fixes for RTX Mega Geometry shader compilation, Opacity Micro-Map stability, Substrate material integration, and NvAPI issues.
39:DLSS 4.5 Unreal Engine plugin
40: to adopt Dynamic Multi Frame Generation and the latest Super Resolution updates.
42:NvRTX 5.7.4
43: for improved stability when integrating RTX features into Unreal Engine 5.7.4 projects.
51: 4.5 arrives as an Unreal Engine (UE) plugin, bringing Dynamic Multi Frame Generation, a new 6x mode, and the second-generation transformer model for Super Resolution. And the
53: gets a stability-focused 5.7.4 release that tightens compatibility across NVIDIA RTX technologies.
58:Figure 1. NVIDIA ACE is a suite of efficient AI models and tooling designed to help middleware and game developers build knowledgeable, actionable and conversational in-game characters
59:ACE now features new multilingual models to ensure a global audience can experience a next level of immersion with game characters in their native languages. Access the latest models optimized for on-device performance with the 
63: This cutting-edge small language model (SLM) delivers low latency, contextually aware responses across 201 languages and dialects, ensuring characters react to player instructions with best-in-class accuracy.
65: This high-performance speech recognition model enables characters to understand and transcribe 
71:, this model provides characters with expressive, emotionally resonant voices that pulls a global audience deeper into their gaming interactions.
72:In addition, NVIGI 1.6 enables you to quickly prototype Day 1 models with new functionality that connects to a locally running llama.cpp server. 
76:NVIDIA DLSS 4.5 Unreal Engine plugin adds support for Dynamic Multi Frame Generation 
78:DLSS 4.5 Unreal Engine plugin
80:DLSS 4.5 Dynamic Multi Frame Generation, Multi Frame Generation 6x Mode, and the second-generation transformer for Super Resolution
82:Figure 2. NVIDIA DLSS 4.5 introduces Dynamic Multi Frame Generation new 6x Multi Frame Generation mode, and the second-generation transformer for Super Resolution, now available for Unreal Engine developers
83:The plugin provides di
[... 1283 more characters not shown]
```

**Sat 14 Nov 19:24:47 · Tool call: Bash** (Read owner note and submission package facts)

```
cd "[notes]/unreal/megajam-2026"; sed -n 255,272p GAME.md; echo; grep -n -iE "shipping|development|package|zip|1 GB|credits|splash|title" SUBMISSION.md | head -20; ls lanes | grep -iE "settings|menu|ui"
```

Result:

```
that looks for its own files in a personal folder filters by time and type, never lists the folder.

**14 Nov 19:24. feel4 DONE (verified: head `6359fc6`, tracked tree clean, Dev package 18:45 and Shipping 19:06
both after the last commit, reference line 6 times in its logs, 121 tests by its report). PLAY FOLDER = feel4 Dev
build, mirrored 19:24 (no Supercut process running).** In: wall marks, chips and shells that stay (B6), hit shove
slides (B7), `StepRate` footstep pace (B10), kill chain semitone steps (B11). Polish list from its handoff: shells
are real size and read as specks (wants a shell scale tuning line); landed chips look like dark dice;
`HitChipSeconds` 0.9 -> 3.0; kill chain never heard. Merge hot spots with feel5: `ASupercutCharacter::StartReload`
(shell drop vs B13 auto reload) and the end-of-frame confirm sound code. Dev package folder is 1.08 GB (exe 347
MB): check the SHIPPING zip size against the 1 GB limit at the next package. feel5 head `5a371d0` (B8, B9
committed; handoff still to come). Testers' copies ([pc-c], [pc-b] `C:\SupercutPlaytest`) NOT updated yet.

**14 Nov 19:23. gen1 DONE; gen2 STARTED (plan A, bake); uiref1 round 1 reported.** gen1 final: 16 modules, 15,000
rooms checked with and without props (14,999 fair first try, 1 re-roll), checker self-test 49/49, 70 rooms load in
a packaged build, 9 played to the gate by script, `test_vectors.json` 51 pairs; `lanes/gen1/PORT.md` (plan A bake
3-4 h; B1 10-14 h; B2 +12-16 h). Its picks stand `[taste: owner review]`: puzzle on odd depths, fight on even;
one Marksman a room; 400 cm walls; a blocking prop 101-110 cm high is never placed; no room where the player can
stand within 200 cm of a wall top; flats swap only for props >= 150 cm (none today). Worth adding later for the

15:| Build | `TeamName_GameName.zip`, packaged Windows development build, under 1 GB |
23:- [ ] Packaged build runs on a clean Windows 10 or 11 machine with nothing else installed
24:- [ ] Zip under 1 GB, named `TeamName_GameName.zip`
37:- [ ] The entry is a Shipping build, and its open ports were checked (a Development build opens TCP 1985 and
38:      Windows Firewall prompts the judge). Checked once on the Shipping test zip of 14 Nov (lane `perf2`, pc2:
39:      no listening TCP or UDP port in 355 samples over full runs). Check the final zip again before ticking
61:| Hyper3D Rodin (Gen-2.5 API) | set-dressing props from reference pictures: desk lamp, craft knife, director's chair and ten more (ruler, pencil, glu
[... 713 more characters not shown]
```

**Sat 14 Nov 19:25:12 · Tool call: Bash** (Check how scalability sets screen percentage)

```
cd /d/UE/UE_5.9/Engine/Config; grep -n -A6 "^\[ResolutionQuality\|^\[AntiAliasingQuality@3\]" BaseScalability.ini | head -30; grep -n "ScreenPercentage" BaseScalability.ini | head; grep -n "ResolutionQuality\|ScreenPercentage\|ResolutionScale" /d/UE/Projects/Supercut59/Source/Supercut/SupercutUserSettings.cpp | head
```

Result:

```
39:[ResolutionQuality]
40-!ResolutionPresets=CLEAR_ARRAY
41-; Use the project's default screen percentage
42-+ResolutionPresets=(Name="Default",ResolutionQuality=0.0)
43-; 1080.0f / 2160.0f = 50%
44-+ResolutionPresets=(Name="Performance",ResolutionQuality=50.0)
45-; 1260.0f / 2160.0f - 0.1f / 2160.0f = 58.328%
--
85:[AntiAliasingQuality@3]
86-r.FXAA.Quality=4
87-r.TemporalAA.Quality=2
88-r.TSR.History.R11G11B10=1
89-r.TSR.History.ScreenPercentage=200
90-r.TSR.History.UpdateQuality=3
91-r.TSR.ShadingRejection.Flickering=1
10:; Note: [ResolutionQuality] isn't using the usual 0/1/2/3 quality levels, the value directly maps to r.ScreenPercentage.
56:r.TSR.History.ScreenPercentage=100
67:r.TSR.History.ScreenPercentage=100
78:r.TSR.History.ScreenPercentage=100
89:r.TSR.History.ScreenPercentage=200
100:r.TSR.History.ScreenPercentage=200
587:r.Bloom.ScreenPercentage=25.000
609:r.Bloom.ScreenPercentage=35.355
644:r.Bloom.ScreenPercentage=50.000
681:r.Bloom.ScreenPercentage=50.000
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:25:19 · Tool call: Bash** (Find default screen percentage settings)

```
cd /d/UE/UE_5.9/Engine/Config; grep -n "ScreenPercentage.Default\|r.AntiAliasingMethod" BaseEngine.ini BaseDeviceProfiles.ini Windows/*.ini 2>/dev/null | head
```

Result:

```
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:25:23 · Tool call: Bash** (Find default screen percentage cvars in source)

```
cd /d/UE/UE_5.9/Engine/Source/Runtime; grep -rn "TEXT(\"r.ScreenPercentage.Default" --include=*.cpp . | head -8
```

Result:

```
./Engine/Private/LegacyScreenPercentageDriver.cpp:13:	TEXT("r.ScreenPercentage.Default"), 100.f,
./Engine/Private/LegacyScreenPercentageDriver.cpp:18:	TEXT("r.ScreenPercentage.Default.Desktop.Mode"), int32(EScreenPercentageMode::BasedOnDisplayResolution),
./Engine/Private/LegacyScreenPercentageDriver.cpp:23:	TEXT("r.ScreenPercentage.Default.Mobile.Mode"), int32(EScreenPercentageMode::Manual),
./Engine/Private/LegacyScreenPercentageDriver.cpp:28:	TEXT("r.ScreenPercentage.Default.VR.Mode"), int32(EScreenPercentageMode::Manual),
./Engine/Private/LegacyScreenPercentageDriver.cpp:33:	TEXT("r.ScreenPercentage.Default.PathTracer.Mode"), int32(EScreenPercentageMode::Manual),
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:25:40 · Tool call: Bash** (Check farm mirror rules for plugin Binaries folders)

```
cd "[notes]/unreal/megajam-2026/farm"; ls; grep -n -iE "Binaries|Intermediate|exclude|/XD|robocopy|rsync|Plugins" farm.sh remote/*.ps1 2>/dev/null | head -30
```

Result:

```
farm.sh
mirror.py
remote
remote/list.ps1:5:$skip = '^(Intermediate|Binaries|Saved|DerivedDataCache|\.git)(\|$)'
```

**Sat 14 Nov 19:25:44 · Tool call: Bash** (Read mirror skip logic)

```
cd "[notes]/unreal/megajam-2026/farm"; grep -n -iE "Binaries|Intermediate|skip|SKIP|prune|delete|DEL_ROOTS|Source|Content" mirror.py | head -30; cat remote/list.ps1 | head -20
```

Result:

```
4:sends Intermediate, Binaries, Saved, DerivedDataCache or .git, and deletes files under Source, Content, Config, Tools
13:SKIP = {"Intermediate", "Binaries", "Saved", "DerivedDataCache", ".git"}
14:PRUNE = ("Source/", "Content/", "Config/", "Tools/", "Script/")
38:        if top in SKIP:
51:    gone = sorted(r for r in remote if r not in local and r.startswith(PRUNE))
54:        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8", newline="\n") as lf:
68:        if "deleted" not in out:
69:            sys.exit(f"FARM delete failed: {out}")
70:    print(f"FARM mirror {host}:{dest} sent {len(send)} files ({nbytes / 1e6:.1f} MB), deleted {len(gone)}, "
# farm mirror helper: prints relpath|size|mtime (unix seconds, UTC) for every file of a mirror, skipping the folders
# the mirror never sends. Prints nothing when the folder does not exist yet.
param([Parameter(Mandatory)][string]$Dir)
if (-not (Test-Path $Dir)) { exit 0 }
$skip = '^(Intermediate|Binaries|Saved|DerivedDataCache|\.git)(\|$)'
$n = $Dir.TrimEnd('\').Length + 1
$e = [DateTime]::new(1970, 1, 1, 0, 0, 0, [DateTimeKind]::Utc)
$w = [Console]::Out
Get-ChildItem -LiteralPath $Dir -Recurse -File -Force | ForEach-Object {
    $r = $_.FullName.Substring($n)
    if ($r -notmatch $skip) { $w.WriteLine("$($r.Replace('\','/'))|$($_.Length)|$([long][Math]::Floor(($_.LastWriteTimeUtc - $e).TotalSeconds))") }
}
```

**Sat 14 Nov 19:25:47 · Tool call: Bash** (Read how mirror decides top folder)

```
cd "[notes]/unreal/megajam-2026/farm"; sed -n 30,45p mirror.py
```

Result:

```
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
        if os.path.isfile(p):
            st = os.stat(p)
            local[top] = (st.st_size, int(st.st_mtime))
            continue
        for d, dirs, files in os.walk(p):
```

**Sat 14 Nov 19:26:15 · Tool call: Bash** (Read 5.9 temporal upscaler interface)

```
sed -n 1,80p /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Public/TemporalUpscaler.h; grep -n "PostRenderViewFamily_RenderThread\|BeginRenderViewFamily\|PreRenderViewFamily_RenderThread" /d/UE/UE_5.9/Engine/Source/Runtime/Engine/Public/SceneViewExtension.h
```

Result:

```
// Copyright Epic Games, Inc. All Rights Reserved.

#pragma once

#include "ScreenPass.h"
#include "SceneView.h"

namespace UE::Renderer::Private
{

/** Interface for implementing third party temporal upscaler. */
class ITemporalUpscaler : public ISceneViewFamilyExtention
{
public:

	/** Ref counted history to be saved in the history. */
	class IHistory : public IRefCountedObject
	{
	public:
		virtual ~IHistory() = default;

		/** Debug name of the history. Must exactly point to the same const TCHAR* as ITemporalUpscaler::GetDebugName().
		 * This is used for debugging GPU memory uses of a viewport, but also to ensure IHistory is fed to a compatible ITemporalUpscaler.
		 */
		virtual const TCHAR* GetDebugName() const = 0;

		/** Size of the history on the GPU in bytes. */
		virtual uint64 GetGPUSizeBytes() const = 0;
	};

	/** Inputs of the temporal upscaler. */
	struct FInputs
	{
		/** Outputs view rect that must be on FOutputs::FullRes::ViewRect. */
		FIntRect OutputViewRect;

		/** Pixel jitter offset of the rendering pixel. */
		FVector2f TemporalJitterPixels;

		/** Pre exposure of the SceneColor. */
		float PreExposure = 1.0f;

		/** The post-DOF and pre-MotionBlur SceneColor. */
		FScreenPassTexture SceneColor;

		/** The scene depth. */
		FScreenPassTexture SceneDepth;

		/** The scene velocity. */
		FScreenPassTexture SceneVelocity;

		/** Texture that contain eye adaptation on the red channel. */
		FRDGTextureRef EyeAdaptationTexture = nullptr;

		/** The history of the previous frame set by FOutputs::NewHistory. PrevHistory->GetDebugName() is guarentee to match the ITemporalUpscaler. */
		TRefCountPtr<IHistory> PrevHistory;
	};

	/** Outputs of the third party temporal upscaler. */
	struct FOutputs
	{
		/** Output of the temporal upscaler. FullRes.ViewRect must match FInputs::OutputViewRect. */
		FScreenPassTexture FullRes;

		/** New history to be kept alive for next frame. NewHistory->GetDebugName() must exactly point to the same const TCHAR* as ITemporalUpscaler::GetDebugName(). */
		TRefCountPtr<IHistory> NewHistory;
	};

	virtual ~ITemporalUpscaler() = default;

	/** Debug name of the history. Must exactly point to the same const TCHAR* as ITemporalUpscaler::IHistory::GetDebugName(). */
	virtual const TCHAR* GetDebugName() const = 0;

	/** Adds the necessary passes into RDG for temporal upscaling the rendering resolution to desired output res. */
	virtual FOutputs AddPasses(
		FRDGBuilder& GraphBuilder,
		const FSceneView& View,
		const FIn
[... 451 more characters not shown]
```

### Sat 14 Nov 19:26:48 · Agent (claude-opus-5-5)

I have what I need. Writing the plan, the build brief, the log and the handoff now.

**Sat 14 Nov 19:26:48 · Tool call: Bash** (Get clock time for log)

```
date "+%H:%M"
```

Result:

```
19:26
```

**Sat 14 Nov 19:28:45 · Tool call: Write**

[input withheld: it held NVIDIA plugin source, which the plugin's licence keeps private]

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\dlss1\PLAN.md (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:28:51 · Tool call: Bash** (Check game repo and worktree layout read only)

```
cd /d/UE/Projects/Supercut59; ls -d .git 2>&1; git -C /d/UE/Projects/Supercut59 rev-parse --abbrev-ref HEAD 2>&1 | head -1; ls /d/UE/wt | head; cat .gitignore 2>/dev/null | head -20
```

Result:

```
.git
ue59
feel5
feel5_farmlogs
gen2
props1
props1_farmlogs
props1_stage
sfx2
shell1
shell1_farmlogs
vfx1
# Unreal Engine build output and caches
Binaries/
Build/
DerivedDataCache/
Intermediate/
Saved/
.vs/
*.sln
*.suo
*.VC.db
*.opensdf
*.sdf
*.xcworkspace
*.xcodeproj

# Tuning.txt and its template, when an editor build reads or writes them in the project folder
/Tuning.txt
/Tuning.example.txt
Shell cwd was reset to [notes]
```

**Sat 14 Nov 19:30:08 · Tool call: Write**

````
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\BUILD_BRIEF.md",
 "content": "GLASSBOX-MEGAJAM-2026 lane=dlss2\n\n# Build brief: DLSS Super Resolution and DLAA in SUPERCUT\n\nYou add NVIDIA DLSS Super Resolution and DLAA to SUPERCUT as a player option: OFF, DLAA, QUALITY, BALANCED,\nPERFORMANCE. The game must start and play exactly as today on a PC without an NVIDIA RTX card. Do the work yourself;\nstart no subagents. Read the research first: `unreal/megajam-2026/lanes/dlss1/PLAN.md` (in\n`[notes]`). It says which facts are checked and which are guesses.\n\n## Why\n\nThe game is an entry in the 2026 Epic AI MegaJam (submissions close Monday 16 Nov 2026, 09:59 Singapore time; feature\nstop Sunday afternoon). The \"Render Royalty: NVIDIA RTX Award\" needs one NVIDIA feature, and \"NVIDIA DLSS\" is on the\nlist. Super Resolution is enough.\n\n## Facts\n\n- Engine: `D:\\UE\\UE_5.9`, an installed build of the UE 5.9 MegaJam Preview (not a source build). Never edit it.\n- Game repo: `D:\\UE\\Projects\\Supercut59` (branch `ue59`). You work only in your own worktree, `D:\\UE\\wt\\dlss2`, made\n  from the current head of `ue59`. Never edit `D:\\UE\\Projects\\Supercut59` itself.\n- Build: `Tools\\build.ps1` (editor target), `Tools\\build.ps1 -Target Supercut` (game target). Package:\n  `cmd /c Tools\\package.cmd` (Development) and `cmd /c Tools\\package_shipping.cmd` (Shipping, the judge build).\n  Scripted run: `Tools\\run_demo.ps1` (read its header). Tests: `Tools\\run_tests.ps1`. These scripts name\n  `D:\\UE\\Builds`: in a worktree, check where your package lands before you trust a result, and never overwrite\n  another lane's build folder.\n- c4 (this PC) has an AMD RX 9070 XT. The only RTX card on the farm is [pc-b] (RTX 4080 Super). Farm use is in\n  `unreal/megajam-2026/FARM.md`: read all of it before your first farm step, and follow its load checks.\n- The plugin zip, downloaded by the owner: `D:\\UE\\dl\\dlss\\2026.10.16_ue5.8_dlss4.5plugin_v8.9.0.zip`. It is the DLSS 4.5\n  plugin v8.9.0 built for UE 5.8. There is no 5.9 build. If the file is missing, stop and say so.\n- The sketch look: when the player claps, the scene freezes and the post-process material `M_SketchFreeze` (blendable\n  location after tonemapping, made by `Tools/make_assets.py`) draws outlines and hatching.\n  `Source/Supercut/SupercutCharacter.cpp` holds it and `FSupercutStillFrame`, which turns off the camera jitter while\n  the sketch shows. Do not change either unless step 9 says so.\n- Settings: `Source/Supercut/SupercutUserSettings.h/.cpp` (the engine's `GameUserSettings`, four values today). A\n  settings menu is being designed by another lane; keep your UI change to one row, or none if that lane owns the\n  screen (ask the main thread).\n\n## Rules\n\n- Never accept a licence, sign in anywhere, or download anything. The owner already did the download.\n- Never put the plugin or its source into a public repo, the dev log export, or a chat paste. The NVIDIA licence\n  forbids it.\n- Plugin names, function names and console variables in this brief are from older plugin versions. Before you use\n  one, find it in the plugin's headers or PDFs and write file and line into your HANDOFF. If it differs, use what\n  the files say.\n- No fallbacks in core code. If the plugin is missing or fails to load on an RTX card, log it clearly. On a non-NVIDIA\n  card \"unsupported\" is the normal state, not an error.\n- Unreal and agents notes go in `unreal/GOTCHAS.md` and `unreal/FINDINGS.md` as the Unreal `AGENTS.md` says.\n- Your lane folder: `unreal/megajam-2026/lanes/dlss2/` (`LOG.md` with clock times from `date`, `HANDOFF.md`).\n- Commit in your worktree only (private repo). No push anywhere.\n- **Timebox:** if the plugin does not build on 5.9 and pass step 7 by **Sunday 15 Nov 11:00 SGT**, stop, revert\n  your plugin commits, and report. Do not leave a half-working DLSS in the game.\n\n## Steps\n\n### 1. Read the plugin (30 min)\n\n1. Unzip to a fresh scratch folder outside the worktree (not under `D:\\UE\\Projects`).\n2. Read the PDFs that come with it (Super Resolution quick start, Streamline guide, release notes). Note in `LOG.md`:\n   the plugin folders, each `.uplugin`'s `\"Modules\"`, `\"Plugins\"` dependencies and `\"EngineVersion\"`, the Blueprint\n   library for DLSS (expected `UDLSSLibrary`), its support query and reason enum, the mode functions, the console\n   variables that enable DLSS and DLAA, the minimum driver, which DLLs each feature needs, and whether any DLL is a\n   watermarked development flavour.\n3. Decide the smallest set of plugins Super Resolution and DLAA need. Leave out Frame Generation, Reflex, DeepDVC,\n   NIS, Movie Render Queue support and samples, unless a needed plugin depends on them.\n\n### 2. Put it in the worktree (30 min)\n\n1. Copy that set into `<worktree>\\Plugins\\`.\n2. Delete each copied plugin's `Binaries\\Win64` and `Intermediate` (5.8 editor builds). Keep `Binaries\\ThirdParty`.\n3. Set `\"EngineVersion\"` to `\"5.9.0\"` in each copied `.uplugin` that has the field.\n4. **Git trap:** the game's `.gitignore` has an unanchored `Binaries/` and `Build/`. They would drop the plugin's\n   `Binaries\\ThirdParty` DLLs from git, and a clean checkout would package without them. Add negations so\n   `Plugins/<name>/Binaries/ThirdParty/**` is tracked and the plugins' `Binaries/Win64` stays ignored. Check with\n   `git status --ignored` and `git check-ignore -v <one DLL path>` that every NVIDIA DLL is tracked. If one file is\n   over 100 MB, say so in HANDOFF (it would block a later GitHub push).\n5. `Supercut.uproject`: add the plugin(s) to `\"Plugins\"` with `\"Enabled\": true`.\n6. `Source/Supercut/Supercut.Build.cs`: add the module that exports the DLSS Blueprint library to\n   `PrivateDependencyModuleNames`.\n\n### 3. Compile (timebox 3 h)\n\n1. `Tools\\build.ps1`, then `Tools\\build.ps1 -Target Supercut`.\n2. Fix errors in the plugin source with the smallest edit each. List every edit in HANDOFF (file, line, why). Look\n   first for these 5.9 changes, found on disk by lane dlss1: `D3D12Shader.h` renamed to `D3D12Shaders.h`\n   (`Engine/Source/Runtime/D3D12RHI/Private`); `FSceneView::bIsMultiViewportEnabled` removed. Also the\n   `EWindowType::GameWindow` deprecation a 5.8 community patch met (should already be fixed in the official 5.8\n   build). `ITemporalUpscaler` (`Renderer/Public/TemporalUpscaler.h`) is unchanged from 5.8.4.\n3. Do not touch the engine. If a fix needs an engine change, stop and report.\n\n### 4. Game code (1.5 to 2 h)\n\n1. `USupercutUserSettings`: one saved value `DlssMode`, an enum or int, 0 OFF, 1 DLAA, 2 QUALITY, 3 BALANCED,\n   4 PERFORMANCE, default OFF. Getter, setter, a name function for the log (\"OFF\", \"DLAA\", ...).\n2. Apply it in `ApplyAndSave` **after** the scalability groups are applied: applying scalability sets\n   `r.ScreenPercentage` from the `ResolutionQuality` group (`Engine/Config/BaseScalability.ini`), which would undo the\n   DLSS mode. Set it through the plugin's own API. OFF must really turn DLSS off (a 2024 forum report says OFF after\n   DLAA kept DLAA running: check by test, step 7).\n3. At start, ask the plugin whether DLSS is supported and why not. If not supported, keep the mode OFF in memory and\n   never call the mode setter. Do not write OFF over the player's saved choice on an unsupported PC (they may move\n   the save to an RTX PC; low stakes either way, your pick, say which).\n4. Command line `-SupercutDLSS=<off|dlaa|quality|balanced|performance>`: for this run only, not saved. Same parsing\n   style as the other `-Supercut...` flags (`SupercutPlayerController.cpp`, `SupercutUserSettings.h IsSizeForced`).\n5. Log lines (category `LogSupercut`), once at start and on each change:\n   - `DLSS support: <reason name> (min driver <version>)`\n   - `DLSS mode: <NAME> screen percentage <value>`\n6. Proof the upscaler ran: in a `FWorldSceneViewExtension` (extend `FSupercutStillFrame` or add one),\n   `PostRenderViewFamily_RenderThread` reads `InViewFamily.GetTemporalUpscalerInterface()` (`SceneView.h`) and logs\n   `DLSS upscaler: <GetDebugName() or none>` when it changes. Log at most on change, never per frame.\n7. Credits / title: one plain-text line \"NVIDIA DLSS\" where the game lists credits or on the title screen. **No NVIDIA\n   logo or badge art**: the licence needs NVIDIA's written approval two weeks ahead for marks. Mark it\n   `[owner decision]` in HANDOFF.\n8. Settings row, if the main thread says the row is yours: label `DLSS`, values `OFF`, `DLAA`, `QUALITY`, `BALANCED`,\n   `PERFORMANCE`; on an unsupported PC the row is greyed with value `UNAVAILABLE`. No helper text.\n   `[taste: owner review]`.\n9. Tests in the game's test style (`Source/Supercut/*Tests.cpp`): the setting clamps and round-trips through the\n   file; the command-line parse; the name function. Run `Tools\\run_tests.ps1`; all must pass.\n\n### 5. Add `-DLSS` to `Tools\\run_demo.ps1`\n\nA `[string]$DLSS = \"\"` parameter that, when set, adds `-SupercutDLSS=$DLSS` to the game's arguments. Update the\nheader's usage line. Nothing else in the script changes.\n\n### 6. Reference line before you start changing behaviour\n\nAt your worktree's starting head (before step 2), package and run the reference script on c4 once and save the\n`RUN wrapped` and `FPS` lines and the shots. FARM.md lists the reference at game head `683bff6`:\n`RUN wrapped: takes 1, time 98.2 s, shots 46, freezes 14, kills 17` (main8, seed 1, FixedFps 240). The head has moved\nsince; use your own baseline.\n\n### 7. c4 check: AMD, no change (1 h)\n\nWith the plugin in, Development package, then:\n\n```powershell\npowershell -File Tools\\run_demo.ps1 -Packaged -Exe <your package>\\Windows\\Supercut.exe -Run main8 -Seed 1 `\n  -Script <worktree>\\Script\\main8.txt -FixedFps 240 -Silent -Log <lane logs>\\c4_off.log -Shots <lane logs>\\c4_off_shots\n```\n\nPass:\n\n- the game starts, no error dialog, no missing-DLL line in the log,\n- `DLSS support:` names a not-supported reason, `DLSS upscaler: none`,\n- `RUN wrapped` equals your step 6 baseline,\n- the `FPS` line within 5% of the baseline,\n- shots match the baseline shots (pixel diff; same shot index; only the noise the baseline shows between two of its\n  own runs),\n- the same run with `-DLSS quality` behaves exactly like OFF on this card.\n\nThen the Shipping package: zip it, record the zip size against the baseline zip and the 1 GB limit, start it on c4,\nplay to the first room, quit. If the zip is over 1 GB, stop and report.\n\n### 8. [pc-b] proof: RTX (1.5 h)\n\nFollow FARM.md \"Five-minute start\" with the name `dlss2`. Then three runs, each into its own log folder:\n\n```bash\nF=\"[notes]/unreal/megajam-2026/farm/farm.sh\"\nfor m in off dlaa quality; do\n  \"$F\" run [pc-b] dlss2 \"/d/UE/wt/dlss2_farmlogs/$m\" -Packaged -Exe '{B}\\Supercut59\\Windows\\Supercut.exe' \\\n      -Run main8 -Seed 1 -Script '{P}\\Script\\main8.txt' -FixedFps 240 -Silent -DLSS $m\ndone\n```\n\nPass:\n\n- `DLSS support: Supported` (or the plugin's word for it) in all three; the driver version in your HANDOFF,\n- `DLSS mode: DLAA ...` and `DLSS mode: QUALITY ...`, and `DLSS upscaler: <a DLSS name>` in those two runs; `none` in\n  the OFF run,\n- `RUN wrapped` identical in all three and equal to the c4 line,\n- shots: one live and one frozen (sketch) shot per mode, same index, side by side into your lane folder; no watermark\n  in any corner,\n- frame times: copy the `FPS` lines, labelled \"offscreen, not a player's frame rate\" (FARM.md).\n\nIf DLSS reports unsupported on [pc-b], record the reason and the driver. Do not update the driver; report.\n\n### 9. Sketch check\n\n1. Two frozen shots 0.3 s apart, camera still, at OFF, DLAA and QUALITY (a script step or two shots in one freeze).\n   Pixel diff as `lanes/slice/HANDOFF.md` \"Risks settled\" did. Pass: DLAA and QUALITY within 0.5 points of OFF\n   (OFF was 1.32% of pixels changed by more than 8 levels).\n2. One frozen shot per mode at 1920x1080 (`-ResX 1920 -ResY 1080`) to the owner as a 4-up picture,\n   `[taste: owner review]`.\n3. Only if QUALITY's outlines fail the owner's eye: make `FSupercutStillFrame` run the frame at 100% screen percentage\n   while `bStill`. Not before the owner sees the pictures.\n\n### 10. Hand back\n\n`HANDOFF.md` in your lane folder: what changed (files), every plugin source edit, the plugin API names with file and\nline, all pass lines from steps 7 and 8 copied from the logs, zip sizes, screenshot paths, open questions, and how to\nremove DLSS in one revert (list the commits). Suggested text for the NVIDIA form question (\"check the NVIDIA features\nyou used and describe how you used them\"): two sentences, true to what the logs show.\n\n## Gotchas\n\n- `.gitignore` drops `Binaries/` at any depth: the NVIDIA DLLs vanish from git unless you add negations (step 2.4).\n- Applying scalability resets `r.ScreenPercentage`: apply the DLSS mode after it (step 4.2).\n- The farm mirror sends `Plugins\\...\\Binaries\\ThirdParty` (it skips only top-level `Binaries`), but also any plugin\n  `Intermediate` you leave: delete those before mirroring.\n- Farm runs are offscreen; Frame Generation and Reflex need a real swap chain and cannot be tested there. They are out\n  of scope.\n- Never run a Shipping package on a farm PC (FARM.md).\n- [pc-b] compiles with MSVC 14.50, c4 with 14.44. The judge zip is built on c4.\n- Two lanes' packages: check `status` shows no `Supercut` process before `run`.\n"
}
````

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\dlss1\BUILD_BRIEF.md (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:30:16 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\PLAN.md",
 "old_string": "3. Delete each copied plugin's prebuilt `Binaries\\Win64` (editor DLLs for 5.8) and `Intermediate`. Keep\n   `Binaries\\ThirdParty` (the NVIDIA runtime DLLs).",
 "new_string": "3. Delete each copied plugin's prebuilt `Binaries\\Win64` (editor DLLs for 5.8) and `Intermediate`. Keep\n   `Binaries\\ThirdParty` (the NVIDIA runtime DLLs).\n   **Git trap (disk):** the game's `.gitignore` has unanchored `Binaries/` and `Build/` lines, so git would drop\n   `Plugins\\<name>\\Binaries\\ThirdParty\\*.dll` without a word, and a package built from a clean checkout would have no\n   DLSS DLLs. Add negations for `Plugins/*/Binaries/ThirdParty/` and check with `git check-ignore -v`."
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\dlss1\PLAN.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:30:18 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\PLAN.md",
 "old_string": "5. A missed attribution line (licence) or a logo used without approval.",
 "new_string": "5. A missed attribution line (licence) or a logo used without approval.\n6. The DLLs silently left out of git by `.gitignore`'s `Binaries/` line, so the c4 judge build has no DLSS while the\n   lane's own folder had it."
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\dlss1\PLAN.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:30:20 · Tool call: Edit**

```
{
 "replace_all": false,
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\PLAN.md",
 "old_string": "6. Compile time: every build and package compiles the plugin's modules.",
 "new_string": "7. Compile time: every build and package compiles the plugin's modules."
}
```

Result:

```
The file [notes]\unreal\megajam-2026\lanes\dlss1\PLAN.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:30:27 · Tool call: Bash** (Get time and check for em dashes)

```
date "+%H:%M"; grep -c "—" "[notes]/unreal/megajam-2026/lanes/dlss1/PLAN.md" "[notes]/unreal/megajam-2026/lanes/dlss1/BUILD_BRIEF.md"
```

Result:

```
19:30
[notes]/unreal/megajam-2026/lanes/dlss1/PLAN.md:0
[notes]/unreal/megajam-2026/lanes/dlss1/BUILD_BRIEF.md:0
```

### Sat 14 Nov 19:30:38 · Agent (claude-opus-5-5)

Plan and build brief are written. Now writing the log and handoff, then I'm done.

**Sat 14 Nov 19:30:49 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\LOG.md",
 "content": "# dlss1 log\n\nClock times from `date` on c4, 14 Nov 2026. (The clock read 19:18 at the start and 19:30 at the end; the work took\nlonger than that gap suggests, so treat the times as the shell's clock, not elapsed time.)\n\n- 19:18 Start. Read FARM.md, project `Supercut.uproject`, `Config/DefaultEngine.ini` (DX12, SM6, Lumen GI and\n  reflections, VSM, distance fields, motion blur off, `r.CustomDepth=3`, no AA line so TSR is the default).\n- Engine search under `D:\\UE\\UE_5.9\\Engine` for DLSS, NGX, Streamline, NVIDIA, Reflex, NVAPI: no DLSS/NGX/Streamline.\n  Found Epic's `Plugins/Runtime/Nvidia/Reflex` (1.6, off by default, NVAPI sleep mode), GeForceNOWWrapper, NVAPI v615.\n- Read the sketch path: `M_SketchFreeze` at `BL_SCENE_COLOR_AFTER_TONEMAPPING` (`Tools/make_assets.py:201`), blendable\n  on the camera (`SupercutCharacter.cpp`), `FSupercutStillFrame` turns jitter off while frozen (GOTCHAS 13 Nov, slice\n  HANDOFF). `run_demo.ps1` has no pass-through for extra game arguments.\n- Web: itch.io jam page (award row, award terms, form field, excluded destinations; Singapore not excluded). Official\n  rules PDF text has no NVIDIA section.\n- Web: NVIDIA DLSS page: plugin 8.9.0 for UE 5.8/5.7/5.6/5.5, SL 2.14.16 / NGX 310.9.16, licence PDF linked on each\n  button, links under `/secure/`. Did not open any download link.\n- Web: NVIDIA plugin archive (nothing for 5.9), 5.7-to-5.8 community patch thread (SR worked, FG crashed), mode-control\n  thread, DLSS 5 thread (not public), DLSS 4.5 blog (\"Built on Streamline\"), DLSS 3 era FG quick start PDF (cvars,\n  watermark rules), Epic's 5.9 MegaJam Preview post.\n- Disk: diffed upscaler-related headers `D:\\UE\\UE_5.8` (5.8.4) against `D:\\UE\\UE_5.9`. `TemporalUpscaler.h`,\n  `ID3D12DynamicRHI.h`, `LegacyScreenPercentageDriver.h`, `TemporalAA.h`, `SceneTextureParameters.h` identical;\n  small additive changes elsewhere; `D3D12Shader.h` renamed; `bIsMultiViewportEnabled` removed.\n- Web: NVIDIA RTX SDKs licence (23 Feb 2024) and supplement: redistribution in object code OK, attribution on splash\n  and credits required, marks need approval two weeks ahead, notify before commercial release, DLSS for NVIDIA GPUs.\n- Disk: `BaseScalability.ini` ResolutionQuality maps to `r.ScreenPercentage`; desktop default mode\n  BasedOnDisplayResolution (`LegacyScreenPercentageDriver.cpp`).\n- Disk: farm `mirror.py` skips only top-level `Binaries` etc., so plugin ThirdParty DLLs travel. Game `.gitignore` has\n  unanchored `Binaries/` and `Build/`: plugin DLLs would be dropped from git. Added to plan and brief.\n- 19:30 Wrote PLAN.md, BUILD_BRIEF.md, this log, HANDOFF.md.\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\dlss1\LOG.md (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:30:59 · Tool call: Write**

```
{
 "file_path": "[notes]\\unreal\\megajam-2026\\lanes\\dlss1\\HANDOFF.md",
 "content": "# dlss1 handoff\n\nResearch lane, 14 Nov 2026. Nothing in the game, engine or farm was changed, built or run. No downloads, sign-ins or\nlicences.\n\n## Files\n\n- `PLAN.md`: the answer, by the eight questions of the brief, with a tag on every claim (disk, web, not verified) and\n  a Sources list.\n- `BUILD_BRIEF.md`: a self-contained brief for build lane `dlss2`, to start once the zip is in `D:\\UE\\dl\\dlss\\`.\n- `LOG.md`: what was read, in order.\n\n## Result in five lines\n\n1. Super Resolution or DLAA through the DLSS 4.5 Unreal plugin qualifies, by the itch.io award wording.\n2. No plugin for 5.9 exists. The newest is v8.9.0 for UE 5.8. The engine's upscaler interface is unchanged 5.8.4 to\n   5.9 on disk, so a port has a fair chance. Unproven.\n3. The owner downloads `2026.10.16_ue5.8_dlss4.5plugin_v8.9.0.zip` from https://developer.nvidia.com/rtx/dlss into\n   `D:\\UE\\dl\\dlss\\`.\n4. Smallest version: 6 to 9 agent hours. Frame Generation and Reflex: skip.\n5. Recommendation: do the smallest version, stop at Sunday 11:00 SGT if it does not build and pass the c4 AMD check.\n\n## How to re-check\n\n- Engine contents: `find /d/UE/UE_5.9/Engine/Plugins -iname \"*dlss*\" -o -iname \"*streamline*\" -o -iname \"*ngx*\"`\n  (empty on 14 Nov).\n- Header diff: `diff /d/UE/UE_5.8/Engine/Source/Runtime/Renderer/Public/TemporalUpscaler.h\n  /d/UE/UE_5.9/Engine/Source/Runtime/Renderer/Public/TemporalUpscaler.h` (empty on 14 Nov).\n- Git trap: `git -C <worktree> check-ignore -v Plugins/X/Binaries/ThirdParty/Win64/a.dll` prints the `Binaries/` line.\n\n## Not done / open\n\n- Everything marked \"not verified\" in PLAN.md needs the zip.\n- The NVIDIA form's checkbox list is not public.\n- [pc-b]'s driver version not read (no remote commands this round).\n- Attribution: plain text \"NVIDIA DLSS\", no logo, is my pick `[owner decision]`.\n\n## Gotchas\n\n- The brief's \"package about 250 MB\" is out of date: the Development folder was 1.08 GB uncompressed on 14 Nov\n  (GAME.md). Watch the Shipping zip against 1 GB.\n- `.gitignore`'s unanchored `Binaries/` hides plugin DLLs from git.\n- Applying scalability resets `r.ScreenPercentage`; apply the DLSS mode after it.\n- Farm runs are offscreen: fine for Super Resolution, useless for Frame Generation, and their frame rates are not a\n  player's.\n"
}
```

Result:

```
File created successfully at: [notes]\unreal\megajam-2026\lanes\dlss1\HANDOFF.md (file state is current in your context — no need to Read it back)
```

**Sat 14 Nov 19:31:04 · Tool call: Bash** (Confirm gitignore drops plugin DLL paths, read only)

```
git -C /d/UE/Projects/Supercut59 check-ignore -v --no-index Plugins/DLSS/Binaries/ThirdParty/Win64/nvngx_dlss.dll; ls "[notes]/unreal/megajam-2026/lanes/dlss1"
```

Result:

```
.gitignore:2:Binaries/	Plugins/DLSS/Binaries/ThirdParty/Win64/nvngx_dlss.dll
BUILD_BRIEF.md
HANDOFF.md
LOG.md
PLAN.md
```

### Sat 14 Nov 19:31:25 · Agent (claude-opus-5-5)

The plan and the build brief are written. I changed nothing in the game, the engine or any farm PC.

**Can we qualify?** Yes, with DLSS Super Resolution or DLAA alone. The jam's award terms on itch.io say the entry must use "at least one of the following NVIDIA features: ... NVIDIA DLSS". Frame Generation is not needed. Two catches:
- The GPU goes to the best-ranked Render Royalty entry that also uses an NVIDIA feature. DLSS gets us in, but the visuals score decides who wins.
- Singapore is not on the award's list of excluded countries.

**Is there a plugin for 5.9?** No.
- Our engine folder has no DLSS, NGX or Streamline plugin. I checked on disk.
- It does ship Epic's own NVIDIA Reflex plugin, but Reflex is not on the award's list.
- The newest DLSS plugin is v8.9.0, built for UE 5.8.
- Good sign: I compared our 5.8.4 and 5.9 engine folders. The file that defines how an outside upscaler plugs into the engine is identical in both, and the DirectX 12 interface the plugin uses is unchanged. So the 5.8 plugin has a fair chance to build on 5.9 with small fixes. That stays unproven until a build runs.

**What the owner must do by hand:**
1. Open https://developer.nvidia.com/rtx/dlss and click "Download UE 5.8 DLSS Plugin". Expect to accept the NVIDIA RTX SDK licence (https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf). Expect a free NVIDIA developer sign-in too, since the link sits under a `/secure/` path. I did not open the link.
2. Save `2026.10.16_ue5.8_dlss4.5plugin_v8.9.0.zip` to `D:\UE\dl\dlss\`. Don't unzip it.
3. Have a person on [pc-b] read the NVIDIA driver version. Don't update the driver without deciding first.
4. Decide on the credit. The licence requires naming DLSS on splash screens and in credits. But using NVIDIA's logos needs their written approval two weeks ahead. My pick: a plain-text "NVIDIA DLSS" line, no logo.

**Hours:** about 6 to 9 agent hours for the smallest version (OFF, DLAA, QUALITY, BALANCED, PERFORMANCE). Frame Generation would add 4 to 8 hours. It can't be proven on the farm, because farm runs have no game window. And when someone ported the plugin to 5.8 before NVIDIA did, Frame Generation crashed. Reflex adds nothing to eligibility.

**Three biggest risks:**
1. The plugin won't compile on 5.9, or compiles and crashes at start.
2. It changes the game on PCs without an NVIDIA card. The c4 AMD run must print the same `RUN wrapped` line and match the old screenshots.
3. The zip goes over 1 GB. The Development package folder was already 1.08 GB uncompressed today, so the "about 250 MB" figure is out of date.

One more trap I confirmed: the game's `.gitignore` line `Binaries/` drops the plugin's NVIDIA DLLs from git without any warning. A judge build from a clean checkout would then have no DLSS. The brief has the fix.

**The sketch look:** DLSS takes TSR's place, and the sketch still runs after it at full output resolution. The existing jitter fix during the freeze should carry over. Outlines get coarser below 100% because depth and normals stay at the lower render resolution, so DLAA is the cleanest choice. The brief includes a still-frame pixel check and a 4-up screenshot for you to judge.

**Recommendation:** do the smallest version only. Start as soon as the zip is on disk. Stop and revert if it doesn't build and pass the AMD check by Sunday 11:00 SGT. Skip Frame Generation and Reflex.

**Not verified (all need the zip):**
- the plugin's folder names, dependencies, version field, function names and console variables for v8.9.0
- whether an NVIDIA sign-in or application ID is needed
- the minimum driver
- the DLL sizes
- whether the DLLs show a watermark
- how Streamline behaves on AMD
- the checkbox list on the NVIDIA form question

Files:
- [PLAN.md](<[notes]/unreal/megajam-2026/lanes/dlss1/PLAN.md>)
- [BUILD_BRIEF.md](<[notes]/unreal/megajam-2026/lanes/dlss1/BUILD_BRIEF.md>)
- [HANDOFF.md](<[notes]/unreal/megajam-2026/lanes/dlss1/HANDOFF.md>)
- [LOG.md](<[notes]/unreal/megajam-2026/lanes/dlss1/LOG.md>)

Sources: [itch.io jam page](https://itch.io/jam/2026-epic-ai-megajam), [NVIDIA DLSS page](https://developer.nvidia.com/rtx/dlss), [NVIDIA Unreal page](https://developer.nvidia.com/game-engines/unreal-engine), [plugin archive](https://forums.developer.nvidia.com/t/nvidia-dlss-unreal-engine-plugin-archive/377564), [5.8 port thread](https://forums.developer.nvidia.com/t/any-hero-who-can-compile-it-for-5-8/370193), [DLSS mode thread](https://forums.developer.nvidia.com/t/turning-off-dlss-by-default-in-unreal-engine-5-3-and-getting-current-dlss-mode/292520), [DLSS 4.5 blog](https://developer.nvidia.com/blog/whats-new-for-game-developers-in-nvidia-rtx-dlss-4-5-for-ue5-and-multilingual-ai-characters/), [Frame Generation guide](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/DLSS_Frame_Generation_Quick_Start_Guide.pdf), [RTX SDK licence](https://developer.download.nvidia.com/licenses/nvidia-rtx-sdk-license-2024.02.23.pdf), [UE 5.9 MegaJam Preview post](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840).
