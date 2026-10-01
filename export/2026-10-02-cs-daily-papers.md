# 2026-10-02 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## FANVIDv2: Evaluating Video Super-Resolution by Face and Licence-Plate Recognition Under Compound Degradation
- **论文链接**: http://arxiv.org/abs/2609.39649v1
- **作者**: Kavitha Viswanathan, Vrinda Goel, Shlesh Gholap, Devayan Ghosh, Madhav Gupta, Dhruvi Ganatra, Sanket Potdar, Amit Sethi
- **原始摘要**: Video super-resolution (VSR) is normally judged by PSNR and SSIM on clips that were downsampled bicubically, although in surveillance its purpose is to make faces and licence plates \emph{recognisable}. We present FANVIDv2, a benchmark that scores VSR by what a recognition pipeline can do with its output. FANVIDv2 provides $320\times180$ low-resolution (LR) clips with high-resolution (HR) references for 48 public figures (with one HR gallery image each) and 375 licence-plate clips covering 360 distinct plate strings. LR clips are generated with a randomised compound degradation (blur, resize jitter, sensor noise, JPEG compression, final downsampling) rather than bicubic downsampling alone. Two metrics score recognition \emph{inside} detections: FaceRecBox rewards a face only if it is localised and correctly identified, and TextRecBox scores plate transcriptions by normalised edit distance weighted by localisation quality. With a 2.3\,M-parameter VSR baseline (RCDM), FaceRecBox rises from 0.6864 to 0.7222, identity accuracy on matched faces from 84.35\% to 86.93\%, and TextRecBox from 0.3088 to 0.3667; a residual-map gated variant (RCDM-RMGF) reaches 0.3801 on plates. We describe the degradation model, the baseline architectures and the scorers in detail, and release annotations, metadata, download and degradation scripts and evaluation code.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## Semifactual Credit-Augmented Policy Optimization
- **论文链接**: http://arxiv.org/abs/2609.40360v1
- **作者**: Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang
- **原始摘要**: Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that suppressing high-drift token candidates during decoding improves reasoning accuracy without updating model weights. These findings highlight a limitation of Group Relative Policy Optimization (GRPO), which assigns the same outcome-derived advantage to every response token and may reinforce potential spurious dependence alongside useful reasoning. Motivated by this observation, we introduce Semifactual Credit-Augmented Policy Optimization (SCAPO), a causally inspired variant of GRPO that incorporates semifactual stability into token-level credit assignment. SCAPO measures token probability drift for fixed responses under semifactual interventions and uses normalized stability scores to reduce advantages for relatively unstable tokens during early training, while granting no additional credit for stability alone. On Qwen3-4B-Base and Qwen3-1.7B-Base, SCAPO improves AIME 2024-2026 accuracy over GRPO by 5.63 and 4.17 percentage points, respectively. At both model scales, SCAPO achieves the best results on most evaluated mathematics benchmarks and all evaluated out-of-distribution benchmarks among the compared methods. These results suggest that semifactual stability provides an effective training signal for improving reasoning and generalization through finer-grained credit assignment in RLVR. The code is available at https://github.com/DtYXs/SCAPO.

### GPT总结

当前论文的 GPT 总结生成失败：`Encountered text corresponding to disallowed special token '<|endoftext|>'. If you want this text to be encoded as a special token, pass it to `allowed_special`, e.g. `allowed_special={'<|endoftext|>', ...}`. If you want this text to be encoded as normal text, disable the check for this token by pas...`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
