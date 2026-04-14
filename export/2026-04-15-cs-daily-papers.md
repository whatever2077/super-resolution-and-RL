# 2026-04-15 计算机领域论文日报

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
论文关注在已有多种预训练 SR 模型可用的现实场景下，如何在不进行再训练的前提下有效融合其互补优势。核心思路是构建一个训练免（training-free）的输出级别双分支集成：以 Hybrid attention network + TLC inference 为主干稳定重建，辅以 MambaIRv2 + 几何自集成用于高频细节补偿，并在图像空间做轻量加权融合。结论显示，该方案在统一的 DIV2K bicubic ×4 评测下，相比基础分支显著提升，并在最佳权重点上略微超过单独强分支的 PSNR，同时无需引入任何可训练模块。

#### 方法
- 构建非对称双分支管线：主分支采用 Hybrid attention network（HAT 类）结合 TLC inference，侧重稳定重建；强分支采用 MambaIRv2 并进行 geometric self-ensemble，强化高频细节。
- 两个分支基于同一低分辨率输入独立推理，输出在图像空间进行轻量的加权融合（weighted combination）。
- 完全训练免：不更新任何模型参数，不引入可学习的融合模块。
- 推理阶段对强分支施加几何自集成以提升细节恢复的稳健性与上限。
- 融合权重作为超参数，在[0,1]范围内扫描以确定在当前评估协议下的最佳 PSNR 操作点。

#### 创新点
- 提出训练免的输出级别补偿框架，用强分支对主分支进行细节“补偿”，避免再训练的成本与工程负担。
- 非对称双分支设计与轻量图像空间加权融合，显式利用不同模型的归纳偏差实现互补。
- 将 TLC inference 与 geometric self-ensemble 的推理策略性结合，强调“更强推理过程”而非“更大骨干网络”的增益路径。
- 面向部署的低开销升级路径：无需额外可训练模块即可改善现有 SR 系统的性能。

#### 实验结论
- 任务与数据：在 NTIRE 2026 Image Super-Resolution（×4）挑战设置下，采用 DIV2K bicubic ×4 统一评估，使用编号 0801–1000 的 200 张图像，指标为 PSNR/SSIM。
- 结果：补偿后的融合结果在最佳权重点上清晰优于基础分支，并在 PSNR 上略微超过单独的强分支；具体 PSNR/SSIM 数值文中未明确说明。
- 消融：随强分支权重从 0 到 1 连续变化的分析验证了输出级别补偿的有效性与稳健性；更多定量细节文中未明确说明。

## 关键词：reinforcement learning

## Solving Physics Olympiad via Reinforcement Learning on Physics Simulators
- **论文链接**: http://arxiv.org/abs/2604.11805v1
- **作者**: Mihir Prabhudesai, Aryan Satpathy, Yangmin Li, Zheyang Qin, Nikash Bhardwaj, Amir Zadeh, Chuan Li, Katerina Fragkiadaki, Deepak Pathak
- **原始摘要**: We have witnessed remarkable advances in LLM reasoning capabilities with the advent of DeepSeek-R1. However, much of this progress has been fueled by the abundance of internet question-answer (QA) pairs, a major bottleneck going forward, since such data is limited in scale and concentrated mainly in domains like mathematics. In contrast, other sciences such as physics lack large-scale QA datasets to effectively train reasoning-capable models. In this work, we show that physics simulators can serve as a powerful alternative source of supervision for training LLMs for physical reasoning. We generate random scenes in physics engines, create synthetic question-answer pairs from simulated interactions, and train LLMs using reinforcement learning on this synthetic data. Our models exhibit zero-shot sim-to-real transfer to real-world physics benchmarks: for example, training solely on synthetic simulated data improves performance on IPhO (International Physics Olympiad) problems by 5-10 percentage points across model sizes. These results demonstrate that physics simulators can act as scalable data generators, enabling LLMs to acquire deep physical reasoning skills beyond the limitations of internet-scale QA data. Code available at: https://sim2reason.github.io/.

### GPT总结
#### 文章内容
本文针对LLM推理依赖互联网QA数据、在物理领域数据稀缺的瓶颈，提出用物理模拟器作为可扩展监督源，生成大规模物理推理QA并用RLVR进行后训练。核心思路是以DSL程序化构造多样物理场景，仿真得到传感轨迹，自动合成数值/逆向/符号三类问题与可验证答案，并经质量过滤后用于强化学习。主要结论是仅用合成仿真数据训练即可在真实物理基准上实现零样本sim-to-real提升：IPhO力学提升5–10个百分点（3B–32B），JEEBench在32B上+17.9%，并在PHYSICS与OlympiadBench上取得一致增益，验证物理模拟器可作为可扩展的数据生成器。

#### 方法
- 设计Domain Specific Language (DSL)结构化随机化，程序化组合多种经典力学系统（如滑轮、转动等），生成多样物理场景与初始条件。
- 将DSL场景编译至MuJoCo进行仿真，记录状态/力等高保真传感轨迹，形成监督信号。
- 从轨迹自动构造三类QA：numeric（状态查询）、reverse（参数反推）、symbolic（闭式表达式），并检索精确答案。
- 质量控制与过滤：剔除退化、过于简单或数值不稳定/不可解样本，聚焦模型可求解难度区间。
- 用RLVR在纯合成数据上进行后训练，不引入真实物理QA；具体奖励形式与优化细节文中未明确说明。

#### 创新点
- 将物理模拟器转化为可扩展、无需人工标注的QA生成器，并以可验证奖励进行RL后训练，替代对互联网QA的依赖。
- 基于DSL的可组合场景生成，跨异质物理系统程序化合成，规模化产生百万级、物理一致性的训练样本。
- 同时覆盖numeric/reverse/symbolic三种推理模式，配合针对性样本过滤，提升训练有效性与稳健性。
- 相较“LLM调用外部模拟器工具”的方案，避免复杂API代码生成与人类工程介入，且展示超出模拟器原生现象范围的泛化能力（文中提及Section 3.6，细节未展开）。

#### 实验结论
- 任务与数据集：在IPhO、JEEBench、PHYSICS、OlympiadBench等真实基准上零样本评估，训练阶段未使用任何真实物理QA。
- 核心结果：IPhO力学零样本提升5–10个百分点（3B–32B）；JEEBench在32B上+17.9%；图示显示Qwen2.5 3B/+7.5、Qwen2.5 32B/+5.4、Qwen3 30B/+4.4。
- 作者结论：质量过滤至关重要；模型并非记忆合成样本而是获得可迁移的物理推理能力；代码与资源公开于https://sim2reason.github.io/。
