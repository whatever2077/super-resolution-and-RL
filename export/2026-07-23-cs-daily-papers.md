# 2026-07-23 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## ERank in Latent Space as an Image-Complexity and Richness Measure
- **论文链接**: http://arxiv.org/abs/2607.19315v1
- **作者**: Maksim Smirnov, Grigory Kononov, Anastasiia Linich, Egor Surkov, Egor Shvetsov
- **原始摘要**: We propose the effective rank (ERank) of the channel covariance of an image's deep feature map as a per-sample, label-free measure of visual richness, computed from a single forward pass through a frozen pretrained encoder. ERank counts how many decorrelated channel directions an image activates, and we characterize its properties, including its behavior under noise. Empirically, ERank orders images from plain to visually rich, correlates with codec bitrate, sharpness, and edge density, and correlates with human complexity annotations on IC9600 with $r = 0.72$. As a data-selection criterion, removing low-ERank samples improves super-resolution and removing high-ERank samples improves OCR, in both pretraining and finetuning, while selection does not help classification, segmentation, or denoising. ERank is thus a cheap richness signal, useful exactly when task difficulty is governed by input richness.

### GPT总结
#### 文章内容
本文提出用深度特征图通道协方差谱的有效秩（ERank）作为单样本、无标签的图像“视觉丰富度/复杂度”度量，只需一次前向通过冻结的预训练编码器即可得到。核心思路是在特征空间计算通道去相关程度：ERank为归一化特征协方差特征值熵的指数，解释为图像激活了多少互不相关的通道方向。实证表明，ERank与编码比特率、锐度、边缘密度有显著相关（r≈0.5），与IC9600的人类复杂度标注相关性达r=0.72；作为数据筛选信号，去除低ERank样本有利于超分辨率，去除高ERank样本有利于OCR，而对分类、分割与去噪无益。作者认为ERank是一种廉价而有效的“丰富度”信号，适用于任务难度受输入丰富度主导的场景。

#### 方法
- 使用预训练编码器f（ResNet-18 或 CLIP ViT-B/32）前向提取中间层特征f(ℓ)(I)，将HW×C特征图按空间位置展平为矩阵X∈R^{N×C}并逐通道去均值。
- 计算通道协方差Σ=(1/N)X^T X，取其特征值λi并归一化为pi=λi/∑jλj，定义ERank=exp(−∑i pi log pi)，分别在多层{1,2,3,4}或{2,5,8,11}上计算并取平均作为单图像分数。
- 将ERank作为无监督数据选择准则：按分数排序并在10–50%裁剪预算下去除低分或高分样本，再在剩余数据上进行预训练或微调，比较随机裁剪基线。
- 理论与性质：ERank取值∈[1, min(N,C)]，对各向同性缩放与通道旋转不变，连续可微；通道越去相关ERank越高；在叠加去相关噪声下单调上升，因而区分细节与噪声需依赖编码器表征。
- 选择在特征空间而非像素空间度量：特征维度更高、包含语义信息、对像素噪声更稳健，避免RGB通道维度过低与像素统计的混淆。

#### 创新点
- 将Effective Rank由“样本集层面/嵌入集层面”扩展到“单样本特征图通道/Token层面”，提出每幅图像的ERank作为标签无关的丰富度度量，与Vendi Score、RankMe等集合级方法区分开来。
- 提供一套清晰的性质刻画（不变性、连续性、与通道相关性的联系、噪声行为），使该度量可解释、可比较并可用于实际选择。
- 在多任务上系统评估ERank作为数据筛选信号，揭示其“任务依赖性”：对受输入丰富度影响显著的任务（×4超分、OCR）有效，而对分类、分割、去噪无益。
- 与像素域代理指标（如编码文件大小、锐度、边缘密度、UAE等）和人类标注进行对比，展示在IC9600上与人类复杂度的高相关性（r=0.72）。

#### 实验结论
- 相关性分析：在LAION子集与IC9600上，ERank与codec比特率、锐度、边缘密度相关约r≈0.5，与失真或色彩度相关极弱（r≈0.03），与IC9600人类复杂度标注相关r=0.72。
- 数据筛选：在DIV2K上用EDSR做×4超分时，去除低ERank样本可提升性能；在IIIT5K上用CRNN做场景文本识别时，去除高ERank样本更优；两者在预训练与微调两种设置下均优于随机裁剪。具体增益数值文中未明确说明。
- 消极结果：基于ERank的数据选择对MNIST/CIFAR-10分类（ResNet-18）、Pascal VOC分割（DeepLabV3–ResNet50）与DIV2K高斯去噪（σ=25, EDSR）无明显收益，支持其作为“输入丰富度主导”任务的专用信号这一结论。

## 关键词：reinforcement learning

## Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2607.19345v1
- **作者**: Lizhe Fang, Weizhou Shen, Tianyi Tang, Yisen Wang
- **原始摘要**: Large language models that generate step-by-step reasoning traces have achieved strong performance on complex tasks, and extending them to long-context settings has emerged as an important frontier. However, we identify a critical failure mode in this regime: \emph{repetitive copying}, where models extensively copy text from the input into their reasoning traces rather than productively solving the problem. We show that this behavior is pervasive across frontier long-context LLMs and intensifies with context length. By separating each prompt into task-relevant key evidence and irrelevant distractor context, we further show that the root cause is insufficient grounding: models copy from the prompt indiscriminately, and those that fail to focus on key evidence are far more likely to answer incorrectly. Motivated by this diagnosis, we propose GEAR (Grounding Evidence-Aware Reward), a reward shaping method that augments the accuracy signal with a grounding reward for overlap with key evidence and a distractor penalty for overlap with irrelevant context. To enable GEAR on natural-language data, we develop an automated pipeline that constructs evidence-annotated training data from arbitrary documents. We validate GEAR across multiple model scales and benchmarks, showing consistent improvements of up to +4.6 average points over standard RL with accuracy-based rewards, with larger gains at longer contexts, while also reducing repetitive copying and thinking length. Our findings suggest that, even as long-context evaluation shifts from simple retrieval toward complex reasoning, accurate grounding in relevant evidence remains an indispensable capability with substantial room for improvement.

### GPT总结
#### 文章内容
这篇论文聚焦长上下文推理中的“重复拷贝”失败模式：模型在思维链中大量复制输入文本而非真正解题，且随上下文变长而加剧。作者将根因归结为证据对齐不足：模型对提示无差别复制，不能聚焦关键证据时更易答错。为此提出GEAR（Grounding Evidence-Aware Reward），在准确率奖励上叠加“与关键证据的重叠奖励”和“与干扰内容的重叠惩罚”，并构建自动化证据标注数据管线。实验显示，GEAR在多规模模型与多基准上相对仅基于准确率的RL最高提升+4.6分，显著降低重复拷贝与思维长度，长上下文下收益更大，并可泛化到训练分布外4×更长的上下文。

#### 方法
- 数据构建：提出自动化管线，从任意自然语言文档中生成带“关键证据/干扰片段”标注的训练数据，用于区分任务相关与无关内容。
- 信号设计：以token级n-gram（文中使用3-gram）重叠率度量思维轨迹与“关键证据/干扰片段”的相似度，得到“证据对齐奖励”和“干扰惩罚”。
- 奖励塑形：总奖励 = 准确率 + α·证据重叠 − β·干扰重叠；默认α=0.1、β=0.3，通过简单n-gram统计即可实现，易于与现有RL集成。
- 训练范式：在GSPO等准确率驱动的RL基础上加入GEAR进行优化，适配Qwen3.5-9B/27B/35B-A3B等不同规模模型；推理阶段不改动生成流程，其他训练细节文中未明确说明。
- 消融设置：对α、β及n-gram大小进行消融；默认系数组合在32k场景下获得最佳平均分81.3，其他具体设置与数值文中未明确说明。

#### 创新点
- 从因果诊断上提出“证据对齐不足”是长上下文重复拷贝的根因，并通过“关键证据/干扰”分离进行量化验证。
- 设计简单、模型无关的奖励塑形：以n-gram重叠实现“正向对齐奖励+显式干扰抑制”的组合目标，区别于仅基于准确率的RL。
- 给出可扩展的证据标注自动化管线，使方法能在任意自然语言数据上落地训练，无需额外模型结构改造。
- 实证表明单独的“对齐奖励”（+Rground）会放大拷贝和冗长思维，只有加入“干扰惩罚”（GEAR）才能系统性抑制重复拷贝并提效。

#### 实验结论
- 现象与诊断：在七个前沿长上下文LLM上观察到重复拷贝普遍存在且随上下文变长而加剧；不能聚焦关键证据的样本显著更易答错。
- 量化收益：以Qwen3.5-35B-A3B（32k）为例，Ruler的3-gram重叠率由Base/GSPO/+Rground的36.9%/35.7%/36.6%降至+GEAR的27.0%，思维长度从2808降至2066（而+Rground升至5727）；在LongBench-v2中重叠率由24.9%降至22.6%，思维长度从4677降至3989（+Rground为6833）。
- 整体表现：GEAR在Ruler、LongBench-v2、Bcomp-LC、Graphwalks、AA-LCR等基准与Qwen3.5-9B/27B/35B-A3B三种规模下，相对仅准确率的RL平均提升最高达+4.6分，长上下文场景收益更显著，并能泛化至训练分布外4×的上下文长度。
