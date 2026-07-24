# 2026-07-25 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Texture++: Elevating 3D Asset Texture Resolution with a Region-Aware Diffusion Model
- **论文链接**: http://arxiv.org/abs/2607.21504v1
- **作者**: Shuaiwei Wang, Shi Li, Jieting Xu, Yuchi Huo, Qi Wang, Wenting Zheng, Rengan Xie
- **原始摘要**: Numerous 3D assets are discarded due to low texture resolution, while current super-resolution models ignore texture maps and focus on natural images. An efficient and generalizable texture super-resolution model can revitalize a large corpus of aging yet valuable assets across industries such as film and video games. We present Texture++, a novel framework for texture super-resolution, which enhances the low-resolution textures of assets to produce high-resolution, high-quality results. Specifically, we reformulate the task of super-resolution in UV space into performing it across multiple rendered views and merging the outputs. Firstly, to achieve more complete and continuous textures in the view space, we propose an adaptive view selection strategy to integrate textures dispersed across UV texture patches. Furthermore, we introduce a quadtree-based texture region organization method for combining super-resolved textures from different viewpoints, providing masks to distinguish regions that require improvement. Finally, we design a diffusion-based super-resolution model that enhances the texture resolution for specified masked regions, seamlessly integrating with surrounding regions. Through comprehensive evaluations, we demonstrate that our approach yields textures with substantially improved detail and coherence over existing methods.

### GPT总结
#### 文章内容
- 论文针对大量3D资产因UV纹理分辨率过低而无法复用的问题，提出一个面向纹理贴图的通用超分辨率框架Texture++。  
- 核心思路是将UV空间的SR重构为多视角渲染空间的SR与融合：自适应选取观察视角，基于四叉树组织纹理区域并生成改进掩码，最后用区域感知的单步扩散模型对掩码区域进行SR并无缝融合。  
- 实验表明方法在细节、连贯性和无缝性方面显著优于现有图像SR与纹理生成方法，同时具备较高效率。

#### 方法
- 将UV空间的纹理SR任务重构为多视角渲染图像的SR与结果合并，以提升覆盖度与跨补丁连续性。  
- 自适应视角选择策略：在视图空间整合分散于UV补丁的纹理信息，获得更完整、连续的观察。  
- 基于四叉树的纹理区域组织：从不同视角的SR结果中生成区域掩码，区分需要改进的局部并指导合并。  
- 区域感知扩散式SR模块：对指定掩码区域进行增强，并与周边区域无缝衔接；采用单步扩散以提升推理效率。  
- 迭代式细化流程：在渲染视图上进行局部SR，生成混合分辨率的渲染结果并逐步融合，减少UV边界接缝与冲突。

#### 创新点
- 任务建模创新：将UV纹理SR转化为多视图渲染空间的SR与融合，显著缓解UV边界接缝与跨补丁不连续问题。  
- 区域级组织与掩码机制：四叉树划分与区域掩码引导跨视角结果的冲突消解与无缝合并，实现“需要则精修”的局部SR。  
- 决策机制创新：自适应视角选择覆盖分散纹理要素，提升可观测性与重建完整性。  
- 高效生成模块：面向局部掩码设计的单步扩散SR模型，兼顾质量与速度并适配混合分辨率渲染输入。

#### 实验结论
- 任务与数据：针对4×纹理SR开展评测；数据集与训练细节文中未明确说明。  
- 核心结果：在PSNR/SSIM/LPIPS/DISTS上优于SOTA图像SR（如DiffBIR, HYPIR, OSEDiff, InvSR, PiSASR）与纹理生成方法（Text2Tex, Paint3D, MVPaint），例如Table 1中Our达到PSNR 37.5277, SSIM 0.9524, LPIPS 0.0637, DISTS 0.0736；推理时间94.4 s，快于多数对比方法。  
- 结论与消融：可见域无缝性与文字/结构保真度显著提升；消融显示自适应视角、四叉树掩码与局部掩码式合成均为关键（完整模型在消融表中PSNR 38.4241，为最佳）。

## 关键词：reinforcement learning

## Drive As You Like: Multi-Head Diffusion with Reinforcement Learning for Personalized Driving
- **论文链接**: http://arxiv.org/abs/2508.16947v2
- **作者**: Fan Ding, Xuewen Luo, Fucai Ke, Hwa Hui Tew, Susilawati Susilawati, Vishnu Monn Baskaran, Junn Yong Loo
- **原始摘要**: Despite significant progress, imitation learning-based autonomous driving planners remain largely restricted to reproducing high-frequency biased behaviors, overlooking the inherent behavioral diversity of human driving. Moreover, existing systems struggle to understand user intent from human interactions and environmental contexts. In real-world advanced deployment, motion planning must accommodate diverse, context-dependent user preferences to support heterogeneous driving services, requiring the ability to interpret human intent and adapt behavior accordingly. However, existing approaches lack such user-oriented capabilities, as they neither explicitly model user intent nor enable flexible policy adaptation. To bridge this gap, we propose an RL-guided multi-strategy framework with a diffusion-based multi-head planner(M-Diffusion Planner) integrated with LLM-based semantic understanding, enabling dynamic perception of user intent and generation of diverse, preference-aligned trajectories. To balance trajectory quality and strategy alignment, we adopt a two-stage training paradigm: first, imitation learning ensures each policy head achieves safe and high-quality planning; second, constrained Group Relative Policy Optimization (GRPO) further aligns each head with user preferences. Experiments on the nuPlan benchmark, under both open-loop and closed-loop settings, demonstrate competitive performance while meeting real-time planning requirements and effectively aligning with user intent.

### GPT总结
#### 文章内容
该文针对模仿学习规划易受高频行为偏置、难以理解用户意图且缺乏可控多样性的痛点，提出面向个性化驾驶的规划框架。核心思路是将LLM语义理解与RL引导的多策略、多头扩散式规划器（M-Diffusion Planner）结合，通过两阶段训练（先模仿、后受限GRPO）在保证轨迹安全与质量的同时对齐用户偏好。实验在nuPlan的开环与闭环设置下验证方法可实时运行、可生成差异化且符合偏好的轨迹，并取得与SOTA相竞争的成绩。

#### 方法
- 多头扩散规划器（M-Diffusion Planner）：为不同驾驶策略配置独立策略头（如Base、Aggressive、Conservative、Comfortable），基于扩散建模生成多样轨迹。
- LLM语义理解：从人机交互与环境语境解析用户意图，并用于条件化规划或策略头选择；具体提示词、接入方式文中未明确说明。
- 两阶段训练：阶段一以模仿学习确保各头具备安全且高质量的轨迹生成能力；阶段二采用受限Group Relative Policy Optimization（GRPO）使各头与对应用户偏好对齐（奖励细节与约束形式文中未明确说明）。
- 推理与控制：按20 Hz、0.5 s规划周期在线生成偏好一致的轨迹；与控制器或下游模块的耦合细节文中未明确说明。

#### 创新点
- 将LLM驱动的意图理解与RL引导的多策略扩散规划相结合，实现对用户偏好的决策级显式建模与可控风格生成。
- 采用“模仿学习→受限GRPO”的两阶段范式，同时兼顾轨迹质量与偏好对齐，缓解仅以语言条件或监督学习带来的软约束与可控性不足。
- 多头结构显式刻画多种驾驶风格，突破数据高频行为偏置对稀有/情境化策略的抑制，增强人机交互与长期一致性。
- 相较标签引导或单一头IL方法，在策略多样性与交互性上更强，支持基于用户意图的持续调整。

#### 实验结论
- 任务与数据：在nuPlan基准进行开环与闭环评测（val14），包含非反应与反应模式；仿真20 Hz、规划周期0.5 s。
- 结果：与Diffusion Planner、PDM、UrbanDriver等基线对比具有竞争力，同时不同策略头呈现显著行为差异；表中给出多项评分，如Base 88.73、Aggressive 82.63、Conservative 85.51、Comfortable 88.72（具体指标名称文中未明确说明）。
- 作者结论：方法满足实时规划需求，能够有效对齐用户意图并生成多样、偏好一致的轨迹。
