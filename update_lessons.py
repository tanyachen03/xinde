#!/usr/bin/env python3
import re

# 所有课程的小节信息
courses = {
    "module1": {
        "title": "Python快速入门",
        "lessons": [
            {"title": "Python简介与环境准备", "emoji": "🐍", "duration": "15分钟", "type": "📹视频"},
            {"title": "Jupyter Notebook使用", "emoji": "📓", "duration": "20分钟", "type": "💻实战"},
            {"title": "基本语法与数据输出", "emoji": "📝", "duration": "25分钟", "type": "📹视频"},
            {"title": "变量定义与命名规范", "emoji": "📦", "duration": "20分钟", "type": "📄图文"},
            {"title": "数字运算与表达式", "emoji": "🔢", "duration": "25分钟", "type": "📹视频"},
            {"title": "初学者常见误区", "emoji": "⚠️", "duration": "15分钟", "type": "📄图文"},
        ]
    },
    "module2": {
        "title": "变量与数据类型",
        "lessons": [
            {"title": "数字类型详解", "emoji": "🔢", "duration": "20分钟", "type": "📹视频"},
            {"title": "字符串操作", "emoji": "📝", "duration": "25分钟", "type": "💻实战"},
            {"title": "列表基础", "emoji": "📋", "duration": "20分钟", "type": "📹视频"},
            {"title": "列表高级操作", "emoji": "⚡", "duration": "25分钟", "type": "💻实战"},
            {"title": "字典类型", "emoji": "📚", "duration": "20分钟", "type": "📹视频"},
            {"title": "元组与集合", "emoji": "🧩", "duration": "20分钟", "type": "📄图文"},
            {"title": "类型转换与判断", "emoji": "🔄", "duration": "15分钟", "type": "📄图文"},
        ]
    },
    "module3": {
        "title": "条件判断与循环",
        "lessons": [
            {"title": "if条件判断", "emoji": "✅", "duration": "20分钟", "type": "📹视频"},
            {"title": "if-else语句", "emoji": "🔀", "duration": "15分钟", "type": "📄图文"},
            {"title": "多条件判断", "emoji": "🔗", "duration": "20分钟", "type": "📹视频"},
            {"title": "逻辑运算符", "emoji": "🧮", "duration": "15分钟", "type": "📄图文"},
            {"title": "for循环基础", "emoji": "🔄", "duration": "20分钟", "type": "📹视频"},
            {"title": "for循环进阶", "emoji": "⚡", "duration": "25分钟", "type": "💻实战"},
            {"title": "while循环", "emoji": "🔁", "duration": "20分钟", "type": "📹视频"},
            {"title": "break与continue", "emoji": "⏸️", "duration": "15分钟", "type": "📄图文"},
        ]
    },
    "module4": {
        "title": "函数与模块",
        "lessons": [
            {"title": "函数定义与调用", "emoji": "📞", "duration": "20分钟", "type": "📹视频"},
            {"title": "函数参数详解", "emoji": "🔧", "duration": "25分钟", "type": "💻实战"},
            {"title": "可变参数", "emoji": "⭐", "duration": "20分钟", "type": "📹视频"},
            {"title": "匿名函数lambda", "emoji": "λ", "duration": "15分钟", "type": "📄图文"},
            {"title": "模块导入", "emoji": "📥", "duration": "15分钟", "type": "📹视频"},
            {"title": "常用内置模块", "emoji": "📦", "duration": "20分钟", "type": "📄图文"},
        ]
    },
    "module5": {
        "title": "Pandas核心操作",
        "lessons": [
            {"title": "Pandas简介与安装", "emoji": "🐼", "duration": "15分钟", "type": "📹视频"},
            {"title": "Series数据结构", "emoji": "📊", "duration": "20分钟", "type": "💻实战"},
            {"title": "DataFrame入门", "emoji": "📋", "duration": "25分钟", "type": "📹视频"},
            {"title": "读取CSV数据", "emoji": "📥", "duration": "20分钟", "type": "💻实战"},
            {"title": "数据基本信息", "emoji": "ℹ️", "duration": "15分钟", "type": "📄图文"},
            {"title": "列操作", "emoji": "📝", "duration": "20分钟", "type": "📹视频"},
            {"title": "行选择与切片", "emoji": "✂️", "duration": "25分钟", "type": "💻实战"},
            {"title": "loc标签索引", "emoji": "📍", "duration": "20分钟", "type": "📹视频"},
            {"title": "布尔索引筛选", "emoji": "🔍", "duration": "20分钟", "type": "💻实战"},
            {"title": "排序与排名", "emoji": "🏆", "duration": "15分钟", "type": "📄图文"},
        ]
    },
    "module6": {
        "title": "数据清洗实战",
        "lessons": [
            {"title": "缺失值检测", "emoji": "🔍", "duration": "20分钟", "type": "📹视频"},
            {"title": "缺失值处理策略", "emoji": "🔧", "duration": "25分钟", "type": "💻实战"},
            {"title": "重复值处理", "emoji": "🗑️", "duration": "15分钟", "type": "📹视频"},
            {"title": "异常值识别", "emoji": "⚠️", "duration": "20分钟", "type": "📄图文"},
            {"title": "数据类型转换", "emoji": "🔄", "duration": "20分钟", "type": "📹视频"},
            {"title": "字符串清洗", "emoji": "🧹", "duration": "25分钟", "type": "💻实战"},
            {"title": "正则表达式", "emoji": "🔤", "duration": "30分钟", "type": "📹视频"},
            {"title": "日期时间处理", "emoji": "⏰", "duration": "25分钟", "type": "💻实战"},
            {"title": "数据清洗综合实战", "emoji": "🎯", "duration": "30分钟", "type": "💻实战"},
        ]
    },
    "module7": {
        "title": "数据可视化",
        "lessons": [
            {"title": "Matplotlib基础", "emoji": "📈", "duration": "25分钟", "type": "📹视频"},
            {"title": "折线图", "emoji": "📉", "duration": "20分钟", "type": "💻实战"},
            {"title": "柱状图", "emoji": "📊", "duration": "20分钟", "type": "📹视频"},
            {"title": "直方图与密度图", "emoji": "📊", "duration": "20分钟", "type": "💻实战"},
            {"title": "饼图", "emoji": "🥧", "duration": "15分钟", "type": "📹视频"},
            {"title": "散点图", "emoji": "🔵", "duration": "20分钟", "type": "💻实战"},
            {"title": "图表美化", "emoji": "🎨", "duration": "20分钟", "type": "📄图文"},
            {"title": "Pandas绘图", "emoji": "🐼", "duration": "20分钟", "type": "💻实战"},
        ]
    },
    "module8": {
        "title": "分组聚合分析",
        "lessons": [
            {"title": "groupby基础", "emoji": "📦", "duration": "20分钟", "type": "📹视频"},
            {"title": "聚合函数", "emoji": "🔢", "duration": "25分钟", "type": "💻实战"},
            {"title": "多列分组", "emoji": "📊", "duration": "20分钟", "type": "📹视频"},
            {"title": "agg聚合方法", "emoji": "⚡", "duration": "25分钟", "type": "💻实战"},
            {"title": "transform方法", "emoji": "🔄", "duration": "20分钟", "type": "📹视频"},
            {"title": "透视表", "emoji": "🔍", "duration": "25分钟", "type": "💻实战"},
            {"title": "交叉表", "emoji": "🔗", "duration": "20分钟", "type": "📄图文"},
        ]
    },
    "module9": {
        "title": "时间序列入门",
        "lessons": [
            {"title": "时间格式转换", "emoji": "⏰", "duration": "20分钟", "type": "📹视频"},
            {"title": "DatetimeIndex", "emoji": "📅", "duration": "20分钟", "type": "💻实战"},
            {"title": "时间提取", "emoji": "📌", "duration": "15分钟", "type": "📄图文"},
            {"title": "时间差计算", "emoji": "⏱️", "duration": "20分钟", "type": "📹视频"},
            {"title": "时间重采样", "emoji": "🔄", "duration": "25分钟", "type": "💻实战"},
            {"title": "移动窗口", "emoji": "🪟", "duration": "20分钟", "type": "📹视频"},
            {"title": "时间序列可视化", "emoji": "📈", "duration": "20分钟", "type": "💻实战"},
        ]
    },
    "module10": {
        "title": "机器学习基础",
        "lessons": [
            {"title": "机器学习概述", "emoji": "🤖", "duration": "25分钟", "type": "📹视频"},
            {"title": "Scikit-learn介绍", "emoji": "🔬", "duration": "20分钟", "type": "📄图文"},
            {"title": "数据预处理", "emoji": "🧹", "duration": "25分钟", "type": "💻实战"},
            {"title": "训练集与测试集", "emoji": "📊", "duration": "20分钟", "type": "📹视频"},
            {"title": "线性回归", "emoji": "📈", "duration": "30分钟", "type": "💻实战"},
            {"title": "逻辑回归", "emoji": "🔄", "duration": "30分钟", "type": "💻实战"},
            {"title": "决策树", "emoji": "🌳", "duration": "25分钟", "type": "📹视频"},
            {"title": "随机森林", "emoji": "🌲", "duration": "25分钟", "type": "💻实战"},
            {"title": "模型评估", "emoji": "✅", "duration": "20分钟", "type": "📹视频"},
            {"title": "模型调优", "emoji": "⚡", "duration": "30分钟", "type": "💻实战"},
        ]
    },
    "module11": {
        "title": "网络爬虫开发",
        "lessons": [
            {"title": "HTTP协议基础", "emoji": "🌐", "duration": "20分钟", "type": "📹视频"},
            {"title": "requests库入门", "emoji": "📡", "duration": "25分钟", "type": "💻实战"},
            {"title": "请求头设置", "emoji": "🔧", "duration": "20分钟", "type": "📄图文"},
            {"title": "HTML解析基础", "emoji": "📄", "duration": "25分钟", "type": "📹视频"},
            {"title": "CSS选择器", "emoji": "🎯", "duration": "20分钟", "type": "💻实战"},
            {"title": "XPath语法", "emoji": "📍", "duration": "25分钟", "type": "📹视频"},
            {"title": "动态网页爬取", "emoji": "⚡", "duration": "30分钟", "type": "💻实战"},
            {"title": "反爬策略应对", "emoji": "🛡️", "duration": "20分钟", "type": "📄图文"},
            {"title": "数据存储与导出", "emoji": "💾", "duration": "20分钟", "type": "💻实战"},
        ]
    },
    "module12": {
        "title": "SQL + Python 数据分析",
        "lessons": [
            {"title": "SQL基础语法", "emoji": "🗄️", "duration": "25分钟", "type": "📹视频"},
            {"title": "数据筛选与排序", "emoji": "🔍", "duration": "20分钟", "type": "💻实战"},
            {"title": "聚合函数", "emoji": "🔢", "duration": "20分钟", "type": "📹视频"},
            {"title": "多表连接", "emoji": "🔗", "duration": "25分钟", "type": "💻实战"},
            {"title": "子查询", "emoji": "📦", "duration": "20分钟", "type": "📹视频"},
            {"title": "SQLite数据库", "emoji": "💾", "duration": "15分钟", "type": "📄图文"},
            {"title": "Python连接数据库", "emoji": "🔗", "duration": "25分钟", "type": "💻实战"},
            {"title": "SQL与Pandas结合", "emoji": "🐼", "duration": "30分钟", "type": "💻实战"},
        ]
    }
}

# 读取原始HTML文件
with open('/workspace/data-analytics-platform/course-center.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 生成新的课程小节HTML
def generate_lesson_html(module_id, lessons):
    module_num = module_id.replace('module', '')
    html = []
    for i, lesson in enumerate(lessons, 1):
        html.append(f'''
                        <a href="course/{module_id}/lesson{i}.html" class="lesson-item" data-module="{module_num}" data-lesson="{i}">
                            <span class="lesson-emoji">{lesson["emoji"]}</span>
                            <span class="lesson-number">{i}</span>
                            <span class="lesson-title">{lesson["title"]}</span>
                            <span class="lesson-meta">
                                <span class="duration">{lesson["duration"]}</span>
                                <span class="lesson-type">{lesson["type"]}</span>
                            </span>
                        </a>
        ''')
    return ''.join(html)

# 更新每个模块的课程列表
for module_id, module_info in courses.items():
    # 找到该模块的lesson-list部分并替换
    pattern = rf'(<!-- 模块[\u4e00-\u9fa5]+：{module_info["title"]} -->.*?<div class="lesson-list">)(.*?)(</div>\s*</div>\s*</div>)'
    replacement = rf'\1{generate_lesson_html(module_id, module_info["lessons"])}\3'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 更新样式部分
new_styles = '''
        .lesson-list {
            padding: 1rem 2rem 2rem;
            border-top: 1px solid #f1f5f9;
            margin-top: 0;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .lesson-item {
            display: flex;
            align-items: center;
            padding: 1rem 1.25rem;
            border-radius: 10px;
            text-decoration: none;
            color: var(--text-primary);
            transition: all 0.2s;
            background: var(--bg-light);
            border: 1px solid #e9ecef;
        }

        .lesson-item:hover {
            background: #e0f2fe;
            transform: translateX(4px);
        }

        .lesson-item.completed {
            background: rgba(16, 185, 129, 0.08);
            opacity: 0.85;
        }

        .lesson-emoji {
            font-size: 1.125rem;
            margin-right: 0.75rem;
        }

        .lesson-number {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 600;
            margin-right: 0.75rem;
            color: var(--primary-color);
            border: 1px solid #e2e8f0;
        }

        .lesson-item.completed .lesson-number {
            background: var(--success-color);
            color: white;
            border-color: var(--success-color);
        }

        .lesson-title {
            flex: 1;
            font-size: 0.95rem;
            font-weight: 500;
        }

        .lesson-item.completed .lesson-title {
            color: #64748b;
        }

        .lesson-meta {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 0.8rem;
            color: var(--text-secondary);
        }

        .duration {
            padding: 0.25rem 0.75rem;
            background: #f1f5f9;
            border-radius: 9999px;
        }

        .lesson-type {
            padding: 0.25rem 0.5rem;
            background: rgba(59, 130, 246, 0.1);
            border-radius: 6px;
        }
'''

# 替换旧样式
content = re.sub(r'\.lesson-list \{.*?\}', new_styles, content, flags=re.DOTALL)

# 写入更新后的文件
with open('/workspace/data-analytics-platform/course-center.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("课程中心页面已更新完成！")