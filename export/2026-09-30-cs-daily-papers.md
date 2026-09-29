# 2026-09-30 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Spectral Super-Resolution using Spatial-Spectral Residual Operator Networks
- **论文链接**: http://arxiv.org/abs/2609.35410v1
- **作者**: Seokhyun Chin
- **原始摘要**: Spectral super-resolution of multispectral satellite images can enable high temporal- and spatial-resolution hyperspectral satellite imagery at a modest cost, significantly increasing the applicability of hyperspectral remote sensing. This task is inherently ill-posed, making it well-suited for deep learning-based methods. In this study, the spectral super-resolution task is framed as an operator learning problem, and SSRON is proposed as a Deep Operator Network that effectively learns function-to-function mappings from downsampled spectra to continuous spectra. The model is trained to super-resolve Sentinel-2A-like multispectral imagery to EMIT images. Compared to baseline models, SSRON achieves superior performance across all metrics. The model also demonstrates zero-shot spectral super-resolution capability by predicting bands unseen during training. Furthermore, its continuous-output formulation suggests the potential to estimate spectra at finer wavelength intervals than the native sensor. These results suggest the potential of SSRON and establishes operator learning as a promising direction for spectral super-resolution.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## Learning Native Reflection in Unified Models with Interleaved Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2609.35767v1
- **作者**: Yijia Fan, Ziqi Huang, Zhongang Cai, Yan Li, Zimo Wen, Wanqi Yin, Haiwen Diao, Ziwei Liu
- **原始摘要**: Unified multimodal models can both look at and render images, so in principle they can repair their own generations: diagnose what an image gets wrong, revise it, observe the result, and diagnose again. Whether a revision helps is known only after it is rendered, so the reflection text and the image generation must be learned jointly, over the whole loop. Supervised fine-tuning (SFT) on reflection trajectories gives a cold start but does not find the high-success repair paths, and naive RL that optimizes only the renderer or only one head leaves most of the gain untapped. We introduce UMM-Reflection, which applies reinforcement learning (RL) to complete reflection trajectories inside one unified model: sibling trajectories share one initial image, so the group-relative advantage compares reflection strategies, and one trajectory-level advantage updates both the reflection tokens and the flow-based revisions, avoiding the combinatorial blow-up of per-round credit assignment. Unlike single-round editing or pipelines with an external critic, credit flows across rounds and to both roles of the same model, and no verifier is needed at inference. On BAGEL, UMM-Reflection improves GenEval by 12.05 points over SFT, and the gains transfer to WISE (+10.97), OneIG-Bench (+3.48), and T2I-CompBench++ (+4.63), none of which is used in training.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
