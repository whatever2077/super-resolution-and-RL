# 2026-09-25 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Tractable Reinforcement Learning for Full Class of Signal Temporal Logic Specifications Using Spatiotemporal Tube Reward
- **论文链接**: http://arxiv.org/abs/2609.28396v1
- **作者**: Vaishnavi Jagabathula, P Sangeerth, Pushpak Jagtap
- **原始摘要**: This paper addresses the control problem for robotic systems, including non-holonomic and underactuated platforms operating under unknown dynamics and strict actuator limits to satisfy complex high-level specifications. We denote these high-level specifications using Signal Temporal Logic (STL) and propose a novel time-aware Reinforcement Learning (RL) framework that leverages the geometric properties of Spatiotemporal Tubes (STTs). While traditional analytical STT controllers often struggle to enforce input constraints, and existing RL approaches rely on memory-intensive state history, our method natively overcomes both limitations. By mapping the logical and temporal complexities of the full class of STL into time-varying geometric boundaries, we directly constrain the multidimensional system state without relying on scalar robustness metrics. Augmenting the state space with time, we train a time-aware Soft Actor-Critic (SAC) agent using a continuous, geometry-aware reward function that eliminates the need to explicitly evaluate complex logical semantics during execution. The proposed framework offers a history-free, computationally efficient approach to learn continuous control policies that ensure robust satisfaction of specifications while strictly adhering to system input constraints.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
