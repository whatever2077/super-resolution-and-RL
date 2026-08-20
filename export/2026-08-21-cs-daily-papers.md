# 2026-08-21 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Enhancing EBSD throughput of battery electrode materials using super-resolution generative adversarial networks
- **论文链接**: http://arxiv.org/abs/2608.19117v1
- **作者**: John Mangum, Andrew Glaws, Francois Usseglio-Viretta, Steven Spurgeon, Donal Finegan
- **原始摘要**: Quantitative microstructural characterization of Li-ion battery electrode materials using electron backscatter diffraction (EBSD) has been proven as a critical method for optimizing cell performance. However, the inherently slow nature of EBSD can hinder the throughput of analyses needed for statistical representation of a material microstructure being developed. This work demonstrates a machine learning super-resolution framework using a generative adversarial network (SRGAN) to significantly increase EBSD throughput. The SRGAN model was trained on EBSD data of LiNixMnyCozO2 (NMC) cathode particles to computationally enhance low-resolution datasets and its performance is compared against classical interpolation methods across various upscaling factors (2x to 12x). Both qualitative image metrics and quantitative microstructural analysis verified that the SRGAN systematically outperformed classical methods, particularly in preserving small grains and maintaining realistic grain boundaries. We demonstrate that a 5x upscaling factor, corresponding to a 25x speed-up in acquisition time or a 25x larger field of view, is practical while maintaining acceptable accuracy in key metrics like grain size and shape. For instance, at 5x upscaling, relative errors were +5.7%, +8.2%, and -14.6% on grain area-equivalent diameter, grain maximum sphere-inscribed diameter, and grain boundary length, respectively. The SRGAN methodology developed in this work significantly enhances the efficiency of EBSD acquisition for more statistically robust microstructural dataset, enabling EBSD as a high-throughput characterization tool for materials research and industrial process development.

### GPT总结
#### 文章内容
- 论文针对EBSD采集速度慢、难以获得统计代表性微观结构数据的问题，提出用SRGAN对低分辨率EBSD进行超分辨重建以提升通量。
- 核心思路是基于LiNixMnyCozO2 (NMC) 正极颗粒的EBSD数据训练SRGAN，在2x–12x放大倍率下与经典插值法对比，并结合图像质量指标与微观结构量化指标进行评估。
- 主要结论是SRGAN系统性优于经典方法，尤以小晶粒保真和真实晶界保持显著；5x放大可带来约25x采集时间或视场提升，且关键统计量误差可接受（+5.7%、+8.2%、-14.6%），有助于将EBSD用于高通量表征。

#### 方法
- 数据与任务：以NMC正极颗粒的EBSD为训练数据，学习从低分辨率到高分辨率的映射，计算式增强低分辨率数据集。
- 放大倍率：在2x–12x多种尺度下进行训练/测试与系统评估。
- 基线对比：与多种经典插值方法进行横向比较。
- 评估维度：结合定性图像质量指标与定量微观结构分析（如晶粒尺寸、形状与晶界长度）综合评估。
- 网络结构与损失细节：文中未明确说明。

#### 创新点
- 将SRGAN引入EBSD超分辨重建场景，以数据驱动方式显著提升EBSD通量，相比传统插值更好地保留微观结构细节。
- 覆盖2x–12x的广泛尺度系统评估，并以微观结构统计量为核心判据，强调对小晶粒和真实晶界形貌的保持。
- 明确给出实用工作点：5x放大对应约25x采集时间/视场收益，并量化关键统计量误差，为高通量EBSD提供可操作指南。

#### 实验结论
- 任务与数据：在NMC正极颗粒EBSD上进行超分辨重建；与经典插值方法对比，使用图像与微观结构双重指标评估。
- 核心结果：SRGAN在各倍率下整体优于经典插值，尤其在小晶粒与晶界保持方面更佳。
- 关键数字：5x放大时带来约25x通量或视场提升；相对误差为+5.7%（grain area-equivalent diameter）、+8.2%（grain maximum sphere-inscribed diameter）、-14.6%（grain boundary length）；作者认为该水平具有实用性。

## 关键词：reinforcement learning

## ADEPT: Accelerating Dexterity via Pre-Training and Post-Training using Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2608.19182v1
- **作者**: Jayjun Lee, Jessica Yin, Asif Rana, Nicholas Blauch, Sam Mady, Mohak Bhardwaj, Nima Fazeli, Nathan Ratliff, Karl Van Wyk, Ankur Handa
- **原始摘要**: We introduce Accelerating Dexterity via Pre-Training (ADEPT), a large-scale reinforcement learning (RL) framework for learning sim-to-real transferable dexterity across high degree-of-freedom (DoF) robot embodiments that can solve long-horizon tasks directly from raw visuo-tactile perception. ADEPT pretrains a dexterous policy on a generic object reposing task, then post-trains downstream policies with this pretrained behavior as a prior. ADEPT enables learning new behaviors that are otherwise difficult to discover from scratch on multi-fingered robots and avoids learning the same set of skills over again for every new downstream task. The pretrained policy zero-shots the reposing phase of downstream tasks, but naïve RL fine-tuning rapidly degrades this capability during transfer. We address this with a stable post-training recipe combining behavior-cloning distillation, critic warm-up, and conservative on-policy updates. To safely exploit the full kinematic dexterity, we introduce a joint-space Geometric Fabric that mediates between the RL policy and the robot. We distill post-trained teachers into perceptive students that zero-shot sim-to-real transfer on two embodiments: a 23 DoF Kuka-Allegro with two RGB cameras, and a 29 DoF Flexiv-Sharpa with two RGB cameras and five vision-based tactile sensors, and can solve long-horizon tasks from challenging initial states with dexterity at human-level speed.

### GPT总结
#### 文章内容
ADEPT旨在解决高DoF臂手系统在稀疏奖励、接触丰富、长时序任务中的可学习性与跨任务/跨形态迁移困难，提出通过通用“reposing”预训练获取通用灵巧基座，再经稳定后训练迁移到下游插装等任务。核心思路是：用大规模RL在仿真中预训练可零样本完成“repose”段落的策略；在迁移时结合行为克隆蒸馏、critic预热与保守的on-policy更新，配合关节空间Geometric Fabric确保安全且充分利用全关节灵巧性；再将教师蒸馏为端到端“感知学生”实现sim-to-real零样本部署。主要结论是：在Kuka-Allegro和Flexiv-Sharpa两种高DoF平台上，ADEPT从纯视觉或视触觉输入零样本完成FMB插装与餐盘上架，仿真达85.0%/89.2%成功率，现实零样本达5/10、3/10、6/10与8/10，并较FMB基线流程获得2×–14×执行速度提升。

#### 方法
- 预训练阶段：在仿真中以通用object reposing任务大规模训练灵巧策略，使其学到reach–grasp–reorient–transport等基础运动原语并可零样本复用至下游任务的“repose”段。
- 后训练阶段：为避免直接微调导致预训练行为退化，采用结构化迁移流程——行为克隆蒸馏以保持先验行为、critic warm-up以缓解价值失配、以及保守的on-policy（基于PPO）更新以限制早期策略漂移。
- 控制接口：提出全关节配置空间（Cspace）的Geometric Fabric，在策略与机器人之间进行调节，既开放全运动学自由度以发挥灵巧性，又在仿真与实机一致地防止碰撞与越限。
- 感知蒸馏：将后训练的“教师”（状态输入）通过两阶段蒸馏课程转为端到端“学生”（纯视觉或视触觉输入），共享Geometric Fabric动作接口以实现仿真到实机的一致性。
- 部署：学生策略以两路RGB（Kuka-Allegro）或RGB+TacMap触觉（Flexiv-Sharpa）作为输入，零样本在真实平台执行长时序插装与上架任务。

#### 创新点
- 提出“预训练通用reposing + 后训练任务特化”的RL范式，避免每个下游任务从零学习基础灵巧技能，显著加速多指灵巧策略的获取与迁移。
- 引入全关节Cspace Geometric Fabric，将安全约束与全自由度灵巧控制统一，区别于以往将手部限制在低维PCA抓取子空间的做法。
- 设计稳定的后训练配方（行为克隆蒸馏、critic预热、保守PPO更新）系统性缓解观测空间不匹配、价值估计错位与策略早期漂移，保持预训练能力不被破坏。
- 提出两阶段感知蒸馏课程，将状态教师蒸馏为端到端视觉/视触觉学生，实现跨两种高DoF形态的sim-to-real零样本长时序插装与上架，无需示教或位姿追踪。

#### 实验结论
- 任务与平台：在23 DoF Kuka-Allegro（双RGB）与29 DoF Flexiv-Sharpa（双RGB+五指端触觉）上评测FMB star与square/round插装，以及餐盘翻转-再抓-上架；随机初始位姿覆盖30 cm × 25 cm平面与[−π, π] yaw。
- 结果：仿真后训练教师在Kuka-Allegro（两种peg汇总）达85.0%，在Flexiv-Sharpa（square/round）达89.2%；Kuka-Allegro视觉学生在仿真为46.7%/65.2%（square/round, star），现实零样本为5/10（star）、3/10（square/round）、6/10（dish）；Flexiv-Sharpa视触觉学生现实零样本为8/10（square/round）。评估采用1024回合与ADR 50（仿真）。
- 结论：与FMB并行爪流水线相比，单策略端到端的多指方案在无需外部治具、无需多阶段重抓的前提下实现2×–14×执行提速（5–10 s/次 vs 20–70 s/次），展示了ADEPT在长时序、接触丰富灵巧操作上的有效性与可迁移性。
