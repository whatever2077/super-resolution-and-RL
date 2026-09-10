# 2026-09-11 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2604.10701v2
- **作者**: Zikang Shan, Han Zhong, Liwei Wang, Li Zhao
- **原始摘要**: Credit assignment is a central challenge in reinforcement learning (RL). Classical actor-critic methods address this challenge through fine-grained advantage estimation based on a learned value function. However, learned value models are often avoided in modern large language model (LLM) RL because conventional discriminative critics are difficult to train reliably. We revisit value modeling and argue that this difficulty is partly due to limited expressiveness. In particular, representation complexity theory suggests that value functions can be hard to approximate under the one-shot prediction paradigm used by existing value models, and our scaling experiments show that such critics do not improve reliably with scale. Motivated by this observation, we propose Generative Actor-Critic (GenAC), which replaces one-shot scalar value prediction with a generative critic that performs chain-of-thought reasoning before producing a value estimate. We further introduce In-Context Conditioning, which helps the critic remain calibrated to the current actor throughout training. GenAC improves value approximation, ranking reliability, and out-of-distribution generalization, and these gains translate into stronger downstream RL performance than both value-based and value-free baselines. Overall, our results suggest that stronger value modeling is a promising direction for improving credit assignment in LLM reinforcement learning.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
