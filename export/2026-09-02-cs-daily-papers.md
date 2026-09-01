# 2026-09-02 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## PixelIR: Fidelity-Perception Decoupling via Pixel-Space Image-Residual Flow Matching for Efficient One-Step Real-World Super-Resolution
- **论文链接**: http://arxiv.org/abs/2608.30782v1
- **作者**: Bingtian Qiao, Yue Shi, Yong Guo, Wenjun Zhang, Jiezhang Cao
- **原始摘要**: Real-world image super-resolution (Real-ISR) aims to preserve structures supported by the degraded observation while reconstructing perceptually realistic details. However, existing Real-ISR methods largely optimize fidelity and perceptual quality within a shared network, causing the two objectives to interfere throughout training and making their balance difficult to control. Recent one-step methods reduce sampling steps, yet often inherit both this coupled optimization behavior and the expensive high-resolution backbone of their multi-step predecessors. We argue that efficient Real-ISR requires not only a shorter sampling trajectory, but also specialized modeling of faithful reconstruction and perceptual detail synthesis. Based on this insight, we propose PixelIR, a fidelity-perception decoupling framework built upon pixel-space image-residual flow matching. PixelIR first learns an image flow that maps the degraded observation to a faithful reconstruction. Then, a residual flow synthesizes the missing perceptual details from noise without repeatedly relearning or overwriting the complete restoration solution. We further distill the teacher into a deployment-oriented one-step student within a coarse-to-fine pyramid architecture. Extensive experiments show that PixelIR achieves leading PSNR, SSIM, and LPIPS on both RealSR and DRealSR. The final model completes pixel-space restoration in a single evaluation with only 32.9M parameters, 89.7G MACs, and 8.5ms latency, demonstrating a strong practical fidelity-perception-efficiency balance.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## PaperGym: Rubric-Centered Evolution for Research-Plan Generation
- **论文链接**: http://arxiv.org/abs/2608.31119v1
- **作者**: Yuhan Wang, Zhengxi Lu, Yuchen Yan, Kaitao Song, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen
- **原始摘要**: Research planning is the decisive capability of AI scientists. Yet a research plan admits no verifiable answer, so reinforcement learning lacks the environment it requires: tasks paired with a critic. Rubrics extracted from scientific papers can supply the critic. Existing pipelines, however, draw the question and the criteria from the same content, so the reward can be earned by paraphrase. The rubric is further compressed into a single scalar per rollout. We introduce PaperGym, a unified framework that turns each research paper into a complete training environment. PaperGym exploits the structure of a paper: the question is synthesized from the research goal and background, while the criteria are derived from the method and experiments. The criteria span methodological innovation and experimental design, and criterion leakage falls to 3.7%, versus 11.90% to 34.10% in existing datasets. Training uses the rubric twice: first as privileged context for OPSD's self-teacher, then as the reward for GRPO. Across Qwen3-1.7B/4B/8B, this schedule outperforms supervised fine-tuning, either stage alone, and the reverse ordering, improving five-benchmark averages by +5.6, +5.0, and +4.8 points. With the recipe held fixed, models trained on PaperGym-20k win 58.1% of three-way comparisons, against 28.2% for RubricHub Science. The trained Qwen3-8B reaches 73.48 on ResearchQA, above the far larger Kimi K2.6. We release the pipeline, the 20,000-instance corpus PaperGym-20k, and the benchmarks PaperGym-Innov and PaperGym-Design.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
