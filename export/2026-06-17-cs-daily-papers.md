# 2026-06-17 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## The Value Axis: Language Models Encode Whether They're on the Right Track
- **论文链接**: http://arxiv.org/abs/2606.17056v1
- **作者**: Nick Jiang, Isaac Kauvar, Jack Lindsey
- **原始摘要**: We investigate whether language models internally track the value of their current trajectory, defined as the likelihood that their ongoing strategy will achieve their goals. Using synthetic, in-context reinforcement learning data, we construct a "value" axis for Qwen3-8B. We find that activations along this axis distinguish between high vs. low verbalized confidence, rollouts without and with backtracking, and correct vs. corrupted code. Steering towards high value causally suppresses self-correction and reduces explanatory verbosity, while steering towards low value induces backtracking and exploration. We demonstrate that direct preference optimization (DPO) can increase the internal value of rewarded behaviors (e.g. use a certain word), causing the model to act more confidently after exhibiting them. Finally, we apply the value axis to study in-the-wild settings. For example, we find that Qwen assigns low value to politically sensitive chat queries after post-training and that supervised fine-tuning increases internal confidence within the training domain. Our results suggest that language models linearly encode an estimate of expected goal success that modulates their confidence in pursuing a direction.

### GPT总结
#### 文章内容
论文探究大型语言模型是否在内部编码“当前轨迹的价值”（即当前策略达成目标的可能性），并在Qwen3-8B中构建了一个可线性提取与操控的“value axis”。核心思路是用合成的 in-context RL 对话生成带正负反馈的轨迹，比较“发现隐藏准则”前后片段以拟合价值方向，并在多域验证其与信心、回溯、代码正确性等行为的相关与因果作用。主要结论是：该轴在层21–22上泛化良好（对25个留出准则AUROC>0.95），沿轴正向/负向干预分别诱导坚持/回溯、减少/增多解释，DPO与SFT等后训练可系统性地抬升特定行为的内部价值与自信，并在真实聊天场景中反映域内与敏感话题的差异。

#### 方法
- 构建ICRL数据：用Claude Opus 4.6合成300段对话，模型在50个隐藏准则上迭代修改段落并收到±1反馈，随机在第2–6个seed后“发现”准则（单次满足），单轮最多5次尝试。
- 价值轴拟合：对“首次发现准则”后与之前的段落token在Qwen3-8B各层隐藏状态做对比，得到线性方向作为value axis，主用layer 21（亦在22层有效）。
- 泛化评估：在25个留出准则上以“发现前/后token分类”为任务，计算AUROC验证跨准则的可迁移性。
- 表征分析与操控：用logit lens投影轴向，发现促发“积极/鼓励”类token；通过在解码时对中间层激活做线性steering，观察因果行为变化。
- 跨域测试：在AIME数学、代码生成与真实聊天（Chatbot Arena）等场景测量轴值与显式信心、回溯、注释冗长度、代码错误等的关联与受控变化；评估DPO与SFT对内部价值的迁移效应。

#### 创新点
- 提出语言模型内部“价值函数”的线性可提取方向（value axis），并以ICRL对话中的“发现前/后”对比作为监督信号，避免依赖任务专属标签。
- 结合表征因果操控：沿价值轴正/负向steering可系统地调制坚持 vs. 回溯、解释冗长度等高层决策行为，显示单一轴可跨任务调控“是否在正确方向上”的策略判断。
- 展示后训练对内部价值的重塑：DPO对偏好词的奖励会提升其内部价值并诱导更高自信；SFT与evaluation-awareness训练在域内/评测提示上抬升内部价值。
- 分层表征洞察：价值表示在中层涌现（layer 13后方向突变、前后近正交），最佳效果出现在layer 21–22，揭示价值相关信息的层级位置。

#### 实验结论
- ICRL泛化：在25个留出准则上，基于layer 21–22的value axis对“发现前/后token”分类AUROC>0.95；logit lens显示轴正向对应“积极鼓励”类token。
- 跨域因果效应：在AIME题目中，轴值与模型口头自信一致，正向steering减少回溯、负向steering增加探索；在代码任务中，轴值区分正确与损坏代码，正向steering减少解释/注释冗余。
- 后训练与“在野”观察：DPO提升被偏好词的内部价值并诱导更自信行为；在Chatbot Arena上，后训练后对信息抽取query内部价值更高、政治敏感query更低；SFT提升训练域内内部价值，evaluation-awareness训练提升评测提示上的内部价值。
