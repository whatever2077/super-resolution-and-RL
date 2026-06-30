# 2026-07-01 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Learning to Balance: Decoupled Siamese Diffusion Transformer for Reference-Based Remote Sensing Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2605.17980v2
- **作者**: Bin Luo, Runmin Dong, Zhaoyang Luo, Jinxiao Zhang, Jiyao Zhao, Fan Wei, Haohuan Fu
- **原始摘要**: Diffusion-based methods demonstrate significant potential for remote sensing image super-resolution at large scaling factors, particularly in reference-based super-resolution (RefSR), where high-resolution reference images provide critical fine-grained texture priors. However, existing methods often suffer from a trade-off between over-reliance on reference information, which leads to texture artifacts, and under-utilization of such information, which results in insufficient detail recovery. To address these issues, we propose DS-DiT, a Decoupled Siamese Diffusion Transformer that decouples the interaction between low-resolution (LR) and reference (Ref) conditions within the attention mechanism. By allowing LR structural priors and Ref texture information to independently interact with the noisy latent, the framework effectively mitigates competition between the two conditional sources. To further compensate for the limited local modeling ability of global attention, we introduce a Patch-Level Weighting (PLW) module that adaptively modulates the fusion of conditional sources. In addition, the siamese architecture enables an inference-time autoguidance strategy that exploits the prediction discrepancy between strong and weak Ref conditions to improve generation quality without additional training. Experimental results across multiple datasets and scaling factors show that DS-DiT outperforms existing methods in both quantitative metrics and visual fidelity.

### GPT总结
#### 文章内容
- 论文聚焦于遥感参考超分辨率（RefSR）在大倍率（×8/×16）下对参考纹理“过度依赖/利用不足”的两难：过度依赖会引入伪纹理，利用不足则细节恢复不充分。  
- 提出DS-DiT（Decoupled Siamese Diffusion Transformer），在扩散Transformer中将LR结构先验与Ref纹理先验在注意力层面解耦为“孪生”分支，各自与噪声潜变量交互，并辅以Patch-Level Weighting（PLW）进行自适应条件融合。  
- 推理期引入无需额外训练的自引导（autoguidance, AG），由强/弱参考条件的预测差异提供引导方向，提升生成质量。  
- 实验表明在多数据集与多倍率上，DS-DiT在定量指标与视觉质量上均优于现有方法。

#### 方法
- 解耦孪生注意力：将LR与Ref作为相互独立的条件分支，仅与噪声潜变量交互，缓解多条件在联合注意力中的信息竞争。  
- Patch-Level Weighting（PLW）：在局部块级别对LR/Ref条件进行自适应加权融合，弥补全局注意力对局部建模能力的不足。  
- 扩散生成框架：基于DiT的多条件扩散模型，以LR提供结构先验、Ref提供纹理先验进行条件控制，联合去噪重建HR。文中未明确说明具体损失函数/噪声调度等训练细节。  
- 推理期自引导（AG）：构造“弱参考”预测（抑制Ref交互分支）与“强参考”预测的差分方向用于引导，训练外零开销；对比PAG、SEG、ICG等训练外引导方案取得小幅总体优势。  
- 计算与开销：默认采样步数为40；启用AG需额外一次弱预测前向，参数不变但推理代价增加。

#### 创新点
- 在DiT中提出“解耦孪生”条件建模，使LR与Ref各自与潜变量独立交互，避免传统MM-DiT式联合注意力导致的条件竞争与失衡。  
- 设计PLW进行块级自适应融合，显式增强局部建模与条件选择性，提升纹理迁移的可靠性。  
- 面向RefSR定制的训练外自引导策略（强/弱参考差分），无需额外训练即可稳定提升视觉质量。  
- 相比依赖理想变化先验的方案（如需要精确变化掩码），该框架在无显式变化掩码条件下实现稳健参考纹理利用。

#### 实验结论
- 任务与数据：在参考遥感超分辨率（×8/×16、大倍率）与跨传感器真实场景上评估；数据集包含SECOND（2968/1694对，512×512）、FUSU（7436/2192对，512×512）、CNAM-CD（1758/750对）与Real-RefRSSRD（NAIP 1 m vs Sentinel-2 10 m）。  
- 主要结果：跨多数据集/倍率，DS-DiT在定量指标与视觉保真度上均优于现有方法；AG较PAG、SEG、ICG取得略优整体表现。  
- 计算开销：生成512×512图像时（NVIDIA A100, 40步），Ours用时约2.48 s、FLOPs约90.88 T；启用AG后约4.73 s、FLOPs约181.75 T，模型参数不变。文中未明确说明具体数值的指标名称与绝对分数。

## 关键词：reinforcement learning

## When and Which Sensor to Observe? Timely Tracking of a Joint Markov Source
- **论文链接**: http://arxiv.org/abs/2606.30623v1
- **作者**: Ismail Cosandal, Sennur Ulukus, Nail Akar
- **原始摘要**: We investigate the problem of remote estimation (at a monitor) of a discrete-time joint Markov process with individual components which can be observed with dedicated sensors. At a given time slot, the monitor has the option of staying idle or sending a pull request to one of the sensors to obtain a partial state value, while the sensors are assumed to have heterogeneous sampling costs. Our goal is to develop a monitor pull policy, i.e., determining when and towards which sensor to send a pull request, in order to minimize a weighted sum of average age of incorrect information (AoII), or in short age, and sampling costs. As the communication model, we assume an erasure channel with a fixed one-slot delay from each sensor to the monitor. In this setting, the monitor does not perfectly know either the state of the process or the age, at any given time. We first obtain a sufficient statistic, namely belief, representing the joint distribution of the age and the current state of the observed process, by using the history of all pull requests and observations. Then, we formulate the optimization problem as a continuous state-space Markov decision process (MDP), namely belief-MDP, for the solution of which we propose two model predictive control (MPC) methods, namely MPC without terminal costs (MPC-WTC), and reinforcement learning MPC (RL-MPC). The effectiveness of the proposed methods is validated by numerical examples.

### GPT总结
#### 文章内容
- 论文研究在多传感器观测的联合离散时间马尔可夫过程下，监控端何时、向哪一传感器发起“拉取”以最小化平均Age of Incorrect Information (AoII)与采样成本加权和的问题。
- 在前向信道存在一时隙固定时延与擦除的条件下，监控端既不知道真实状态也不知道AoII；作者以历史请求与观测构造对(状态, AoII)的联合分布belief作为充分统计量。
- 将问题表述为连续状态空间的belief-MDP，并提出两种模型预测控制方法：MPC without terminal costs (MPC-WTC) 与 reinforcement learning MPC (RL-MPC)。
- 数值实验验证所提方法的有效性。

#### 方法
- 构造belief：利用所有历史拉取请求与观测，估计当前源状态与AoII的联合分布，作为决策的充分统计量。
- 建模为belief-MDP：连续状态为belief，动作为空闲或选择某一传感器拉取，目标为平均AoII与采样成本的加权和最小化。
- 信道与时延：反向拉取请求即时到达，前向为一时隙传输并具有固定擦除概率。
- 设计两种MPC策略：MPC-WTC（不含终端代价）与RL-MPC（结合reinforcement learning的MPC求解框架）。
- 适配异质采样成本：在动作选择中显式权衡不同传感器的采样代价与AoII降低收益。

#### 创新点
- 面向联合马尔可夫源的“按需拉取”决策：各传感器仅观测部分状态，个体可能非马尔可夫，但联合过程马尔可夫。
- 在存在时延与擦除且AoII不可直接观测的条件下，提出以(状态, AoII)联合belief为充分统计量的belief-MDP建模。
- 面向连续belief空间的求解，提出MPC-WTC与RL-MPC两种可实现策略，兼顾模型信息与学习能力。
- 以AoII这一语义化新鲜度—失配指标作为优化目标，区别于传统AoI类建模。

#### 实验结论
- 通过数值算例验证所提MPC-WTC与RL-MPC在加权平均AoII与采样成本上的有效性与适用性。
- 文中未明确说明具体数据集、基线方法与数值对比指标的细节。
- 文中未明确说明不同信道擦除概率、时延或成本权重下的量化性能增益。
