# 2026-04-29 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## Dual-Branch Remote Sensing Infrared Image Super-Resolution
- **论文链接**: http://arxiv.org/abs/2604.10112v2
- **作者**: Xining Ge, Gengjia Chang, Weijun Yuan, Zhan Li, Zhanglu Chen, Boyang Yao, Yihang Chen, Yifan Deng, Shuhong Liu
- **原始摘要**: Remote sensing infrared image super-resolution aims to recover sharper thermal observations from low-resolution inputs while preserving target contours, scene layout, and radiometric stability. Unlike visible-image super-resolution, thermal imagery is weakly textured and more sensitive to unstable local sharpening, which makes complementary local and global modeling especially important. This paper presents our solution to the NTIRE 2026 Infrared Image Super-Resolution Challenge, a dual-branch system that combines a HAT-L branch and a MambaIRv2-L branch. The inference pipeline applies test-time local conversion on HAT, eight-way self-ensemble on MambaIRv2, and fixed equal-weight image-space fusion. We report both the official challenge score and a reproducible evaluation on 12 synthetic times-four thermal samples derived from Caltech Aerial RGB-Thermal, on which the fused output outperforms either single branch in PSNR, SSIM, and the overall Score. The results suggest that infrared super-resolution benefits from explicit complementarity between locally strong transformer restoration and globally stable state-space modeling.

### GPT总结
#### 文章内容
该论文面向遥感红外图像超分辨，针对热成像纹理弱、对局部锐化不稳定更敏感的问题，提出同时兼顾局部细节恢复与全局辐射一致性的方案。核心思路是构建双分支系统：以HAT-L承担强局部恢复、以MambaIRv2-L提供全局稳定建模，推理时分别配合TLC与八向自集成，并以等权图像空间融合输出。在NTIRE 2026隐藏测试集与从Caltech Aerial RGB-Thermal合成的12个×4样本上，融合结果在PSNR、SSIM与总体Score上均优于单分支。官方挑战得分为54.23，作者认为红外SR受益于“局部Transformer + 全局状态空间”的显式互补。

#### 方法
- 架构：双分支框架，包含HAT-L（Transformer）与MambaIRv2-L（state-space）两条主干，分别侧重局部边界恢复与全局辐射稳定。
- 训练：在NTIRE 2026开发集1019对红外图像上训练；两分支均用L1损失，HAT-L采用AdamW训练260K次迭代，MambaIRv2-L采用Adam训练250K次迭代；单卡NVIDIA H200完成训练。
- 推理（HAT-L）：窗口大小32，结合测试时本地转换（test-time local conversion，TLC）以增强局部细节重建。
- 推理（MambaIRv2-L）：采用八向几何自集成（eight-way self-ensemble）提高全局一致性与稳健性。
- 融合：在图像空间进行固定等权平均融合两分支输出，作为最终结果。

#### 创新点
- 将Transformer分支（HAT-L）的强局部细节恢复与状态空间分支（MambaIRv2-L）的全局稳定传播进行显式互补建模，契合红外图像“弱纹理、重边界与辐射一致性”的任务特性。
- 推理期针对不同分支定制化增强：对HAT-L引入TLC、对MambaIRv2-L采用八向自集成，并通过简单的等权图像融合有效汇聚两者优势。
- 给出可复现实验设置（Caltech Aerial RGB-Thermal合成的12个×4样本）验证双分支互补性的有效性，且无需复杂融合学习即可取得稳定增益。

#### 实验结论
- 任务与数据：在NTIRE 2026隐藏测试集与Caltech Aerial RGB-Thermal构建的12个×4合成热红外样本上评测；采用modcrop并在计算指标前裁去4像素边界。
- 结果：官方挑战最终得分54.23；在可复现实验上，融合结果在PSNR、SSIM及总体Score上均优于任一单分支；具体PSNR/SSIM数值文中未明确说明。
- 结论：作者认为红外超分辨适合采用“局部强Transformer恢复 + 全局稳态空间建模”的互补策略，能够同时提升边界结构与全局辐射一致性。

## 关键词：reinforcement learning

## World-R1: Reinforcing 3D Constraints for Text-to-Video Generation
- **论文链接**: http://arxiv.org/abs/2604.24764v1
- **作者**: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang
- **原始摘要**: Recent video foundation models demonstrate impressive visual synthesis but frequently suffer from geometric inconsistencies. While existing methods attempt to inject 3D priors via architectural modifications, they often incur high computational costs and limit scalability. We propose World-R1, a framework that aligns video generation with 3D constraints through reinforcement learning. To facilitate this alignment, we introduce a specialized pure text dataset tailored for world simulation. Utilizing Flow-GRPO, we optimize the model using feedback from pre-trained 3D foundation models and vision-language models to enforce structural coherence without altering the underlying architecture. We further employ a periodic decoupled training strategy to balance rigid geometric consistency with dynamic scene fluidity. Extensive evaluations reveal that our approach significantly enhances 3D consistency while preserving the original visual quality of the foundation model, effectively bridging the gap between video generation and scalable world simulation.

### GPT总结
#### 文章内容
本文针对文本生成视频模型在大幅相机运动和长时序场景中出现的几何错位与时序不一致问题，提出用强化学习将视频生成对齐至3D约束。核心思路是基于Flow-GRPO对预训练视频基础模型进行后训练，利用预训练3D基础模型与视觉语言模型提供的复合奖励，辅以隐式相机条件（噪声包裹）与周期性解耦训练以在“刚性几何一致性—动态流畅性”间取得平衡。实验显示在不改动架构的前提下显著提升3D一致性和相机控制，同时保持甚至提升原有视觉质量，并获得用户偏好优势。

#### 方法
- 基于Flow-GRPO的强化学习对齐：在不改动视频基础模型架构的前提下，以在线视频rollout与奖励反馈进行优化。
- 复合奖励设计：包含3D-aware奖励R3D（由预训练3D基础模型评估多视一致性/结构稳定）与通用生成奖励Rgen（由视觉语言模型评估语义一致与审美质量），共同约束物理有效性与感知质量。
- 纯文本“世界模拟”数据集：构建面向相机运动与场景结构的专用文本提示集以驱动RL对齐；数据规模与构成细节文中未明确说明。
- 隐式相机注入（噪声包裹，noise wrapping）：在扩散/流匹配的潜空间初始化中嵌入运动先验，促进轨迹对齐与收敛。
- 周期性解耦训练：交替使用刚性几何约束与动态数据子集，抑制过拟合静态刚性，保持非刚性动态的自然性。

#### 创新点
- 将“视频生成—3D几何一致性”的对齐问题重构为强化学习优化，结合Flow-GRPO与多源反馈，在无需显式3D模块或架构改动下为大模型注入空间意识与可扩展性。
- 提出基于预训练3D基础模型与VLM的复合奖励体系，直接以多视几何一致性与语义/审美质量作为优化目标，规避高成本的3D标注或渲染监督。
- 引入隐式相机条件（噪声包裹）作为运动先验，显著改善相机轨迹遵从性并加速收敛。
- 设计周期性解耦训练以平衡刚性结构一致性与非刚性动态流畅性，缓解“结构增强导致画面僵硬”的常见副作用。

#### 实验结论
- 任务与评测：在3DGS重建-重渲染框架下评估多视一致性，并在VBench进行通用视频质量评测；还开展了含30条复杂相机运动提示、25名受试者的盲评用户研究。VBench具体分数文中未明确说明。
- 核心结果：World-R1-Small在重建集上达成PSNR 27.63 / SSIM 0.858 / LPIPS 0.201，World-R1-Large达成PSNR 27.67 / SSIM 0.865 / LPIPS 0.162，显著优于CogVideoX-1.5-5B（PSNR 24.44 / SSIM 0.783 / LPIPS 0.242）与多种Wan 2.1/2.2基线；相较显式相机控制方法，保持更高的美学/成像质量与主体一致性。
- 用户偏好：相对于Wan 2.1，World-R1在几何一致性与相机控制上的胜率分别为92%与76%，总体偏好为86%，验证RL对齐在不牺牲视觉质量的前提下显著提升了几何合理性与控制力。
