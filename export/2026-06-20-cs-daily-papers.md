# 2026-06-20 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Generating Robot Hands from Human Demonstrations
- **论文链接**: http://arxiv.org/abs/2606.20549v1
- **作者**: Sha Yi, Nicklas Hansen, Xueqian Bai, Carmelo Sferrazza, Michael T. Tolley, Xiaolong Wang
- **原始摘要**: Robot learning has advanced rapidly in learning control, but learning the physical body of a robot remains much more difficult because jointly searching over design and control creates a very large combinatorial problem. Here, we present a data-driven framework for generating robot hands from human demonstrations. Instead of learning a complex controller together with each candidate design, we generate robot hand designs using the same simple control policy used after fabrication: matching fingertip positions through inverse kinematics. Using more than 4 million frames of human fingertip motion from everyday manipulation, our algorithm optimizes tree-structured robot hands to reproduce desired target motions. The framework produced both a 6-degree-of-freedom (DoF) general-purpose hand and lower-DoF task-specific hands with spatial four-bar mimic joints. To accelerate the search over designs, we trained a reinforcement-learning (RL) actor to propose good hand designs and joint angles, reducing search time from hours to minutes. We fabricated the mechanisms directly as one-piece articulated structures with print-in-place joints. In real-world experiments, the 6-DoF hand achieved highly accurate teleoperated fingertip tracking better than available commercial robot hands, whereas the specialized 3-DoF hands reproduced structured human and synthetic trajectories with reduced mechanical complexity. These results showed that large-scale human motion data can be used not only to train robot controllers but also as a reference for optimizing and generating the physical embodiment of robots.

### GPT总结
#### 文章内容
该论文面向“同时搜索机器人硬件与控制”的高维非凸难题，提出用大规模人类手部演示直接生成机器人手的硬件形态。核心思路是在训练与部署均使用同一简单控制（逆运动学匹配指尖位置），以人类拇指-食指指尖轨迹为目标，通过可微前向运动学与联合优化搜索树型手部参数与关节轨迹，并结合轨迹条件的RL actor加速设计。结果表明，框架可自动生成6-DoF通用手与带空间四杆（Bennett）从动联动的低DoF任务手，真实实验中6-DoF手的遥操作指尖跟踪精度优于商用品，3-DoF手以更低机械复杂度复现结构化轨迹。

#### 方法
- 输入与表示：以超过4百万帧日常操控的人类拇指-食指指尖6D轨迹为目标；候选手设计由硬件参数ϕ与关节序列q表征，经可微前向运动学g(ϕ, q)计算指尖位置。
- 联合优化目标：最小化L_track（指尖L1跟踪误差）+ λ_joint L_joint（关节平滑）+ λ_design（抑制过长连杆/正则化联动参数）+ λ_col（基于线段最近距离的碰撞项），并考虑关节限幅约束。
- 设计空间：以腕为根的二叉树型手（拇指/食指分支）；全驱型优化连杆长度、预留电机安装长度与关节朝向；低DoF型引入空间四杆Bennett模仿关节，用半角关系θ_c = f − 2 atan2(k sin(θ_p/2), cos(θ_p/2))进行从动耦合。
- 可微与几何一致性：训练时采用“软残差”放宽闭环约束以稳定梯度搜索，优化后通过非线性最小二乘回收满足几何闭合的四杆参数用于制造。
- 轨迹条件硬件生成：先以轨迹自编码器获得压缩上下文，再由actor按该上下文采样硬件与关节初始化，经过可微共设计评估后将actor均值朝最优样本更新，将设计时间由小时级降至分钟级；全驱情形用连续6D旋转表示保持端到端可微。

#### 创新点
- 部署一致的共设计范式：在训练与部署均使用同一“逆运动学指尖匹配”简单控制，避免为每个候选硬件另学复杂策略，直接以人类运动为硬件参考生成具身形态。
- 将人类运动用于“生成硬件”而非仅做“动作重定向/控制学习”，以大规模人类指尖轨迹驱动树型手的几何与自由度配置优化。
- 在低DoF手中引入空间四杆（Bennett）模仿关节并以软化闭环约束+事后几何回收的两阶段策略，兼顾优化可行性与可制造性。
- 轨迹条件的RL actor用于“摊销初始化搜索”，显著缓解非凸空间带来的敏感性，将设计搜索从小时级加速到分钟级。

#### 实验结论
- 数据与任务：使用超过4百万帧日常人类拇指-食指指尖轨迹进行训练与评估；面向通用遥操作与结构化目标轨迹复现两类场景。
- 关键结果：6-DoF通用手在仿真与真实中实现亚毫米级指尖跟踪与实时遥操作，且在指尖跟踪精度上优于商用机器人手；专用3-DoF手以更低机械复杂度准确复现人类与合成的结构化轨迹。
- 结论与效率：利用大规模人类运动数据可同时优化并生成机器人硬件具身；轨迹条件RL actor将硬件生成时间由小时级降至分钟级。其他实现细节（如具体对比基线、硬件成本等）文中未明确说明。
