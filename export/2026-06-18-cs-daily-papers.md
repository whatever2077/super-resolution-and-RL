# 2026-06-18 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification
- **论文链接**: http://arxiv.org/abs/2606.18249v1
- **作者**: Wujian Peng, Lingchen Meng, Yuxuan Cai, Xianwei Zhuang, Yuhuan Yang, Rongyao Fang, Chenfei Wu, Junyang Lin, Zuxuan Wu, Shuai Bai
- **原始摘要**: Unified Multimodal Modeling aims to integrate visual understanding and generation within a single system. However, existing approaches typically rely on two disparate visual tokenizers, which splits the representation space and hinders truly unified modeling. We propose UniAR, a unified autoregressive framework where a single discrete visual tokenizer serves as the key bridge between understanding and generation, enabling a shared context in which the model can directly interpret its own generated visual tokens without additional re-encoding. UniAR adapts a pretrained vision encoder with multi-level feature fusion and a lookup-free bitwise quantization scheme, preserving both high-level semantics and low-level details while scaling the effective visual vocabulary at minimal cost. Building on this, the unified autoregressive model adopts parallel-bitwise-prediction to jointly predict spatially grouped, multi-level visual codes, substantially reducing visual sequence length and accelerating generation. Finally, a diffusion-based visual decoder operates on discrete visual tokens to decode high-fidelity images. Through large-scale pre-training, followed by supervised fine-tuning and reinforcement learning, UniAR achieves state-of-the-art performance on image generation and image editing while remaining competitive on multimodal understanding benchmarks. The project page is available at https://sharelab-sii.github.io/uniar-web.

### GPT总结
#### 文章内容
- 论文解决统一多模态建模中“理解-生成分裂”的问题：现有方法常用两套视觉tokenizer，导致表示空间割裂与无法共享上下文。  
- 核心思路是用单一离散视觉tokenizer桥接理解与生成，结合多层级特征融合与lookup-free比特量化，配合统一自回归(next-token)建模与并行比特级预测、以及仅依赖视觉token的DiT解码器实现高效高保真图像生成。  
- 作者结论：在图像生成与图像编辑上达到SOTA，同时在多模态理解上保持竞争力。

#### 方法
- 视觉表征与离散化：在预训练视觉编码器上进行多层级特征融合，兼顾高层语义与低层细节；采用lookup-free bitwise quantization，将特征映射为二进制向量（如64-bit可表示2^64种代码），无需显式码本。  
- 统一自回归范式：单模型按next-token预测同时处理理解、生成与编辑，生成过程中无需在理解端对图像重新编码，实现共享上下文。  
- 并行比特级预测：对每个2×2空间网格同时预测多层级视觉二进制码，显著缩短视觉序列，达到32×视觉压缩并加速生成。  
- 视觉解码器：采用DiT-based扩散解码器，仅以离散视觉token为条件并支持分辨率上采样；生成1024×1024图像时仅需预测256个视觉token。  
- 训练流程：三阶段训练（大规模预训练→有监督微调→强化学习）；训练自回归模型时冻结视觉tokenizer与解码器，解码器仅在RL阶段用于图像解码以计算奖励。

#### 创新点
- 单一共享视觉tokenizer统一理解与生成，模型可直接解释自身生成的视觉token，无需额外重编码，实现真正的“shared context”。  
- Lookup-free比特量化替代传统码本式VQ，指数级扩展有效词表（如64-bit→2^64），成本低且保留细节与语义。  
- 并行比特级预测对空间分组的多层级代码联合建模，显著减少序列长度并提升生成速度。  
- 多层级特征融合的tokenizer设计，同时满足判别与生成需求；DiT-based解码器仅依赖视觉token并支持分辨率上采样，利于高分辨率重建。

#### 实验结论
- 任务与结果：在图像生成（含文本渲染与指令跟随）和图像编辑上达到SOTA，在多模态理解基准上表现具有竞争力。  
- 数据集与指标：文中未明确说明具体数据集与评价指标的名称与数值。  
- 效率与可扩展性：并行比特级预测带来32×视觉压缩；在1024×1024分辨率仅需256个视觉token，显示出高效生成特性。
