# 2026-06-25 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Multi-Agent LLM Governance for Safe Two-Timescale Reinforcement Learning in SDN-IoT Defense
- **论文链接**: http://arxiv.org/abs/2604.01127v2
- **作者**: Saeid Jamshidi, Negar Shahabi, Foutse Khomh, Carol Fung, Mohammad Hamdaqa
- **原始摘要**: Software-Defined Networking (SDN) is increasingly adopted to secure Internet-of-Things (IoT) networks due to its centralized control and programmable forwarding. However, SDN-IoT defense is inherently a closed-loop control problem in which mitigation actions impact controller workload, queue dynamics, rule-installation delay, and future traffic observations. Aggressive mitigation may destabilize the control plane, degrade Quality of Service (QoS), and amplify systemic risk. Existing learning-based approaches prioritize detection accuracy while neglecting controller coupling and short-horizon Reinforcement Learning (RL) optimization without structured, auditable policy evolution. This paper introduces a self-reflective two-timescale SDN-IoT defense solution separating fast mitigation from slow policy governance. At the fast timescale, per-switch Proximal Policy Optimization (PPO) agents perform controller-aware mitigation under safety constraints and action masking. At the slow timescale, a multi-agent Large Language Model (LLM) governance engine generates machine-parsable updates to the global policy constitution Pi, which encodes admissible actions, safety thresholds, and reward priorities. Updates (Delta Pi) are validated through stress testing and deployed only with non-regression and safety guarantees, ensuring an auditable evolution without retraining RL agents. Evaluation under heterogeneous IoT traffic and adversarial stress shows improvements of 9.1% Macro-F1 over PPO and 15.4% over static baselines. Worst-case degradation drops by 36.8%, controller backlog peaks by 42.7%, and RTT p95 inflation remains below 5.8% under high-intensity attacks. Policy evolution converges within five cycles, reducing catastrophic overload from 11.6% to 2.3%.

### GPT总结
#### 文章内容
论文关注SDN-IoT防御的闭环耦合问题：缓解动作会改变控制器负载、队列与规则安装延迟，从而影响后续观测与系统稳定性。作者提出“两时间尺度”的治理框架：快时域由每交换机的PPO执行带安全约束的控制器感知型缓解，慢时域由多智能体LLM治理引擎以机器可解析的方式演化全局“政策宪法”Π。实验在异构物联网流量与对抗压力下表明，该方法在保持QoS与控制面稳定性的同时显著提升检测与稳健性；关键指标如Macro-F1、控制器积压峰值与RTT p95均得到改善。

#### 方法
- 快时域：每交换机去中心化PPO执行“控制器感知”缓解，采用显式安全约束与action masking限制高风险动作，以避免过度安装规则造成控制面过载。
- 慢时域：多智能体LLM治理引擎生成对全局政策宪法Π的机器可解析增量更新ΔΠ，编码可行动作集合、安全阈值与奖励优先级。
- 治理验证：对ΔΠ进行定向压力测试，仅在满足non-regression与硬安全条件时发布，实现fail-closed、可审计的策略演化，且无需改动RL参数。
- 系统建模：显式建模控制器服务率上限与动作延迟，将缓解—控制面—观测的耦合纳入闭环优化。
- 部署机制：政策演化与执行解耦；快时域策略受宪法Π约束，慢时域以周期性反思-验证-发布闭环更新Π。

#### 创新点
- 两时间尺度治理：将快速缓解与慢速政策治理解耦，用LLM驱动的“宪法”Π约束PPO行为，实现结构化、可审计的策略演化。
- 机器可解析治理增量：通过ΔΠ描述可行动作、安全阈值和奖励权重，并以non-regression与硬安全测试把关，更新无需重新训练RL。
- 控制器耦合显式纳入：在方法与评测中显式建模控制器服务率与延迟，将安全约束与action masking融入PPO，降低系统性风险与不稳定。
- 闭环系统级评测：在异构IoT流量与对抗压力下，面向QoS稳定性、尾部风险与控制面健康的系统级指标进行验证。

#### 实验结论
- 任务与数据：在异构IoT流量与高强度对抗压力的闭环SDN-IoT环境中评估；具体数据集名称与规模文中未明确说明。
- 核心结果：相较于不受限PPO与静态基线，Macro-F1提高9.1%与15.4%；最坏性能劣化下降36.8%；控制器backlog峰值下降42.7%；高强度攻击下RTT p95膨胀≤5.8%；无振荡失稳或控制器崩溃。
- 其他发现：治理迭代在5个周期内收敛，将灾难性过载从11.6%降至2.3%；各交换机F1分布一致（均值0.776–0.804，无显著差异p=0.27，d=0.32），最低为SW3的0.615。
