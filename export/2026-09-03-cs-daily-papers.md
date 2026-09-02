# 2026-09-03 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Lightweight Interpretable RGB-Guided Hyperspectral Super-Resolution under Real Cross-resolution Misalignment
- **论文链接**: http://arxiv.org/abs/2609.01060v1
- **作者**: Mohamad Jouni, Aurélien Godet, Mauro Dalla Mura
- **原始摘要**: Compact snapshot hyperspectral cameras provide rich instantaneous spectral measurements for ground-level machine vision, but at lower spatial resolution than standard RGB cameras. RGB-guided hyperspectral super-resolution (HSR) addresses this limitation by transferring spatial detail from a high-resolution RGB guide to a low-resolution hyperspectral image (HSI). These dual-camera systems are typically in a horizontal rig geometry, requiring cross-camera image alignment due to different fields of view. However, residual misregistration can inject spurious high-frequency details. Existing learned unaligned-fusion methods are usually trained for a fixed spectral support and spatial scale factors and can be computationally demanding, limiting their flexibility across sensors. We propose a lightweight and interpretable RGB-guided HSR framework combining cross-modal flow alignment with model-based Gram-Schmidt orthogonalization fusion. The method first warps the RGB guide onto the HSI grid, then estimates an energy-based confidence weight map by measuring local alignment reliability. This map is then used both in a weighted least-squares spectral regression and in a gated fusion between the super-resolved estimate and an HSI-preserving estimate. Unlike existing learned methods, the proposed framework has a low computational footprint and supports VIS-NIR spectral supports and scale factors without retraining. Experiments on the Real benchmark show that the proposed method improves reconstruction accuracy over learned fusion baselines while remaining substantially faster. On a 34-frame sequence acquired with our real RGB-HSI dual-camera setup, a reduced-resolution quantitative evaluation validates the method under genuine cross-sensor radiometric, noise, and geometric differences, while native-resolution qualitative results demonstrate deployment on the full 51-band VIS-NIR acquisition.

### GPT总结
#### 文章内容
本文关注双相机RGB引导的HSR在真实近景场景中存在视差与残余错配时易引入伪高频的问题。作者提出一个轻量、可解释的框架：先用跨模态光流将RGB对齐到HSI网格，再基于能量的置信度图进行加权光谱回归与门控融合，从而在不精确对齐下稳健利用RGB细节。方法无需针对特定光谱范围或放大倍数重新训练，支持VIS-NIR与多尺度，实验在Real基准与自建双相机序列上显示较已学方法更准且更快。

#### 方法
- 预处理与代理构建：将LR HSI上采样为H↑，通过Ψ(·)从H↑投影生成HSI→RGB代理Ψ(H↑)。
- 跨模态对齐：用CMF/CrossRAFT估计HSI→RGB稠密光流FH→R，并反向重采样RGB得到对齐的Rw；由采样网格获得几何有效性掩码M。
- 置信度估计：基于局部一致性构建能量项（如与低通Rw的RGB代理残差Ergb或结构一致性残差Estr，以及光流循环一致性Ecyc），结合M得到空间置信图C∈[0,1]。
- 置信加权回归：在GSA框架中以C作为空间权重进行加权最小二乘光谱回归，得到RGB引导的SR估计X̂G。
- 门控融合：以C门控融合X̂G与HSI保真估计H↑，形成X̂ = H↑ + C ⊙ (X̂G − H↑)，在不可信区域保留HSI，在可信区域注入RGB细节。全流程为模型驱动推理，无需针对新光谱带或放大因子再训练。

#### 创新点
- 将跨模态光流对齐与Gram-Schmidt orthogonalization (GSA)模型式融合有机结合，面向未对齐RGB引导HSR的轻量可解释方案。
- 提出非学习式、能量驱动的置信度图，同时用于加权光谱回归与门控细节融合，抑制错配导致的伪高频。
- 显式处理视差/遮挡：通过有效性掩码M与循环一致性/结构一致性线索评估局部可靠性。
- 跨传感器可迁移性：无需针对不同VIS-NIR光谱支持或缩放因子再训练，计算开销低、部署灵活。

#### 实验结论
- 任务与数据：在Real基准上评测，并在自建RGB–HSI双相机（Ultris SR5与RPi HQ）34帧序列上做降尺度定量与原生分辨率定性验证。
- 核心结果：相较已学的未对齐融合基线，所提方法在重建精度上更优且速度更快；在51-band VIS-NIR获取上成功部署，超出现有31-band学习基线的设定。
- 指标与数值细节（如具体PSNR/SSIM、运行时等）文中未明确说明。

## 关键词：reinforcement learning

## The Rise of Verbal Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2609.01597v1
- **作者**: Kshitij Tayal, Arun Sharma, Genta Indra Winata, Anirban Das, Sambit Sahu
- **原始摘要**: Natural language is emerging as a primary feedback channel for improving language agents, capable of conveying intent, preferences, and causal structure in forms interpretable by both humans and modern language models. We call this paradigm Verbal Reinforcement Learning (VRL) and offer the first unified account of it. We organize the field around a single axis, \textit{when} verbal feedback takes effect in an agent's lifecycle and \textit{what} it modifies, yielding three pillars: (1) \textbf{Language as Grounding Signal}, where language defines the task itself by specifying goals, states, and reward structures; (2) \textbf{Language as Deliberative Feedback}, where natural language guides reasoning at test time without the need to update model parameters; (3) \textbf{Language as Learning Signal}, where language-based feedback shapes model parameters through training. Within each pillar, we synthesize representative work, distinguish key subcategories of approaches, and outline the distinct role language plays in shaping agent behavior. Together, this taxonomy shows how verbal reinforcement is reshaping agent development, while also defining the challenges and opportunities for building more capable and aligned agents.

### GPT总结
#### 文章内容
论文提出“Verbal Reinforcement Learning (VRL)”范式，将自然语言作为一等反馈信号来改进语言智能体，系统性地统一并梳理该领域。核心思路是按语言反馈在智能体生命周期中“何时生效、修改何物”这一单一轴组织方法，提出三大支柱：Language as Grounding Signal、Language as Deliberative Feedback、Language as Learning Signal。作者综述代表性工作、划分子类别并总结各自挑战与机遇，结论认为口头强化正在重塑智能体开发并为更强、更对齐的智能体提供新路径。

#### 方法
- 三支柱框架与时间轴划分：按语言反馈生效时机与作用对象组织方法——Grounding（问题定义期；修改任务/状态/动作/奖励）、Deliberation（推理期；引导中间推理与输出、不改参数）、Learning（训练期；将语言转为训练信号更新权重）。
- Grounding：用语言定义目标、以文本刻画状态、解析指令到可执行动作、用语言生成或塑形奖励，对应映射MDP各要素，解决环境与任务规格化难题。
- Deliberation：在推理时利用自我反思/批评、工具与错误日志等语言信号迭代改进（如提示工程、链式思维、批评-修正循环）；通常对单次回合生效，可结合记忆扩展。
- Learning：将语言反馈压缩为可训练信号进行SFT、PPO、DPO等偏好优化，持久更新策略；强调信号抽取、过滤与对齐。
- 工作示例（代码智能体）：Issue文本定义目标（Grounding）；测试与报错提供口头/可读反馈驱动迭代修复（Deliberation）；成功/失败轨迹汇总为偏好数据做微调（Learning），展示同一语言信号在不同时间尺度的不同效应。并总结跨支柱挑战：Grounding gap/组合性、反馈质量/计算成本、信号压缩/过滤质量。

#### 创新点
- 提出首个系统性的VRL三支柱分类法，以“时间与作用”而非来源/模态组织方法，统一Grounding、推理期自我反思与训练期偏好优化等分散线索。
- 明确语言在MDP各组件中的功能定位与“持久性”差异，给出工作化范例，澄清相同语言信号在不同阶段产生的本质不同效果。
- 提炼跨支柱的共性挑战与研究议题（如反馈质量评估、信号压缩与过滤、组合泛化），为构建稳健、可对齐的VRL代理提供路线图。
- 相较既有综述仅聚焦单一侧面（如LLM自纠错或语言条件策略），本工作从功能角色维度提供统一框架并覆盖更广应用版图。

#### 实验结论
- 论文为综述型工作，不报告新的实验或专属数据集；文中未明确说明 自家实验任务与数据集。
- 汇总的早期证据显示语言反馈可显著提升性能，例如：Shinn et al. (2023) 通过 verbal self-reflection 在 HumanEval 达到 91% pass@1；Ouyang et al. (2022) 显示 1.3B 偏好模型可超越 175B GPT-3 基线。
- 作者结论：VRL是有效的监督通道，正重塑智能体开发流程，同时存在反馈质量、Grounding gap、信号压缩/过滤等开放问题与机会。
