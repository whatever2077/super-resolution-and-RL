# 2026-05-09 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## sFRC for assessing hallucinations in medical image restoration
- **论文链接**: http://arxiv.org/abs/2603.04673v2
- **作者**: Prabhat Kc, Rongping Zeng, Nirmal Soni, Aldo Badano
- **原始摘要**: Deep learning (DL) methods are currently being explored to restore images from sparse-view-, limited-data-, and undersampled-based acquisitions in medical applications. Although outputs from DL may appear visually appealing based on likability/subjective criteria (such as less noise, smooth features), they may also suffer from hallucinations. This issue is further exacerbated by a lack of easy-to-use techniques and robust metrics for the identification of hallucinations in DL outputs. In this work, we propose performing Fourier Ring Correlation (FRC) analysis over small patches and concomitantly (s)canning across DL outputs and their reference counterparts to detect hallucinations (termed as sFRC). We describe the rationale behind sFRC and provide its mathematical formulation. The parameters essential to sFRC may be set using predefined hallucinated features annotated by subject matter experts or using imaging theory-based hallucination maps. We use sFRC to detect hallucinations for three undersampled medical imaging problems: CT super-resolution, CT sparse view, and MRI subsampled restoration. In the testing phase, we demonstrate sFRC's effectiveness in detecting hallucinated features for the CT problem and sFRC's agreement with imaging theory-based outputs on hallucinated feature maps for the MR problem. Finally, we quantify the hallucination rates of DL methods on in-distribution versus out-of-distribution data and under increasing subsampling rates to characterize the robustness of DL methods. Beyond DL-based methods, sFRC's effectiveness in detecting hallucinations for a conventional regularization-based restoration method and a state-of-the-art unrolled method is also shown.

### GPT总结
#### 文章内容
本文关注AI恢复（重建/后处理）医学影像中“幻觉”（虚假或被删除的结构）难以识别、缺乏易用且稳健指标的问题。核心思路是将 Fourier Ring Correlation (FRC) 扩展为在小块上计算并在图像上滑动扫描的局部相关分析（sFRC），对比DL输出与参考图像以定位幻觉。作者给出sFRC的数学形式与参数设定策略，并在CT超分辨率、CT稀疏视角、MRI欠采样三类任务上验证。实验显示，sFRC可有效检测CT中的幻觉、与MRI成像理论的幻觉图一致，并能量化DL方法在ID/OOD与不同采样率下的幻觉率，亦适用于常规模型与unrolled方法。

#### 方法
- 在DL输出与参考图像之间，按小块进行FRC计算，并以滑动/扫描方式在全图生成局部FRC图以指示可疑幻觉区域（sFRC）。
- 提供sFRC的数学表述；关键参数可通过两种途径设定：由专家标注的幻觉样例校准，或依据成像理论导出的幻觉地图进行设定。
- 在多任务场景中应用：CT super-resolution、CT sparse view重建、MRI subsampled restoration，以评估sFRC的跨模态有效性。
- 在评测阶段比较sFRC热图与理论幻觉图或参考图，检测并量化“加性/减性”幻觉特征的出现与分布。
- 训练/推理方式与阈值细节等实现超参数设置，文中未明确说明。

#### 创新点
- 将全局FRC引入局部小块并扫描的形式（sFRC），面向医学图像恢复中的幻觉检测，提供可操作的空间化频域一致性度量。
- 参数标定机制兼顾专家标注与成像理论先验，连接数据驱动与物理可解释性两条路径。
- 统一在CT与MRI、从DL到常规模型与state-of-the-art unrolled方法上验证，强调方法的通用性与稳健性评估能力。
- 系统性量化ID vs OOD与不同欠采样率条件下的幻觉率，作为模型鲁棒性的新维度评价。

#### 实验结论
- 任务与数据：在CT超分辨率、CT稀疏视角、MRI欠采样恢复等任务上评估；CT实验使用了LDGC数据并进行轻度TV降噪预处理；还使用Michigan Image Reconstruction Toolbox模拟常规伪影。
- 核心结果：sFRC能够有效检测CT场景中的幻觉特征；在MRI中，sFRC的幻觉地图与成像理论导出的结果具有一致性。
- 作者结论：sFRC可用于检测并量化不同方法的幻觉率，区分ID与OOD条件、随采样率变化的鲁棒性差异；方法同样适用于常规正则化重建与先进unrolled方法。

## 关键词：reinforcement learning

## Beyond Negative Rollouts: Positive-Only Policy Optimization with Implicit Negative Gradients
- **论文链接**: http://arxiv.org/abs/2605.06650v1
- **作者**: Mingwei Xu, Hao Fang
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR), due to the deterministic verification, becomes a dominant paradigm for enhancing the reasoning ability of large language models (LLMs). The community witnesses the rapid change from the Proximal Policy Optimization (PPO) to Group Relative Policy Optimization (GRPO), in which GRPO reduces the complicated advantage estimation with simple estimation over grouped positive and negative rollouts. However, we note that negative rollouts may admit no gradation of failure severity, and the combinatorial vastness makes penalizing a few sampled negatives unlikely to cover a meaningful reward signal under sparse binary rewards. In this work, we propose Positive-Only Policy Optimization (POPO), a novel RLVR framework in which learning can occur exclusively via online positive rollouts. Specifically, POPO utilizes bounded importance sampling over the positive rollout set. Thus, no disjoint negative rollouts are used for the gradient guidance. We show that implicit negative gradients can emerge naturally through reinforcing the positive probability via rollouts redistribution. Next, POPO stabilizes the policy optimization through two mechanisms. First, it applies a siamese policy network with a momentum-based adaptation law for stabilized policy evolution. Second, we replace the KL-divergence with a bounded similarity penalty term in the siamese representation space. We conduct extensive experiments using publicly available, well-established text-LLM models, e.g., the Qwen family, across all-level mathematical benchmarks. Our experiment demonstrates that POPO achieves performance comparable to, or even superior to GRPO. Notably, we show that POPO can achieve 36.67% in AIME 2025 with Qwen-Math-7B, outperforming GRPO 30.00%. Our ablation and sweep studies further illustrate the necessity and robustness of POPO components.

### GPT总结
#### 文章内容
本文关注RLVR场景下负样本回合在稀疏二值奖励中难以提供有效学习信号的问题，提出仅基于正样本回合更新策略的Positive-Only Policy Optimization (POPO)。核心思路是对正回合集合进行有界重要性采样归一化，仅强化正概率，通过概率质量再分配诱导“隐式负梯度”，并用动量式孪生策略与表征空间的有界相似度正则稳定训练。实验证明POPO在多数学基准上与GRPO相当或更优，例如在AIME 2025上Qwen-Math-7B达36.67%，优于GRPO的30.00%。作者结论是：在RLVR中无需显式使用负回合也能取得强性能，指向新的训练范式。

#### 方法
- 正样本强化：在每轮on-policy交互中，只保留通过确定性验证器的正回合；对正回合集合施加有界重要性采样权重并归一化，进行策略更新。
- 隐式负梯度：通过提升正回合概率导致概率质量从非正空间转移，从而无需显式使用负回合即可产生对错误行为的隐式惩罚。
- 孪生策略架构：采用student–teacher式孪生网络，teacher以EMA动量更新，作为自适应策略锚点以平滑策略演化。
- 正则替换：以孪生表征空间中的有界相似度惩罚替代传统KL-divergence，提供软约束并保持语义结构稳定。
- 训练与评测：训练使用DeepScaleR-Preview-Dataset；评测覆盖Qwen家族、DeepSeek-R1 distilled与通用text-LLM，在数学推理基准上统一验证。推理流程为常规生成，文中未明确说明额外推理trick。

#### 创新点
- 提出仅用正回合的POPO，在RLVR中摒弃显式负回合与分组对比，配合有界重要性采样实现稳定优化。
- 通过概率再分配引入“隐式负梯度”，避免在组合爆炸的错误空间中采样覆盖不足的问题。
- 以EMA孪生策略作为自适应锚点，将BYOL/SimSiam等SSL的稳定化思想引入策略优化。
- 用表征空间的有界相似度替代KL正则，弱化对参考策略的刚性约束并提升优化可控性。

#### 实验结论
- 任务与数据集：在数学推理RLVR任务上，评测于MATH-500、AMC23、AIME 2024、AIME 2025、Olympiad等基准，并展示GSM8K上的训练轨迹对比。
- 核心结果：POPO整体与GRPO相当或更优；例如Qwen-Math-7B在AIME 2025上36.67%，显著高于GRPO的30.00%。
- 作者结论：消融与超参探索显示各组件必要且鲁棒，POPO验证了“无负回合”的RLVR方向可行并具备竞争力。
