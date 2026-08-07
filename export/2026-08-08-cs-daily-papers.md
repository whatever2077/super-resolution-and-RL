# 2026-08-08 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Flow-Map Distillation on Relation Manifolds for Image Restoration
- **论文链接**: http://arxiv.org/abs/2608.05769v1
- **作者**: Zihao He, Songhua Liu
- **原始摘要**: Knowledge distillation for image restoration typically aligns intermediate features or relation matrices between teacher and student networks as static targets, ignoring the dynamic structure of the knowledge transfer process. In this paper, we propose Flow-Map Distillation on Relation Manifolds (FoRM), which reformulates relation-based knowledge transfer as a continuous flow mapping problem on the relation manifold. Rather than regressing a constant velocity field between student and teacher relation states, FoRM learns a flow map operator $\mathcal{F}_θ(\mathbf{z}, t, s)$ that directly predicts the relation state at any target time $s$ given the current state at time $t$, enabling richer trajectory-level supervision. To ensure global self-consistency of the learned flow map, we introduce a safe semigroup consistency constraint that enforces compositional agreement using ground-truth bridge states, eliminating phantom-state error accumulation. An endpoint anchoring loss further prevents the operator from drifting away from the teacher target. Extensive experiments on five image restoration tasks, including super-resolution, deraining, denoising, deblurring, and low-light enhancement, demonstrate consistent gains over state-of-the-art distillation baselines across multiple backbone architectures, reducing training variance by approximately 50\% compared to naive flow matching distillation while achieving superior restoration quality.

### GPT总结
#### 文章内容
该论文针对图像复原中的知识蒸馏长期将教师-学生对齐视为“静态目标”而忽视迁移轨迹的问题，提出在关系流形上进行“流映射”式蒸馏。核心思想是学习一个流映射算子 F_θ(z, t, s)，直接从当前关系状态预测任意目标时间的关系状态，并通过安全的半群一致性约束与端点锚定损失确保全局自洽与不漂移。实验在超分、去雨、去噪、去模糊、低光增强五项任务与多种骨干网络中均优于SOTA蒸馏方法，并将训练方差相对naive flow matching降低约50%。

#### 方法
- 在教师-学生的关系流形上定义关系状态 z 及时间参数 t、s，学习流映射算子 F_θ(z, t, s) 以轨迹级监督替代静态回归。
- 引入安全的半群一致性约束（safe semigroup consistency），使用ground-truth桥接状态强制复合一致，避免phantom-state误差累积。
- 设计端点锚定损失（endpoint anchoring loss），将预测轨迹稳固到教师终点，防止流映射漂移。
- 以关系结构对齐为核心的蒸馏训练流程，优于特征/注意力/关系矩阵的单点对齐；具体损失权重、网络细节与实现超参文中未明确说明。
- 推理阶段是否引入额外算子或计算开销文中未明确说明。

#### 创新点
- 将关系蒸馏从“静态对齐”重构为“连续流映射”的轨迹级建模，直接学习 F_θ(z, t, s) 而非常速场回归。
- 提出安全的半群一致性约束，通过真实桥接状态实现可交换复合与全局自洽，抑制虚假状态的误差传播。
- 端点锚定损失与一致性约束的联合优化，实证将训练方差较naive flow matching降低约50%，并显著提升关系结构对齐（Urban100上top-6 patch overlap 71% vs 33%，CKA 0.9847 vs 0.8153）。
- 在多任务与多骨干（SwinIR、RCAN、EDSR、cross-architecture）下的广泛验证，显示相较SOTA蒸馏基线的稳定优胜与泛化性。

#### 实验结论
- 五类复原任务（super-resolution、deraining、denoising、deblurring、low-light）采用Restormer教师–学生设置，FoRM在SOTS、Rain100L、BSD68(σ=25)、GoPro、LOLv1均有提升，平均PSNR/SSIM为27.34/0.877，优于DCKD的27.29/0.875及其他基线。
- ×4 SR在Set5/Set14/BSD100/Urban100上，跨SwinIR、RCAN、EDSR与cross-architecture均优于Logits、FAKD、MiPKD、DCKD等基线；并在Urban100上显著提升与教师的关系对齐指标（top-6 patch overlap与CKA如上）。
- 相较naive flow matching distillation，FoRM将训练方差降低约50%，并在可视化上呈现更锐利结构与更少伪影；更细节的训练设置与计算开销文中未明确说明。

## 关键词：reinforcement learning

## OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models
- **论文链接**: http://arxiv.org/abs/2607.28609v2
- **作者**: Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong
- **原始摘要**: Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, and are then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60x lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

### GPT总结
#### 文章内容
- 论文聚焦于计算机使用代理（CUA）轨迹是否完成任务的判定问题，指出当前依赖的VLM评审在可靠性与可扩展性上存在缺口。
- 提出跨平台高质量评审基准OSReward（含OSReward-Hard与OSReward-Multi），并系统评测大量VLM judges，发现普遍的“宽松偏差”（将失败误判为成功）。
- 构建并开源OS-Shepherd-100K语料，训练开放奖励模型OS-Shepherd（9B/35B），以30–60×更低成本达到接近商用评审的可靠性。

#### 方法
- 跨平台数据采集与环境构建：在desktop、mobile、web上搭建真实应用与初始状态（用户配置、文件、数据库、干扰内容/直播网站）以收集新鲜轨迹，确保评审基于真实环境变化而非叙述。
- 指令与轨迹来源多样化：由不同agent backbones执行经人工核验的指令，覆盖真实使用情境，保证平台间一致的轨迹格式。
- 多阶段人工标注生成金标：对轨迹进行严格多轮人工标注，获得可作为评审模型“金标准”的成败判定；据此构建OSReward，并派生OSReward-Hard与用于细粒度效率/对齐评分的OSReward-Multi。
- 评审协议与指标：制定统一judge协议与二分类等指标评测VLM judges在长时序、多模态轨迹上的稳定性与偏差。具体判定细则与损失设计文中未明确说明。
- 构建与训练奖励模型：基于OS-Shepherd-100K（带推理标注的轨迹评审语料）训练OS-Shepherd 9B/35B，提供低成本、稳定、可靠的轨迹级奖励信号。

#### 创新点
- 首个跨web/mobile/desktop平台、基于“新采集+多阶段人工金标”的CUA轨迹评审标准基准，避免复用基准带来的质量与标注噪声偏差。
- 揭示VLM评审的系统性“宽松偏差”与成本-可靠性权衡：可托付的模型过贵，开源可负担模型显著落后。
- 提出OSReward-Hard与OSReward-Multi，实现更具挑战性的难例评测与细粒度效率/对齐维度的打分。
- 开源OS-Shepherd-100K与OS-Shepherd（9B/35B），在开放可复现的前提下，以30–60×更低成本达到接近商用评审的效果，面向大规模RL数据过滤与奖励提供。

#### 实验结论
- 在OSReward与OSReward-Hard上的大规模评测显示：即便是SOTA VLM judges也远未达“理想法官”，普遍存在将失败误判为成功的“宽松偏差”；难集上性能进一步下降。
- 仅少数高性能评审模型可靠性可用但成本高昂，难以规模化；相对低成本的开源模型整体落后。
- OS-Shepherd（9B/35B）在稳定性与可靠性上接近商用评审，同时实现30–60×成本下降，为CUA评估、数据筛选与RL提供可扩展的奖励信号。
