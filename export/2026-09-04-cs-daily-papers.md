# 2026-09-04 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Genesis: A Generative Engine for Hierarchical Satellite Image Synthesis
- **论文链接**: http://arxiv.org/abs/2609.02683v1
- **作者**: Subash Khanal, Yangzhi Cui, Daniel Cher, Eric Xing, Brian Wei, Srikumar Sastry, Nathan Jacobs
- **原始摘要**: Earth observation is fundamentally multi-scale; geospatial tasks span varied resolutions, and satellite imagery is organized into cascading tile pyramids that nest fine detail within wide coverage. Current generative models of satellite imagery, however, operate along a single axis: they either zoom to enhance a single tile's resolution or pan to extend imagery at a fixed scale. As a result, no existing method produces a complete pyramid that stays consistent across both scale and space, where a high-zoom tile must agree with the coarse context it refines and with the neighbors it meets. Motivated by this gap, we introduce a new task, multi-scale tile completion: given a sparse set of seed tiles at arbitrary zoom levels and positions, synthesize a complete, uniform quadtree that is globally consistent across both scale and space. We approach this task with Genesis, a generative engine that brings both axes together by composing two specialized operators over the quadtree: a vertical super-resolution model and a horizontal mask-based outpainting model, producing pyramids that are consistent across zoom levels and seamless across neighboring tiles. Each operator achieves state-of-the-art results on its subtask, and the engine propagates sparse seeds into seamless, multi-resolution maps from any initial configuration. To evaluate the task and benchmark Genesis, we introduce dense500, a fully observed multi-scale pyramid dataset spanning diverse geographic regions, together with a suite of pyramid-level metrics. Code, models, and our dataset are available at https://github.com/mvrl/genesis.

### GPT总结
#### 文章内容
论文提出多尺度瓦片补全任务，目标是从任意缩放级别与位置的稀疏seed tiles生成一个在尺度与空间上全局一致的完整瓦片金字塔。核心思路是构建Genesis引擎，组合垂直方向的超分辨率算子与水平方向的掩码外延算子，并配合确定性下采样，在四叉树上双轴协同生成。作者引入dense500全观测金字塔基准与金字塔级评测指标，实验显示两个算子在各自子任务达成SOTA，整机可从稀疏种子生成跨尺度一致、邻接无缝的多分辨率地图。代码与数据集已公开。

#### 方法
- 任务建模：定义multi-scale tile completion，从任意缩放与位置的稀疏种子出发，重建完整统一的quadtree，满足父子跨尺度一致与同层相邻无缝约束。
- 垂直算子（超分辨率）：将缩放级别z的N×N tile映射为z+1级四个子瓦片组成的2N×2N马赛克，实现纵向细化。
- 水平算子（掩码外延）：在256×256 tile上，根据任意已知象限子集完成缺失区域，确保邻接边界平滑衔接。
- 辅助操作：使用确定性下采样提供自上而下/自下而上信息传递闭环，使任意种子可传播到任意目标瓦片。
- 引擎组合与推理：在四叉树上调度垂直/水平算子与下采样，按需传播与融合以完成整金字塔；训练细节与损失设计文中未明确说明。

#### 创新点
- 提出新的多尺度瓦片补全任务，首次同时对“垂直跨尺度一致性”和“水平相邻无缝性”提出联合约束。
- 设计Genesis引擎，将垂直超分与水平外延两类专用算子在四叉树上可组合化，统一实现“放大+扩展”的双轴生成。
- 发布dense500全观测金字塔数据集与金字塔级评测协议，支持从 pyramid-level 角度量化多尺度生成一致性。
- 引入boundary-difference (B-diff) 指标评估合成区域与上下文边界融合程度，补充LPIPS/DISTS等感知指标与FID。

#### 实验结论
- 任务与数据：在Git-10M测试划分上分别评估超分辨率与外延模块；在dense500上按三种seed protocols（Single seed、Three independent seeds、Four spatially independent seeds）评测整机金字塔补全。
- 评测设置：SR按子瓦片缩放段z12–15、z16–17、z18分组，报告PSNR、SSIM、LPIPS、DISTS、FID；Outpainting在quad3/quad2_adj/quad2_diag/quad1四种遮罩下报告LPIPS、DISTS（洞区）与FID（整图），并提出B-diff衡量边界拼接质量。
- 主要结论：两个专用算子在各自子任务取得state-of-the-art，Genesis可将稀疏种子传播为跨尺度一致、相邻无缝的多分辨率地图；具体训练细节与数值增益文中未明确说明。

## 关键词：reinforcement learning

## Post-Training Language Models for Gold-Medal Performance in Coding Competitions
- **论文链接**: http://arxiv.org/abs/2609.02849v1
- **作者**: Aleksander Ficek, Sean Narenthiran, Mehrzad Samadi, Somshubra Majumdar, Boris Ginsburg
- **原始摘要**: Competitive programming has become a key test of large language model reasoning, with international competitions such as IOI and ICPC representing its most challenging settings. We present an end-to-end specialization pipeline combining large-scale problem curation, synthetic reasoning traces, supervised fine-tuning (SFT), and reinforcement learning (RL). Using 22,000 curated problems, we train Nemotron-3-Nano-CC (30B-A3B) with SFT and RL and Nemotron-3-Ultra-CC (550B-A55B) with SFT alone. We further introduce GenCorrect, a feedback-driven test-time compute strategy that iteratively generates, evaluates, and refines diverse solutions. On IOI 2025, Nano-CC improves from 130 points to 291 after post-training and to 468 with GenCorrect, exceeding the gold threshold of 438.3 while Ultra-CC reaches 502. Guided by these results, we develop a competition-specific Ultra-CC system and evaluate it prospectively during IOI 2026. Under the same time, internet-access, and submission constraints as human contestants, it scores 535.4 out of 600, exceeding both the gold threshold of 361.12 and the top human score of 498.27. To our knowledge, this is the first AI system to outscore the highest-scoring human contestant on an IOI problem set.

### GPT总结
#### 文章内容
本文针对LLM在竞赛编程（如IOI/ICPC）中的算法综合与受限评测环境下的可靠通过问题，提出一条端到端专精流水线：大规模题目整理与可执行环境构建、合成推理轨迹、长上下文SFT、以及带可执行奖励的RL，并配合测试时闭环推理GenCorrect。核心思路是在训练阶段通过高质量合成推理与执行反馈对齐模型的算法推导与实现能力，在推理阶段用评测反馈迭代生成与纠错以最大化有限提交预算下的得分。主要结论是：在IOI 2025上，小模型Nano-CC经SFT+RL并结合GenCorrect达468分（超金线438.3），大模型Ultra-CC达502分；在IOI 2026的前瞻性实战评估中，Competition Ultra-CC以535.4/600超越金线361.12和最高人类498.27，首次在IOI题集上超过最高分人类选手。

#### 方法
- 数据与评测环境：从16个竞赛体系与在线平台整理22,000题，构建可执行评测环境（题面、约束、测试、参考解），确保判题一致性；排除并去重IOI 2025、ICPC 2025、LiveCodeBench Pro等评测集。
- 合成推理与SFT：用DeepSeek-V4-Flash生成1.2M（Nano）/477,642（Ultra）条推理与自改进轨迹，难题给更多样本，进行长上下文SFT。
- 强化学习：在Nemotron-3-Nano-30B-A3B上进行带可执行奖励的RL，得到Nemotron-3-Nano-CC；在Nemotron-3-Ultra-550B-A55B上仅进行SFT得到Nemotron-3-Ultra-CC（未做代码RL）。
- 测试时计算GenCorrect：闭环“生成-评测-反馈-再生成”，多轮迭代（5轮，每轮+10次提交，在官方50次提交内）生成多样解并用反馈纠错与引导后续生成。
- 模型与推理设置：MoE架构，Nano为30B总参/3B激活，Ultra为550B/55B激活；统一采用GenCorrect。具体RL算法细节、训练超参与推理硬件配置文中未明确说明。

#### 创新点
- 提出覆盖数据、SFT、RL与测试时计算的一体化竞赛编程专精流水线，并使用可执行奖励将代码正确性直接纳入RL目标。
- 提出GenCorrect，在严格提交预算下利用判题反馈进行多样化解的迭代纠错与优化的闭环TTC策略。
- 系统性实证分解合成数据、SFT、RL、模型规模与TTC对性能的相对贡献，给出从基础到金牌水平的能力提升轨迹。
- 进行严格的前瞻性实战评估：在IOI 2026按与人类一致的时间、网络与提交限制运行系统，验证外部有效性。

#### 实验结论
- IOI 2025：Nemotron-3-Nano-CC Score@1由130（基线）→280（SFT）→291（RL）；结合GenCorrect（5轮、50次提交）达468，超过金线438.3。Nemotron-3-Ultra-CC无代码RL的情况下Score@1为304，结合GenCorrect达502。
- IOI 2026（前瞻性、非官方计分）：Competition Ultra-CC在与人类等价限制下得分535.4/600，超过金线361.12与最高人类498.27，作者称为首次在IOI题集上超越最高分人类选手的AI系统。
- 训练与数据支撑：22,000题与最多1.2M合成推理轨迹支撑SFT；RL与GenCorrect对小模型提升显著，而大模型在SFT+TTC下亦可达金牌水平。更细粒度消融细节文中未明确说明。
