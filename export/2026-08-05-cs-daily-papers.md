# 2026-08-05 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Loggia dei Lanzi: AI Thermography Enhancement Comparisons through 3D Photogrammetry
- **论文链接**: http://arxiv.org/abs/2608.02404v1
- **作者**: Scott McAvoy, Jonathan Klingspon, George Bent, Dave Pfaff, Aviral Agarwal, Maurizio Seracini, Falko Kuester
- **原始摘要**: The Loggia dei Lanzi in the Piazza della Signoria is one of Florence's most prominent structures visited by millions every year. Its construction history spans multiple centuries of modification. This paper presents the results of a thermal imaging campaign conducted in December 2025, using a FLIR T1020 HD camera, revealing hidden architectural features including walled-up openings and material transitions beneath the plaster surface. The favorable winter ambient conditions provided a feature-rich benchmark upon which to compare the results of enhancement algorithms and artificial intelligence models. We evaluate the application of AI-based image enhancement to thermal heritage documentation through a comparison of three tiers of image resolution in a photogrammetric Structure-from-Motion (SfM) pipeline: native resolution, FLIR's hardware-based pixel-shifted super-resolution (UltraMax), and state of the art AI-upscaled imagery models. We quantify the effect of each resolution tier on feature detection and tie-point generation, assessing whether the additional detail produced by super-resolution, whether hardware or AI-derived, translates into meaningfully denser and more accurate 3D thermal models. Our results contribute to the emerging intersection of artificial intelligence and heritage thermography by providing a direct comparison of hardware microscanning and AI super-resolution within a thermal photogrammetric workflow for cultural heritage. All datasets are made publicly available and accessible within an interactive 3D archival framework, and integrated into a custom citywide extended reality overlay application.

### GPT总结
#### 文章内容
该文在文化遗产热成像的SfM工作流中，对比原生分辨率、硬件像素移位超分（FLIR UltraMax）与AI超分（SwinIR、DRCT/TongJi-SR、DifIISR）的实际价值，关注其对特征检测、匹配与3D重建质量的影响。核心思路是在Agisoft Metashape v2.2中统一管线、固定相机位姿与标定，跨四种分辨率以几何一致性（reconstruction uncertainty）与GSD归一化重投影误差进行评估。结论显示UltraMax仅带来轻微的tie-point增益但稀疏点云更干净、接近原生质量；AI超分无可测提升且按质量指标出现降级，并因需要从16-bit降至8-bit而不利于定量记录。作者建议在受控位移条件下继续验证UltraMax，AI超分更适合可视化传播而非定量测量。

#### 方法
- 采集与对齐：用FLIR T1020 HD在冬季现场采集161张热像，160张进入网络；各层级成功对齐数为154–159，最终选用所有层级共同对齐的149张进行严格比较。
- 统一SfM设置：在Agisoft Metashape Professional v2.2中处理，导入先前LiDAR对齐的固定相机位姿；相机标定一次性在原生图像求解，并按分辨率比（2×/4×/8×）缩放焦距与主点，畸变系数保持不变，避免逐层自标定漂移。
- 指标采集：项目级记录tie-point数量、总投影、平均重投影误差与GSD；点级通过自编Metashape Python脚本导出观测次数、重投影误差、reconstruction uncertainty、projection accuracy。
- 归一化与判据：用固定采集几何解析得到GSD，并将重投影误差换算到毫米（8.75/4.375/2.188/1.094 mm/px）；以reconstruction uncertainty为主判据，设置bicubic上采样为控制；不将各输出重采样到统一网格以避免低通滤波掩盖高频合成内容；特征检测采用SIFT。
- 分辨率与模型：跨四种分辨率与六个项目，包含原生、硬件UltraMax（2×）、AI模型SwinIR、DRCT/TongJi-SR（TongJi）、DifIISR，以及bicubic基线；各模型在其原生输出分辨率下评估。

#### 创新点
- 在文化遗产热成像的SfM管线中，首次直接对比硬件微扫描（UltraMax）与多种AI超分（SwinIR/DRCT/TongJi-SR/DifIISR），并以bicubic作为像素增多的控制基线。
- 评价转向跨视角几何一致性，使用reconstruction uncertainty与GSD归一化重投影误差，且通过固定相机位姿与标定严格隔离图像内容对重建的影响。
- 提出“不重采样到统一分辨率”的对比策略，专门检验AI合成的高频细节在多视角中的可三角化一致性，而非依赖单幅PSNR/SSIM。
- 数据集全公开并集成至交互式3D归档与城市级XR叠加应用，提升热遗产文档的可访问性与复用性。

#### 实验结论
- 在Loggia dei Lanzi场景中，UltraMax相较原生仅提供边际的tie-point增益，但其稀疏点云的reconstruction uncertainty与跨视一致性最佳、接近原生质量；其优势规模有限，可能受现场“手抖式”位移不完全匹配专利算法要求的影响，需在精确致动的亚像素位移等受控条件下进一步验证。
- SwinIR、DRCT/TongJi-SR、DifIISR等AI超分在SfM重建中无可测提升且按质量指标出现降级；获取其输出需将16-bit辐射数据降为8-bit，削弱定量热诊断的辐射学完整性。
- 统一采用149张共同对齐图像与解析GSD（8.75/4.375/2.188/1.094 mm/px）进行统计；作者建议UltraMax可作为低成本、低风险的附加采集步骤，而AI超分当前更适用于可视化与公众传播而非定量文档。文中未明确说明具体数值上的tie-point或误差增幅比例。

## 关键词：reinforcement learning

## Bridging Artificial Intelligence and Power Systems Education Using a Hands-On Executable Framework
- **论文链接**: http://arxiv.org/abs/2608.02599v1
- **作者**: Junjie Yin, Buxin She, Xinyu Feng, Fangxing, Li
- **原始摘要**: Artificial intelligence (AI) is increasingly central to power and energy systems, supporting modeling, forecasting, optimization, and control. Yet most existing works emphasize specialized applications and offer little reusable material for newcomers or interdisciplinary learners, who increasingly rely on large language models rather than building their own. This gap points to a need for engineering-grounded AI (EGAI), in which AI workflows follow established engineering and power-system domain rules rather than acting as task-agnostic black boxes. Motivated by a community survey of researchers and practitioners, which shows 92% report at least one barrier before running an AI model and 94% want a power-specific hands-on course. This paper presents a framework consisting of open, executable module library that lowers the entry barrier for AI in power systems. The modules follow a progressive difficulty ladder that maps core AI concepts onto representative power-system tasks: (i) foundational deep neural network (DNN) templates for function approximation and load-curve fitting; (ii) a domain-coupled convolutional neural network (CNN) power-flow surrogate for a 5-bus system; and (iii) frontier modules on DNN-assisted optimization, deep reinforcement learning (DRL) for battery storage control, and physics-informed neural networks (PINNs) for the swing equation. All modules are released as Jupyter notebooks that run locally or on Google Colab and are delivered through an IEEE online course and IEEE Power & Energy Society (PES) webinar series. The webinar drew more than 590 live attendees, which is among the ten most-attended IEEE PES webinars, and over 344 repository visits within two weeks, reinforcing the survey-based motivation.

### GPT总结
#### 文章内容
本文面向电力系统教育中AI入门门槛高、可复用教材缺失的问题，提出“工程约束型AI（Engineering-Grounded AI, EGAI）”理念与一套可执行、开源的教学模块库。核心思路是以渐进式难度阶梯，将基础到前沿的AI概念映射到代表性电力任务，并以可直接运行的Jupyter笔记本提供端到端示例。结论表明：统一的DNN模板能在未见数据上泛化到不同函数族并迁移到负荷曲线拟合；配套的IEEE课程与PES网络研讨会的参与度（>590 live）与仓库访问量（>344/两周）佐证了框架的实用性与需求。

#### 方法
- 渐进式三层模块库：Tier 1为基础DNN模板（多层感知机，TensorFlow/Keras，MSE+Adam）实现标量回归y=f(x)，支持sin/cos/exp/log/poly3/custom等可选目标；Tier 2为与电力域耦合的CNN 5-bus潮流代理；Tier 3含DNN-assisted optimization、用于电池储能控制的DRL与求解摆动方程的PINNs。
- 统一可配置训练流程：关键超参数（如EPOCHS、HIDDEN_LAYERS、TRAIN_RATIO等）集中在单一配置块暴露，避免改动底层代码；典型设置包含70/30训练–测试划分以评估泛化。
- 训练与推理：以未见测试集验证DNN在不同函数族与实际负荷数据上的拟合与泛化，流程从函数逼近无缝过渡到数据驱动的曲线学习。
- 可执行交付：全部模块以Jupyter notebooks发布，可在本地或Google Colab直接运行，并配套IEEE在线课程与IEEE PES系列讲座。
- Tier 2/3的具体网络结构、训练细节与超参数设定文中未明确说明。

#### 创新点
- 提出EGAI范式：将AI工作流置于明确的工程与电力系统规则之内，避免“任务无关黑盒”，强调可复用、可实操的工程化范式。
- 设计“难度阶梯”式教学框架：从函数逼近与负荷曲线拟合到5-bus潮流CNN代理，再到DNN-assisted optimization、DRL与PINNs，系统化连接基础概念与电力域代表任务。
- 提供统一、可执行且高度可配置的模板库：以配置驱动的DNN模板贯穿多任务，降低入门门槛、提升可移植性和可复用性。
- 面向社区的工程教育落地：通过Jupyter/Colab与IEEE课程+PES研讨会实现大规模传播与即时上手，弥补以往偏研究性、碎片化代码资源的不足。

#### 实验结论
- 任务与数据：在一维回归上针对sin与三次多项式等函数族进行泛化评估，并在实际负荷曲线数据上进行拟合，采用70/30训练–测试划分。
- 结果与观察：相同的MLP架构与训练管线在未见数据上能准确再现实函数与多项式曲线，并能重现负荷曲线形态，显示模板对不同映射的迁移性与泛化性；定量指标文中未明确说明。
- Tier 2/3的定量实验结果与对比基线文中未明确说明；作者指出IEEE PES研讨会>590人在线参与、代码仓库两周内>344访问，佐证框架的社区需求与实用价值。
