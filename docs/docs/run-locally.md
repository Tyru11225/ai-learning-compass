# 本地运行指南

这个文档说明如何在本地运行 AI Learning Compass / 人工智能学习指南针。

## 1. 克隆项目

```bash
git clone https://github.com/Tyru11225/ai-learning-compass.git
cd ai-learning-compass
```

## 2. 安装依赖

```bash
pip install -r requirements.txt
```

## 3. 启动应用

```bash
streamlit run app/main.py
```

## 4. 打开浏览器

运行成功后，浏览器通常会自动打开本地页面。

如果没有自动打开，可以手动访问：

```text
http://localhost:8501
```

## 5. 项目运行效果

用户填写自己的学习基础、学习目标和可投入时间后，系统会生成：

- 用户学习画像
- 30 天 AI 学习路线
- 推荐课程与资源
- 下一步行动清单
