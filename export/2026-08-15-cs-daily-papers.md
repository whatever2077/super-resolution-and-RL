# 2026-08-15 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：reinforcement learning

## Intern-S2-Preview: Scientific Agentic Foundation Model
- **论文链接**: http://arxiv.org/abs/2608.13505v1
- **作者**: Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, Erfei Cui, Xuanlang Dai, Shengyuan Ding, Shangheng Du, Yanhui Duan, Yue Fan, Youqing Fang, Quan Gan, Yuanyuan Gao, Jiaye Ge, Lixin Gu, Yuzhe Gu, Qipeng Guo, Junjun He, Xin Hong, Ming Hu, Zhouqi Hua, Haian Huang, Junhao Huang, Zixian Huang, Minxi Jin, Lingkai Kong, Alexander Lam, Zehao Li, Zonglin Li, Tianhao Liang, Dahua Lin, Junyao Lin, Tianyang Lin, Zhouhan Lin, Jiangning Liu, Jin Liu, Kuikun Liu, Wenran Liu, Yifei Liu, Yuhong Liu, Yuhong Liu, Zhoumianze Liu, Ziyan Liu, Ziyu Liu, Haijun Lv, Han Lv, Chengqi Lyu, Le Ma, Ningsheng Ma, Zerun Ma, Haoyang Peng, Runyu Peng, Jifei Shan, Zixin Shang, Kou Shi, Xiang Shi, Qisheng Su, Xuerui Su, Hao Sun, Xiao Sun, Yanan Sun, Yu Sun, Huanze Tang, Yinghao Tang, Wenhui Tian, Zhongbo Tian, Bingli Wang, Haomin Wang, Jiarui Wang, Jingzhi Wang, Rui Wang, Xiquan Wang, Yi Wang, Zhecan Wang, Ziyi Wang, Zun Wang, Rubin Wei, Lianyi Wu, Wen Wu, Yue Wu, Yuhan Wu, Zhenyu Wu, Zijian Wu, Shuhao Xing, Jun Xu, Xingle Xu, Xuenan Xu, Xiangchao Yan, Ziang Yan, Bowen Yang, Danni Yang, Lin Yang, Zhiqi Yang, Qian Yao, Haochen Ye, Peng Ye, Jinhui Yin, Jiashuo Yu, Dingbo Yuan, Fei Yuan, Yuhang Zang, Bo Zhang, Chao Zhang, Chen Zhang, Hongjie Zhang, Junming Zhang, Wenlong Zhang, Wenwei Zhang, Yiming Zhang, Zhuo Zhang, Ziyang Zhang, Haiteng Zhao, Penghao Zhao, Yibo Zhao, Zhonghan Zhao, Zhihang Zhong, Bowen Zhou, Peiheng Zhou, Xin Zhou, Xinyu Zhou, Yunhua Zhou, Dongsheng Zhu, Yicheng Zou
- **原始摘要**: Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific documents, interleaved image-text data, and diverse scientific corpora. Starting from the pretrained checkpoint, we apply a unified post-training pipeline consisting of supervised fine-tuning, scalable multi-task reinforcement learning (RL), black- and white-box agentic RL, and on-policy distillation. This pipeline is supported by practical techniques that improve rollout and training stability and efficiency, including partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly for agentic tasks. At the architecture level, Intern-S2-Preview-397B extends time series modelling from efficient long-sequence understanding to numerical forecasting, while Memory Decoder is studied as a separate memory-augmented path for rapid scientific specialization without modifying the frozen 397B backbone. Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show that Intern-S2-Preview-397B achieves competitive or leading results in multiple settings. The time series modules improve scientific signal understanding and forecasting on SciTS, while the separate Intern-MemDec-4B extension improves the Biology-Instructions average score from 56.92 to 60.32 without modifying the frozen 397B backbone.

### GPT总结
#### 文章内容
该工作面向科学发现中“多模态证据、工具交互与长程任务”需求，提出科学Agent型基础模型系列Intern-S2-Preview。其核心思路是先进行科学多模态预训练，再以统一的后训练管线融合SFT、可扩展多任务RL、黑/白盒Agentic RL与on-policy蒸馏，并在架构上加入时间序列预测分支与独立的Memory Decoder以支持快速专业化。结论表明，Intern-S2-Preview-397B在科学、多模态、Agentic与通用基准上达到有竞争力或领先的结果；时间序列模块提升了SciTS上的信号理解与预测，独立的Intern-MemDec-4B在不改动397B骨干的前提下将Biology-Instructions均分从56.92提升到60.32。

#### 方法
- 科学多模态预训练：覆盖渲染的科学文档、交织的图文数据与多样科学语料。
- 统一后训练管线：Supervised Fine-Tuning + 可扩展多任务RL + 黑/白盒Agentic RL + on-policy distillation。
- 训练/推理稳健性技术：partial rollout + off-policy校正、adaptive length regularization、online speculative decoding、稳健多任务优化、面向Agent任务的trace-aware经验组装。
- 架构设计：Intern-S2-Preview-397B在高效长序列理解基础上增设时间序列数值预测分支。
- 记忆增强专化：以独立的Memory Decoder路径（如Intern-MemDec-4B）实现快速科学领域专化，冻结397B骨干无需改动。

#### 创新点
- 将SFT、可扩展多任务RL、黑/白盒Agentic RL与on-policy蒸馏统一到一条面向科学Agent的后训练管线。
- 提出一套面向Agent长程交互与多任务RL的稳定/效率技术组合（partial rollout+off-policy校正、长度自适应正则、trace-aware经验组装、在线推测解码等）。
- 在基础模型中系统性扩展时间序列能力，从长序列理解到数值预测的一体化设计。
- 引入独立的Memory Decoder作为外置记忆增强与快速专化通道，实现对大骨干的“冻结式”增益。

#### 实验结论
- 覆盖广泛评测：在科学与通用任务、文本与多模态场景上评估（如Biology-Instructions、Mol-Instructions、MolecularIQ、SciReasoner、TOMG-Bench、MP20、ProteinBinder-9、XLRS-Bench、MicroVQA、SFE、ObsCrisis-Bench、SciCode、SGI-Bench、ResearchClawBench，以及MMLU-Pro、SimpleQA-Verified等），总体表现具竞争力或领先。
- 关键结果：时间序列模块提升SciTS上的理解与预测；独立Intern-MemDec-4B将Biology-Instructions均分从56.92提升到60.32，且不改动397B骨干。
- 其余具体分项分数与对比细节，文中未明确说明。
