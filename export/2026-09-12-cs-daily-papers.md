# 2026-09-12 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Guided Super-Resolution of Digital Elevation Models with Diffusion-Based Image Generators
- **论文链接**: http://arxiv.org/abs/2609.11886v1
- **作者**: Armand Mihai Nicolicioiu, Dominik Narnhofer, Nando Metzger, Daniel Panangian, Ksenia Bittner, Konrad Schindler
- **原始摘要**: High-resolution digital surface models (DSMs) play an important role in urban analysis, 3D building reconstruction, and infrastructure monitoring, yet their availability remains limited due to the high cost and complexity of data acquisition. In contrast, coarse DSMs from commercial satellite missions are widely accessible, and high-resolution optical imagery is increasingly available from aerial and satellite platforms. We address the resulting mismatch in spatial resolution and propose a DSM superresolution approach that enhances 5 m DSMs to 0.5 m resolution, using guidance from high-resolution spectral images. Our method employs denoising diffusion to transfer information that is visible only in the image, like crisp outlines and detailed roof structures, into the elevation maps. In this way, surface details are reconstructed more accurately than with conventional interpolation or filtering techniques. Experiments on several cities in Central Europe demonstrate that the proposed approach produces high-quality DSMs with improved structural detail and accurate surface geometry. Our results highlight the potential of guided super-resolution with foundational image priors as a means of reconstructing high-resolution surface models.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## SenseNova-U1.5: Towards Native Unified Visual Intelligence
- **论文链接**: http://arxiv.org/abs/2609.11929v1
- **作者**: Haiwen Diao, Jiahao Wang, Chenjing Ding, Hanming Deng, Jiangnan Chen, Ruixi Zhang, Ruohui Wang, Wenwen Tong, Xiangyu Fan, Yubo Wang, Yue Zhu, Yuwei Niu, Zhengqi Bai, Zhiqian Lin, Zhitao Yang, Zhongang Cai, Bo Yang, Chen Feng, Chengguang Lv, Guangjia Liu, Guanlin Wang, Hanyu Zhang, Haojia Yu, Hongcan Xiao, Hongli Wang, Huan Wu, Huaping Zhong, Jian Fang, Jianan Fan, Jiaqi Li, Jiefan Lu, Jing Zuo, Jingcheng Ni, Junxiang Xu, Linjun Dai, Mutian Xu, Peishen Yan, Penghao Wu, Ruijie Mao, Ruisi Wang, Shihao Bai, Shuang Yang, Shuya Yang, Shuyan Zheng, Silei Wu, Siying Li, Tao Chu, Tianbo Zhong, Tongxi Zhou, Weichao Luo, Weichen Fan, Wenhao Jia, Wenjie Gao, Xiangli Kong, Yan Li, Yang Yong, Zimo Wen, Zixuan Qian, Wenxiu Sun, Ruihao Gong, Quan Wang, Lewei Lu, Lei Yang, Ziwei Liu, Dahua Lin
- **原始摘要**: We launch SenseNova-U1.5, an 8B-MoT native unified multimodal model that understands, reasons about, and generates visual content within an encoder-free and VAE-free architecture. We strengthen its visual interface through spatially coherent patch reconstruction and scale its training with carefully curated generation and editing data, improved task formulation, structural prompt enhancement, and native resolutions of up to 4K. For post-training, we optimize specialized experts for visual aesthetics, bilingual text rendering, infographic generation, and image editing, and consolidate their capabilities through multi-expert on-policy distillation. Across extensive evaluations, SenseNova-U1.5 largely advances image fidelity, text rendering, complex composition, multi-reference editing, and interleaved generation, while improving instruction following and preserving subject identity, geometry, and unmodified regions. Despite limited exposure to structured formats in its generation data, SenseNova-U1.5 generalizes effectively to long, complex, and structured visual instructions, further proving that multimodal understanding can transfer to visual planning and creation. Together, these findings position native unified modelling as a promising path towards systems that perceive, reason and create within a fully end-to-end framework. We will open-source training code, including supervised fine-tuning, reinforcement learning, and on-policy distillation.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
