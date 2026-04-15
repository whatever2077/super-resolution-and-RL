# 2026-04-16 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## LPNSR: Optimal Noise-Guided Diffusion Image Super-Resolution Via Learnable Noise Prediction
- **论文链接**: http://arxiv.org/abs/2603.21045v5
- **作者**: Shuwei Huang, Shizhuo Liu, Zijun Wei
- **原始摘要**: Diffusion-based image super-resolution (SR) aims to reconstruct high-resolution (HR) images from low-resolution (LR) observations. However, the inherent randomness injected during the reverse diffusion process causes the performance of diffusion-based SR models to vary significantly across different sampling runs, particularly when the sampling trajectory is compressed into a limited number of steps. A critical yet underexplored question is: what is the optimal noise to inject at each intermediate diffusion step? In this paper, we establish a theoretical framework that derives the closed-form analytical solution for optimal intermediate noise in diffusion models from a maximum likelihood estimation perspective, revealing a consistent conditional dependence structure that generalizes across diffusion paradigms. We instantiate this framework under the residual-shifting diffusion paradigm and accordingly design an LR-guided multi-input-aware noise predictor to replace random Gaussian noise. We further mitigate initialization bias with a high-quality pre-upsampling network. The compact 4-step trajectory uniquely enables end-to-end optimization of the entire reverse chain, which is computationally prohibitive for conventional long-trajectory diffusion models. Extensive experiments demonstrate that LPNSR achieves state-of-the-art perceptual performance on both synthetic and real-world datasets, without relying on any large-scale text-to-image priors. The source code of our method can be found at https://github.com/Faze-Hsw/LPNSR.

### GPT总结
#### 文章内容
该论文关注少步采样下扩散式超分辨率因中间随机噪声注入而导致性能不稳定与退化的问题。作者从最大似然估计（MLE）出发，推导出扩散模型“最优中间噪声”的闭式解及其跨范式一致的条件依赖结构，并在残差平移扩散（ResShift）框架中用LR引导的多输入噪声预测器替代高斯噪声，配合高质量预上采样初始化与4步紧凑反推。实验表明，无需依赖大规模T2I先验，所提LPNSR在合成与真实数据上取得SOTA级感知表现。

#### 方法
- 理论层面：建立统一的MLE框架，给出“最优中间噪声”的闭式解，揭示其在主流扩散范式中的一致条件依赖结构。
- 框架实例化：在ResShift范式中落地该解，设计LR-guided的multi-input-aware噪声预测器替代各反向步的随机高斯噪声，保持原轻量化推理机制不变。
- 预上采样初始化：以高质量预上采样网络替代双三次初始化，缓解少步反推难以纠正初值偏差的问题，并支持任意步数推理而无需重训去噪器。
- 端到端优化：利用4-step紧凑轨迹，可对完整反向链路进行端到端训练，学习近似最优噪声，同时不改动预训练去噪网络。
- 推理流程：先预上采样得到初态，再在4步ResShift反向过程中由噪声预测器逐步生成指导噪声完成重建。

#### 创新点
- 从MLE出发推导“最优中间噪声”闭式解，提出可跨扩散范式泛化的一致条件依赖结构，提供少步扩散稳健性的理论依据。
- 在ResShift中以LR-guided多输入噪声预测器替代随机噪声，不改变去噪器结构与高效机制，实现学习式噪声注入。
- 通过预上采样缓解初始化偏差，使4-step端到端可训练，并带来无需重设超参数/重训去噪器的任意步数推理能力。
- 摒弃外部大规模T2I先验，专注于SR任务内生的最优噪声建模以提升感知质量。

#### 实验结论
- 任务与数据集：在合成与真实场景的SR数据上评估，具体数据集名称与设置文中未明确说明。
- 结果与对比：LPNSR在感知质量上达到SOTA，尤其在4步少步采样下显著优于使用随机噪声的扩散式SR方法；具体数值提升文中未明确说明。
- 作者结论：学习式最优噪声与预上采样结合，可在不依赖大规模T2I先验的前提下，兼顾推理效率与高感知质量，并缓解少步扩散的性能退化。

## 关键词：reinforcement learning

## KG-Hopper: Empowering Compact Open LLMs with Knowledge Graph Reasoning via Reinforcement Learning
- **论文链接**: http://arxiv.org/abs/2603.21440v4
- **作者**: Shuai Wang, Yinan Yu
- **原始摘要**: Large Language Models (LLMs) demonstrate impressive natural language capabilities but often struggle with knowledge-intensive reasoning tasks. Knowledge Base Question Answering (KBQA), which leverages structured Knowledge Graphs (KGs) exemplifies this challenge due to the need for accurate multi-hop reasoning. Existing approaches typically perform sequential reasoning steps guided by predefined pipelines, restricting flexibility and causing error cascades due to isolated reasoning at each step. To address these limitations, we propose KG-Hopper, a novel Reinforcement Learning (RL) framework that empowers compact open LLMs with the ability to perform integrated multi-hop KG reasoning within a single inference round. Rather than reasoning step-by-step, we train a Reasoning LLM that embeds the entire KG traversal and decision process into a unified ``thinking'' stage, enabling global reasoning over cross-step dependencies and dynamic path exploration with backtracking. Experimental results on eight KG reasoning benchmarks show that KG-Hopper, based on a 7B-parameter LLM, consistently outperforms larger multi-step systems (up to 70B) and achieves competitive performance with proprietary models such as GPT-3.5-Turbo and GPT-4o-mini, while remaining compact, open, and data-efficient. The code is publicly available at: https://github.com/Wangshuaiia/KG-Hopper.

### GPT总结
#### 文章内容
该论文针对LLMs在知识密集型的知识图谱问答（KBQA）中易受多步管线约束、产生误差级联的问题，提出通过强化学习训练一个“Reasoning LLM”，在单次推理中完成整合式的多跳KG推理。核心思路是在统一的“thinking”阶段嵌入KG遍历与决策，利用工具化检索、全局依赖建模与可回溯探索替代逐步管线。实验显示，基于7B模型的KG-Hopper在八个KG推理基准上稳定优于更大的多步系统（最高至70B），并与GPT-3.5-Turbo与GPT-4o-mini表现相当，同时保持紧凑、开源与数据高效。

#### 方法
- 将整个KG多跳遍历与决策嵌入Reasoning LLM的单轮“thinking”阶段，在生成最终答案前进行全局推理以捕获跨步依赖。
- 通过强化学习训练模型有效使用KG检索工具，在离散图上优化推理策略以兼顾探索与长期回报（具体RL算法与奖励细节文中未明确说明）。
- 支持动态路径探索与回溯，弱化对预设管线的依赖，降低早期错误的级联影响。
- 单轮推理中统一产生检索意图与读取结果（如查询KG并汇总返回的三元组），再输出最终答案。

#### 创新点
- 将多跳KG推理从多次LLM调用的逐步管线，重构为单次调用内的统一“thinking”阶段，显式建模跨步全局依赖。
- 用RL引导LLM的工具化KG遍历与可回溯探索，替代固定步骤与束搜索的局部最优倾向。
- 在开源、紧凑的7B模型上实现与更大或专有模型相当的多跳推理能力，体现数据效率与工程简洁性。
- 将“Reasoning LLM”的可自我修正思维过程（后续token可修订先前推断）与结构化KG检索结合用于KBQA。

#### 实验结论
- 在八个KG推理基准上，KG-Hopper（7B）持续优于更大的多步系统（最高至70B）。
- 与GPT-3.5-Turbo与GPT-4o-mini具有竞争性表现，同时保持紧凑、开源与数据高效。
- 具体数据集名称、评价指标与量化数值文中未明确说明。
