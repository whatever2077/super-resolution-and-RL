# 2026-07-08 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Weak-to-Strong Generalization via Direct On-Policy Distillation
- **论文链接**: http://arxiv.org/abs/2607.05394v1
- **作者**: Shiyuan Feng, Huan-ang Gao, Haohan Chi, Hanlin Wu, Zhilong Zhang, Zheng Jiang, Bingxiang He, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR) is a powerful recipe for improving language-model reasoning, but it is expensive to repeat on every new strong model because the target model must generate many rollouts during training. As models scale, post-training itself becomes a bottleneck. We study a weak-to-strong alternative: run RL on a smaller model where rollouts are cheaper, then reuse what that RL run learned to improve a stronger target model. Directly distilling the post-RL weak teacher is not enough, because the teacher's final policy mixes useful RL gains with the limitations of the smaller model. We propose Direct On-Policy Distillation (Direct-OPD), which transfers the teacher's RL-induced policy shift instead. Direct-OPD compares the post-RL teacher with its own pre-RL reference and treats their log-ratio as a dense implicit reward for the student. In plain terms, the checkpoint pair tells us which actions RL made the weak model more or less likely to take, and Direct-OPD applies that signal on the stronger student's own on-policy states. This directly reuses the weak model's RL supervision signal without training an explicit reward model or running sparse-reward RL on the target model. Empirically, Direct-OPD consistently leverages weaker teachers to improve stronger target models; notably, it boosts Qwen3-1.7B from 48.3% to 62.4% on AIME 2024 in just 4 hours on 8 A100 GPUs. It outperforms step-matched direct RL and enables the sequential composition of multiple policy shifts. Our results show that RL outcomes can be reused across model scales as implicit reward signals, not merely as final models to imitate.

### GPT总结
#### 文章内容
该工作针对RLVR在大模型上昂贵且需大量on-policy rollouts的痛点，提出一种弱带强的替代路径：先在小模型上做RL，再把RL学到的“改变量”迁移到更强学生模型。核心思路是对比弱教师RL前后策略，使用两者log概率之差作为稠密隐式奖励，在学生自身on-policy状态上进行蒸馏，并以KL项锚定学生初始策略，避免直接模仿弱教师最终策略的容量上限。实验表明，Direct-OPD可稳定把小模型RL的收益迁移到更强学生上：例如将Qwen3-1.7B在AIME 2024上从48.3%提升到62.4%，仅用8×A100约4小时，并优于步数匹配的直接RL。作者结论是：RL的结果可作为跨尺度可复用的隐式奖励信号，而不只是供模仿的终态策略。

#### 方法
- 构造教师成对检查点：以弱模型RL前策略π_Tref与RL后策略π_T之对比，定义策略迁移信号为log概率差（policy shift），表示RL使哪些动作更可能或更不可能。
- 将该policy shift视为稠密隐式奖励，作用于学生模型在其自身on-policy采样到的状态-动作上，训练目标包含对学生初始策略π_S的KL正则锚定，稳定优化。
- 不训练显式奖励模型，也不在目标学生上运行稀疏奖励RL；直接把小模型RL所蕴含的监督信号转化为可迁移的reward-like指导。
- 相比标准OPD模仿教师最终策略，Direct-OPD只迁移“由RL引起的改变”，减少弱教师固有限制对更强学生的负迁移。
- 支持顺序组合多个policy shift，以累积不同小模型RL阶段的收益；文中指出该信号在一定响应长度与KL范围内更能对齐验证准确率。

#### 创新点
- 从“模仿弱教师最终策略”转向“迁移弱教师RL诱导的策略改变量”，解耦RL收益与小模型容量上限，适配弱带强场景。
- 将教师RL前后log概率差解释为稠密隐式奖励，并证明其在KL正则化RL目标下与原始奖励等价，避免训练显式RM与在大模型上跑RL。
- 在学生自身on-policy分布上施加隐式奖励并KL锚定初始策略，提高稳定性与适用性；无需高teacher–student top-k重合，能跨“思维模式”迁移。
- 计算经济性与可组合性：支持多次policy shift顺序叠加；在步数匹配下优于直接在大模型上做RL。

#### 实验结论
- 任务与模型：在AIME 2024上验证；学生包括Qwen3-1.7B、Qwen3-4B、R1-Distill-7B；教师对包括R1-Distill-1.5B → JustRL-1.5B与Nemotron-1.5B → QuestA-Nemotron-1.5B。
- 关键结果：Direct-OPD使Qwen3-1.7B从48.3%升至62.4%（8×A100约4小时），跨学生均取得增益，甚至当学生初始性能已高于教师时仍有效；对比下，标准OPD在R1-Distill-7B（56.7）与JustRL-1.5B（51.3）场景中会将性能拉低至约50。与步数匹配的直接RL相比，弱上RL+Direct-OPD在准确率与计算成本上更优。
- 作者结论：Direct-OPD将小模型RL的成果以隐式奖励形式跨尺度复用，较大幅度降低大模型后训练成本，并在计算效率上接近或优于直接大模型RL（如与需至少一周32×A100的Polaris相比）。
