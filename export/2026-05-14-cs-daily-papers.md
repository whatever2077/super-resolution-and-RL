# 2026-05-14 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Fast Image Super-Resolution via Consistency Rectified Flow
- **论文链接**: http://arxiv.org/abs/2605.12377v1
- **作者**: Jiaqi Xu, Wenbo Li, Haoze Sun, Fan Li, Zhixin Wang, Long Peng, Jingjing Ren, Haoran Yang, Xiaowei Hu, Renjing Pei, Pheng-Ann Heng
- **原始摘要**: Diffusion models (DMs) have demonstrated remarkable success in real-world image super-resolution (SR), yet their reliance on time-consuming multi-step sampling largely hinders their practical applications. While recent efforts have introduced few- or single-step solutions, existing methods either inefficiently model the process from noisy input or fail to fully exploit iterative generative priors, compromising the fidelity and quality of the reconstructed images. To address this issue, we propose FlowSR, a novel approach that reformulates the SR problem as a rectified flow from low-resolution (LR) to high-resolution (HR) images. Our method leverages an improved consistency learning strategy to enable high-quality SR in a single step. Specifically, we refine the original consistency distillation process by incorporating HR regularization, ensuring that the learned SR flow not only enforces self-consistency but also converges precisely to the ground-truth HR target. Furthermore, we introduce a fast-slow scheduling strategy, where adjacent timesteps for consistency learning are sampled from two distinct schedulers: a fast scheduler with fewer timesteps to improve efficiency, and a slow scheduler with more timesteps to capture fine-grained texture details. Extensive experiments demonstrate that FlowSR achieves outstanding performance in both efficiency and image quality.

### GPT总结
#### 文章内容
该文关注扩散模型在真实场景图像超分辨率（SR）中的推理慢问题，现有few-/single-step方案要么从噪声出发建模效率低，要么未充分利用迭代生成先验而影响质量。作者提出FlowSR，将SR重构重塑为从LR到HR的Rectified Flow，并以改进的Consistency Distillation（加入HR正则与快慢时间调度）将多步生成能力蒸馏为单步。实验表明该方法在单步即可实现高质量SR，同时在效率与画质上兼顾。

#### 方法
- 将SR建模为Rectified Flow：定义直线路径Xt=(1−t)·XHR + t·XLR（将XLR上采样到HR尺度），学习向量场vθ(Xt,t)去回归XLR−XHR的方向，目标为E||vθ(Xt,t) − (XLR−XHR)||2。
- 逆向推理：从t=1的XLR出发，采用Euler等数值方法沿学得的流场积分至t=0获得HR；支持任意步数，单步形式为X̂HR = XLR − vθ(XLR,1)。
- 一步化蒸馏：以预训练多步教师SR flow vϕ为目标，进行Consistency Distillation（CD），将多步采样能力压缩到单步推理。
- HR正则化一致性学习：在CD中显式引入HR目标约束，保证流的一致性同时精确收敛至真值HR。
- 快慢时间调度：一致性学习时相邻时间步从两个调度器采样——“快”调度器（步数少，提升效率）与“慢”调度器（步数多，捕获细节），兼顾效率与纹理刻画。

#### 创新点
- 任务建模：首将真实场景SR重塑为从LR到HR的Rectified Flow，避免扩散式噪声破坏，直接利用LR与HR的强相关性实现高效采样。
- 优化目标：提出带HR正则项的改进一致性蒸馏，使学习到的SR流不仅自一致且准确收敛到HR真值。
- 训练策略：设计快-慢混合时间调度以提升蒸馏效率并保留细粒度纹理先验。
- 推理范式：通过一致性蒸馏将多步迭代先验压缩为单步映射，实现高质量single-step SR。

#### 实验结论
- 任务与设置：面向real-world image SR；具体数据集与评测指标文中未明确说明。
- 结果与对比：作者报告FlowSR在效率与图像质量上均表现突出，可在单步实现高质量重建；具体数值与与SOTA的量化对比文中未明确说明。
- 额外观察：多步采样可进一步提升视觉细节；具体提升幅度与消融细节文中未明确说明。

## 关键词：reinforcement learning

## OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation
- **论文链接**: http://arxiv.org/abs/2605.12480v1
- **作者**: Guohui Zhang, XiaoXiao Ma, Jie Huang, Hang Xu, Hu Yu, Siming Fu, Yuming Li, Zeyue Xue, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao
- **原始摘要**: Recent advances in joint audio-video generation have been remarkable, yet real-world applications demand strong per-modality fidelity, cross-modal alignment, and fine-grained synchronization. Reinforcement Learning (RL) offers a promising paradigm, but its extension to multi-objective and multi-modal joint audio-video generation remains unexplored. Notably, our in-depth analysis first reveals that the primary obstacles to applying RL in this stem from: (i) multi-objective advantages inconsistency, where the advantages of multimodal outputs are not always consistent within a group; (ii) multi-modal gradients imbalance, where video-branch gradients leak into shallow audio layers responsible for intra-modal generation; (iii) uniform credit assignment, where fine-grained cross-modal alignment regions fail to get efficient exploration. These shortcomings suggest that vanilla RL fine-tuning strategy with a single global advantage often leads to suboptimal results. To address these challenges, we propose OmniNFT, a novel modality-aware online diffusion RL framework with three key innovations: (1) Modality-wise advantage routing, which routes independent per-reward advantages to their respective modality generation branches. (2) Layer-wise gradient surgery, which selectively detaches video-branch gradients on shallow audio layers while retaining those for cross-modal interaction layers. (3) Region-wise loss reweighting, which modulates policy optimization toward critical regions related to audio-video synchronization and fine-grained alignment. Extensive experiments on JavisBench and VBench with the LTX-2 backbone demonstrate that OmniNFT achieves comprehensive improvements in audio and video perceptual quality, cross-modal alignment, and audio-video synchronization.

### GPT总结
#### 文章内容
本文关注联合音视频生成中同时优化单模态保真度、跨模态语义一致性与细粒度音画同步的难题，指出直接用单一全局优势的RL微调在多目标、多模态场景下会产生优化错配。作者提出OmniNFT，一个面向模态的在线扩散RL框架，通过模态级优势路由、层级梯度手术与区域级损失重加权，分别缓解优势不一致、跨模态梯度失衡与统一信用分配的问题。基于LTX-2在JavisBench与VBench的实验显示，OmniNFT在音视频感知质量、跨模态对齐与音画同步上取得全面提升。

#### 方法
- 组内采样与奖励分解：对每个文本条件c生成G组联合音视频对{(x_v^(i), x_a^(i))}，对k∈{v, a, av}分别打分{R_k^(i)}并计算独立的reward-wise优势{A_k^(i)}，形成三套解耦优势集合。
- 模态级优势路由（Modality-wise advantage routing）：将A_v、A_a、A_av分别路由到视频分支、音频分支与跨模态交互模块，避免单一全局优势驱动多模态更新。
- 层级梯度手术（Layer-wise gradient surgery）：在音频模型浅层选择性截断来自视频分支的梯度，保留作用于跨模态交互层的有效梯度，抑制视频梯度对音频内模态生成的“渗漏”和主导。
- 区域级损失重加权（Region-wise loss reweighting）：对与音画同步与细粒度对齐相关的关键区域进行损失加权，强化策略在关键时空区域的优化与探索。
- 在线扩散RL优化：在扩散生成范式下进行在线RL微调，结合RLVR/GRPO式组相对优势以稳定训练和多目标优化（具体实现细节如超参数与训练配置文中未明确说明）。

#### 创新点
- 首次系统性揭示RL用于联合音视频生成的三大瓶颈：多目标优势不一致、多模态梯度失衡与统一信用分配不当，并据此设计对应机制。
- 提出模态级优势路由，将多奖励、多模态的优势解耦并定向施加到对应生成分支，避免全局优势引发的跨模态干扰。
- 提出层级梯度手术，按网络层次精细控制跨分支梯度流，既保护各自内模态生成，又保留跨模态交互所需的梯度信号。
- 提出区域级损失重加权，将优化重心聚焦到与音画同步和细粒度对齐最相关的关键区域，实现更细致的信用分配。

#### 实验结论
- 基于LTX-2在JavisBench与VBench评测，OmniNFT相对基线在音视频感知质量、跨模态对齐与音画同步上总体提升；如图示指标中LTX-2+OmniNFT达到Motion Quality 0.797、Visual Quality 3.326、Audio Quality 5.715、CLAP 0.445、AVH-Score 0.257。
- 与LTX-2和LTX-2.3相比，OmniNFT在多数核心指标上取得更优结果（例如相对LTX-2的显著增益；个别指标如JavisScore相较LTX-2.3差异较小但整体趋势向好）。
- 作者结论：面向模态与区域的细粒度信用分配与梯度控制，使RL在联合音视频扩散模型中的多目标、多模态优化更有效，带来全面性能提升。
