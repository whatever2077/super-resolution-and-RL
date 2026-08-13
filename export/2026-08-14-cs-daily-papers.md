# 2026-08-14 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Self-Supervised Weighted Image Guided Quantitative MRI Super-Resolution
- **论文链接**: http://arxiv.org/abs/2512.17612v2
- **作者**: Alireza Samadifardheris, Dirk H. J. Poot, Florian Wiesinger, Stefan Klein, Juan A. Hernandez-Tamames
- **原始摘要**: Object: To present and evaluate Self-supervised Weighted Image Guided quantitative MRI Super-Resolution (SWIG qMRI SR), a physics-informed framework recovering high-resolution (HR) qMRI from a rapid low-resolution (LR) acquisition guided by routine weighted images (wMRI), without HR training targets.   Materials and Methods: A CNN matches acquired wMRI to images synthesized from predicted maps through forward signal models, while anchoring those maps to the acquired LR qMRI. Training and ablation used synthetic data (n = 27); cross-sequence generalizability was tested in three volunteers scanned with silent 3D MuPa-ZTE at 1 and 5min, with clinical T1w/T2w guides.   Results: In synthetic data, dual-guide SR reduced the T1 high-frequency error norm 45.4% below baseline; removing the LR qMRI anchor raised gray-matter T1 error from 63 to 110ms. In vivo, super-resolved 1-min maps synthesized T1w images (SSIM 0.93, PSNR 27.3dB) surpassing synthesis from 5-min maps (SSIM 0.83), and improved synthesis of T2-FLAIR, never used as a guide (SSIM 0.69 to 0.75).   Discussion: HR detail was recovered without HR supervision, and the network transferred across a different qMRI sequence. Because the guides are already acquired, adding a 1-min qMRI scan to a standard exam offers a practical route to routine clinical qMRI integration.

### GPT总结
#### 文章内容
该文旨在在无HR qMRI标注的前提下，利用常规高分辨率加权影像（wMRI）引导，将快速采集的低分辨率（LR）qMRI重建为高分辨率（HR）定量图。核心思路是以物理先验为约束：用CNN预测HR参数图，通过前向信号模型合成wMRI并与实采wMRI匹配，同时用LR qMRI作为锚点保持量化一致性。结果显示在合成与体内数据上均能恢复高频细节并跨序列泛化，且1分钟qMRI经SR后生成的T1w/T2-FLAIR合成图像质量优于更长扫描基线。作者认为在现有临床流程中仅增加1分钟qMRI即可实现可行的临床qMRI集成。

#### 方法
- 输入/输出：输入为LR qMRI参数图与HR临床wMRI（如T1w/T2w）作为引导，网络输出HR qMRI参数图。
- 物理一致性：借助前向信号模型由预测的HR参数图合成wMRI，并与实采HR wMRI构成重建匹配损失。
- 量化锚定：对预测的HR参数图与输入LR qMRI施加一致性约束，避免仅凭先验产生的偏差。
- 双引导与跨序列：利用双wMRI引导（T1w/T2w），并在参数图域建模，从而弱化对特定采集序列的依赖以实现跨qMRI序列泛化。
- 训练/推理：训练主要基于合成数据（n=27）含消融；推理阶段在受试者数据上仅需现成临床wMRI与短时LR qMRI。具体网络结构、损失权重与训练细节文中未明确说明。

#### 创新点
- 提出无需HR qMRI标注的自监督qMRI超分辨框架，将wMRI作为空间先验且以LR qMRI为量化锚点，兼顾分辨率与量化可靠性。
- 物理约束优化目标：通过前向信号模型把参数图域与对比度图域桥接，直接以实采HR wMRI监督合成一致性。
- 在参数图域进行SR而非序列依赖的对比度域，提高跨qMRI序列（cross-sequence）泛化潜力。
- 系统性消融验证LR锚点与双引导的重要性，量化其对误差与细节恢复的贡献。

#### 实验结论
- 数据与设定：合成数据训练/消融（n=27）；体内三名志愿者，silent 3D MuPa-ZTE采集1与5分钟qMRI，并以临床T1w/T2w为引导。
- 关键结果：合成数据中，双引导SR相较基线将T1高频误差范数降低45.4%；去除LR锚点使灰质T1误差由63 ms升至110 ms。体内中，基于1分钟SR参数图合成的T1w达到SSIM 0.93、PSNR 27.3 dB，优于5分钟参数图合成（SSIM 0.83）；T2-FLAIR合成SSIM由0.69提升至0.75。
- 作者结论：在无HR监督下可恢复HR细节并实现跨序列迁移；由于临床wMRI已常规采集，仅需额外1分钟qMRI即可为常规工作流带来可用的qMRI。

## 关键词：reinforcement learning

## A-3PO: Accelerating Asynchronous LLM Training with Staleness-aware Proximal Policy Approximation
- **论文链接**: http://arxiv.org/abs/2512.06547v4
- **作者**: Xiaocan Li, Shiliang Wu, Zheng Shen
- **原始摘要**: Decoupled PPO has been a successful reinforcement learning (RL) algorithm to deal with the high data staleness under the asynchronous RL setting. Decoupled loss used in decoupled PPO improves coupled-loss style of algorithms' (e.g., standard PPO, GRPO) learning stability by introducing a proximal policy to decouple the off-policy correction (importance weight) from the policy update constraint (trust region). However, the proximal policy requires an extra forward pass through the model at each training step, creating a computational overhead for large language models training. We observe that since the proximal policy only serves as a trust region anchor between the behavior and target policies, we can approximate it through simple interpolation without explicit computation. We call this approach A-3PO (APproximated Proximal Policy Optimization). A-3PO eliminates this overhead, accelerating training by 1.8x speedup while maintaining comparable performance. Code \& off-the-shelf example are contributed to the open-source RL training system AReaL at: https://github.com/areal-project/AReaL/blob/v1.0.0.rc1/docs/algorithms/prox_approx.md

### GPT总结
#### 文章内容
- 论文针对异步RL训练中Decoupled PPO/GRPO需显式重算proximal policy带来的额外前向开销，导致大模型训练效率受限的问题。
- 提出A-3PO：在对数概率空间用基于“陈旧度”d的插值近似proximal policy（log π_prox = α log π_behav + (1−α) log π_θ，α=1(d=0)，α=1/d(d≥1)），既保留信赖域锚点作用又免去额外前向。
- 结论显示在LLM后训练中可实现最高1.8×加速且与显式重算/同步GRPO性能相当，并表现出更稳健的训练动态，尤其在8B规模上更明显。

#### 方法
- 在Decoupled损失中以插值近似proximal policy：在log-prob空间按α对行为策略π_behav与目标策略π_θ线性插值，α由数据陈旧度d自适应设定（α=1或1/d）。
- 以近似的π_prox作为信赖域锚点将校正因子与更新约束解耦；重要性比r=π_θ/π_prox满足r=w^α（w=π_θ/π_behav），对新鲜数据赋予更大权重。
- 取消proximal前向重算，仅需逐元素张量运算融入训练环路，嵌入AReaL异步RL框架，无额外模型推理开销。
- 优势函数采用group reward normalization；在异步设置下并行收集与训练，保持Decoupled PPO/GRPO的信赖域更新结构。

#### 创新点
- 提出“陈旧度感知”的proximal概率插值，保留PPO信赖域结构的同时完全去除proximal重算开销。
- 给出理论保证：满足trust-region sandwich性质与收缩稳定性r=w^α；随陈旧度增大r的方差趋零，抑制离策略方差。
- 在1.5B与8B两种模型规模上验证，实现最高1.8×训练加速且稳定性优于显式重算Decoupled GRPO与同步GRPO；并以最小代码改动集成至AReaL。

#### 实验结论
- 任务与数据：数学推理（GSM8K、DAPO-Math-17k）；模型与设置：Qwen2.5-1.5B-Instruct@GSM8K、Qwen3-8B@DAPO-Math-17k；基线：Decoupled GRPO（显式proximal重算）与同步GRPO。
- 结果：训练时间最高加速1.8×；在两套设置中与基线取得可比任务表现，并显著提升训练稳定性（更受控的重要性比、更少clipped tokens），8B规模下显式重算出现很高的重要性比而A-3PO保持稳定。
- 具体准确率/奖励等数值指标与统计显著性检验：文中未明确说明。
