# Developer Productivity & Workflow Guide

A practical guide to terminal customization, dotfiles, editor configuration, Git productivity, local environment setup, and debugging techniques.

## Table of Contents

- [Terminal Customization](#terminal-customization)
- [Dotfiles Management](#dotfiles-management)
- [Editor Configuration](#editor-configuration)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Git Aliases & Productivity Shortcuts](#git-aliases--productivity-shortcuts)
- [Local Development Environment Setup](#local-development-environment-setup)
- [Debugging Techniques](#debugging-techniques)

---

## Terminal Customization

A well-configured terminal dramatically speeds up your daily workflow. The two most popular shells for customization are **Zsh** (default on macOS) and **Bash** (default on most Linux distros).

### Shell Configuration Files

| Shell | Config File | Loaded When |
|-------|-------------|-------------|
| Bash  | `~/.bashrc` / `~/.bash_profile` | New shell session |
| Zsh   | `~/.zshrc`  | New Zsh session |

### Oh My Zsh

[Oh My Zsh](https://ohmyz.sh/) is a framework for managing your Zsh configuration with hundreds of plugins and themes.

```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

Enable plugins in `~/.zshrc`:

```zsh
plugins=(git node npm python docker kubectl)
```

### Starship Prompt

[Starship](https://starship.rs/) is a fast, cross-shell prompt that works with Bash, Zsh, Fish, and more.

```bash
# Install via curl
curl -sS https://starship.rs/install.sh | sh

# Add to ~/.zshrc or ~/.bashrc
eval "$(starship init zsh)"
# or for bash:
eval "$(starship init bash)"
```

Configure it in `~/.config/starship.toml`:

```toml
[character]
success_symbol = "[➜](bold green)"
error_symbol = "[✗](bold red)"

[git_branch]
symbol = " "

[nodejs]
symbol = " "

[python]
symbol = " "
```

### Useful Shell Aliases

Add these to your `~/.zshrc` or `~/.bashrc`:

```bash
# Navigation
alias ..='cd ..'
alias ...='cd ../..'
alias ll='ls -lah'
alias la='ls -A'

# Git shortcuts (see full Git aliases section below)
alias gs='git status'
alias gp='git push'

# Development
alias serve='python3 -m http.server 8000'
alias myip='curl ifconfig.me'

# Safety nets
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
```

Reload your shell config without restarting:

```bash
source ~/.zshrc
# or
. ~/.bashrc
```

---

## Dotfiles Management

Dotfiles are configuration files that start with a `.` (e.g., `.zshrc`, `.gitconfig`, `.vimrc`). Versioning them in a Git repository lets you replicate your setup on any machine in minutes.

### What to Version

Common dotfiles worth tracking:

- `~/.zshrc` or `~/.bashrc` — shell config
- `~/.gitconfig` — Git settings and aliases
- `~/.vimrc` or `~/.config/nvim/init.vim` — Vim/Neovim config
- `~/.config/starship.toml` — Starship prompt config
- `~/.tmux.conf` — tmux config
- `~/.ssh/config` — SSH host aliases (never commit private keys)

### Setting Up a Dotfiles Repo

```bash
# Create a bare Git repo to track dotfiles
git init --bare $HOME/.dotfiles

# Create an alias to manage it (add to ~/.zshrc)
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# Hide untracked files so git status isn't noisy
dotfiles config --local status.showUntrackedFiles no

# Add files
dotfiles add ~/.zshrc
dotfiles add ~/.gitconfig
dotfiles commit -m "Initial dotfiles"
dotfiles remote add origin git@github.com:yourusername/dotfiles.git
dotfiles push -u origin main
```

### Restoring on a New Machine

```bash
# Clone the bare repo
git clone --bare git@github.com:yourusername/dotfiles.git $HOME/.dotfiles

# Define the alias temporarily
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# Checkout the files
dotfiles checkout

# If there are conflicts with existing files, back them up first
mkdir -p ~/.dotfiles-backup
dotfiles checkout 2>&1 | grep "\s\+\." | awk {'print $1'} | xargs -I{} mv {} ~/.dotfiles-backup/{}
dotfiles checkout
```

### Symlinking with GNU Stow

[GNU Stow](https://www.gnu.org/software/stow/) is a symlink manager that makes dotfile management cleaner.

```bash
# Install stow
brew install stow        # macOS
sudo apt install stow    # Ubuntu/Debian

# Structure your dotfiles repo like this:
# ~/dotfiles/
#   zsh/
#     .zshrc
#   git/
#     .gitconfig
#   vim/
#     .vimrc

# Symlink a package (run from ~/dotfiles)
stow zsh    # creates ~/.zshrc -> ~/dotfiles/zsh/.zshrc
stow git    # creates ~/.gitconfig -> ~/dotfiles/git/.gitconfig
stow vim    # creates ~/.vimrc -> ~/dotfiles/vim/.vimrc

# Remove symlinks
stow -D zsh
```

---

## Editor Configuration

### VS Code

VS Code stores settings in `settings.json`. Open it with `Cmd+Shift+P` → "Open User Settings (JSON)".

```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.minimap.enabled": false,
  "editor.wordWrap": "on",
  "editor.bracketPairColorization.enabled": true,
  "editor.guides.bracketPairs": true,
  "terminal.integrated.fontSize": 13,
  "files.autoSave": "onFocusChange",
  "workbench.colorTheme": "One Dark Pro",
  "workbench.iconTheme": "material-icon-theme",
  "explorer.confirmDelete": false,
  "git.autofetch": true
}
```

#### Recommended Extensions

| Extension | Purpose |
|-----------|---------|
| Prettier | Code formatting |
| ESLint | JavaScript/TypeScript linting |
| GitLens | Enhanced Git integration |
| GitHub Copilot | AI code completion |
| REST Client | Test HTTP requests in `.http` files |
| Docker | Docker file support |
| Python (ms-python) | Python language support |
| Vim | Vim keybindings in VS Code |

Install extensions from the command line:

```bash
code --install-extension esbenp.prettier-vscode
code --install-extension eamodio.gitlens
code --install-extension ms-python.python
```

Export and restore your extensions:

```bash
# Export
code --list-extensions > extensions.txt

# Restore on a new machine
cat extensions.txt | xargs -L 1 code --install-extension
```

#### Workspace Settings

Per-project settings live in `.vscode/settings.json` at the project root:

```json
{
  "editor.tabSize": 4,
  "python.defaultInterpreterPath": ".venv/bin/python",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```

### Vim Configuration

Vim config lives in `~/.vimrc` (Vim) or `~/.config/nvim/init.vim` (Neovim).

```vim
" Basic settings
set number              " Show line numbers
set relativenumber      " Relative line numbers
set tabstop=2           " Tab width
set shiftwidth=2        " Indent width
set expandtab           " Use spaces instead of tabs
set autoindent          " Auto-indent new lines
set smartindent         " Smart indentation
set hlsearch            " Highlight search results
set incsearch           " Incremental search
set ignorecase          " Case-insensitive search
set smartcase           " Case-sensitive if uppercase used
set wrap                " Wrap long lines
set clipboard=unnamed   " Use system clipboard
set mouse=a             " Enable mouse support
set cursorline          " Highlight current line
set showmatch           " Highlight matching brackets
set wildmenu            " Enhanced command completion
set laststatus=2        " Always show status line
syntax on               " Syntax highlighting
colorscheme desert      " Color scheme

" Leader key
let mapleader = " "

" Quick save and quit
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>x :x<CR>

" Split navigation
nnoremap <C-h> <C-w>h
nnoremap <C-j> <C-w>j
nnoremap <C-k> <C-w>k
nnoremap <C-l> <C-w>l
```

---

## Keyboard Shortcuts

### VS Code Shortcuts

#### Navigation

| Shortcut (Mac) | Shortcut (Win/Linux) | Action |
|----------------|----------------------|--------|
| `Cmd+P` | `Ctrl+P` | Quick open file |
| `Cmd+Shift+P` | `Ctrl+Shift+P` | Command palette |
| `Cmd+B` | `Ctrl+B` | Toggle sidebar |
| `Cmd+J` | `Ctrl+J` | Toggle terminal |
| `Ctrl+Tab` | `Ctrl+Tab` | Switch between open files |
| `Cmd+\` | `Ctrl+\` | Split editor |
| `Cmd+1/2/3` | `Ctrl+1/2/3` | Focus editor group |

#### Editing

| Shortcut (Mac) | Shortcut (Win/Linux) | Action |
|----------------|----------------------|--------|
| `Cmd+D` | `Ctrl+D` | Select next occurrence |
| `Cmd+Shift+L` | `Ctrl+Shift+L` | Select all occurrences |
| `Alt+Up/Down` | `Alt+Up/Down` | Move line up/down |
| `Shift+Alt+Up/Down` | `Shift+Alt+Up/Down` | Duplicate line |
| `Cmd+/` | `Ctrl+/` | Toggle line comment |
| `Cmd+Shift+K` | `Ctrl+Shift+K` | Delete line |
| `Cmd+Enter` | `Ctrl+Enter` | Insert line below |
| `F2` | `F2` | Rename symbol |
| `F12` | `F12` | Go to definition |
| `Shift+F12` | `Shift+F12` | Find all references |

#### Search & Replace

| Shortcut (Mac) | Shortcut (Win/Linux) | Action |
|----------------|----------------------|--------|
| `Cmd+F` | `Ctrl+F` | Find in file |
| `Cmd+H` | `Ctrl+H` | Replace in file |
| `Cmd+Shift+F` | `Ctrl+Shift+F` | Search across files |
| `Cmd+Shift+H` | `Ctrl+Shift+H` | Replace across files |

### Vim Shortcuts

#### Modes

| Key | Action |
|-----|--------|
| `i` | Insert mode (before cursor) |
| `a` | Insert mode (after cursor) |
| `o` | Insert mode (new line below) |
| `O` | Insert mode (new line above) |
| `v` | Visual mode |
| `V` | Visual line mode |
| `Ctrl+v` | Visual block mode |
| `Esc` | Return to Normal mode |

#### Navigation

| Key | Action |
|-----|--------|
| `h/j/k/l` | Left/Down/Up/Right |
| `w` / `b` | Next/previous word |
| `0` / `$` | Start/end of line |
| `gg` / `G` | Top/bottom of file |
| `Ctrl+d` / `Ctrl+u` | Half-page down/up |
| `{` / `}` | Previous/next paragraph |
| `%` | Jump to matching bracket |
| `*` | Search for word under cursor |

#### Editing

| Key | Action |
|-----|--------|
| `dd` | Delete line |
| `yy` | Yank (copy) line |
| `p` / `P` | Paste after/before |
| `u` | Undo |
| `Ctrl+r` | Redo |
| `ciw` | Change inner word |
| `di"` | Delete inside quotes |
| `=G` | Auto-indent to end of file |
| `.` | Repeat last command |

#### Search & Replace

```vim
" Search
/pattern        " Search forward
?pattern        " Search backward
n / N           " Next/previous match

" Replace in file
:%s/old/new/g   " Replace all occurrences
:%s/old/new/gc  " Replace with confirmation

" Replace in selection (visual mode first)
:s/old/new/g
```

---

## Git Aliases & Productivity Shortcuts

Git aliases let you create short commands for frequently used Git operations. Add them to `~/.gitconfig` under `[alias]` or use `git config --global`.

### Setting Up Aliases

```bash
# Method 1: via git config command
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch

# Method 2: edit ~/.gitconfig directly
```

Add this block to your `~/.gitconfig`:

```ini
[alias]
    # Shortcuts
    st = status
    co = checkout
    br = branch
    ci = commit
    cp = cherry-pick
    rb = rebase

    # Logging
    lg = log --oneline --graph --decorate --all
    ll = log --oneline -20
    last = log -1 HEAD --stat

    # Branching
    new = checkout -b
    del = branch -d
    gone = "!git fetch -p && git branch -vv | grep ': gone]' | awk '{print $1}' | xargs git branch -d"

    # Staging
    unstage = reset HEAD --
    discard = checkout --
    aa = add --all
    ap = add --patch

    # Committing
    amend = commit --amend --no-edit
    fixup = commit --fixup
    wip = "!git add -A && git commit -m 'WIP'"

    # Stashing
    save = stash push -m
    pop = stash pop
    ls-stash = stash list

    # Diffing
    df = diff
    dfs = diff --staged
    dc = diff --cached

    # Remote
    pf = push --force-with-lease
    pu = "!git push -u origin $(git rev-parse --abbrev-ref HEAD)"
    sync = "!git fetch origin && git rebase origin/main"

    # Utilities
    aliases = config --get-regexp alias
    root = rev-parse --show-toplevel
    contributors = shortlog --summary --numbered --email
    cleanup = "!git branch --merged | grep -v '\\*\\|main\\|master\\|develop' | xargs -n 1 git branch -d"
```

### Usage Examples

```bash
# Quick status
git st

# Create and switch to a new branch
git new feature/my-feature

# Stage all changes and commit
git aa && git ci -m "feat: add new feature"

# Amend last commit without changing the message
git amend

# Push current branch to origin (sets upstream automatically)
git pu

# View a pretty log graph
git lg

# Delete all local branches that have been merged and deleted on remote
git gone

# Clean up merged local branches
git cleanup

# Save work in progress
git wip

# Sync with main branch via rebase
git sync

# Force push safely (won't overwrite others' work)
git pf

# See who contributed most
git contributors
```

---

## Local Development Environment Setup

### Package Managers

#### macOS — Homebrew

```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Common installs
brew install git node python3 wget curl jq

# Install GUI apps (casks)
brew install --cask visual-studio-code docker iterm2

# Update everything
brew update && brew upgrade

# Search for a package
brew search postgres

# See what's installed
brew list
```

#### Ubuntu/Debian — apt

```bash
# Update package list
sudo apt update && sudo apt upgrade -y

# Install common tools
sudo apt install -y git curl wget build-essential

# Add a PPA (third-party repo)
sudo add-apt-repository ppa:deadsnakes/python3.12
sudo apt update
sudo apt install python3.12
```

#### Windows — Chocolatey

```powershell
# Install Chocolatey (run as Administrator)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install packages
choco install git nodejs python vscode -y

# Update all packages
choco upgrade all -y
```

### Version Managers

Version managers let you install and switch between multiple versions of a language runtime — essential when working on projects with different requirements.

#### nvm — Node Version Manager

```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# Reload shell config
source ~/.zshrc

# Install a specific Node version
nvm install 20
nvm install 18
nvm install --lts   # Install latest LTS

# Switch versions
nvm use 20
nvm use 18

# Set a default version
nvm alias default 20

# List installed versions
nvm ls

# Use the version specified in .nvmrc
nvm use

# Create a .nvmrc file for your project
echo "20" > .nvmrc
```

#### pyenv — Python Version Manager

```bash
# Install pyenv (macOS/Linux)
curl https://pyenv.run | bash

# Add to ~/.zshrc or ~/.bashrc
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# Reload shell
source ~/.zshrc

# Install a Python version
pyenv install 3.12.0
pyenv install 3.11.5

# Set global default
pyenv global 3.12.0

# Set local version for a project (creates .python-version file)
pyenv local 3.11.5

# List available versions
pyenv install --list | grep "3\."

# List installed versions
pyenv versions
```

#### Virtual Environments (Python)

Always use a virtual environment per project to isolate dependencies:

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate       # macOS/Linux
.venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Deactivate
deactivate

# With pyenv + virtualenv plugin
pyenv virtualenv 3.12.0 my-project-env
pyenv activate my-project-env
```

### Environment Variables

#### .env Files

Store environment-specific config in a `.env` file at the project root. Never commit this file — add it to `.gitignore`.

```bash
# .env
DATABASE_URL=postgres://user:password@localhost:5432/mydb
API_KEY=your_secret_api_key_here
NODE_ENV=development
PORT=3000
DEBUG=true
```

```bash
# .gitignore
.env
.env.local
.env.*.local
```

Load `.env` in different environments:

```bash
# Bash — load manually
export $(grep -v '^#' .env | xargs)

# Node.js — use dotenv package
npm install dotenv
```

```javascript
// At the top of your entry file
require('dotenv').config();
console.log(process.env.DATABASE_URL);
```

```python
# Python — use python-dotenv
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv("DATABASE_URL")
```

#### export (Temporary Variables)

```bash
# Set for current session only
export MY_VAR="hello"

# Verify it's set
echo $MY_VAR
printenv MY_VAR

# Unset a variable
unset MY_VAR
```

#### direnv — Per-Directory Environment Variables

[direnv](https://direnv.net/) automatically loads/unloads environment variables when you enter/leave a directory.

```bash
# Install
brew install direnv          # macOS
sudo apt install direnv      # Ubuntu

# Add to ~/.zshrc
eval "$(direnv hook zsh)"
# or for bash:
eval "$(direnv hook bash)"

# Create a .envrc file in your project
echo 'export DATABASE_URL="postgres://localhost/mydb"' > .envrc
echo 'export NODE_ENV=development' >> .envrc

# Allow direnv to load it (required once per file change)
direnv allow

# Variables are now automatically set when you cd into the directory
# and unset when you leave
```

---

## Debugging Techniques

### Browser DevTools

Chrome and Firefox DevTools are your primary tools for frontend debugging.

#### Opening DevTools

```
F12                    # Open DevTools
Cmd+Option+I (Mac)     # Open DevTools
Ctrl+Shift+I (Win/Linux)
Cmd+Option+J (Mac)     # Open Console directly
```

#### JavaScript Breakpoints

Set breakpoints directly in the Sources panel, or use `debugger` in your code:

```javascript
function calculateTotal(items) {
  let total = 0;
  for (const item of items) {
    debugger; // Execution pauses here when DevTools is open
    total += item.price * item.quantity;
  }
  return total;
}
```

When paused at a breakpoint you can:
- **Step Over** (`F10`) — execute the current line and move to the next
- **Step Into** (`F11`) — step into a function call
- **Step Out** (`Shift+F11`) — finish the current function and return to the caller
- **Resume** (`F8`) — continue execution until the next breakpoint

#### Console Tricks

```javascript
// Log with labels
console.log('user:', user);
console.table(arrayOfObjects);   // Renders as a table
console.group('API Response');
console.log(response.status);
console.log(response.data);
console.groupEnd();

// Measure performance
console.time('fetchUsers');
await fetchUsers();
console.timeEnd('fetchUsers');   // Prints: fetchUsers: 123.45ms

// Assert conditions
console.assert(user.id > 0, 'User ID must be positive', user);
```

#### Network Tab

The Network tab lets you inspect every HTTP request your page makes:

1. Open DevTools → Network tab
2. Reload the page to capture all requests
3. Filter by type: XHR/Fetch for API calls, JS, CSS, Img
4. Click a request to see Headers, Payload, Response, Timing
5. Right-click a request → "Copy as cURL" to replay it in the terminal

```bash
# Replaying a captured request in the terminal
curl 'https://api.example.com/users' \
  -H 'Authorization: Bearer eyJhbGc...' \
  -H 'Content-Type: application/json'
```

#### Inspecting and Modifying the DOM

```javascript
// In the Console, $ is an alias for document.querySelector
$('h1').textContent = 'Modified!';
$$('p')                          // Returns all <p> elements (like querySelectorAll)

// Monitor events on an element
monitorEvents($('#submit-btn'), 'click');
unmonitorEvents($('#submit-btn'));
```

---

### Node.js Debugging

#### Using the --inspect Flag

```bash
# Start Node.js with the inspector enabled
node --inspect server.js

# Break on the first line (useful for short scripts)
node --inspect-brk script.js

# Specify a custom port
node --inspect=9229 server.js
```

Open `chrome://inspect` in Chrome, click "Open dedicated DevTools for Node", and you get the full Chrome DevTools experience for your Node process — breakpoints, call stack, memory profiling, and more.

#### Debugging with VS Code

Create a `.vscode/launch.json` in your project:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Launch Program",
      "skipFiles": ["<node_internals>/**"],
      "program": "${workspaceFolder}/src/index.js"
    },
    {
      "type": "node",
      "request": "attach",
      "name": "Attach to Process",
      "port": 9229,
      "skipFiles": ["<node_internals>/**"]
    }
  ]
}
```

For a running server, use the "Attach" configuration. Start your server with `--inspect`, then press `F5` in VS Code to attach.

#### Debugging npm Scripts

```json
// package.json
{
  "scripts": {
    "start": "node src/index.js",
    "debug": "node --inspect-brk src/index.js"
  }
}
```

```bash
npm run debug
# Then attach VS Code or open chrome://inspect
```

#### Logging Best Practices

```javascript
// Use the debug package for conditional logging
const debug = require('debug')('app:server');

debug('Server starting on port %d', port);

// Enable in terminal:
// DEBUG=app:* node server.js
// DEBUG=app:server node server.js
```

---

### Python Debugging

#### pdb — Python Debugger

`pdb` is Python's built-in interactive debugger. Drop it anywhere in your code:

```python
import pdb

def process_data(data):
    result = []
    for item in data:
        pdb.set_trace()  # Execution pauses here
        processed = transform(item)
        result.append(processed)
    return result
```

#### breakpoint() — Python 3.7+

`breakpoint()` is the modern, cleaner way to drop into the debugger:

```python
def calculate_discount(price, discount_pct):
    breakpoint()  # Opens pdb at this line
    discount = price * (discount_pct / 100)
    final_price = price - discount
    return final_price
```

#### pdb Commands

Once inside the debugger:

| Command | Action |
|---------|--------|
| `n` | Next line (step over) |
| `s` | Step into function |
| `r` | Return from current function |
| `c` | Continue to next breakpoint |
| `q` | Quit debugger |
| `p expr` | Print expression value |
| `pp expr` | Pretty-print expression |
| `l` | List source code around current line |
| `w` | Print call stack (where) |
| `b 42` | Set breakpoint at line 42 |
| `cl` | Clear all breakpoints |

```bash
# Example session
> /path/to/script.py(8)calculate_discount()
-> discount = price * (discount_pct / 100)
(Pdb) p price
99.99
(Pdb) p discount_pct
0   # Bug found! discount_pct is 0, not 10
(Pdb) c
```

#### Disable breakpoint() in Production

```bash
# Set this environment variable to disable all breakpoint() calls
export PYTHONBREAKPOINT=0
```

#### Debugging with VS Code

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Django",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "--noreload"],
      "django": true,
      "justMyCode": true
    },
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["main:app", "--reload"],
      "justMyCode": true
    }
  ]
}
```

Set breakpoints by clicking the gutter (left of line numbers) in VS Code, then press `F5` to start debugging. The Variables panel shows all local and global variables, and the Debug Console lets you evaluate expressions at the current breakpoint.

#### ipdb — Enhanced pdb

`ipdb` integrates IPython's interface into pdb for syntax highlighting and tab completion:

```bash
pip install ipdb
```

```python
import ipdb

def my_function(data):
    ipdb.set_trace()  # Drop into ipdb instead of pdb
    return process(data)
```

---

## Additional Resources

- [Oh My Zsh Documentation](https://github.com/ohmyzsh/ohmyzsh/wiki)
- [Starship Configuration Reference](https://starship.rs/config/)
- [GNU Stow Manual](https://www.gnu.org/software/stow/manual/stow.html)
- [nvm Repository](https://github.com/nvm-sh/nvm)
- [pyenv Repository](https://github.com/pyenv/pyenv)
- [direnv Documentation](https://direnv.net/)
- [VS Code Debugging Docs](https://code.visualstudio.com/docs/editor/debugging)
- [Python pdb Documentation](https://docs.python.org/3/library/pdb.html)
- [Chrome DevTools Reference](https://developer.chrome.com/docs/devtools/)
