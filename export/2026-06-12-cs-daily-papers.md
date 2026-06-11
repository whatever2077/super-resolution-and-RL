# 2026-06-12 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## ATLAS: Active Theory Learning for Automated Science
- **论文链接**: http://arxiv.org/abs/2606.12386v1
- **作者**: Noémi Éltető, Nathaniel D. Daw, Kimberly L. Stachenfeld, Kevin J. Miller
- **原始摘要**: Advancing scientific understanding through mechanistic modeling requires posing the right experimental questions to yield maximally informative data. To automate this pursuit within cognitive science, we introduce ATLAS (Active Theory Learning for Automated Science), an active learning framework for the data-driven discovery of interpretable behavioral models. ATLAS iterates between generating mechanistic hypotheses--instantiated as a diverse ensemble of sparse neural networks (Disentangled RNNs)--and designing experiments that optimally distinguish between them. We test this approach on the problem of recovering reinforcement learning agents from their behavior in bandit tasks. ATLAS designs varied sequences of qualitatively novel experiments with temporal structure tailored to underlying agent characteristics. The models trained on these experiments are evaluated against a comprehensive set of metrics for mechanistic modeling that capture behavioral, structural, and computational similarity. ATLAS achieves a 5-10x improvement in sample efficiency across all metrics compared to random experimentation, and its performance is further validated against expert-designed experiments derived from literature. These in silico results showcase ATLAS's potential to accelerate human-interpretable insights in cognitive science and other domains where scientific inquiry relies on discovering mechanistic models.

### GPT总结
#### 文章内容
本文旨在自动化地通过高信息量实验来加速可解释的机制模型发现，聚焦于从行为数据中恢复强化学习（RL）代理的算法。核心思路是用一组具稀疏约束的可解释 Disentangled RNNs（DisRNNs）作为“假说集合”，并通过主动实验设计（最大化模型间分歧/信息增益）迭代选择最区分假说的实验。主要结论是：在多臂赌博机任务上，ATLAS 相比随机实验在行为预测、结构恢复和计算相似性等指标上实现了5–10×的样本效率提升，并能恢复与真值同构的计算图，且表现不逊于文献中的专家设计实验。

#### 方法
- 使用多样化的 DisRNN 集合作为可解释的机制假说：通过信息瓶颈和稀疏化约束得到少量稀疏交互的潜变量，并以调节稀疏强度维持集成多样性。
- 主动学习闭环：在每个循环中，基于当前数据拟合（从头训练）DisRNN 集合，然后优化下一批实验以最大化集成成员间的分歧/期望信息增益（EIG），贪心选择实验。
- 实验设计采用进化算法搜索实验参数，自动产生能在时间结构上区分不同机制的奖励序列/任务配置。
- 以综合“机制建模”指标评估与选择模型：包括对外部分布实验的行为预测性能、计算图（结构）恢复率，以及状态动力学的均方误差（MSE）等。
- 与开放式基线（i.i.d. 随机奖励、Gaussian random walks）和文献专家设计方案对比，进行多次独立运行与循环评估。

#### 创新点
- 将可解释的机制模型（DisRNN 集合）直接纳入主动实验设计闭环，兼顾可解释性与发现性，弥合黑盒主动学习与预设机制比较之间的鸿沟。
- 通过稀疏度调节构建多样化的可解释假说空间，并以进化搜索最大化模型间分歧/EIG，驱动产生“结构化且新颖”的时间型实验。
- 提出覆盖行为、结构与计算层面的综合评估框架，用于验证是否恢复“可同构”的计算图与动力学，而非仅限于预测精度。
- 在 RL 代理（如 Q-learning、Leaky Actor-Critic）的恢复任务上系统验证样本效率与泛化性能，并与文献中的专家实验生成器进行并行对照。

#### 实验结论
- 任务与设置：在多臂赌博机环境中从行为恢复 RL 代理（Q-learning、Leaky Actor-Critic）；每个数据集进行8次独立 ATLAS 运行、每次100个循环；基线为i.i.d. 随机奖励与Gaussian random walks（匹配[22]）。
- 核心结果：相较随机实验，ATLAS 在行为预测、计算图恢复与状态动力学MSE等指标上实现5–10×样本效率提升；在保留实验上的预测接近天花板，结构恢复率显著更高，并与专家设计实验相比表现相当或更优。
- 现象观察：ATLAS 自动生成的实验呈现丰富的时间结构并随循环演化；最佳模型在约第100循环收敛到与真值同构的计算图，体现出针对不同代理特性的定制化实验策略。
