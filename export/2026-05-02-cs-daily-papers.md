# 2026-05-02 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## LaST-R1: Reinforcing Action via Adaptive Physical Latent Reasoning for VLA Models
- **论文链接**: http://arxiv.org/abs/2604.28192v1
- **作者**: Hao Chen, Jiaming Liu, Zhonghao Yan, Nuowei Han, Renrui Zhang, Chenyang Gu, Jialin Gao, Ziyu Guo, Siyuan Qian, Yinxi Wang, Peng Jia, Chi-Wing Fu, Shanghang Zhang, Pheng-Ann Heng
- **原始摘要**: Vision-Language-Action (VLA) models have increasingly incorporated reasoning mechanisms for complex robotic manipulation. However, existing approaches share a critical limitation: whether employing explicit linguistic reasoning that suffers from latency and discretization, or utilizing more expressive continuous latent reasoning, they are predominantly confined to static imitation learning that limits adaptability and generalization. While online reinforcement learning (RL) has been introduced to VLAs to enable trial-and-error exploration, current methods exclusively optimize the vanilla action space, bypassing the underlying physical reasoning process. In this paper, we present \textbf{LaST-R1}, a unified VLA framework that integrates latent Chain-of-Thought (CoT) reasoning over physical dynamics prior to action execution, along with a tailored RL post-training paradigm. Specifically, we propose \textbf{Latent-to-Action Policy Optimization (LAPO)}, a novel RL algorithm that jointly optimizes the latent reasoning process and the action generation. By bridging reasoning and control, LAPO improves the representation of physical world modeling and enhances robustness in interactive environments. Furthermore, an \textbf{adaptive latent CoT mechanism} is introduced to allow the policy to dynamically adjust its reasoning horizon based on environment complexity. Extensive experiments show that LaST-R1 achieves a near-perfect 99.8\% average success rate on the LIBERO benchmark with only one-shot supervised warm-up, significantly improving convergence speed and performance over prior state-of-the-art methods. In real-world deployments, LAPO post-training yields up to a 44\% improvement over the initial warm-up policy across four complex tasks, including both single-arm and dual-arm settings. Finally, LaST-R1 demonstrates strong generalization across simulated and real-world environments.

### GPT总结
#### 文章内容
- 论文针对VLA在复杂操控中仅用模仿学习训练、以及现有在线RL只优化动作而忽略物理推理的局限，提出在执行前进行物理潜在CoT推理并联合优化的范式。核心思路是构建LaST-R1框架，通过LAPO在RL中联合优化潜在推理token与动作生成，并引入自适应潜在CoT以动态调节推理步长。
- 结论显示，该方法在LIBERO基准上一枪SFT预热后达到99.8%平均成功率，收敛更快、性能优于SOTA；真实机器人四个复杂任务上，RL后训练相对预热策略最高提升44%，平均成功率约90%，且具有强泛化到新物体/背景/光照的能力。

#### 方法
- 模型架构：LaST-R1在动作生成前自回归地产生表征物理动态的潜在推理token，并以其作为条件并行解码动作；潜在token锚定于来自视觉基础模型[31]的全局“未来”表示以增强语义与空间先验。
- 强化学习算法：提出LAPO（Latent-to-Action Policy Optimization），将潜在推理与动作作为隐式/显式联合决策变量，通过联合的步级似然比进行优化，使环境回报能有效回溯并塑造内部推理空间。
- 自适应潜在CoT：根据环境复杂度动态调整推理步长，在需要高层规划时分配更多计算，在反应式操作时降低时延，平衡推理能力与推理开销。
- 训练流程：以Qwen3-VL-4B初始化，先在多源机器人操作数据集[32,33,34]进行大规模预训练，针对下游任务进行一次SFT预热（one-shot），随后开展在线RL后训练（使用LAPO）。
- 动作表征：输出SE(3)空间的动作片段；单臂为7-DoF（3维位置偏移、3维欧拉角姿态、1维夹爪），双臂任务相应扩展。

#### 创新点
- 在VLA中首次将“先推理后执行”的潜在CoT作为RL优化目标与动作联合优化，打通认知推理与低层控制，突破以往仅在动作空间做RL的范式。
- 提出LAPO，以联合步级似然比实现对潜在推理与动作的端到端信用分配，使奖励信号能直接塑形潜在物理推理过程。
- 设计自适应潜在CoT机制，按任务难度动态调节推理地平线，兼顾高精度规划与低时延执行。
- 将潜在推理token锚定到视觉基础模型的全局未来表征，强化对物理世界建模与鲁棒性。

#### 实验结论
- 模拟：在LIBERO基准上一枪SFT后达成99.8%平均成功率，收敛更快且显著优于既有方法；在LIBERO-Long单轨迹RL设定中，LaST-R1+LAPO达99.4%，Action-Only+PPO为88.2%。
- 真实机器人：在四个复杂任务（含单臂与双臂）中，LAPO后训练相对预热策略最高提升44%，平均成功率约90%。
- 泛化：在仿真与真实环境中均稳定优于基于PPO的纯动作RL策略；RL后训练实现对未见物体、背景与光照的零样本泛化。文中未明确说明更细的训练超参数与具体预训练数据集名称。
