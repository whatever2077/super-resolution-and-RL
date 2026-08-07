# 2026-08-07 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Cardiac MRI Through-Plane Super-Resolution Guided by Reference and Memory
- **论文链接**: http://arxiv.org/abs/2607.07581v2
- **作者**: Shaoming Pan, Chenchuhui Hu, Leon Axel, Meng Ye
- **原始摘要**: Clinical cardiac MRI is commonly acquired with high in-plane resolution but coarse through-plane resolution to reduce scan time and accommodate breath-hold and cardiac-motion constraints, which limits 3D analysis and diagnostic accuracy. We propose STRMSR, a reference- and memory-guided through-plane super-resolution (SR) framework that reconstructs high-resolution (HR) cardiac volumes by leveraging HR reference views acquired from the same subject and intermediate SR results as the memory. Our method uses coarse-to-fine contextual matching to establish robust correspondence between low-resolution target and reference/memory images under spatial misalignment. A learnable patch-wise dynamic feature aggregation module predicts content-adaptive mixture weights for each local patch, effectively fusing dynamic information while suppressing unreliable feature transfers. The intermediate SR results stored in the memory bank ensure slice-to-slice consistency for the super-resolved 3D volume. Experiments on the WHS cardiac MRI dataset under two reference protocols, orthogonal-plane views and long-axis chamber views, demonstrate consistent improvements over baselines at 4x and 8x upsampling factors.Code is available at https://github.com/030108ming/STRMSR

### GPT总结
#### 文章内容
该论文针对临床 CMR 仅在层间方向（through-plane）分辨率较粗造成的三维分析受限问题，提出参考与记忆联合引导的 through-plane 超分辨框架 STRMSR。方法以同一受试者的 HR 参考视图为跨视角先验，并将中间 SR 结果作为“记忆”在层间传播，通过粗到细的上下文匹配与按块动态特征聚合实现稳健细节迁移与不可靠传递抑制。实验在 WHS 数据集、两种参考协议（orthogonal-plane views 与 long-axis chamber views）下，×4/×8 放大均较基线取得一致改进。

#### 方法
- 特征提取：将 HR 参考下采样到与目标 LR 一致的层厚，采用共享参数的 LR 分支与独立的 HR 分支构成双路 Swin Transformer Group（含 RSTB），对 LR 先在层向用 center-copy 上采样后构建多尺度特征金字塔。
- CFCM：在最粗尺度进行全局块级检索（多膨胀归一化相关），在局部区域进行 3×3 密集补丁匹配（余弦相似度），利用置信度加权的 fold 对 HR 参考特征进行变形；匹配中心通过最近邻插值逐级传播，并在更细尺度内局部细化。
- PDFA：对每个局部 patch 预测内容自适应混合权重（MLP+SoftMax）以融合目标/参考/记忆特征，选择性传递可靠细节并抑制错误迁移。
- 记忆引导：将中间 SR 切片结果存入 memory bank，作为额外参考在第三轴传播，强化层间一致性与体数据连贯性（受视频目标分割启发）。
- 训练/推理细节（损失函数、优化器、数据增广等）：文中未明确说明。

#### 创新点
- 将“参考视图引导 + 记忆传播”统一到 through-plane SR 中，既利用跨视角 HR 线索，又通过记忆机制提升层间一致性。
- 设计 CFCM 的粗到细双阶段匹配，在多尺度上逐级细化对应关系，较 McMRSR 仅复用 LR 对应关系的做法更鲁棒于空间失配。
- 提出按块动态特征聚合（PDFA），以可学习的内容自适应权重实现选择性信息融合并抑制不可靠特征传递。
- 引入基于中间 SR 结果的 memory bank 进行层间传播，面向 3D 体数据的连贯性优化，借鉴视频对象分割中的记忆思想。

#### 实验结论
- 任务与数据：在 WHS cardiac MRI 上验证，采用 orthogonal-plane views 与 long-axis chamber views 两种参考协议，评估 ×4 与 ×8 放大。
- 结果：相较多种基线在两种协议与两个放大倍率下均获得一致改进；具体数值与评价指标文中未明确说明。
- 作者结论与复现：方法提升了层间一致性与体数据连贯性；代码发布于 https://github.com/030108ming/STRMSR。

## 关键词：reinforcement learning

## Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning
- **论文链接**: http://arxiv.org/abs/2608.05144v1
- **作者**: Boxiu Li, Zimo Wen, Yijia Fan, Junxiang Lei, Sufeng Guo, Jiaao Wu, Ruize Tang, Mukai Li, Yifei Shen, Xiaoyu Chen, Wanbo Zhang, Runjing Gu, Yifei Gao, Yuheng Wu, Xuyao Huang, Zelong Zhao, Jiachen Zhang, Shibo Hu, Hangxi Guo, Yilin Chen, Yuzhe Zhang, Fan Yang, Chuan Wen, Xian Zhang, Xuanhe Zhou, Zhijie Deng
- **原始摘要**: Long-horizon reasoning requires an agentic runtime that can persist when evidence supports its current approach and pivot when measurements reveal failure, hidden constraints, or a misspecified objective. We present Argus, a persistent, self-evolving runtime in which Manager, Planner, Engineer, and Reviewer execute bounded missions over durable project state. Argus separates stable user intent from operational objectives, constraints, and verification criteria, and admits memories, skills, procedures, verifiers, routing decisions, and rejected routes only after role-owned review and, when available, task-native verification. Model weights remain fixed; self-evolution occurs through persistent runtime state and control policy, with autonomous execution between operator-owned escalation points. Across seven GPT-5.5 benchmark arenas, Argus achieves about 78% on SWE-Bench Pro versus 59% for Direct Copilot while using 1.41 times the aggregate tokens. After verification-gated self-evolution, mature SWE-Bench waves use 21% fewer solve-input tokens and 15% less active workflow time per task than startup waves, while recording 34 verifier recoveries and 22 strict review-loop rescues. Argus also reaches 76.8% on AARRI-Bench and a 28.0-point gap on mathematical data synthesis, with competitive GPU-kernel and language-model-training results. Beyond benchmarks, an optimized RWKV6 kernel was merged upstream; a multi-day mathematics campaign retained falsified routes and proof-backed frontier updates; and six paper pipelines completed 254 missions with 16 stage rollbacks. These results show that a fixed-weight, self-evolving harness can revise, recover, and accumulate verified approaches while producing structured trajectories for future supervised and reinforcement learning.

### GPT总结
#### 文章内容
- 论文聚焦长周期任务中的“持久推进+可验证转向”问题：在证据支持时坚持当前路线，在测量暴露失败、隐含约束或目标失配时安全地调整目标与路线。  
- 提出Argus，一个固定模型权重的通用代理运行时，采用Manager/Planner/Engineer/Reviewer分权机制，在持久项目态上执行有界Mission，并用验证门控将记忆、技能、流程、路由与被否决路线纳入可复用资产。  
- 核心思想是将稳定用户意图与可演化的操作性目标、约束、验证标准解耦，用角色边界与任务原生验证区分“理性转向”与“失败合理化”，并把自进化落在运行时状态与控制策略而非权重更新。  
- 结论显示该通用运行时在七个GPT-5.5基准场景上保持有效：SWE-Bench Pro约78%（对比Direct Copilot的59%，Token×1.41），AARRI-Bench达76.8%，并在自进化后降低Token与时延，且在真实工程与科研活动中产出经验证的可复用成果与结构化轨迹。

#### 方法
- 有界Mission + 持久项目态：以连续Mission在共享工作空间上推进，项目态持久化知识、事件日志、制品、待办、预算、守护进程与记忆。  
- 角色分权与三级面：Manager统筹目标、任务与Stage切换；Planner择定工作单元；Engineer实现与评估；Reviewer独立审查与裁决；控制/执行/记录三平面将调度、工作与记载解耦。  
- 契约形式化与意图分离：工作契约Kt = (ι, o_t, c_t, v_t)分离稳定意图ι与阶段性操作目标o_t、约束c_t与验证标准v_t，X_t记录澄清与优先级。  
- 验证门控的自进化：记忆、技能、流程、验证器、路由决策与被否决路线，只有经角色所有的评审且在可用时通过任务原生验证后方可纳入与复用；关键转向需证据、权限与记录背书。  
- 固定权重与自治执行：模型权重固定，自进化发生在运行时状态与控制策略；在显式升级点之间自治执行，低风险任务可采用Engineer自审。

#### 创新点
- 将“稳定用户意图”与“操作性目标/约束/验证标准”显式解耦，用验证作为区分“合理转向”与“目标漂移”的机制，而非事后质量过滤。  
- 提出验证门控的知识与路线资产化策略：不仅吸纳成功路径，也保留被证伪路线与路由决策，形成可追溯、可复用的研究与工程记忆。  
- 自进化落在运行时（状态与控制策略）而非模型训练，支持固定权重下的长期积累与迭代。  
- 通用、跨任务的代理运行时架构（四角色、三平面、持久项目态），生成可用于后续监督学习与强化学习的结构化轨迹数据。

#### 实验结论
- 基准性能：在七个GPT-5.5基准场景中，SWE-Bench Pro约78%（vs. Direct Copilot 59%），总Token×1.41；自进化后成熟Wave的solve-input Token下降21%，单任务活跃工作时间下降15%，并记录34次verifier恢复与22次严格审查环路救援。  
- 跨领域结果：AARRI-Bench达76.8%；数学数据合成上取得28.0点优势；GPU-kernel与语言模型训练任务表现具竞争力。  
- 超越基准的产出：优化的RWKV6内核合入上游Flash Linear Attention仓库；多日数学攻关保留被证伪路线与6次带证明的前沿更新；6条论文流水线自治完成254个Mission并发生16次Stage回滚；两个垂直方向通过外部检查器收敛（推理加速器在示范范围内获认证，材料方向以更简法替代已发表方案）。
