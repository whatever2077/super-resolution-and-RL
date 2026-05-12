# 2026-05-13 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Power Reinforcement Post-Training of Text-to-Image Models with Super-Linear Advantage Shaping
- **论文链接**: http://arxiv.org/abs/2605.10937v1
- **作者**: Haoyuan Sun, Jing Wang, Yuxin Song, Yu Lu, Bo Fang, Yifu Luo, Jun Yin, Pengyu Zeng, Miao Zhang, Tiantian Zhang, Xueqian Wang, Shijian Lu
- **原始摘要**: Recently, post-training methods based on reinforcement learning, with a particular focus on Group Relative Policy Optimization (GRPO), have emerged as the robust paradigm for further advancement of text-to-image (T2I) models. However, these methods are often prone to reward hacking, wherein models exploit biases in imperfect reward functions rather than yielding genuine performance gains. In this work, we identify that normalization could lead to miscalibration and directly removing the prompt-level standard deviation term yields an optimal policy ascent direction that is linear in the advantage but still limits the separation of genuine signals from noise. To mitigate the above issues, we propose Super-Linear Advantage Shaping (SLAS) by revisiting the functional update from an information geometry perspective. By extending the Fisher-Rao information metric with advantage-dependent weighting, SLAS introduces a non-linear geometric structure that reshapes the local policy space. This design relaxes constraints along high-advantage directions to amplify informative updates, while tightening those in low-advantage regions to suppress illusory gradients. In addition, batch-level normalization is applied to stabilize training under varying reward scales. Extensive evaluations demonstrate that SLAS consistently surpasses the DanceGRPO baseline across multiple backbones and benchmarks. In particular, it yields faster training dynamics, improved out-of-domain performance on GenEval and UniGenBench++, and enhanced robustness to model scaling, while mitigating reward hacking and preserving semantic and compositional fidelity in generations.

### GPT总结
#### 文章内容
该文关注基于GRPO的文本生成图像（T2I）模型强化后训练易出现的reward hacking问题，指出组内归一化导致的优势估计失准会把噪声当作有效信号。作者提出Super-Linear Advantage Shaping (SLAS)：从信息几何出发扩展Fisher–Rao度量为优势依赖的非线性几何，结合去除prompt级标准差与批级归一化，放大高优势、抑制低优势更新。实验证明SLAS在多种骨干与基准上优于DanceGRPO，训练更快、在GenEval与UniGenBench++上更稳健，并缓解reward hacking且保持语义与组合一致性。

#### 方法
- 诊断问题：GRPO的组相对归一化在奖励差距很小的情形下产生“错配”，使不同方差组得到相同相对优势，诱发虚假梯度与reward hacking。
- 线性基线：去除prompt级标准差后，通过局部泛函优化与泰勒展开（Theorem 2）推导出最优更新方向对优势呈线性，但仍难有效区分信号与噪声。
- 信息几何重构：在概率单纯形切空间上构造γ加权变分度量，扩展Fisher–Rao为优势依赖的几何结构，重塑局部策略空间以非线性区分优势强弱。
- 超线性塑形：定义Â = sign(Δr)·|Δr|^(1+γ)，在高优势方向放松约束（更大步长），在低优势方向收紧（抑制虚假更新）（Theorem 3）。
- 稳定化：采用批级标准差归一化以适应不同奖励尺度，防止过大/过小优势导致的梯度不稳；方法无侵入接入GRPO式后训练流程，推理阶段无需改动。

#### 创新点
- 从信息几何视角扩展Fisher–Rao度量为优势加权的非线性几何，提出超线性优势塑形以克服线性更新难以抗噪的问题。
- 理论上给出从去除prompt级标准差到非线性几何更新的统一推导（含Theorem 2与Theorem 3），明确最优上升方向与塑形形式。
- 通过去除prompt级标准差并配合批级归一化，缓解归一化误配导致的优势高估与reward hacking，而无需改动奖励模型。
- 在T2I后训练场景中提供一种简单可插拔的算法层面解决方案，相比仅调数据或设计奖励更具通用性。

#### 实验结论
- 任务与设置：在文本生成图像的强化后训练中评估，骨干包括SD1.4 (0.9B)与FLUX.1 Dev (12B)，与DanceGRPO在相同奖励配置下对比。
- 核心结果：SLAS训练收敛更快、对模型规模更稳健、在GenEval与UniGenBench++上取得更优出域性能，同时减轻reward hacking并保持语义与组合作图一致性；具体数值提升幅度文中未明确说明。
- 作者结论：SLAS在多基线与基准上稳定超越DanceGRPO，体现更强的泛化与鲁棒性，并提供抑制奖励模型偏置的有效机制。具体实验细节与完整指标表格文中未明确说明。
