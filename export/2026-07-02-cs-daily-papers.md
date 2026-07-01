# 2026-07-02 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Reinforcement Learning with Metacognitive Feedback Elicits Faithful Uncertainty Expression in LLMs
- **论文链接**: http://arxiv.org/abs/2606.32032v1
- **作者**: Gabrielle Kaili-May Liu, Avi Caciularu, Gal Yona, Idan Szpektor, Arman Cohan
- **原始摘要**: Metacognition is a critical component of intelligence that describes the ability to monitor and regulate one's own cognitive processes. Yet LLMs exhibit systemic deficiencies in key metacognitive faculties: they hallucinate with high confidence, fail to recognize knowledge boundaries, and misrepresent their internal uncertainty--undermining trustworthiness and reliability. Since monitoring task performance and adapting behavior accordingly are central to metacognition, we posit that models capable of accurately judging their own performance are better positioned to improve it. We operationalize this idea via two novel mechanisms: reinforcement learning with metacognitive feedback (RLMF), a paradigm to refine completion rankings during preference optimization based on the quality of a model's self-judgments of performance, and metacognitive data selection, which uses similar self-judgments to identify high-value training examples, outperforming naive active learning. We apply these innovations to the problem of faithful calibration (FC), a task that is itself fundamentally metacognitive: the goal is to align expressed with intrinsic uncertainty, difficult even for frontier LLMs. We adopt a two-stage, decoupled approach, first using these methods to calibrate the faithfulness of models' self-reported confidence scores, then mapping to natural, context-adaptable linguistic uncertainty via targeted output editing. Extensive experiments show RLMF achieves generalizable, state-of-the-art FC on diverse tasks while preserving accuracy. Further, RLMF surpasses standard RL by up to 63% while enhancing models' ability to assess and express their own capability limits. This positions RLMF as a promising paradigm to enhance LLM metacognition toward improved abilities and alignment, and suggests metacognitive performance as an effective RL signal to overcome limits of prior intrinsic feedback methods.

### GPT总结
#### 文章内容
- 论文针对LLMs在元认知能力上的系统性缺陷（如高置信幻觉、无法识别知识边界、误表内部不确定性），提出使模型“忠实表达不确定性”的Faithful Calibration（FC）框架。
- 核心思路是将“自我评估的准确性”作为训练信号：提出RLMF（reinforcement learning with metacognitive feedback）与“元认知数据选择”，先校准数值置信度的忠实性，再通过定向重写将其映射为自然语言不确定性表达。
- 主要结论：RLMF在多任务、多模型上实现SOTA的FC并保持准确率与事实校准，较标准RL最高提升达63%，并提升模型识别与表达自身能力边界的能力；在人评中对比最强基线取得平均96%胜率。

#### 方法
- RLMF：在偏好优化的RL训练中，不仅奖励输出质量，还按“模型自我评估是否准确”对每个completion的优势项进行缩放（metacognitive advantage scaling），从而重排并强化更“自知”的输出。
- 元认知数据选择：为候选训练样本打分（基于模型自评表现好坏），同时选取高分与低分两端样本，提供互补监督信号，优于朴素的主动学习式“只挑错题”。
- 两阶段FC：Stage 1 用RLMF+数据选择校准模型“句级自报数值置信度”的忠实性；Stage 2 将数值分映射到相应hedge表达，并对回答做定向重写以保证连贯与语境适配。
- 解耦设计与推理机制：Stage 1一次训练后固定；Stage 2可按用户偏好与场景灵活映射/重写，无需重复昂贵RL训练。
- 相比仅用“内在置信度”作奖励的先前方法，该方法直接利用“自评质量”作为更高层的元认知反馈信号强化策略更新。

#### 创新点
- 提出RLMF与metacognitive advantage scaling：用“自我判断的正确性”而非原始置信度作为RL信号，直接优化模型的元认知能力与输出排序。
- 提出元认知数据选择：基于自评难度信号的双端样本挑选机制，优于朴素/主动学习式仅选低表现样本的策略。
- 建立首个覆盖“数值+语言”两种不确定性表达的端到端FC管线，并通过两阶段解耦实现对用户偏好的可适配性与跨任务泛化。
- 将数值置信度通过定向重写映射为自然、语境感知的语言hedge表达，提升人机对齐与可用性。

#### 实验结论
- 在多种LLM与10个任务（覆盖6+领域）上评测，尽管仅在单一数据集上训练，方法仍实现可泛化的SOTA FC，同时保持任务准确率与factual calibration不受损。
- 与标准RL相比，RLMF带来最高63%的提升，并显著增强模型对自身能力上限的评估与表达能力。
- 人类评测显示：在多任务、多偏好设置下，语言不确定性表达的多样性、自然度、助益性与语境适配性方面，相比最强基线平均取得96%胜率。
