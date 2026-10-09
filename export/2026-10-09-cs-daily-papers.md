# 2026-10-09 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Decoupling Exploration from Optimization in RLVR
- **论文链接**: http://arxiv.org/abs/2610.10536v1
- **作者**: Saif Punjwani, Micah Goldblum
- **原始摘要**: Modern language models undergo reinforcement learning with verifiable rewards (RLVR) on top of already-trained checkpoints. A key promise of RLVR is the discovery of new reasoning strategies. In principle, a model can sample novel ideas absent from its prior training data. In practice, however, augmenting RLVR with strong novelty incentives has seen limited success and can degrade model quality. Because verifiable rewards supervise only a narrow slice of the model's knowledge and behavior, such degradations are difficult to recover from. Instead, we decouple exploration from optimization in a framework we call Exploration-Distillation (ExpDis). We train one or more explorer policies with a novelty bonus in the reward, filter their trajectories for correctness and quality, and distill them into a separate student policy. The student policy is then trained without a novelty bonus. We repeat the above procedure for several rounds, alternating between exploration and optimization. This decoupling allows us to aggressively scale exploration without degrading the student policy. Across seven mathematical reasoning benchmarks and two model families, ExpDis outperforms DAPO at the same wall-clock budget. Moreover, we observe improved pass@$k$ scaling, indicating that ExpDis produces models that generate more diverse correct solutions.

### GPT总结
#### 文章内容
这篇论文关注RLVR中“探索”和“优化”耦合导致的质量退化问题，尤其是直接在单一策略上加入强“novelty”激励会损伤模型的广泛能力。核心思路是提出Exploration-Distillation (ExpDis)：用带novelty奖励的“explorer”策略进行激进探索并筛选正确/高质轨迹，再将其蒸馏到不含novelty奖励的“student”策略并用标准RLVR优化，交替多轮进行。主要结论是ExpDis在相同wall-clock预算下优于DAPO，显著改善pass@k并提升正确解的多样性；反之，直接对DAPO施加novelty奖励会降低数学推理性能。

#### 方法
- 训练一个或多个“explorer”策略，在奖励中加入novelty bonus（如RND），其权重λ控制相对正确性的探索强度。
- 对explorer生成的轨迹进行程序化验证与质量过滤，仅保留“正确/高质”样本（具体过滤标准与实现细节文中未明确说明）。
- 将过滤后的轨迹蒸馏到独立的“student”策略，student不接触novelty奖励，仅通过轨迹吸收新策略（蒸馏损失与参数细节文中未明确说明）。
- 用标准RLVR继续优化student，并与explorer交替进行多轮“探索—蒸馏—优化”的循环（轮次数与调度策略文中未明确说明）。
- 评估采用Chen et al.的无偏pass@k估计器；采样设置包含Temperature=1.0/0.6、top-p=0.95、top-k=20、max tokens=32,768、每题16或64样本（“64*”的含义文中未明确说明）。

#### 创新点
- 将“探索”与“优化”彻底解耦：分别使用explorer与student两套策略，从根源避免novelty对主模型参数的负面干扰。
- 策略间通过“过滤后的轨迹”而非参数直接传播信息，使student继承探索成果但不继承探索造成的退化。
- 交替多轮的Exploration-Distillation流程，允许在探索端大幅提高novelty强度与规模，同时在优化端保持稳定性与质量。
- 设计洞见：novelty奖励应仅施加在explorer端；实验显示直接在单模型（DAPO）上加novelty会显著降准。

#### 实验结论
- 任务与数据：七个数学推理基准（表中包含AIME24/25/26、MATH500、Minerva-Math等），两类模型家族（如Qwen3与Ministral）。
- 主要结果：在五个主基准的mean pass@k上，Qwen3-1.7B的ExpDis相较DAPO从@1的45.63提升至51.81、@64从74.64至83.04；Qwen3-4B从@1的62.58至66.50、@64从81.14至87.63。单轮ExpDis即优于DAPO，多轮进一步提升。
- 作者结论：ExpDis在相同wall-clock预算下显著优于DAPO，并带来更好的pass@k scaling与正确解的多样性；同时，DAPO(+novelty)在RND激励下整体性能下降。
