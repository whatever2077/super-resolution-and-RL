# 2026-10-07 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Multi-Task Partially Supervised Learning for Super-Resolution and Semantic Segmentation on Earth Observation data
- **论文链接**: http://arxiv.org/abs/2610.06389v1
- **作者**: Hoàng-Ân Lê, Minh-Tan Pham, Solange Lemai-Chenevier, Daniel Greslou
- **原始摘要**: Super-resolution and semantic segmentation are known to benefit one another, especially in the Earth observation context. However, learning both tasks in a joint model often requires both task annotations, which is impractical and expensive. In this paper, we study the multi-task partially supervised learning paradigm for both tasks, where each example is assumed to have only a single-task annotation. To that end, we examine two multi-task architectural variations, the sequential and shared variants, and then propose a hybrid variant and a re-projection loss to benefit from the shared representation and enforce image quality of super-resolution when training with semantic segmentation. Experiments show favorable results compared to the SOTA sequential variant. Source code will be published at https://github.com/lhoangan/munera.

### GPT总结
#### 文章内容
- 论文针对Earth Observation场景中同时进行超分辨率（SR）与语义分割（Seg）的高标注成本问题，提出在“部分监督”设定下的多任务学习框架，每个样本只含单一任务标注。
- 核心思路是比较“共享式”和“顺序式”架构，并提出结合二者优势的“混合式”架构与re-projection损失，在使用分割标注训练时约束SR子网的图像质量。
- 主要结论是相较于SOTA的顺序式方法（SS-guided SR与SR4IR），所提共享与混合方案在ISPRS数据上的SR质量（PSNR/SSIM）更优。

#### 方法
- 采用部分监督多任务学习：每个训练样本仅有SR或Seg标注，通过共享编码器联合优化两任务。
- 架构层面：共享编码器为B=23的RRDB blocks；SR解码器为2次上采样+2个卷积层；Seg解码器来自HRNet-W18（含多分辨率融合与head）。
- 比较三种架构变体：共享式（单编码器双解码）、顺序式（SR→Seg，对应[2],[4]）、混合式（共享表示与顺序耦合的折中方案）。
- 引入re-projection损失：在仅有Seg标注样本上训练时，通过重投影一致性约束SR子网的重建质量（具体形式文中未明确说明）。
- 评价遵循Clean Super-Resolution策略：从HR合成LR，使用隐藏5×5 Gaussian核（σ∈[0.8,3.0]、椭圆率r_ellip∈[1.0,1.5]、旋转θ∈[0,2π]）、降采样步长s∈{2,3,4}与高斯噪声N(0,σ^2), σ∈[0.001,0.05]（其余退化细节与损失项的具体公式文中未明确说明）。

#### 创新点
- 在Earth Observation场景下，将生成式任务（SR）与判别式任务（Seg）置于“部分监督多任务”框架，免除每样本双任务标注的刚性需求。
- 设计混合式多任务架构，兼具共享表示与顺序耦合优势，并提出re-projection损失在无SR标注时仍能约束重建质量。
- 使用RRDB共享编码与HRNet-W18分割解码的组合，面向遥感图像的跨尺度与多分辨率特性进行结构适配。
- 在CSR设定下进行评测，增强对未知退化核与噪声条件的鲁棒性（相较既有顺序式方法的对比设定）。

#### 实验结论
- 任务：超分辨率与语义分割的联合学习；数据：ISPRS 2D semantic labeling（Potsdam用于SR训练，Vaihingen用于Seg训练与测试）及专有Pléiades数据。
- 在Vaihingen测试集SR效果上，相比SS-guided SR [4]与SR4IR [2]的顺序式方法，所提共享/混合方案取得更高PSNR/SSIM：Ours(shared) SSIM 0.804/PSNR 25.491；Ours(hybrid) SSIM 0.804/PSNR 25.446；[4] 0.746/23.890；[2] 0.694/22.830。
- 结论：所提部分监督多任务框架与混合式架构在SR质量上优于SOTA顺序式方案；关于Seg定量指标与更多训练细节文中未明确说明。

## 关键词：reinforcement learning

## Base Models Can Reason By Taking a Cue From Training Data
- **论文链接**: http://arxiv.org/abs/2610.06851v1
- **作者**: Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min, Alexei A. Efros
- **原始摘要**: In this paper, we study how training data creates associations between the tokens at the start of a base model's response and the reasoning behavior that follows. First, we demonstrate that fixing particular starting token cues makes a base model's performance competitive with that of its reinforcement learning (RL)-trained counterparts on math and coding. For instance, the cue ".\n\nOkay" raises Olmo-3-7B's MATH-500 pass@1 accuracy from 42% to 78%, while "Alright," raises Qwen3-14B's from 72% to 87%. Second, RL makes these cues more likely, while fixing them recovers much of its performance gain over the base model. Third, we trace the reasoning effects of token cues to the training data. We perform causal data interventions to turn an arbitrary word, such as "chicken", into an effective reasoning cue, or remove an existing cue's effect. A similar edit makes the prompt instruction "Think duck duck goose" as effective as "Think step by step" at eliciting reasoning. We also find that the hidden state representations induced by different cues correlate with different document types from the training set. Finally, we extend our study of token cues with a case study in language model safety, finding that different cues elicit distinct refusal and compliance behaviors that correspond to different types of training data.

### GPT总结
#### 文章内容
本文研究训练数据如何在基座模型输出开头的少量“起始token线索”（token cues）与后续推理行为之间建立关联。核心思路是仅固定回答的前两枚token即可显著改变后续生成分布，从而在数学与代码任务上逼近甚至匹敌对应的强化学习（RL）后训练模型；并通过因果性数据编辑验证这些线索与训练语料的可塑关联。主要结论：特定起始线索（如“.\n\n Okay”“Alright,”）可将基座模型的推理性能提升到接近RL水平；RL提高了这些线索在开头出现的概率；通过编辑训练数据可创造或移除有效线索，线索触发的隐表示与训练集中不同文档类型相关；线索还可调控安全拒答与顺从行为。

#### 方法
- 固定输出开头两枚token，比较p(y|x,c)下的生成与原始无约束生成，评估对推理正确率的影响；以MATH-500、GSM8K、AMC 23、AIME 2024、HumanEval为基准。
- 基座模型与其RL后训练对应体对比：测量RL后首若干位置的策略变化与起始线索概率提升；在RL rollouts中强制线索以验证收敛与样本效率变化（具体RL算法文中未明确说明）。
- 因果数据干预：从中间检查点继续训练，在100B-token中期数据混合中替换训练出现（如将“okay”替为“chicken”，将“step by step”替为“duck duck goose”），检验新线索是否获得推理触发能力。
- 表示与数据来源分析：比较不同线索诱发的隐藏状态与训练集中不同文档类型的相关性，追溯线索—行为映射的语料来源。
- 安全性案例研究：用“I’m sorry”“Okay,”“.\n\n Okay”等不同线索触发不同的拒答/顺从模式，并与Instruct、Think-SFT变体对照。

#### 创新点
- 提出“最小干预”的线索驱动框架：仅两枚起始token即可将基座模型推理性能推至接近或匹配RL模型，揭示能力与行为表达的解耦。
- 以因果数据编辑直接操控线索—推理关联，既能将任意词（如“chicken”）条件化为有效推理线索，也能消除既有线索效应。
- 连接训练分布与模型表示：展示线索诱发的隐藏表示与特定文档类型相关，并发现RL主要在首位置偏好上重塑策略而非创造全新能力。
- 将线索视为安全行为的“行为选择器”，系统展示不同线索对拒答与有害合规的差异化调控。

#### 实验结论
- 任务与模型：在Olmo-3-7B与Qwen3-14B上评估MATH-500、GSM8K、AMC 23、AIME 2024与HumanEval（32次rollouts）。在Olmo-3-7B上，固定“.\n\n Okay”使MATH-500 pass@1由42%升至78%，与其RL变体的75%相当；跨五基准提升为1.4×–1.9×，多处匹敌或超越RL-Zero。Qwen3-14B用“Alright,”使MATH-500由72%至87%，数学类任务达RL水平，而HumanEval与无线索相当。
- RL与线索：RL提升了有效线索在开头出现的概率，策略更改集中在前几个输出位置；预置线索可回收RL的大部分性能增益；在RL训练中强制线索可在更少更新步内达到相近精度（具体数值文中未明确说明）。
- 数据干预与可迁移性：在中期数据中将“okay”替为“chicken”后，“.\n\n Chicken”在MATH-500上的准确率由2.4%升至37.2%；将“step by step”替为“duck duck goose”后，“Think duck duck goose”与“Think step by step”同样有效；不同线索的表示与训练文档类型相关；在安全场景中，“I’m sorry”倾向广泛拒答，“Okay,”降低拒答并增加不安全合规，而“.\n\n Okay”更具选择性地拒答，趋近Instruct与Think-SFT的行为。
