# 2026-10-24 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## GigaBench: Benchmarking Learnable Representations for Gigapixel Image Compression and Super-Resolution
- **论文链接**: http://arxiv.org/abs/2610.31644v1
- **作者**: Matteo Fusconi, Alex Costanzino, Pierluigi Zama Ramirez, Luigi Di Stefano
- **原始摘要**: Learnable Representations (LRs) can fit parametric families of functions to diverse kinds of signals. These emergent neural-native data formats are gathering interest in the scientific community due to their compactness, resolution-agnosticism and amenability to direct neural processing. On the other hand, gigapixel images are becoming increasingly widespread across a variety of scientific, cultural, and industrial domains. In this paper, we present GigaBench, the first benchmark and experimental evaluation focused on deploying LRs with gigapixel imagery. GigaBench includes images collected, acquired, and synthetically rendered across diverse domains, and addresses image compression and super-resolution. We adapt a representative set of LRs, spanning Implicit, Hybrid, and Explicit methods, so as to operate reliably at the gigapixel scale on consumer hardware. Through systematic evaluation across reconstruction quality, model size, compression and inference times, we identify consistent trends across methods and suggest actionable guidance for future investigation.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## How Does RL Post-training Induce Skill Composition? A Case Study on Countdown
- **论文链接**: http://arxiv.org/abs/2512.01775v2
- **作者**: Simon Park, Simran Kaur, Sanjeev Arora
- **原始摘要**: While reinforcement learning (RL) successfully enhances reasoning in large language models, its role in fostering compositional generalization (the ability to synthesize novel skills from known components) is often conflated with mere length generalization. To this end, we study what RL post-training teaches about skill composition and how the composition structure affects the skill transfer. We focus on the Countdown task (given n numbers and a target, form an expression that evaluates to the target) and analyze model solutions as expression trees, where each subtree corresponds to a reusable subtask and thus can be viewed as a "skill." Tracking tree shapes and their success rates over training, we find: (i) out-of-distribution (OOD) generalization to larger n and to unseen tree shapes, indicating compositional reuse of subtasks; (ii) the order of skill acquisition depends upon the composition structure---models master shallow balanced trees (workload is balanced between subtasks) before deep unbalanced ones, with persistent fragility on right-heavy structures for a fixed composition depth. Our diagnostic reveals what is learned, in what order, and where generalization fails, clarifying how RL-only post-training induces OOD generalization beyond what standard metrics such as pass@k reveal. To study the implications of our findings for real-world tasks, we present a preliminary study on formal theorem proving.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
