# 2026-08-06 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Morphology-Aware Implicit Super-Resolution Network for Pathological Images
- **论文链接**: http://arxiv.org/abs/2608.03664v1
- **作者**: Jiaming Liang, QiHui Han, Haolin Chen, Chengxin Ye, Jiawen Liu, Jiazhou Chen, Xiaoqi Sheng, Hongmin Cai
- **原始摘要**: Accurate diagnosis in Digital Pathology (DP) relies on high-resolution whole-slide images, yet clinical deployment is often limited by hardware costs. Super-Resolution (SR) offers a promising alternative by computationally enhancing low-resolution acquisitions. However, existing SR methods frequently struggle to preserve fine-grained cellular morphology, leading to texture oversmoothing and blurred structural boundaries under complex tissue variability. To address this issue, we propose Morph-ISR, a morphology-aware implicit super-resolution framework for DP that restores diagnostically relevant details with sub-pixel precision. Morph-ISR reformulates SR as a continuous coordinate-based reconstruction problem and integrates an Implicit Position-aware Kernel Generator (IPKG) to adaptively model spatially varying tissue morphology. To further enhance structural fidelity, a Morphological Fidelity Prior (MFP) is introduced, leveraging semantic guidance from a pre-trained cell segmentation network to enforce boundary-preserving and region-aware reconstruction, thereby improving the representation of critical cellular boundaries and nuclear textures. Experiments on TCGA and SurGen datasets show that Morph-ISR achieves the best LPIPS and ST-LPIPS among the evaluated methods, reducing them by up to 38.37% and 39.55%, respectively, over the second-best methods while maintaining strong PSNR and SSIM. These results demonstrate superior preservation of diagnostically relevant cellular boundaries and nuclear textures, while compact parameterization and high throughput support efficient edge deployment. Code and trained models will be released upon publication.

### GPT总结
#### 文章内容
该文面向数字病理图像的超分辨重建，针对现有方法在复杂组织形态下易出现纹理过度平滑与结构边界模糊的问题。作者提出Morph-ISR，将SR重构建模为连续坐标的隐式函数学习，并引入位置感知核生成器（IPKG）与形态先验（MFP）以自适应捕获组织形态并增强边界保真。实验在TCGA与SurGen上表明，该方法在LPIPS与ST-LPIPS上取得最优（相较次优方法最高降幅分别为38.37%与39.55%），同时维持较强的PSNR与SSIM。模型参数紧凑、吞吐高，具备边缘部署潜力。

#### 方法
- 将SR问题重构为连续坐标的隐式表示学习，以坐标查询实现亚像素级细节重建并适配空间可变形态。
- 设计Implicit Position-aware Kernel Generator（IPKG），根据空间坐标与局部特征自适应生成位置相关的卷积核，建模组织形态的空间非均匀性。
- 引入Morphological Fidelity Prior（MFP）：利用预训练细胞分割网络提供语义引导，从损失/约束层面强化边界保留与区域感知重建，突出细胞核纹理与关键结构界面。
- 训练目标在像素重建与感知/结构保真间权衡，重点提升LPIPS与ST-LPIPS的结构与感知质量，同时保持PSNR/SSIM不显著下降；具体损失权重与优化细节文中未明确说明。
- 推理阶段依托隐式坐标表示可支持任意放大倍率与亚像素插值；具体加速策略与部署细节文中未明确说明。

#### 创新点
- 将病理SR建模为连续坐标的隐式重建问题，并结合位置感知核生成（IPKG），以空间自适应方式刻画复杂、非均匀的组织形态。
- 提出形态保真先验（MFP），借助预训练细胞分割的语义信息，显式增强边界保留与区域一致性，从而改善细胞边界与核纹理的可辨识度。
- 在不依赖纯生成先验的前提下，兼顾感知/结构指标（LPIPS、ST-LPIPS）与失真指标（PSNR、SSIM），实现临床相关细节的可解释性与稳定性。
- 以紧凑参数化与高吞吐为设计目标，强调在边缘设备上的高效推理；具体参数规模与FPS对比细节文中未明确说明。

#### 实验结论
- 任务与数据：在数字病理SR任务上，使用TCGA与SurGen数据进行评估，涵盖复杂组织变异场景。
- 核心结果：整体上LPIPS与ST-LPIPS最优，对次优方法的最大降幅分别为38.37%与39.55%，同时保持较强的PSNR/SSIM；例如在TCGA-LUAD上LPIPS 0.1330、ST-LPIPS 0.1302、PSNR 29.34、SSIM 0.8476；在TCGA-KIRC上LPIPS 0.1452、ST-LPIPS 0.1425、PSNR 29.67、SSIM 0.8251。
- 作者结论：Morph-ISR能更好地保留诊断相关的细胞边界与核纹理，兼具紧凑性与高吞吐，适合边缘部署；具体吞吐量（FPS）与参数量的定量对比文中未明确说明。

## 关键词：reinforcement learning

## TurnSight: Turn-Level Hindsight Self-Distillation for Tool-Integrated Reasoning
- **论文链接**: http://arxiv.org/abs/2608.04007v1
- **作者**: Changle Qu, Sunhao Dai, Hengyi Cai, Yuqi Zhou, Xinran Chen, Simon, Jun Xu
- **原始摘要**: Tool-Integrated Reasoning (TIR) enables LLMs to solve complex tasks through iterative tool interactions. However, existing reinforcement learning methods often rely on trajectory-level supervision, limiting fine-grained credit assignment in long-horizon TIR scenarios. On-policy self-distillation offers denser signals through teacher branches with privileged context, but existing approaches typically derive such context from ground-truth answers or retrieved skills, which may not reflect the states actually visited by the agent. Moreover, token-level supervision fails to capture the turn-level structure of tool interactions. To address this, we propose TurnSight, a turn-level hindsight self-distillation framework that derives supervision directly from execution-conditioned hindsight. It then constructs multiple hindsight views with different lookahead horizons and selects reliable supervision through cross-horizon directional agreement. Finally, the selected hindsight signal is normalized across sibling rollouts and used to adaptively modulate RL advantages while preserving their original optimization direction. Extensive experiments on three benchmarks demonstrate the effectiveness of TurnSight. Our codes are available at https://github.com/quchangle1/TurnSight.

### GPT总结
#### 文章内容
该论文针对Tool-Integrated Reasoning（TIR）中长程交互导致的细粒度时序信用分配困难，指出现有基于轨迹级RL与基于特权上下文的on-policy自蒸馏（OPSD）要么过于粗粒度、要么与真实访问状态失配，且多为token级监督，无法反映turn结构。作者提出TurnSight：一种基于执行结果的turn-level hindsight自蒸馏框架，沿着在训策略构造多种不同前瞻深度的“事后视角”，通过跨视角方向一致性筛选可靠监督，并用其归一化调制RL优势而不改变优化方向。实验证明TurnSight在三个TIR基准上显著优于强基线，展现出更细粒度、状态对齐的信用分配能力。

#### 方法
- 在on-policy轨迹上，学生模型与外部工具交互；教师分支依据实际执行结果构造execution-conditioned hindsight，对每个turn输出方向性质量信号（而非token级）。
- 以不同lookahead深度d（如d=1, d=2, …）构造多视角hindsight，对同一turn形成多种前瞻评估。
- 通过跨前瞻视角的“方向一致性”准则筛选出可靠的turn级监督，抑制噪声与失配信号。
- 将选中的hindsight信号在同源“兄弟”rollouts间归一化，用其自适应调制RL优势（advantage），仅改变幅度不改变符号，从而保留原始优化方向。
- 训练使用FTRL数据集进行后训练（含>2,000个带可执行工具的问题）；推理阶段无需任何特权上下文，按常规TIR流程执行。其余训练细节文中未明确说明。

#### 创新点
- 将自蒸馏从传统token级提升为turn级，直接对齐TIR的交互粒度，并以execution-conditioned hindsight提供状态对齐的监督。
- 提出多前瞻深度的hindsight视角与跨视角方向一致性选择机制，提升监督可靠性与稳健性。
- 设计“优势调制而不改向”的优化策略：在兄弟轨迹上归一化hindsight信号，用于自适应缩放RL优势，兼顾稳定性与效率。
- 相较依赖ground-truth答案或检索技能的OPSD，避免状态失配与外轨迹依赖，严格在on-policy访问状态上评估与学习。

#### 实验结论
- 基准与数据集：在FTRL、BFCL（含MF/MP/LC子集）与ToolHop三大基准上评测；骨干模型为Qwen3-4B与Qwen3-8B。
- 结果：TurnSight在Qwen3-4B上整体Avg.达到37.51，超过MatchTIR的34.76等强基线；在Qwen3-8B上整体Avg.为42.02，超过MatchTIR的39.03，同时在多个子项上取得最佳或次佳结果。
- 结论：跨模型与数据集稳定提升，表明turn级、状态对齐的hindsight自蒸馏能够显著改善长程TIR的信用分配与任务表现。
