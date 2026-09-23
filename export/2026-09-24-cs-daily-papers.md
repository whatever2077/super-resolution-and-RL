# 2026-09-24 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## ASTRA-SR: Atmospheric Seeing and Turbulence Restoration for Astronomical Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2609.26731v1
- **作者**: Xining Ge, Ziteng Cui, Shuhong Liu
- **原始摘要**: Ground-based planetary imaging suffers from atmospheric turbulence, sensor noise, and limited sampling, making restoration a joint denoising, deblurring, and super-resolution problem. We present ASTRA-SR, a blind single-frame restoration framework trained on a physics-grounded synthetic dataset. High-dynamic-range spacecraft RAW observations serve as clean sources, and paired LR inputs are synthesized using measured layer-integrated turbulence strengths, propagated moving phase screens, exposure-averaged spatially varying PSFs, and sensor noise.ASTRA-SR first estimates a noise-suppressed but blur-retaining LR image, then restores spatial structure through multiscale processing and reconstructs HR detail with serial spatial-amplitude refinement. It yields a 0.49 dB foreground PSNR gain over the strongest baseline approaches.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## Optimal Sequential Annotations for Off-Policy Evaluation
- **论文链接**: http://arxiv.org/abs/2609.26707v1
- **作者**: Woojin Chae, Ezinne Nwankwo, Haitong Qin, Angela Zhou
- **原始摘要**: Offline reinforcement learning and off-policy evaluation evaluates dynamic treatment rules based on retrospectively collected data prior to deployment. In recent AI applications, state and reward information is recorded as complex text or image, which recent AI advancements such as LLM-as-a-judge can label with unknown bias. Expert annotation may be available but at a higher cost. For example, safety classification via cheap but imperfect classifiers vs. expensive expert review. We show how a limited budget for ground-truth data-annotation can be used via doubly-robust OPE with missing rewards, and we optimize variance-optimal annotation probabilities for sequential off-policy evaluation, where the target policy value is estimated from annotated data. We characterize the optimal annotation probabilities for sequential forward-monotone annotation protocols, and provide a feasible batch-adaptive implementation. Our work is motivated by a collaboration with a homelessness services nonprofit that writes casenotes for individuals over time. Our method can be used to unlock trustworthy inference from casenote data and answer new inferential questions such as: how does expanding outreach effort over time affect progress towards a housing application and improvement in housing placement? In simulations and on two real datasets - casenotes from the nonprofit and human-preference votes from LMArena - we see reductions in RMSE of 34-65% for housing placement and 17-68% for progress towards a housing application at budgets of 40% of full annotation and above, and by 55-62% at every budget on LMArena.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
