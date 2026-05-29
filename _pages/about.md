---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am an undergraduate student of [School of Intelligence Science and Technology, Nanjing University](https://is.nju.edu.cn/) where I have the privilege of conducting research under the supervision of [Prof. Kai Zhang](https://cszn.github.io/).

I will join [XLANG Lab](https://xlang.ai/) as a PhD student, supervised by Prof. [Tao Yu](https://taoyds.github.io/), focusing on Spatial Intelligence, including VLA, World Action Model, and Embodied Agent.

Now, I am a Research Intern in [Qwen](https://qwen.ai/) supervised by [Shuai Bai](https://scholar.google.com/citations?user=ylhI1JsAAAAJ&hl=zh-CN), and also focus on the VLA!

My research interest includes Multimodal Learning. 

Feel free to reach out to me if you are interested.


# 🔥 News
- *2026.05*: &nbsp;🎉🎉 Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments is released on arXiv. I am a core contributor responsible for data processing and real-robot deployment.
- *2026.05*: &nbsp;🎉🎉 FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies is released on arXiv.
- *2025.06*: &nbsp;🎉🎉 Reverse Convolution and Its application to Image Restoration is accepted by ICCV2025.
<!-- - *2022.02*: &nbsp;🎉🎉 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/qwenvla_overview.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments](https://arxiv.org/pdf/2605.30280)

Qwen-VLA Team (**Xuhong Huang** is a core contributor, responsible for data processing, real-world benchmark design, and real-robot deployment)

- Qwen-VLA is a unified embodied foundation model that extends Qwen's vision-language modeling to continuous action and trajectory generation, achieving strong multi-task performance across manipulation, navigation, and trajectory prediction benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2026</div><img src='images/finevla_overview.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies](https://arxiv.org/pdf/2605.27284)

Xintong Hu<sup>*</sup>, **Xuhong Huang<sup>*</sup>**, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu<sup>†</sup> (<sup>*</sup>Equal Contribution, <sup>†</sup>Corresponding Author)

[**Project**](https://finevla.xlang.ai/)
- We introduce FineVLA, an open framework for action-aligned fine-grained VLA supervision, including a data construction tool, a held-out benchmark, a robotics-specialized VLM annotator, and a steerable VLA policy trained with controlled mixtures of fine-grained and raw goal-level instructions.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='images/1751533534899.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Reverse Convolution and Its application to Image Restoration](https://arxiv.org/pdf/2508.09824)

**Xuhong Huang<sup>*</sup>**, Shiqi Liu<sup>*</sup>, Kai Zhang<sup>†</sup>, Ying Tai, Jian Yang, Hui Zeng, Lei Zhang (<sup>*</sup>Equal Contribution, <sup>†</sup>Corresponding Author)

[**Project**](https://github.com/cszn/ConverseNet) <strong><span class='show_paper_citations' data='m0jbWYYAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose a novel depthwise
reverse convolution operator as a first-step exploration to
effectively reverse the depthwise convolution by formulating and solving a regularized least-squares optimization
problem.
</div>
</div>

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 🎖 Honors and Awards
- *2025.12* Nanjing University Top-Grade Scholarship,the highest honor in the university, awarded to only 13 students university-wide.
- *2025.10* Yanbao Scholarship (Top1).
- *2024.10* National Scholarship (Top5).
<!-- - *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2022.09 - Now*, *B.S.* Nanjing University, School of Intelligence Science and Technology. 
<!-- - *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2025.01 - 2025.9*, [CUHK MMLab](https://mmlab.ie.cuhk.edu.hk/index_cn.html), Hong Kong, China
- *2025.09 - 2026.1*, [XLANG](https://xlang.ai/), Hong Kong, China
- *2026.01 - now*, [Qwen](https://qwen.ai/), Beijing, China
