# 2026-09-10 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Entropy-Regularized Rank-Masked Policy Optimization for Test-Time Reinforcement Learning in Code Generation
- **论文链接**: http://arxiv.org/abs/2609.09135v1
- **作者**: Jiacheng Xu, Feng Chen, Xiuneng Xu, Bo An
- **原始摘要**: Existing methods for test-time reinforcement learning (TTRL) derive rewards from answer-level self-voting on unlabeled test-time tasks with canonical answers, but this breaks down for code generation because programs cannot be compared by surface form and therefore do not directly provide a usable training signal. To make TTRL applicable to code generation, we propose probe-driven TTRL, which constructs output-free probe inputs from the problem statement, executes candidate programs on these probes, and defines a Probe Consensus Reward (PCR) from the resulting behavioral agreement. PCR provides a behavioral training signal for open-vocabulary programs, but it is not a fully reliable verifier and remains susceptible to reward hacking through spurious consensus. We therefore introduce Entropy-Regularized Rank-Masked Policy Optimization (ERPO), which converts low PCR into conservative negative updates through rank masking and controls policy drift with an entropy ceiling. On coding benchmarks, ERPO substantially improves pass@1 and pass@k in both in-domain adaptation and zero-shot transfer.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
