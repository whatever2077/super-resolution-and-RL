# 2026-04-23 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Synthetic Abundance Maps for Unsupervised Super-Resolution of Hyperspectral Remote Sensing Images
- **论文链接**: http://arxiv.org/abs/2601.22755v2
- **作者**: Xinxin Xu, Yann Gousseau, Christophe Kervazo, Saïd Ladjal
- **原始摘要**: Hyperspectral single image super-resolution (HS-SISR) aims to enhance the spatial resolution of hyperspectral images to fully exploit their spectral information. While considerable progress has been made in this field, most existing methods are supervised and require ground truth data for training-data that is often unavailable in practice. To overcome this limitation, we propose a novel unsupervised training framework for HS-SISR, based on synthetic abundance data, where no high-resolution ground-truth reference is required for training. The approach begins by unmixing the hyperspectral image into endmembers and abundances. A neural network is then trained to perform abundance super-resolution using synthetic abundances only. These synthetic abundance maps are generated from a dead leaves model whose characteristics are inherited from the low-resolution image to be super-resolved and from the known point spread function (PSF) of the hyperspectral sensor. This trained network is subsequently used to enhance the spatial resolution of the original image's abundances, and the final super-resolution hyperspectral image is reconstructed by combining them with the endmembers. Experimental results demonstrate both the training value of the synthetic data and the effectiveness of the proposed method across 3 datasets, 3 scaling factors, and several evaluation metrics. The code is available at https://github.com/xinxinxu99/SISR-DL.git

### GPT总结
#### 文章内容
- 论文关注无高分辨率标注的Hyperspectral Single Image Super-Resolution (HS-SISR) 问题，目标是在不依赖HR地面实况的条件下提升HSI空间分辨率。
- 核心思路：先将低分辨率HSI进行端元-丰度分解；利用从待超分图像与已知传感器PSF继承统计特性的dead leaves model合成丰度图，基于这些合成数据训练一个“丰度超分”网络；再用该网络提升真实丰度并与端元重构得到HR HSI。
- 主要结论：在3个数据集、3个放大倍率与多种评价指标上，合成数据对训练具有价值，方法有效；无需HR参考即可实现HS-SISR。

#### 方法
- 预处理：对输入低分辨率HSI进行端元/丰度分解，得到端元光谱与对应丰度图。
- 合成数据：基于dead leaves model生成丰度图，模型参数从待超分LR图像与已知PSF继承，以贴合成像/降质特性。
- 训练阶段：仅用上述合成丰度构建训练对，训练一个丰度超分网络，实现从LR丰度到HR丰度的映射；具体网络结构与损失设计文中未明确说明。
- 推理阶段：将训练好的网络应用于原始图像的丰度图，获取超分后的HR丰度。
- 重建输出：以端元与HR丰度线性组合重建HR HSI，完成HS-SISR流程。

#### 创新点
- 用dead leaves model按图像与传感器PSF自适应生成“合成丰度”，构建无需真实HR标注的训练数据，解决HS-SISR缺乏监督的问题。
- 将HS-SISR任务重构为“丰度超分+端元重建”的两步式流程，以物理可解释的分解-重建管线替代直接对高维光谱立方体做端到端超分。
- 训练仅依赖目标LR图像与已知PSF，无需外部MSI或HR HSI，提供了一种通用、可迁移的无监督训练范式。
- 实证强调“合成数据的训练价值”，验证由dead leaves合成的丰度可有效支撑实际HSI超分训练与推理。

#### 实验结论
- 任务与设置：在HS-SISR上进行评估，覆盖3个数据集、3个放大倍率与多种评价指标；具体数据集名称、倍率数值与指标列表文中未明确说明。
- 核心结果：方法在多数据集、多倍率下均取得有效提升，证明仅用合成丰度训练即可带来可靠的超分效果；与哪些基线对比及具体数值文中未明确说明。
- 复现与资源：代码公开于https://github.com/xinxinxu99/SISR-DL.git。

## 关键词：reinforcement learning

## Safe Continual Reinforcement Learning in Non-stationary Environments
- **论文链接**: http://arxiv.org/abs/2604.19737v1
- **作者**: Austin Coursey, Abel Diaz-Gonzalez, Marcos Quinones-Grueiro, Gautam Biswas
- **原始摘要**: Reinforcement learning (RL) offers a compelling data-driven paradigm for synthesizing controllers for complex systems when accurate physical models are unavailable; however, most existing control-oriented RL methods assume stationarity and, therefore, struggle in real-world non-stationary deployments where system dynamics and operating conditions can change unexpectedly. Moreover, RL controllers acting in physical environments must satisfy safety constraints throughout their learning and execution phases, rendering transient violations during adaptation unacceptable. Although continual RL and safe RL have each addressed non-stationarity and safety, respectively, their intersection remains comparatively unexplored, motivating the study of safe continual RL algorithms that can adapt over the system's lifetime while preserving safety. In this work, we systematically investigate safe continual reinforcement learning by introducing three benchmark environments that capture safety-critical continual adaptation and by evaluating representative approaches from safe RL, continual RL, and their combinations. Our empirical results reveal a fundamental tension between maintaining safety constraints and preventing catastrophic forgetting under non-stationary dynamics, with existing methods generally failing to achieve both objectives simultaneously. To address this shortcoming, we examine regularization-based strategies that partially mitigate this trade-off and characterize their benefits and limitations. Finally, we outline key open challenges and research directions toward developing safe, resilient learning-based controllers capable of sustained autonomous operation in changing environments.

### GPT总结
#### 文章内容
该文聚焦安全与持续性并存的强化学习：在非平稳环境中，智能体需一边适配动态变化、一边全程满足安全约束且避免灾难性遗忘。作者系统性构造了安全-持续适配的基准环境，评测安全RL、持续RL及其组合，并提出基于正则化的Safe EWC与CF-EWC。结论指出维持安全与防遗忘存在根本张力，现有方法难以同时兼顾，而基于EWC的正则化策略可部分缓解但仍有局限。

#### 方法
- 以 PPO+EWC 为基础框架：在每个任务结束后保存参数 θ* 并用对角 Fisher 信息近似评估参数重要性，跨任务通过 EWC 惩罚项抑制对重要参数的偏移，缓解遗忘。
- Safe EWC：采用代价塑形 rSafe = r − βC（文中 β=5），在 PPO 的策略损失中叠加 EWC 正则；同时维护 cost critic 监控安全信号，但优化仅使用代价塑形回报。
- CF-EWC：不改动奖励，而在 Fisher 估计中对每个样本以 1/(c+1) 加权，提升低代价（更安全）样本对应参数的重要性、降低高代价（不安全）样本的重要性，使对违反安全的参数更可塑。
- 训练流程：按任务顺序滚动收集轨迹—进行 PPO 更新（含 GAE、熵正则与价值回归）—在任务末基于代表性采样估计 Fisher—将(θ*, F)加入记忆并用于后续任务的 EWC 正则。
- 评测基线：选取基于 trust-region 的 on-policy 策略梯度方法（PPO/TRPO）及其在安全RL、持续RL与二者结合中的代表实现，统一比较安全性与持续学习能力。

#### 创新点
- 提出安全持续RL视角下的两种EWC扩展：Safe EWC（代价塑形+EWC）与CF-EWC（代价加权Fisher+EWC），分别从奖励层与正则层嵌入安全信号。
- 通过“Cost-Fisher”机制在不改动奖励的前提下把安全约束编码进参数重要性估计，允许对不安全参数更大幅度更新，兼顾适配与保留安全行为。
- 构建并公开三类面向安全-持续适配的非平稳基准环境与系统化评测设置，覆盖safe RL、continual RL及其组合，揭示两目标间的结构性权衡。
- 实证刻画正则化方法的缓解效果与局限，提出未来面向安全、鲁棒、长期自主运行控制器的关键开放问题与研究方向。

#### 实验结论
- 任务与数据：作者引入三个安全关键的非平稳基准环境用于持续适配评测（具体环境名称与规模文中未明确说明），并在代表性 PPO/TRPO 系列方法及其安全/持续扩展上进行对比。
- 核心结果：在非平稳动力学下，维持安全约束与防灾难性遗忘存在显著张力，现有方法普遍难以同时最优；基于EWC的正则化（Safe EWC、CF-EWC）能在一定程度上缓解该权衡，但仍不能完全兼顾两者。
- 作者结论：需要面向安全持续RL的更强方法，包括更有效的安全信息融入、任务变化检测与无任务标识的在线适配等方向；当前正则化策略是可行但不充分的第一步。
