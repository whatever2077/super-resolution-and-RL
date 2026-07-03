# 2026-07-04 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Seek to Segment: Active Perception for Panoramic Referring Segmentation
- **论文链接**: http://arxiv.org/abs/2607.02497v1
- **作者**: Song Tang, Shuming Hu, Xincheng Shuai, Henghui Ding, Yu-Gang Jiang
- **原始摘要**: Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruction for segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual memory. By progressively integrating sequential local observations into a unified 360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-redundant search trajectories. Once the target is found, the agent performs active viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning, followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's exploration efficiency. Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

### GPT总结
#### 文章内容
该文提出Active Panoramic Referring Segmentation (APRS) 新任务，要求智能体在连续360°环境中根据语言指令主动调整视角搜索并分割目标。核心思路是构建PanoSeeker：以Vision-Language Model为基础，引入显式空间可视记忆EgoSphere，将连续局部观测逐步整合为统一的360°表示，用于规划高效、非冗余的搜索轨迹，并在找到目标后进行主动视角对齐输出分割。作者基于专家标注的搜索轨迹与记忆时间线进行监督微调，随后通过强化学习后训练优化探索效率。实验显示，PanoSeeker在新建APRS基准上显著提升搜索效率与分割精度，优于改造的现有方法。

#### 方法
- 任务建模：从初始朝向(θ0, ϕ0)出发，智能体在每步t感知Vt并维护记忆Mt，输出动作at=(Δθt, Δϕt)或终止信号以触发分割；视图由equirectangular panorama经gnomonic投影获取，FoV设为ψh=120°、ψv=90°。
- 空间记忆EgoSphere：将时序局部视图显式映射到固定分辨率的360°画布，形成统一全景表示，提供稳定、常长度上下文并支持跨视角空间推理。
- 视觉语言集成：以VLM驱动感知与指令理解，结合EgoSphere规划非冗余视角移动并进行目标在场性判断与定位。
- 主动对齐与分割：检测到目标后执行视角微调（active viewpoint alignment），再输出目标分割掩码。
- 训练范式：先以专家标注的搜索轨迹和记忆时间线进行Supervised Fine-Tuning，再用Reinforcement Learning后训练显式优化探索效率；推理时按上述感知-记忆-决策闭环运行。

#### 创新点
- 提出APRS任务，强调在连续360°环境中结合语言指令的主动感知与分割，区别于传统静态单视图RIS。
- 设计EgoSphere为显式空间视觉记忆，将多步观测整合为统一全景并保持上下文长度恒定，缓解历史扩张带来的检索与冗余问题。
- 记忆增强的VLM智能体框架，实现高效、非冗余的搜索轨迹规划与主动视角对齐，兼顾定位与精细分割。
- 构建带有专家搜索轨迹与记忆时间线的监督数据，并结合强化学习后训练，直接优化探索效率这一目标。

#### 实验结论
- 任务与数据：在新建立的APRS基准上评测，场景来自360-Indoor、PANDORA、SUN360，共4,971个全景场景；通过gnomonic投影生成视图（ψh=120°、ψv=90°）。
- 核心结果：PanoSeeker在搜索效率与分割精度上均显著优于改造的state-of-the-art基线，证明空间记忆与RL后训练对主动感知有效。
- 作者结论：相较被动全景处理或代价高昂的显式3D重建方案，EgoSphere+VLM的记忆增强式主动感知在效率与精度间取得更佳平衡。文中未明确说明具体数值指标与消融细节。
