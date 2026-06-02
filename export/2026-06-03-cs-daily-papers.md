# 2026-06-03 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Fast Image Super-Resolution via Consistency Rectified Flow
- **论文链接**: http://arxiv.org/abs/2605.12377v2
- **作者**: Jiaqi Xu, Wenbo Li, Haoze Sun, Fan Li, Zhixin Wang, Long Peng, Jingjing Ren, Haoran Yang, Xiaowei Hu, Renjing Pei, Pheng-Ann Heng
- **原始摘要**: Diffusion models (DMs) have demonstrated remarkable success in real-world image super-resolution (SR), yet their reliance on time-consuming multi-step sampling largely hinders their practical applications. While recent efforts have introduced few- or single-step solutions, existing methods either inefficiently model the process from noisy input or fail to fully exploit iterative generative priors, compromising the fidelity and quality of the reconstructed images. To address this issue, we propose FlowSR, a novel approach that reformulates the SR problem as a rectified flow from low-resolution (LR) to high-resolution (HR) images. Our method leverages an improved consistency learning strategy to enable high-quality SR in a single step. Specifically, we refine the original consistency distillation process by incorporating HR regularization, ensuring that the learned SR flow not only enforces self-consistency but also converges precisely to the ground-truth HR target. Furthermore, we introduce a fast-slow scheduling strategy, where adjacent timesteps for consistency learning are sampled from two distinct schedulers: a fast scheduler with fewer timesteps to improve efficiency, and a slow scheduler with more timesteps to capture fine-grained texture details. Extensive experiments demonstrate that FlowSR achieves outstanding performance in both efficiency and image quality. Code: \href{https://github.com/jiaqixuac/FlowSR}{this https URL}.

### GPT总结
#### 文章内容
这篇论文针对扩散模型在超分辨中依赖多步采样导致推理缓慢的问题，提出将SR重构建模为从LR到HR的Rectified Flow，并通过改进的一致性学习实现单步高质量重建。核心思路是学习一个SR flow的向量场以连接LR与HR，再将多步采样能力蒸馏到单步模型，辅以显式HR正则与快-慢时间调度。作者结论是：FlowSR在效率与图像质量上均取得优异表现，实现单步高质量SR，同时可使用多步进一步提升纹理细节。

#### 方法
- 定义SR flow：在HR与上采样后的LR之间采用线性插值Xt=(1−t)XHR+tXLR，训练向量场vθ回归XLR−XHR（L2损失），直接从LR而非噪声出发以保留结构信息。
- 推理为逆向ODE积分（如Euler），从t=1到t=0；支持任意步数，单步形式为X̂HR = XLR − vθ(XLR, 1)。
- 一致性蒸馏（Consistency Distillation）：以多步采样的教师SR flow vϕ为目标，将其迭代生成能力蒸馏到学生模型，实现更少步甚至单步推理。
- HR正则化：在一致性学习中显式引入HR目标，既强化自一致性，又保证流的终点精确收敛到GT HR。
- 快-慢调度：一致性学习中相邻时间步同时来自“快”调度（步数少、提效）与“慢”调度（步数多、强化细节），在效率与纹理保真间折中。

#### 创新点
- 将超分辨重构为LR→HR的Rectified Flow，避免DDPM式从噪声到图像的弯曲轨迹与信息损失，更契合LR/HR的强相关性。
- 提出带HR正则的一致性学习，兼顾自一致与对GT收敛，提升单步重建的保真度。
- 设计快-慢时间采样调度用于一致性蒸馏，兼顾效率与细粒度纹理捕获。
- 通过蒸馏迭代生成先验至单步模型，实现单步高质量SR，保留迭代先验优势且显著加速。

#### 实验结论
- 任务与数据集：定位于真实场景图像超分辨；具体数据集与评测设置文中未明确说明。
- 核心结果：相较现有扩散式SR（如DDPM/DDIM系、ResShift、DoSSR），FlowSR在效率与画质上均表现优异，单步即可获得高质量结果，多步可进一步增强纹理细节；具体数值文中未明确说明。
- 作者结论：FlowSR在单步高质量与可调步数的效率-质量权衡上具有优势，证明一致性整流的SR flow有效；代码已开源。

## 关键词：reinforcement learning

## Towards Automated Discovery: A Review of Generative Models, Multimodal Learning and Closed-Loop Workflows in Inverse Materials Design
- **论文链接**: http://arxiv.org/abs/2606.02507v1
- **作者**: Anand Babu, Rogério Almeida Gouvêa, Gian-Marco Rignanese
- **原始摘要**: Inverse materials design is shifting materials discovery from forward prediction to targeted proposal of candidates that satisfy objectives under physical constraints. Here, we review recent advances in generative crystal structure modeling, multimodal learning, and closed-loop design pipelines for crystalline solids. We survey how modern generators learn chemical-structural priors from large databases to enable controllable sampling of periodic structures, and compare leading model classes including variational autoencoders, normalizing flows, autoregressive formulations, and diffusion models. Particular attention is given to how feasibility constraints and physical priors are enforced across the workflow, through representation choices, training objectives, sampling-time guidance, and post-generation screening and relaxation. We also discuss how multimodal learning fuses diverse materials modalities, including crystal structures, thermodynamic, electronic information, microscopy, spectroscopy, processing context, and scientific text, to construct a more universal, transferable representation of chemical space. In addition, diverse inverse-design strategies are examined, particularly those that integrate conditional generation with latent optimization, Bayesian optimization, reinforcement learning, and active learning. Finally, we highlight recurring failure modes, such as surrogate exploitation, diversity collapse, distribution shift, and the stability-synthesizability gap, and outline discovery-grade evaluation practices based on staged reporting of validity, novelty, uniqueness, stability, and cost.

### GPT总结
#### 文章内容
这篇综述聚焦逆向材料设计，从“预测给定候选的性质”转向“在物理与合成可行性约束下有目标地提出候选”。核心思路是系统梳理晶体结构生成（VAE、Normalizing Flows、autoregressive、diffusion 等）、多模态学习与闭环（proposal–evaluation–feedback）工作流，并强调在表征、训练、采样与后处理各环节注入物理先验与可行性约束。作者主张采用分级、可验证的评估（validity、novelty、uniqueness、stability、cost）以规避 surrogate exploitation、diversity collapse、distribution shift 与稳定性-可合成性鸿沟等失效模式，作为通向自驱动实验室的实践框架。

#### 方法
- 闭环框架：Proposal–Evaluation–Feedback 三步循环；自低成本到高保真（快速合法性筛查→代理模型→结构弛豫/DFT/实验）分层评估，并用反馈（含失败样本）更新模型与策略。
- 生成模型族：对 VAE（ELBO 优化）、GAN（对抗训练）、Normalizing Flows（可逆变换、精确似然）、DDPM（前向加噪/反向去噪）等进行机制与对比性梳理，用于可控采样周期性晶体。
- 约束注入：通过表示（周期性/对称性/电荷平衡等）、训练目标（正则化与物理引导）、采样期引导（guidance）、以及生成后筛查与弛豫来确保结构可行与物理一致性。
- 多模态学习：融合 crystal structures、thermodynamic/electronic、microscopy、spectroscopy、processing context 与科学文本，构建更通用、可迁移、可用于条件约束的表示。
- 逆向设计策略：将条件生成与 latent optimization、Bayesian optimization、reinforcement learning、active learning 相结合，形式化为在可行流形 C 上最大化效用 U(x) 的定向搜索。

#### 创新点
- 将候选生成、目标设定、验证成本与闭环反馈统一为“验证感知”的自动化发现框架，强调仅加速筛选不足，需系统集成。
- 系统化总结在表示、训练、采样与后处理全流程注入物理/化学可行性约束的方法，面向晶体固体的生成与筛选。
- 强调多模态对齐以增强条件可控性与泛化，并提出“discovery-grade”分级评估规范诊断常见失效模式，尤其关注稳定性–可合成性鸿沟。
- 对 surrogate exploitation、diversity collapse、distribution shift 等风险进行分类与对策化讨论，提供可复用的实践指南。

#### 实验结论
- 任务与数据：本文为综述与方法论框架梳理，未报告新模型的对比实证；所依托的大型开放晶体数据库与高通量计算资源的具体名单文中未明确说明。
- 核心结果：比较 VAE、Normalizing Flows、autoregressive、DDPM 等生成范式，梳理多模态融合与闭环设计策略，并给出有效性/新颖性/唯一性/稳定性/成本的分级评估流程以避免常见失效。
- 作者结论：逆向设计应在闭环中一体化可行性约束与可验证目标，结合不确定性与主动学习，方能从“快速筛选”迈向可靠的自动化发现与 self-driving laboratories。
