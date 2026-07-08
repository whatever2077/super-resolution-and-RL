# 2026-07-09 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2607.06238v1
- **作者**: Lihua Wei, Huatong Gao, Jia Gong, Zhiyu Tan, Hao Li, Jun Liu, Zhihua Ren
- **原始摘要**: Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realizations under varying acquisition trade-offs. We rethink MRI super-resolution as a physics-aware reconstruction problem, in which the goal is to identify the optimal resolution-SNR configuration and then super-resolve it to obtain high-quality MRI results. A key implication of this formulation is that MRI resolution becomes dynamic rather than fixed. To handle such resolution-heterogeneous inputs, we adapt 2D Gaussian Splatting (2D GS) to MRI by formulating reconstruction as a coordinate-based, resolution-agnostic rendering problem. To further enhance fidelity, we introduce three innovations: (1) a prior-aware Gaussian representation that combines an Anatomical Structure Prior for tissue-specific kernel initialization with an Imaging System Prior that captures hardware characteristics via a covariance dictionary; (2) a physics-constrained signal modeling scheme that predicts intrinsic tissue parameters (proton density rho and effective relaxation rate R2) and synthesizes intensities through governing physical equations, ensuring biophysically plausible contrast; and (3) a meta-learning framework that alleviates paired-data scarcity by pretraining on simulated data and adapting to real-world conditions. Extensive experiments on dynamic-resolution datasets and standard benchmarks demonstrate that our method achieves state-of-the-art performance, highlighting its strong potential for clinical deployment.

### GPT总结
#### 文章内容
论文将MRI超分辨从“固定LR到固定HR的确定性映射”重塑为一个与采集物理相关的重建问题，强调空间分辨率与SNR耦合，输入分辨率应视为动态而非固定。核心思路是先识别最优的分辨率–SNR配置，再通过适配MRI的2D Gaussian Splatting进行坐标式、分辨率无关的渲染，同时引入结构与系统先验以及物理约束的信号建模。方法在动态分辨率数据与标准基准上达到SOTA，并在真实3T–5T数据上生成与5T Ground Truth更一致的结构与纹理。作者认为该框架具备临床落地潜力。

#### 方法
- 问题建模：将MRI SR表述为“选择最优分辨率–SNR配置→超分辨重建”的物理感知流程，将输入视为分辨率异构且动态变化。具体的配置搜索/选择机制文中未明确说明。
- 渲染核心：将2D Gaussian Splatting（2D GS）适配于MRI，构建基于坐标的、分辨率不可知的渲染器，以统一处理不同输入分辨率。
- 表示先验：提出“先验感知高斯表示”，结合Anatomical Structure Prior进行组织特异的核初始化，并以Imaging System Prior通过协方差字典刻画硬件特性。
- 物理建模：采用物理约束的信号建模，显式预测组织本征参数（proton density ρ、effective relaxation rate R2），并通过MRI成像物理方程合成强度，保证生物物理一致性。
- 学习策略：基于元学习，先在模拟数据上预训练，再适配真实世界条件以缓解成对数据稀缺；训练损失与超参数细节文中未明确说明。

#### 创新点
- 将MRI SR从固定尺度映射转为物理感知的动态分辨率重建任务，显式考虑分辨率–SNR耦合并追求最优配置。
- 首次将2D Gaussian Splatting用于MRI SR，构建坐标式、分辨率无关的渲染框架以处理分辨率异构输入。
- 提出结合Anatomical Structure Prior与Imaging System Prior（协方差字典）的先验感知高斯表示，联合编码组织与设备信息。
- 物理约束信号建模（预测ρ与R2并由物理方程合成对比）与元学习迁移（模拟→真实）相结合，提升可解释性与泛化。

#### 实验结论
- 动态分辨率实验：在模拟的64 mT–3T成对数据以及真实3T–5T动态分辨率数据（3T United Imaging uMR 890多尺度：1.04/0.9/0.83/0.76/0.69/0.625/0.55/0.5；5T uMR Jupiter为GT；10名受试者）上评估，并与LIIF、LTE、Pixel-to-Gaussian对比。
- 关键观察：在模拟IXI数据上，最佳视觉质量出现在×0.7输入尺度；在真实3T–5T数据上，方法产生与5T Ground Truth最一致的结构细节与纹理。
- 结论与指标：作者宣称在动态分辨率与标准基准（如fastMRI）上达到SOTA；具体定量指标与数值提升幅度文中未明确说明。

## 关键词：reinforcement learning

## Embodied Human-Robot Interaction via Acoustics: A MARL Approach with AcoustoBots for Spatial Data Physicalization
- **论文链接**: http://arxiv.org/abs/2607.06563v1
- **作者**: Shiqi Liu, Narsimlu Kemsaram, Prateek Mittal, Pengyuan Wei, Sriram Subramanian
- **原始摘要**: Traditional data physicalization is often static and disconnected from real environments, limiting its ability to convey embodied spatial dynamics and engage users. To address this limitation, we present AcoustoBots, a mobile acoustophoretic data-physicalization platform in which TurtleBot3 robots carry upward-facing 8 x 8 ultrasonic phased arrays. Each array levitates a particle whose height (1-10 cm) encodes a local urban scalar value, such as population density, noise, or traffic. A MARL (Multi-Agent Reinforcement Learning) policy based on the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm, with centralized training and decentralized execution, selects collision-aware navigation actions, while a high-rate Gerchberg-Saxton-Phased Array of Transducers (GS-PAT) acoustic controller maintains trap stability and updates array phases to achieve the commanded height during motion. This creates a closed perception-display-action loop. We evaluate single-robot city-to-city traversal and dual-robot cooperative coverage on a 4 m x 3 m scaled UK map using PhaseSpace-based localization for repeatable multi-robot trials. Results show stable in-motion levitation and consistent, location-dependent height rendering, with task success rates of 90% and 80% for the single and dual-robot regimes, respectively, over 10 trials per regime, and low collision counts. These findings support acoustophoretic levitation as a simple, glanceable, robot-mediated communication cue for embodied human-robot interaction in spatial analytics.

### GPT总结
#### 文章内容
论文面向传统数据物理化静态、与环境脱节的问题，提出AcoustoBots：在TurtleBot3上搭载8×8超声相控阵，以声悬浮粒子高度（1–10 cm）编码本地城市标量数据，并随机器人移动实现嵌入式、可一瞥感知的空间数据呈现。核心思路是用MADDPG（集中式训练、分布式执行）的MARL策略进行避碰与覆盖导航，同时以高频GS-PAT控制器在运动中稳定声陷并将相位实时更新到命令高度，闭合“感知—显示—行动”回路。实测在4 m × 3 m缩放UK地图与PhaseSpace定位下，单机器人城际穿越与双机器人协同覆盖分别达到90%与80%成功率（各10次试验），且碰撞少、在动悬浮稳定。作者认为声悬浮高度是一种简洁、可解释的人机交流通道，但在规模化与鲁棒性方面仍有提升空间。

#### 方法
- 平台与物理化通道：TurtleBot3搭载向上的8×8超声相控阵，利用声悬浮粒子高度（1–10 cm）编码本地标量场（如population density、noise、traffic）。
- 控制栈分层：高频GS-PAT声学控制器在运动中维持陷阱稳定并将相位更新到指令高度；导航由MARL策略负责避碰与任务导向移动。
- 决策与训练：采用MADDPG进行集中式训练、分布式执行（CTDE），以机器人状态与与物理化相关的观测选择安全、信息量大的动作。
- 奖励与协同：基于物理约束与任务目标的奖励设计引导覆盖效率、避免碰撞并保持位置—高度一致性，支持双机器人协同。
- 系统集成与定位：ROS 2集成，使用PhaseSpace定位在4 m × 3 m UK地图上进行可重复多机器人实验。

#### 创新点
- 将移动机器人与声学悬浮物理化深度耦合，实现同时具备“机动性—物理化—数据响应性”的嵌入式呈现，扩展静态声悬浮系统到移动探索场景。
- 设计运动中的实时声学操控：在存在加减速与振动的条件下，GS-PAT持续稳定声陷并精确追踪高度指令，闭合“感知—显示—行动”回路。
- 基于MADDPG的MARL协同覆盖，将可解释的粒子高度作为对人类与队友的语义交流线索，并通过物理约束感知的奖励塑形提升安全与任务绩效。
- 在缩放UK地图与PhaseSpace定位环境中完成双机器人协同与在动物理化的端到端实证，为空间分析的人机共融交互提供原型验证。

#### 实验结论
- 任务与环境：评估单机器人城市穿越（London→Liverpool→Edinburgh）与双机器人协同覆盖（含路径长度预算）两类任务，场地为4 m × 3 m缩放UK地图，使用PhaseSpace定位。
- 核心结果：实现运动中的稳定声悬浮与位置依赖的高度渲染；单机器人与双机器人成功率分别为90%与80%（各10次试验），碰撞次数低。
- 作者结论与局限：MARL产生平滑、避碰的轨迹，适合演示与交流；但成功率未达100%，对探索与环境随机性敏感，且仅在简化二维与小规模团队上验证。未来拟扩展到更大规模与异质团队、改进奖励（或加入人类反馈）并融合更丰富传感。文中未明确说明更细粒度的网络结构与超参数细节。
