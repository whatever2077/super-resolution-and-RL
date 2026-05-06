# 2026-05-07 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## FluxFlow: Conservative Flow-Matching for Astronomical Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2605.03749v1
- **作者**: Shuhong Liu, Xining Ge, Ziteng Cui, Liuzhuozheng Li, Gengjia Chang, Jun Liu, Ziying Gu, Dong Li, Xuangeng Chu, Lin Gu, Tatsuya Harada
- **原始摘要**: Ground-to-space astronomical super-resolution requires recovering space-quality images from ground-based observations that are simultaneously limited by pixel sampling resolution and atmospheric seeing, which imposes a stochastic, spatially varying PSF that cannot be resolved through upsampling alone. Existing methods rely on synthetic training pairs that fail to capture real atmospheric statistics and are prone to either over-smoothed reconstructions or hallucination sources with no physical counterpart in the observed sky. We propose FluxFlow, a conservative pixel-space flow-matching framework that incorporates observation uncertainty and source-region importance weights during training, and a training-free Wiener-regularized test-time correction to suppress hallucination sources while preserving recovered detail. We further construct the DESI--HST Dataset, the large-scale real-world benchmark comprising 19,500 real co-registered ground-to-space image pairs with real atmospheric PSF variation. Experiments demonstrate that FluxFlow consistently outperforms existing baseline methods in both photometric and scientific accuracy.

### GPT总结
#### 文章内容
论文面向“ground-to-space”天文图像超分辨问题，针对地基观测同时受像素采样与大气视宁度（随机且空间变化的PSF）限制，传统上采样放大无法恢复真实物理细节且易产生过度平滑或虚假源。作者提出FluxFlow：一种保守的像素域flow-matching框架，在训练中显式纳入观测不确定性与源区重要性权重，在推理阶段引入无需再训练的Wiener正则化一致性校正以抑制幻觉源同时保留细节。并构建包含19,500对真实配准图像的DESI–HST Dataset，覆盖真实大气PSF变化与不确定性。实验显示FluxFlow在光度一致性与科学准确性上均优于现有回归与生成基线。

#### 方法
- 模型：像素空间的conservative flow-matching（文中亦称OT-CFM），以UNet为骨干网络学习速度场。
- 训练目标：速度损失按每像素逆方差（观测不确定性）与源区域重要性图加权，聚焦科学相关区域并抑制伪影带来的不稳定梯度。
- 推理机制：Measurement-consistent sampling，先对重建结果做PSF卷积与下采样形成前向投影，与观测残差经Wiener去卷积后回投并以系数η0校正，训练外实现物理一致性与幻觉源抑制。
- 具体设定：20步Euler采样并配MC-FS校正；前向投影采用Gaussian PSF与面积下采样；Wiener参数λSNR=50，残差校正η0=0.5。
- 数据与实现：在DESI–HST真实配对数据上训练；优化器AdamW、EMA与标准学习率调度（其余超参如lr与epoch已给出）。

#### 创新点
- 将观测不确定性与源区域重要性显式纳入flow-matching损失，加权学习科学相关结构，缓解真实观测中噪声与伪影的负面影响。
- 提出训练外的Wiener正则化一致性回投，作为通用推理期校正，显著抑制生成式方法常见的紧致幻觉源，同时保持细节。
- 构建大规模真实配对基准DESI–HST Dataset（19,500对，×2/×4），包含真实大气PSF变化与逐像素不确定性权重，为跨仪器SR提供可靠评测。
- 面向天文SR的“保守”生成策略，将物理一致性与科学可用性置于感知锐利度之上，兼顾细节恢复与测量稳健性。

#### 实验结论
- 任务与数据：在DESI–HST Dataset上进行ground-to-space超分辨（×2与×4），评测指标含PSNR、SSIM与基于SExtractor源椭圆掩膜的Flux-L1（源区绝对通量偏差）。
- 对比方法：与Bicubic、SwinIR、HAT、FISR等回归法，以及cGAN、GD-Net、AS-Bridge等生成法比较，FluxFlow在光度保真与科学准确性两类指标上均取得一致领先。
- 结论与补充：方法有效抑制幻觉源并提升细节恢复；附录报告在AstroSR与STAR上的补充实验。作者同时指出局限：幻觉并未完全消除，后续将探索多波段联合重建与不确定性校准采样以进一步提升SNR。

## 关键词：reinforcement learning

## Sequential vs. Simultaneous Entanglement Swapping under Optimal Link-Layer Control
- **论文链接**: http://arxiv.org/abs/2605.04047v1
- **作者**: Priyam Srivastava, Akshat R. Sabavat, Siddharth Jain, Alan Scheller-Wolf, Sridhar Tayur, David Tipper, Prashant Krishnamurthy, Amy Babay, Kaushik P. Seshadreesan
- **原始摘要**: Connection-less, packet-switched quantum network architectures distribute entanglement across multi-hop paths through sequential entanglement swapping, in which each node acts on purely local state information. The architectural advantages over the connection-oriented alternative -- simultaneous SWAP-ASAP -- are compelling, but sequential swapping holds partial chains in intermediate buffers between successive swaps, exposing them to memory decoherence in a way simultaneous SWAP-ASAP avoids by design. We present a proof-of-principle study at fixed chain length $n = 4$ in which each elementary link is governed by a fixed reinforcement-learning policy optimizing the secret-key rate of the six-state protocol, leaving the network-layer protocol as the sole independent variable. Sweeping the network-layer memory coherence time $T_c^{\mathrm{ext}}$ over four orders of magnitude reveals a clear regime structure governed by the dimensionless ratio $T_c^{\mathrm{ext}}/τ$, where $τ$ is the per-link entanglement heralding latency. Simultaneous SWAP-ASAP delivers a constant rate across the full sweep. Sequential swapping, by contrast, collapses to zero end-to-end deliveries below $T_c^{\mathrm{ext}}/τ= 25$, and begins recovering at $T_c^{\mathrm{ext}}/τ= 50$. It remains limited by the simultaneous rate, which it saturates only at the relaxed end of the sweep. These results suggest that the connection-less penalty is a near-term phenomenon tied to present-day memory coherence rather than a fundamental property of sequential swapping.

### GPT总结
#### 文章内容
- 论文比较两类量子网络层协议的可行性：连接导向的 simultaneous SWAP-ASAP（wait-and-swap）与连接无关的 sequential swapping（swap-and-wait），在存在量子存储退相干时的表现差异。
- 核心思路是将链路层固定为经强化学习优化（最大化 six-state QKD 秘钥率）的策略，仅改变网络层时序协议，并在两层解耦的内/外存储模型中，通过扫网络层外部存储相干时间 T_c^{ext} 与链路叠加延迟 τ 的比值 T_c^{ext}/τ 来绘制性能区间。
- 主要结论：SWAP-ASAP 在全范围内保持恒定速率；Sequential 在 T_c^{ext}/τ < 25 时几乎无端到端交付，至 T_c^{ext}/τ ≈ 50 开始恢复，且仅在相干时间充裕端逼近并最终饱和于 SWAP-ASAP 的速率；连接无关的性能劣势更像近端器件（存储相干）受限而非方法的根本缺陷。

#### 方法
- 两层体系：链路层由固定的强化学习策略控制基本链（WN2M2：两个节点、各两存储，成功后生成 Werner 态）；网络层为待比较的两种时序协议（sequential 与 SWAP-ASAP）。
- 存储层级与接口：内部通信存储（相干时间 T_c^{int}）用于生成/蒸馏/临时存放；外部存储（相干时间 T_c^{ext}）作为链路缓冲队列（容量 B=20）向网络层“交付”对。Sequential 额外维护 n−1 个链缓冲。
- 网络层操作：对外部缓冲中条目执行 n−1 次 BSM 以组装端到端纠缠；sequential 在相邻就绪即交换并暂存部分链；SWAP-ASAP 先全链就绪后并行交换。
- 强化学习策略目标：最大化 six-state 协议的秘钥率，链路层动作包括 generate/distill/discard/deliver（CONSUME）。具体算法/训练细节文中未明确说明。
- 评估设置：固定链长 n=4；扫 T_c^{ext} 跨四个数量级，用无量纲比 T_c^{ext}/τ 刻画区间；性能指标为端到端速率/秘钥率，精确定义公式文中未明确说明。

#### 创新点
- 将链路层用单链路最优的强化学习策略冻结，只让网络层协议成为唯一自变量，干净隔离比较 sequential 与 SWAP-ASAP 的系统效应。
- 引入内/外部量子存储的层级与缓冲接口建模，明确将“等待”成本外显为 T_c^{ext} 的退相干暴露，形成可控的协议比较平台。
- 用维度比 T_c^{ext}/τ 划分硬件—协议工作区间，给出清晰阈值行为（≈25/≈50）并将连接无关惩罚归因于当前存储相干的近端限制。
- 以 six-state QKD 秘钥率为链路层 RL 优化目标，将网络层时序比较与应用相关效用直接对齐。

#### 实验结论
- 任务与设置：在模拟 n=4 的多跳链路上，对比 sequential 与 SWAP-ASAP，在固定链路层 RL 策略下，扫 T_c^{ext}（相对 τ）评估端到端纠缠/秘钥率。
- 核心结果：SWAP-ASAP 速率对 T_c^{ext}/τ 不敏感、近似常数；Sequential 在 T_c^{ext}/τ < 25 时端到端交付坍塌为零，于 ≈50 开始恢复，并仅在更高 T_c^{ext}/τ 时逼近并饱和于 SWAP-ASAP。
- 作者结论：连接无关（packet-switched、sequential）方案的性能劣势主要是现阶段量子存储相干时间受限所致，而非 sequential 机制的根本缺陷，随着存储相干改进可进入可行区间。
