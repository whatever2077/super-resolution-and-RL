# 2026-04-14 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Training-Free Model Ensemble for Single-Image Super-Resolution via Strong-Branch Compensation
- **论文链接**: http://arxiv.org/abs/2604.11564v1
- **作者**: Gengjia Chang, Xining Ge, Weijun Yuan, Zhan Li, Qiurong Song, Luen Zhu, Shuhong Liu
- **原始摘要**: Single-image super-resolution has progressed from deep convolutional baselines to stronger Transformer and state-space architectures, yet the corresponding performance gains typically come with higher training cost, longer engineering iteration, and heavier deployment burden. In many practical settings, multiple pretrained models with partially complementary behaviors are already available, and the binding constraint is no longer architectural capacity but how effectively their outputs can be combined without additional training. Rather than pursuing further architectural redesign, this paper proposes a training-free output-level ensemble framework. A dual-branch pipeline is constructed in which a Hybrid attention network with TLC inference provides stable main reconstruction, while a MambaIRv2 branch with geometric self-ensemble supplies strong compensation for high-frequency detail recovery. The two branches process the same low-resolution input independently and are fused in the image space via a lightweight weighted combination, without updating any model parameters or introducing an additional trainable module. As our solution to the NTIRE 2026 Image Super-Resolution ($\times 4$) Challenge, the proposed design consistently improves over the base branch and slightly exceeds the pure strong branch in PSNR at the best operating point under a unified DIV2K bicubic $\times 4$ evaluation protocol. Ablation studies confirm that output-level compensation provides a low-overhead and practically accessible upgrade path for existing super-resolution systems.



## 关键词：reinforcement learning

## Relax: An Asynchronous Reinforcement Learning Engine for Omni-Modal Post-Training at Scale
- **论文链接**: http://arxiv.org/abs/2604.11554v1
- **作者**: Liujie Zhang, Benzhe Ning, Rui Yang, Xiaoyan Yu, Jiaxing Li, Lumeng Wu, Jia Liu, Minghao Li, Weihang Chen, Weiqi Hu, Lei Zhang
- **原始摘要**: Reinforcement learning (RL) post-training has proven effective at unlocking reasoning, self-reflection, and tool-use capabilities in large language models. As models extend to omni-modal inputs and agentic multi-turn workflows, RL training systems face three interdependent challenges: heterogeneous data flows, operational robustness at scale, and the staleness -- throughput tradeoff. We present \textbf{Relax} (Reinforcement Engine Leveraging Agentic X-modality), an open-source RL training engine that addresses these challenges through three co-designed architectural layers. First, an \emph{omni-native architecture} builds multimodal support into the full stack -- from data preprocessing and modality-aware parallelism to inference generation -- rather than retrofitting it onto a text-centric pipeline. Second, each RL role runs as an independent, fault-isolated service that can be scaled, recovered, and upgraded without global coordination. Third, service-level decoupling enables asynchronous training via the TransferQueue data bus, where a single staleness parameter smoothly interpolates among on-policy, near-on-policy, and fully asynchronous execution. Relax achieves a 1.20$\times$ end-to-end speedup over veRL on Qwen3-4B on-policy training. Its fully async mode delivers a 1.76$\times$ speedup over colocate on Qwen3-4B and a 2.00$\times$ speedup on Qwen3-Omni-30B, while all modes converge to the same reward level. Relax supports R3 (Rollout Routing Replay)~\cite{ma2025r3} for MoE models with only 1.9\% overhead, compared to 32\% degradation in veRL under the same configuration. It further demonstrates stable omni-modal RL convergence on Qwen3-Omni across image, text, and audio, sustaining over 2{,}000 steps on video without degradation. Relax is available at https://github.com/rednote-ai/Relax.


