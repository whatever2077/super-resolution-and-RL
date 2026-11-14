# 2026-11-14 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation
- **论文链接**: http://arxiv.org/abs/2611.17329v1
- **作者**: Zeynep Yıldız, Satchit Chatterji, Ercan Atam, Erman Acar
- **原始摘要**: Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer constraint-satisfying reinforcement learning (RL) via differentiable symbolic supervision but assume a finite, discrete action space. We present a PLPG-inspired continuous allocation method that estimates the probability that the policy's own executed action satisfies the investment mandate, using reparameterized Monte Carlo sampling, and adds it to the training objective. No post-hoc enforcement mechanism intercepts actions at inference time and compliance is learned by the agent. Audited directly on deterministic mean actions with no correction, the policy reduces violations of a six-rule regime-conditional mandate from 96-98% for unconstrained RL and 33.4% for a reward-penalty baseline to 4.8%, showing that a continuous-action neurosymbolic policy can substantially internalize a symbolic mandate.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
