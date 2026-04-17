# 2026-04-18 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Bird-SR: Bidirectional Reward-Guided Diffusion for Real-World Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2602.07069v2
- **作者**: Zihao Fan, Xin Lu, Yidi Liu, Jie Huang, Dong Li, Xueyang Fu, Baocai Yin
- **原始摘要**: Powered by multimodal text-to-image priors, diffusion-based super-resolution excels at synthesizing intricate details; however, models trained on synthetic low-resolution (LR) and high-resolution (HR) image pairs often degrade when applied to real-world LR images due to significant distribution shifts. We propose Bird-SR, a bidirectional reward-guided diffusion framework that formulates super-resolution as trajectory-level preference optimization via reward feedback learning (ReFL), jointly leveraging synthetic LR-HR pairs and real-world LR images. For structural fidelity easily affected in ReFL, the model is directly optimized on synthetic pairs at early diffusion steps, which also facilitates structure preservation for real-world inputs under smaller distribution gap in structure levels. For perceptual enhancement, quality-guided rewards are applied to both synthetic and real LR images at the later trajectory phase. To mitigate reward hacking, the rewards for synthetic results are formulated in a relative advantage space bounded by their ground-truth counterparts, while real-world optimization is regularized via a semantic alignment constraint. Furthermore, to balance structural and perceptual learning, we introduce a dynamic fidelity-perception weighting strategy that emphasizes structure preservation at early stages and progressively shifts focus toward perceptual optimization at later diffusion steps. Extensive experiments on real-world SR benchmarks demonstrate that Bird-SR consistently outperforms state-of-the-art methods in perceptual quality while preserving structural consistency, validating its effectiveness for real-world super-resolution. Our code can be obtained at https://github.com/fanzh03/Bird-SR.

### GPT总结
#### 文章内容
这篇论文针对合成LR-HR配对训练与真实世界LR输入之间的显著分布偏移导致的退化问题，以及直接进行感知奖励优化易“奖励黑客化”的风险，提出Bird-SR：一种双向、基于奖励反馈学习（ReFL）的扩散式超分框架。核心思路是在扩散轨迹的早期用合成配对直接优化结构保真，在后期对合成与真实LR共同施加质量引导的奖励，并通过相对优势空间与语义对齐约束抑制奖励黑客化；同时引入沿轨迹动态的保真-感知权重。实验表明，Bird-SR在真实世界超分基准上在感知质量上优于SOTA且保持结构一致性。

#### 方法
- 双向奖励引导：前向过程在合成HR上注入高斯噪声并用闭式单步公式恢复，实现结构保真的直接优化；反向过程沿去噪轨迹进行奖励反馈以提升真实与合成LR的感知细节。
- 相对优势奖励：对合成数据的结果在以GT为边界的相对优势空间中定义奖励，稳定训练并缓解奖励黑客化，同时提供灵活的时间步控制。
- 语义对齐约束：在真实世界优化中加入语义对齐以约束结构一致性，奖励信号主要在后期时间步作用于纹理与高频细节。
- 动态保真-感知加权：沿扩散轨迹早期强调结构保真，后期逐步转向感知优化，以平衡失真与感知。
- 依据扩散的时序机制（早期生成语义、后期合成纹理），在ReFL框架下联合利用合成LR-HR与真实LR数据进行轨迹级偏好优化。

#### 创新点
- 将超分任务建模为扩散“轨迹级”偏好优化（ReFL），并在前向与反向两个方向上协同对齐合成与真实数据。
- 提出基于噪声注入与“以GT为界”的相对优势奖励的稳定前向优化策略，显著降低奖励黑客化并增强结构监督。
- 在真实世界优化中引入语义对齐约束，针对无配对场景保证结构一致性同时提升感知质量。
- 设计沿扩散轨迹的动态保真-感知权重，显式协调结构与感知的时序性权衡。

#### 实验结论
- 任务：真实世界图像超分（Real-World SR）；数据集与具体指标文中未明确说明，仅称“real-world SR benchmarks”。
- 核心结果：Bird-SR在真实世界基准上“consistently outperforms state-of-the-art methods in perceptual quality while preserving structural consistency”。
- 辅助证据：t-SNE（VGG、LBP）与KDE分析揭示真实与合成数据在纹理域存在显著差异，而语义在轨迹各阶段更为一致，支持“早期结构/后期纹理”的时序优化设计。

## 关键词：reinforcement learning

## RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework
- **论文链接**: http://arxiv.org/abs/2604.15308v1
- **作者**: Hao Gao, Shaoyu Chen, Yifan Zhu, Yuehao Song, Wenyu Liu, Qian Zhang, Xinggang Wang
- **原始摘要**: High-level autonomous driving requires motion planners capable of modeling multimodal future uncertainties while remaining robust in closed-loop interactions. Although diffusion-based planners are effective at modeling complex trajectory distributions, they often suffer from stochastic instabilities and the lack of corrective negative feedback when trained purely with imitation learning. To address these issues, we propose RAD-2, a unified generator-discriminator framework for closed-loop planning. Specifically, a diffusion-based generator is used to produce diverse trajectory candidates, while an RL-optimized discriminator reranks these candidates according to their long-term driving quality. This decoupled design avoids directly applying sparse scalar rewards to the full high-dimensional trajectory space, thereby improving optimization stability. To further enhance reinforcement learning, we introduce Temporally Consistent Group Relative Policy Optimization, which exploits temporal coherence to alleviate the credit assignment problem. In addition, we propose On-policy Generator Optimization, which converts closed-loop feedback into structured longitudinal optimization signals and progressively shifts the generator toward high-reward trajectory manifolds. To support efficient large-scale training, we introduce BEV-Warp, a high-throughput simulation environment that performs closed-loop evaluation directly in Bird's-Eye View feature space via spatial warping. RAD-2 reduces the collision rate by 56% compared with strong diffusion-based planners. Real-world deployment further demonstrates improved perceived safety and driving smoothness in complex urban traffic.

### GPT总结
#### 文章内容
论文针对高维连续轨迹的扩散式模仿学习规划在闭环场景中易出现随机不稳定、缺乏负反馈和信用分配困难的问题，提出RAD-2生成器-判别器一体化框架。核心思想是用扩散生成器产生多样候选轨迹，用经RL优化的判别器在闭环中按长期驾驶质量重排序，并通过Temporally Consistent Group Relative Policy Optimization与On-policy Generator Optimization稳定、有效地利用稀疏奖励。结果显示，在闭环评估中相较强扩散式规划器碰撞率降低56%，并在真实道路部署中提升主观安全感与平顺性。

#### 方法
- 生成器-判别器解耦：扩散式生成器生成多模态候选，RL优化的判别器输出低维轨迹评分进行重排，避免将稀疏标量奖励直接作用于高维轨迹空间，提升优化稳定性。
- Temporally Consistent Group Relative Policy Optimization：利用时序一致性进行分组相对优化，缓解信用分配问题并稳定策略更新。
- On-policy Generator Optimization：将闭环反馈转换为结构化“纵向”优化信号，仅在纵向维度上推移生成器分布至高回报流形，保留轨迹形状并提高训练稳定性。
- BEV-Warp仿真：在Bird’s-Eye View特征空间中通过空间扭转载体实现高吞吐闭环评估，避免游戏引擎/重建/生成式世界模型的效率与保真权衡。
- 训练与推理：先用约50,000小时真实驾驶数据对扩散生成器进行IL预训练；闭环中每步生成多候选并由判别器重排选择；生成器与判别器在同一交互数据上联合优化，无需额外仿真开销。

#### 创新点
- 规划中的生成器-判别器协同：将RL限定在与奖励维度匹配的判别器上，实现低维评分对高维轨迹的稳定指导。
- 新的RL优化策略：提出Temporally Consistent Group Relative Policy Optimization以显式利用时序一致性做信用分配。
- 生成器在策略内优化：提出On-policy Generator Optimization，聚焦纵向分量的结构化优化，避免对全轨迹做不稳定的RL更新。
- 高效闭环仿真：提出BEV-Warp在特征空间进行空间扭转的轻量化闭环训练框架，兼顾效率与环境保真度。

#### 实验结论
- 任务与数据：面向闭环自动驾驶规划；生成器以约50,000小时真实驾驶数据预训练；在BEV-Warp中从50k段10–20秒日志片段闭环评估与筛选，聚焦高碰撞风险与低效率场景。
- 主要结果：相较强扩散式规划器，RAD-2将碰撞率降低56%；真实道路部署显示更高的主观安全感与行驶平顺性。
- 其他量化指标与消融、训练效率对比的具体数值文中未明确说明。
