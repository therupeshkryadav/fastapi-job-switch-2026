# Git Essential Commands Guide

## 1. Check Current Status
Shows changed, staged, and untracked files.

git status


## 2. Add Files to Staging Area

Add specific file:
git add filename.py

Add entire folder:
git add folder-name/

Add everything in current directory:
git add .


## 3. Commit Changes
Creates a snapshot of staged files.

git commit -m "Write meaningful commit message"


## 4. Push to Remote Repository
Uploads local commits to GitHub.

git push


## 5. Pull Latest Changes
Downloads latest changes from remote.

git pull


## 6. View Commit History

git log

Compact version:
git log --oneline


## 7. Check Differences Before Commit

See changes not staged:
git diff

See staged changes:
git diff --staged


## 8. Remove File from Staging

git reset filename.py


## 9. Remove Tracked File (Keep in Local)

git rm --cached filename.py


## 10. Create New Branch

git branch branch-name

Switch to branch:
git checkout branch-name

Create and switch:
git checkout -b branch-name


## 11. Merge Branch

git checkout main
git merge branch-name


## 12. Clone Repository

git clone repository-url


---

# Professional Workflow Example

1. git status
2. git add specific-file.py
3. git diff --staged
4. git commit -m "Clear message"
5. git push

Always check before pushing.
Never blindly use git add .
