# REMO: A Tool for Replaying with Modifications for Scenario-Based Testing in Autonomous Driving Systems


**Matthew I Leach** [![ORCID iD](https://img.shields.io/badge/-green?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-8901-5609) $^1$^¶$ ,
**Sanjeetha Pennada** [![ORCID iD](https://img.shields.io/badge/-green?logo=orcid&logoColor=white)](https://orcid.org/0000-0003-4650-862X) $^1$, **and**
**Donghwan Shin** [![ORCID iD](https://img.shields.io/badge/-green?logo=orcid&logoColor=white)](https://orcid.org/0000-0002-0840-6449) $^1$  


**1** School of Computer Science, University of Sheffield, Sheffield **¶** Corresponding author  


## Summary
Reproducing autonomous driving scenarios with deterministic behaviour is a significant challenge in the field of autonomous vehicle (AV) research. While current simulation platforms like CARLA offer high-fidelity environments, they often fall short in providing user-friendly interfaces for recording, modifying, and deterministically replaying scenarios which is essential for testing different Autonomous Driving Systems (ADS) under uniform conditions. The manual adjustment of factors such as weather and time conditions, street lights, buildings and the behaviour of non-player characters (NPCs) frequently results in inconsistencies that hinder reproducibility and fair benchmarking. 

The tool REMO (Replay with Modifications) is designed to allow the deterministic replay of simulation scenarios and modification of various scenario entities such as weather conditions, number of NPCs, street lights, and time of day, as well as structural components like buildings. REMO tests the behaviour of ego vehicle driven by ADS while maintaining deterministic NPC behaviour. This functionality provides a reliable, adaptable, and ADS-agnostic testing framework for evaluating autonomous driving systems.  

## Statement of Need
Recent work has recognised the importance of scenario simplification for understanding failures in machine learning–enabled autonomous systems. Arcaini et al. (2022) proposed iterative removal of traffic participants to isolate the minimal set of elements responsible for triggering a failure, showing that simplified scenarios significantly aid engineers during debugging. Similarly, Shin and Pennada (2024) highlight the need for automated failure scenario simplification and outline challenges such as combinatorial explosion, non-linear ML behaviour, and the high cost of repeated simulations, motivating surrogate-assisted and search-based strategies to reduce scenario complexity while preserving the triggering failure. While these studies demonstrate that simplification enhances explainability and debugging, they primarily operate on already executed scenarios and do not provide deterministic replay, or modification of entities inside the simulator. Moreover, despite growing interest in scenario generation and scenario minimisation, very little research addresses the broader problem of ADS debugging itself, particularly the need to reliably reconstruct, modify, and compare failure-inducing scenarios across different ADSs.

ADS are developed and evaluated in simulation environments such as CARLA, LGSVL (Kaur et al., 2021), where diverse traffic scenarios, environmental settings, and weather conditions can be recreated safely. Therefore, a persistent challenge in this field is reproducibility i.e., the ability to run identical scenarios with deterministic non-player character (NPC) behaviours, traffic dynamics, and environmental conditions. When testing different ADS models on the same scenario, even minor variations in NPC behaviour or timing can lead to different outcomes, making it difficult to perform fair comparisons or conduct systematic debugging of autonomous driving failures.

CARLA allows both manual control and Traffic Manager control. However, the current versions of CARLA only allows specifying start and destination points for vehicles managed by the Traffic Manager, and does not provide the ability to replay or modify scenarios (Ai et al., 2025). They lack an interactive graphical interface for editing recorded scenarios, and modifications (such as weather, time of day, or removal of specific entities) often disrupt deterministic replay. Moreover, the inability to replay scenarios without the ego vehicle prevents researchers from isolating NPC behaviour and testing multiple ADS controllers under identical external conditions. This gap limits the ability of researchers to perform ADS-agnostic testing and to study how different systems respond to the same real-world failures.

REMO addresses these limitations by introducing a deterministic scenario replay tool that enables users to record, replay, and modify complex simulation scenarios directly within CARLA. Unlike traditional record–replay methods, REMO ensures deterministic NPC behaviour while allowing selective modification of scenario parameters such as weather, lighting, buildings, and time of the day. It also supports scenario replay, enabling independent testing of ego vehicle driven by different ADSs (e.g., TransFuser++) in identical conditions.

This combination of determinism, and configurability makes REMO a unique and valuable tool for the autonomous driving research community. REMO bridges the gap between realistic scenario generation and reproducible experimentation, establishing a robust foundation for debugging and validating machine learning–enabled driving systems. Its capabilities extend beyond scenario simplification research, addressing broader needs in ADS debugging, such as isolating faulty perception inputs, exploring alternative ADS responses, and testing multiple ADSs within the same scenario.


## State of Field
Despite CARLA’s widespread adoption as an open-source simulation platform for autonomous driving research, it still lacks several essential features needed for reproducible experimentation, systematic debugging, and ADS-agnostic evaluation. CARLA cannot deterministically replay previously executed scenarios, as its Traffic Manager controls NPCs stochastically, causing different outcomes even with identical initialisations. Modifying scenarios, such as removing actors, adjusting weather, or changing the environment, often breaks determinism and causes unpredictable NPC behaviors. Furthermore, CARLA cannot modify or replay complex scenarios, and does not support scenario replay without an ego vehicle, which prevents testing multiple ADS models under identical NPC conditions. 

While simulation-based testing is a standard practice, the lack of deterministic record–replay mechanisms, consistent NPC behavior, and flexible scenario modification tools undermines efforts to isolate failure cases,  validate scenario simplifications, and support ADS-agnostic evaluation. As the field advances in scenario complexity and generation algorithms, there remains a critical gap in tools that enable robust, repeatable scenario editing and replay. This gap directly motivates the development of REMO. REMO directly addresses these limitations by providing deterministic scenario replay and flexible modification of scenario entities, which are absent in standard CARLA. The following are key contributions of REMO:

* Enables users to record, replay, and edit complex simulation scenarios while maintaining deterministic NPC behavior.
* Supports scenario replay with or without an ego vehicle, facilitating direct, ADS-agnostic comparisons under identical conditions.
* Integrates scenario editing into a user-friendly workflow, allowing easy removal or addition of actors and adjustment of environmental entities.



## Repository and Installation






## Acknowledgements


## References
> [1] P. Kaur, S. Taghavi, Z. Tian and W. Shi, "A Survey on Simulators for Testing Self-Driving Cars," 2021 Fourth International Conference on Connected and Autonomous Driving (MetroCAD), Detroit, MI, USA, 2021, pp. 62-70, doi: 10.1109/MetroCAD51599.2021.00018. 

> [2] Ai, Yan, et al. Reproduction of Real-World Scenarios in CARLA: An Extension of CARLA Functionality. No. 2025-01-8059. SAE Technical Paper, 2025.

> [3] Arcaini, Paolo, Xiao-Yi Zhang, and Fuyuki Ishikawa. "Less is more: Simplification of test scenarios for autonomous driving system testing." 2022 IEEE Conference on Software Testing, Verification and Validation (ICST). IEEE Computer Society, 2022.

> [4] Shin, Donghwan, and Sanjeetha Pennada. "Towards simplification of failure scenarios for machine learning-enabled autonomous systems." 2024 IEEE 24th International Conference on Software Quality, Reliability, and Security Companion (QRS-C). IEEE, 2024.



