# 2026-09-16 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## LPNSR: Learnable Noise Prediction for Diffusion-Based Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2603.21045v6
- **作者**: Shuwei Huang, Shizhuo Liu, Zijun Wei
- **原始摘要**: Diffusion-based image super-resolution (SR) aims to reconstruct high-resolution (HR) images from low-resolution (LR) observations. A key property of diffusion models is that, once the starting point of the reverse chain and the denoising network are fixed, the quality of the generated image is dictated by the noise maps sampled at the intermediate steps, which are drawn from an unconstrained standard Gaussian distribution in conventional pipelines. This property raises a natural question: does there exist a noise sampling distribution better than the standard Gaussian that improves the quality of the generated images? To this end, we use a parameterized deep neural network to predict the mean and the variance of the Gaussian noise sampling distribution at each intermediate step, and design two training schemes, one supervised by the quality of the final generated image and the other by aligning each reverse step with the forward posterior. Experiments show that, compared with the standard Gaussian distribution, the learnable noise sampling distribution improves the quality of the generated images. The source code of our method can be found at https://github.com/Faze-Hsw/LPNSR.

### GPT总结

当前论文的 GPT 总结生成失败：`'str' object has no attribute 'get'`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## ResSafe: Learning Safety Filtering with Residual Reinforcement Learning for Humanoids
- **论文链接**: http://arxiv.org/abs/2609.15988v1
- **作者**: Gechen Qu, Tong Zhang, Bike Zhang, Yen-Jen Wang, Koushil Sreenath, Claire Tomlin, Jason Jangho Choi
- **原始摘要**: Safe control of humanoid robots remains challenging due to their high-dimensional dynamics, contact-rich interactions, and sensitivity to disturbances. Although reinforcement learning has enabled effective locomotion and motion tracking, learned policies can still generate unsafe actions that lead to instability or falls. In this work, we propose residual reinforcement learning as an implicit safety-filtering mechanism for safe humanoid control. Instead of relying on a single nominal policy to simultaneously balance performance, safety, and robustness, we decouple performance and safety. The nominal policy focuses solely on task performance, while a residual policy learns safety corrections. This decoupling leads to a better performance--safety Pareto trade-off and avoids the need for careful tuning of multiple competing reward terms within a single policy training. We show that the residual policy can act as an implicit safety filter.

### GPT总结

当前论文的 GPT 总结生成失败：`'str' object has no attribute 'get'`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
