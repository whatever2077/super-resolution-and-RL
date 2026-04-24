# 2026-04-25 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Multiscale Super Resolution without Image Priors
- **论文链接**: http://arxiv.org/abs/2604.21810v1
- **作者**: Daniel Fu, Gabby Litterio, Pedro Felzenszwalb, Rashid Zia
- **原始摘要**: We address the ambiguities in the super-resolution problem under translation. We demonstrate that combinations of low-resolution images at different scales can be used to make the super-resolution problem well posed. Such differences in scale can be achieved using sensors with different pixel sizes (as demonstrated here) or by varying the effective pixel size through changes in optical magnification (e.g., using a zoom lens). We show that images acquired with pairwise coprime pixel sizes lead to a system with a stable inverse, and furthermore, that super-resolution images can be reconstructed efficiently using Fourier domain techniques or iterative least squares methods. Our mathematical analysis provides an expression for the expected error of the least squares reconstruction for large signals assuming i.i.d. noise that elucidates the noise-resolution tradeoff. These results are validated through both one- and two-dimensional experiments that leverage charge-coupled device (CCD) hardware binning to explore reconstructions over a large range of effective pixel sizes. Finally, two-dimensional reconstructions for a series of targets are used to demonstrate the advantages of multiscale super-resolution, and implications of these results for common imaging systems are discussed.

### GPT总结
#### 文章内容
这篇论文针对仅有平移情况下超分辨率（SR）的不适定性问题，提出利用多尺度（不同有效像素尺寸）低分辨数据来消除歧义、无需图像先验的方案。核心思路是选择成对互质的像素尺寸，使各尺度在傅里叶域提供互补信息，从而构成可稳定求逆的系统，并用傅里叶域显式重建或迭代最小二乘实现。主要结论包括：对d维信号，只需d+1个成对互质的整数像素尺寸即可稳定重建（Theorem 5.7），并给出大尺度信号在i.i.d.噪声下最小二乘重建的期望误差表达式，阐明噪声-分辨率权衡（Theorem 5.8, Observation 5.9）。在1D与2D实验（基于CCD硬件binning）中，三尺度样本（221/234/247 µm，对应13 µm的17/18/19倍）重建出与13 µm像素相当的细节，显示多尺度优于单一或双尺度。

#### 方法
- 成像建模：将连续辐照度在像素内积分形成离散观测；通过改变传感器像素或光学放大率获得多种有效像素尺寸（实践中用CCD硬件binning实现）。
- 尺度设计：选取成对互质的整数倍像素尺寸；对d维信号，使用d+1个互质尺度保证系统稳定可逆（Theorem 5.7）。
- 重建策略：基于各尺度混叠在频域的互补性，采用傅里叶域显式求逆，或将观测写成线性方程组并用迭代最小二乘求解。
- 数据组织：在每个尺度下获取多张低分辨图并进行interlacing组合，跨尺度汇聚为统一超分辨重建。
- 噪声分析：在i.i.d.噪声假设下推导最小二乘重建的期望误差公式，刻画噪声-分辨率折中（Theorem 5.8, Observation 5.9）。

#### 创新点
- 用多尺度采样（成对互质像素尺寸）从根本上解决平移SR的不适定性，无需任何图像先验或训练数据，即可仅凭成像约束实现稳定重建。
- 给出严格的充分条件：d维信号只需d+1个互质尺度即可稳定重建，并提供高效的傅里叶域重建与迭代最小二乘两种实现路径。
- 提供最小二乘重建在i.i.d.噪声下的期望误差解析式，系统揭示多尺度SR的噪声-分辨率权衡。
- 通过CCD硬件binning在高倍数尺度（17/18/19×）上的系统实证，验证理论在1D与2D中的可行性与鲁棒性。

#### 实验结论
- 任务与数据：在1D与2D设置下进行验证，利用CCD硬件binning生成不同有效像素尺寸的多尺度观测；具体数据集与目标类别细节文中未明确说明。
- 核心结果：三尺度（221/234/247 µm，分别为13 µm的17/18/19倍、两两互质）联合重建可恢复接近13 µm像素的细节；多尺度明显优于单尺度或双尺度设置。
- 作者结论：多尺度SR在理论与实践上均可使平移场景的SR问题变为适定并可高效求解，对常见成像系统（如多相机/变焦镜头/显微镜）具有直接启示。

## 关键词：reinforcement learning

## Cyber Defense Benchmark: Agentic Threat Hunting Evaluation for LLMs in SecOps
- **论文链接**: http://arxiv.org/abs/2604.19533v3
- **作者**: Alankrit Chona, Igor Kozlov, Ambuj Kumar
- **原始摘要**: We introduce the Cyber Defense Benchmark, a benchmark for measuring how well large language model (LLM) agents perform the core SOC analyst task of threat hunting: given a database of raw Windows event logs with no guided questions or hints, identify the exact timestamps of malicious events.   The benchmark wraps 106 real attack procedures from the OTRF Security-Datasets corpus - spanning 86 MITRE ATT&CK sub-techniques across 12 tactics - into a Gymnasium reinforcement-learning environment. Each episode presents the agent with an in-memory SQLite database of 75,000-135,000 log records produced by a deterministic campaign simulator that time-shifts and entity-obfuscates the raw recordings.   The agent must iteratively submit SQL queries to discover malicious event timestamps and explicitly flag them, scored CTF-style against Sigma-rule-derived ground truth.   Evaluating five frontier models - Claude Opus 4.6, GPT-5, Gemini 3.1 Pro, Kimi K2.5, and Gemini 3 Flash - on 26 campaigns covering 105 of 106 procedures, we find that all models fail dramatically: the best model (Claude Opus 4.6) submits correct flags for only 3.8% of malicious events on average, and no run across any model ever finds all flags.   We define a passing score as >= 50% recall on every ATT&CK tactic - the minimum bar for unsupervised SOC deployment. No model passes: the leader clears this bar on 5 of 13 tactics and the remaining four on zero.   These results suggest that current LLMs are poorly suited for open-ended, evidence-driven threat hunting despite strong performance on curated Q&A security benchmarks.

### GPT总结
#### 文章内容
该论文旨在评估大型语言模型（LLM）在无提示、开放式安全运营（SOC）威胁狩猎中的能力：面对仅含原始Windows事件日志的数据库，能否自主提出假设、发起查询并精确标注恶意事件时间戳。核心思路是将OTRF Security-Datasets中106个真实攻击过程封装为一个Gymnasium强化学习环境，提供经时间平移与实体混淆的单表SQLite日志，限制查询预算，要求代理以SQL迭代检索与提交“旗标”时间戳，采用叙事步骤覆盖率（Coverage Score）计分。主要结论是多家前沿LLM在该开放式任务上表现不佳：无模型达到作者设定的通过线（每个ATT&CK战术≥50%召回），且无一次运行能找全所有威胁，显示当前LLM难以胜任证据驱动的端到端威胁狩猎。

#### 方法
- 数据与模拟器：基于OTRF Security-Datasets（Mordor）提取106个攻击过程，覆盖93 MITRE ATT&CK子技术、13个战术；通过确定性“战役”模拟器进行时间平移与逐步实体混淆，组合多阶段攻击链并防止记忆化。
- 环境设计：实现Gymnasium环境HolodeckHuntEnv，提供单表、内存型SQLite日志（约75k–135k条、恶意占比约1–5%），仅允许通过SQL收集信息，无RAG/工具API。
- 交互与预算：动作为空间为自由格式SQL字符串；每次查询最多返回10行；每回合可选择查询或提交恶意时间戳；最大50次查询（75步安全上限），可提前放弃。
- 标注与对齐：以Sigma规则及LLM补充的后果事件构建旗标集合，时间戳按微秒精度匹配并统一UTC后缀。
- 评分机制：主指标Coverage Score=被覆盖的“叙事步骤”占比（按实例平均）；辅以n_flags_in_submitted与n_flags_in_query诊断“看见但未归因”的差距。

#### 创新点
- 任务建模新意：面向“无引导问题”的开放式威胁狩猎，要求代理自主形成假设、迭代检索与证据归因，区别于传统知识/引导式日志问答基准。
- 真实可扩数据：使用真实Windows攻防遥测并通过可编程模拟器构造可扩规模、多阶段、具杀伤链依赖的战役，叠加时间/实体扰动以防止模式记忆。
- 指标设计：提出面向“叙事步骤”的Coverage Score，弱化不同战役旗标密度差异，更关注端到端攻击链覆盖与进展连续性。
- 防御视角评测：作为现有攻防CTF/渗透型基准的防御侧对应，首次系统性评估“证据发现+显式标注”的代理能力。

#### 实验结论
- 任务与数据：在26个战役上评测，覆盖106个过程中的105个，涉及93个ATT&CK子技术/13个战术；日志规模约75k–135k行/实例，恶意事件占比约1–5%。
- 模型与设置：评测多款前沿模型（如Claude Opus 4.6/4.7、GPT-5、Gemini 3.1 Pro、Kimi K2.6、Qwen3.6 Plus、DeepSeek V3.2、MiniMax M2.7），仅通过SQL交互、无外部工具。
- 核心结果与结论：所有模型均未达成通过线（每个战术≥50%召回），最佳模型仍在13个战术中的6个未达标，且无一次运行能发现全部威胁；作者据此认为，现阶段LLM不适用于无监督、开放式的证据驱动威胁狩猎。
