#!/usr/bin/env python3
import os

# 课程1：Python简介与环境准备
lesson1_content = """
Python是一种高级编程语言，以其简洁的语法和强大的功能而闻名。它被广泛应用于数据分析、人工智能、Web开发等领域。Python的设计哲学强调代码的可读性，使用缩进来组织代码块，这使得Python代码非常易于理解和维护。

为什么选择Python进行数据分析呢？首先，Python拥有丰富的数据处理库，如NumPy、Pandas、Matplotlib等，这些库为数据分析提供了强大的支持。其次，Python的语法简洁，学习曲线相对平缓，非常适合初学者入门。此外，Python拥有庞大的社区支持，遇到问题时可以很容易找到解决方案。

Anaconda是一个用于数据科学的Python发行版，它包含了常用的数据科学库和工具。安装Anaconda可以省去手动安装各个库的麻烦。安装完成后，我们可以通过Anaconda Navigator来管理环境和启动Jupyter Notebook。
"""

lesson1_code1 = '''# 检查Python版本
import sys
print('Python版本:', sys.version)
print('欢迎来到Python数据分析之旅！')'''

lesson1_code2 = '''# 打印Python的特点
features = ['简单易学', '代码可读性强', '丰富的库支持', '跨平台', '社区活跃']
for i, feature in enumerate(features, 1):
    print(f'{i}. {feature}')'''

# 课程2：Jupyter Notebook使用
lesson2_content = """
Jupyter Notebook是一个交互式的编程环境，它允许你在浏览器中编写和运行代码，同时可以添加文字说明、公式和图表。这使得Jupyter Notebook成为数据探索和报告生成的理想工具。

Jupyter Notebook的界面由多个单元格组成，每个单元格可以包含代码、Markdown文字或原始文本。代码单元格可以独立运行，运行结果会显示在单元格下方。这种交互式的方式非常适合数据探索和教学演示。

常用的快捷键包括：Shift+Enter运行当前单元格并移动到下一个，Ctrl+Enter仅运行当前单元格，Esc进入命令模式，Enter进入编辑模式。熟练使用快捷键可以大大提高工作效率。
"""

lesson2_code1 = '''# 第一个Jupyter Notebook代码
print('Hello, Jupyter!')'''

lesson2_code2 = '''# 在Notebook中进行简单计算
radius = 5
area = 3.14159 * radius ** 2
print(f'半径为{radius}的圆面积是: {area:.2f}')'''

# 课程3：基本语法与数据输出
lesson3_content = """
print()函数是Python中最常用的函数之一，用于向控制台输出信息。它可以输出字符串、数字、变量等各种类型的数据。print()函数还支持格式化输出，可以通过多种方式控制输出格式。

注释是代码中非常重要的一部分，它用于解释代码的功能和逻辑。Python中有两种注释方式：单行注释以#开头，多行注释用三个单引号或双引号包裹。良好的注释习惯可以提高代码的可读性和可维护性。

Python使用缩进来组织代码块，这是Python语法的一个重要特点。通常使用4个空格或1个制表符作为缩进。正确的缩进对于代码的执行至关重要。
"""

lesson3_code1 = '''# 基本的print用法
print('Hello, World!')
print(123)
print(3.14)
print(True)'''

lesson3_code2 = '''# 格式化输出
name = '小明'
age = 25
score = 95.5
print(f'{name}今年{age}岁，考试成绩{score}分')
print('{}今年{}岁，考试成绩{}分'.format(name, age, score))'''

# 课程4：变量定义与命名规范
lesson4_content = """
变量是程序中存储数据的容器。在Python中，变量不需要声明类型，直接赋值即可创建。变量名可以包含字母、数字和下划线，但不能以数字开头，也不能使用Python的关键字。

Python的命名规范建议使用蛇形命名法(snake_case)，即单词之间用下划线连接，全部使用小写字母。常量通常使用全大写字母，单词之间用下划线连接。

Python中有多种数据类型，包括整数(int)、浮点数(float)、字符串(str)、布尔值(bool)等。理解这些基本数据类型是学习Python的基础。
"""

lesson4_code1 = '''# 变量定义与赋值
name = '张三'
age = 30
height = 1.75
is_student = False
print(name, age, height, is_student)'''

lesson4_code2 = '''# 变量类型检查
x = 10
y = 'hello'
z = 3.14
print(f'x的类型: {type(x)}')
print(f'y的类型: {type(y)}')
print(f'z的类型: {type(z)}')'''

# 课程5：数字运算与表达式
lesson5_content = """
Python支持丰富的数学运算，包括基本的算术运算（加、减、乘、除）、幂运算、取模运算等。算术运算符的优先级遵循数学中的运算规则，可以使用括号改变运算顺序。

比较运算符用于比较两个值的大小关系，返回布尔值True或False。常见的比较运算符包括等于(==)、不等于(!=)、大于(>)、小于(<)、大于等于(>=)、小于等于(<=)。

逻辑运算符用于组合多个条件表达式，包括and（与）、or（或）、not（非）。逻辑运算在条件判断中非常常用。
"""

lesson5_code1 = '''# 算术运算
a = 10
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')'''

lesson5_code2 = '''# 比较运算和逻辑运算
x = 15
result1 = x > 10 and x < 20
result2 = x < 5 or x > 25
result3 = not (x == 10)
print(f'x在10到20之间: {result1}')
print(f'x小于5或大于25: {result2}')
print(f'x不等于10: {result3}')'''

# 课程6：初学者常见误区
lesson6_content = """
初学者在学习Python时常常会遇到一些常见问题。其中最常见的是编码问题，特别是在处理中文时。Python 3默认使用UTF-8编码，但如果文件中包含特殊字符，可能会出现编码错误。

缩进问题也是初学者经常遇到的问题。Python使用缩进来区分代码块，缩进不一致会导致SyntaxError。建议使用4个空格作为缩进，不要混用空格和制表符。

调试是编程中必不可少的技能。print()函数是最简单的调试工具，可以用来查看变量的值。此外，学会阅读错误信息也是非常重要的，错误信息通常会指出问题所在的位置和原因。
"""

lesson6_code1 = '''# 调试技巧：使用print查看变量
def calculate_area(radius):
    print(f'计算半径为{radius}的圆面积')
    area = 3.14159 * radius ** 2
    print(f'计算结果: {area}')
    return area

calculate_area(5)'''

lesson6_code2 = '''# 常见错误示例
# 注意：以下代码故意包含错误用于演示

# 错误1：缩进不一致
# def greet(name):
#     print(f'Hello, {name}')
#      print('Welcome!')  # 这里缩进错误

# 错误2：中英文符号混用
# print("你好")  # 注意引号是中文的

# 正确写法示例
def greet(name):
    print(f'Hello, {name}')
    print('Welcome!')

greet('Python')'''

lessons = [
    {
        "lesson_num": 1,
        "title": "Python简介与环境准备",
        "subtitle": "了解Python特点，安装Anaconda开发环境",
        "objectives": ["了解Python的特点和应用领域", "安装Anaconda开发环境", "验证Python安装是否成功"],
        "content": lesson1_content.strip(),
        "code1": lesson1_code1,
        "code2": lesson1_code2,
        "question": "为什么Python是数据分析的首选语言？请列举至少三个理由。",
        "tip": "建议安装Anaconda而不是单独安装Python，这样可以避免很多依赖问题。"
    },
    {
        "lesson_num": 2,
        "title": "Jupyter Notebook使用",
        "subtitle": "掌握在线笔记本的基本操作和快捷键",
        "objectives": ["理解Jupyter Notebook的概念", "掌握基本操作和快捷键", "创建和运行代码单元格"],
        "content": lesson2_content.strip(),
        "code1": lesson2_code1,
        "code2": lesson2_code2,
        "question": "在Jupyter Notebook中，如何将一个代码单元格转换为Markdown单元格？",
        "tip": "使用Shift+Enter快捷键运行单元格比点击工具栏按钮更快捷高效。"
    },
    {
        "lesson_num": 3,
        "title": "基本语法与数据输出",
        "subtitle": "print函数、注释、代码结构基础",
        "objectives": ["掌握print函数的使用", "理解注释的重要性", "了解Python代码结构"],
        "content": lesson3_content.strip(),
        "code1": lesson3_code1,
        "code2": lesson3_code2,
        "question": "为什么Python代码需要缩进？缩进在Python中有什么作用？",
        "tip": "使用#进行注释时，注释内容应简洁明了，避免过多的冗余注释。"
    },
    {
        "lesson_num": 4,
        "title": "变量定义与命名规范",
        "subtitle": "变量赋值、命名规则、常见数据类型",
        "objectives": ["学会定义和使用变量", "掌握Python的命名规范", "了解常见数据类型"],
        "content": lesson4_content.strip(),
        "code1": lesson4_code1,
        "code2": lesson4_code2,
        "question": "变量名'1name'和'name'有什么区别？为什么？",
        "tip": "变量名应具有描述性，能够清晰表达变量的用途，避免使用无意义的变量名如'a'、'b'等。"
    },
    {
        "lesson_num": 5,
        "title": "数字运算与表达式",
        "subtitle": "算术运算、比较运算、逻辑运算",
        "objectives": ["掌握基本算术运算符", "理解比较运算的返回值", "学会使用逻辑运算符"],
        "content": lesson5_content.strip(),
        "code1": lesson5_code1,
        "code2": lesson5_code2,
        "question": "表达式'10 < x < 20'和'x > 10 and x < 20'有什么关系？",
        "tip": "在复杂表达式中使用括号可以提高代码可读性，避免因运算符优先级造成的错误。"
    },
    {
        "lesson_num": 6,
        "title": "初学者常见误区",
        "subtitle": "编码格式、缩进、调试技巧",
        "objectives": ["了解常见的编码问题", "掌握正确的缩进方式", "学会基本的调试技巧"],
        "content": lesson6_content.strip(),
        "code1": lesson6_code1,
        "code2": lesson6_code2,
        "question": "当Python程序出现错误时，应该如何定位和解决问题？",
        "tip": "养成良好的代码习惯，使用IDE（如VS Code）可以自动检测缩进和语法错误，提高编程效率。"
    }
]

def escape_js_string(s):
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('"', '\\"')
    return s

def generate_lesson(lesson):
    lesson_num = lesson["lesson_num"]
    
    objectives_html = ''.join([f'<li>{obj}</li>' for obj in lesson["objectives"]])
    code1_escaped = escape_js_string(lesson["code1"])
    code2_escaped = escape_js_string(lesson["code2"])
    
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson["title"]} - 数析学院</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/theme/monokai.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.13/mode/python/python.min.js"></script>
<script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--p:#3b82f6;--b:#f8fafc;--w:#fff}}
body{{font-family:-apple-system,sans-serif;background:var(--b);color:#1e293b;line-height:1.7}}
.n{{position:fixed;top:0;left:0;right:0;background:var(--w);box-shadow:0 2px 8px rgba(0,0,0,.08);z-index:100}}
.nc{{max-width:1400px;margin:0 auto;padding:0 2rem;display:flex;align-items:center;justify-content:space-between;height:60px}}
.nl{{display:flex;align-items:center;gap:.5rem;font-size:1.25rem;font-weight:700;color:var(--p);text-decoration:none}}
.bl{{color:#64748b;text-decoration:none;font-size:.9rem}}
.lc{{display:grid;grid-template-columns:260px 1fr;gap:2rem;max-width:1400px;margin:80px auto 2rem;padding:0 2rem}}
.s{{position:sticky;top:80px;height:fit-content}}
.sc{{background:var(--w);border-radius:12px;padding:1.5rem;box-shadow:0 4px 12px rgba(0,0,0,.08)}}
.st{{font-size:.9rem;font-weight:600;color:#64748b;margin-bottom:1rem}}
.lni{{display:flex;align-items:center;padding:.75rem;border-radius:8px;text-decoration:none;color:#1e293b;font-size:.9rem;margin-bottom:.5rem;transition:all .2s}}
.lni:hover{{background:#f1f5f9}}
.lni.active{{background:#eff6ff;color:var(--p);font-weight:600}}
.nn{{width:24px;height:24px;border-radius:50%;background:#e2e8f0;display:flex;align-items:center;justify-content:center;font-size:.75rem;margin-right:.75rem}}
.nt{{flex:1}}
.mc{{background:var(--w);border-radius:12px;padding:2rem;box-shadow:0 4px 12px rgba(0,0,0,.08)}}
.lh{{border-bottom:2px solid #f1f5f9;padding-bottom:1.5rem;margin-bottom:2rem}}
.lm{{display:flex;gap:1rem;margin-bottom:.75rem}}
.mt{{padding:.25rem .75rem;border-radius:9999px;font-size:.8rem;font-weight:600;background:#eff6ff;color:var(--p)}}
.lh h1{{font-size:1.75rem;font-weight:700;color:#1e293b;margin-bottom:.5rem}}
.lh p{{color:#64748b;font-size:1rem}}
.se{{margin-bottom:2rem}}
.se h2{{font-size:1.25rem;font-weight:700;color:#1e293b;margin-bottom:1rem;padding-bottom:.5rem;border-bottom:2px solid #e2e8f0}}
.se p{{color:#475569;margin-bottom:1rem}}
.se ul{{padding-left:1.5rem;color:#475569;margin-bottom:1rem}}
.se li{{margin-bottom:.5rem}}
.tb{{background:#eff6ff;border-left:4px solid var(--p);padding:1rem;border-radius:8px;margin:1rem 0}}
.tt{{font-weight:600;color:var(--p);margin-bottom:.5rem}}
.eb{{background:#fef2f2;border-left:4px solid #ef4444;padding:1rem;border-radius:8px;margin:1rem 0}}
.et{{font-weight:600;color:#ef4444;margin-bottom:.5rem}}
.qb{{background:#f0fdf4;border-left:4px solid #22c55e;padding:1rem;border-radius:8px;margin:1rem 0}}
.qt{{font-weight:600;color:#22c55e;margin-bottom:.5rem}}
.ec{{background:white;border-radius:12px;overflow:hidden;border:1px solid #e2e8f0;margin:1.5rem 0}}
.etb{{background:#f8fafc;padding:12px 16px;border-bottom:1px solid #e2e8f0;display:flex;gap:10px}}
.etb button{{padding:8px 16px;border:none;border-radius:6px;font-size:14px;font-weight:500;cursor:pointer}}
.br{{background:#22c55e;color:white}}
.bz{{background:#f1f5f9;color:#475569}}
.CodeMirror{{height:250px!important;font-size:14px}}
.oa{{background:#0f172a;padding:16px}}
.oa pre{{margin:0;color:#e2e8f0;font-family:monospace;font-size:14px}}
.cb{{display:inline-flex;align-items:center;gap:.5rem;padding:.75rem 1.5rem;background:linear-gradient(135deg,#10b981,#06b6d4);color:white;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer}}
@media(max-width:1024px){{.lc{{grid-template-columns:1fr}}.s{{position:static}}}}
</style>
</head>
<body>
<header class="n">
<div class="nc">
<a href="../../course-center.html" class="bl"><i class="fas fa-arrow-left"></i> 返回课程中心</a>
<a href="../../index.html" class="nl"><i class="fas fa-chart-bar"></i> 数析学院</a>
</div>
</header>
<div class="lc">
<aside class="s">
<div class="sc">
<div class="st">模块一：Python快速入门</div>
<a href="lesson1.html" class="lni {'active' if lesson_num == 1 else ''}"><span class="nn">1</span><span class="nt">Python简介与环境准备</span></a>
<a href="lesson2.html" class="lni {'active' if lesson_num == 2 else ''}"><span class="nn">2</span><span class="nt">Jupyter Notebook使用</span></a>
<a href="lesson3.html" class="lni {'active' if lesson_num == 3 else ''}"><span class="nn">3</span><span class="nt">基本语法与数据输出</span></a>
<a href="lesson4.html" class="lni {'active' if lesson_num == 4 else ''}"><span class="nn">4</span><span class="nt">变量定义与命名规范</span></a>
<a href="lesson5.html" class="lni {'active' if lesson_num == 5 else ''}"><span class="nn">5</span><span class="nt">数字运算与表达式</span></a>
<a href="lesson6.html" class="lni {'active' if lesson_num == 6 else ''}"><span class="nn">6</span><span class="nt">初学者常见误区</span></a>
</div>
</aside>
<main class="mc">
<div class="lh">
<div class="lm"><span class="mt">入门必学</span></div>
<h1>{lesson["title"]}</h1>
<p>{lesson["subtitle"]}</p>
</div>
<div class="se">
<h2>学习目标</h2>
<ul>
{objectives_html}
</ul>
</div>
<div class="se">
<h2>知识点讲解</h2>
<p>{lesson["content"]}</p>
</div>
<div class="se">
<h2>代码示例一</h2>
<p>尝试运行以下代码，观察输出结果：</p>
<div class="ec">
<div class="etb">
<button class="br" onclick="runCode1()"><i class="fas fa-play"></i> 运行</button>
<button class="bz" onclick="resetCode1()"><i class="fas fa-undo"></i> 重置</button>
<span id="status1" style="margin-left:auto;color:#64748b;font-size:14px;">环境加载中...</span>
</div>
<div id="code-editor1"></div>
<div class="oa"><pre id="output1"></pre></div>
</div>
</div>
<div class="se">
<h2>代码示例二</h2>
<p>尝试运行以下代码，观察输出结果：</p>
<div class="ec">
<div class="etb">
<button class="br" onclick="runCode2()"><i class="fas fa-play"></i> 运行</button>
<button class="bz" onclick="resetCode2()"><i class="fas fa-undo"></i> 重置</button>
<span id="status2" style="margin-left:auto;color:#64748b;font-size:14px;">环境加载中...</span>
</div>
<div id="code-editor2"></div>
<div class="oa"><pre id="output2"></pre></div>
</div>
</div>
<div class="qb"><div class="qt">💡 互动思考</div><p>{lesson["question"]}</p></div>
<div class="tb"><div class="tt">💫 小贴士</div><p>{lesson["tip"]}</p></div>
<div style="margin-top:2rem;padding-top:2rem;border-top:2px solid #f1f5f9;">
<button class="cb" id="completeBtn" onclick="markComplete()"><i class="fas fa-check-circle"></i><span id="btnText">标记为已完成</span></button>
</div>
</main>
</div>
<script>
let editor1, editor2, pyodide;
const code1 = '{code1_escaped}';
const code2 = '{code2_escaped}';

function initEditor(){{
editor1 = CodeMirror(document.getElementById('code-editor1'), {{mode:'python',theme:'monokai',lineNumbers:true,tabSize:4,value:code1}});
editor2 = CodeMirror(document.getElementById('code-editor2'), {{mode:'python',theme:'monokai',lineNumbers:true,tabSize:4,value:code2}});
}}

async function initPyodide(){{
try{{
pyodide = await loadPyodide();
document.getElementById('status1').textContent = '环境就绪';
document.getElementById('status2').textContent = '环境就绪';
}} catch(e) {{
document.getElementById('status1').textContent = '加载失败';
document.getElementById('status2').textContent = '加载失败';
}}
}}

async function runCode(code, outputId){{
if(!pyodide){{
document.getElementById(outputId).textContent = '环境加载中...';
return;
}}
document.getElementById(outputId).textContent = '运行中...';
try{{
pyodide.runPython("import sys;from io import StringIO;sys.stdout=StringIO()");
await pyodide.runPythonAsync(code);
const out = pyodide.runPython("sys.stdout.getvalue()");
document.getElementById(outputId).textContent = out || '（无输出）';
}} catch(e) {{
document.getElementById(outputId).textContent = '错误: ' + e;
}}
}}

function runCode1(){{ runCode(editor1.getValue(), 'output1'); }}
function runCode2(){{ runCode(editor2.getValue(), 'output2'); }}
function resetCode1(){{ editor1.setValue(code1); document.getElementById('output1').textContent = ''; }}
function resetCode2(){{ editor2.setValue(code2); document.getElementById('output2').textContent = ''; }}

function markComplete(){{
const progress = JSON.parse(localStorage.getItem('module-1-progress') || '[]');
if(!progress.includes({lesson_num})){{
progress.push({lesson_num});
localStorage.setItem('module-1-progress', JSON.stringify(progress));
}}
const b = document.getElementById('completeBtn');
b.innerHTML = '<i class=\"fas fa-check-circle\"></i> 已完成';
b.disabled = true;
}}

document.addEventListener('DOMContentLoaded', function(){{
initEditor();
initPyodide();
const progress = JSON.parse(localStorage.getItem('module-1-progress') || '[]');
if(progress.includes({lesson_num})){{
const b = document.getElementById('completeBtn');
b.innerHTML = '<i class=\"fas fa-check-circle\"></i> 已完成';
b.disabled = true;
}}
}});
</script>
</body>
</html>'''
    return html

module_path = "/workspace/data-analytics-platform/course/module1"
for lesson in lessons:
    lesson_path = os.path.join(module_path, f"lesson{lesson['lesson_num']}.html")
    html = generate_lesson(lesson)
    with open(lesson_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated lesson{lesson['lesson_num']}.html")

print("Module 1 lessons generated successfully!")