# 2026-07-03 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training
- **论文链接**: http://arxiv.org/abs/2607.01232v1
- **作者**: Zijian Zhang, Rizhen Hu, Athanasios Glentis, Dawei Li, Chung-Yiu Yau, Hongzhou Lin, Mingyi Hong
- **原始摘要**: Reinforcement learning (RL) has become a central component of post-training large language models (LLMs), yet little is understood about how RL adaptation is distributed across transformer layers. Existing approaches typically update all model parameters uniformly, implicitly assuming that every layer contributes similarly to the gains obtained during RL post-training. In this work, we challenge this assumption through a systematic layer-wise study of RL training. Surprisingly, we find that training a single transformer layer can recover most of the gains achieved by full-parameter RL training, and in some cases even surpass it. To quantify this phenomenon, we introduce the quantity layer contribution, which measures the fraction of full RL improvement recovered by training a layer in isolation. Across seven models spanning two model families (Qwen3, Qwen2.5), three RL algorithms (GRPO, GiGPO, Dr. GRPO), and multiple task domains including mathematical reasoning, code generation, and agentic decision-making, we observe a remarkably stable pattern: RL gains are highly concentrated in a small subset of, and in many cases even a single, transformer layers. More strikingly, the same structural pattern consistently emerges: high-contribution layers concentrate in the middle of the transformer stack, while layers near the input and output ends contribute substantially less. The resulting layer rankings remain strongly correlated across datasets, tasks, model families, and RL algorithms.

### GPT总结
#### 文章内容
- 论文关注RL后训练对LLM各Transformer层的作用分布，质疑“全层均等贡献”的隐含假设。核心思路是仅训练单层并冻结其余层，提出“layer contribution”度量单层可恢复的全参RL提升比例。
- 跨Qwen3与Qwen2.5两大家族、7个模型、3种RL算法（GRPO、GiGPO、Dr. GRPO）与多个任务域（数学推理、代码生成、Agentic决策）进行系统层扫，发现RL增益高度集中于少数、甚至单个中间层。
- 主要结论：中间层（约40%–60%深度）贡献最高，输入端与输出端层贡献显著更低；单层训练可恢复大部分全参RL增益，且在部分设置下甚至超越全参RL；基于层贡献的训练策略与分层集成可进一步优于标准全参RL。

#### 方法
- 定义“layer contribution”：在仅训练某一层、冻结其他层的设置下，该层单独可恢复的全参RL性能提升比例。
- 对各层逐一进行RL训练扫描，覆盖7个模型（Qwen3与Qwen2.5系列）、多任务域（数学推理、代码生成、Agentic），与三种RL算法（GRPO、GiGPO、Dr. GRPO）。
- 分析不同深度层的贡献分布并建立层排序，聚焦识别稳定的高贡献层（集中在网络深度的40%–60%）。
- 提出层感知训练策略：对高贡献层提高学习率，或仅选择这些层参与训练，以期在相同预算下获得更高增益。
- 通过训练多个“层专长”模型并进行集成，利用互补行为进一步提升性能。

#### 创新点
- 揭示RL后训练的结构性特征：增益并非在网络中均匀分布，而是集中于少数中间层，颠覆“全层均等更新”的普遍做法。
- 提出可量化的“layer contribution”指标，为RL增益的层级归因提供统一测度。
- 发现跨数据集、任务、模型家族与RL算法的层贡献排序高度一致，表明该结构模式具有稳健的普适性。
- 基于层贡献的简单层感知训练（提高高贡献层学习率或仅训练高贡献层）在多设置下稳定优于全参RL；层专长模型的集成进一步带来增益。

#### 实验结论
- 任务与模型：覆盖数学推理、代码生成与Agentic决策；模型横跨Qwen3与Qwen2.5系列，共7个模型；RL算法包括GRPO、GiGPO与Dr. GRPO。
- 关键发现：高贡献层稳定出现在网络中部（约40%–60%深度），输入/输出端层贡献较低；仅训练单层即可恢复大部分全参RL增益，部分情况下还可超越全参RL。
- 在Qwen3系列（NuminaMath-CoT与数学基准）上，基于层贡献指导的策略（提高高贡献层学习率或仅训练这些层）相较全参RL进一步取得+43%/+27%/+32%的额外提升（相对于全参RL总增益的相对比例）；训练仅高贡献层在三个规模上均优于全参RL。
