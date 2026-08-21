# 2026-08-22 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Swift-Image: Exploring the Performance Frontier of Compact Unified Image Generation Models
- **论文链接**: http://arxiv.org/abs/2608.20334v1
- **作者**: Taihang Hu, Zhao Wang, Zuan Gao, Tao Liu, Hao Yan, Zhengze Xu, Yuhang Yu, Yongchao Du, Xingjian Wang, Jun Zheng, Qinye Zhou, Zhengrui Chen, Chao Lin, Yefeng Shen, Zhengtao Wu, Ge Wu, Xiaoli Xu, Denghui Yang, Huayu Zhang, Mingzhou Zhang, Mengting Chen
- **原始摘要**: We present Swift-Image, a compact unified model for text-to-image generation, single-image editing, and multi-image editing. Our goal is to explore how far a relatively small visual generator can be pushed through systematic training engineering under a constrained computational budget. Swift-Image adopts an efficient 6B single-stream DiT and a progressive training pipeline that evolves from broad semantic coverage to higher resolution, stronger visual quality, and unified generation-editing supervision. For post-training, we employ parallel expert reinforcement learning followed by multi-teacher on-policy distillation to alleviate interference among heterogeneous objectives. We further decouple high-level reasoning from pixel-level rendering with a Prompt Enhancer that translates user requests into generator-aligned visual specifications. For efficient deployment, structural pruning and few-step distillation produce 3B and accelerated variants. Swift-Image achieves leading aggregate performance among evaluated open-source models with only 6B parameters and 243K GPU training hours; the compressed 3B model incurs nearly no loss, while few-step distillation further improves aggregate editing performance with substantially fewer sampling steps. Our study also summarizes practical lessons for architecture, data curriculum, post-training, prompt enhancement, and model compression.

### GPT总结
#### 文章内容
本文探讨在受限算力预算下，如何通过系统性的训练工程将相对小型的统一图像生成模型推向性能边界。作者提出Swift-Image：基于6B参数的单流DiT骨干，统一支持text-to-image、单图编辑与多图编辑，并通过渐进式训练、并行专家强化学习与多教师on-policy蒸馏提升与统一多目标能力冲突。还引入Prompt Enhancer，将高层意图解析与像素渲染解耦；在部署侧通过结构化剪枝与少步采样蒸馏得到3B与加速变体。实验显示该6B模型在开源模型中取得领先的综合指标，用时243K GPU小时；3B压缩几乎无损，少步蒸馏在显著减少采样步数下进一步提升编辑综合性能。

#### 方法
- 统一多模态扩散骨干：采用单流并行Transformer（DiT），以Qwen3-VL-8B作为条件编码器（输入System Prompt、0-N张参考图与指令），连接三层隐藏表征并映射到扩散空间；像素级参考通过FLUX.2 AE编码并线性投影；不将VLM的图像token传入DiT以控制序列长度。
- 高效并行块与稳定化：每个块并行计算MHA与SwiGLU-MLP，支持算子融合，推理提效约10%；共享的时间步调制网络提供scale/shift与零初始化门控；使用4D-RoPE于[T,H,W,L]，并在T轴以偏移10区分多图索引以缓解多图编辑拷贝伪影；规范化采用QK端RMSNorm、其余LayerNorm与Sandwich Norm，调制门用Tanh约束，所有投影与调制层无bias。
- 渐进式统一训练：沿分辨率、任务复杂度、数据质量三轴的课程学习；先以低分辨率T2I起步，从256px到512px，再引入编辑数据，避免分辨率与任务分布同时突变；首500K步侧重规模与语义覆盖，随后进行SFT与持续预训练。
- 后训练优化：采用并行专家强化学习对不同目标进行专门化，再以多教师on-policy distillation整合，缓解多目标干扰与分布漂移；具体强化学习算法与奖励设计文中未明确说明。
- 推理与部署：Prompt Enhancer在必要时将用户请求重写为与生成器对齐的视觉规范（引用文本使用字符级分词以提升文本渲染）；通过结构化剪枝得到3B模型，并以少步蒸馏获得加速变体。

#### 创新点
- 在仅6B参数下，通过单流并行DiT与共享调制设计，实现统一生成-编辑框架与高效推理（约10%提效），展示紧凑模型的性能上限。
- 提出“并行专家RL + 多教师OPD”的后训练范式，用于缓解统一多目标（生成/编辑/文本渲染/布局等）间的相互干扰。
- 设计Prompt Enhancer解耦意图理解与像素渲染，提升复杂指令、文本排版与多参考编辑的可控性。
- 在多图编辑中采用4D-RoPE与时间轴偏移构建图像索引先验，减少同位拷贝伪影；系统性课程学习将分辨率提升与任务异质化解耦，稳定训练。

#### 实验结论
- 在综合指标上，Swift-Image于评测的开源模型中取得领先，整体分数为三项公开编辑基准与作者自建基准的平均；具体基准名称与数值文中未明确说明。
- 仅以243K GPU training hours完成训练的6B模型达到领先综合表现；通过结构剪枝得到的3B模型几乎无性能损失。
- 少步蒸馏在显著减少采样步数的同时，进一步提升了编辑类任务的综合表现；具体采样步数与速度提升比例文中未明确说明。
