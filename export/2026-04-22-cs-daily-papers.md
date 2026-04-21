# 2026-04-22 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Trustworthy Endoscopic Super-Resolution
- **论文链接**: http://arxiv.org/abs/2604.18001v1
- **作者**: Julio Silva-Rodríguez, Ender Konukoglu
- **原始摘要**: Super-resolution (SR) models are attracting growing interest for enhancing minimally invasive surgery and diagnostic videos under hardware constraints. However, valid concerns remain regarding the introduction of hallucinated structures and amplified noise, limiting their reliability in safety-critical settings. We propose a direct and practical framework to make SR systems more trustworthy by identifying where reconstructions are likely to fail. Our approach integrates a lightweight error-prediction network that operates on intermediate representations to estimate pixel-wise reconstruction error. The module is computationally efficient and low-latency, making it suitable for real-time deployment. We convert these predictions into operational failure decisions by constructing Conformal Failure Masks (CFM), which localize regions where the SR output should not be trusted. Built on conformal risk control principles, our method provides theoretical guarantees for controlling both the tolerated error limit and the miscoverage in detected failures. We evaluate our approach on image and video SR, demonstrating its effectiveness in detecting unreliable reconstructions in endoscopic and robotic surgery settings. To our knowledge, this is the first study to provide a model-agnostic, theoretically grounded approach to improving the safety of real-time endoscopic image SR.

### GPT总结
#### 文章内容
本文面向内镜与机器人手术场景的图像/视频超分辨率（SR）安全性问题，针对SR可能产生幻觉结构与放大噪声，提出在像素级识别不可靠重建区域的实用框架。核心思路是在冻结的SR模型中引入轻量级误差预测网络，基于中间表征估计像素级重建误差，并通过构建具有理论保证的 Conformal Failure Masks (CFM) 将连续误差转为可操作的二值失效决策。方法基于 conformal risk control，在控制可容忍误差上限的同时，控制失效检测的误覆盖率，适用于实时部署。实验在内镜与手术数据的图像与视频SR上验证了能有效定位不可靠区域，提高系统可托度。

#### 方法
- 冻结预训练SR模型fθ（encoder fθenc + reconstruction fθrec），训练辅助的 Reconstruction Error Network fΦ，输入为encoder的中间特征F，输出像素级误差估计Ĕ。
- 监督信号为预测HR与参考HR之间的像素级误差：训练时最小化Ĕ与逐像素平方误差的差异；用于定义观测误差时采用PSNR（文中称实践中采用PSNR）。
- 通过 split conformal 校准，将连续误差分数转为二值 Conformal Failure Masks：设定失效阈值τ_fail，并以“双层”风险控制同时约束（1）允许的重建误差水平与（2）失效区域的误覆盖率。
- 误差预测头采用双三次上采样 + 多层卷积/BN/ReLU + 线性层的轻量结构，可与SR重建并行，几乎不增加延迟，满足实时需求。
- 训练使用与SR预训练互不重叠的小规模新数据用于误差头拟合与校准；推理阶段同时输出SR结果与CFM以标注不可信区域。

#### 创新点
- 提出面向图像SR的双层 conformal risk control 程序，首次在内镜SR中实现“可容忍误差+误覆盖率”同时受控的二值失效决策，具备模型无关、分布无关的理论保证。
- 设计基于SR中间特征的轻量像素级误差预测网络，在不改动SR主干的前提下实现实时失效感知。
- 从以往区间/热力图式不确定性可视化转向可操作的二值 Conformal Failure Masks，便于在临床实时流程中做出明确的“信任/不信任”决策。
- 面向内镜与机器人手术的实时SR安全性，文中声称为首个具备理论保障的模型无关方案。

#### 实验结论
- 任务与数据：在内镜与机器人手术场景的图像与视频SR上评估，包括 SurgiSR4K（如Surgi-2×：480×270→960×540；Surgi-4×：960×540→更高分辨率）及最小创伤诊断视频等。
- 结果：CFM可有效检测并定位不可靠重建区域，提升实时内镜SR的安全可用性；具体定量指标、与基线对比数值与运行时延等，文中未明确说明。
- 作者结论：方法在控制漏检（假阴性）方面具备保证，但效果依赖误差预测质量；受限于conformal方法的校准规模、边际覆盖与可交换性假设，后续将探索在实时约束下进一步提升误差预测。

## 关键词：reinforcement learning

## Bounded Ratio Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2604.18578v1
- **作者**: Yunke Ao, Le Chen, Bruce D. Lee, Assefa S. Wahd, Aline Czarnobai, Philipp Fürnstahl, Bernhard Schölkopf, Andreas Krause
- **原始摘要**: Proximal Policy Optimization (PPO) has become the predominant algorithm for on-policy reinforcement learning due to its scalability and empirical robustness across domains. However, there is a significant disconnect between the underlying foundations of trust region methods and the heuristic clipped objective used in PPO. In this paper, we bridge this gap by introducing the Bounded Ratio Reinforcement Learning (BRRL) framework. We formulate a novel regularized and constrained policy optimization problem and derive its analytical optimal solution. We prove that this solution ensures monotonic performance improvement. To handle parameterized policy classes, we develop a policy optimization algorithm called Bounded Policy Optimization (BPO) that minimizes an advantage-weighted divergence between the policy and the analytic optimal solution from BRRL. We further establish a lower bound on the expected performance of the resulting policy in terms of the BPO loss function. Notably, our framework also provides a new theoretical lens to interpret the success of the PPO loss, and connects trust region policy optimization and the Cross-Entropy Method (CEM). We additionally extend BPO to Group-relative BPO (GBPO) for LLM fine-tuning. Empirical evaluations of BPO across MuJoCo, Atari, and complex IsaacLab environments (e.g., Humanoid locomotion), and of GBPO for LLM fine-tuning tasks, demonstrate that BPO and GBPO generally match or outperform PPO and GRPO in stability and final performance.

### GPT总结
#### 文章内容
本文针对PPO的剪切目标与TRPO信任域理论脱节的问题，提出Bounded Ratio Reinforcement Learning (BRRL) 框架，以有界似然比约束重构策略优化。核心思路是在有界比率与正则化的约束下得到解析最优策略，并以此为目标通过Bounded Policy Optimization (BPO) 在参数化策略类中进行拟合，同时给出单调性能提升与下界保证。主要结论是：BRRL提供了统一的理论视角解释PPO/GRPO的有效性并联系到CEM，BPO/GBPO在MuJoCo、Atari、IsaacLab（如Humanoid locomotion）和LLM微调中整体匹配或优于PPO/GRPO，且更稳定。

#### 方法
- 提出BRRL：以策略似然比的上下界作为信任域约束，构建正则化与约束的策略优化问题，避免直接使用KL约束。
- 给出解析最优解：基于优势函数（含“(soft-)median-advantages”）推导每个状态-动作的最优比率结构，证明可带来单调性能提升。
- BPO算法：以解析最优策略为“教师”，通过最小化优势加权的策略散度，将参数化策略拟合到该解析解；并给出以BPO损失为指标的期望性能下界。
- 理论连接：从BRRL视角解释PPO剪切目标的合理性，建立与TRPO和Cross-Entropy Method (CEM) 的联系。
- 扩展到GBPO：引入Group-relative设定以适配LLM微调（对应GRPO对PPO的扩展）。

#### 创新点
- 用“有界比率信任域”替代KL信任域，形成可解析求解的策略优化问题，弥合PPO启发式剪切与信任域理论的缺口。
- 推导解析最优更新并证明单调改进，为PPO类目标提供新的理论解释与性能保证。
- 提出优势加权散度匹配的BPO训练目标，从解析解出发更直接地指导参数化策略更新。
- 建立与CEM的结构性联系，并将框架扩展为GBPO以支持LLM微调场景。

#### 实验结论
- 任务与环境：MuJoCo、Atari、IsaacLab（如Humanoid locomotion）以及LLM微调任务。
- 结果：BPO与GBPO在稳定性与最终性能上整体匹配或优于PPO与GRPO。
- 细节：具体数据集、超参数与精确数值对比等文中未明确说明。
