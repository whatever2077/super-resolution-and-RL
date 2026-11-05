# 2026-11-05 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## PolicyIK: High-Precision Inverse Kinematics for Robot Arms with Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2611.05372v1
- **作者**: Yuhan Liu, Xinqi Liu, Zixuan Dong, Keith W. Ross, Shenji Wan
- **原始摘要**: Inverse kinematics (IK) converts end-effector pose commands into joint motion, and many vision-language-action (VLA) policies rely on it to act on a given arm and to transfer across embodiments. Precise IK remains laborious: redundancy and singularities complicate the inverse mapping, execution depends on hand-tuned controllers, and training data on physical robots are costly to collect. We present PolicyIK, a goal-conditioned reinforcement learning policy for high-precision IK. It updates joint-position references from pose feedback and observes its accumulated reference relative to the measured joints, so it can retain the offset that the position controller needs at rest. Two-scale pose errors with an error-dependent action gain resolve millimeter residuals while preserving large motions. Progress and dwell rewards teach it to both reach the tolerance and stay within it. In simulation, a single attempt by the trained PPO policy keeps the mean errors over the final second within 1 mm and 0.2° on 93.5% of held-out tasks, and a deployment protocol raises success to 98.9%. When trained directly on a physical arm with an off-policy RL learner, PolicyIK achieves higher reaching and holding success than all four classical IK controllers under the same time budgets. In simulated pick-and-place, PolicyIK executes the end-effector commands of the $π_{0.5}$ VLA policy with 95.7% success. These results show that reinforcement learning can provide high-precision inverse kinematics for robot arms. Code is available at https://github.com/Tinaliu0123/PolicyIK.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
