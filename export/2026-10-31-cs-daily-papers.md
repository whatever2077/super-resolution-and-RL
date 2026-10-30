# 2026-10-31 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Coupled Guidance for Flow Matching
- **论文链接**: http://arxiv.org/abs/2610.40109v1
- **作者**: Mateo Clémente, Léo Maxime Brunswic, Rui Heng Yang, Amir Rasouli
- **原始摘要**: Guidance methods are essential tools for steering the generation process in diffusion models, improving the generalizability of stochastic robotic controllers and enabling high-quality controlled image synthesis. Despite strong parallels between flow-matching and diffusion, integrating guidance into flow-matching models remains quite challenging. Recent work has proposed general guidance frameworks for flow-matching, however, they are direct adaptations of diffusion guidance methods and can prove unstable. In this work, we conduct a theoretical analysis of guidance in flow-matching and show that a naive translation of diffusion-based guidance to flow-matching breaks the coupling distribution used during training, resulting in weaker control over sampling accuracy. Building on this insight, we propose Coupled Guidance, a flow-matching-specific guidance mechanism derived from a geometric perspective that leverages the coupling structure inherent to flow-matching training. To validate the effectiveness of our approach, we conduct extensive experimentation on a custom robotic collision avoidance task using ManiSkill3, four robotic dexterous manipulation tasks from the Adroit benchmark, and three image generation tasks, namely inpainting, super-resolution, and deblurring, using the ImageNet-128 and CelebA-HQ-256 datasets. Our findings show that our framework improves sample quality and guidance stability across all tasks, without imposing any additional overhead.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender
- **论文链接**: http://arxiv.org/abs/2610.40627v1
- **作者**: Qiyao Ma, Xiaodong Liu, Weiwei Yang, Mingqian Feng, Chengquan Guo, Jialin Song, Carolyn Buractaon, Zhe Zhao, Junshan Zhang, Sandeep Atluri, Christopher White, Jianfeng Gao
- **原始摘要**: Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model's first few output tokens, and existing defenses inherit the weakness, supervising the surface form of the response without ever giving the model an explicit safety decision to learn. We take the opposite view of shallowness: if a short span determines the trajectory of an entire response, that span is the highest-leverage place to intervene, and the defender can occupy it first. We propose Assess $\to$ Decide $\to$ Respond, a framework in which the defender assesses the user's intent, commits to an explicit, parseable safety decision, and only then generates a reply conditioned on it, with the commitment trained by reinforcement learning at the payload turn. Because the decision is a token span, the reward can be a rule: a self-verified reward checks the committed label against the conversation's known nature, requiring no judge and no annotation, while the same format also supports an LLM-as-judge reward over a graded decision space with safe redirection. Across two model families and fourteen benchmarks spanning safety, utility, and helpfulness, our defenders achieve the strongest multi-turn safety in a controlled comparison, maintaining their lead in safety while preserving utility at a modest cost to helpfulness. A per-token KL analysis and interventional probes confirm why this works: training concentrates its effect on the brief deliberation that sets a response's trajectory, and the decision committed there is a causal control point. The very shallowness attackers exploit becomes the mechanism of defense.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
