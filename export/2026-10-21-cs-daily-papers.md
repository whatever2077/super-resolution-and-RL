# 2026-10-21 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Time-Correlated Video Bridge Matching
- **论文链接**: http://arxiv.org/abs/2510.12453v4
- **作者**: Viacheslav Vasilev, Arseny Ivanov, Nikita Gushchin, Maria Kovaleva, Alexander Korotin
- **原始摘要**: Bridge Matching (BM) learns a stochastic transport between two data distributions and is therefore a natural tool for data-to-data tasks such as video frame interpolation, image-to-video generation, and video super-resolution. Existing bridge models for video, however, use a reference process that treats the frames of a clip independently, so temporal structure enters only through the network or the choice of the bridge endpoints. We propose Time-Correlated Video Bridge Matching (TCVBM), which places temporal structure into the reference process itself: the frames of a clip are coupled by a linear SDE whose drift is a discrete Laplacian along the time axis, and known frames enter as boundary conditions. The transition and bridge distributions remain Gaussian and available in closed form, so training and sampling are as simple as in standard BM, which is recovered in the limit of zero coupling. A spectral analysis shows that the prior damps high temporal frequencies, injects temporally smooth noise, and relaxes towards a boundary-determined profile, such as the linear interpolation between key frames. In controlled comparisons with frame-independent bridges under identical architectures and training budgets, TCVBM improves most automatic metrics for frame interpolation (Moving MNIST, UCF-101, Vimeo-90K) and image-to-video generation (Moving MNIST, UCF-101), e.g., reducing FVD from 688 to 611 for frame interpolation on UCF-101, and human raters prefer its frame interpolations for temporal consistency in 49$\%$ of comparisons versus 15$\%$ for the baseline ($p<10^{-17}$); for super-resolution, it performs on par with BM on automatic metrics.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## Reinforcement Learning with Visually Attributable On-Policy Self-Distillation
- **论文链接**: http://arxiv.org/abs/2610.26856v1
- **作者**: Shiao Xie, Siyu Chen, Jianwei Lv, Xiandong Li, Yujin Wang
- **原始摘要**: Multimodal reinforcement learning with verifiable rewards (RLVR) provides reliable task-level supervision, yet offers limited guidance for localizing errors in visual reasoning. On-policy self-distillation (OPSD) complements this supervision with dense token-level corrections from a privileged teacher equipped with an evidence-centered visual view. However, the resulting corrections may conflate visual evidence with non-visual shifts induced by linguistic priors, response style, or the privileged view itself. We formalize this phenomenon as privileged-correction contamination: a token-level correction is contaminated when its update direction cannot be consistently attributed to the privileged visual evidence. Directly distilling contaminated corrections may therefore reinforce erroneous token-level updates. To address this issue, we propose reinforcement learning with visually attributable on-policy self-distillation, an evidence-consistent paradigm that augments task-level RLVR supervision with privileged token-level corrections grounded in visual evidence. We instantiate this paradigm with Visual-Attribution Gating (VAG), which uses the verifier-derived advantage as the optimization anchor and validates each privileged correction against the contrast between evidence-present and evidence-degraded teacher views. By admitting only corrections directionally supported by this visual contrast, VAG preserves visually grounded guidance while suppressing inconsistent residuals. Experiments across six visual reasoning benchmarks show that VAG consistently outperforms GRPO and OPSD methods, establishing new state-of-the-art average performance.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
