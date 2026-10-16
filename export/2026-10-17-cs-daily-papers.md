# 2026-10-17 计算机领域论文日报

> 更新时间范围：最近 1.5 天
> 分类限制：cs.
> 单次最多输出：3 篇

## 关键词：image super-resolution

## SR-Prominence: A Crowdsourced Protocol and Dataset Suite for Perceptually-Weighted Super-Resolution Artifact Evaluation
- **论文链接**: http://arxiv.org/abs/2605.14847v2
- **作者**: Ivan Molodetskikh, Kirill Malyshev, Mark Mirgaleev, Nikita Zagainov, Evgeney Bogatyrev, Dmitriy Vatolin
- **原始摘要**: Modern image super-resolution methods generate detailed, visually appealing results, but they often introduce visual artifacts: unnatural patterns and texture distortions that degrade perceived quality. These defects vary widely in perceptual impact--some are barely noticeable, while others are highly disturbing--yet existing detection methods treat them equally. We propose artifact prominence as an evaluative target, defined as the fraction of viewers who judge a highlighted region to contain a noticeable artifact. We design a crowdsourced annotation protocol and construct SR-Prominence, a dataset suite containing 3,935 artifact masks from DeSRA, Open Images, Urban100, and a realistic no-ground-truth Urban100-HR setting, annotated with prominence. Re-annotating DeSRA reveals that 48.2% of its in-lab binary artifacts are not noticed by a majority of viewers. Across the suite, we audit SR artifact detectors, image-quality metrics, and SR methods. We find that classical full-reference metrics, especially SSIM and DISTS, provide surprisingly strong localized prominence signals, whereas no-reference IQA methods and specialized artifact detectors often fail to generalize across datasets and reference settings. SR-Prominence is released with an objective scoring protocol that allows new metrics to be benchmarked on our suite without further crowdsourcing. Together, the data and protocols enable SR artifact evaluation to move from binary defect presence toward perceptual impact. SR-Prominence is available at https://huggingface.co/datasets/imolodetskikh/sr-artifact-prominence.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。

## 关键词：reinforcement learning

## Value as Memory: Online Value-Guided Post-training for General Robot Policies
- **论文链接**: http://arxiv.org/abs/2610.22368v1
- **作者**: Wenye Yu, Yijin Chen, Kaiyi Xiong, Wenbo Han, Wendi Chen, Yang Jin, Han Xue, Jun Lv, Cewu Lu, Chuan Wen
- **原始摘要**: Real-world post-training of generalist robot policies faces two challenges: partial observability makes action selection ambiguous, while offline post-training methods delay feedback from deployment experience. We present Value as Memory (VaM), a framework that addresses these challenges through value caching and online real-world reinforcement learning (RL). Value caching conditions actions on recent value predictions as task-progress memory, while online updates enable timely policy improvement by combining offline demonstrations, off-policy interventions, and on-policy rollouts for sample-efficient adaptation. As a result, VaM transitions from offline RL warmup to online autonomous learning with sparse rewards. Across long-horizon tasks involving deformable objects and contact-rich manipulation, VaM yields a mean absolute success-rate gain of $29.4\%$ with value caching, while achieving a $32.8\%$ gain with online autonomous learning over matched offline training. The evaluated online schedule performs $8\times$ as many policy iterations under the same gradient-step budget, with more than $2\times$ lower recorded time per gradient step with concurrent data collection and training.

### GPT总结

当前论文的 GPT 总结生成失败：`The server is overloaded or not ready yet.`

建议检查 `OPENAI_API_KEYS`、`OPENAI_API_BASE`、`OPENAI_MODEL` 是否可用，然后重新运行脚本。
