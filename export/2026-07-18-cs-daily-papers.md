# 2026-07-18 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Domain Adaptation of Mismatched Proximal Denoiser for Plug-and-Play Image Reconstruction
- **论文链接**: http://arxiv.org/abs/2607.14894v1
- **作者**: Guixian Xu, Jinglai Li, Junqi Tang
- **原始摘要**: Plug-and-play proximal gradient descent (PnP-PGD) enables flexible image reconstruction by using denoisers as implicit priors. In practice, these denoisers are often deployed outside their training domains. Existing analyses establish convergence under structural assumptions on the deployed denoiser, such as requiring it to be a proximal map or a contraction. However, they do not measure how domain mismatch affects convergence of PnP-PGD. We define this effect as \emph{proximal mismatch}: the discrepancy between a deployed denoiser $\widehat{\mathsf D}$ and a target-domain reference map $\mathsf D_\star=\operatorname{prox}_{R_\star}$ associated with the underlying regularizer $R_\star$. Under this mismatch, each denoising update becomes an inexact proximal step for the target objective. We further derive a stationarity bound that decays at a rate of $\mathcal{O}(1/K)$, with an additive term proportional to the average squared proximal mismatch. This result motivates adaptation via proximal matching rather than MSE-based adaptation alone. We study this approach with two established denoiser families: learned proximal networks and gradient-step denoisers. Experiments on Gaussian deblurring and super-resolution under substantial domain shift show that proximal matching adaptation improves reconstruction quality significantly over MSE-based adaptation, yielding the largest numerical gains in the few-shot regime.

### GPT总结
#### 文章内容
- 论文关注 PnP-PGD 在跨域部署时的收敛与性能退化问题，提出“proximal mismatch”来刻画已部署去噪器与目标域参考近端映射之间的偏差。
- 在理论上，将去噪更新视为对目标函数的非精确近端步，给出一条包含“平均平方 proximal mismatch”加性项的 O(1/K) 一阶平稳性上界。
- 在方法上，主张用“proximal matching”替代仅基于 MSE 的微调，使去噪器更贴合目标域的近端算子；在实践上于 Gaussian deblurring 与 super-resolution 的大幅域偏移下显著提升重建质量。
- 实验显示 proximal matching 尤其在 few-shot 场景带来最大增益，严重不匹配设置下 PSNR 提升可超过 10 dB。

#### 方法
- 将目标域先验建模为 R⋆，参考映射 D⋆ = prox_{R⋆}，目标函数 F⋆ = η f + R⋆；把部署去噪器 Ḋ 与 D⋆ 的差异定义为 proximal mismatch，并在 PnP-PGD 轨迹上的查询点度量该偏差。
- 证明使用 Ḋ 的每步去噪相当于对 F⋆ 的非精确近端更新，推导含加性 mismatch 项的 O(1/K) 一阶平稳性界，从而把域偏移与收敛质量直接联系起来。
- 提出基于 proximal matching 的自适应目标，使 Ḋ 的输出在目标域上与 D⋆ 对齐，优先匹配近端行为而非仅最小化去噪 MSE。
- 在两类结构化去噪器上实例化与验证：learned proximal networks 与 gradient-step denoisers，展示跨实现形式的一致适用性。
- 训练细节（如具体损失形式、超参数、数据构造）文中未明确说明；推理采用 PnP-PGD 框架进行重建。

#### 创新点
- 首次将 PnP 跨域问题系统表述为“proximal mismatch”，并把去噪器不匹配对目标优化的影响形式化为非精确近端步。
- 给出带“平均平方 proximal mismatch”加性项的一阶平稳性 O(1/K) 上界，把域偏移规模与收敛误差下界直接关联。
- 用 proximal matching 指导适配，超越传统基于 denoising MSE 的微调范式，并在两类结构化近端型去噪器上统一验证。
- 在大幅域偏移与 few-shot 设置中验证理论动机，实证显示 proximal 行为对齐优于仅提升去噪 MSE 的适配策略。

#### 实验结论
- 任务与设置：在 Gaussian deblurring 与 super-resolution 下进行大幅域偏移评测；few-shot 适配场景重点检验。
- 结果：proximal matching 相比 MSE-based adaptation 显著提升重建质量，在严重不匹配时 PSNR 提升可>10 dB，few-shot 场景收益最大。
- 数据集与实现细节文中未明确说明。

## 关键词：reinforcement learning

## MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators
- **论文链接**: http://arxiv.org/abs/2607.15273v1
- **作者**: Yushi Huang, Xiangxin Zhou, Jun Zhang, Liefeng Bo, Tianyu Pang
- **原始摘要**: MeanFlow generators achieve fast few-step sampling by predicting average velocities over time intervals, making them attractive for efficient generation. Reinforcement learning (RL) has become a powerful way to align diffusion and flow models with human preferences and task-specific objectives. In particular, DiffusionNFT offers an efficient forward-process RL framework that does not require reverse-process trajectories or likelihood estimation. However, applying such RL methods to MeanFlow remains underexplored. DiffusionNFT optimizes instantaneous velocities, whereas MeanFlow samples with average velocities. To bridge this gap, we introduce MeanFlowNFT. Inspired by the MeanFlow identity, which bridges average and instantaneous velocities, we construct an induced instantaneous-velocity predictor. We apply the DiffusionNFT objective to this predictor, making reward optimization well-defined for MeanFlow. Sampling remains based on the average velocity, preserving MeanFlow's fast few-step generation. We further prove that MeanFlowNFT inherits DiffusionNFT's strict policy-improvement guarantee. Experiments on image and video generation show that MeanFlowNFT consistently improves baselines. Moreover, it outperforms prior state-of-the-art RL-tuned few-step generators on most metrics ($6$ of $8$ on SD3.5-M), and can even surpass multi-step RL-tuned diffusion while using only a few sampling steps. For instance, on Wan 2.1, $4$-step MeanFlowNFT reaches a VBench score of $84.33$, surpassing $50$-step LongCat-Video RL ($82.57$).

### GPT总结
#### 文章内容
本文关注如何将高效的前向过程强化学习（RL）用于仅预测区间平均速度、以少步采样著称的 MeanFlow 生成器。核心思路是基于 MeanFlow identity 将平均速度网络诱导为一个“瞬时速度”预测器，并对该诱导预测器施加 DiffusionNFT 的前向过程目标，从而在不改动少步采样机制的前提下进行基于奖励的优化。结论表明，MeanFlowNFT 继承了 DiffusionNFT 的严格策略改进保证，在图像与视频任务上稳定提升 MeanFlow 基线，且在多数指标上超越既有少步 RL 方法，甚至以极少步数超过多步 RL 调优的扩散模型（如 Wan 2.1 上 4 步 VBench 84.33 > 50 步 LongCat-Video RL 的 82.57）。

#### 方法
- 通过 MeanFlow identity 将平均速度网络构造成一个诱导的瞬时速度预测器，用作 RL 优化的目标函数输入。
- 对该诱导预测器应用 DiffusionNFT 风格的前向过程 RL 目标：基于奖励将“正/负”样本对比并融入 flow-matching 式训练，训练全程无需反向轨迹与似然估计、保持 solver-agnostic。
- 对诱导预测中的全导数项采用有限差分近似，并在可训练预测器与参考预测器间共享沿前向条件速度计算的同一估计。
- 训练与采样解耦：训练仅作用于诱导的瞬时速度；推理仍使用 MeanFlow 的平均速度少步采样，保持快速 few-step 生成与推理开销不变。

#### 创新点
- 首个面向 MeanFlow（平均速度生成器）的前向过程 RL 框架，将 DiffusionNFT 成功迁移到少步平均速度范式。
- 通过 MeanFlow identity 构造“诱导瞬时速度”桥接量，使得在不直接作用于平均速度的情况下实现奖励优化。
- 给出理论保证：在理想化设定下，诱导预测器的最优解与 DiffusionNFT 的改进策略一致，且该策略改进可传递至平均速度生成器。
- 提出基于有限差分的全导数近似并在训练/参考预测器间共享估计，简化实现并与前向条件速度对齐。

#### 实验结论
- 任务覆盖文本到图像与文本到视频；在多个基准上相较 MeanFlow 基线与既有少步方法取得稳定提升，且在 SD3.5-M 上 8 项指标中的 6 项领先。
- 少步数即可超越多步 RL 扩散：如 Wan 2.1 上，4-step MeanFlowNFT 的 VBench 得分为 84.33，高于 50-step LongCat-Video RL 的 82.57；定性对比如 Wan2.1 1.3B、SD3.5-M 亦显示更佳视觉质量。
- 方法在保持少步高效采样的同时实现策略改进，测试阶段具备良好扩展性。
