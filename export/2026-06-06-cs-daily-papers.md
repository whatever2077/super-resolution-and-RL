# 2026-06-06 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
- **论文链接**: http://arxiv.org/abs/2606.06491v1
- **作者**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding
- **原始摘要**: Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion. Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache reuse, or reinforcement learning only shift the policy from one fixed speed to another, and leave deceleration almost unexplored. We observe that the magnitude of each predicted action already governs how fast the robot moves, opening a direct route to controllable execution speed. We turn this observation into TempoVLA, a single VLA whose execution speed is controlled by an explicit condition. TempoVLA combines two coupled components. (1) A data-side Variable-Speed Trajectory Augmentation (VSTA) that re-times demonstration to any target speed by merging or splitting actions while preserving its motion semantics. (2) A model-side conditioning mechanism that feeds the speed to the policy. Statistics show that VSTA reaches the requested speed with negligible motion error. Experiments in simulation and on real-world tasks demonstrate that TempoVLA achieves flexible speed control in both directions, while VSTA additionally boosts the default $1\times$ performance via better data utilization. Furthermore, by cooperating with a large multimodal model, TempoVLA realizes dynamic speed control, accelerating through low-risk phases and decelerating for high-risk ones.

### GPT总结
#### 文章内容
该论文关注现有 Vision-Language-Action (VLA) 模型只能继承演示数据的单一固定执行速度的问题，难以在真实操作中按需加速与减速。核心思路是利用“动作幅值决定执行速度”的观察，提出TempoVLA：通过数据侧的Variable-Speed Trajectory Augmentation (VSTA)对示范轨迹按目标速度重定时，以及模型侧将标量速度s显式注入以缩放动作幅值，在不改动低层控制器的前提下实现速度可控。主要结论是TempoVLA在仿真与真实任务中实现双向速度控制，VSTA能以可忽略的运动误差达到目标速度，并作为数据增广提升默认1×性能；与大型多模态模型（VLM）协同可实现动态速度调度。

#### 方法
- 问题建模：在标准模仿学习框架下，令策略πθ接收(o, s)，其中s∈R+为显式速度条件；目标是在不改变低层控制器的情况下，使s>1加速、s<1减速、s=1为默认速度。
- 数据侧（VSTA）：在线将任意示范重定时到目标速度s，通过合并相邻动作以加速、或将动作拆分为更小步幅以减速，同时保持运动语义不变，生成多速度增广数据集。
- 模型侧条件注入：将标量速度s作为条件输入以缩放预测动作的幅值，论文提到三种注入方案，但具体实现细节文中未明确说明。
- 训练与设置：在速度集合{0.75, 1, 1.25, 1.5}×上训练单一TempoVLA策略，并与单速1×基线比较；损失为模仿学习目标（回归或flow-matching）。
- 推理与控制：策略输出动作序列（chunk），每次执行前10步后再查询；动作为8维（7维关节速度+1维夹爪），低层控制器保持不变，确保VSTA可直接作用于线性可合成的动作空间。

#### 创新点
- 提出VSTA：通过“合并/拆分动作”在数据侧对轨迹进行任意速度重定时，保证运动语义一致，形成在线、多速度的数据增广机制。
- 提出显式速度条件的VLA：以标量s控制动作幅值，实现同一策略的双向速度控制；且对现有VLA架构轻量可插拔，无需新数据采集与架构重训。
- 发现与验证：变量速度训练本身成为有效增广，能系统性提升默认1×的成功率；速度控制对具体条件注入机制相对不敏感。
- 将“速度”作为高层推理的新控制通道：与VLM协同，实现基于风险阶段的动态加减速调度。

#### 实验结论
- 设定：在7-DoF Franka臂+1-DoF夹爪平台上，5个任务（含4类抓放与1个可变形物体任务），每任务50条示范，按各速度进行10次测试；同时在LIBERO与真实场景开展实验。
- 结果：TempoVLA在仿真与真实中实现灵活的双向速度控制；统计显示VSTA能以可忽略的运动误差达到目标速度，并进一步提升默认1×性能。
- 拓展与限制：与VLM协同可实现无需人干预的动态速度调度；高速度端存在由低层控制器带宽导致的加速饱和现象。
