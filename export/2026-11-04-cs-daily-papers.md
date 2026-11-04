# 2026-11-04 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## TaoMate-FVSR:Audio-Guided Facial Video Restoration
- **论文链接**: http://arxiv.org/abs/2611.03393v1
- **作者**: Xinyang Li, Zeran Xu, Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma
- **原始摘要**: AI-generated videos often depict people within detailed scenes while leaving their small facial regions poorly resolved. Visual super-resolution can sharpen these regions without resolving whether the recovered lips and teeth agree with the spoken audio. We present an audio-guided facial video restoration framework that addresses this ambiguity within a reference-guided video flow model. Source--noise mixing initializes reconstruction from a partially preserved observation, and structured reference injection separates appearance anchors from continuous motion context. Training combines restoration of degraded images and videos with correction of degraded dubbed sources under target audio. Appearance and synchronization supervision allow the model to recover facial detail and support visual dubbing when the audio is replaced. On talking-head restoration benchmarks, our method achieves the best paired perceptual similarity and synchronization scores among the compared restoration methods. Component comparisons examine audio conditioning, the reconstruction formulation, and reference injection. Native AIGC examples further illustrate the recovery of lip contours, dental structure, and surrounding facial texture in scene-level footage. injection. Native AIGC examples further illustrate the recovery of lip contours, dental structure, and surrounding facial texture in scene-level footage.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## EgoActionBench: Benchmarking Dense Action Captioning for Egocentric Human Videos
- **论文链接**: http://arxiv.org/abs/2611.03646v1
- **作者**: Yujiao Shen, Jiahe Song, Haitian Li, Jingkang Yang, Ziwei Liu
- **原始摘要**: Learning from human data offers a scalable path toward embodied intelligence, yet it requires models to accurately understand fine-grained human actions from egocentric observations. However, existing benchmarks remain limited in action atomicity, temporal precision, and hand-action association. We introduce EgoActionBench, a benchmark that represents continuous human manipulation as temporally localized atomic actions associated with the left hand, right hand, or both hands. EgoActionBench contains 1,407 episodes with 41,132 human-refined action annotations. To evaluate such dense predictions, we propose an evaluation protocol that retrieves temporally eligible candidates, selects a prediction by content agreement, and scores semantic fidelity and temporal overlap alongside action precision and recall, jointly capturing what happens, when it happens, and which hand performs it. We benchmark 20 baseline models and systems on EgoActionBench and further adapt two backbones, Qwen3-VL-4B and LLaVA-OneVision-2-8B, through supervised fine-tuning followed by reinforcement learning on automatically annotated training episodes. EgoAction improves EgoActionScore by 15.9 and 23.2 points on the two backbones, and both adapted models outperform all open-source baselines. Our experiments reveal substantial limitations of current models in action atomicity, temporal precision, and hand-action association, highlighting the gap between general video understanding and the action understanding required for embodied intelligence.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
