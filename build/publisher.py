import os
from github import Github

token = os.environ['TOKEN']
git = Github(token)
git_user = git.get_user()

back_repo  = git_user.get_repo('log')
front_repo = git_user.get_repo('g0pher98.github.io')

issues = back_repo.get_issues()

print("Hello")
