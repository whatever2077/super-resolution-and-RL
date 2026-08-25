# 2026-08-26 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Bridging Restoration and Generation in One-step Diffusion for Real-World Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2604.24136v3
- **作者**: Shyang-En Weng, Yi-Cheng Liao, Yu-Syuan Xu, Chia-Hung Yuan, Wei-Chen Chiu, Ching-Chun Huang
- **原始摘要**: Pretrained diffusion models have revolutionized real-world image super-resolution (Real-ISR), but their iterative sampling is computationally prohibitive, driving efforts to distill it into a single step. General one-step methods fine-tune the generative prior into a deterministic mapping, restoring efficiency but discarding its stochastic nature. Conversely, recent attempts re-engage generation by shifting the timestep or injecting random noise, adjusting either the position or the state while the other stays fixed. Because only one side is controlled, the two align at isolated preset timesteps but drift apart once steered, leaving generation unstable. To address this, we present one-step diffusion via Inversion and Degradation-aware Sampling for Real-ISR (IDaS-SR), a one-step framework that bridges deterministic restoration and stochastic generation. At its core, Manifold Anchoring grounds the low-quality latent on the pretrained trajectory through two operations jointly estimated by the Manifold Inversion Noise Estimator (MINE): positioning declares where the latent lies and how it deviates from the clean state, while inversion aligns the latent to the declared position. Upon the anchor, CHARIOT reintroduces controlled stochasticity by jointly rescheduling the trajectory and interpolating the noise, enabling a single scalar to smoothly navigate the fidelity-realism trade-off. Extensive experiments demonstrate that IDaS-SR effectively unleashes the generative prior, achieving state-of-the-art performance under explicit control in a single inference step.

### GPT总结
#### 文章内容
该论文针对Real-ISR中预训练扩散模型多步采样推理开销大、单步蒸馏又丢失随机性的矛盾，提出一套在单步内同时实现确定性复原与可控生成的框架IDaS-SR。核心思路是通过Manifold Anchoring将LQ潜变量“锚定”回预训练扩散轨迹（同时对齐位置与状态），并用CHARIOT在单步中联合重排时间表与噪声插值，引入可控随机性。实验表明，IDaS-SR在NFE=1下即可在多项无参考IQA指标上达到或超越现有方法，并可用单一标量平滑控制保真—真实感权衡。

#### 方法
- Manifold Anchoring：以MINE（Manifold Inversion Noise Estimator）联合估计两类量；
  - Positioning：判定LQ潜变量在预训练扩散轨迹上的位置及偏离洁净状态的程度；
  - Inversion：生成与该位置匹配的“逆映射噪声”，把潜变量对齐到声明位置，实现位置—状态配对。
- CHARIOT：在锚点之上，联合“重设采样时间表”与“噪声插值”，在单步中稳健引入受控随机性。
- 单一标量控制：用一个连续标量在保真与真实感之间平滑调节，避免仅改时间步或仅加噪导致的位置—状态失配与不稳定。
- 训练与数据：在LSDIR、FFHQ前10K、Flickr2K、DIV2K上，采用Real-ESRGAN退化管线合成LR–HR对进行训练；基于预训练T2I扩散先验（如Stable Diffusion）。具体损失函数与微调细节文中未明确说明。
- 推理：单步（NFE=1）前向，即时输出；不依赖多步迭代。

#### 创新点
- 将确定性复原与随机生成在单步内统一：通过“位置—状态”双向对齐的Manifold Anchoring，避免既有单步方法仅控其一所致的失配与不稳定。
- MINE联合估计“positioning + inversion noise”，首次在单步蒸馏中显式重构预训练扩散轨迹上的成对关系。
- CHARIOT提出“联合时间重排+噪声插值”的退化感知采样策略，用单一标量实现可解释、可连续的保真—真实感权衡。
- 在一阶段、一步推理框架中有效释放T2I扩散先验的生成能力，同时保持效率与稳定性。

#### 实验结论
- 数据与任务：在RealSR、DRealSR两套配对真实数据集及无配对RealPhoto60上评测，指标涵盖LPIPS、DISTS、CLIPIQA、HyperIQA、MUSIQ、TOPIQ、MANIQA、TReS等。
- 关键结果（NFE=1）：在DRealSR上CLIPIQA 0.746、TOPIQ 0.674达最好或并列最优；在RealSR上CLIPIQA 0.734、HyperIQA 0.680、MUSIQ 70.49、TOPIQ 0.711为最佳；在RealPhoto60上CLIPIQA 0.796、HyperIQA 0.681、TOPIQ 0.725、TReS 85.29为最佳（MUSIQ 73.65、MANIQA 0.626具竞争力）。部分失真类指标（如LPIPS、DISTS）非最优，体现可控权衡。
- 作者结论：IDaS-SR在单步推理下实现显式、平滑的保真—真实感控制，释放扩散先验的生成力，在多项无参考IQA上达到SOTA或强竞争力。

## 关键词：reinforcement learning

## How to Train a Critic Stably and Efficiently
- **论文链接**: http://arxiv.org/abs/2608.23566v1
- **作者**: Penghui Qi, Xiangxin Zhou, Wee Sun Lee
- **原始摘要**: Group-based reinforcement learning methods such as GRPO for large language models avoid training a critic by sampling multiple responses for each prompt. A reliable critic could instead estimate token-level advantages from one response, but standard critic-based training recipes are often unstable. We study this instability and develop \textbf{Best-Practice Critic Optimization (BPCO)}, a recipe that combines DPPO, value predictions bounded to the reward range, Monte Carlo value targets, unnormalized policy advantages, and length-adaptive generalized advantage estimation. Because the critic is used only during training, BPCO can also condition it on reward-defining information, such as a reference answer or grading rubric, that is hidden from the policy. Controlled experiments isolate the effect of each design choice. Across mathematical reasoning tasks with models ranging from 1.5B parameters to 30B-A3B mixtures of experts, BPCO improves a strong critic-based baseline consistently, and matches or exceeds a group-based baseline while sampling one response per prompt. The same recipe also improves learning with rubric-based rewards. These results show that a carefully designed critic provides a reliable alternative to group-relative advantage estimation. Code is available at https://github.com/QPHutu/golden_critic

### GPT总结
#### 文章内容
论文聚焦于大语言模型RL训练中基于critic的方法不稳定、效率不高的问题，旨在用单次采样实现稳定、细粒度的token级优势估计，替代依赖多次采样的组相对方法（如GRPO）。作者提出Best-Practice Critic Optimization (BPCO)：将DPPO、值函数有界化、Monte Carlo目标、非归一化优势与长度自适应GAE组合，并允许critic在训练期接收参考答案/评分rubric等“特权信息”。实验表明，BPCO在数学推理任务上稳定、可复现地提升强critic基线，且在每prompt仅采样一次的条件下匹配或超过GRPO类方法，同时提升基于rubric的奖励学习。结论是：精心设计的critic为组相对优势估计提供了可靠替代方案。

#### 方法
- 单轨迹actor–critic：采用DPPO替代PPO，按采样token概率定义剪切，降低对高/低概率token的非对称影响。
- 值函数有界化：用缩放arctan将线性head输出映射到已知回报区间[Rmin, Rmax]，避免超范围预测引发不稳定。
- 目标与优势：使用Monte Carlo值目标；采用非归一化的policy优势，避免批内归一化强制单位尺度导致信号失真。
- 信号时序：引入长度自适应GAE，缓解固定λ在不同长度序列中对终回报权重不一致的问题。
- 特权信息训练：critic仅在训练时接收参考答案或rubric等奖励定义信息，推理时对policy隐藏，降低值函数近似难度而不改变部署接口。

#### 创新点
- 系统诊断与修复两类常被忽视的不稳定源：线性value head越界预测与批内优势归一化；提出值函数有界化与非归一化优势作为对策。
- 将DPPO、Monte Carlo目标、非归一化优势与长度自适应GAE整合为统一且稳健的BPCO训练配方。
- 引入“critic特权信息”范式：在不改变policy输入与部署的前提下向critic提供参考答案/评分rubric以简化值函数学习。
- 在LLM-RL语境下给出可复现的受控消融，逐步隔离各设计选择的效应，形成可操作的最佳实践。

#### 实验结论
- 受控小数据“理智测试”：在DeepSeek-R1-Distill-Qwen-1.5B与1,460个可解数学题上，PPO在λ=1下训练回报崩溃；DPPO稳定；将λ=0.99作为压力测试暴露critic误差敏感性；对值函数进行有界化显著稳定训练，AIME 2025 avg@32作为持出指标随之改善。具体数值文中未明确说明。
- 大规模数学推理：在1.5B至30B-A3B MoE范围模型上，BPCO持续优于强critic基线，并在每prompt单样本条件下匹配/超过GRPO/Dr.GRPO。具体数值文中未明确说明。
- 基于rubric的奖励：同一训练配方可提升此类设置下的学习效果，进一步验证BPCO的普适性。具体数值文中未明确说明。
