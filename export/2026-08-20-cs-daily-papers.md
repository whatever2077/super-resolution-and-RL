# 2026-08-20 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## EDITBRIDGE: Towards Faithful and Efficient Ultra-High-Resolution Image Editing
- **论文链接**: http://arxiv.org/abs/2608.18063v1
- **作者**: Jiayi Song, Shijie Huang, Fangtai Wu, Yubo Huang, Zhenxiong Tan, Songhua Liu, Jiaming Liu, Ruihua Huang
- **原始摘要**: High-resolution image editing is increasingly demanded in professional workflows, yet existing diffusion-based models remain constrained to resolutions below 1K due to quadratic attention complexity and prohibitive memory requirements. A prevalent workaround employs a two-stage pipeline: editing at low resolution followed by independent super-resolution. However, this approach suffers from two critical issues: information divergence, where hallucinated details contradict the original high-resolution (HR) source, and texture degradation, manifesting as over-smoothed or over-sharpened artifacts. We propose EditBridge, a diffusion bridge framework for efficient ultra high-resolution editing. Unlike conventional diffusion that regenerates from noise, we formulate refinement as structured data-to-data translation from the low-resolution (LR) edited result to its HR counterpart, explicitly conditioned on the original HR source to preserve authentic details. To efficiently incorporate HR source guidance, we introduce a prior-guided block-wise sparse attention mechanism that exploits semantic correspondence from first-stage editing to constrain cross-image interactions to spatially aligned regions, significantly reducing computational overhead. Extensive experiments demonstrate that EditBridge achieves high-fidelity editing with superior perceptual quality at resolutions up to 4K, delivering 3.6--8.4$\times$ speedup at 2K and enabling practical 4K editing in 61 seconds.

### GPT总结
#### 文章内容
该论文聚焦于超高分辨率图像编辑中常见的两阶段方案（低分辨率编辑+独立SR）导致的信息偏离与纹理退化问题，指出现有扩散模型在>1K分辨率下因注意力二次复杂度与显存限制效率低下。作者提出EditBridge：将高分辨率编辑建模为从已编辑的LR结果到HR图像的“数据到数据”的扩散桥过程，并显式以原始HR源图像为条件进行细节保真。实验表明，方法在最高4K分辨率下实现高保真编辑，在2K分辨率下实现3.6–8.4×加速，4K编辑用时61秒，同时获得更优的感知质量。

#### 方法
- 两阶段整体流程：先用现有编辑模型在低分辨率完成语义级编辑，再通过扩散桥从LR编辑结果精炼到HR，过程中以原始HR源图像作为条件约束细节与结构一致性。
- 扩散桥建模：不从噪声重生成，而是学习在两个数据分布之间的随机过渡，沿采样轨迹保留LR编辑图的结构与内容，提升效率与保真。
- 先验提取：在第一阶段编辑中利用注意力图提取跨图语义对应先验，指示被修改区域及其在HR源图中的语义锚点位置。
- 先验引导的块状稀疏注意力：在DiT中以块为单位限制跨图查询-键的交互到空间对齐、语义相关的区域，避免全局稠密注意力导致的二次复杂度与冗余计算。
- 条件融合与计算策略：通过上述稀疏跨图注意力高效引入HR源图指导，对未编辑区域侧重细节保真、对编辑区域侧重局部上下文细节合成；具体训练细节与损失设定文中未明确说明。

#### 创新点
- 将高分辨率编辑从“噪声到数据”的常规扩散转为“LR已编辑数据到HR目标”的扩散桥建模，显著减少重生成冗余并提升一致性。
- 提出先验引导的块状稀疏跨图注意力，利用第一阶段编辑的语义对应先验，精确路由HR源图信息到对齐区域，兼顾保真与效率。
- 在DiT框架下实现语义选择性的跨图交互，避免直接拼接令牌引发的注意力膨胀与显存瓶颈。
- 面向超高分辨率编辑的高效化设计，使4K级别编辑成为可实用的流程（61秒/幅）。

#### 实验结论
- 任务与设置：面向超高分辨率图像编辑（最高至4K），比较对象包含两阶段“LR编辑+独立SR”等常见范式；具体数据集与评价指标文中未明确说明。
- 关键结果：在2K分辨率实现3.6–8.4×加速；4K编辑在61秒内完成；相较两阶段SR管线获得更优的感知质量，并缓解信息偏离与纹理退化。
- 作者结论：EditBridge在4K内实现高保真、高效率的编辑，证明扩散桥+先验引导稀疏注意力可兼顾细节一致性与计算可扩展性。

## 关键词：reinforcement learning

## Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents
- **论文链接**: http://arxiv.org/abs/2608.18008v1
- **作者**: Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
- **原始摘要**: Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.

### GPT总结
#### 文章内容
该论文关注LLM规划器与RL控制器的混合体系中，LLM产生的奖励信号是否会改变最优策略集合这一“正确性/定点”问题。作者将混合架构形式化为Goal-Augmented MDP，并将LLM逐状态进度分数作为有界势函数进行潜在式奖励塑形，从而在理论上保证不改变最优策略集合。数值实验与小型管线验证显示该构造在LLM打分不准甚至对抗性放大（20×）时依然保持策略不变性，优于通用LLM-as-reward方案。论文不主张在基准上超越现有方法，而是强调混合训练的理论定点可审计，经验收敛留待后续工作。

#### 方法
- 将LLM-planner + RL-controller建模为Goal-Augmented MDP（GA-MDP），由任务文本ℓ与状态字幕ϕ(s)驱动规划器输出子目标序列g。
- 让LLM对每个状态给出“任务进度”分数，并将其裁剪/约束为有界势函数，按Ng, Harada, Russell (1999)的潜在式塑形加入奖励（γΦ(s′)−Φ(s)）。
- 证明：在GA-MDP中使用上述有界势函数塑形，不论LLM逐状态分数多么不准确，最优策略集合保持不变（策略不变性）。
- 给出完整推理算法（Algorithm 1）与参考实现；在推理中，规划器P(ℓ, ϕ(s))输出子目标序列，控制器按塑形后的奖励执行与学习。
- 训练细节（具体RL算法、超参数等）文中未明确说明。

#### 创新点
- 首次在LLM-RL混合架构中，将LLM逐状态反馈严格纳入潜在式奖励塑形框架（有界势函数），相较Text2Reward与Eureka等通用“LLM-as-reward”方案提供更强的“最优策略不变”保证。
- 策略不变性对LLM打分误差鲁棒：即使LLM分数在个别状态极端不准或被对抗性放大（20×基准奖励），只要保持有界潜在式塑形，最优策略集合不变。
- 将体系定点与经验收敛显式解耦：设计使混合训练的理论定点可独立审计；并通过对MiniGrid管线的失败模式（Done-oracle词汇不匹配）进行预测与诊断，体现理论-工程闭环。
- 提供可复现的端到端推理流程与参考实现，兼容多种LLM规划器，便于社区采用与检验。

#### 实验结论
- 在一个3状态MDP上进行数值验证，覆盖四种势函数配置（含绝对值为基准奖励20×的对抗性配置），观察到策略不变性与理论一致。
- 在20个MiniGrid任务上对规划器（Qwen-2.5:14b，本地服务）进行独立评测：解析率100%，ground-truth coverage为54.8%。
- 在MiniGrid-DoorKey-6x6进行小规模端到端管线验证：框架按规格运行，同时定位到与理论预期一致的集成失败案例（Done-oracle与LLM计划词汇不匹配）。作者不声称在基准上超越现有方法。
