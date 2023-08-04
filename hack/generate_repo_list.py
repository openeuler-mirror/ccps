# 如何使用： 执行命令 ENV_GITEE_ACCESS_TOKEN={your_gitee_access_token} python hack/generate_repo_list.py
import requests
import time
import os

# Gitee组织名称
ORG_NAME = 'ccps'

# Gitee API请求头
## 获取环境变量ENV_GITEE_ACCESS_TOKEN的值
GITEE_ACCESS_TOKEN = os.environ.get('ENV_GITEE_ACCESS_TOKEN')
headers = {
    'Authorization': f'token {GITEE_ACCESS_TOKEN}',
    'Content-Type': 'application/json;charset=UTF-8'
}

# 获取组织所有仓库
def get_all_organization_repos():
    page = 1
    per_page = 100
    all_repos = []

    while True:
        url = f'https://gitee.com/api/v5/orgs/{ORG_NAME}/repos?page={page}&per_page={per_page}'
        response = requests.get(url, headers=headers)
        repos_data = response.json()

        if not repos_data:
            break

        all_repos.extend(repos_data)
        page += 1

    return all_repos

# 获取仓库最新commit的SHA哈希值
def get_latest_commit_sha(repo_name):
    # 防止请求频率过快导致请求终止
    time.sleep(1)
    url = f'https://gitee.com/api/v5/repos/{ORG_NAME}/{repo_name}/commits/master'
    response = requests.get(url, headers=headers)
    return response.json().get('sha')

if __name__ == "__main__":
    repos = get_all_organization_repos()
    repos_name = []
    commit_urls = []
    # 构建Markdown表格
    markdown_table = "# CCPS仓库及最新提交\n| 仓库名称 | 最新一次提交 |\n| -------- | ------------ |\n"
    
    for repo_data in repos:
        repos_name.append(repo_data.get('name'))
    repos_name = sorted(repos_name)

    for repo_name in repos_name:
        latest_commit_sha = get_latest_commit_sha(repo_name)
        commit_url = f'https://gitee.com/{ORG_NAME}/{repo_name}/commit/{latest_commit_sha}'
        markdown_table += f"| {repo_name} | {commit_url} |\n"

    # 将Markdown表格保存在文件中
    with open('repo_list.md', 'w') as file:
        file.write(markdown_table)