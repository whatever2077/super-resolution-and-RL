# 2026-06-27 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Reinforcement Learning without Ground-Truth Solutions can Improve LLMs
- **论文链接**: http://arxiv.org/abs/2606.27369v1
- **作者**: Yingyu Lin, Qiyue Gao, Nikki Lijing Kuang, Xunpeng Huang, Kun Zhou, Tongtong Liang, Zhewei Yao, Yi-An Ma, Yuxiong He
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR) for training LLMs typically rely on ground-truth answers to assign rewards, limiting their applicability to tasks where the ground-truth solution is unknown. We introduce a \textbf{R}anking-\textbf{i}nduced \textbf{VER}ifiable framework (RiVER) that trains LLMs on score-based optimization tasks without ground-truth solutions, using deterministic execution feedback as continuous-valued supervision. When applying group-relative RL to such continuous rewards, we identify two key challenges: \emph{scale dominance}, where uncalibrated score magnitudes across test instances distort policy updates, and \emph{frequency dominance}, where repeatedly sampled suboptimal solutions can outweigh rare but stronger candidates. RiVER addresses these challenges with calibrated reward shaping that uses instance-wise comparisons and emphasizes top-ranked solvers while retaining bounded feedback for other valid solutions. We train on 12 AtCoder Heuristic Contest tasks and evaluate on Algorithm Engineering Benchmark (ALE-Bench), LiveCodeBench, and USACO. RiVER advances Qwen3-8B and GLM-Z1-9B-0414 by 8.9\% and 9.4\% in ALE rating rank. More importantly, despite training exclusively on score-based tasks without any ground-truth solutions, RiVER also improves the backbones across exact-solution benchmarks such as LiveCodeBench and USACO by an absolute average improvement of 2.4\% and 3.5\%. By contrast, baselines trained with raw execution scores improve ALE rating but fail to transfer to exact-solution benchmarks. These results suggest that score-based optimization tasks, combined with proper reward calibration, can serve as effective training environments for general coding ability without ground-truth solutions.

### GPT总结
#### 文章内容
- 论文关注RLVR对“答案匹配”的依赖，提出在无标准答案的score-based优化任务上训练LLM的RiVER框架，用确定性执行反馈作为连续监督信号。
- 作者识别了在对连续分数应用group-relative RL时的两大问题：scale dominance与frequency dominance，并通过基于实例的比较与校准的奖励塑形加以缓解。
- 在12个AtCoder Heuristic Contest任务上训练后，RiVER在ALE-Bench显著提升，并能迁移提升LiveCodeBench与USACO等“精确答案”基准。
- 结论：只要进行恰当的奖励校准，score-based优化任务可以在无ground-truth的条件下有效提升通用编程能力。

#### 方法
- 构建“排名诱导的可验证环境”：对同一隐藏实例采样多份候选求解器，确定性执行，进行约束检查与目标函数评估，无需gold code或gold output。
- 奖励校准与实例内比较：对每个实例进行组内比较与标准化，缓解不同实例分数量级不一致引发的scale dominance。
- 排名强化与有界反馈：强调top-ranked解的贡献，同时对其他可行解提供有界反馈，抑制频繁但次优样本对梯度的不当主导（frequency dominance）。
- 采用group-relative RL对连续奖励进行优化更新，将相对表现转化为策略梯度信号。
- 训练设置：仅使用12个AtCoder Heuristic Contest的score-based任务进行训练，未使用任何ground-truth解。

#### 创新点
- 将RLVR从“答案匹配”扩展到“无标准答案的score-based可验证监督”，以执行反馈驱动学习。
- 系统性地提出并分析连续奖励下group-relative RL的两类偏置：scale dominance与frequency dominance。
- 设计基于实例比较的奖励校准与top-rank加权策略，并保持对其它可行解的有界反馈，兼顾稳定性与探索。
- 证明经校准的score-based训练不仅提升ALE-Bench，也能迁移到LiveCodeBench与USACO，而“原始分数训练”基线无法实现该迁移。

#### 实验结论
- 任务与数据：在12个AtCoder Heuristic Contest任务上训练，评测于Algorithm Engineering Benchmark (ALE-Bench)、LiveCodeBench与USACO。
- 主要结果：在ALE rating rank上，Qwen3-8B与GLM-Z1-9B-0414分别提升8.9%与9.4%；在LiveCodeBench与USACO上分别实现绝对平均+2.4%与+3.5%的提升。
- 作者结论：与使用原始执行分数训练的基线相比，RiVER的奖励校准带来跨基准的泛化与迁移收益，表明无ground-truth的score-based优化任务可作为有效的LLM编程能力训练环境。
