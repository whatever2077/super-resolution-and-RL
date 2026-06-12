# 2026-06-13 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning
- **论文链接**: http://arxiv.org/abs/2606.13680v1
- **作者**: Zilin Xiao, Qi Ma, Chun-cheng Jason Chen, Xintao Chen, Avinash Atreya, Hanjie Chen, Vicente Ordonez
- **原始摘要**: Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then fine-tunes the policy model via reinforcement fine-tuning methods with retrieved analogous demonstrations, so the model learns to leverage reasoning traces under verifiable outcome rewards. We further analyze the diversity of retrieved contexts and find that reasoning-aware retrieval surfaces complementary solution strategies that provide distinct reasoning scaffolds for individual problems. Across challenging mathematical reasoning benchmarks, RA-RFT consistently outperforms standard reinforcement fine-tuning methods. For example, it improves AIME 2025 average@32 accuracy by 7.1 and 2.8 points over GRPO for Qwen3-1.7B and Qwen3-4B respectively -- suggesting that reasoning-aware retrieval is a complementary axis of improvement and orthogonal to advances in reward design or training curricula.

### GPT总结
#### 文章内容
这篇工作关注传统语义相似度检索对复杂推理任务不适配的问题，并提出通过“类比”来选取对推理真正有用的外部示例。核心思路是用“gold-relevance distillation”训练一个“面向推理效用”的检索器，再在强化微调（RLVR）中用检索到的类比推理轨迹作为示范，让策略在可验证奖励下学会利用外部推理脚手架。结论是该框架在数学推理基准上稳健提升，并且与奖励设计或训练日程正交；例如在 AIME 2025 上，Qwen3-1.7B 与 Qwen3-4B 相比 GRPO 的 average@32 分别提升 7.1 和 2.8 个点。

#### 方法
- 数据与外部库：给定带可验证答案的训练集 D 与包含问题-推理轨迹对的外部语料 C（轨迹由教师模型生成）。
- 阶段一（Gold-relevance distillation）：用评审模型（例如 GPT-4o）对每个“目标问题—候选轨迹”对进行判定，生成二值标签以度量“结构性/可迁移的推理相关性”，而非表层语义相似。
- 阶段二（检索器训练）：基于上述标签进行对比学习，训练“面向推理的检索器”，使其按“预期推理收益”而非语义重合度来排序候选上下文。
- 阶段三（强化微调）：在 RLVR 框架下，用检索到的类比示范作为上下文进行策略优化，直接以答案可验证性作为奖励信号；对比基线为标准 RFT/GRPO 类方法。
- 推理时是否仍进行检索增强：文中未明确说明。

#### 创新点
- 将检索目标从“语义相似”重定义为“推理效用”，通过 gold-relevance distillation 让评审模型为“可迁移推理结构”打标签。
- 将“面向推理的检索”与 RLVR 有机结合为后训练流程，使模型在可验证奖励下学会利用外部推理轨迹；与奖励设计、优化器或课程学习正交。
- 经验分析显示该检索能暴露“互补的解决策略”，为单个问题提供差异化的推理脚手架，而非单一模式的示例检索。
- 利用教师模型生成的细粒度推理轨迹作为类比示范，面向“策略迁移”而非答案模仿的监督信号。

#### 实验结论
- 任务与数据：面向“数学推理”类基准进行评测；除 AIME 2025 外的具体数据集名单与规模文中未明确说明。
- 主要结果：相较标准强化微调（如 GRPO），RA-RFT 一致性更好；在 AIME 2025 average@32 上，Qwen3-1.7B 与 Qwen3-4B 分别较 GRPO 提升 7.1 与 2.8 个点。
- 作者结论：面向推理的检索提供与奖励/课程正交的增益维度，且能检索到多样且互补的推理策略，从而稳定提升复杂推理性能。
