# 2026-08-19 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Binarized High-Efficiency RAW Video Restoration and Beyond
- **论文链接**: http://arxiv.org/abs/2608.16756v1
- **作者**: Tianyu Zhu, Ying Fu, Hesong Li, Gengchen Zhang, Xin Yuan, Yulun Zhang
- **原始摘要**: RAW video restoration is fundamental to high-quality low-level perception and serves as the basis for a wide range of downstream vision applications. While binary neural networks (BNNs) enable efficient lightweight deployment for image enhancement, their deficiencies in modeling temporal coherence and activation value distributions hinder their effectiveness when applied to video scenarios. In this paper, we propose BinRVR, a binarized RAW video restoration framework that reduces computation and parameters by approximately 96% while incurring only about 4% performance degradation. Specifically, we present a Binarized Information Interaction Module (BIIM) to jointly model spatial and temporal information in an efficient and unified manner. Moreover, we develop a Distribution-Aware Binarized Convolution (DAB-Conv) that leverages the statistics of full-precision activations to mitigate quantization errors. The proposed framework further supports multi-bit quantization, enabling flexible accuracy-efficiency trade-offs across different hardware constraints. Extensive experiments demonstrate that our BinRVR achieves competitive performance compared with state-of-the-art binarized methods on RAW video restoration tasks, including low-light enhancement, denoising, deblurring, and super-resolution. We further explore the potential of our method on downstream video applications, including object detection and monocular depth estimation.

### GPT总结
#### 文章内容
- 论文针对RAW视频恢复中BNN难以建模时域一致性与激活分布的问题，提出高效的二值化框架BinRVR。
- 核心思路是设计联合时空的信息交互模块（BIIM）与分布感知的二值卷积（DAB-Conv），在保持效率的同时缓解量化误差；并支持多比特量化以灵活权衡精度与效率。
- 主要结论是：在约96%计算与参数压缩的前提下仅带来约4%的性能下降；在低照度增强、去噪、去模糊和超分等RAW视频任务上对比SOTA二值化方法具备竞争力，并在下游检测与单目深度估计上展现潜力。

#### 方法
- 提出BinRVR：面向RAW视频恢复的端到端二值化框架，对权重与激活进行极低比特表示以实现高压缩与低计算。
- Binarized Information Interaction Module（BIIM）：在统一、轻量的结构中联合建模空间与时间信息，面向BNN友好设计，避免复杂对齐与注意力操作带来的二值化不稳定。
- Distribution-Aware Binarized Convolution（DAB-Conv）：利用全精度激活的统计信息引导二值卷积，缓解符号化带来的量化误差累积。
- 支持multi-bit quantization：在不同硬件约束下实现精度-效率可调，兼容二值与多比特推理。
- 训练/推理范式：采用分布感知的量化设计，推理时以低比特运算获得高吞吐与低存储；其他训练细节文中未明确说明。

#### 创新点
- 面向视频场景的分布感知二值卷积（DAB-Conv），显式利用全精度激活统计以降低BNN在跨层/跨帧分布差异下的量化误差。
- 设计BNN友好的时空信息交互模块（BIIM），在不依赖光流/可变形卷积/复杂注意力的前提下高效融合时空信息。
- 在RAW视频恢复领域系统性探索二值化与多比特量化的统一框架，并扩展至下游视频应用验证。
- 在极端压缩（约96%）下仅约4%性能损失，展示了二值化在RAW视频恢复中的实用性边界。

#### 实验结论
- 任务覆盖：RAW视频低照度增强、去噪、去模糊、超分；并进一步评估下游object detection与monocular depth estimation。
- 结果概述：相较SOTA二值化方法取得竞争性性能；在计算与参数上约减少96%，仅约4%性能下降；具体数据集与度量指标文中未明确说明。
- 作者结论：BinRVR在多类RAW视频恢复任务上兼具高效与高质，并在下游感知任务上显示可迁移的恢复收益。

## 关键词：reinforcement learning

## Q-based Variational Inverse Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2608.16888v1
- **作者**: Ondrej Bajgar, Peter Tisnikar, Alessandro Abate, Konstantinos Gatsis, Maike Osborne
- **原始摘要**: The development of safe and beneficial AI requires that systems can learn and act in accordance with human preferences. However, explicitly specifying these preferences by hand is often infeasible. Inverse reinforcement learning (IRL) addresses this challenge by inferring preferences, represented as reward functions, from expert behaviour. We introduce Q-based Variational IRL (QVIRL), a novel Bayesian IRL method that recovers a posterior distribution over rewards from expert demonstrations via primarily learning a variational distribution over optimal Q-values. Unlike previous approaches, QVIRL combines scalability with uncertainty quantification, important for safety-critical applications as well as active learning. We demonstrate QVIRL's strong performance in apprenticeship learning across various tasks, including gridworlds, Lunar Lander, the Highway Environment, and two ATARI games both with static expert data and with active learning. It is the first method for Bayesian IRL that demonstrates training from raw pixel observations.

### GPT总结
#### 文章内容
- 论文关注在不易手动指定偏好的情况下，从专家演示中推断人类偏好的奖励函数，提出一种可扩展且可量化不确定性的贝叶斯IRL方法 QVIRL。
- 核心思路是直接学习最优Q-values的变分分布，并由此诱导出奖励的后验分布，从而在保持可扩展性的同时提供对Q和奖励的不确定性估计。
- 实验表明，QVIRL在apprenticeship learning上于多种任务（gridworlds、Lunar Lander、Highway Environment、两款ATARI）表现强劲，并支持从原始像素训练；在主动学习中，基于Q后验的不确定性可有效驱动查询策略。
- 作者结论是：QVIRL能在更复杂环境中实现贝叶斯IRL的后验估计与不确定性量化，优于仅点估计或仅奖励后验的方法，并可作为主动IRL的可扩展贝叶斯骨干。

#### 方法
- 以奖励函数的先验为起点，基于专家近似最优演示，构建并优化关于最优Q-values的变分分布，以近似贝叶斯后验；具体变分目标形式文中未明确说明。
- 通过学得的Q-value后验诱导出奖励后验，实现对“Q与奖励”双重不确定性的联合量化。
- 采用高效的梯度型训练范式，配合函数逼近器以支持连续状态与原始像素输入；具体网络结构文中未明确说明。
- 在apprenticeship learning中，利用得到的后验（或其点估计/采样）导出策略；具体策略提取机制文中未明确说明。
- 将QVIRL与主动查询机制集成，结合Reward EIG与ActiveVaR等获取函数，利用Q后验的不确定性来选择信息量大的查询。

#### 创新点
- 从“最优Q-values”入手进行变分贝叶斯建模，并由Q后验派生奖励后验，区别于仅对奖励建模或MCMC采样的传统贝叶斯IRL。
- 在保持可扩展性的同时提供校准良好的不确定性估计，弥补了非贝叶斯IRL的点估计与MCMC方法难以扩展的缺陷。
- 首次在Bayesian IRL框架下实现从原始像素观测端到端训练，拓展了贝叶斯IRL在高维感知输入下的适用性。
- 通过显式Q后验使主动IRL可扩展地使用以Q或策略不确定性为目标的获取函数（如Reward EIG、ActiveVaR），克服仅有奖励后验方法（如AVRIL）在主动学习中的瓶颈。

#### 实验结论
- 任务覆盖gridworlds、Lunar Lander、Highway Environment与两款ATARI游戏，并在静态专家数据与主动学习两种设置下评测。
- 在apprenticeship learning对比中，QVIRL获得与最强基线相当或更优的Return，并显著优于AVRIL的对数似然（例如某表中LL为-2.09而AVRIL为-8.79；具体对应环境文中未明确说明），同时在另一个对比中Return为701±42且LL为-5.19±1.04（对应环境文中未明确说明）。
- 在主动学习中：在随机化gridworlds里，QVIRL+Reward EIG接近ValueWalk，而AVRIL在约10次查询后停滞；在Lunar Lander中，QVIRL结合Reward EIG或ActiveVaR均明显优于随机查询，显示其作为可扩展贝叶斯主动IRL骨干的有效性。
