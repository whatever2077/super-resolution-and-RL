# 2026-10-28 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## HiFiPix: Bringing High-Fidelity Real-World Super-Resolution Back to Pixel Space
- **论文链接**: http://arxiv.org/abs/2610.35515v1
- **作者**: Wenjie Li, Du Chen, Hui Wang, Linlong Fan, Youwei Lv, Zeyi Chen, Zehan Chen, Jinwei Chen, Heng Guo, Zhanyu Ma, Qingnan Fan
- **原始摘要**: Diffusion-based real-world image super-resolution suffers from limited reconstruction fidelity due to information loss in VAE-based latent representations. Recently, pixel-space diffusion models offer a promising high-faithfulness alternative by avoiding latent compression, but adapting them to Real-ISR remains challenging due to inherent patch boundary artifacts and degraded generative capability. To address the issues and maximize the potential of pretrained pixel-space diffusion models, we propose HiFiPix, a pixel-space Real-ISR framework capable of ultra high-fidelity reconstruction and fine-grained visual generation effects. To suppress patch boundary artifacts, we penalize unrealistic high-frequency periodic components with a Cross-Scale Wavelet Discriminator (CWSD) for image-level supervision, and Mixup Contrastive Self-Distillation (MixCSD) for intermediate representation regularization. Furthermore, we uncover a heterogeneous generation-fidelity trade-off across low-rank adapters (LoRA) and propose Selective LoRA Pruning (LoRA-SP) to adaptively prune LoRA layers, enhancing generative capability with minimal deterioration of reconstruction fidelity. Extensive experiments demonstrate that HiFiPix consistently outperforms existing state-of-the-art latent space methods in terms of both restoration accuracy and perceptual quality by a large margin. Code and models will be released.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## World Model for Energy Efficiency Maximization in Dynamic Metasurface Antennas
- **论文链接**: http://arxiv.org/abs/2610.35813v1
- **作者**: Abdolrasoul Sakhaei Gharagezlou, Mehdi Monemi, Matti Latva-aho, Mehdi Rasti
- **原始摘要**: Dynamic metasurface antennas (DMAs) have emerged as a promising technology for realizing large-scale antenna arrays in next-generation wireless networks owing to their ability to enable dense and energy-efficient antenna architectures. However, jointly optimizing digital beamforming and DMA element weights under time-varying channel conditions remains challenging due to their coupled effects on the received signal and interference powers. We formulate this problem to maximize time-averaged energy efficiency (EE) under time-varying channel conditions, subject to transmit power constraints, Lorentzian phase limitations, and minimum rate requirements. To enable long-term planning and improve sample efficiency compared with model-free reinforcement learning, we develop a world model framework that learns latent system dynamics from interactions with the environment and jointly optimizes digital beamforming and DMA element weights through imagined trajectories. Furthermore, we incorporate feasibility-preserving action mappings and safety cost signals to ensure constraint satisfaction during policy learning. Simulation results demonstrate that the proposed framework improves the time-averaged EE by approximately 20% compared with the deep Q-network baseline, while achieving higher sample efficiency and more reliable constraint satisfaction.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
