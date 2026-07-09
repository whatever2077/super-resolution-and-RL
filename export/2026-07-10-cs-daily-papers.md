# 2026-07-10 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Allo{SR}$^2$: Rectifying One-Step Super-Resolution to Stay Real via Allomorphic Generative Flows
- **论文链接**: http://arxiv.org/abs/2604.19238v2
- **作者**: Zihan Wang, Xudong Huang, Junbo Qiao, Wei Li, Jie Hu, Xinghao Chen, Shaohui Lin
- **原始摘要**: Real-world image super-resolution (Real-SR) has been revolutionized by leveraging the powerful generative priors from Diffusion Models (DMs) and Flow Matching (FM). However, existing one-step methods typically replace Gaussian noise with degraded low-resolution (LR) latents at initialization, introducing a substantial distribution shift that further leads to trajectory deviation and prior collapse under extreme acceleration. To overcome these limitations, we propose Allo{SR}$^2$, a novel FM-based framework that rectifies one-step SR flows via allomorphic generative flows to maintain high-fidelity generative realism. Specifically, we utilize SNR-Guided Trajectory Initialization to identify a statistically aligned intermediate state along the pre-trained path to integrate LR representations into the generative flow. To ensure a stable, low-curvature path for one-step inference, we propose Flow-Anchored Trajectory Consistency (FATC), which explicitly regularizes the velocity field of the underlying probability flow. Furthermore, we develop Allomorphic Trajectory Matching (ATM), a self-adversarial distillation strategy that jointly models the SR flow and the generative flow within a unified velocity field, enabling one-step Real-SR while preserving the generative prior. Extensive experiments on both synthetic and real-world benchmarks demonstrate that Allo{SR}$^2$ achieves state-of-the-art performance in one-step Real-SR, offering a superior balance between fidelity and realism while maintaining extreme efficiency.

### GPT总结
#### 文章内容
该论文聚焦于Real-SR中一步推理的分布偏移与先验坍塌问题，指出直接用LR潜变量替换高斯噪声会导致生成轨迹偏离、破坏预训练DM/FM的生成先验。核心思路是通过FM框架下的“异形（allomorphic）”联合流，将生成流作为动态锚点，与SR流共享速度场并在统计上对齐注入点，从而在一步推理中保持低曲率、稳定轨迹与真实感。结论表明，Allo{SR}$^2$在合成与真实数据基准上实现一步Real-SR的SOTA，兼顾保真与真实感并显著提升效率。

#### 方法
- 构建FM-based的双路径框架：全局生成流（从噪声到HR）与局部SR流（从LR到HR）在统一的velocity field中建模、共享权重，并通过跨轨迹的score/velocity一致性约束实现互相校正。
- SNR-Guided Trajectory Initialization：基于SNR分析选择预训练生成轨迹上的统计对齐中间态，将LR表示在该时刻注入以缓解与高斯先验的分布偏移。
- Flow-Anchored Trajectory Consistency (FATC)：显式正则化概率流的速度场，降低轨迹曲率并保证一步推理的稳定性与可控性。
- Allomorphic Trajectory Matching (ATM)：自对抗式蒸馏策略，在统一速度场中联合拟合生成流与SR流，传递并保留生成先验，避免先验坍塌。
- 一步推理：在上述轨迹整形与先验对齐之后，以单次函数评估完成Real-SR推理，提升极端效率。

#### 创新点
- 提出“异形流”视角：将图像生成与恢复视为同向收敛至HR真实图像流形的结构同形轨迹，用生成流作动态锚点而非静态骨干，持续矫正SR流。
- SNR引导的注入点选择：从统计匹配角度确定LR潜变量的最佳注入时刻，替代以往直接用LR替换高斯噪声的做法，显著缓解分布偏移与轨迹偏离。
- FATC的速度场正则化：围绕概率流的velocity field设计一致性约束，显式控制轨迹曲率以实现极端加速下的一步稳定推理。
- ATM自对抗蒸馏：在统一速度场中联合建模生成与SR轨迹，保留并迁移生成先验，避免DM/FM在一步加速下的先验坍塌。

#### 实验结论
- 在合成与真实世界基准上验证，Allo{SR}$^2$实现一步Real-SR的SOTA表现，并在严重退化区域相较OSEDiff与TSD-SR更好地恢复真实纹理。具体数据集与评价指标的名称与数值文中未明确说明。
- 方法在保真与真实感之间取得更优平衡，同时保持“极端效率”的一步推理。具体速度指标与资源开销文中未明确说明。
- 作者结论：通过轨迹初始化、速度场一致性与自对抗蒸馏的组合，能在一步推理中维持生成先验与真实感，避免过平滑与伪影。

## 关键词：reinforcement learning

## Weak-to-Strong Generalization via Direct On-Policy Distillation
- **论文链接**: http://arxiv.org/abs/2607.05394v2
- **作者**: Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL weak teacher is not enough, because the teacher's final policy mixes useful RL gains with the limitations of the smaller model. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher's RL-induced policy shift instead. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward for the student. In plain terms, the checkpoint pair tells us which actions RL made the weak model more or less likely to take, and Direct-OPD applies that signal on the stronger student's own on-policy states. This directly reuses the weak model's RL supervision signal without running sparse-reward RL on the target model. Empirically, Direct-OPD consistently leverages weaker teachers to improve stronger target models; notably, it boosts Qwen3-1.7B from 48.3% to 58.3% on AIME 2024 in just 4 hours on 8 A100 GPUs. It outperforms step-matched direct RL and enables the sequential composition of multiple policy shifts. Our results show that RL outcomes can be reused across model scales as implicit reward signals, not merely as final models to imitate.

### GPT总结
#### 文章内容
- 论文关注RLVR在大模型上训练代价高的问题，提出弱到强的Direct On-Policy Distillation（Direct-OPD）：先在小模型上做RL，再把RL带来的“策略位移”迁移到强学生模型上。
- 核心思路是用弱教师RL前后两检查点的log概率差作为隐式密集奖励，在学生自身的on-policy状态上进行蒸馏，并用KL约束锚定到学生初始策略，避免在大模型上重复稀疏奖励RL。
- 主要结论：Direct-OPD能稳定用更弱教师提升更强学生，在AIME 2024上将Qwen3-1.7B从48.3%提升到58.3%，仅需8×A100约4小时；优于步数匹配的直接RL，并可顺序组合多个策略位移。

#### 方法
- 构造教师对(πTref, πT)：分别为弱模型RL前的参考与RL后的教师；定义策略位移ΔT(y|x)=log πT(y|x)−log πTref(y|x)，刻画RL让哪些动作更/不更可能。
- 学生采用on-policy采样生成轨迹，将ΔT在这些学生轨迹上作为逐token的隐式奖励信号进行训练。
- 目标函数包含对学生初始策略πS的KL正则锚定，防止偏离初始能力并稳定训练。
- 利用理论等价性：在KL正则化RL下，教师的log比值与训练所用的奖励等价，从而无需训练显式奖励模型或在学生上运行稀疏奖励RL。
- 支持顺序组合多个弱教师的策略位移，实现累积迁移；不依赖教师与学生top-k输出高度重叠，可跨“思维模式”迁移。

#### 创新点
- 从“模仿教师最终策略”转为“迁移教师RL诱导的策略位移”，隔离出RL增益而不继承小模型能力上限的偏差。
- 将小模型RL的结果表征为可跨模型规模复用的隐式奖励信号，而非只能当作最终策略去模仿。
- 给出与KL正则化RL目标的等价性证明，使对比检查点的log比值成为可直接优化的监督信号。
- 提供弱到强的高效后训练范式，可顺序组合多次策略位移，且在学生已强于教师时依然带来增益，避免vanilla OPD的“拉低”效应。

#### 实验结论
- 任务/数据：以AIME 2024等可验证推理任务为主；教师对包括R1-Distill-1.5B → JustRL-1.5B与Nemotron-1.5B → QuestA-Nemotron-1.5B；学生包括R1-Distill-7B、Qwen3-1.7B、Qwen3-4B。
- 关键结果：Direct-OPD在AIME 2024上将Qwen3-1.7B从48.3%提至58.3%，训练仅需约4小时（8×A100）；当学生初始精度已高于教师（如R1-Distill-7B 56.7 vs JustRL-1.5B 51.3）时，vanilla OPD会下降到≈50，而Direct-OPD带来提升。
- 结论与对比：在步数匹配下，“小模型上RL + Direct-OPD到大模型”在准确率与计算成本上均优于直接在大模型上做RL；方法还能顺序叠加多次策略位移，显示良好的可组合性与性价比。文中未明确说明更广泛基准的完整数值细节。
