# AI Learning Compass / 人工智能学习指南针

AI Learning Compass 是一个面向中文 AI 小白的开源学习路线规划 Agent。

它帮助用户根据自己的基础、目标、学习时间和学习偏好，生成个性化 AI 学习路线，并推荐适合的课程资源、实践项目和下一步行动计划。

---

## 项目定位

在 AI 快速发展的时代，很多初学者并不是缺少资料，而是面临这些问题：

- 不知道从哪里开始学习 AI
- 不知道 Prompt、Python、机器学习、RAG、Agent 应该先学哪个
- 收藏了很多课程，但没有清晰学习顺序
- 学了很多理论，却做不出一个实际项目
- 想参加大创、比赛或做作品集，但不知道如何规划路线

AI Learning Compass 的目标是：

> 让每一个想学习 AI 的人，都能找到适合自己的起点、路径和第一个项目。

---

## 核心功能

- 学习画像诊断
- 个性化 AI 学习路线生成
- 7 天 / 30 天 / 90 天学习路径规划
- 老师与课程资源推荐
- AI 项目实践建议
- 下一步行动清单生成
- Markdown 学习计划下载

---

## 运行效果

### 首页表单

![首页表单](assets/demo-form.png)

### 学习路线生成结果

![学习路线生成结果](assets/demo-result.png)

---

## 第一版 MVP

当前版本是一个最小可用原型，主要实现：

1. 用户填写学习情况
2. 系统生成用户学习画像
3. 系统读取本地路线数据
4. 输出 4 周 AI 学习路线
5. 推荐课程资源
6. 生成下一步行动清单
7. 支持下载 Markdown 学习计划

当前版本暂未接入大模型 API，路线生成主要基于结构化 YAML 数据和规则模板。

---

## 适合人群

- AI 零基础小白
- 想用 AI 提高学习效率的学生
- 想做 AI 项目的大学生
- 准备参加大创、互联网+、挑战杯等比赛的人
- 想入门 AI 应用开发的人
- 想学习 Prompt、RAG、Agent 的初学者

---

## 项目结构

```text
ai-learning-compass/
├── app/
│   └── main.py              # Streamlit 应用入口
├── data/
│   ├── courses.yaml         # 课程资源数据
│   ├── projects.yaml        # 项目实践资源
│   └── roadmaps.yaml        # 学习路线数据
├── docs/
│   ├── product-positioning.md
│   └── run-locally.md
├── assets/
│   ├── demo-form.png
│   └── demo-result.png
├── README.md
├── requirements.txt
└── LICENSE
