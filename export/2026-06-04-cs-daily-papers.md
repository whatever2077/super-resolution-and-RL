# 2026-06-04 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill
- **论文链接**: http://arxiv.org/abs/2606.03980v1
- **作者**: Tao Chen, Gangwei Jiang, Pengyu Cheng, Siyuan Huang, Yihao Liu, Jingwei Ni, Jiaqi Guo, Mengyu Zhou, Kai Tang, Junling Liu, Qinliang Su, Xiaoxi Jiang, Guanjun Jiang
- **原始摘要**: Reward models (RMs) provide critical feedback signals for LLM post-training, notably in reinforced fine-tuning (RFT) and reinforcement learning (RL) pipelines. However, current reward evaluation relies on heterogeneous criteria such as rule-based verifiers, ground-truth references, procedural checklists, and complex rubrics, where a unified mechanism to integrate all types of evidence remains unexplored. To this end, we propose Skill Reward Model (Skill-RM), a unified framework that reformulates reward modeling as the execution of a reusable Reward-Evaluation Skill. By treating reward computation as a structured agentic task, Skill-RM provides a consistent interface to orchestrate heterogeneous resources, dynamically selecting and aggregating evidence tailored to the specific requirements of each input. This approach enables the reward model to move beyond static evaluation, ensuring consistency and transparency across diverse tasks. Extensive experiments on reward benchmarks and downstream applications, including best-of-N selection and reinforcement learning, demonstrate that Skill-RM consistently outperforms traditional judge baselines. Our findings suggest that Skill-RM not only provides a unified solution for reward modeling but also achieves superior performance through the strategic and dynamic orchestration of evidence. The code is at https://github.com/Qwen-Applications/Skill-RM.

### GPT总结
#### 文章内容
- 论文关注当前奖励模型（RM）评估标准异构、缺乏统一整合机制的问题，提出将奖励计算重塑为可复用的 Reward-Evaluation Skill 的代理式任务。
- 核心思路是以统一接口组织并编排 rubrics、references、checklists、verifiers 与聚合规则，按输入自适应地选择与汇总证据，输出可溯源的 verdict+evidence。
- 实验表明，Skill-RM 在多种奖励评测基准和下游 best-of-N 选择与强化学习（RL）中，稳定优于传统 LLM-as-a-Judge 基线。
- 结论是：通过策略性、动态的证据编排，Skill-RM 同时实现统一化与性能提升。

#### 方法
- 将奖励建模任务化为代理执行的 Reward-Evaluation Skill，使用 SKILL.md 规范化技能描述（名称、适用条件、流程与输出字段）。
- 基于“diagnose → select → verify → aggregate”的流程：诊断所需标准，选择合适资源与工具，执行可验证检查，最后进行证据加权/规则化聚合得到奖励决策。
- 构建结构化资源库（Resource Bank）：包含 rubrics、ground-truth references、procedural checklists、rule/LLM-based verifiers 与 aggregation 规则，提供统一检索与调用接口。
- 推理阶段动态编排：按输入特征检索资源与工具（如执行器/沙箱、API），生成可审计的 evaluation trace，并产出 verdict + evidence，确保一致性与透明度。
- 集成场景：用于 RFT/RL 管线中的奖励反馈与下游 best-of-N 选择；具体训练细节与损失设计文中未明确说明。

#### 创新点
- 以可复用的 Agent Skill 抽象统一异构评估范式，将奖励建模从静态评分转为程序化的代理执行与证据编排。
- 引入结构化资源库与可执行流程，支持对 rubrics、references、checklists、verifiers 的输入自适应选择与聚合，形成一致的接口与可追踪的评估轨迹。
- 将“验证优先”的思想系统化（如代码测试、事实核验、规则检查），在统一框架下融合可验证信号与主观偏好。
- 提升评估过程的透明性与可控性，通过显式的 aggregation 规则与 evidence 输出降低黑箱性。

#### 实验结论
- 任务与数据：在“reward benchmarks”以及下游 best-of-N 选择与 RL 应用上进行评测；具体数据集名称与规模文中未明确说明。
- 结果：Skill-RM 在各基准与应用上均优于传统 judge baselines，表现出更高的一致性与稳健性；具体数值增益文中未明确说明。
- 作者结论：统一的 Skill-RM 通过动态证据编排带来更强的泛化与可靠性，适合作为多场景奖励建模的通用方案；代码开源于 https://github.com/Qwen-Applications/Skill-RM。
