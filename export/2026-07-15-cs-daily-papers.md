# 2026-07-15 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation
- **论文链接**: http://arxiv.org/abs/2607.11886v1
- **作者**: Runhui Huang, Qihui Zhang, Zhe Liu, Yu Gao, Jie Wu, Hengshuang Zhao
- **原始摘要**: In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. We use the average image-conditioned prompt log-likelihood as the reward, directly reusing the MLLM's pretrained image-text alignment ability without preference labels, reward-model fine-tuning. We further introduce Self-SpectraReward, a special case for unified multimodal models where the policy's own understanding branch serves as the reward model for its generation branch, forming a closed-loop self-improving framework without external reward models or external knowledge. Extensive experiments validate SpectraReward through a broad image-generation RL study covering two diffusion models, three RL algorithms, nine reward MLLM backbones from four MLLM families spanning 4B to 235B parameters, and five out-of-distribution text-to-image benchmarks. Results show that both SpectraReward and Self-SpectraReward significantly and consistently improve generation performance and outperform prior MLLM-derived reward training methods. Further analysis reveals that larger reward MLLMs are not always better, while Self-SpectraReward can match or surpass much larger external reward models, suggesting that reward-policy alignment is a key factor for effective image-generation RL. Project Page: https://huangrh99.github.io/SpectraReward/

### GPT总结
#### 文章内容
论文聚焦于文本到图像生成的强化学习阶段中“高效、可靠且无需偏好标注”的奖励建模难题，提出SpectraReward：通过对生成图像进行一次图像条件、教师强制的前向计算，将原始提示可被“读回”的程度（提示token对数似然均值）作为确定性奖励。论文进一步提出Self-SpectraReward，在统一多模态模型（UMM）内以策略自身的理解分支为生成分支提供奖励，形成无外部依赖的闭环自提升。大规模实验覆盖两种扩散模型、三种RL算法、九个MLLM骨干（4B–235B）及五个OOD基准，表明两种方法均显著、稳定提升生成质量并优于既有MLLM派生奖励训练方法。分析显示更大的奖励MLLM不一定更好，且自奖励可匹配/超越更大外部模型，奖励-策略对齐是关键因素。

#### 方法
- 将生成图像与原始文本提示输入冻结的预训练MLLM，以图像为条件对提示执行一次教师强制的自回归前向，得到按token的对数似然谱（semantic spectrum）。
- 以提示token的图像条件对数似然均值作为标量奖励，直接作为文本到图像RL的回报信号；无需偏好标签、无需奖励模型微调。
- 将该训练无关的奖励接入标准扩散式生成策略的RL流程，适配多种RL算法，训练中奖励随生成质量稳步提升。
- Self-SpectraReward：在UMM中使用同一模型的理解分支为其生成分支打分，利用共享的tokenizer、视觉编码器与预训练分布获得更强的奖励-策略对齐，实现无外部模型/知识的闭环自改进。
- 系统比较不同规模与家族的奖励MLLM，观察并利用规模带来的非单调收益，强调选择与策略对齐更佳的模型。

#### 创新点
- 奖励定义新颖：将“图像能否读回提示”的图像条件语言建模对数似然作为奖励，将预训练MLLM的图文对齐能力直接转化为确定性、免训练、免标注的奖励信号。
- 提出Self-SpectraReward，在统一多模态模型内部实现“自理解→自生成”的闭环强化学习，无需外部奖励模型或外部知识。
- 广泛而系统的实验设置：跨两种扩散模型、三种RL算法、九个奖励MLLM骨干（覆盖四个家族，4B–235B）与五个OOD基准，实证分析规模效应与奖励-策略对齐。
- 相比直接打分或问题分解式零样本奖励，避免评判标定与工程复杂度，凸显“对齐性”而非“规模”是有效图像生成RL奖励的关键。

#### 实验结论
- 任务与设置：文本到图像生成的RL后训练；在SD3.5-M与BAGEL等策略上结合三种RL算法进行评测；奖励MLLM涵盖九个骨干、四个家族，参数范围4B–235B。
- 核心结果：SpectraReward与Self-SpectraReward在五个OOD基准上均显著且一致地优于基线与既有MLLM派生奖励方法；更大奖励模型并非总是更优，Qwen3-VL-30B-A3B是外部奖励中的最佳，而Self-SpectraReward（BAGEL自奖励）可超过所有外部模型。
- 其他发现：训练过程中SpectraReward与复杂场景的可见生成质量同步上升；具体RL算法名称与超参数在提供文本中未明确说明。
