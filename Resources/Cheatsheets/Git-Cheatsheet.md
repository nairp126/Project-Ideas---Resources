# 🐙 Git Cheatsheet for Students

A quick reference guide for the most essential Git commands.

---

## 🏁 Setup & Configuration

### `git config`

Sets configuration values for your username, email, etc.

```bash
# Set your username
git config --global user.name "Your Name"

# Set your email
git config --global user.email "youremail@example.com"
```

### `git init`

Initializes a new Git repository in the current directory.

```bash
git init
```

### `git clone`

Creates a copy of a remote repository on your local machine.

```bash
git clone https://github.com/username/repository.git
```

---

## 💾 Saving Changes (Staging & Committing)

### `git status`

Displays the state of the working directory and staging area. Shows which files are modified or untracked.

```bash
git status
```

### `git add`

Adds files to the staging area to be included in the next commit.

```bash
# Add a specific file
git add filename.txt

# Add all changed files
git add .
```

### `git commit`

Captures a snapshot of the project's currently staged changes.

```bash
# Commit with a message
git commit -m "fix: corrected typo in README"
```

---

## 🌿 Branching & Merging

### `git branch`

Lists, creates, or deletes branches.

```bash
# List all branches
git branch

# Create a new branch
git branch feature-login

# Delete a branch
git branch -d feature-login
```

### `git checkout`

Switches branches or restores working tree files.

```bash
# Switch to an existing branch
git checkout feature-login

# Create and switch to a new branch (shortcut)
git checkout -b feature-login
```

### `git merge`

Joins two or more development histories together. Merges the specified branch *into* the current branch.

```bash
# Merge 'feature-login' into the current branch (e.g., main)
git merge feature-login
```

---

## ☁️ Syncing with Remote

### `git remote add`

Connects a local repository to a remote server.

```bash
git remote add origin https://github.com/username/repository.git
```

### `git push`

Uploads local branch commits to the remote repository.

```bash
# Push changes to the 'main' branch of 'origin'
git push origin main
```

### `git pull`

Fetches changes from the remote repository and immediately merges them into the current branch.

```bash
git pull origin main
```

### `git fetch`

Downloads objects and refs from another repository but doesn't merge them.

```bash
git fetch origin
```

---

## ⏪ Undoing Changes

### `git log`

Shows the commit logs.

```bash
git log
```

### `git reset`

Resets current HEAD to the specified state.

```bash
# Unstage a file (keep changes in working directory)
git reset HEAD filename.txt
```

### `git restore`

Restore working tree files.

```bash
# Discard changes in a specific file
git restore filename.txt
```

---

## 🚫 Ignoring Files (.gitignore)

Create a file named `.gitignore` to list files Git should ignore (like build artifacts, keys, etc.).

```text
# Example .gitignore content
node_modules/
.env
*.log
.DS_Store
```
