# 2026-07-29 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## MicroZoom: Structure-Preserving Detail Synthesis at Extreme Scale
- **论文链接**: http://arxiv.org/abs/2607.24729v1
- **作者**: Huy Huynh, Jingwei Ma, Brian Curless, Ira Kemelmacher-Shlizerman, Steven M. Seitz
- **原始摘要**: We introduce MicroZoom, a generative framework for gigapixel image synthesis at the microscopic scale. Given a standard photograph and a sparse set of consumer-grade microscope close-ups, MicroZoom synthesizes a seamless, gigapixel-resolution image grounded in the material character of the real references, enabling exploratory visualization of microscopic texture across the full spatial extent of an object. Our goal is plausible synthesis, not exact reconstruction. We focus on full-image, reference-based, extreme-scale super-resolution at magnification levels of up to 350x, a setting that introduces two major challenges: (1) recovering texture-specific detail from highly lossy inputs near ambiguous material boundaries, and (2) preserving correct large-scale pattern structure, such as the repeating geometry of a fabric weave, across millions of local predictions. We address these with a two-stage cascaded design, where the first stage recovers global pattern coherence and the second refines local texture detail, supplemented by a segmentation mask to guide synthesis at ambiguous boundaries. We verify our approach on a collection of self-captured everyday objects and demonstrate globally coherent, materially grounded gigapixel imagery.

### GPT总结
#### 文章内容
- 论文针对极端放大倍率（65×–350×）下从一张普通照片与少量消费级显微近景合成“具有材料特征且全局结构一致”的千兆像素微观图像，重点解决纹理边界处的歧义与大范围结构一致性难题。  
- 核心思路是“两阶段级联生成+分割引导”：先在较粗尺度恢复全局周期结构，再细化局部纹理；同时以分割掩码在材料边界处约束纹理不串扰，并用显微参考图作为外观锚点。  
- 结论表明，该方法可在0.6 MP输入与少量显微近景条件下生成高达4890 MP（示例93.23×，上限350×）且结构连贯、材料风格可信的千兆像素图像，适合探索性微观可视化。

#### 方法
- 数据与配准：用手机拍全局图F，消费级数字显微镜采集多视角近景并进行“每个焦平面快速连拍去噪+SIFT配准+拉普拉斯金字塔融合”的对焦叠加，得到全清晰的显微近景X_GT；以标尺估计像素密度ρ并计算尺度s=ρ_XGT/ρ_F。  
- 合成监督对：将X_GT在伽马域匹配至F的颜色后做双三次Down_s，得到Y，形成(X_GT, Y)的配对训练样本；用SAM生成多区域分割掩码以在材料边界处提供结构引导。  
- 实例级微调：在预训练生成模型（文中未明确说明具体基座）的基础上进行参数高效微调（LoRA），同时引入两类条件信号——用于结构保持的ControlNet适配器与通道级拼接的分割掩码；采取“先纹理后结构”的条件热启策略。损失细节文中未明确说明（图示提到Flow Matching Loss）。  
- 两阶段级联推理：Stage-1合成全局周期/结构一致的中间结果，Stage-2在此基础上细化纹理、增强材料特征，分割掩码在两阶段均用于边界抑串扰。  
- 千兆像素融合：采用MultiDiffusion的可变步长滑窗，对局部块进行重叠采样与无缝聚合，跨数百万局部预测生成无伪影的千兆像素输出。

#### 创新点
- 提出针对极端尺度的“两阶段级联+分割引导”框架：先全局结构一致性，后局部纹理细化，有效缓解高倍率下的结构碎片化与纹理跨域污染。  
- 用实例级、弱标注友好的数据构造：通过显微焦段叠加+颜色匹配+尺度标定，从X_GT自洽地产生监督对，避免难以获得的成对（全局-显微）真值。  
- 在RefSR场景中结合ControlNet与分割掩码进行结构感知的条件控制，专门针对材料边界歧义进行约束，而非仅语义级别的先验注入。  
- 面向千兆像素合成的可变步长MultiDiffusion拼接策略，保障超大幅面下跨块的一致性与无缝融合。

#### 实验结论
- 任务与数据：在自采日常物体数据上验证，从单张全局手机图+少量显微近景合成极端尺度微观千兆像素图像。  
- 结果：示例从0.6 MP放大至4890 MP（93.23×），总体可达350×；生成结果在大范围模式（如织物纹理周期）与材料风格上保持一致，边界处伪影受控。  
- 对比与定量：文中未明确说明系统性的定量指标及与现有方法（如UltraZoom等）的全面对比，仅展示项目页交互式可视化与案例质检。

## 关键词：reinforcement learning

## Explainable Reinforcement Learning via Physics-Aware Policy Distillation
- **论文链接**: http://arxiv.org/abs/2607.24672v1
- **作者**: Shaker Al-Tamari, Waled Kadour
- **原始摘要**: In safety-critical sectors such as robotics and automotive engineering, the deployment of Deep Reinforcement Learning (DRL) is often hindered by the black-box nature of deep neural networks. This lack of transparency poses significant challenges for regulatory compliance and human-agent trust. This paper presents an experimental study aimed at making high-performance continuous control DRL systems interpretable. A policy distillation framework is implemented using the classic Inverted Pendulum benchmark. A high-performance Twin Delayed DDPG (TD3) agent serves as an opaque, continuous teacher model, whose policy is distilled into an interpretable student surrogate based on a shallow Decision Tree. By leveraging a custom physics-aware feature and "Noisy Oracle Rollouts" for dataset generation, the distillation process achieves performance equivalent to the expert teacher. Furthermore, comparative control theory analysis reveals a fundamental trade-off: transitioning from continuous to discrete rule-based control induces high-frequency Bang-Bang actuation and a stable bimodal limit cycle. Simulation results indicate that Bounded-Input Bounded-Output (BIBO) stability is maintained while providing both global and local interpretability for safe autonomous systems.

### GPT总结
#### 文章内容
本文面向安全关键的连续控制场景，关注DRL黑箱难以解释的问题，提出将高性能连续控制策略蒸馏为可解释的决策树代理。核心思路是以TD3在InvertedPendulum-v4上训练为“教师”，通过“物理感知”的特征工程与“Noisy Oracle Rollouts”构造覆盖危急状态的数据集，训练浅层Decision Tree Regressor模仿连续策略。结果表明学生模型在性能上可达到教师等效，同时从控制论角度揭示离散规则控制导致的高频Bang-Bang作动与稳定的双峰极限环，并保持BIBO稳定性。

#### 方法
- 教师策略：采用TD3在InvertedPendulum-v4上训练（CleanRL实现），Actor为4-256-256-1网络，Tanh输出缩放至[-3, 3]；奖励为存活+1/步，目标为连续1000步平衡。
- 数据集生成：运行已收敛的教师策略，并在动作上注入高斯噪声（Noisy Oracle Rollouts），重点采集早期瞬态与接近失稳的状态—动作，以覆盖恢复策略。
- 特征工程：在原始4维状态基础上加入定制的“physics-aware”特征以提升可分性与可解释性（具体特征形式文中未明确说明）。
- 蒸馏学生：以Decision Tree Regressor进行行为克隆回归，获得可全局可视化的规则集，并可通过样本决策路径提供局部解释。
- 评估与分析：在仿真中比较学生与教师的控制性能，并用控制理论分析树模型近饱和输出引发的Bang-Bang作动与双峰极限环，验证BIBO稳定性。

#### 创新点
- 将连续控制DRL策略蒸馏为浅层Decision Tree，实现同时具备全局与局部可解释性的高性能代理。
- 引入“Noisy Oracle Rollouts”，通过动作加噪主动触发近失稳与恢复过程，显式覆盖“紧急控制逻辑”以提高蒸馏鲁棒性。
- 融合物理先验的“physics-aware”特征用于蒸馏数据表征，强化规则可分性与人类可读性（具体设计文中未明确说明）。
- 以控制论视角揭示从连续到离散/规则控制的内在权衡：高频Bang-Bang与稳定极限环的出现及其对BIBO稳定的影响与保障。

#### 实验结论
- 任务与数据：在InvertedPendulum-v4上进行实验，学生模型在平衡控制任务中的表现与TD3教师等效；具体数值与树深/节点规模、数据集规模文中未明确说明。
- 关键结果：蒸馏后的决策树在动作接近饱和时呈现高频Bang-Bang作动并形成稳定的双峰极限环，但系统保持Bounded-Input Bounded-Output稳定。
- 作者结论：该物理感知的策略蒸馏框架在不牺牲性能的前提下提供全局与局部可解释性，适用于对安全与合规要求较高的自主系统。
