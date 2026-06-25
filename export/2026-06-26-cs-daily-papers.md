# 2026-06-26 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
- **论文链接**: http://arxiv.org/abs/2606.26091v1
- **作者**: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
- **原始摘要**: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.

### GPT总结
#### 文章内容
- 论文关注“Self-Distillation with Sampled Demonstrations (SDSD)”在提高pass@1的同时可能带来的隐性代价：输出多样性下降，导致pass@k曲线变平，更多采样不再带来覆盖提升。
- 作者理论上证明：SDSD的最优策略不是按奖励加权，而是将基模型分布按“期望的点式条件互信息（PCMI）”对学生轨迹与示范之间的相容性进行倾斜，从而放大已占优模式的概率。
- 与理想的on-policy RL（如GRPO）对等正确解保持概率比不同，SDSD会对与示范更相似的解给予更强强化，压制同样正确但非典型的策略。
- 在图路径寻优与科学问答上，SDSD的平均性能匹配或超过RL，但功能与语义多样性显著降低，在需要多样策略的OOD设置中失败。

#### 方法
- 框架：同一模型兼任teacher与student；teacher在上下文中接收一个已验证正确的示范（通常为采样的正确轨迹），对student生成的每个token提供密集反馈。
- 训练信号：teacher在条件化示范下对每个student rollout打分，越接近示范的轨迹获更强强化；对比RL（如GRPO），二元验证器对所有正确解给予相同奖励。
- 理论刻画：推导SDSD最优策略为对基分布按“期望PCMI”进行倾斜，区别于按奖励保持等正确解概率比的理想on-policy RL；该倾斜会放大既有概率差距。
- 多样性度量：提出功能多样性（pass@k曲线的提升速率）与语义多样性（高层策略差异，例如不同图路径或证明思路）；证明token-level entropy无法反映两者。
- 具体损失形式、架构与超参数：文中未明确说明。

#### 创新点
- 提出并证明SDSD最优策略为PCMI倾斜基分布的理论结果（Prop. 2），系统阐释了为何与示范相容的模式被过度强化，区别于标准RL的奖励驱动机制。
- 揭示“示范条件化+自评分”引入的复合偏置链条，解释pass@k变平和输出多样性下降的根源。
- 引入可精确计量语义多样性的受控图路径寻优任务，展示语义多样性对OOD泛化的预测性，并指出仅用token-level entropy不足。
- 在科学问答与图任务上系统对比SDSD与GRPO，强调平均准确率与多样性/泛化之间的权衡。

#### 实验结论
- 任务与数据：受控图路径寻优任务与科学问答基准（Feng et al., 2024）；对比基线包括GRPO。
- 结果：SDSD在pass@1上匹配或优于RL，但pass@k曲线更平、功能与语义多样性显著降低；token-level entropy无法捕捉该差异。
- 结论：多样性受损使SDSD在需要多策略的OOD设置中失败；相比之下，RL展现更陡峭的pass@k提升与更好的覆盖能力。
