# 2026-07-30 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance
- **论文链接**: http://arxiv.org/abs/2607.26040v1
- **作者**: Gaspard Lambrechts, Adrien Bolland, Daniel Ebi, Damien Ernst
- **原始摘要**: Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available. Focusing on model-based reinforcement learning, we study the effect of asymmetric learning on observation representations and on privileged information representations. First, we identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer. Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer. Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.

### GPT总结
#### 文章内容
该文研究模型驱动的非对称强化学习，指出 Informed Dreamer 在学习“特权信息”潜表示时使用的非对称 VAE 目标存在松弛下界、导致表示不理想的问题。作者提出 Reinformed Dreamer：以“特权变分编码器”定义更正确的特权表示学习目标，并用“latent guidance”联合训练仅依赖观测的编码器，在保持单一世界模型与不改变 Dreamer 想象流程的前提下提升性能。实验显示，在多个基准上其相较 Dreamer 的提升更一致，优于以往非对称方法。

#### 方法
- 单一世界模型、双编码器结构：训练期可用的 privileged encoder 与执行期依赖观测的 unprivileged encoder。
- 以特权变分编码器为特权信息建立合适的变分目标（对其似然的更严格下界），修复 Informed Dreamer 的松下界问题。
- 通过 latent guidance 将 unprivileged encoder 对齐到特权潜表示，使仅凭观测历史即可获得足以控制的表示。
- 保持 Dreamer 风格的想象与基于想象的 actor-critic 流程不变，世界模型仍预测奖励与下一步潜表示；无需像 Scaffolder 那样进行显式解码-再编码。
- 训练阶段利用特权信息进行监督，对执行阶段仅用观测与动作历史运行策略。

#### 创新点
- 提出“latent guidance”非对称表示学习目标，在单一世界模型内实现 privileged/unprivileged 双编码器对齐。
- 采用 privileged variational encoder，提供更合适的特权表示学习目标，克服 Informed Dreamer 使用的非对称 VAE 的松弛下界问题。
- 在不增加想象开销的前提下避免 Scaffolder 的双世界模型与显式解码流程，提升训练与推理效率。
- 系统分析非对称学习对观测表示与特权表示的影响，明确现有方法的表示瓶颈并给出修正路径。

#### 实验结论
- 在“several benchmarks/several suites of environments”上，Reinformed Dreamer 相比 Dreamer 展现更一致的性能提升，且相较既有非对称方法表现更稳定/一致。
- 方法在部分可观及可用更细粒度状态信息的场景均有效，验证了使用特权指导学习表示并在执行期去特权的可行性。
- 具体任务名称、数据集、评测指标与绝对数值，文中未明确说明。
