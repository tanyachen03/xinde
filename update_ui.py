import os
import re

STYLES_PATH = '/workspace/data-analytics-platform/styles.css'
PROJECTS_PATH = '/workspace/data-analytics-platform/projects.html'
COURSE_DIR = '/workspace/data-analytics-platform/course'

def update_styles():
    with open(STYLES_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('#3b82f6', '#4F46E5')
    content = content.replace('#2563eb', '#4338CA')
    content = content.replace('#60a5fa', '#818CF8')

    content = content.replace(
        '--primary-color: #4F46E5;',
        '--primary-color: #4F46E5;\n    --primary-light: #818CF8;\n    --primary-dark: #4338CA;'
    )

    with open(STYLES_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print('styles.css 已更新')

def update_projects_page():
    with open(PROJECTS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    old_header = '''<div class="projects-page-container">
            <div class="projects-filter">'''

    new_header = '''<div class="projects-page-container">
            <div class="social-proof-banner">
                <span class="banner-icon">🎉</span>
                <span class="banner-text">已有 <strong>500+</strong> 学员完成实战项目</span>
            </div>
            <div class="projects-filter">'''

    content = content.replace(old_header, new_header)

    social_proof_css = '''
    .social-proof-banner {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        padding: 1rem 2rem;
        background: linear-gradient(135deg, rgba(79, 70, 229, 0.08), rgba(129, 140, 248, 0.08));
        border: 1px solid rgba(79, 70, 229, 0.15);
        border-radius: 12px;
        margin-bottom: 2rem;
        font-size: 1rem;
        color: #4F46E5;
    }

    .social-proof-banner .banner-icon {
        font-size: 1.5rem;
    }

    .social-proof-banner .banner-text strong {
        font-weight: 700;
        color: #4F46E5;
    }

    @media (max-width: 768px) {
        .social-proof-banner {
            flex-direction: column;
            text-align: center;
            padding: 1rem;
        }
    }
    '''

    content = content.replace('.projects-filter {', social_proof_css + '\n.projects-filter {')

    with open(PROJECTS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    print('projects.html 已更新')

def update_course_cards():
    for module in ['module2', 'module3', 'module4']:
        if module == 'module4':
            lesson_num = 5
        else:
            lesson_num = 7

        lesson_path = os.path.join(COURSE_DIR, module, f'lesson{lesson_num}.html')

        if not os.path.exists(lesson_path):
            continue

        with open(lesson_path, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.replace('立即开始', '🚀 免费开始实战')

        with open(lesson_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f'{lesson_path} 已更新')

def main():
    print('开始更新 UI 设计...')
    update_styles()
    update_projects_page()
    update_course_cards()
    print('更新完成！')

if __name__ == '__main__':
    main()