# 2026-06-11 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## SRT: Super-Resolution for Time Series via Disentangled Rectified Flow
- **论文链接**: http://arxiv.org/abs/2606.07605v2
- **作者**: Jufang Duan, Shenglong Xiao, Yuren Zhang
- **原始摘要**: Fine-grained time series data with high temporal resolution is critical for accurate analytics across a wide range of applications. However, the acquisition of such data is often limited by cost and feasibility. This problem can be tackled by reconstructing high-resolution signals from low-resolution inputs based on specific priors, known as super-resolution. While extensively studied in computer vision, directly transferring image super-resolution techniques to time series is not trivial. To address this challenge at a fundamental level, we propose Super-Resolution for Time series (SRT), a novel framework that reconstructs temporal patterns lost in low-resolution inputs via disentangled rectified flow. SRT decomposes the input into trend and seasonal components, aligns them to the target resolution using an implicit neural representation, and leverages a novel cross-resolution attention mechanism to guide the generation of high-resolution details. We further introduce SRT-large, a scaled-up version with extensive pre-training, which enables strong zero-shot super-resolution capability. Extensive experiments on nine public datasets demonstrate that SRT and SRT-large consistently outperform existing methods across multiple scale factors, showing both robust performance and the effectiveness of each component in our architecture.

### GPT总结
#### 文章内容
本文面向时间序列超分辨率（TSSR）难以直接沿用图像SR先验与建模的问题，提出SRT框架。核心思路是先将低分辨率序列分解为trend与seasonal两部分，利用隐式时间函数（implicit time function, ITF）对齐到目标时间分辨率，再通过“解耦的rectified flow”双路径生成残差高频细节，并以cross-resolution attention（CRA）引导细节重建。作者同时给出大规模预训练版本SRT-large，实现零样本超分辨率。在9个公共数据集与多倍率设置上，SRT/SRT-large相较现有方法取得一致领先，并能更忠实地重构高分辨率细节。

#### 方法
- 任务建模：正式区分sampled super-resolution (SSR) 与 aggregated super-resolution (ASR)，在统一框架内处理“欠采样补点”和“聚合值分解”两类难题。
- 结构流程：对输入序列进行趋势（trend）与季节（seasonal）分解；使用连续隐式表示的ITF将两路分量对齐至目标时间尺度，作为条件信号。
- 生成机制：为trend与seasonal分别训练独立的rectified flow，以速度场形式生成高分辨率残差细节，最后与对齐分量融合得到HR输出。
- 表征融合：在decoder-only的速度预测器中引入CRA，将跨分辨率条件有效注入以指导细节生成。
- 训练/推理：采用rectified flow范式进行条件生成与采样；具体损失细节、采样步数与训练超参文中未明确说明。SRT-large通过大规模预训练获得强零样本能力。

#### 创新点
- 将时间序列分解（trend/seasonal）与rectified flow解耦结合，分别建模慢变与周期性的高频残差，提升可解释性与生成质量。
- 提出ITF作为连续隐式神经插值器，实现从低分辨率到目标分辨率的统一对齐与条件构造。
- 设计CRA跨分辨率注意力，在速度场预测阶段高效融合多尺度条件信息，精准引导细节重建。
- 给出SRT-large的规模化预训练方案，显著增强跨数据集与零样本TSSR泛化能力。

#### 实验结论
- 数据与任务：在ETTh1/ETTh2/ETTm1/ETTm2、weather、PEMS-SF、MotorImagery、SelfRegulationSCP1/2共9个数据集、多个放大倍率下评测，覆盖SSR与更具歧义的ASR场景。
- 主要结果：SRT与SRT-large在点位与整体精度上均优于现有方法，并能更好重构尖峰/振荡等高频细节；消融验证了分解、ITF、CRA与双流rectified flow等组件的有效性。具体评价指标与数值增益文中未明确说明。
- 额外发现：SRT-large展现出强零样本超分辨率能力，对跨域与未见数据具有稳健泛化。

## 关键词：reinforcement learning

## ARM: An AutoRegressive Large Multimodal Model with Unified Discrete Representations
- **论文链接**: http://arxiv.org/abs/2606.11188v1
- **作者**: Junke Wang, Xiao Wang, Jiacheng Pan, Xuefeng Hu, Feng Li, Jingxiang Sun, Chaorui Deng, Zilong Chen, Yunpeng Chen, Kaibin Tian, Matthew Gwilliam, Hao Chen, Danhui Guan, Kun Xu, Weilin Huang, Zuxuan Wu, Haoqi Fan, Yu-Gang Jiang, Zhenheng Yang
- **原始摘要**: This paper introduces ARM, a discrete representation-based AutoRegressive Model that unifies image understanding, generation, and editing within a next-token prediction framework. ARM is built on three efforts: first, we train a discrete semantic visual tokenizer that maps images into compact token sequences. Our tokenizer is supervised with multiple objectives that jointly promote semantic discriminability, language alignment and faithful reconstruction, thereby supporting diverse tasks in a shared latent space. With this, we train a 7B autoregressive model over large-scale text and image token sequences, seamlessly developing vision-language perception and generation capabilities. Finally, to further improve preference-aligned behavior for text-to-image generation and instruction-guided editing, ARM applies reinforcement learning (RL) to optimize task-level objectives such as visual quality, instruction adherence, and edit consistency. Surprisingly, the results show that RL not only substantially improves performance on the target tasks (e.g., raising WISE overall from 0.50 to 0.56, GEdit-Bench-EN G_O from 5.75 to 6.68), but also induces cross-task synergy between text-to-image generation and editing. Collectively, these findings highlight autoregressive modeling, when paired with strong representations and preference optimization, as a scalable foundation for multimodal intelligence. Code: https://github.com/wdrink/ARM.

### GPT总结
#### 文章内容
ARM旨在用统一的离散视觉表示，将图像理解、生成与编辑纳入同一自回归(next-token)建模框架，解决理解与生成偏好的表示不一致与系统割裂问题。核心思路是：训练具备语义判别、语言对齐与高保真重建能力的离散语义视觉tokenizer；在大规模文本-图像离散序列上训练7B自回归模型；再通过RL偏好优化对齐生成与编辑的任务级目标。主要结论是：RL显著提升T2I与编辑性能（如WISE从0.50→0.56、GEdit-Bench-EN G_O从5.75→6.68），并产生跨任务协同而不削弱理解能力；整体在MMMU 40.2、POPE 87.3、GenEval 0.86、WISE 0.56、GEdit-Bench-EN 6.68达成SOTA或具竞争力结果。

#### 方法
- 训练离散语义视觉tokenizer，联合优化语义可判别、语言对齐与重建目标；实现细节含：SigLIP2-SO400M-512编码器、FSQ量化器（L_i=2, 1≤i≤16，约65K码本）、两层轻量投影；配套像素级DiT解码器（24层）与从FLUX.1 [dev]初始化的潜空间扩散解码器，以及与冻结的0.5B Qwen2.5进行语言对齐。
- 构建统一7B自回归模型（初始化自Qwen2.5-7B），新增视觉token预测头，在大规模交错的文本-图像token序列上进行next-token训练，实现理解、生成与指令编辑一体化。
- 动态分辨率生成/编辑：在文本提示中插入shape tokens，显式指定离散token网格的高宽。
- 四阶段训练：预训练（2.5T多模态tokens）→持续训练（再2.5T，提升分辨率与交错数据占比）→监督微调（0.2B高质量指令数据）→RL偏好优化（VeRL/GRPO），T2I用GPT-o3打分对象/属性/空间关系，编辑用GPT-4.1考察指令遵循、非目标区域保持与整体质量。
- 数据构成：文本-only（含数学/代码）、图像到文本（含OCR、图表、grounding）、文本到图像（精选高质对、少量来自现有T2I的合成样本）、交错多模态（视频序列与网页文档）、公开编辑数据集；RL提示来自Share-GPT-4o与HQ-Editing-6000等。

#### 创新点
- 用单一离散视觉表示统一理解与生成/编辑，缓解以往多编码器/多潜空间导致的体系割裂与推理开销。
- 提出“语义判别+语言对齐+高保真重建”的多目标tokenizer训练范式，结合FSQ量化与扩散解码器，兼顾识别语义与重建细节。
- 将多任务统一为自回归的next-token预测，在同一序列空间中处理文本与视觉token，并通过shape tokens实现可变分辨率。
- 采用基于偏好优化的RL（GRPO，经由VeRL实现）并以GPT-o3/GPT-4.1为奖励模型，显著提升T2I与编辑且产生跨任务正迁移，同时不损伤多模态理解。

#### 实验结论
- 多模态理解：在MMMU 40.2、POPE 87.3，显著优于使用离散表示的既有方法，显示理解能力稳定且强健。
- 文生图与编辑：GenEval 0.86、WISE 0.56（相较扩散基线具领先水平），GEdit-Bench-EN G_O 6.68；RL将WISE由0.50提升至0.56、将GEdit由5.75提升至6.68。
- 结论：偏好对齐的RL在T2I与编辑间带来协同增益，且未观察到对理解性能的不利影响；统一自回归建模配合强表征与偏好优化可作为可扩展的多模态智能基础。
