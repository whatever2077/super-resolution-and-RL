# 2026-07-22 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Co-addition and Subtraction of Undersampled Images
- **论文链接**: http://arxiv.org/abs/2607.18054v1
- **作者**: Matan Schlanger, Barak Zackay
- **原始摘要**: In astronomical imaging surveys, repeated observations of the same sky patches are taken in order to obtain deeper images and detect new sources. This is the case in the search for many transient phenomena, such as supernovae, gravitational wave (GW) optical counterparts and other cataclysmic variables. In many such surveys some of the images are undersampled, meaning that the pixel size is too large, and the image suffers from aliasing. For undersampled images, both co-addition of the images and background subtraction are done in a non-optimal manner, which leads to reduced sensitivity and an increased rate of false alarms.   We present a new method (named Linear Undersampled Transients \& Addition (LUTRA)) that performs both processes in a mathematically proven optimal way, which allows improved performance for many scientific applications. It also allows easy and direct performance of measurements such as photometry and astrometry in a simple manner, while providing results in super-resolution. We demonstrate the performance of the method on public ZTF data and show $\times 1.25$ higher SNR compared to current methods. We provide an open source Python implementation.

### GPT总结
#### 文章内容
- 论文针对天文巡天中普遍存在的“欠采样”图像，提出在联合图像合成（co-addition）与背景/参考减法中当前方法非最优导致灵敏度下降和误警率升高的问题。
- 核心思路是提出线性方法 LUTRA（Linear Undersampled Transients & Addition），以“充分统计量”在信息论意义上保留整组欠采样观测对任何静态背景假设的全部似然信息，实现在超分辨率栅格上的最优合成与差分，同时便于直接进行光度和天体测量。
- 在公开 ZTF 数据上，方法相较“当前方法”获得约×1.25 的 SNR 提升，并提供开源 Python 实现。

#### 方法
- 将一组欠采样、PSF各异的观测转化为对静态背景假设的充分统计量，保证对任意后续假设检验/估计，基于该统计量与基于全量观测获得相同的似然。
- 采用线性、噪声加权的合成策略，联合执行最优 co-addition 与背景/参考减法，显式利用每幅图像的 PSF/PRF 与噪声水平，克服 Drizzle 等方法不利用 PSF、噪声处理不足的问题。
- 输出在高分辨率网格上的结果（super-resolution），并提供便于进行光度测量和天体测量的统计图像/滤波结果。
- 数值上避免病态矩阵求逆，具有良好的稳定性；支持增量式更新，整体计算复杂度近似与像素数线性，并可通过图像分块进一步提速。
- 无训练过程，纯基于线性推断与最优统计设计。

#### 创新点
- 首次将欠采样多帧合成与差分统一为构造充分统计量的线性框架，在数学上证明对静态背景假设的最优性与似然保持。
- 同时处理欠采样与跨帧 PSF 差异，直接产出超分辨率结果，并简化了光度/天体测量的下游流程。
- 相比 Drizzle、Lauer (1999) 与 ImCom 等方案，兼顾噪声加权、PSF 显式建模、数值稳定性与可增量更新，避免大规模求解的数值/存储瓶颈。
- 在真实巡天数据上展示实证收益，并提供开源实现，便于工程落地与复现。

#### 实验结论
- 任务与数据：在公开 ZTF 欠采样数据上评估图像合成与差分检测性能。
- 核心结果：相对当前常用流程，LUTRA 在 SNR 上实现约 ×1.25 的提升；其他指标与对比基线细节文中未明确说明。
- 作者结论：LUTRA 在理论上最优、数值稳定、可超分辨率地完成合成与差分，支持直接光度/天体测量，并具备开源实现。

## 关键词：reinforcement learning

## A Systematic Investigation of RL-Jailbreaking in LLMs
- **论文链接**: http://arxiv.org/abs/2605.07032v3
- **作者**: Montaser Mohammedalamen, Kevin Roice, Reginald McLean, Alyssa Lefaivre Škopac
- **原始摘要**: The evolution of generative models from next-token predictors to autonomous engines of complex systems necessitates rigorous safety hardening. Adversarial jailbreaking, the strategic manipulation of models to elicit harmful output, remains a primary threat to safe deployment. While Reinforcement Learning (RL) frames jailbreaking as a multi-step attack through sequential optimization, a mechanistic understanding of why the framework succeeds remains incomplete. To fill this gap, we present the first systematic decomposition of RL jailbreaking. We deconstruct the framework into problem formalization (reward function, action space, episode length), and algorithmic measures (RL algorithm, training data, reward-shaping) to identify the structural determinants of adversarial success. Our results reveal that the RL-jailbreaker successfully compromised all targeted models and safeguards. Through this first-of-its-kind analysis, we demonstrate that environment formalization, specifically dense rewards and extended episode lengths, is the primary driver of jailbreaking success. This work provides a tool for improving RL-jailbreaker efficiency and, ultimately, harden generative models resistant to RL-based attacks.

### GPT总结
#### 文章内容
本文系统性分解RL-jailbreaking框架，聚焦其为何在多步交互与序列优化下能有效攻破LLM及其防护。核心思路是将问题划分为环境形式化（奖励函数、动作空间、episode长度）与算法设计（RL算法、训练数据、reward shaping）两大维度，并通过控制变量的实证对比量化其贡献。主要结论指出：环境形式化，尤其是dense rewards与更长的episode，是攻破成功的主导因素；实验证实RL-jailbreaker可攻破被测的开源LLM与防护系统。

#### 方法
- 将攻击建模为RL问题：将目标LLM/安全防护视作环境，奖励与攻击成功度挂钩，进行多轮交互式优化。
- 分解两类因素并逐一对比：环境形式化（reward function、action space、episode length）与算法设计（value-based vs. actor-critic、training data规模、reward shaping）。
- 采用控制变量的系统实验，量化各组件对攻破率/效率的边际贡献，重点检验dense rewards与延长episode的作用。
- 在多种开源LLM（如Llama, Qwen, Tiny-aya）与防护（如Llama-guard, Shieldgemma）上统一评测以考察泛化；具体数据集与评价指标文中未明确说明。

#### 创新点
- 首次对RL-jailbreaking进行系统性机制分解，从“生成模型中心”转向“RL中心”的研究范式。
- 明确区分并量化环境形式化与算法设计两大支柱，对其各自的贡献进行结构化评估。
- 揭示dense rewards与较长episode长度是成功攻破的主要驱动因素，为后续攻防设计提供可操作的环境建模准则。
- 提供提升RL-jailbreaker效率与加固模型抗RL攻击的实证依据与方法学工具。

#### 实验结论
- 任务与设置：在多种开源LLM（Llama, Qwen, Tiny-aya）及防护系统（Llama-guard, Shieldgemma）上评估RL驱动的jailbreaking；具体数据集与指标文中未明确说明。
- 核心结果：RL-jailbreaker攻破了所有被测模型与防护；相比算法选择，环境形式化（特别是dense rewards与更长episode）对成功率影响更大。
- 作者结论：环境设计是提升RL-jailbreaking效率与成效的关键杠杆，该结论为构建更抗RL攻击的安全机制提供方向。
