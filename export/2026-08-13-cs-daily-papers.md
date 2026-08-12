# 2026-08-13 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory
- **论文链接**: http://arxiv.org/abs/2607.07581v3
- **作者**: Shaoming Pan, Chenchuhui Hu, Leon Axel, Meng Ye
- **原始摘要**: Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference views acquired from the same subject and intermediate SR results as the memory. Our method uses coarse-to-fine contextual matching to establish robust correspondence between low-resolution target and reference/memory images under spatial misalignment. A learnable patch-wise dynamic feature aggregation module predicts content-adaptive mixture weights for each local patch, effectively fusing dynamic information while suppressing unreliable feature transfers. The intermediate SR results stored in the memory bank ensure slice-to-slice consistency for the super-resolved 3D volume. Experiments on the WHS cardiac MRI dataset under two reference protocols, orthogonal-plane views and long-axis chamber views, demonstrate consistent improvements over baselines at 4x and 8x upsampling factors.Code is available at https://github.com/030108ming/STRMSR

### GPT总结
#### 文章内容
该文面向临床心脏MRI在层厚方向分辨率低的问题，提出通过参考视图与记忆引导的层厚超分辨框架STRMSR，以重建各向同性高分辨3D体数据。核心思路是利用来自同一受试者的HR参考视图做跨视角细粒度匹配，并以中间SR结果作为“记忆”在切片间传播；通过粗到细的上下文匹配与按块的动态特征聚合，实现在空间失配下的稳健细节迁移并抑制不可靠传递。实验在WHS数据集、两种参考协议（orthogonal-plane views与long-axis chamber views）及×4/×8放大下，优于多种基线。作者还表明引入记忆有助于提升切片间一致性与体数据连贯性。

#### 方法
- 特征提取：采用双分支Transformer编码器（Swin-based RSTB），目标LR与下采样参考LR分支共享权重、HR参考单独分支；对LR在层厚轴中心复制上采样，构建多尺度金字塔(s=1,2,3)以对齐与匹配。
- 粗到细上下文匹配（CFCM）：在最粗层以块级全局搜索（多膨胀归一化相关）定位候选，再在局部以3×3补丁级余弦相似度做致密匹配；用置信度加权folding将HR参考特征精确扭曲到目标对齐，并通过最近邻传播与半径局部搜索在更细层级迭代细化对应关系。
- 按块动态特征聚合（PDFA）：对每个局部块学习内容自适应的混合权重，融合目标、扭曲后的HR参考以及记忆特征，抑制低置信度转移；配合Feature Aggregation Module与Dual-Path Residual Block进行重建与细化。
- 记忆机制：将中间SR结果存入memory bank，作为后续切片的参考以进行跨切片传播，借鉴视频目标分割中的记忆匹配思想，提升slice-to-slice一致性与体数据连贯性。
- 训练/推理细节（损失函数、优化器、数据划分等）：文中未明确说明。

#### 创新点
- 提出参考与记忆联合引导的层厚SR框架，将同受试者HR视图与中间SR结果共同用于跨视角与跨切片的信息迁移与约束。
- 设计粗到细的块到补丁级上下文匹配（CFCM），在存在空间失配时实现稳健对应关系估计，并在多尺度上逐级细化。
- 提出按块的动态特征聚合（PDFA），通过可学习的内容自适应混合权重融合参考/记忆信息，有效抑制不可靠特征转移。
- 引入记忆式跨切片传播机制以显式优化体数据的切片间一致性，将视频分割的记忆思想迁移到医学图像层厚SR。

#### 实验结论
- 任务与数据：在WHS心脏MRI数据集上，评估两种参考协议（orthogonal-plane views与long-axis chamber views）下的through-plane SR，放大倍数为×4与×8。
- 结果：在两种参考协议和两个放大倍率下均较多种基线方法取得一致性提升；具体定量指标与统计显著性文中未明确说明。
- 结论：参考与记忆联合引导提升了细节恢复与切片间一致性，改善了重建3D体的体素连贯性与诊断潜力。

## 关键词：reinforcement learning

## VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics
- **论文链接**: http://arxiv.org/abs/2608.11201v1
- **作者**: Bowei Liu, Zheng Lu, Yuhan Bian, Xinchen Zhang, Xingming Shui, Yuesheng Huang, Xuhuan Li, Zihao Liu, Yifan Yang, Jun Zhou, Xiu Li
- **原始摘要**: Recent advances in video generation models have significantly improved the realism of synthetic videos, blurring the boundary between generated and authentic content and raising concerns about misinformation. Existing MLLM-based detectors mainly rely on supervised fine-tuning or label-level reinforcement learning, where coarse supervision limits generalization to unseen scenarios and emerging video generators. To overcome these limitations, we are the first to introduce \textbf{meta-detection} into AI-generated video detection, enabling reliable forgery detection by jointly optimizing predicted labels and supporting evidence within reinforcement learning. This paradigm requires reliable evidence signals and effective mechanisms to integrate them into label-level optimization. Textual rationales provide semantic descriptions of forgery artifacts, but their generation and verification depend on external models, making supervision vulnerable to hallucinations and semantic biases. In contrast, temporal grounding provides more objective and verifiable evidence, as manipulated intervals can be precisely controlled during forgery construction. Based on this insight, we propose an automated data construction pipeline that generates paired real-fake videos by replacing temporal segments with boundary-frame-conditioned video generation models. Furthermore, we introduce \textbf{Evidence-Guided Reward Redistribution}, which performs evidence-aware credit assignment by redistributing rewards among label-correct responses according to evidence quality. This preserves reliable label supervision while encouraging detectors to acquire fine-grained and verifiable forgery localization capabilities. Extensive experiments demonstrate that \textbf{VidForensics-M1} effectively leverages verifiable temporal evidence to achieve robust and generalizable AI-generated video detection.

### GPT总结
#### 文章内容
该论文聚焦AI生成视频检测中监督信号粗糙导致的泛化差的问题，提出在强化学习中联合优化“标签判定+可验证证据”的meta-detection范式。核心思路是以可验证的时间定位（temporal grounding）替代易受偏置的文本解释作为证据，并通过自动化的片段替换数据生成管线获得精确的伪造时间区间监督。方法引入Evidence-Guided Reward Redistribution，在GRPO中依据证据质量在标签正确的响应间重新分配奖励，既保留标签监督又鼓励细粒度定位。实验显示VidForensics-M1能有效利用可验证的时间证据，提升鲁棒性与泛化性；具体数据集与数值指标文中未明确说明。

#### 方法
- Meta-detection建模：模型输出JSON，包含"answer"（real/fake）、"explanation"与"time_range"，训练时同时解析标签与证据以进行联合优化。
- 自动数据构建：从真实视频中选取时间段，提取boundary frames，用boundary-frame-conditioned视频生成模型重建该段并替换，形成成对的real/fake视频，精确记录操控的起止时间作为真值证据。
- 规则化时间证据反馈：以规则对齐的方式比较预测time_range与已知操控区间，得到客观可验证的证据质量信号，避免模型与评估器的语义偏置与幻觉。
- Evidence-Guided Reward Redistribution：在GRPO中对“标签正确”的候选按证据质量重分奖励，保持标签层监督同时促进习得可验证的伪造定位能力；仍包含必要的格式遵循奖励。
- 训练/推理：训练采用Group Relative Policy Optimization进行RLVR；推理阶段输出标签与对应的时间区间；是否使用SFT冷启动文中未明确说明。

#### 创新点
- 首次将meta-detection引入AI生成视频检测，在RL中联合优化预测正确性与证据可信度。
- 以规则驱动的temporal grounding取代模型生成的文本解释作为元监督信号，显著降低幻觉与语义偏置风险并可高效验证。
- 设计自动化的片段替换数据管线，利用boundary-frame-conditioned生成确保可控伪造并获得精确时间标注。
- 提出Evidence-Guided Reward Redistribution，实现证据感知的信用分配，与GRPO无缝结合以提升细粒度、可验证的定位能力。

#### 实验结论
- 作者报告了“广泛实验”验证：VidForensics-M1在AI生成视频检测中更鲁棒、具更强泛化，尤其在需要细粒度时间定位的场景中获益；具体数据集名称、规模与评测指标文中未明确说明。
- 相比依赖文本解释的监督，基于时间定位的证据反馈在训练中更稳定、可验证，减轻了reward hacking与外部评估偏置；定量提升幅度文中未明确说明。
- 总体结论：结合可验证的temporal grounding与证据引导的奖励重分配，可在不牺牲标签级准确性的前提下，促进检测器学习可解释、可验证的伪造定位能力。
