# 2026-07-11 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Real-World Blind Super-Resolution via Feature Matching with Implicit High-Resolution Priors
- **论文链接**: http://arxiv.org/abs/2202.13142v3
- **作者**: Chaofeng Chen, Xinyu Shi, Yipeng Qin, Xiaoming Li, Xiaoguang Han, Tao Yang, Shihui Guo
- **原始摘要**: A key challenge of real-world image super-resolution (SR) is to recover the missing details in low-resolution (LR) images with complex unknown degradations (e.g., downsampling, noise and compression). Most previous works restore such missing details in the image space. To cope with the high diversity of natural images, they either rely on the unstable GANs that are difficult to train and prone to artifacts, or resort to explicit references from high-resolution (HR) images that are usually unavailable. In this work, we propose Feature Matching SR (FeMaSR), which restores realistic HR images in a much more compact feature space. Unlike image-space methods, our FeMaSR restores HR images by matching distorted LR image features to their distortion-free HR counterparts in our pretrained HR priors, and decoding the matched features to obtain realistic HR images. Specifically, our HR priors contain a discrete feature codebook and its associated decoder, which are pretrained on HR images with a Vector Quantized Generative Adversarial Network (VQGAN). Notably, we incorporate a novel semantic regularization in VQGAN to improve the quality of reconstructed images. For the feature matching, we first extract LR features with an LR encoder consisting of several Swin Transformer blocks and then follow a simple nearest neighbour strategy to match them with the pretrained codebook. In particular, we equip the LR encoder with residual shortcut connections to the decoder, which is critical to the optimization of feature matching loss and also helps to complement the possible feature matching errors. Experimental results show that our approach produces more realistic HR images than previous methods. Codes are released at https://github.com/chaofengc/FeMaSR.

### GPT总结
#### 文章内容
本文针对真实场景盲超分（未知退化导致细节缺失、噪声与压缩等复杂失真）难以稳定复原真实纹理的问题，提出在离散特征空间而非像素空间进行恢复的FeMaSR。核心思路是先用VQGAN在HR图像上预训练得到“隐式HR先验”（离散特征码本Z与解码器G），再将LR特征通过最近邻匹配映射到HR码本并由G解码重建；同时以语义正则提升码本的语义一致性，并通过多尺度残差捷径稳定特征匹配的优化与纠错。实验显示，相比Real-ESRGAN+与SwinIR-GAN等方法，FeMaSR能生成更真实、伪影更少的HR纹理。

#### 方法
- 两阶段框架：Stage I 以HR补丁预训练VQGAN得到HR Priors（离散codebook Z与decoder G）；Stage II 将盲SR转化为特征匹配问题，把LR编码得到的特征映射到Z中的HR代码并交由G解码重建。
- 语义正则：在VQGAN预训练中引入基于VGG19感知特征的L2正则，增强语义与码本条目的相关性，提升重建质量与纹理语义一致性。
- LR编码器：采用若干Swin Transformer blocks提取LR特征，利用简单的nearest neighbour策略在Z中选取对应代码；以特征匹配损失监督从LR特征到HR代码的映射。
- 残差捷径：在多尺度上为LR编码器到解码器引入残差短连接，缓解量化带来的优化困难，提供直接梯度通路并补偿可能的匹配误差。
- 训练/推理：训练时固定HRP（Z与G）优化LR编码器的特征匹配；推理时对LR图像编码→码本最近邻匹配→经G解码输出HR图像。具体损失细节与训练数据设置文中未明确说明。

#### 创新点
- 将盲超分重构从图像空间转为离散潜特征空间的“特征匹配”任务，利用预训练的隐式HR先验（VQGAN codebook+decoder）替代不稳定的像素空间GAN合成或外部参考图像。
- 在VQGAN中加入语义正则（VGG19感知特征L2），显著增强码本的语义感知能力，推动更真实且语义一致的纹理生成。
- 设计带多尺度残差捷径的LR编码器，与固定解码器协同，缓解量化与匹配带来的优化难题并对匹配误差进行补偿。
- 采用Swin Transformer编码+nearest neighbour匹配的简洁决策机制，在复杂退化下实现稳健映射到HR codebook。

#### 实验结论
- 任务：真实场景盲超分（未知下采样、噪声、压缩等复合退化）。
- 数据集与评价指标：文中未明确说明。
- 结果与结论：与Real-ESRGAN+、SwinIR-GAN等相比，FeMaSR在视觉上恢复更真实的细节纹理（如细小毛发）且伪影更少；总体实验表明所提出的特征匹配+隐式HR先验框架能生成更逼真的HR图像。

## 关键词：reinforcement learning

## Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?
- **论文链接**: http://arxiv.org/abs/2606.26428v2
- **作者**: Tyler Ga Wei Lum, Kushal Kedia, C. Karen Liu, Jeannette Bohg
- **原始摘要**: Multi-fingered robots promise the speed and dexterity of human hands, yet challenging problems such as precise assembly have remained out of reach. These tasks are contact-rich, making data collection for imitation learning difficult, and sparse-reward, making direct exploration with reinforcement learning (RL) intractable. Consequently, prior work has made progress by structuring the problem with specialized grippers, tool attachments, and environment fixtures. In this work, we argue that before a robot can perfect precise assembly, it must first learn to play. We further ask the question: what factors in the process of learning to play matter for precise assembly? We propose Play2Perfect, an RL framework for task-agnostic pretraining through play on diverse objects and goals, which is then perfected on precise assembly. The goal of play is to acquire reusable manipulation priors, such as grasping, in-hand reorientation and pose reaching. Finetuning then adapts this general prior to assembly, focusing exploration on the final contact-rich, high-precision interactions needed for success. We systematically study key design choices in play pretraining, including object diversity, training objective, trajectory diversity, and goal precision. We show that our prior is 33x more sample-efficient than RL training from scratch, even when provided with dense, multi-stage rewards. We demonstrate zero-shot sim-to-real transfer, achieving 60% success on tight insertions with only 0.5 mm contact clearance, and over 50% success on long-horizon multi-part assembly and screwing.

### GPT总结
#### 文章内容
这篇论文针对多指灵巧手在“精密装配”中稀疏奖励与接触复杂导致的学习困难，提出先通过“玩耍”学通用操纵，再微调到装配的两阶段思路。核心是用目标条件RL在多样物体与随机6D目标姿态上预训练，获取可迁移的抓取、指间重排与姿态到达等操纵先验，再在CAD定义的稀疏奖励装配环境中微调聚焦最后的高精接触。结论显示：相较从零开始的RL（即便有密集分阶段奖励），该先验使学习效率提升33x，并在真实机器人上实现0.5 mm间隙紧配合插入60%成功率、长时程多件组装与拧螺纹超50%成功率；关键迁移因素是促使手内操纵的6D目标、对象/轨迹多样性和高精目标。

#### 方法
- 预训练：在仿真中对多种基本体对象设定随机6D目标姿态，用目标条件RL学习通用操纵先验（含抓取、手内重排、6D位姿控制）。
- 微调：在由CAD派生的装配环境中使用稀疏终态奖励进行RL微调，将探索集中于最终对位、接触与插入等高精交互。
- 任务与硬件：22-DoF Sharpa五指手+7-DoF KUKA iiwa 14，任务涵盖 Tight-Insertion（T形销不同间隙）、Assemble-Beam（Fabrica）、Screw-Leg（FurnitureBench），为适配灵巧手对部件进行了3×尺度放大。
- 对比基线：从零开始的RL包含Sparse与Dense两种（后者加入抓取/抬升及10个路径点跟踪的密集 shaping）。
- 设计选择消融：系统评估对象多样性（10/100/1000）、训练目标（6D vs 仅平移/仅旋转）、轨迹多样性、目标精度（1 cm/5 cm/10 cm）。

#### 创新点
- 提出“Play2Perfect”两阶段框架：任务无关的玩耍预训练获取灵巧操纵先验，再用稀疏奖励微调到精密装配，避免大量人工示教与密集奖励工程。
- 首次系统化量化“玩耍预训练”对精密装配迁移的关键因素，指出6D手内控制、对象/轨迹多样性与高精目标是效果最敏感的环节。
- 在强对比下证明：相较从零开始（含密集分阶段奖励与10 waypoints），玩耍先验实现数量级（33x）样本效率与更稳健的多指抓持策略。
- 展示零样本 sim-to-real 到真实装配（0.5 mm紧配合、长时程多部件组装与旋拧），验证泛化与可落地性。

#### 实验结论
- 任务与设置：Tight-Insertion、Assemble-Beam（Fabrica）、Screw-Leg（FurnitureBench），仿真评估500次随机初始位姿；真实实验每任务10次。Scratch基线含Sparse与Dense（抓取/抬升+10 waypoints）两版。
- 关键结果：Play2Perfect在2–5小时内解出全部任务；Scratch两版24小时无成功（简化支撑版任务中Dense需>100小时），Play2Perfect仅4小时达同等成功率，达成33x加速；在外力10N下，Dense基线成功率降至约20%并进一步归零，而Play2Perfect在最大扰动下仍>75%。
- 设计选择：最佳迁移来自6D位姿目标、1000对象的更高对象多样性、更多样的随机轨迹以及更严格的目标精度（1 cm）；仅平移/仅旋转目标、较低多样性或粗目标精度均显著削弱下游装配表现。其他训练细节（具体RL算法、感知输入）文中未明确说明。
