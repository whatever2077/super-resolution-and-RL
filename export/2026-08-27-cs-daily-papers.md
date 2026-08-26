# 2026-08-27 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## SPO++: Stream-Aligned Policy Optimization for Asynchronous Agentic RL
- **论文链接**: http://arxiv.org/abs/2608.24870v1
- **作者**: Kai Ruan, Jinghao Lin, Qianshan Wei, Ziqi Zhou, Zihe Huang
- **原始摘要**: Group-relative reinforcement learning waits for sibling rollouts of the same prompt, which is costly for long and variable tool-use trajectories. Single-stream Policy Optimization (SPO) removes this dependency with a persistent prompt-level value estimate, but its recipe whitens one advantage per trajectory before optimizing a token-mean actor loss. We show that trajectory centering generally does not center the token-weighted quantity consumed by the actor, and fix the mismatch by standardizing terminal-outcome advantages under the action-token measure. We additionally organize prompt evidence by the policy event that generated it rather than learner receipt order. Across matched runs on ALFWorld at two model scales and on Math-TIR, SPO++ improves online learning efficiency over SPO. A paired ablation identifies action-token-measure normalization as the strongest tested component.

### GPT总结
#### 文章内容
本文针对群相对RL（如GRPO）在长且异步的工具使用轨迹中需等待同组样本的问题，以及SPO在单流设定下“轨迹白化”与“按token均值的actor损失”之间的度量不匹配问题，提出SPO++。核心思路是在异步执行中以“策略事件时间”冻结与组织prompt基线，并在与actor损失一致的“动作token度量”下标准化终止优势。实验在ALFWorld与Math-TIR上表明，SPO++在相同预算下显著提升在线学习效率；消融显示动作token度量的归一化是最强贡献项。结论是：单流RL需同时对齐策略时钟与actor优化所用的度量，才能稳定高效地学习。

#### 方法
- 单流依赖图：保持每个prompt仅一条在线rollout、仅使用终止结果奖励；为每个prompt维护Bernoulli证据(α, β)，估计基线v̂=α/(α+β)，优势A=R−v̂，并以保留因子ρ更新证据（SPO++采用固定ρ=0.875）。
- 事件时间记忆（event-time memory）：以策略快照坐标z标记请求，在“派发时”冻结prompt基线；回传时将结果归档到生成该样本的策略事件，避免因系统返回顺序导致的基线偏差。
- 动作token度量归一化：在与actor损失一致的“action-token measure”下标准化终止优势，解决SPO中按轨迹白化却用token均值优化带来的长度依赖型偏置。
- 优化与稳定性：采用token-mean actor loss，配合Dual-Clip（SPO++使用c=2；SPO为c=10）与重要性修正（importance correction保留，文中未明确说明细节），在完全异步运行时对齐度量与时钟。

#### 创新点
- 将优势标准化的度量从“轨迹级”对齐到“动作token级”，直接匹配token-mean actor loss，消除响应长度引起的隐式中心偏移。
- 以“策略事件时间”组织与冻结prompt基线，替代按学习器接收顺序更新，确保异步环境下基线与策略时钟一致。
- 在单流RL配方中引入固定保留因子ρ与事件坐标，使基线随策略演化但不受系统时序噪声影响；并通过成体系实验表明该对齐对于长地平线任务尤为关键。

#### 实验结论
- 任务与设置：在ALFWorld（128个任务）上评测Qwen3.5-0.8B与Qwen3.5-2B，在Math-TIR（DAPO-Math-17K的1,500样本训练划分，带Python工具）上评测Qwen3.5-0.8B；两域分别使用6,400与25,600条在线轨迹预算，指标为曲线面积（AUC）与末端平均奖励。
- 主要结果：相对SPO，SPO++在AUC上提升+19.00 ± 8.95（ALFWorld 0.8B）、+15.92 ± 10.25（ALFWorld 2B）、+2.50 ± 1.64（Math-TIR）；末端奖励提升+7.86 ± 7.18、+4.88 ± 6.83、+5.03 ± 4.74。
- 作者结论：SPO++在各设置下均提高在线学习效率；长地平线ALFWorld收益更大，支持“当响应token数与优势相关时，按动作token度量归一化更重要”的预测；配对消融表明动作token度量归一化是最显著的独立改进点。
