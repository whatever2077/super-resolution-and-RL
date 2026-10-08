# 2026-10-08 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## QF3: Fast Flow RL with Filtered Q-Gradients
- **论文链接**: http://arxiv.org/abs/2610.08789v1
- **作者**: Chung Min Kim, Brent Yi, David McAllister, Hongsuk Choi, Himanshu Gaurav Singh, Jinkun Cao, Ken Goldberg, Pieter Abbeel, Carmelo Sferrazza, Angjoo Kanazawa
- **原始摘要**: Flow policies have become a standard policy class for learning robot behaviors from demonstrations, but reinforcement learning is still critical for improving pre-trained flow policies or learning them from scratch through interaction. We introduce QF3 (Fast Flow RL with Filtered Q-Gradients), an online off-policy RL algorithm that trains a flow policy with flow matching plus the critic's action gradient, backpropagated through a one-step prediction of the flow's output. To keep updates where the critic and this prediction are reliable, QF3 applies the critic gradient only to action dimensions that stay near the replay action. To our knowledge, QF3 is the first off-policy flow RL method to train humanoid locomotion policies from scratch and transfer them zero-shot to hardware. Paired with a high-throughput off-policy training recipe, it trains humanoid locomotion and motion-tracking policies with a 10x wall-clock speedup over FPO++, a recent on-policy flow RL method. We further apply QF3 to fine-tune pretrained flow-based manipulation policies on both ABC-Sim and Robomimic tasks. These results suggest that QF3 can both learn robot policies from scratch and refine those acquired from demonstrations. Website: https://qf3-rl.github.io/

### GPT总结
#### 文章内容
- 论文关注如何用强化学习高效训练或微调流式（flow/diffusion）策略，提出在线、离线采样（off-policy）的QF3以提升从演示学习到交互学习的能力与效率。
- 核心思路是将连续流匹配（flow matching, CFM）与critic的动作梯度结合，并通过对flow输出的一步预测进行反向传播，同时仅在与重放动作接近的动作维度上施加Q梯度（Filtered Q-Gradients）。
- 主要结论是：QF3在人体型（humanoid）行走与运动跟踪上实现对FPO++约10×的墙钟加速，首次在off-policy flow RL中从零训练出可零样本上机部署的双足策略，并在ABC-Sim与Robomimic中高效微调基于flow的操作策略。

#### 方法
- 训练目标：在flow策略上联合优化CFM损失与critic的动作梯度目标，通过对策略输出的一步预测进行反向传播以注入价值导向。
- 过滤Q梯度：对与重放动作相距较小的动作维度施加critic梯度（以clip半径α控制），屏蔽偏离较大的维度以提升梯度可靠性。
- 训练框架：基于CleanRL/TD3样式的离线采样管线，使用复数环境与重放缓冲、双Q（distributional twin-Q）与目标网络以稳定训练。
- 控制与集成：flow以少步Euler积分生成动作；联合使用CFM与“chunk-conditioned” CFM（权重λ_cfm）在噪声时间τ处训练，停止梯度穿过积分器的一部分以控制方差。
- 微调方案：在ABC-VLA体系上，仅训练DiT动作头的LoRA适配器（VLM与基头冻结），以低参数量（约229k）在线微调。

#### 创新点
- 提出Filtered Q-Gradients：按维度过滤的critic动作梯度，仅在局部可信区域更新，缓解off-policy分布漂移带来的梯度失真。
- 将Q梯度通过flow的一步预测进行可微传递，兼顾价值引导与flow匹配的生成式建模优势。
- 首个在off-policy范式下成功从零训练humanoid并零样本上机的flow RL方法，同时实现对FPO++约10×的墙钟加速。
- 提出高吞吐离线采样训练配方，并在视觉条件策略上用LoRA实现高效低开销的在线微调。

#### 实验结论
- Locomotion：在Holosoma的Unitree G1速度跟踪与单段舞蹈跟踪任务中，QF3相较FPO++达成约10×的训练墙钟加速；策略从仿真训练可零样本部署到硬件，完成约3分钟动态舞蹈。
- Manipulation：在ABC-Sim与Robomimic（如tool hang、transport等）上，QF3在线微调提升了flow策略的操作性能；具体数值增益文中未明确说明。
- 标准控制基准：在MuJoCo-v4（Hopper/Walker2d/Ant/Humanoid）上，QF3在统一TD3式训练框架下表现稳健；除加速比外的详细对比指标文中未明确说明。
