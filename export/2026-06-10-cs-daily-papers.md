# 2026-06-10 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution
- **论文链接**: http://arxiv.org/abs/2606.09608v1
- **作者**: Zhiqiang Wu, Yitong Dong, Xian Wei
- **原始摘要**: Diffusion-based generative models have achieved remarkable success in real-world image super-resolution (SR). With tiled diffusion techniques, these models can produce high-resolution images that exceed their native-supported resolution. However, the quality of such high-resolution (e.g $2048^2$) outputs often remains extremely poor, primarily due to two factors we consider: the image upsampling ratio (e.g $\times8$) exceeding the model's native-supported upsampling ratio (e.g $\times4$), and the model's native-supported resolution. In practice, training a native high-resolution model requires larger architectures, which incur significant computational overhead and GPU memory costs, making it hard on limited-resource equipment. Thus, we present TUDSR, a Twice Upsampling-Diffusion framework for higher SR. The TUDSR framework mainly consists of two stages: the first involves training at $R$-resolution, and the second introduces a looped chunk-based training strategy at $NR$-resolution. Each stage adapts a one-step GAN architecture comprising a generator and a discriminator. Based on SD2.1-base, we develop TUDSR-S, which achieves state-of-the-art performance across multiple benchmarks. Extensive experiments further demonstrate that TUDSR-S generates high-quality images at the resolutions of $1024^2$ and even $2048^2$, significantly outperforming existing approaches. Code is available at https://github.com/wuer5/TUDSR.

### GPT总结
#### 文章内容
这篇论文针对扩散式SR在高分辨率与大倍率（如×8）上采样时质量显著下降的问题，指出其根源在于模型原生支持的上采样倍率与分辨率受限。作者提出TUDSR（Twice Upsampling–Diffusion）框架，将大倍率上采样拆解为两阶段训练：先在R分辨率训练，再在NR分辨率采用循环分块训练，两个阶段均采用一步式GAN架构。基于SD2.1-base实现的TUDSR-S在多项基准上取得SOTA，并能在1024^2与2048^2分辨率生成高质量图像，显著优于现有方法。

#### 方法
- 两阶段流程：阶段一在R分辨率训练，阶段二在NR分辨率引入循环（looped）分块（chunk-based）训练，以适配更高分辨率与显存限制。
- 两次上采样策略：将整体大倍率上采样拆解为两次上采样，缓解模型原生倍率与分辨率上限带来的退化。
- 一步式GAN训练范式：每个阶段均由生成器与判别器组成的一步式架构进行训练，提高推理效率并减少迭代采样开销。
- 基于Stable Diffusion（SD2.1-base）构建SR模型，推理阶段支持不拼贴或拼贴（tiled diffusion）以适配不同输入尺寸。
- 具体实例TUDSR-S作为实现，代码开源（https://github.com/wuer5/TUDSR）。

#### 创新点
- 提出Twice Upsampling–Diffusion的两阶段上采样范式，系统性地化解“倍率过大”和“原生分辨率过低”两类瓶颈。
- 设计NR分辨率下的循环分块训练策略，在有限资源设备上实现原生高分辨率能力，降低显存与算力需求。
- 在扩散式SR背景下采用一步式GAN架构进行端到端训练，相较多步扩散推理更高效。
- 在不依赖超大基础生成模型的前提下，基于SD2.1-base实现至2048^2的高质量重建。

#### 实验结论
- 在RealSR与DrealSR等基准上对比RealESRGAN、OSEDiff、PiSA-SR、InvSR、SinSR，TUDSR-S在多项无参考IQA指标上领先：如RealSR上MANIQA达到0.6126；DrealSR上C-IQA 0.7186、C-IQA+ 0.6680、NIMA 4.7217、MUSIQ 60.7886、MANIQA 0.5325等均优于对比方法。
- 模型可在1024^2与2048^2分辨率生成高质量图像，整体效果显著优于现有扩散式SR与传统GAN式SR方法。
- 作者结论称TUDSR-S取得SOTA表现，并在多基准上稳定超过现有方法；部分实现细节（如损失函数、训练数据构成等）文中未明确说明。

## 关键词：reinforcement learning

## An Agency-Transferring Model-Free Policy Enhancement Technique
- **论文链接**: http://arxiv.org/abs/2606.09825v1
- **作者**: Anton Bolychev, Georgiy Malaniya, Sinan Ibrahim, Pavel Osinenko
- **原始摘要**: Training reinforcement learning (RL) policies from scratch is   costly: it requires careful reward and environment design,   extensive tuning, and substantial computation.   Yet many control problems already have a functional but   suboptimal policy available as a baseline.   This paper proposes a method for embedding such a baseline into   the RL training process, simultaneously improving training   efficiency relative to from-scratch methods and producing a   learning policy that outperforms the baseline.   At each step, the method arbitrates between the baseline policy   and a trainable learning policy, initially relying strongly on   the baseline policy and then progressively transferring agency to   the learning policy.   By the end of training, the learning policy is a standalone   neural network that operates without baseline policy support.   The paper formalizes what it means for the baseline policy to be   functional: under this policy, the agent reaches a goal set and   remains there with high probability.   The proposed arbitration mechanism is designed to exploit this   property during training, yielding high goal-reaching rates right   from the beginning of training.   A theoretical analysis provides a formal interpretation of this   behavior under stated assumptions and extends it to the final   baseline-free regime, where explicit lower bounds are derived for   the goal-reaching probability of the standalone learning policy.   Empirical results on continuous-control benchmarks show that the   proposed method achieves returns that match or exceed those of   competitive approaches, while maintaining the highest   goal-reaching rates throughout training among the compared   methods -- including in the final stage, where the learning policy   operates without any baseline support.

### GPT总结
#### 文章内容
该文针对“已有可用但次优策略”的控制任务，提出在训练中嵌入并逐步摆脱基线策略的无模型强化学习方法。核心思路是通过逐步转移行动决策权的策略仲裁机制，在训练早期大量采用基线策略以确保高到达目标率，随后将“代理权”移交给可训练的神经网络策略，最终得到可单独运行的策略。结论表明：在连续控制基准上，该方法在整个训练过程中（包括最终无基线阶段）保持最高的目标到达率，同时回报达到或超过竞争方法，并给出最终策略目标到达概率的理论下界。

#### 方法
- 策略仲裁/切换：每个时间步在基线策略与可训练策略之间仲裁，初期强依赖基线，随后按计划逐步提升学习策略的采样概率（代理权转移）。
- 功能性基线假设：形式化“功能性”定义——基线策略以高概率到达并停留在目标集合；仲裁机制专门利用该性质以在训练初期即获得高成功率。
- 训练目标与过程：在仲裁产生的数据上对学习策略进行无模型RL训练（与SAC/PPO/TD3等从零训练对比），同时调整仲裁权重直至学习策略独立运行。
- 最终部署：训练结束后丢弃基线，使用独立的神经网络策略进行推理与控制。
- 理论分析：在给定假设下解释训练期高目标到达率的来源，并对最终无基线策略的目标到达概率给出显式下界。

#### 创新点
- 提出“代理权转移”的策略仲裁框架，相较 residual RL 等仅做残差叠加的方法，直接在决策层面控制从基线到学习策略的平滑接管。
- 形式化“功能性基线”的到达-停留（reach-and-stay）定义，并据此设计仲裁机制以在训练早期确保高成功率。
- 给出最终无基线阶段的目标到达概率显式下界，为基于基线增强的模型无关RL提供可解释的性能保证。
- 在训练动态与收敛阶段统一分析仲裁对成功率的影响，连接“带基线训练高成功率”与“无基线部署可靠性”。

#### 实验结论
- 任务与数据：在连续控制基准环境上评测，具体环境名称与规模文中未明确说明。
- 结果：相较 SAC、PPO、TD3 与 residual RL 等竞争方法，该方法在训练全过程保持最高的目标到达率；最终无基线阶段仍维持领先的成功率。
- 结论：在效率与性能上，回报与最优对手相当或更优，同时提供更稳定的目标达成过程；理论结果与实证结果一致支撑方法有效性。文中未明确说明具体数值提升幅度与显著性检验细节。
