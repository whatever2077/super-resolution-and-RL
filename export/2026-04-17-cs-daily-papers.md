# 2026-04-17 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Remote Sensing Image Super-Resolution for Imbalanced Textures: A Texture-Aware Diffusion Framework
- **论文链接**: http://arxiv.org/abs/2604.13994v1
- **作者**: Enzhuo Zhang, Sijie Zhao, Dilxat Muhtar, Zhenshi Li, Xueliang Zhang, Pengfeng Xiao
- **原始摘要**: Generative diffusion priors have recently achieved state-of-the-art performance in natural image super-resolution, demonstrating a powerful capability to synthesize photorealistic details. However, their direct application to remote sensing image super-resolution (RSISR) reveals significant shortcomings. Unlike natural images, remote sensing images exhibit a unique texture distribution where ground objects are globally stochastic yet locally clustered, leading to highly imbalanced textures. This imbalance severely hinders the model's spatial perception. To address this, we propose TexADiff, a novel framework that begins by estimating a Relative Texture Density Map (RTDM) to represent the texture distribution. TexADiff then leverages this RTDM in three synergistic ways: as an explicit spatial conditioning to guide the diffusion process, as a loss modulation term to prioritize texture-rich regions, and as a dynamic adapter for the sampling schedule. These modifications are designed to endow the model with explicit texture-aware capabilities. Experiments demonstrate that TexADiff achieves superior or competitive quantitative metrics. Furthermore, qualitative results show that our model generates faithful high-frequency details while effectively suppressing texture hallucinations. This improved reconstruction quality also results in significant gains in downstream task performance. The source code of our method can be found at https://github.com/ZezFuture/TexAdiff.

### GPT总结
#### 文章内容
本文关注遥感图像中“全局随机、局部成簇”的纹理失衡导致扩散式SR模型空间感知受限、易产生纹理幻觉的问题。核心思路是构建并利用Relative Texture Density Map (RTDM) 显式刻画目标HR的纹理分布，并将其用于扩散过程的空间条件、损失加权与采样调度自适应三方面的联合约束。实验显示，TexADiff在定量指标上优于或可比现有方法，定性上能生成真实的高频细节并抑制纹理幻觉，同时提升下游任务表现。

#### 方法
- RTDM估计（训练期）：先用PSNR-oriented SR得到初步重建IPSR，计算SSIM-based对比一致性MCCT与Spatial LPIPS的MSL，构造M = (1 − MSL) · MCCT；对M进行阈值二值化（τ ∈ [0.35, 0.4]）、形态学后处理并以8× max-pooling下采样至潜空间，得到二值RTDM ˆMb。
- RTDM预测（推理期）：构建RTDM预测网络，输入为LR与PSR的双分支编码，门控融合后经U-Net式解码器输出连续M，以L1监督学习；推理时同样二值化得到RTDM。
- 多条件融合：设计轻量MiniControlNet，将LR/PSR特征与RTDM等多条件输入有效接入扩散U-Net，采用SFT（Spatial Feature Transformations）、CN（Cross Normalization）与时间感知残块（TRB）等模块进行条件注入与时序建模。
- 纹理感知扩散：将RTDM用于三处——(1) 显式空间条件，引导去噪；(2) 纹理区优先的损失调制，强化高频重建；(3) 纹理感知采样，对采样日程进行动态自适应以匹配局部纹理密度。
- 训练/损失：采用标准扩散噪声回归损失并叠加基于RTDM的损失权重；更细节（如具体权重系数、优化器等）文中未明确说明。

#### 创新点
- 提出RTDM以相对纹理密度建模遥感图像的纹理失衡，并首次在扩散SR中同时用于空间条件、损失加权与采样调度三重耦合引导。
- 设计稳健的RTDM构建：将SSIM-based对比一致性与Spatial LPIPS结合，并通过二值化与形态学处理将连续引导稳定化。
- 提出轻量MiniControlNet与纹理感知去噪架构（含SFT、CN、TRB），面向多条件融合与时序一致性，适配遥感场景的局部成簇纹理。
- 提出纹理感知采样策略（dynamic adapter for the sampling schedule），以RTDM动态调整采样路径，缓解纹理幻觉与过度锐化。

#### 实验结论
- 任务：RSISR；对比方法包含FaithDiff、ResShiftL、PASD等，TexADiff在定量指标上优于或可比SOTA，定性上在纹理丰富区域生成更忠实细节、在纹理稀疏区域避免条纹伪影。使用的数据集与放大倍数文中未明确说明。
- 下游效果：改进的重建质量带来下游任务的显著收益，具体任务名称与数值增益文中未明确说明。
- 开源：代码开源于https://github.com/ZezFuture/TexAdiff。

## 关键词：reinforcement learning

## From $P(y|x)$ to $P(y)$: Investigating Reinforcement Learning in Pre-train Space
- **论文链接**: http://arxiv.org/abs/2604.14142v1
- **作者**: Yuqiao Tan, Minzheng Wang, Bo Liu, Zichen Liu, Tian Liang, Shizhu He, Jun Zhao, Kang Liu
- **原始摘要**: While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization. Extensive experiments demonstrate that DSRL consistently outperforms strong baselines, proving that pre-train space pruning effectively steers the policy toward a refined correct reasoning subspace.

### GPT总结
#### 文章内容
该文指出当前以可验证奖励为核心的后训练RL（优化P(y|x)）受基座模型输出分布上限的约束，提出在“预训练空间”直接优化边缘分布P(y)的PreRL以突破该瓶颈。作者理论与实证证明log P(y)与log P(y|x)的梯度强对齐，使PreRL可作为标准RL的有效替代，同时发现“负样本强化（NSR）”在预训练空间中可高效剪枝错误推理并激发内生反思。基于此，提出先用NSR-PreRL扩展推理地平线、再切换到标准RL细化策略的Dual Space RL（DSRL）。实验显示DSRL稳定优于强基线，具备更高准确率、样本效率与Pass@K。

#### 方法
- PreRL：在预训练空间以奖励驱动的在线更新直接优化P(y)，在更新中去除问题条件x，保留更广的探索能力。
- 梯度对齐：从理论与实证上验证∇θ log P(y)与∇θ log P(y|x)强对齐，用P(y)优化作为P(y|x)优化的代理目标。
- 样本作用机理解析：将预训练空间的强化分为PSR与NSR，发现PSR会把质量集中到自生成的正确样本上而伤害性能；NSR则快速剪枝错误轨迹。
- NSR-PreRL效应：通过对负样本的强化削弱错误推理子空间，同时诱发内生推理行为，使transition与reflection想法分别提升14.89×与6.54×。
- DSRL（Policy Reincarnation）：先用NSR-PreRL在P(y)上扩展与净化推理子空间，再切换到标准后训练RL（优化P(y|x)）进行细粒度轨迹优化。

#### 创新点
- 将RL优化目标从条件分布P(y|x)转向边缘分布P(y)，并给出梯度强对齐的理论与实证依据，确立PreRL作为标准RL的可行替代。
- 揭示预训练空间中正/负样本强化的非对称性：首次系统性指出PSR有害而NSR格外有效，并量化其对“思维转移与反思”行为的促进。
- 提出Dual Space RL（DSRL）的策略重生范式：先在预训练空间进行NSR剪枝与能力内化，再在后训练空间做条件策略的精修。
- 通过“预训练空间剪枝→后训练空间细化”的两阶段设计，兼顾广域探索与目标对齐，缓解传统RL陷入局部最优的问题。

#### 实验结论
- DSRL在总体准确率、样本效率与Pass@K上稳定优于强基线（文中示例包括GRPO），训练过程中保持更好的探索与响应长度增长。具体任务与数据集：文中未明确说明。
- 仅用NSR-PreRL即可在更少训练步内取得可比准确率，并显著提升内生推理：transition与reflection想法分别提升14.89×与6.54×。
- 作者结论：预训练空间的错误轨迹剪枝能将策略引向精炼的正确推理子空间，且与后训练RL结合的DSRL优于单一空间的RL方案。具体数值提升细节与完整评测设置：文中未明确说明。
