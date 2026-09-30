# 2026-10-01 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## GTRL: Grounding Divide-and-Conquer Value Learning with Temporal Differences
- **论文链接**: http://arxiv.org/abs/2609.33259v2
- **作者**: Abdul Monaf Chowdhury, MD Sameer Iqbal Chowdhury, Shifat E Arman, Md Mehedi Hasan
- **原始摘要**: In offline goal-conditioned reinforcement learning (GCRL), divide-and-conquer scales to long horizons by joining two shorter segments at a subgoal. However, under stochastic dynamics, the base case of this rule values the luckiest trajectories through the data. The subgoal must also lie on a shared trajectory, so a state-goal pair that no trajectory connects gets no value update at all. To address both, we present Grounded Transitive RL (GTRL), an offline GCRL value learning algorithm that grounds the divide-and-conquer update with a one-step TD target. Over a single step, TD is correct, as its target averages over the successors and needs no subgoal. GTRL adds this target to the composition rather than replacing it, so every pair receives an update, and the composition still carries the long horizon. GTRL also corrects the bias from hindsight relabeling by reweighting each goal against how reachable it was from other successors. We evaluate our algorithm on nineteen OGBench tasks spanning stochastic, deterministic, and stitching environments, where it achieves the highest average success rate. Code will be released soon.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
