# 2026-04-30 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## GramSR: Visual Feature Conditioning for Diffusion-Based Super-Resolution
- **论文链接**: http://arxiv.org/abs/2604.25457v1
- **作者**: Fabio D'Oronzio, Federico Putamorsi, Leonardo Zini, Marcella Cornia, Lorenzo Baraldi
- **原始摘要**: Despite recent advances, single-image super-resolution (SR) remains challenging, especially in real-world scenarios with complex degradations. Diffusion-based SR methods, particularly those built on Stable Diffusion, leverage strong generative priors but commonly rely on text conditioning derived from semantic captioning. Such textual descriptions provide only high-level semantics and lack the spatially aligned visual information required for faithful restoration, leading to a representation gap between abstract semantics and spatially aligned visual details. To address this limitation, we propose GramSR, a one-step diffusion-based SR framework that replaces text conditioning with dense visual features extracted from the low-resolution input using a pre-trained DINOv3 encoder. GramSR adopts a three-stage LoRA architecture, where pixel-level, semantic-level, and texture-level LoRA modules are trained sequentially. The pixel-level module focuses on degradation removal using $\ell_2$ loss, the semantic-level module enhances perceptual details via LPIPS and CSD losses, and the texture-level module enforces feature correlation consistency through a Gram matrix loss computed from DINOv3 features. At inference, independent guidance scales enable flexible control over degradation removal, semantic enhancement, and texture preservation. Extensive experiments on standard SR benchmarks demonstrate that GramSR consistently outperforms existing one-step diffusion-based methods, achieving superior structural fidelity and texture realism. The code for this work is available at: https://github.com/aimagelab/GramSR.

### GPT总结
#### 文章内容
论文针对基于扩散的单幅超分在真实退化下依赖文本条件（语义抽象且与空间细节不对齐）导致还原不忠实的问题，提出GramSR：以低分辨率图像的稠密视觉特征替代文本条件的一步扩散式超分框架。方法基于Stable Diffusion v2.1，顺序训练像素级、语义级与纹理级三类LoRA，分别用ℓ2、LPIPS+CSD以及基于DINOv3特征的Gram矩阵损失进行约束；推理阶段通过独立指导系数解耦控制去退化、细节增强与纹理保真。实验证明在DIV2K、RealSR、DRealSR上，GramSR在PSNR/SSIM与LPIPS/DISTS等指标上优于现有一步扩散方法，实现更好的结构忠实度与纹理真实感。

#### 方法
- 视觉条件替换：用预训练DINOv3从LR输入提取稠密特征，取代文本条件并注入扩散U-Net，实现与空间对齐的视觉引导。
- 三阶段LoRA架构：顺序训练
  1) 像素级LoRA（ℓ2，聚焦去退化），
  2) 语义级LoRA（LPIPS + CSD，增强感知细节；CSD具体定义文中未明确说明），
  3) 纹理级LoRA（基于DINOv3特征的Gram matrix对齐，保持特征相关性与纹理一致性）。
- 轻量适配：在去噪U-Net的卷积与MLP层插入rank=4的LoRA，小样本高效调优；底座为Stable Diffusion v2.1的一步扩散SR。
- 推理控制：为三类LoRA设置独立guidance scales，分别控制去退化强度、语义细节增强与纹理保真度。
- 训练与实现：×4 SR；训练集LSDIR + FFHQ前10k，退化采用Real-ESRGAN流程；随机512×512裁剪；Adam，batch=16，单NVIDIA L40S；像素/语义LoRA学习率5e−5，纹理LoRA学习率5e−6并以NIQE早停；视觉条件用DINOv3 ViT-B(768-dim)，Gram对齐用ViT-S+(384-dim)；损失权重λ1=λ3=1.0，λ2=2.0，λ4=500.0。

#### 创新点
- 用稠密视觉特征（DINOv3）替代文本条件，弥合抽象语义与空间细节之间的表示鸿沟，实现与LR输入空间对齐的条件引导。
- 将LoRA按功能解耦为像素/语义/纹理三级并顺序优化，分别配以匹配的目标函数；推理阶段通过独立guidance实现可控的感知-保真权衡。
- 在纹理级引入基于DINOv3特征的Gram matrix对齐，直接约束特征相关性以提升纹理一致性与真实感。
- 相较于文本条件、双LoRA的PiSA-SR，提出三阶段LoRA与视觉条件的组合，在一步扩散框架下同时提升结构忠实度与感知质量。

#### 实验结论
- 任务与数据：×4 SR；合成退化遵循Real-ESRGAN；评估集包括DIV2K(3,000样本)、RealSR、DRealSR；指标含PSNR/SSIM（Y通道）、LPIPS/DISTS（RGB）、FID与NIQE。
- 关键结果：在DIV2K上PSNR=24.79、SSIM=63.31、LPIPS=27.18均优于同类一步方法；在RealSR上PSNR=26.81、SSIM=76.68、LPIPS=23.05、DISTS=17.91最佳；在DRealSR上PSNR=29.69、SSIM=81.21、LPIPS=26.03、DISTS=19.12最佳，FID亦普遍改善（NIQE并非始终最优）。
- 作者结论：GramSR在真实复杂退化下实现更强的结构恢复与纹理真实感，较S3Diff、SinSR、OSEDiff、PiSA-SR、AdcSR等一步扩散方法取得一致领先，并提供可控的去退化/细节/纹理权衡能力。

## 关键词：reinforcement learning

## How Fast Should a Model Commit to Supervision? Training Reasoning Models on the Tsallis Loss Continuum
- **论文链接**: http://arxiv.org/abs/2604.25907v1
- **作者**: Chu-Cheng Lin, Eugene Ie
- **原始摘要**: Adapting reasoning models to new tasks during post-training with only output-level supervision stalls under reinforcement learning from verifiable rewards (RLVR) when the initial success probability $p_0$ is small. Using the Tsallis $q$-logarithm, we define a loss family $J_Q$ that interpolates between RLVR (at $q{=}0$, the exploitation pole) and the log-marginal-likelihood over latent trajectories (at $q{=}1$, the density-estimation pole). All members share the same per-example gradient direction, differing only by a scalar amplification $P_{θ^{-q}}$ that reweights each instance independently of the learning rate. This amplification is the mechanism that addresses cold-start stalling: under gradient flow, the exploitation pole requires $Ω(\frac{1}{p_0})$ time to escape cold start, while the density-estimation pole escapes in $Θ\big(\log(\frac{1}{p_0})\big)$; intermediate $q$ trades escape speed against noise memorization. Because $P_θ$ is intractable, we derive two Monte Carlo estimators from the two factorizations of the gradient: Gradient-Amplified RL (GARL) samples from the prior and amplifies the RL gradient, and Posterior-Attenuated Fine-Tuning (PAFT) importance-resamples from the posterior and runs standard SFT. Both have bias $O\big(\frac{q}{M P_θ^{q+1}}\big)$; GARL has lower variance, PAFT has semantically coherent gradients. On FinQA, HotPotQA, and MuSiQue, GARL at $q{=}0.75$ substantially mitigates cold-start stalling, escaping cold start where GRPO fails entirely. In warm start, GARL at low $q$ dominates FinQA where training is stable; on HotPotQA and MuSiQue, GARL destabilizes during training, and PAFT at $q{=}0.75$ provides stable gradients (best overall on HotPotQA at 47.9 maj@16, $+14.4$ over GRPO).

### GPT总结
#### 文章内容
- 论文关注“仅有输出级监督”的推理模型在冷启动阶段（初始成功率 p0 很小）下，RLVR 训练停滞的问题，以及与噪声记忆之间的对立。  
- 核心思路是利用 Tsallis q-logarithm 构造一个统一损失族 J_Q，在 q=0 退化为 RLVR（开发端），在 q=1 退化为对潜在轨迹的 log-marginal-likelihood（密度估计端），所有成员具有相同的样本梯度方向但以 Pθ^{-q} 做幅度放大，从而用“对监督的承诺度”q 自适应地重加权低成功概率样本。  
- 主要结论：在梯度流下，q=0 的冷启动逃逸时间为 Ω(1/p0)，而 q=1 为 Θ(log(1/p0))；中间 q 在逃逸速度与噪声记忆之间折中。实证上，GARL（q=0.75）能显著缓解 FinQA/HotPotQA/MuSiQue 的冷启动停滞并在 GRPO 失败处成功逃逸；在热启动下，GARL 在 FinQA 表现更优，而在 HotPotQA/MuSiQue 上 PAFT（q=0.75）更稳定并取得 HotPotQA 47.9 maj@16（较 GRPO +14.4）。

#### 方法
- 基于 Tsallis q-对数定义损失 ℓ_q = −log_q(Pθ) = (1−Pθ^{1−q})/(1−q)，形成 J_Q 连续体：q=0 对应 ℓ_0=1−Pθ（RLVR，界限、偏向模式求解），q=1 对应 ℓ_1=−log Pθ（对数边际似然，proper、偏向覆盖）。  
- 证明每个样本的梯度方向一致，仅以 Pθ^{-q} 放大：∇θℓ_q = Pθ^{-q}∇θℓ_0 = Pθ^{1−q}∇θℓ_1；q 即“承诺度”，对低 Pθ 样本更强牵引，从而加速冷启动逃逸。  
- 冷启动动力学分析（梯度流）：q=0 需 Ω(1/p0) 时间，q=1 需 Θ(log(1/p0))；低 q 借助有界损失与 escort tempering 更抗噪，高 q 易记忆噪声。  
- 提出两类 Monte Carlo 估计器以应对 Pθ 不可 tractable：GARL（从先验采样、放大 RL 梯度，方差更低）与 PAFT（从后验重要性重采样并执行标准 SFT，语义一致性更好）；二者偏差均为 O(q/(M·Pθ^{q+1}))。

#### 创新点
- 用 Tsallis q-logarithm 将 RLVR 与 log-marginal-likelihood 统一为单参数损失连续体 J_Q，以“承诺度”q 在开发与覆盖之间连续调节。  
- 揭示并形式化“按样本梯度放大”Pθ^{-q} 这一机制，直接针对冷启动逃逸瓶颈进行加速，是训练期的探索–开发权衡对应物。  
- 给出冷启动逃逸时间的定量保证（Ω(1/p0) vs Θ(log(1/p0))），并刻画解歧义（高 q）与抗噪（低 q）的系统性权衡。  
- 设计两种跨端点的可实现估计器（GARL/PAFT），并分析其偏差–方差与语义一致性取舍，连接经典 RL 与 SFT 估计方法。

#### 实验结论
- 数据集：FinQA、HotPotQA、MuSiQue。冷启动场景中，GARL 在 q=0.75 时显著缓解训练停滞，并在 GRPO 完全失败的情形下成功逃逸。  
- 热启动下：在 FinQA，低 q 的 GARL 于稳定训练条件下占优；在 HotPotQA 与 MuSiQue，GARL 易失稳，而 q=0.75 的 PAFT 更稳定，并在 HotPotQA 达到 47.9 maj@16（较 GRPO 提升 +14.4）。  
- 结果与理论一致：提高 q 可加速脱离冷启动但更易记忆噪声；中等 q（如 0.75）在多任务上取得更佳的速度–稳健折中。
