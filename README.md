# 珞珈数智助教 (Luojia Math Tutoe) 🎓

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Agent Status](https://img.shields.io/badge/Agent-Online-brightgreen.svg)](http://lailuojia.whu.edu.cn/product/llm/chat/d5csn0eebtnc72t895n0)

[cite_start]**赋能大学数学教育的专属 AI 引擎** —— 武汉大学“火山杯”AI 智能体创新设计大赛参赛项目 [cite: 10]。

👉 **[点击这里立即体验珞珈数智助教](http://lailuojia.whu.edu.cn/product/llm/chat/d5csn0eebtnc72t895n0)**

---

## 💡 项目背景 (Pain Points)

[cite_start]目前的通用大模型文采飞扬，但一面对高等数学往往会遭遇“理科翻车” [cite: 3]。它们面临三大硬伤：
1. [cite_start]**算不准（计算幻觉）：** 面对高阶矩阵运算和复杂积分，常一本正经地算错数值，误导学生 [cite: 3]。
2. [cite_start]**画不出（缺乏可视化）：** 诸如方向导数、概率分布等抽象概念，纯文字解释让学生越看越懵，缺乏几何直观 [cite: 3]。
3. [cite_start]**管不住（暴力剧透）：** 传统搜题 AI 直接甩出最终答案，剥夺了学生的思考过程，沦为抄作业工具 [cite: 3]。

[cite_start]本项目专为被《高等数学》、《线性代数》、《概率论与数理统计》折磨的理工科大学生及考研党设计 [cite: 4][cite_start]。提供“权威概念答疑 + 动态图像绘制 + 考研难题分步引导”的真正导师级服务 [cite: 4]。

## 🚀 核心架构与创新 (Core Features)

[cite_start]珞珈数智助教摒弃了传统的单线程对话，采用 **“意图识别 —— 双引擎驱动 —— 多模态输出”** 的复合工作流架构 [cite: 35]：

### 1. 神经符号双引擎 (Neuro-Symbolic Engine)
[cite_start]我们引入了外部 Python “大脑皮层”接管纯粹的数值计算，彻底消灭 AI 幻觉 [cite: 6]。
* [cite_start]**分支 A（可视化解析）：** 面对抽象概念，系统自动调用本地知识库提取权威定义，并由 LLM 编写 `Matplotlib/NumPy` 代码 [cite: 5][cite_start]。沙盒运行生成动态几何图（如绘制 $z=x^2+y^2$ 的等值线与梯度向量图） [cite: 35]。
* [cite_start]**分支 B（严谨推导引擎）：** 面对复杂习题，LLM 负责输出宏观解题思路，并后台编写 `SymPy` 符号计算代码，获取绝对精确的数值解（保留6位有效数字） [cite: 37]。

### 2. 暗箱自愈风控 (Self-Healing System)
[cite_start]绝不“带病上岗” [cite: 6][cite_start]。在向用户输出结果前，系统后台会强制比对自然语言推理与代码运行结果 [cite: 6][cite_start]。若代码报错（`status_code != 0`），AI 会自动反思并重写代码，对学生端完全“隐形” [cite: 6, 37]。

### 3. 自适应助教人格 (Step-by-Step CoT)
[cite_start]不直接给答案，而是进行“考点定调”与思维链引导 [cite: 6][cite_start]。例如在积分计算卡壳时，智能体会利用后台算出的中间结果验证学生的推导，并抛出启发式提问（*“你觉得下一步该换元还是分部积分？”*），符合真实教育心理学 [cite: 35][cite_start]。所有的复杂数学公式均转化为严谨优美的 LaTeX 排版输出 [cite: 6]。

## 🗄️ 珞珈数学武器库 (Data Moat)

[cite_start]为了支撑高质量的推理引擎，我们构建了包含超 10,000 条高质量结构化记录的三层金字塔数据基座 [cite: 7]：
* [cite_start]**L1 权威基座：** 从武大同济版现行教材提纯的 500+ 定理与定义 [cite: 7]。
* [cite_start]**L2 推理引擎：** 基于 OpenMathInstruct-1 开源数据集，通过自研 Python 自动化数据流水线（`process_math_corpus_final_v5.py`）清洗出的 8,000+ 包含“问题-代码-解答”的三元组数据 [cite: 40]。
* [cite_start]**L3 评测标准：** 独家整理的 2016-2024 考研数学一真题库 [cite: 7, 40]。

[cite_start]**自动化提纯流水线揭秘：** 原始数据经由 50+ 专业数学术语矩阵过滤 $\rightarrow$ 正则算法强制提取代码块 $\rightarrow$ LaTeX 深度脱水 [cite: 7, 40][cite_start]。严格的 JSON 结构化物理隔离（独立 `problem/concept` 字段精准匹配考点），确保 AI 检索精度 [cite: 21]。

## 👥 关于团队 (About the Team)
[cite_start]**队长：** 肖圣鑫 (武汉大学 数学与统计学院) [cite: 1, 34]
[cite_start]本项目致力于将强大的前沿算法架构与严谨的数理逻辑相结合。未来期待将该架构复用并推广至大学物理等更广阔的理工科领域 [cite: 9]。

---

*(Note: 涉及项目数据处理核心脚本 `process_math_corpus_final_v5.py` 可在仓库 `scripts/` 目录下查看。)*
