#!/usr/bin/env python3
import requests
import json
import base64
import os
from pathlib import Path

GITHUB_TOKEN = "ghp_DqdLO4kfOhjyA82jJAn9weLOnezKw43EaND"
REPO_OWNER = "tanyachen03"
REPO_NAME = "xinde"
BRANCH = "main"
PROJECT_DIR = "/workspace/data-analytics-platform"

def get_file_sha(filepath):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filepath}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["sha"]
    return None

def update_file(filepath, content, message, sha=None):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filepath}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
    
    data = {
        "message": message,
        "content": encoded_content,
        "branch": BRANCH
    }
    
    if sha:
        data["sha"] = sha
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code in [200, 201]:
        print(f"✓ 上传成功: {filepath}")
        return True
    else:
        print(f"✗ 上传失败 {filepath}: {response.status_code}")
        try:
            print(f"  错误详情: {response.json()}")
        except:
            print(f"  响应: {response.text[:200]}")
        return False

def deploy():
    print("=" * 60)
    print("🚀 开始部署 Python 学习网站到 GitHub Pages")
    print("=" * 60)
    print(f"\n📦 仓库: {REPO_OWNER}/{REPO_NAME}")
    print(f"🌿 分支: {BRANCH}")
    print(f"🌐 目标地址: https://{REPO_OWNER}.github.io/{REPO_NAME}/\n")
    
    success_count = 0
    fail_count = 0
    
    # 主文件列表 - 优先上传
    main_files = [
        "index.html"
    ]
    
    print("📤 步骤 1: 上传核心文件...")
    for filename in main_files:
        filepath = os.path.join(PROJECT_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_sha = get_file_sha(filename)
            message = f"更新 {filename} - Python学习网站完整版本"
            
            if update_file(filename, content, message, file_sha):
                success_count += 1
            else:
                fail_count += 1
        else:
            print(f"✗ 文件不存在: {filename}")
            fail_count += 1
    
    # 静态资源文件
    static_files = [
        "styles.css",
        "script.js"
    ]
    
    print("\n📤 步骤 2: 上传静态资源...")
    for filename in static_files:
        filepath = os.path.join(PROJECT_DIR, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            file_sha = get_file_sha(filename)
            message = f"更新 {filename}"
            
            if update_file(filename, content, message, file_sha):
                success_count += 1
            else:
                fail_count += 1
        else:
            print(f"⚠ 跳过不存在的文件: {filename}")
    
    print("\n" + "=" * 60)
    print("✅ 部署完成!")
    print("=" * 60)
    print(f"✓ 成功: {success_count}")
    if fail_count > 0:
        print(f"✗ 失败: {fail_count}")
    print(f"\n🌐 网站地址: https://{REPO_OWNER}.github.io/{REPO_NAME}/")
    print("💡 提示: 如果页面没有更新，请等待1-2分钟让 GitHub Pages 构建完成")
    print()

if __name__ == "__main__":
    deploy()
