# 2026-05-20 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## General Preference Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2605.18721v1
- **作者**: Muhammad Umer, Muhammad Ahmed Mohsin, Ahsan Bilal, Arslan Chaudhry, Andreas Haupt, Sanmi Koyejo, Emily Fox, John M. Cioffi
- **原始摘要**: Post-training has split large language model (LLM) alignment into two largely disconnected tracks. Online reinforcement learning (RL) with verifiable rewards drives emergent reasoning on math and code but depends on a programmatic verifier that cannot reach open-ended tasks, while preference optimization handles open-ended generation yet forgoes the continuous exploration that powers online RL. Closing this gap requires a verifier for open-ended quality, but a scalar reward model is the wrong shape for the job. Quality is multi-dimensional, and any scalar score is an incomplete proxy that lets online RL collapse onto whichever axis the score is most sensitive to. We turn instead to the General Preference Model (GPM), which embeds responses into $k$ skew-symmetric subspaces and represents preference as a structured, intransitivity-aware comparison. Building on this, we propose General Preference Reinforcement Learning (GPRL), which carries the $k$-way structure through to the policy update. GPRL computes per-dimension group-relative advantages, normalizes each on its own scale so no axis can dominate, and aggregates them with context-dependent eigenvalues. The same structure powers a closed-loop drift monitor that detects single-axis exploitation and corrects it on the fly by reweighting dimensions and tightening the trust region. Starting from $\texttt{Llama-3-8B-Instruct}$, GPRL reaches a length-controlled win rate of $56.51\%$ on AlpacaEval~2.0 while also outperforming SimPO and SPPO on Arena-Hard, MT-Bench, and WildBench by resisting reward hacking across extended training runs.

### GPT总结
#### 文章内容
该文针对LLM后训练的两条路线割裂：在线RL需可验证奖励而难覆盖开放式任务，偏好优化虽适配开放式生成却缺乏持续探索；标量RM在开放域会被单一维度“劫持”。作者提出基于General Preference Model (GPM) 的General Preference Reinforcement Learning (GPRL)，用多维、可处理不传递性的偏好嵌入替代标量奖励，并在策略更新中保留k维结构与归一化聚合。实验表明，GPRL在保持在线探索的同时抑制单轴利用，显著优于标量RM方案与主流偏好优化方法。主要结论：在Llama-3-8B-Instruct上，GPRL在AlpacaEval 2.0长度控制设定达56.51%胜率，并在Arena-Hard、MT-Bench、WildBench上整体领先，同时更能抵抗reward hacking。

#### 方法
- 以GPM将响应嵌入至k个反对称二维子空间，建模结构化、可不传递的偏好信号；文中采用k=3（在Skywork-Reward上饱和），k=1时退化为GRPO。
- 在GRPO范式内，按维度计算group-relative advantages，保留每个质量轴的相对优势信息。
- 对各维优势分别归一化，使其处于各自尺度上，防止某一轴通过幅度扩大而主导更新。
- 通过上下文依赖的特征值（eigenvalues）对各维优势加权聚合，得到用于策略更新的总优势。
- 设计闭环漂移监控：跟踪优势方差谱以检测单轴利用，并在触发时重加权各维且收紧KL trust region，实现在线矫正。

#### 创新点
- 用GPM提供多维、可表达不传递性的偏好嵌入作为在线RL的奖励源，系统性替代标量RM；k=1时与GRPO一致。
- 提出“按维优势估计—独立尺度归一化—特征值加权聚合”的更新机制，并给出拒绝单轴利用的充分条件，从理论上将GPRL与标量GRPO区分开。
- 引入无需外部评测信号的闭环漂移监控与控制器，通过维度重加权与KL约束自适应抑制reward hacking。
- 区别于多目标RLHF返回Pareto族，GPRL以GPM的轴结构直接训练单一在线策略。

#### 实验结论
- 起始模型为Llama-3-8B-Instruct；在AlpacaEval 2.0（length-controlled）取得56.51%胜率，较GRPO+BT提升14.59个百分点。
- 在Arena-Hard、MT-Bench、WildBench上，GPRL整体优于DPO、SimPO、SPPO、GPO与GRPO+BT，并在长程训练中表现出更强的reward hacking抵抗力。
- 训练细节（如超参数、数据规模等）文中未明确说明。
