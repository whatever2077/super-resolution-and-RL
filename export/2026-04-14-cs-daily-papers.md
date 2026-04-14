# 2026-04-14 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Training-Free Model Ensemble for Single-Image Super-Resolution via Strong-Branch Compensation
- **论文链接**: http://arxiv.org/abs/2604.11564v1
- **作者**: Gengjia Chang, Xining Ge, Weijun Yuan, Zhan Li, Qiurong Song, Luen Zhu, Shuhong Liu
- **原始摘要**: Single-image super-resolution has progressed from deep convolutional baselines to stronger Transformer and state-space architectures, yet the corresponding performance gains typically come with higher training cost, longer engineering iteration, and heavier deployment burden. In many practical settings, multiple pretrained models with partially complementary behaviors are already available, and the binding constraint is no longer architectural capacity but how effectively their outputs can be combined without additional training. Rather than pursuing further architectural redesign, this paper proposes a training-free output-level ensemble framework. A dual-branch pipeline is constructed in which a Hybrid attention network with TLC inference provides stable main reconstruction, while a MambaIRv2 branch with geometric self-ensemble supplies strong compensation for high-frequency detail recovery. The two branches process the same low-resolution input independently and are fused in the image space via a lightweight weighted combination, without updating any model parameters or introducing an additional trainable module. As our solution to the NTIRE 2026 Image Super-Resolution ($\times 4$) Challenge, the proposed design consistently improves over the base branch and slightly exceeds the pure strong branch in PSNR at the best operating point under a unified DIV2K bicubic $\times 4$ evaluation protocol. Ablation studies confirm that output-level compensation provides a low-overhead and practically accessible upgrade path for existing super-resolution systems.

### GPT总结
#### 文章内容
该论文面向单幅图像超分辨率（SISR）提出一种无需训练的输出级集成方案，旨在在已有多模型可用的现实条件下，通过有效融合其互补优势提升重建质量。核心思路是构建不对称的双分支：以Hybrid attention network + TLC推理为稳定主分支，辅以带有geometric self-ensemble的MambaIRv2强分支进行高频细节补偿，并在图像空间以轻量加权方式融合输出。主要结论是该方法在DIV2K bicubic ×4统一协议下，相比基线分支稳定提升，并在最佳权重点上PSNR略高于单纯强分支，同时无需更新任何参数或新增可训练模块。

#### 方法
- 双分支管线：主分支采用Hybrid attention network并配合TLC推理；补偿分支采用MambaIRv2并进行geometric self-ensemble以强化高频细节恢复。
- 两个分支对同一低分辨率输入独立推理，保持完全训练自由（无再训练、无微调）。
- 在图像空间对两路重建结果进行轻量化的加权融合，无引入可训练的融合模块。
- 通过调节强分支权重（0→1连续变化）分析性能曲线，并选取在当前评估协议下PSNR最优的补偿比例作为主结果。
- 采用统一的推理与评估设置，确保比较的可复现与一致性。

#### 创新点
- 提出训练自由（training-free）的输出级补偿式集成框架，绕开重新训练强模型的高成本，直接利用现成模型的互补性。
- 不对称设计：以稳定主干（Hybrid + TLC）提供鲁棒重建，强分支（MambaIRv2 + geometric self-ensemble）专注高频补偿，降低部署与工程负担。
- 纯后处理级的加权融合策略，无需新增可训练模块，实现对现有SR系统的低开销可达升级路径。
- 在统一协议下系统性地扫描强分支权重，给出操作点选择的实证依据，并配合消融验证输出级补偿有效性。

#### 实验结论
- 任务与数据集：在单幅超分辨率 ×4 任务上，使用DIV2K bicubic ×4 评估（图像0801–1000，共200张），指标为PSNR与SSIM。
- 主要结果：所提补偿结果相较主分支显著提升，并在最佳操作点PSNR上略优于纯强分支；具体数值提升幅度文中未明确说明。
- 作者结论：输出级强分支补偿是一条实用、部署友好的升级路径，无需参数更新或新增可训练模块，消融研究进一步支持这一结论（具体消融设置与数值文中未明确说明）。

## 关键词：reinforcement learning

## Solving Physics Olympiad via Reinforcement Learning on Physics Simulators
- **论文链接**: http://arxiv.org/abs/2604.11805v1
- **作者**: Mihir Prabhudesai, Aryan Satpathy, Yangmin Li, Zheyang Qin, Nikash Bhardwaj, Amir Zadeh, Chuan Li, Katerina Fragkiadaki, Deepak Pathak
- **原始摘要**: We have witnessed remarkable advances in LLM reasoning capabilities with the advent of DeepSeek-R1. However, much of this progress has been fueled by the abundance of internet question-answer (QA) pairs, a major bottleneck going forward, since such data is limited in scale and concentrated mainly in domains like mathematics. In contrast, other sciences such as physics lack large-scale QA datasets to effectively train reasoning-capable models. In this work, we show that physics simulators can serve as a powerful alternative source of supervision for training LLMs for physical reasoning. We generate random scenes in physics engines, create synthetic question-answer pairs from simulated interactions, and train LLMs using reinforcement learning on this synthetic data. Our models exhibit zero-shot sim-to-real transfer to real-world physics benchmarks: for example, training solely on synthetic simulated data improves performance on IPhO (International Physics Olympiad) problems by 5-10 percentage points across model sizes. These results demonstrate that physics simulators can act as scalable data generators, enabling LLMs to acquire deep physical reasoning skills beyond the limitations of internet-scale QA data. Code available at: https://sim2reason.github.io/.

### GPT总结
#### 文章内容
论文针对RLVR训练LLM受限于高质量互联网QA数据稀缺（尤以物理为甚）的问题，提出用物理模拟器作为可扩展监督源。核心思路是通过DSL程序化生成多样物理场景，用MuJoCo模拟获得可验证轨迹，自动构造多类型问答，并以RLVR在纯合成数据上后训练LLM。主要结论是模型在不使用真实物理QA对的情况下实现零样本sim-to-real迁移：IPhO力学题准确率提升5–10个百分点（3B–32B），并在JEEBench（32B：+17.9%）与PHYSICS等基准上取得一致增益，且数据质量过滤至关重要。

#### 方法
- 使用Domain Specific Language (DSL)程序化组合经典力学异质场景，编译为MuJoCo仿真并记录状态/力等物理轨迹。
- 从轨迹自动生成场景描述与三类QA：numeric（状态查询）、reverse（参数反推）、symbolic（闭式表达式），答案由仿真传感数据直接检索。
- 进行质量过滤，剔除退化题（过易/不可算）与不稳定仿真片段，聚焦LLM可解样本。
- 采用RLVR在纯合成数据上对LLM进行后训练，奖励基于QA可验证正确性；训练阶段不引入真实物理QA对。
- 以零样本设置评估在IPhO、JEEBench、PHYSICS、OlympiadBench等真实基准上的迁移效果。

#### 创新点
- 将物理模拟器转化为可规模化的QA生成器，摆脱互联网QA与人工标注的瓶颈。
- 通过DSL把连续仿真轨迹映射为多样化文本问题（含逆向与符号推导），连接前向数值演化与逆向/解析推理。
- 使用RLVR在仅含模拟器生成数据上进行后训练，无需工具调用或代码生成，即可获得物理推理能力与sim-to-real迁移。
- 系统化的题目与仿真质量控制策略，证明过滤对提升训练有效性和最终性能关键。

#### 实验结论
- 在International Physics Olympiad (IPhO)力学题上，3B–32B模型零样本准确率提升5–10个百分点。
- 在JEEBench与PHYSICS等基准上获得一致增益，其中32B模型在JEEBench提升+17.9%；对OlympiadBench也有改进。
- 仅用Sim2Reason合成数据训练即可实现稳健sim-to-real迁移；质量过滤对最终效果影响显著。
