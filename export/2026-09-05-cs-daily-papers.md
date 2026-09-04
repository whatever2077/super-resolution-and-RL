# 2026-09-05 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## SPARK: Input-Conditioned Sparse Activation Modulation for Frozen DiT-based Super-Resolution
- **论文链接**: http://arxiv.org/abs/2609.03813v1
- **作者**: Federico Putamorsi, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- **原始摘要**: Real-world image super-resolution (SR) increasingly relies on Diffusion Transformer (DiT) backbones, whose internal activations can be dominated by a small number of massive channels. Yet improving perceptual quality in these models still typically requires fine-tuning the network or attaching additional adapters, leaving this structured activation space largely unexplored for adaptation. We investigate whether dominant channels can instead serve as a compact adaptation interface for frozen DiT-based SR models. We first characterize their behavior in pretrained SR backbones and show through controlled interventions that they strongly affect reconstruction quality. Building on this observation, we introduce SPARK, a lightweight input-conditioned controller that predicts bounded per-channel affine transformations for only the selected channels, while keeping the SR backbone and VAE frozen. Dominant channels are identified through an online activation-ranking procedure, and only a small predictor conditioned on the low-resolution VAE latent is optimized. Experiments on three DiT-based SR backbones across DIV2K, RealSR, and DRealSR show consistent gains in both fidelity and perceptual quality while modulating only eight channels per stream and block. Controlled comparisons further show that these gains cannot be explained by parameter budget or access to the selected channels alone.

### GPT总结
#### 文章内容
该论文关注DiT-based超分模型中感知质量难以可控的问题，提出不改动主体网络而仅在“主导通道”上进行稀疏调制的适配策略。核心思路是在线识别激活中幅值占优的少数通道，并用输入（低分辨率VAE潜变量）条件的小型预测器为这些通道生成有界的逐通道仿射变换，同时冻结SR主干与VAE。实验显示仅调制每个块每个流的8个通道即可在DIV2K、RealSR、DRealSR上稳定提升失真与感知指标，且在无参考指标上达到或超过现有方法。

#### 方法
- 在线通道选择：在各块内通过对通道重要性的指数滑动平均进行排名，子集稳定即停止，避免全数据遍历。
- 稀疏通道调制：仅对选中的“主导通道”施加逐通道仿射变换，并对变换参数做边界约束。
- 输入条件控制：用低分辨率图像的VAE潜变量作为条件，训练一个小型预测器输出仿射参数；SR主干与VAE均冻结。
- 轻量适配规模：在每个流与每个块仅调制8个通道，参数量极小。
- 训练/损失细节：除在DIV2K上进行训练的设定外，具体优化目标与损失函数文中未明确说明。

#### 创新点
- 将Transformer中“massive activations”引入SR适配界面，把少数主导通道作为可控的紧凑干预点。
- 提出输入条件的稀疏通道级仿射调制，在不微调主干或加挂大型adapter的前提下实现感知质量控制。
- 在线激活排名与早停机制，高效确定通道子集，避免昂贵的离线统计。
- 在DiT-based SR上验证“仅少量通道即足以提升”的结构性规律，强调与参数规模无关的有效性。

#### 实验结论
- 任务与数据集：在三个DiT-based SR主干（TSD-SR、DiT4SR、TEASR）上进行适配；训练于DIV2K，评估于DIV2K、RealSR、DRealSR。
- 关键结果：在RealSR上，TSD-SR+SPARK达到75.35 CLIP-IQA与4.69 LIQE；在DRealSR上达到76.32 CLIP-IQA与4.47 LIQE，均优于对比方法的无参考感知指标；同时各主干的SSIM、LPIPS、MANIQA、MUSIQ、TOPIQ等指标也有一致改善。
- 作者结论：仅调制每块每流8个通道即可显著提升失真与感知质量，且改进并非由参数预算或通道访问策略本身解释，表明主导通道是有效的适配与控制界面。

## 关键词：reinforcement learning

## Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR
- **论文链接**: http://arxiv.org/abs/2609.04108v1
- **作者**: Boyan Li, Bingsen Chen, Chenghao Yang, Ping Nie, Chen Zhao, Xi Ye
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a \emph{teacher-modulated rescaling} of the RL advantage. In this paper, we show that a simple two-stage scheme, OPD-then-RL, consistently outperforms pure OPD, pure RLVR, and all such joint baselines across logic and math reasoning benchmarks. Beyond the empirical results, we further provide a systematic understanding of this through pass@$k$ behavior, learning dynamics, and parameter updates, yielding a consistent explanation: OPD expands the student's coverage of teacher-supported solutions and RL sharpens within that support, while jointly optimizing the two signals causes them to interfere.To provide a practical recipe, we find that the OPD validation score is the key signal for when to switch to RL, and that OPD is a better cold start for RL than SFT. Together, our results establish OPD-then-RL as a simple yet strong way to combine the two methods, turning two entangled signals into complementary stages.

### GPT总结

当前论文的 GPT 总结生成失败：`Encountered text corresponding to disallowed special token '<|endoftext|>'. If you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|endoftext|>', ...}`. If you want this text to be encoded as normal text, disable the check for this token by pas...`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
