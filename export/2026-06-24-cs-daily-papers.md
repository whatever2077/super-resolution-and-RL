# 2026-06-24 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation
- **论文链接**: http://arxiv.org/abs/2606.23680v1
- **作者**: Sikai Li, Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding
- **原始摘要**: Humanoid loco-manipulation is often simplified into a stop-and-go process: walking to an object, stopping to manipulate it, and then resuming locomotion. It also commonly relies on low degree-of-freedom (DoF) end effectors that behave like an open-close grasp primitive. We introduce CoorDex, a learning pipeline that converts high-dimensional body and dexterous hand control into coordinated latent residual control, enabling high-DoF dexterous loco-manipulation on the move. Starting from simulated whole-body and hand demonstrations, CoorDex trains privileged motion tracking teachers for the humanoid body and dexterous hand, distills them into proprioception-conditioned latent priors, and uses the frozen priors as the action space for downstream residual reinforcement learning. A coordinated latent residual policy composes these priors through shared task context and separate body-hand residual heads, preserving natural whole-body motion while improving finger-level contact reliability. CoorDex enables a Unitree G1 humanoid with a 20-DoF WUJI hand to execute dexterous manipulation while in motion, including non-stop bottle grasping and carrying, fridge door opening on the move, and cube pick-and-turn. Ablations on the walk-grasp-carry task show that joint-space PPO, joint-space hand control, and monolithic latent prediction all fail under the same reward budget, while the latent-prior interface and coordinated residual structure make high-dimensional contact-rich loco-manipulation trainable. Project Page: https://skevinci.github.io/coordex/

### GPT总结
#### 文章内容
这篇论文针对“停走式”的人形机器人操控，将高维全身与高DoF手部控制转化为可训练的、在运动中持续执行的灵巧联合（loco-manipulation）问题。核心思路是：先用含特权信息的全身/手部跟踪教师学习，再蒸馏为仅依赖本体感知的体先验与手先验，并以“协调的潜变量残差”策略在下游RL中组合两者，从而分离腕部放置与指尖协调并保持全身自然运动。主要结论是：CoorDex在Unitree G1 + 20-DoF WUJI hand上实现了不停步抓取搬运、边退步开冰箱门、抓取并旋转方块等任务；在相同奖励预算下，关节空间PPO、仅体先验+手关节空间、以及单体潜残策略均失败，而CoorDex成功且手指接触更可靠、全身动作更平滑。

#### 方法
- 从仿真的全身与手部示范出发，训练含特权信息的运动跟踪教师；再通过变分瓶颈将教师蒸馏为仅以本体感知为条件的“体先验”和“手先验”及其解码器。
- 体先验负责步行、到达与腕部放置；手先验为“腕稳定化”设计，仅控制活跃手指关节，专注可复用的指尖协调模式。
- 将冻结的体/手先验作为下游动作空间，构建“协调的潜变量残差策略”：先由先验编码当前本体感知得到潜均值，再与目标相对几何、接触特征、当前本体状态一起输入共享协调主干，输出体/手两路残差头。
- 将两路残差加到对应先验潜均值后解码为关节目标；体残差调节步态、躯干与腕放置，手残差细化手指预形、闭合与接触。
- 训练采用残差强化学习，在统一的任务奖励与环境设置下优化策略；具体RL算法对CoorDex本身文中未明确说明（对照基线包含关节空间PPO）。

#### 创新点
- 体-手因子化先验与“腕稳定化”手先验：显式将腕部全身侧放置与手指侧灵巧分离，减少手先验对腕轨迹的容量占用，聚焦指尖协调。
- 冻结潜先验作为动作接口的“潜残”框架：在高维、接触丰富的联合任务中显著降低探索难度，使残差RL可训练。
- 协调结构设计：共享协调主干+体/手分头残差，避免单体潜残带来的耦合与动作抖动，保持全身运动的自然性同时提升手部接触稳定性。
- 教师-学生蒸馏与变分瓶颈结合：由特权跟踪教师蒸馏出仅依赖本体感知的潜先验，兼顾可表达性与可控性。

#### 实验结论
- 任务与平台：在Isaac Lab构建的高DoF灵巧联合任务，包括 WALKGRAB（不停步走-抓-搬）、边退步开冰箱门、walk-pick-turn；平台为Unitree G1 humanoid + 20-DoF WUJI hand。是否包含实机验证文中未明确说明。
- 关键对比（WALKGRAB，同一奖励预算与环境）：All Joint Space无法抓取；Body Prior + Hand Joint Space常在目标附近减速/停下，难以实现不停步灵巧；Monolithic Latent Residual成功率0.00、Action rate 0.40、Fall 0.02；CoorDex成功率0.55、Action rate 0.22、Fall 0.00，体现更平滑自然的全身动作与稳定抓取。
- 非停走性分析：在目标相对位置dt≈0附近，CoorDex前向速度约0.25 m/s，表明并非通过停下完成抓取。指标包括Reach/Grasp/Stop/Fall。
