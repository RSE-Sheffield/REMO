---
title: 'REMO: Deterministic Scenario Record and Replay with Modification for ADS Debugging in CARLA'
tags:
  - Python
  - autonomous vehicles
  - simulation-based testing
authors:
  - name: Matthew I Leach
    orcid: 0000-0002-8901-5609
    affiliation: 1
  - name: Sanjeetha Pennada
    orcid: 0000-0003-4650-862X
    affiliation: 1
  - name: Donghwan Shin
    orcid: 0000-0002-0840-6449
    corresponding: true
    affiliation: 1
affiliations:
 - name: School of Computer Science, University of Sheffield, United Kingdom
   index: 1
date: 00 December 2025
bibliography: paper.bib
---


## Summary
In simulation-based testing of autonomous driving systems (ADS), the ability to reproducibly recreate and modify driving scenarios is crucial for testing and debugging system performance. 
For example, when an ADS fails to navigate a complex urban driving scenario, researchers and engineers need to isolate the contributing factors by systematically modifying scenario elements, such as weather conditions, time of day, street lights, traffic signs, or the presence of other vehicles and pedestrians. 
However, existing simulation platforms like CARLA [@CARLA2017] often lack the capability to deterministically replay scenarios with modified parameters while maintaining consistent non-player character (NPC) behaviour. 

To address this limitation, we present `REMO`, a tool that enables deterministic replay and modification of simulation scenarios within CARLA. 
`REMO` provides the following key features:

- **Deterministic Scenario Replay**: `REMO` allows users to record and replay any driving scenarios in CARLA while ensuring that all static and dynamic elements, including NPC behaviours, remain consistent across replays, unless intentionally modified.
- **Scenario Modification**: Users can modify various scenario elements/parameters, including environmental conditions (e.g. weather, time of day) and the presence of specific actors (e.g. vehicles, pedestrians), without disrupting the deterministic nature of the replay.
- **ADS-Agnostic Testing**: `REMO` supports scenario replay with or without an ego vehicle (i.e. the autonomous vehicle under test), enabling researchers to test different ADS models under identical NPC conditions for fair comparisons.
By enabling deterministic replay and flexible scenario modification, `REMO` facilitates systematic debugging and evaluation of autonomous driving systems.


## Statement of Need
Debugging failures in machine learning–enabled autonomous driving systems (ADS) is a complex task that requires the ability to reproducibly recreate and modify driving scenarios [@10726945].
For example, @9787893 proposed iterative removal of NPC vehicles to isolate the minimal set of NPCs responsible for triggering a failure, showing that simplified scenarios significantly aid engineers during debugging. 
However, they focused on NPC removal and did not address the broader need for deterministic scenario replay and modification of other scenario elements (e.g. weather, time of day, buildings).
Furthermore, due to the inherent non-determinism of simulation platforms [@11052713; @9793395], simply re-running a scenario without explicitly recording and replaying it can lead to different outcomes, making it difficult to isolate failure causes.
Although CARLA supports record and replay functionality, it lacks the ability to modify scenarios while maintaining deterministic NPC behaviour.

`REMO` is designed to fill this gap by providing a tool that enables deterministic replay of recorded scenarios with the ability to modify various scenario parameters without affecting NPC behaviour.
It allows users to systematically explore how different factors contribute to ADS failures by enabling controlled modifications of the simulation environment.
It also supports ADS-agnostic testing by allowing scenario replay without an ego vehicle, facilitating fair comparisons between different ADS models under identical conditions.

## Research Impact 
REMO addresses a fundamental limitation in ADS: the lack of deterministic scenario replay and controlled scenario modification in CARLA-based testing workflows. It fills a critical gap between high-fidelity simulation and reproducible ADS evaluation by enabling the recording, deterministic replay, and modification of critical driving scenarios.

The deterministic scenario replay, including NPC trajectories, with controlled changes to environmental and structural entities in REMO, improves the reliability and fairness of ADS benchmarking and debugging of failure scenarios. This capability enables researchers and developers to isolate the root causes of ADS failures, compare multiple ADS under identical conditions, and examine the effects of environmental variation on scenario simplification.

## Overview of the Tool
\autoref{fig:architecture} illustrates the workflow of the tool in three main phases: scenario setup, scenario recording, and replay with modification.

- **Setup**: In the setup phase, users define a scenario using the configuration files, such as XML or JSON, optionally assisted by a graphical user interface. This scenario definition specifies the simulation environment, scenario entities, and the system under test. The REMO API uses this configuration to initialize the CARLA server by loading the simulation world, spawning the ego vehicle and other entities, configuring the ADS, and applying the specified environmental conditions. 

- **Scenario Recording**: During the scenario recording phase, the REMO API controls the execution of the simulation and collects relevant state information from the CARLA server at each simulation step. The runtime information for all the entities is captured and stored along with static metadata describing the scenario configuration and the ADS under test. These recordings provide a complete description of the executed scenario, which can be reused for deterministic replay with or without modifications. 

- **Replay with Modification**: In the replay with modification phase, previously recorded scenarios can be loaded using stored metadata and replayed deterministically with user-defined modifications. These modifications may include, but are not limited to, changing weather or time conditions, removing NPCs, toggling structural entities, modifying the system under test, or altering the position of NPCs. 
  
Together, these phases provide a reproducible workflow for executing, recording, and replaying autonomous driving scenarios with modifications in CARLA environment, enabling systematic evaluation of ADS performance under different conditions.

![Overall Architecture of `REMO`\label{fig:architecture}](remo-overview.png)

## Repository and Installation

The tool requires Python 3.8 and CARLA version 0.9.15. 
The source code of `REMO`, including detailed installation instructions and example scripts, is hosted on GitHub: [https://github.com/RSE-Sheffield/REMO](https://github.com/RSE-Sheffield/REMO).

## AI Usage Disclosure
No generative artificial intelligence tools were used in the creation of the software, documentation, or the writing of this paper.


## Acknowledgements
This work was supported by the Institute of Information & Communications Technology Planning & Evaluation(IITP) grant funded by the Korea government(MSIT) (No. RS-2025-02218761, 50%) and by the Engineering and Physical Sciences Research Council (EPSRC) [EP/Y014219/1].


## References





















