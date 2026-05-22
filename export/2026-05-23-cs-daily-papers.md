# 2026-05-23 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Moment-Reenacting: Inverse Motion Degradation with Cross-shutter Guidance
- **论文链接**: http://arxiv.org/abs/2605.22423v1
- **作者**: Ji Xiang, Lin Guixu, Yin Zhengwei, Zhao Jiancheng, Zheng Yinqiang
- **原始摘要**: Motion degradation, manifested as blur in global shutter (GS) images or rolling shutter (RS) distortion in RS counterparts, remains a fundamental challenge in computational imaging, especially under fast motion or low-light conditions. While prior works have treated blur decomposition and RS temporal super-resolution as separate tasks, this separation fails to exploit their intrinsic complementarity. In this paper, we propose a unified framework to invert motion degradation and reenact imaging moment by jointly leveraging the complementary characteristics of GS blur and RS distortion. To this end, we introduce a novel dual-shutter setup that captures synchronized blur-RS image pairs and demonstrate that this combination effectively resolves temporal and spatial ambiguities inherent in both modalities. For allowing flexible performance-cost trade-offs, we further extend this dual-shutter setup to a stereo Blur-RS configuration with a narrow baseline. In addition, we construct a triaxial imaging system to collect a real-world dataset with aligned GS-RS pairs and ground-truth high-speed frames, enabling robust training and evaluation beyond synthetic data. Our proposed network explicitly disentangles motion into context-aware and temporally-sensitive representations via a dual-stream motion interpretation module, followed by a self-prompted frame reconstruction stage. Extensive experiments validate the superiority and generalizability of our approach, establishing a new paradigm for realistic high-speed video reconstruction under complex motion degradations. Codes and more resources are available at https://jixiang2016.github.io/dualBR_site/.

### GPT总结
#### 文章内容
论文针对在快速运动或低光照下由不同快门模式导致的GS图像模糊与RS几何失真，提出一个统一的跨快门指导框架，同时逆转两类退化并重现成像时刻。核心思路是采用双快门采集同步的Blur-RS图像对，利用GS与RS的互补特性消解时间与空间歧义，并通过双流动解释与自提示重建模块生成高帧率清晰视频。作者还构建三轴成像系统，采集对齐的GS-RS真实数据与高帧率真值序列，用于稳健训练与评估。实验表明方法具有优越性与泛化性，提出了现实复杂运动退化下高帧率视频重建的新范式。

#### 方法
- 双快门采集：设计能同时捕获同步的Blur-RS图像对的dual-shutter方案，以联合利用GS blur与RS distortion的互补信息，缓解时间排序与空间几何歧义。
- 立体扩展：进一步提出窄基线的stereo Blur-RS配置，在性能与成本之间提供可调权衡。
- 真实数据采集：构建triaxial imaging system，获取对齐的GS-RS图像与ground-truth高帧率帧序列，实现超越合成数据的训练与评估。
- 模型结构：采用dual-stream motion interpretation模块，将运动显式解耦为“context-aware”和“temporally-sensitive”两类表示。
- 重建机制：通过self-prompted frame reconstruction阶段，根据解耦的运动表征自引导地重建高帧率清晰帧；训练细节、损失函数与推理超参文中未明确说明。

#### 创新点
- 任务统一：首次在统一框架中同时处理blur decomposition与RS temporal super-resolution，利用GS/RS跨快门视角的互补性来逆转运动退化。
- 硬件与数据：提出dual-shutter与窄基线stereo Blur-RS配置，并搭建triaxial成像系统，采集包含对齐GS-RS与高帧率真值的真实数据集。
- 模型设计：引入dual-stream motion interpretation进行上下文与时间敏感运动的显式解耦，配合self-prompted重建机制提升时序与空间一致性。
- 现实泛化：强调基于真实数据的训练与评估，缓解仅用合成数据带来的伪影与泛化不确定性。

#### 实验结论
- 任务：在复杂运动退化下重建高帧率清晰视频，统一解决GS模糊与RS失真造成的时间/空间歧义。
- 数据集：使用三轴系统采集的真实对齐GS-RS图像与ground-truth高帧率序列进行训练与测试。
- 结果与结论：大量实验验证方法的优越性与泛化性，作者认为该框架为现实场景中的高帧率视频重建建立了新的范式；具体指标与对比细节文中未明确说明。

## 关键词：reinforcement learning

## Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
- **论文链接**: http://arxiv.org/abs/2605.22814v1
- **作者**: Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa
- **原始摘要**: Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at https://recuriosity.github.io/.

### GPT总结
#### 文章内容
- 论文针对在复杂、照片级真实3D环境中，基于好奇心的强化学习易陷入“遗忘-循环”的探索失败，归因于缺乏空间持久性与情节化上下文。
- 核心思路：训练期引入一个随时间持续更新的在线3D重建作为持久世界模型，用其新视角渲染与真实观测的差异定义内在奖励；同时以仅基于RGB序列的长上下文Transformer策略维持情节记忆，实现长程回溯与前探。
- 主要结论：在HM3D上纯靠好奇心训练的策略优于RL式主动建图基线，零样本泛化到Gibson和AI生成世界，并可在下游任务（如摘苹果、图像目标导航）中以少量微调超越从零训练。

#### 方法
- 持久前向模型：使用在线3D Gaussian Splatting (3DGS)从流式观测构建场景G，训练期以RGB-D与相机位姿增量更新、重建与稀疏化/致密化维护。
- 好奇心奖励：在每一步用3DGS从新位姿渲染预测视图，与真实观测的视觉误差作为内在奖励，鼓励访问尚未解释的区域；部署期不再需要该模型。
- 策略网络：将每帧RGB编码为融合图像patch嵌入与DINOv2特征的token，经因果时序自注意力与具全局隐状态的线性注意力，Actor-Critic头输出动作与价值。
- 训练与探索机制：采用on-policy RL以内在奖励优化；通过调度式、临时的随机行为注入克服长程无奖励段，促成回溯-分支式探索。
- 推理：仅依赖RGB图像流，无需深度、位姿或显式建图/定位，保持端到端。

#### 创新点
- 将在线3DGS作为“持久世界模型”，以可持续更新的空间记忆产生稳定的好奇心信号，避免ICM等统计先验在已见区域反复给奖的问题。
- 提出仅基于RGB序列的长上下文Transformer策略，显式建模情节化轨迹历史，无需显式几何地图与深度传感器即可学得空间意识并在部署中保持端到端。
- 训练/部署解耦：训练期使用位姿与深度作为特权信息更新前向模型，部署期完全移除，仅以视觉驱动。
- 实证指出持久记忆长度对探索至关重要（将持久记忆截断为短窗会显著退化探索能力）；并通过调度式随机注入在不依赖模仿或层级目标选择下实现有效长程探索。

#### 实验结论
- 任务与数据：在静态3D场景中进行视觉探索，自主产生内在奖励；主要在HM3D训练，评估于HM3D，并零样本泛化到Gibson及AI生成3D世界。
- 核心结果：纯好奇心训练的端到端策略优于RL-based active mapping基线；在下游任务（apple picking、image-goal navigation）上，以少量外部奖励微调优于从头训练。
- 指标与具体数值提升幅度：文中未明确说明。
