# 2026-08-01 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## RFMSR: Residual Flow Matching for Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2607.12753v2
- **作者**: Shuwei Huang, Tianyao Luo, Jicheng Liu, Pan Zhou
- **原始摘要**: Image super-resolution (ISR) has witnessed remarkable progress with diffusion models and flow matching. The dominant text-to-image (T2I) based approaches leverage large-scale foundation models as generative priors, achieving impressive perceptual quality but at the cost of massive model sizes and prohibitive training expenses. Recent flow-matching-based vision-only approaches have made significant strides; however, they adopt standard flow formulations that transport from a pure Gaussian prior to the data distribution, discarding the rich structural information already present in the low-quality (LQ) input. Furthermore, existing single-step acceleration techniques often forfeit the model's multi-step inference capability. In this paper, we propose Residual Flow Matching for Image Super-Resolution (RFMSR), a vision-only framework that centers the source distribution at the LQ latent, reducing transport distance and preserving structural priors throughout the flow trajectory. We further introduce a two-phase training strategy: Phase I pretrains the velocity field via conditional flow matching, while Phase II applies end-to-end supervision to the single-step prediction while retaining the velocity loss across all timesteps, achieving high-quality single-step generation without sacrificing multi-step refinement. Extensive experiments demonstrate that RFMSR achieves comparable or even superior perceptual quality compared to state-of-the-art (SOTA) methods. The source code is available at https://github.com/Faze-Hsw/RFMSR.

### GPT总结
#### 文章内容
- 论文关注单幅图像超分辨率（ISR）中基于扩散/流匹配方法的两大问题：标准流从纯高斯先验出发而忽略LQ输入结构先验，以及单步加速常牺牲多步细化能力。  
- 核心思路是提出Residual Flow Matching：将源分布居中于LQ潜变量y0，缩短传输距离并沿轨迹保持结构约束；并采用“两阶段训练”，先用条件流匹配预训练速度场，再在保持各时刻速度损失的同时对单步输出进行端到端监督。  
- 主要结论是：在不依赖T2I教师的前提下，RFMSR作为纯视觉范式，在多/单步推理上均取得与SOTA相当或更优的感知质量，且单步质量显著提升而不损失多步细化能力。

#### 方法
- 残差流建模：以LQ图像编码得到的潜变量y0为源分布中心，而非纯高斯，显式建模“HQ−LQ”的残差流，降低最优传输距离并保留结构先验。  
- 两阶段训练：Phase I采用Conditional Flow Matching预训练速度场；Phase II在保持全时间步速度损失的同时，对单步预测进行端到端监督，实现高质量单步生成与多步可细化兼得。  
- 模型与条件：沿用VOSR架构（LightningDiT 0.5B），SD2.1 VAE编码图像，DINOv2-Base提取语义；条件为c=(y0, DINOv2(LQ Image))，噪声水平σ=1.0。  
- 推理形态：提供多步（Phase I模型）与单步（Phase II后模型）两种推理；单步作为快速生成，仍可保留多步细化能力。  
- 数据与合成：约100万HQ图像（LSDIR、DIV2K、Flickr2K及筛选网页图像），HQ裁剪512×512，经Real-ESRGAN退化为128×128 LQ用于训练。

#### 创新点
- 将流匹配的源分布从纯高斯改为以LQ潜变量为中心的残差流，显著缩短传输路径并在轨迹中保留结构先验。  
- 提出保留速度监督的单步端到端训练：在优化单步输出的同时不丢失多步轨迹学习，从而避免“单步加速⇔丧失多步能力”的常见权衡。  
- 纯视觉范式下结合大模型骨干（LightningDiT）与DINOv2条件，无需T2I预训练/教师，减少模型规模与训练成本依赖。  
- 通过统一的残差流与两阶段策略，兼容单步和多步推理，提升实用性。

#### 实验结论
- 任务与数据：主评估为×4 ISR，在RealSR、ImageNet随机250张、LSDIR随机250张测试；对比ResShift、VOSR(0.5B)、SeeSR、OSEDiff、SinSR、InvSR及VOSR单步蒸馏变体，采用PSNR/SSIM(Y通道)、LPIPS/DISTS/FID与NIQE/MUSIQ/MANIQA/CLIPIQA等指标。  
- 结果与结论：RFMSR在感知质量上总体达到或优于代表性SOTA（含T2I与纯视觉路线），单步版本在保证高质量的同时不牺牲多步细化能力；消融验证残差流与两阶段训练均有效。  
- 具体数值与统计显著性：文中未明确说明。

## 关键词：reinforcement learning

## OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models
- **论文链接**: http://arxiv.org/abs/2607.28609v1
- **作者**: Qiushi Sun, Kanzhi Cheng, Yian Wang, Bowen Yang, Hang Yan, Liheng Chen, Fangzhi Xu, Zichen Ding, Nuo Chen, Jialin Cao, Xingdong Gong, Zehao Li, Kaiming Jin, Xinfeng Yuan, Zhoumianze Liu, Jingyang Gong, Zhangyue Yin, Jiahui Gao, Zhiyong Wu, Tianbao Xie, Jianbing Zhang, Ben Kao, Lingpeng Kong
- **原始摘要**: Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

### GPT总结
#### 文章内容
该论文关注计算机使用代理（CUA）轨迹的自动判定问题：在大规模数据筛选与强化学习中，如何可靠判断一段跨平台、长时序交互是否完成指令。作者构建了跨平台、高质量的人类真值基准 OSReward（及 OSReward-Hard、OSReward-Multi），系统评估当前 VLM 作为“评审”的可靠性，发现广泛存在的“宽松偏置”会将失败误判为成功。为降低成本与提升可用性，作者发布了带推理标注的 OS-Shepherd-100K，并训练开源奖励模型 OS-Shepherd（9B/35B），在成本显著降低的同时达到与商用评审相当的稳定与可靠性。

#### 方法
- 构建跨平台收集基础设施：在 Web、Windows、Ubuntu、Mobile 等真实化环境中配置常用应用与初始状态，由标注者撰写可落地的任务指令，驱动来自四类代理骨干的执行以采集轨迹（含动作、屏幕状态与推理）。
- 采用多阶段人工标注流程，得到轨迹级“是否完成指令”的高可信真值；在此基础上形成 OSReward，并派生挑战集 OSReward-Hard 与用于细粒度效率/对齐评分的 OSReward-Multi。
- 设计评审协议与指标：要求 VLM 对长时序、多模态轨迹给出二分类判定及多维度评分，并以成功召回率与失败召回率刻画“严格—宽松”偏置。
- 系统评测多种闭源与开源 VLM 评审，比较其在不同平台、不同难度上的可靠性与成本，分析失误模式与偏置来源。
- 构建 OS-Shepherd-100K（带推理标注的轨迹判定语料），在此上训练开源奖励模型 OS-Shepherd（9B/35B），用于提供可扩展、低成本且稳定的轨迹级奖励信号。

#### 创新点
- 首个跨平台、基于新鲜人类真值的 CUA 轨迹评审基准，避免复用旧基准带来的环境、代理与自动验证器噪声干扰。
- 从基准中系统揭示并量化 VLM 评审的“宽松偏置”（对失败召回低，易将失败判为成功），为大规模奖励建模提供诊断工具。
- 引入 OSReward-Hard 与 OSReward-Multi，分别聚焦真实困难案例与提供超越二分类的效率/对齐细粒度评测视角。
- 发布带推理标注的开源评审语料 OS-Shepherd-100K，并据此训练开源奖励模型 OS-Shepherd（9B/35B），在保持可靠性的同时显著降低评审成本。

#### 实验结论
- 在 OSReward 与 OSReward-Hard 上，即便最先进模型距离“理想评审”仍有差距，部分结果接近或仅优于“50% (coin flip)”基线；跨模型普遍存在对失败的低召回（宽松）偏置。
- 可靠度较高的商用评审成本过高，开源可负担模型整体落后；OS-Shepherd（9B/35B）在稳定性与可靠性上与商用评审相当，同时显著降低使用成本。
- 数据与分析表明：高质量、跨平台的人类真值与针对偏置的评测维度对于在强化学习与数据管线中构建可扩展的轨迹级奖励模型至关重要。
