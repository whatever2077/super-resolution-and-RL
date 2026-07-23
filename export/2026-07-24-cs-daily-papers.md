# 2026-07-24 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2607.20399v1
- **作者**: Nicolas Kosanovic, Jordan Dowdy, Jean Chagas Vaz
- **原始摘要**: Full-sized humanoid robot capabilities have grown exponentially in recent years, aiming towards general-purpose deployment in human environments. A popular control method used by manufacturers utilizes Virtual Reality for upper-body teleoperation and Reinforcement Learning for lower-body balance and locomotion control. As a result, a single remote operator can see, manipulate, and navigate about a real, distant physical environment. This powerful control stack is often relegated to expensive full-sized robots, many of which are inaccessible to the research community. Miniature humanoids are more prevalent, but employ less biomimicry in their design (e.g. fewer sensors, Degrees of Freedom, etc) and lack similar developments. This paper describes a compliant full-body telepresence control stack developed from the ground up for miniature humanoids. Framework experimentation on ROBOTIS OP3 hardware showcases walking at speeds up to 0.45 m/s independent of arm motions. Tele-loco-manipulation is demonstrated via a cube relocation experiment with an expert human operator. On average, the teleoperated system moved 2 different 40 g cubes within 10 mins, walking a total distance of 5 m. Overall, the developed system shows potential for miniature humanoid tele-loco-manipulation.

### GPT总结
#### 文章内容
- 论文面向小型人形机器人缺乏可用的“VR上肢遥操作 + RL下肢平衡/行走”的全身遥在（telepresence）控制栈这一问题，旨在为低成本平台提供可用于采集演示数据与原型验证的tele-loco-manipulation能力。
- 核心思路是：用VR实现操作者的头手姿态到机器人上肢的逆解映射，同时用强化学习训练的下肢行走/平衡控制器在存在扰动和上肢运动时保持稳定；在关节侧叠加基于PD的阻抗控制并结合DYNAMIXEL执行器的数据驱动建模以保证硬件安全与顺应。
- 主要结论是：在ROBOTIS OP3上实现了独立于手臂运动的稳定行走（最高0.45 m/s），并由专家操作者完成了“移动盒子”的tele-loco-manipulation演示（10分钟内搬运2个不同的40 g方块、累计步行5 m），显示出面向小型人形机器人的可行性与潜力。

#### 方法
- 系统架构：VR HMD与手柄采集头手6D姿态→多目标IK生成上肢关节参考→RL步行/平衡控制器输出下肢行为→全身PD阻抗控制实现顺应；通过Unity + ROS + Unity Robotics插件进行状态与指令流传输。
- 具身化与映射：将虚拟OP3模型按操作者肩宽与身高缩放；采用带梯形速度曲线的多目标IK [28]，同时考虑关节限位与自碰撞避免，确保上肢跟随与安全性。
- 硬件/软件链路：VIVE Pro 2 + SteamVR Basestation 2.0进行头手追踪；机器人端为ROBOTIS OP3（20 DoF，DYNAMIXEL XM430-W350-R），替换VR180双鱼眼USB相机增强临场；机载i7 NUC与OpenCR（含9 DoF IMU）。
- 执行器与顺应：基于数据驱动建模的DYNAMIXEL XM430力矩控制；在关节侧实现全身PD阻抗控制；为适配目标平台进行硬件改造与底层软件重写，提升安全性与可控性。
- RL训练：通过在训练中加入随机扰动获得鲁棒行走/平衡策略；具体算法、观测/奖励设计、训练超参数与仿真环境细节文中未明确说明。

#### 创新点
- 面向小型人形（以ROBOTIS OP3为代表）从零构建的“VR上肢遥操作 + RL下肢行走/平衡 + 全身阻抗”一体化tele-loco-manipulation控制栈，弥补小型平台在全身遥在控制上的空白。
- 提出针对DYNAMIXEL XM430的 数据驱动力矩建模与链式执行器全身PD阻抗控制，使低成本硬件上实现可顺应、可安全的全身控制。
- 在Unity-ROS流水线中集成具身化缩放与带运动学速度轮廓的多目标IK，兼顾低DoF硬件的可达性、安全性与操作流畅度。
- 将商用VR设备（VIVE Pro 2、VR180相机等）与RL步行控制整合于小型人形平台，为低成本采集teleoperation示范数据提供可复用框架。

#### 实验结论
- 平台与任务：在ROBOTIS OP3上验证了独立于上肢运动的行走与全身遥操作；核心任务为远程“方块搬运”演示。
- 关键结果：实现最高行走速度0.45 m/s；专家操作者在10分钟内搬运2个不同的40 g方块，累计步行约5 m。
- 作者结论：所提出的VR+RL全身控制栈在小型人形机器人上可行且具潜力，为后续小型人形的tele-loco-manipulation与数据采集铺路；更细节的性能对比、消融与RL训练配置文中未明确说明。
