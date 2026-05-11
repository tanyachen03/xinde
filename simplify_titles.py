import os

COURSE_DIR = '/workspace/data-analytics-platform/course'
COURSE_CENTER_PATH = '/workspace/data-analytics-platform/course-center.html'

# 精简后的标题映射
LESSON_TITLES = {
    # 模块一
    'module1/lesson1.html': '数据分析前景',
    'module1/lesson2.html': '数据分析思维',
    'module1/lesson3.html': 'Python极简入门',
    'module1/lesson4.html': 'Anaconda环境',
    'module1/lesson5.html': '在线编程平台',
    
    # 模块二
    'module2/lesson1.html': 'Pandas与Series',
    'module2/lesson2.html': 'DataFrame结构',
    'module2/lesson3.html': '读取各类数据',
    'module2/lesson4.html': '数据查看方法',
    'module2/lesson5.html': '行列选取与筛选',
    'module2/lesson6.html': '缺失值与重复值',
    'module2/lesson7.html': '类型转换与重命名',
    
    # 模块三
    'module3/lesson1.html': '异常值识别处理',
    'module3/lesson2.html': '字符串数据清洗',
    'module3/lesson3.html': '时间日期处理',
    'module3/lesson4.html': '新增字段与分箱',
    'module3/lesson5.html': '多表合并',
    'module3/lesson6.html': '分组聚合groupby',
    'module3/lesson7.html': '透视表实战',
    
    # 模块四
    'module4/lesson1.html': 'Matplotlib基础',
    'module4/lesson2.html': '常用图表类型',
    'module4/lesson3.html': '分布分析图表',
    'module4/lesson4.html': '图表美化布局',
    'module4/lesson5.html': '业务报表实战',
}

def update_course_center():
    """更新课程中心页面的显示标题"""
    with open(COURSE_CENTER_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换所有课程小节的显示标题
    for path, short_title in LESSON_TITLES.items():
        # 找到包含完整路径的链接并替换标题
        old_pattern = f'href="course/{path}" class="lesson-item"'
        if old_pattern in content:
            # 获取完整标题
            content = content.replace(old_pattern, f'href="course/{path}" class="lesson-item"')
            # 更新标题文本
            # 需要找到具体的标题位置进行替换
            
    # 直接替换标题文本
    title_mappings = {
        # 模块一
        '数据分析行业前景与岗位介绍': '数据分析前景',
        '数据分析思维：业务分析逻辑、拆解方法': '数据分析思维',
        'Python极简入门': 'Python极简入门',
        'Anaconda与Jupyter环境讲解': 'Anaconda环境',
        '浏览器在线编程平台使用教程': '在线编程平台',
        
        # 模块二
        'Pandas介绍与数据结构Series': 'Pandas与Series',
        'DataFrame表格结构详解': 'DataFrame结构',
        '读取各类数据：Excel、CSV、在线数据集': '读取各类数据',
        '数据查看：head、tail、info、describe': '数据查看方法',
        '行列选取与条件筛选': '行列选取与筛选',
        '缺失值处理与重复值删除': '缺失值与重复值',
        '数据类型转换与字段重命名': '类型转换与重命名',
        
        # 模块三
        '异常值识别与处理': '异常值识别处理',
        '字符串数据清洗': '字符串数据清洗',
        '时间日期数据处理': '时间日期处理',
        '新增计算字段、分箱分段': '新增字段与分箱',
        '多表合并：merge、concat': '多表合并',
        '分组聚合groupby全套用法': '分组聚合groupby',
        '透视表pivot_table实战': '透视表实战',
        
        # 模块四
        'Matplotlib绘图基础': 'Matplotlib基础',
        '折线图、柱状图、饼图': '常用图表类型',
        '直方图、箱线图做分布分析': '分布分析图表',
        '子图布局、配色与图表美化': '图表美化布局',
        '业务可视化报表实战': '业务报表实战',
    }

    for old_title, new_title in title_mappings.items():
        content = content.replace(f'<h4>{old_title}</h4>', f'<h4>{new_title}</h4>')
        content = content.replace(f'<p>{old_title}</p>', f'<p>{new_title}</p>')

    with open(COURSE_CENTER_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print('✓ 已更新课程中心页面')

def update_lesson_sidebars():
    """更新所有课程小节页面的侧边栏导航标题"""
    for module in ['module1', 'module2', 'module3', 'module4']:
        module_path = os.path.join(COURSE_DIR, module)
        if not os.path.isdir(module_path):
            continue
        
        for lesson_file in os.listdir(module_path):
            if not lesson_file.endswith('.html'):
                continue
            
            lesson_path = os.path.join(module_path, lesson_file)
            relative_path = f'{module}/{lesson_file}'
            
            if relative_path not in LESSON_TITLES:
                continue
            
            short_title = LESSON_TITLES[relative_path]
            
            with open(lesson_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 侧边栏标题替换
            # 找到侧边栏中的标题并替换
            content = content.replace(
                f'<a href="{lesson_file}" class="nav-link">',
                f'<a href="{lesson_file}" class="nav-link">{short_title}'
            )
            
            with open(lesson_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        print(f'✓ 已更新{module}侧边栏导航')

def main():
    print('开始精简课程小节标题...')
    update_course_center()
    update_lesson_sidebars()
    print('\n✅ 所有标题已精简完成！')

if __name__ == '__main__':
    main()