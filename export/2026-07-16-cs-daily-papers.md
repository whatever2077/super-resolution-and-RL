# 2026-07-16 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## RFMSR: Residual Flow Matching for Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2607.12753v1
- **作者**: Shuwei Huang, Tianyao Luo, Jicheng Liu, Daizong Liu, Pan Zhou
- **原始摘要**: Image super-resolution (ISR) has witnessed remarkable progress with diffusion models and flow matching. The dominant text-to-image (T2I) based approaches leverage large-scale foundation models as generative priors, achieving impressive perceptual quality but at the cost of massive model sizes and prohibitive training expenses. Recent flow-matching-based vision-only approaches have made significant strides; however, they adopt standard flow formulations that transport from a pure Gaussian prior to the data distribution, discarding the rich structural information already present in the low-quality (LQ) input. Furthermore, existing single-step acceleration techniques often forfeit the model's multi-step inference capability. In this paper, we propose Residual Flow Matching for Image Super-Resolution (RFMSR), a vision-only framework that centers the source distribution at the LQ latent, reducing transport distance and preserving structural priors throughout the flow trajectory. We further introduce a two-phase training strategy: Phase I pretrains the velocity field via conditional flow matching, while Phase II applies end-to-end supervision to the single-step prediction while retaining the velocity loss across all timesteps, achieving high-quality single-step generation without sacrificing multi-step refinement. Extensive experiments demonstrate that RFMSR achieves comparable or even superior perceptual quality compared to state-of-the-art (SOTA) methods. The source code is available at https://github.com/Faze-Hsw/RFMSR.

### GPT总结
#### 文章内容
- 论文聚焦于单幅图像超分辨率中的生成式方法，指出标准流匹配从高斯先验出发会丢弃低质图像（LQ）中已有的结构信息，且现有单步加速常牺牲多步推理能力。
- 提出RFMSR，通过“残差流匹配”将源分布居中到LQ潜变量，缩短传输距离并沿轨迹保留结构先验；并采用两阶段训练兼顾单步高质生成与多步细化。
- 实验显示RFMSR在感知质量上可与或优于SOTA，且单步与多步兼容。

#### 方法
- 残差流匹配：在潜空间以LQ编码y0为源分布中心，而非纯高斯，从而在流动轨迹中保留结构先验并降低数据传输距离；以条件流匹配学习速度场。
- 两阶段训练：Phase I 用Conditional Flow Matching预训练速度场；Phase II 在保持全时刻速度损失的同时，对单步预测施加端到端监督，实现单步生成而不损失多步性能。
- 模型与条件：采用VOSR同构的LightningDiT（0.5B）为骨干，SD2.1 VAE进行图像编码，DINOv2-Base提供语义特征；条件c = (y0, DINOv2(LQ Image))，从VOSR权重初始化。
- 数据与配置：约100万张高质图像，经Real-ESRGAN退化合成HQ-LQ对；训练/评测以×4 ISR为主，噪声水平设为σ=1.0；HR裁剪为512×512并退化到128×128。
- 推理方式：支持多步细化与单步快速生成两种模式。

#### 创新点
- 将流匹配的源分布从纯高斯改为以LQ潜变量为中心的残差流，显著缩短OT路径并显式利用输入结构先验。
- 提出保留多步能力的单步训练机制：在Phase II对单步输出进行端到端监督，同时维持全时刻速度损失，避免常见的“单步加速—多步退化”权衡。
- 纯视觉范式（vision-only）规避T2I巨型先验与文本提示依赖，降低参数规模与训练成本，减少语义幻觉带来的不一致细节。
- 在训练目标设计上，结合残差流与跨时刻速度一致性，提升单/多步统一性与感知质量。

#### 实验结论
- 任务与数据：主评×4 ISR；训练集约100万张经Real-ESRGAN合成的HQ-LQ对；测试于RealSR、以及从ImageNet和LSDIR各随机采样的250张图像。
- 对比与指标：对比ResShift、SeeSR、VOSR、OSEDiff、SinSR、InvSR等，采用PSNR/SSIM、LPIPS/DISTS/FID与NIQE/MUSIQ/MANIQA/CLIPIQA等指标。
- 结果与结论：RFMSR在感知质量上达到或超过SOTA，单步模型获得高质输出且保留多步细化能力；具体数值与显著性差异文中未明确说明。

## 关键词：reinforcement learning

## DenseReward: Dense Reward Learning via Failure Synthesis for Robotic Manipulation
- **论文链接**: http://arxiv.org/abs/2607.13033v1
- **作者**: Yu Fang, Wanxi Dong, Jiaqi Liu, Yue Yang, Mingxiao Huo, Yao Mu, Huaxiu Yao, Li Erran Li, Daniel Szafir, Mingyu Ding
- **原始摘要**: Reinforcement learning holds great promise for improving robot policies beyond the limits of imitation learning. However, its practical adoption remains bottlenecked by the lack of reliable vision-language reward models that provide dense and informative feedback. Two key challenges remain: acquiring diverse failure data at scale and obtaining fine-grained reward signals beyond sparse trajectory-level success labels. Collecting failure trajectories typically requires laborious human effort, while pseudo-failures constructed by relabeling successful demonstrations fail to capture the diverse physical failure modes that arise during robot execution. Meanwhile, existing reward models often predict sparse binary or trajectory-level rewards, which provide limited guidance for efficient policy optimization. We introduce DenseReward, a dense robotic reward model that addresses both challenges. To train DenseReward, we develop an automated failure data generation pipeline that synthesizes physically realistic failure trajectories in simulation without human labeling, covering diverse failure modes such as collisions, missed grasps, object drops, and recovery behaviors. DenseReward predicts dense frame-level reward scores from visual observations and language instructions, enabling fine-grained estimation of task progress throughout an episode. Experiments show that DenseReward outperforms general-purpose VLMs and existing robotic reward models in dense reward prediction across both simulated and real-world manipulation. We further demonstrate that DenseReward provides effective reward guidance for downstream model predictive control and reinforcement learning. We release the dataset, trained reward models, and evaluation suite to support the development of failure-aware dense reward modeling for robot learning.

### GPT总结
#### 文章内容
该文针对机器人操作中缺乏可靠的视觉-语言密集奖励模型这一瓶颈，聚焦于两大难题：难以规模化获取多样失败数据与仅有稀疏/轨迹级奖励。作者提出DenseReward，通过在仿真中自动合成物理真实的失败轨迹，并学习从视觉与指令到帧级奖励的映射，实现细粒度任务进度评估。实验显示，DenseReward在模拟与真实操作的密集奖励预测上优于通用VLM与现有机器人奖励模型，并能为MPC与RL提供有效奖励指导。

#### 方法
- 自动数据生成：将操作分解为五个阶段（Reach/Grasp/Lift/Move/Place），随机化场景；用GraspNet从多视角RGB-D提出最多N=50个抓取候选，结合CuRobo进行避碰规划，执行六段运动并基于仿真状态自动检测阶段边界。
- 失败合成：在抓取检测与运动规划中注入针对性扰动，诱发碰撞、错抓（抓取偏移）、运输中掉落、次优运动与恢复等多种物理真实失败模式，形成覆盖成功到失败再到恢复的多样轨迹。
- 密集奖励标注：为每步时间t赋予rt∈[0,1]的帧级奖励，随任务进度单调上升，并能体现失败后的退化与恢复过程，无需人工标注。
- 模型训练与推理：DenseReward输入语言指令与当前/历史图像帧，推断当前执行状态/失败类型并输出标量帧级奖励；训练在成功与失败混合轨迹上进行，具体网络结构与损失设计文中未明确说明。
- 下游应用：将预测的密集奖励用于MPC与强化学习中的策略优化，以克服稀疏回报的信用分配难题。

#### 创新点
- 提出面向失败的密集奖励建模：通过仿真中自动合成物理真实失败（非截断或重标注的伪失败），系统覆盖碰撞、错抓、掉落、恢复等关键失效模式。
- 阶段感知的任务建模：五阶段分解使得无需人工即可生成帧级、进度一致的密集奖励，并支持对失败与恢复过程的细粒度刻画。
- 视觉-语言到帧级奖励的统一模型：相较于仅给出轨迹末端二值/稀疏奖励的既有方法，DenseReward直接输出反映中间状态与进度的密集评分。
- 资源与评测：发布含27k episodes的数据集、训练好的奖励模型与评估套件，促进失败感知的密集奖励研究。

#### 实验结论
- 在模拟与真实机器人操作的密集奖励预测上，DenseReward优于通用VLM与现有机器人奖励模型，体现更准确的进度评估能力（具体数值文中未明确说明）。
- 作为下游信号，DenseReward为MPC与强化学习提供有效的密集回报指导，改善策略优化效率（具体算法与提升幅度文中未明确说明）。
- 数据覆盖DROID、Isaac Sim、RoboSuite、LIBERO等场景，合计约27k episodes，并配套评估基准；更详尽的实验设置与指标文中未明确说明。
