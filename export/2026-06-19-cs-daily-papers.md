# 2026-06-19 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Native Active Perception as Reasoning for Omni-Modal Understanding
- **论文链接**: http://arxiv.org/abs/2606.19341v1
- **作者**: Zhenghao Xing, Ruiyang Xu, Yuxuan Wang, Jinzheng He, Ziyang Ma, Qize Yang, Yunfei Chu, Jin Xu, Junyang Lin, Chi-Wing Fu, Pheng-Ann Heng
- **原始摘要**: Passive models for long video understanding typically rely on a "watch-it-all" paradigm, processing frames uniformly regardless of query difficulty, causing computational cost to grow with video duration. Although interactive frameworks have emerged, they often rely on global pre-scanning, and their context cost still scales with video length. We propose OmniAgent, the first native omni-modal agent that formulates video understanding as a POMDP-based iterative Observation-Thought-Action cycle. OmniAgent executes on-demand actions to selectively distill audio-visual cues into a persistent textual memory, effectively decoupling reasoning complexity from raw video duration. To operationalize this, we introduce (1) Agentic Supervised Fine-Tuning to bootstrap native active perception via best-of-N trajectory synthesis with dual-stage quality control, and (2) Agentic Reinforcement Learning with TAURA (Turn-aware Adaptive Uncertainty Rescaled Advantage), which leverages turn-level entropy to steer credit assignment toward pivotal discovery turns. Crucially, OmniAgent exhibits positive test-time scaling, where performance improves as the number of reasoning turns increases, validating the efficacy of active perception. Empirical results across ten benchmarks (e.g., VideoMME, LVBench) demonstrate that OmniAgent achieves state-of-the-art performance among open-source models. Notably, on LVBench, our 7B agent outperforms the 10$\times$ larger Qwen2.5-VL-72B (50.5% vs. 47.3%).

### GPT总结
#### 文章内容
论文针对长视频理解中“看全再答”的高计算成本与交互式方法仍随视频时长线性/超线性增长的问题，提出将多模态理解建模为POMDP中的迭代Observation-Thought-Action（OTA）循环。核心思路是让单一原生omni-modal模型按需执行取证动作，选择性提取音视频线索并蒸馏为持久文本记忆，从而将推理复杂度与视频时长解耦。方法包含Agentic SFT与基于TAURA的Agentic RL以训练多轮主动感知与信用分配。结果显示测试时随推理轮次增加性能正向缩放，并在10个基准（如VideoMME、LVBench）上达成开源SOTA，其中7B模型在LVBench上以50.5%超越Qwen2.5-VL-72B的47.3%。

#### 方法
- 任务建模：将音视频探索表述为POMDP，采用迭代OTA循环；动作包括按需取帧、取音频段、取音视频片段，并将高维瞬时感知蒸馏到持久文本记忆中，直到证据充分作答。
- 模型形态：单一原生omni模型统一“感知-推理-行动”，环境仅负责原始媒体提取，模型自身完成多模态理解与决策，从机制上将推理复杂度与原始时长解耦。
- 监督阶段（Agentic SFT）：通过best-of-N轨迹合成与双阶段质量控制来引导和冷启动主动感知策略与多轮推理能力（具体质量控制细节文中未明确说明）。
- 强化学习阶段（Agentic RL with TAURA）：提出Turn-aware Adaptive Uncertainty Rescaled Advantage，利用回合级熵度量对优势进行重标定，将信用分配聚焦于关键“发现”回合，缓解GRPO在多轮场景中的优势同质化问题。
- 推理策略：体现正向测试时缩放（positive test-time scaling），可随问题难度自适应增加推理轮数以提升性能。

#### 创新点
- 原生主动感知范式：在单一模型内统一多模态感知、推理与行动，不依赖外部感知模块或全局预扫描，真正实现与视频时长解耦。
- POMDP+OTA+持久记忆：以POMDP为框架、OTA为循环、文本记忆为信息瓶颈，系统性地将高维音视频转化为紧凑可推理的状态表示。
- TAURA优化目标：基于回合熵的不确定性加权优势重标定，专门面向多轮代理的信用分配，解决GRPO在多轮轨迹上的优势混淆。
- Agentic SFT流程：best-of-N轨迹合成与双阶段质控的监督范式，用以高效启动“原生主动感知”能力。

#### 实验结论
- 任务与数据：在包含VideoMME、LVBench在内的10个视频理解基准上评测，覆盖长视频与多模态理解场景（其余数据集名称文中未明确说明）。
- 关键结果：OmniAgent在开源模型中达SOTA；在LVBench上，7B模型得分50.5%，超过10×更大的Qwen2.5-VL-72B的47.3%。
- 主要发现：模型呈现正向测试时缩放，增加推理回合数可显著提升性能，验证主动感知与多轮推理的有效性。
