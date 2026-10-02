# 2026-10-03 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Convergent Plug-and-Play Image Restoration with Annealed Noise Levels
- **论文链接**: http://arxiv.org/abs/2609.32393v2
- **作者**: Samuel Hurault
- **原始摘要**: Plug-and-Play (PnP) methods solve imaging inverse problems by incorporating deep denoisers into iterative optimization algorithms. Although practical implementations often decrease the denoiser noise level $σ$ along iterations, most existing convergence analyses assume a fixed denoiser. In this work, we establish convergence guarantees for a broad family of Plug-and-Play algorithms with annealed noise level, spanning deterministic methods (RED--GD and PnP--PGD) and stochastic methods (SNORE, equivariant RED, and a variant of PnP--Flow). For each method, we identify an explicit, nonconvex objective associated with the terminal denoising level and prove asymptotic stationarity of the iterates with respect to this objective. Our analysis does not prescribe any decay rate for the noise schedule, and our assumptions cover both learned gradient-step denoisers and exact MMSE denoisers. Overall, our theoretical results bridge the gap between existing PnP convergence theory and the decreasing-denoising practices used by state-of-the-art image restoration methods. We empirically demonstrate the benefits of such schedules and illustrate the predicted convergence behavior on several imaging inverse problems, including inpainting, super-resolution, demosaicing and tomography.

### GPT总结
#### 文章内容
该文关注Plug-and-Play (PnP) 图像恢复在实践中常用“逐步降低去噪强度σ”的做法与现有“固定去噪器σ”的收敛理论之间的鸿沟。作者针对一类广泛的PnP/RED算法（含确定性与随机变体）提出收敛分析：将去噪器建模为梯度或近端映射，在σ按迭代单调递减并趋于终值ϵ>0时，为与终值ϵ对应的显式非凸目标证明迭代的渐近站点性。该分析不要求σ的特定衰减速率，适用于learned gradient-step denoisers与精确MMSE denoisers。实验表明，噪声退火带来稳定收敛行为与更佳重建效果，且覆盖inpainting、super-resolution、demosaicing与tomography等问题。

#### 方法
- 覆盖算法族：确定性RED–GD与PnP–PGD；随机型SNORE、Equivariant RED，以及与PnP–Flow相关的变体。
- 将去噪器视为保守映射：例如gradient-step denoiser Dσ = Id − ∇gσ；MMSE高斯去噪器由Tweedie’s formula保证保守性且可为近端算子；在Id − Dσ收缩条件下获得近端表示。
- 采用单调退火σk ↓ ϵ > 0的调度，不设具体衰减率；在算法特定步长假设下，证明对与终值ϵ关联的显式目标的渐近站点性。
- 算法结构为数据一致性步与去噪步交替；随机变体在该框架下引入随机化以实现同类保证。
- 实证实现中使用经微调的gradient-step或proximal型去噪器以匹配理论假设；训练细节与数据规模文中未明确说明。

#### 创新点
- 首次为广泛的PnP/RED确定性与随机算法在退火σ设置下提供统一的收敛保证，且不需规定噪声调度的衰减速率。
- 明确构造与终端σ（ϵ）对应的非凸变分目标，并证明迭代对该目标的渐近站点性，从而将实践中的退火策略纳入可解释的优化框架。
- 统一覆盖learned gradient-step denoisers与精确MMSE denoisers（含其近端表示）的理论分析，连接数据驱动先验与变分优化。
- 理论与实践对齐，系统展示退火在多类成像逆问题中的收益，弥合现有固定σ理论与实际退火使用之间的差距。

#### 实验结论
- 任务覆盖inpainting、super-resolution、demosaicing与tomography；在这些逆问题中，退火σ相较固定σ的基线呈现一致性提升，并符合理论预测的收敛行为。
- 以RED–GD的人脸图像inpainting示例为证：固定σ时，σ小（0.02）难以补齐大结构，σ大（1）过度平滑细节；几何退火σk: 5 → 0.014可达27.18 dB，优于多种固定σ设置（21.51/20.00/26.93 dB），体现从粗到细的重建优势。
- 使用的具体数据集、全面的量化指标与训练细节文中未明确说明；代码提供于https://github.com/samuro95/annealed-pnp。

## 关键词：reinforcement learning

## KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards
- **论文链接**: http://arxiv.org/abs/2610.02206v1
- **作者**: Pengfei Li, Naufal Suryanto, Sicheng Zhang, Muzammal Naseer
- **原始摘要**: LLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations. However, existing evaluations focus on knowledge-based assessments or end-to-end agentic tasks, and do not directly measure LLMs' ability to generate executable commands for real-world cybersecurity tools. This gap is critical because cybersecurity operations rely on strict command-line interfaces (CLIs), where minor syntax errors, incorrect flag--value bindings, or argument misordering can invalidate execution. We introduce KaliBench, a fine-grained benchmark and dataset for natural-language--to--CLI translation on Kali Linux, comprising 8,504 query--command pairs spanning 1,642 tools across 23 capability dimensions and 5 security phases. KaliBench is constructed via a manuscript-grounded pipeline with deterministic canonicalization and alias-aware evaluation, enabling precise and reproducible assessment of tool selection and argument construction. To ensure both semantic correctness and practical executability, we develop a multi-stage verification pipeline that combines LLM-based validation, sandboxed terminal execution, and human-in-the-loop refinement. Building on these fine-grained, deterministic signals, KaliBench further enables runtime-free verifiable rewards for training. Across three evaluation modes and 24 configurations of general-purpose and security-focused open-weight models, no open-weight model exceeds 42% exact-command accuracy in the unrestricted setting, highlighting the difficulty of accurate CLI-based cybersecurity tool use without explicit tool hints. We further show that supervised fine-tuning and reinforcement learning with verifiable rewards derived from KaliBench significantly improve an 8B model and achieve performance comparable to a 685B MoE model.

### GPT总结
#### 文章内容
该论文关注LLMs在网络安全流程中将自然语言意图准确翻译为可执行CLI命令的能力评估缺口，指出现有评测多为知识问答或端到端Agent任务，无法细粒度衡量真实工具的命令生成正确性。作者提出KaliBench，一个面向Kali Linux的细粒度基准与数据集，包含8,504条查询-命令对、覆盖1,642个工具、23个能力维度与5个安全阶段，基于手册驱动的数据构建、确定性规范化与别名感知评估，并辅以LLM校验、沙箱执行与人工复核的多阶段验证。实验显示，在无提示（unrestricted）设置下，开放权重模型的exact-command accuracy均不超过42%，而基于KaliBench的监督微调与用可验证奖励的强化学习显著提升了一个8B模型的表现，接近一个685B MoE模型。

#### 方法
- 手册驱动的数据生成：从Kali Linux官方文档抽取工具名、flag–value对与别名，作为结构化信号引导LLM生成自然语言到CLI的配对样本。
- 多阶段验证管线：依次采用LLM-based验证、沙箱终端执行与人工复核，确保语义正确性与可执行性，并进行去重与数据划分。
- 确定性规范化与别名感知评估：对工具选择、可选参数、位置参数以及参数顺序/语法进行可复现、细粒度打分。
- 评测与奖励设计：提供三种评测模式与细粒度、确定性的信号，构建无需运行时的runtime-free verifiable rewards。
- 训练策略：在训练划分上进行参数高效的监督微调（SFT）与基于可验证奖励的强化学习（RL），从而提升命令生成能力。

#### 创新点
- 首个在schema-free条件下、直接评估真实网络安全工具NL-to-CLI翻译的细粒度基准，区别于依赖显式API Schema的函数调用评测。
- 手册驱动的数据构建与确定性规范化、别名感知评估相结合，实现对工具选择与参数构造的精确、可复现测量。
- 融合LLM校验、沙箱执行与人工复核的多阶段验证，兼顾语义正确性与实际可执行性。
- 提出runtime-free verifiable rewards，用细粒度且可验证的静态信号支撑训练中的RL优化，避免运行时依赖。

#### 实验结论
- 数据与设置：KaliBench覆盖8,504查询-命令对、1,642工具、23能力维度与5安全阶段，并在三种评测模式下对24种通用与安全向开放权重模型进行系统评估。
- 关键结果：在unrestricted设置中，开放权重模型的exact-command accuracy均未超过42%，表明无显式工具提示下的准确CLI生成仍然困难。
- 训练收益：基于KaliBench的SFT与利用verifiable rewards的RL能显著提升一个8B模型，使其表现可与一个685B MoE模型相当。
