import streamlit as st
import yaml
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_yaml(file_name):
    file_path = DATA_DIR / file_name
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def build_profile(user_type, coding_level, goal, daily_time, duration):
    return f"""
### 一、用户学习画像

- 用户类型：{user_type}
- 编程基础：{coding_level}
- 学习目标：{goal}
- 每天可投入时间：{daily_time}
- 期望周期：{duration}
- 推荐学习方向：AI 应用开发入门路线
- 推荐路径：AI 认知 → Prompt → Python/API → RAG → Agent → 项目展示
"""


def build_roadmap(roadmaps):
    if not roadmaps:
        return "暂无路线数据，请先在 data/roadmaps.yaml 中添加学习路线。"

    roadmap = roadmaps[0]
    result = f"""
### 二、推荐学习路线：{roadmap.get("title", "未命名路线")}

目标：{roadmap.get("goal", "")}

难度：{roadmap.get("difficulty", "")}

周期：{roadmap.get("duration", "")}
"""

    for stage in roadmap.get("stages", []):
        result += f"""

#### 第 {stage.get("week")} 周：{stage.get("name")}

**学习目标：**

"""
        for item in stage.get("objectives", []):
            result += f"- {item}\n"

        result += "\n**任务安排：**\n\n"
        for item in stage.get("tasks", []):
            result += f"- {item}\n"

        result += "\n**阶段产出：**\n\n"
        for item in stage.get("output", []):
            result += f"- {item}\n"

    return result


def build_course_recommendations(courses):
    if not courses:
        return "暂无课程数据，请先在 data/courses.yaml 中添加课程资源。"

    result = "\n### 三、推荐课程与资源\n"

    for course in courses[:5]:
        result += f"""
#### {course.get("title")}

- 老师/机构：{course.get("teacher")}
- 平台：{course.get("platform")}
- 语言：{course.get("language")}
- 难度：{course.get("difficulty")}
- 推荐理由：{course.get("recommendation_reason")}
"""

    return result


def build_next_steps():
    return """
### 四、下一步行动清单

1. 先完成第 1 周的 AI 基础认知和 Prompt 练习。
2. 每天学习 30 到 60 分钟，不追求一次学完。
3. 第 1 周结束时，整理一份 AI 学习笔记。
4. 第 2 周开始尝试用 Python 调用大模型 API。
5. 第 4 周完成一个可以展示的 AI 学习路线规划 Demo。
"""


st.set_page_config(
    page_title="AI 学习指南针",
    page_icon="🧭",
    layout="wide"
)

st.title("🧭 AI 学习指南针")
st.caption("面向中文 AI 小白的开源学习路线规划 Agent")

st.markdown("""
这个 Demo 会根据你的基础、目标和学习时间，生成一份简单的 AI 学习路线。
当前版本是 MVP 原型，后续可以接入大模型 API，实现更智能的个性化规划。
""")

with st.form("profile_form"):
    st.subheader("填写你的学习情况")

    col1, col2 = st.columns(2)

    with col1:
        user_type = st.selectbox(
            "你目前的身份是？",
            ["AI 零基础小白", "大学生", "程序员", "产品/运营", "创业者", "科研/深造党"]
        )

        coding_level = st.selectbox(
            "你的编程基础如何？",
            ["完全不会编程", "会一点 Python", "能写简单项目", "有开发经验"]
        )

        daily_time = st.selectbox(
            "你每天大概能学多久？",
            ["30 分钟以内", "30 分钟到 1 小时", "1 到 2 小时", "2 小时以上"]
        )

    with col2:
        goal = st.selectbox(
            "你学习 AI 的主要目标是？",
            ["了解 AI 并提高效率", "做一个 AI 项目", "参加大创/比赛", "转 AI 应用开发", "系统学习机器学习", "做 AI 产品或创业"]
        )

        duration = st.selectbox(
            "你希望多久看到成果？",
            ["7 天", "30 天", "90 天", "半年以上"]
        )

        learning_style = st.selectbox(
            "你更喜欢哪种学习方式？",
            ["视频课程", "图文教程", "项目实战", "老师系统课", "边做边学"]
        )

    submitted = st.form_submit_button("生成我的 AI 学习路线")

if submitted:
    roadmaps = load_yaml("roadmaps.yaml")
    courses = load_yaml("courses.yaml")

    st.success("已生成你的 AI 学习路线")

    profile = build_profile(user_type, coding_level, goal, daily_time, duration)
    roadmap_text = build_roadmap(roadmaps)
    course_text = build_course_recommendations(courses)
    next_steps = build_next_steps()

    full_plan = profile + roadmap_text + course_text + next_steps

    st.markdown(full_plan)

    st.download_button(
        label="下载学习路线 Markdown 文件",
        data=full_plan,
        file_name="ai_learning_plan.md",
        mime="text/markdown"
    )
else:
    st.info("请先填写上方信息，然后点击“生成我的 AI 学习路线”。")
