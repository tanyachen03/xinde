#!/usr/bin/env python3
import os

courses = {
    "module5": {
        "title": "Pandas核心操作",
        "subtitle": "数据分析必备",
        "lessons": [
            {"title": "Pandas简介与安装", "desc": "数据分析利器Pandas概述", "code": "import pandas as pd\nprint('Pandas版本:', pd.__version__)"},
            {"title": "Series数据结构", "desc": "一维数组对象的创建与操作", "code": "import pandas as pd\ns = pd.Series([1, 2, 3, 4, 5])\nprint(s)"},
            {"title": "DataFrame入门", "desc": "二维表格数据结构", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df)"},
            {"title": "读取CSV数据", "desc": "pd.read_csv参数详解", "code": "# 读取CSV文件\nimport pandas as pd\n# df = pd.read_csv('data.csv')\nprint('CSV读取示例')"},
            {"title": "数据基本信息", "desc": "head、info、describe方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})\nprint(df.head())\nprint(df.info())\nprint(df.describe())"},
            {"title": "列操作", "desc": "选择、添加、删除列", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1,2], 'B': [3,4]})\nprint(df['A'])\ndf['C'] = [5,6]\nprint(df)"},
            {"title": "行选择与切片", "desc": "iloc位置索引", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})\nprint(df.iloc[0])\nprint(df.iloc[0:2])"},
            {"title": "loc标签索引", "desc": "基于标签的选择方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1,2], 'B': [3,4]}, index=['x', 'y'])\nprint(df.loc['x'])"},
            {"title": "布尔索引筛选", "desc": "条件筛选数据", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})\nprint(df[df['A'] > 1])"},
            {"title": "排序与排名", "desc": "sort_values、rank方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [3,1,2], 'B': [6,4,5]})\nprint(df.sort_values('A'))"}
        ]
    },
    "module6": {
        "title": "数据清洗实战",
        "subtitle": "工作必备",
        "lessons": [
            {"title": "缺失值检测", "desc": "isnull、notnull方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})\nprint(df.isnull())"},
            {"title": "缺失值处理策略", "desc": "删除、填充、插值方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, None, 3]})\ndf_filled = df.fillna(0)\nprint(df_filled)"},
            {"title": "重复值处理", "desc": "duplicated、drop_duplicates", "code": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 1, 2]})\nprint(df.duplicated())\nprint(df.drop_duplicates())"},
            {"title": "异常值识别", "desc": "IQR方法识别离群值", "code": "import pandas as pd\nimport numpy as np\ndf = pd.DataFrame({'A': [1, 2, 3, 100]})\nQ1 = df['A'].quantile(0.25)\nQ3 = df['A'].quantile(0.75)\nIQR = Q3 - Q1\nprint((df['A'] < Q1 - 1.5 * IQR) | (df['A'] > Q3 + 1.5 * IQR))"},
            {"title": "数据类型转换", "desc": "astype、to_numeric方法", "code": "import pandas as pd\ndf = pd.DataFrame({'A': ['1', '2', '3']})\ndf['A'] = df['A'].astype(int)\nprint(df.dtypes)"},
            {"title": "字符串清洗", "desc": "strip、replace、split方法", "code": "import pandas as pd\ns = pd.Series(['  hello  ', 'world'])\nprint(s.str.strip())\nprint(s.str.replace('l', 'x'))"},
            {"title": "正则表达式", "desc": "str.contains、str.extract", "code": "import pandas as pd\ns = pd.Series(['abc123', 'def456', 'ghi'])\nprint(s.str.contains(r'\\d'))\nprint(s.str.extract(r'(\\d+)'))"},
            {"title": "日期时间处理", "desc": "pd.to_datetime详解", "code": "import pandas as pd\ndates = pd.Series(['2024-01-01', '2024-01-02'])\ndt = pd.to_datetime(dates)\nprint(dt)\nprint(dt.dt.year)"},
            {"title": "数据清洗综合实战", "desc": "完整案例实操", "code": "import pandas as pd\n# 综合实战示例\ndf = pd.DataFrame({\n    'date': ['2024-01-01', '2024-01-02', None],\n    'value': ['100', '200', 'abc']\n})\ndf['date'] = pd.to_datetime(df['date'])\ndf['value'] = pd.to_numeric(df['value'], errors='coerce')\nprint(df)"},
        ]
    },
    "module7": {
        "title": "数据可视化",
        "subtitle": "图表展示",
        "lessons": [
            {"title": "Matplotlib基础", "desc": "figure、axes对象", "code": "import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\nax.plot([1, 2, 3], [4, 5, 6])\nplt.show()"},
            {"title": "折线图", "desc": "plot方法与样式设置", "code": "import matplotlib.pyplot as plt\nimport numpy as np\nx = np.linspace(0, 10, 100)\ny = np.sin(x)\nplt.plot(x, y, color='red', linestyle='--')\nplt.show()"},
            {"title": "柱状图", "desc": "bar、barh水平柱状图", "code": "import matplotlib.pyplot as plt\nx = ['A', 'B', 'C']\ny = [10, 20, 15]\nplt.bar(x, y, color='skyblue')\nplt.barh(x, y)  # 水平柱状图\nplt.show()"},
            {"title": "直方图与密度图", "desc": "hist、kde分布图", "code": "import matplotlib.pyplot as plt\nimport numpy as np\ndata = np.random.randn(1000)\nplt.hist(data, bins=30, alpha=0.5)\nplt.show()"},
            {"title": "饼图", "desc": "pie方法与标签设置", "code": "import matplotlib.pyplot as plt\nlabels = ['A', 'B', 'C', 'D']\nsizes = [15, 30, 45, 10]\nplt.pie(sizes, labels=labels, autopct='%1.1f%%')\nplt.show()"},
            {"title": "散点图", "desc": "scatter相关关系展示", "code": "import matplotlib.pyplot as plt\nimport numpy as np\nx = np.random.rand(50)\ny = np.random.rand(50)\nsizes = np.random.rand(50) * 100\nplt.scatter(x, y, s=sizes, alpha=0.5)\nplt.show()"},
            {"title": "图表美化", "desc": "标题、标签、图例设置", "code": "import matplotlib.pyplot as plt\nplt.plot([1,2,3], [4,5,6])\nplt.title('My Plot')\nplt.xlabel('X Axis')\nplt.ylabel('Y Axis')\nplt.legend(['Line 1'])\nplt.grid(True)\nplt.show()"},
            {"title": "Pandas绘图", "desc": "DataFrame.plot方法", "code": "import pandas as pd\nimport matplotlib.pyplot as plt\ndf = pd.DataFrame({'A': [1,2,3], 'B': [4,5,6]})\ndf.plot(kind='bar')\nplt.show()"},
        ]
    },
    "module8": {
        "title": "分组聚合分析",
        "subtitle": "数据汇总",
        "lessons": [
            {"title": "groupby基础", "desc": "分组操作原理", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Category': ['A', 'A', 'B'],\n    'Value': [10, 20, 30]\n})\ngrouped = df.groupby('Category')\nprint(grouped.sum())"},
            {"title": "聚合函数", "desc": "sum、mean、count等", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Category': ['A', 'A', 'B'],\n    'Value': [10, 20, 30]\n})\nprint(df.groupby('Category').sum())\nprint(df.groupby('Category').mean())"},
            {"title": "多列分组", "desc": "多层次分组统计", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Year': [2023, 2023, 2024],\n    'Category': ['A', 'B', 'A'],\n    'Value': [10, 20, 30]\n})\nprint(df.groupby(['Year', 'Category']).sum())"},
            {"title": "agg聚合方法", "desc": "自定义聚合函数", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Category': ['A', 'A', 'B'],\n    'Value': [10, 20, 30]\n})\nprint(df.groupby('Category').agg(['sum', 'mean', 'max']))"},
            {"title": "transform方法", "desc": "分组内数据转换", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Category': ['A', 'A', 'B'],\n    'Value': [10, 20, 30]\n})\ndf['Mean'] = df.groupby('Category')['Value'].transform('mean')\nprint(df)"},
            {"title": "透视表", "desc": "pivot_table多维度分析", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Year': [2023, 2023, 2024],\n    'Category': ['A', 'B', 'A'],\n    'Value': [10, 20, 30]\n})\nprint(pd.pivot_table(df, values='Value', index='Year', columns='Category', aggfunc='sum'))"},
            {"title": "交叉表", "desc": "crosstab列联表分析", "code": "import pandas as pd\ndf = pd.DataFrame({\n    'Gender': ['M', 'F', 'M', 'F'],\n    'Status': ['Active', 'Active', 'Inactive', 'Active']\n})\nprint(pd.crosstab(df['Gender'], df['Status']))"},
        ]
    },
    "module9": {
        "title": "时间序列入门",
        "subtitle": "时序分析",
        "lessons": [
            {"title": "时间格式转换", "desc": "字符串转时间对象", "code": "import pandas as pd\ndates = pd.Series(['2024-01-01', '2024-01-02'])\ndt = pd.to_datetime(dates)\nprint(dt)"},
            {"title": "DatetimeIndex", "desc": "时间索引设置", "code": "import pandas as pd\ndates = pd.date_range('2024-01-01', periods=5)\ndf = pd.DataFrame({'Value': [1,2,3,4,5]}, index=dates)\nprint(df)"},
            {"title": "时间提取", "desc": "年、月、日、时、分、秒提取", "code": "import pandas as pd\ndates = pd.date_range('2024-01-01', periods=3, freq='H')\nprint(dates.year)\nprint(dates.month)\nprint(dates.day)"},
            {"title": "时间差计算", "desc": "timedelta时间间隔", "code": "import pandas as pd\nfrom datetime import timedelta\nd1 = pd.to_datetime('2024-01-01')\nd2 = pd.to_datetime('2024-01-10')\ndiff = d2 - d1\nprint(diff)\nprint(d1 + timedelta(days=7))"},
            {"title": "时间重采样", "desc": "resample降采样与升采样", "code": "import pandas as pd\ndates = pd.date_range('2024-01-01', periods=30, freq='D')\ndf = pd.DataFrame({'Value': range(30)}, index=dates)\nprint(df.resample('W').sum())"},
            {"title": "移动窗口", "desc": "rolling移动平均", "code": "import pandas as pd\ndf = pd.DataFrame({'Value': [1,2,3,4,5,6,7,8,9,10]})\nprint(df.rolling(window=3).mean())"},
            {"title": "时间序列可视化", "desc": "时序数据图表展示", "code": "import pandas as pd\nimport matplotlib.pyplot as plt\ndates = pd.date_range('2024-01-01', periods=30, freq='D')\ndf = pd.DataFrame({'Value': range(30)}, index=dates)\ndf.plot()\nplt.show()"},
        ]
    },
    "module10": {
        "title": "机器学习基础",
        "subtitle": "AI入门",
        "lessons": [
            {"title": "机器学习概述", "desc": "监督学习与无监督学习", "code": "# 机器学习类型介绍\nprint('监督学习：分类、回归')\nprint('无监督学习：聚类、降维')\nprint('强化学习：决策优化')"},
            {"title": "Scikit-learn介绍", "desc": "ML库安装与基本用法", "code": "# 安装scikit-learn\n# pip install scikit-learn\nfrom sklearn import datasets\niris = datasets.load_iris()\nprint('特征数:', iris.data.shape)\nprint('标签数:', iris.target.shape)"},
            {"title": "数据预处理", "desc": "标准化、归一化", "code": "from sklearn.preprocessing import StandardScaler, MinMaxScaler\nimport numpy as np\nX = np.array([[1, 2], [3, 4], [5, 6]])\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)\nprint(X_scaled)"},
            {"title": "训练集与测试集", "desc": "train_test_split划分", "code": "from sklearn.model_selection import train_test_split\nimport numpy as np\nX = np.random.rand(100, 5)\ny = np.random.randint(0, 2, 100)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\nprint('训练集:', X_train.shape)\nprint('测试集:', X_test.shape)"},
            {"title": "线性回归", "desc": "LinearRegression模型", "code": "from sklearn.linear_model import LinearRegression\nimport numpy as np\nX = np.array([[1], [2], [3], [4], [5]])\ny = np.array([2, 4, 5, 4, 5])\nmodel = LinearRegression()\nmodel.fit(X, y)\nprint('系数:', model.coef_)\nprint('截距:', model.intercept_)"},
            {"title": "逻辑回归", "desc": "分类问题入门", "code": "from sklearn.linear_model import LogisticRegression\nimport numpy as np\nX = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])\ny = np.array([0, 0, 1, 1])\nmodel = LogisticRegression()\nmodel.fit(X, y)\nprint('预测:', model.predict([[4, 5]]))"},
            {"title": "决策树", "desc": "分类与回归树", "code": "from sklearn.tree import DecisionTreeClassifier\nfrom sklearn.datasets import load_iris\niris = load_iris()\nmodel = DecisionTreeClassifier()\nmodel.fit(iris.data, iris.target)\nprint('特征重要性:', model.feature_importances_)"},
            {"title": "随机森林", "desc": "集成学习方法", "code": "from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.datasets import load_iris\niris = load_iris()\nmodel = RandomForestClassifier(n_estimators=100)\nmodel.fit(iris.data, iris.target)\nprint('准确率:', model.score(iris.data, iris.target))"},
            {"title": "模型评估", "desc": "准确率、召回率、F1分数", "code": "from sklearn.metrics import accuracy_score, recall_score, f1_score\ny_true = [0, 1, 0, 1, 0, 1]\ny_pred = [0, 1, 1, 1, 0, 0]\nprint('准确率:', accuracy_score(y_true, y_pred))\nprint('召回率:', recall_score(y_true, y_pred))\nprint('F1:', f1_score(y_true, y_pred))"},
            {"title": "模型调优", "desc": "GridSearchCV超参数搜索", "code": "from sklearn.model_selection import GridSearchCV\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.datasets import load_iris\niris = load_iris()\nmodel = DecisionTreeClassifier()\nparams = {'max_depth': [2, 3, 4], 'min_samples_split': [2, 3]}\ngrid = GridSearchCV(model, params, cv=3)\ngrid.fit(iris.data, iris.target)\nprint('最佳参数:', grid.best_params_)"},
        ]
    },
    "module11": {
        "title": "网络爬虫开发",
        "subtitle": "数据采集",
        "lessons": [
            {"title": "HTTP协议基础", "desc": "请求与响应原理", "code": "# HTTP协议基础\nprint('HTTP方法: GET, POST, PUT, DELETE')\nprint('状态码: 200成功, 404未找到, 500服务器错误')"},
            {"title": "requests库入门", "desc": "发送HTTP请求", "code": "import requests\nresponse = requests.get('https://httpbin.org/get')\nprint('状态码:', response.status_code)\nprint('响应内容:', response.text[:200])"},
            {"title": "请求头设置", "desc": "模拟浏览器访问", "code": "import requests\nheaders = {\n    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'\n}\nresponse = requests.get('https://httpbin.org/headers', headers=headers)\nprint(response.json())"},
            {"title": "HTML解析基础", "desc": "BeautifulSoup入门", "code": "from bs4 import BeautifulSoup\nhtml = '<html><body><h1>Hello</h1></body></html>'\nsoup = BeautifulSoup(html, 'html.parser')\nprint(soup.h1.text)"},
            {"title": "CSS选择器", "desc": "定位页面元素", "code": "from bs4 import BeautifulSoup\nhtml = '<div class=\"content\"><p>Text</p><p>More</p></div>'\nsoup = BeautifulSoup(html, 'html.parser')\nprint(soup.select('.content p'))"},
            {"title": "XPath语法", "desc": "路径表达式定位", "code": "from lxml import etree\nhtml = '<html><body><div id=\"main\"><h1>Hello</h1></div></body></html>'\ntree = etree.HTML(html)\nprint(tree.xpath('//div[@id=\"main\"]/h1/text()'))"},
            {"title": "动态网页爬取", "desc": "Selenium浏览器自动化", "code": "# 需要安装 selenium\n# pip install selenium\nfrom selenium import webdriver\n# driver = webdriver.Chrome()\n# driver.get('https://example.com')\nprint('Selenium动态爬取')"},
            {"title": "反爬策略应对", "desc": "代理IP、请求间隔", "code": "import requests\nimport time\nproxies = {\n    'http': 'http://proxy:port',\n    'https': 'https://proxy:port'\n}\ntime.sleep(1)  # 请求间隔\nresponse = requests.get('https://httpbin.org/ip')\nprint(response.json())"},
            {"title": "数据存储与导出", "desc": "CSV、Excel文件保存", "code": "import pandas as pd\ndata = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}\ndf = pd.DataFrame(data)\ndf.to_csv('output.csv', index=False)\ndf.to_excel('output.xlsx', index=False)\nprint('数据已保存')"},
        ]
    },
    "module12": {
        "title": "SQL + Python 数据分析",
        "subtitle": "数据库技能",
        "lessons": [
            {"title": "SQL基础语法", "desc": "SELECT、FROM、WHERE子句", "code": "# SQL基础查询\n# SELECT column1, column2 FROM table WHERE condition;\nprint('SELECT name, age FROM users WHERE age > 18;')"},
            {"title": "数据筛选与排序", "desc": "ORDER BY、LIMIT、IN操作符", "code": "# SQL筛选与排序\n# SELECT * FROM table ORDER BY column DESC LIMIT 10;\nprint('SELECT * FROM orders WHERE status IN (\"completed\", \"pending\") ORDER BY create_time DESC;')"},
            {"title": "聚合函数", "desc": "COUNT、SUM、AVG、GROUP BY", "code": "# SQL聚合函数\n# SELECT category, COUNT(*), SUM(price) FROM products GROUP BY category;\nprint('SELECT department, AVG(salary) FROM employees GROUP BY department;')"},
            {"title": "多表连接", "desc": "JOIN、LEFT JOIN、RIGHT JOIN", "code": "# SQL表连接\n# SELECT * FROM orders JOIN customers ON orders.customer_id = customers.id;\nprint('SELECT o.id, c.name FROM orders o LEFT JOIN customers c ON o.customer_id = c.id;')"},
            {"title": "子查询", "desc": "嵌套查询与相关子查询", "code": "# SQL子查询\n# SELECT name FROM products WHERE price > (SELECT AVG(price) FROM products);\nprint('SELECT name FROM customers WHERE id IN (SELECT customer_id FROM orders);')"},
            {"title": "SQLite数据库", "desc": "轻量级数据库操作", "code": "import sqlite3\nconn = sqlite3.connect('example.db')\ncursor = conn.cursor()\ncursor.execute('CREATE TABLE IF NOT EXISTS users (id INT, name TEXT)')\nconn.commit()\nconn.close()\nprint('数据库创建成功')"},
            {"title": "Python连接数据库", "desc": "sqlite3库使用", "code": "import sqlite3\nconn = sqlite3.connect('example.db')\ncursor = conn.cursor()\ncursor.execute('INSERT INTO users VALUES (1, \"Alice\")')\nconn.commit()\ncursor.execute('SELECT * FROM users')\nprint(cursor.fetchall())\nconn.close()"},
            {"title": "SQL与Pandas结合", "desc": "读取数据库数据到DataFrame", "code": "import pandas as pd\nimport sqlite3\nconn = sqlite3.connect('example.db')\ndf = pd.read_sql('SELECT * FROM users', conn)\nprint(df)\nconn.close()"},
        ]
    }
}

def generate_lesson_html(module_name, lesson_num, lesson_data, total_lessons, module_info):
    module_num = module_name.replace('module', '')
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson_data['title']} - 数析学院</title>
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
.ec{{background:white;border-radius:12px;overflow:hidden;border:1px solid #e2e8f0;margin:1.5rem 0}}
.etb{{background:#f8fafc;padding:12px 16px;border-bottom:1px solid #e2e8f0;display:flex;gap:10px}}
.etb button{{padding:8px 16px;border:none;border-radius:6px;font-size:14px;font-weight:500;cursor:pointer}}
.br{{background:#22c55e;color:white}}
.bz{{background:#f1f5f9;color:#475569}}
.CodeMirror{{height:300px!important;font-size:14px}}
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
<div class="st">模块{module_num}：{module_info['title']}</div>
'''
    
    for i, lesson in enumerate(module_info['lessons'], 1):
        active_class = ' active' if i == lesson_num else ''
        html += f'<a href="lesson{i}.html" class="lni{active_class}"><span class="nn">{i}</span><span class="nt">{lesson["title"]}</span></a>'
    
    html += f'''</div>
</aside>
<main class="mc">
<div class="lh">
<div class="lm"><span class="mt">{module_info['subtitle']}</span></div>
<h1>{lesson_data['title']}</h1>
<p>{lesson_data['desc']}</p>
</div>
<div class="se">
<h2>学习目标</h2>
<ul>
<li>理解{lesson_data['title']}的核心概念</li>
<li>掌握相关的代码实现方法</li>
<li>能够在实际项目中应用所学知识</li>
</ul>
</div>
<div class="se">
<h2>知识点讲解</h2>
<p>{lesson_data['desc']}。本节将详细介绍相关概念和实用技巧。</p>
</div>
<div class="tb"><div class="tt">小贴士</div><p>多动手实践，遇到问题多查看官方文档。</p></div>
<div class="se">
<h2>代码示例</h2>
<p>在下方编辑器中尝试运行代码：</p>
</div>
<div class="ec">
<div class="etb">
<button class="br" onclick="runCode()"><i class="fas fa-play"></i> 运行</button>
<button class="bz" onclick="resetCode()"><i class="fas fa-undo"></i> 重置</button>
<span id="status" style="margin-left:auto;color:#64748b;font-size:14px;">环境加载中...</span>
</div>
<div id="code-editor"></div>
<div class="oa"><pre id="output"></pre></div>
</div>
<div class="eb"><div class="et">常见错误</div><p>注意代码缩进，确保Python语法正确。</p></div>
<div style="margin-top:2rem;padding-top:2rem;border-top:2px solid #f1f5f9;">
<button class="cb" id="completeBtn" onclick="markComplete()"><i class="fas fa-check-circle"></i><span id="btnText">标记为已完成</span></button>
</div>
</main>
</div>
<script>
let editor, pyodide;
function initEditor(){{
editor=CodeMirror(document.getElementById('code-editor'),{{mode:'python',theme:'monokai',lineNumbers:true,tabSize:4,value:{repr(lesson_data['code'])} }});
}}
async function initPyodide(){{
try{{pyodide=await loadPyodide();document.getElementById('status').textContent='环境就绪'}}catch(e){{document.getElementById('status').textContent='加载失败'}}}}
async function runCode(){{
if(!pyodide){{document.getElementById('output').textContent='环境加载中...';return}}
const code=editor.getValue();
document.getElementById('output').textContent='运行中...';
try{{
pyodide.runPython("import sys;from io import StringIO;sys.stdout=StringIO()");
await pyodide.runPythonAsync(code);
const out=pyodide.runPython("sys.stdout.getvalue()");
document.getElementById('output').textContent=out||'（无输出）';
}}catch(e){{document.getElementById('output').textContent='错误: '+e}}}}
function resetCode(){{editor.setValue({repr(lesson_data['code'])});document.getElementById('output').textContent=''}}
function markComplete(){{
const progress=JSON.parse(localStorage.getItem('module-{module_num}-progress')||'[]');
if(!progress.includes({lesson_num})){{
progress.push({lesson_num});
localStorage.setItem('module-{module_num}-progress',JSON.stringify(progress));
}}
const b=document.getElementById('completeBtn');
b.innerHTML='<i class="fas fa-check-circle"></i> 已完成';
b.disabled=true}}
document.addEventListener('DOMContentLoaded',function(){{
initEditor();initPyodide();
const progress=JSON.parse(localStorage.getItem('module-{module_num}-progress')||'[]');
if(progress.includes({lesson_num})){{const b=document.getElementById('completeBtn');b.innerHTML='<i class="fas fa-check-circle"></i> 已完成';b.disabled=true}}}});
</script>
</body>
</html>'''
    return html

for module_name, module_info in courses.items():
    module_path = f"/workspace/data-analytics-platform/course/{module_name}"
    for i, lesson in enumerate(module_info['lessons'], 1):
        lesson_path = os.path.join(module_path, f"lesson{i}.html")
        html = generate_lesson_html(module_name, i, lesson, len(module_info['lessons']), module_info)
        with open(lesson_path, 'w', encoding='utf-8') as f:
            f.write(html)
    print(f"Generated {len(module_info['lessons'])} lessons for {module_name}")

print("All courses generated successfully!")