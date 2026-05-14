# 2026-05-15 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## HADAR-Based Thermal Infrared Hyperspectral Image Restoration
- **论文链接**: http://arxiv.org/abs/2605.13664v1
- **作者**: Cheng Dai, Jiale Lin, Bingxuan Song, Yifei Chen, Jiashuo Chen, Xin Yuan, Fanglin Bao
- **原始摘要**: Thermal-infrared (TIR) hyperspectral imagery (HSI) provides critical scene information for various applications. However, its practical utility is severely limited by unique sensor degradations beyond the capabilities of existing restoration methods, which are ignorant of underlying thermal physics. Here, we propose HAIR (HADAR-based Image Restoration) as a physics-driven framework for ground-based TIR-HSI restoration. HAIR utilizes the HADAR rendering equation (HRE) and combines it with the atmospheric downwelling radiative transfer equation (RTE) to model TIR-HSI using temperature, emissivity, and texture (TeX) physical triplets. This physical model leads to a TeX decompose-synthesize strategy that guarantees physical consistency and spatio-spectral noise resilience, in stark contrast to existing approaches. Moreover, our framework uses a forward-modeled atmospheric downwelling reference, along with spectral smoothness of emissivity and blackbody radiation, to enable spectral calibration and generation that would otherwise be elusive. Our extensive experiments on the outdoor DARPA Invisible Headlights dataset and in-lab FTIR measurements show that HAIR consistently outperforms state-of-the-art methods across denoising, inpainting, spectral calibration, and spectral super-resolution, establishing a benchmark in objective accuracy and visual quality.

### GPT总结
#### 文章内容
- 论文针对地基TIR-HSI存在的噪声、死谱带、谱采样不足与波长漂移等传感器退化问题，提出难以被忽视的热学物理一致性恢复需求。
- 核心思路是以HADAR rendering equation (HRE) 联合大气下行radiative transfer equation (RTE) 构建TIR-HSI物理成因模型，用温度-发射率-纹理(TeX)三元组进行分解-合成式恢复，并以RTE前向模拟的大气下行参考与发射率光滑性/黑体辐射先验进行谱标定与生成。
- 实验表明，所提HAIR在去噪、修复(inpainting)、谱标定与谱超分辨等任务上稳定优于现有方法，在客观指标与视觉质量上建立新基线。

#### 方法
- 物理建模：以HRE刻画目标热辐射与环境散射的叠加，并结合大气下行RTE，把TIR-HSI由单一潜变量扩展为TeX三元物理属性。
- TeX分解-合成策略：先物理解耦温度T、发射率e与纹理X，再据此重建HSI，确保热力学一致性并提升时空-光谱抗噪性，避免辐亮度域直接操作导致的TeX退化误判。
- 下行辐射引导的谱标定：利用LibRadtran前向生成的大气下行参考，将观测谱特征与RTE参考对齐以估计波长漂移，实现谱带标定、补全与增强，同时保持TeX结构。
- 先验约束：引入发射率谱平滑性与blackbody radiation物理先验，辅助谱校准与谱生成（含超分辨）。
- 适配多传感器退化：面向pushbroom与FTIR相机的条带、带依赖热噪声、谱欠采样与灾难性带损等进行统一恢复建模；训练/推理范式文中未明确说明。

#### 创新点
- 基于HRE+RTE的物理驱动TeX分解-合成恢复范式，从根源上保证热学一致性，相较传统辐亮度域恢复显著降低TeX退化风险。
- 提出“下行辐射引导”谱标定：将观测与RTE模拟参考（LibRadtran）对齐以估计波长偏移，并实现谱带校准、补全与增强。
- 利用发射率光滑性与黑体辐射先验，使得谱校准与谱生成（含超分辨）在弱标定场景下成为可能。
- 将去噪、inpainting、谱标定与谱超分辨统一到同一物理框架，在多种TIR-HSI退化与相机架构下提供稳健恢复。

#### 实验结论
- 任务与数据：在DARPA Invisible Headlights室外数据与实验室FTIR测量上，评估去噪、inpainting、谱标定与谱超分辨。
- 结果：HAIR在上述任务上“consistently outperforms state-of-the-art”，在客观准确度与视觉质量上建立基准。
- 作者结论：物理一致的TeX分解-合成与下行辐射引导校准为TIR-HSI恢复提供统一有效框架，显著提升HADAR相关应用的实用性。

## 关键词：reinforcement learning

## EvoGround: Self-Evolving Video Agents for Video Temporal Grounding
- **论文链接**: http://arxiv.org/abs/2605.13803v1
- **作者**: Minjoon Jung, Byoung-Tak Zhang, Lorenzo Torresani
- **原始摘要**: Video temporal grounding (VTG) takes an untrimmed video and a natural-language query as input and localizes the temporal moment that best matches the query. Existing methods rely on large, task-specific datasets requiring costly manual annotation. We introduce EvoGround, a framework of two coupled self-evolving agents, a proposer and a solver, that learn temporal grounding from raw videos without any human-labeled data. The proposer generates query--moment pairs from raw videos, while the solver learns to ground them and feeds back signals that improve the proposer in return. Through this self-reinforcing reinforcement-learning loop, the two agents are initialized from the same backbone and mutually improve across iterations. Trained on 2.5K unlabeled videos, EvoGround matches or surpasses fully supervised models across multiple VTG benchmarks, while emerging as a state-of-the-art fine-grained video captioner without manual labels.

### GPT总结
#### 文章内容
- 论文面向 Video Temporal Grounding (VTG) 的标签成本高、可扩展性受限问题，提出在无人工标注的原始视频上学习时间定位。
- 核心思路是构建互相促进的两代理框架：proposer 从原始视频生成 query–moment 对，solver 学习定位并回传信号反哺 proposer，形成自强化的强化学习闭环；两者从同一视觉语言骨干初始化。
- 在仅用2.5K未标注视频训练下，EvoGround 在多项 VTG 基准上达到或超过全监督模型，同时在细粒度视频描述上达到 SOTA；作者认为自进化带来超出单一训练目标的更广泛视频理解。

#### 方法
- 双代理协同：proposer 在无标签视频中选取时间片段并生成自然语言查询；solver 根据查询进行时间定位，并将反馈信号用于提升 proposer。
- 自强化 RL 闭环与迭代训练：两代理从同一骨干初始化，分两阶段交替更新，进行3次迭代；每次迭代 proposer 生成约9K对 query–moment 用于更新 solver。
- 奖励与调度：proposer 训练中逐步增大 δ（0→0.3→0.5）；奖励由格式、语义一致性与反馈三部分加权组成，权重 w_format=0.5、w_consistency=0.5、w_feedback=1.0。
- 模型与数据：以 Qwen2.5-VL-7B 为骨干，在 TimeRFT 的2.5K原始视频上训练；视频采样2 FPS，分辨率自适应至2.8M像素；单次迭代约24小时、4×A100 GPU。
- 推理流程或具体 RL 算法（如使用何种策略梯度/PPO等）、网络结构细节与损失形式：文中未明确说明。

#### 创新点
- 首次在 VTG 上通过“proposer–solver”耦合自进化的无标注强化学习范式替代人工标注：proposer 充当“自动标注者”，solver 的定位能力反哺 proposer 质量。
- 两代理共享骨干、在闭环中相互提升，除VTG外还“涌现”细粒度视频描述能力，无需任何人工文本标签。
- 以仅2.5K未标注视频实现与全监督模型比肩或超越的性能，显著降低数据依赖与标注成本。
- 实验评估采用95% bootstrap 置信区间，提升对比的可靠性（ReXTime 因官方测评未参与区间估计）。

#### 实验结论
- 任务与数据集：在五个 VTG 基准（Charades-STA、ActivityNet-Captions、TVGBench、ReXTime、E.T.Bench）和 TemporalBench（描述）上评测；对比 SFT 类与 RL 类 Video-LLMs（多数为7B规模）。
- 指标：VTG 用 R@n, IoU=m（m∈{0.3,0.5,0.7}）、mIoU、F1，并报告95%置信区间；描述用 CIDEr、BLEU、ROUGE、Sentence Transformer 相似度。
- 结果：EvoGround 在多个 VTG 基准上匹配或超越全监督模型，并在细粒度视频描述上达 SOTA；具体数值文中未明确说明。作者总结其无标签自进化范式具有较强通用性，但在超长视频上代价较高、仍受视频语料影响，且存在进一步扩展空间。
