# Linux/Bash Cheatsheet

A quick reference for essential Linux commands and Bash scripting.

## Table of Contents
- [Navigation & File System](#navigation--file-system)
- [File Operations](#file-operations)
- [Permissions & Ownership](#permissions--ownership)
- [Process Management](#process-management)
- [Text Processing](#text-processing)
- [Networking](#networking)
- [Bash Scripting](#bash-scripting)
- [Environment & Variables](#environment--variables)

---

## Navigation & File System

Move around the filesystem and inspect directory contents.

```bash
# Print working directory
pwd

# List files (long format, hidden files)
ls -la

# Change directory
cd /path/to/dir
cd ~          # home directory
cd -          # previous directory

# Show directory tree
tree -L 2

# Find files by name
find /path -name "*.log"

# Find files modified in the last 7 days
find . -mtime -7
```

---

## File Operations

Create, copy, move, and delete files and directories.

```bash
# Create a file
touch file.txt

# Create directories (including parents)
mkdir -p parent/child/grandchild

# Copy file
cp source.txt dest.txt

# Copy directory recursively
cp -r src_dir/ dest_dir/

# Move / rename
mv old_name.txt new_name.txt

# Remove file
rm file.txt

# Remove directory recursively (use with caution)
rm -rf dir/

# View file contents
cat file.txt
less file.txt     # paginated view
head -20 file.txt # first 20 lines
tail -20 file.txt # last 20 lines
tail -f app.log   # follow live output

# Create a symbolic link
ln -s /path/to/target link_name

# Show disk usage
du -sh *
df -h
```

---

## Permissions & Ownership

Control who can read, write, and execute files.

```bash
# View permissions
ls -l file.txt
# Output: -rwxr-xr-- 1 user group 1234 Jan 1 12:00 file.txt

# Change permissions (numeric)
chmod 755 script.sh   # rwxr-xr-x
chmod 644 file.txt    # rw-r--r--

# Change permissions (symbolic)
chmod +x script.sh    # add execute for all
chmod u+w file.txt    # add write for owner
chmod o-r file.txt    # remove read for others

# Change owner
chown user:group file.txt
chown -R user:group dir/

# Run command as superuser
sudo command
```

---

## Process Management

Monitor and control running processes.

```bash
# List running processes
ps aux
ps aux | grep nginx

# Interactive process viewer
top
htop   # enhanced version (may need install)

# Kill a process by PID
kill 1234
kill -9 1234   # force kill

# Kill by name
pkill nginx
killall node

# Run process in background
command &

# Bring background job to foreground
fg %1

# List background jobs
jobs

# Check port usage
lsof -i :3000
ss -tlnp | grep 3000
```

---

## Text Processing

Search, filter, and transform text.

```bash
# Search for pattern in file
grep "error" app.log
grep -i "error" app.log    # case-insensitive
grep -r "TODO" ./src       # recursive
grep -n "error" app.log    # show line numbers
grep -v "debug" app.log    # invert match

# Stream editor — substitute text
sed 's/old/new/g' file.txt
sed -i 's/old/new/g' file.txt   # in-place edit

# Print specific columns
awk '{print $1, $3}' file.txt
awk -F',' '{print $2}' data.csv  # CSV column 2

# Sort lines
sort file.txt
sort -r file.txt    # reverse
sort -n numbers.txt # numeric sort

# Remove duplicate lines
sort file.txt | uniq
sort file.txt | uniq -c   # count occurrences

# Count lines, words, characters
wc -l file.txt
wc -w file.txt

# Cut columns from delimited file
cut -d',' -f1,3 data.csv
```

---

## Networking

Inspect and test network connections.

```bash
# Check connectivity
ping google.com
ping -c 4 google.com   # send 4 packets

# DNS lookup
nslookup example.com
dig example.com

# Download a file
curl -O https://example.com/file.zip
wget https://example.com/file.zip

# Make HTTP requests
curl https://api.example.com/data
curl -X POST -H "Content-Type: application/json" \
  -d '{"key":"value"}' https://api.example.com/endpoint

# Show network interfaces
ip addr
ifconfig   # older systems

# Show routing table
ip route
netstat -rn

# SSH into remote server
ssh user@hostname
ssh -i ~/.ssh/key.pem user@hostname

# Copy files over SSH
scp file.txt user@host:/remote/path
rsync -avz local/ user@host:/remote/
```

---

## Bash Scripting

Write reusable shell scripts.

```bash
#!/bin/bash
# Shebang line — always first

# Variables
NAME="World"
echo "Hello, $NAME!"

# Command substitution
DATE=$(date +%Y-%m-%d)
FILES=$(ls *.txt)

# Conditionals
if [ -f "file.txt" ]; then
  echo "File exists"
elif [ -d "dir" ]; then
  echo "Directory exists"
else
  echo "Neither found"
fi

# Loops
for i in 1 2 3 4 5; do
  echo "Number: $i"
done

for file in *.txt; do
  echo "Processing $file"
done

while [ $COUNT -lt 10 ]; do
  echo $COUNT
  COUNT=$((COUNT + 1))
done

# Functions
greet() {
  local name=$1
  echo "Hello, $name!"
}
greet "Alice"

# Exit codes
command && echo "Success" || echo "Failed"
```

---

## Environment & Variables

Manage shell environment and configuration.

```bash
# Print all environment variables
env
printenv

# Print specific variable
echo $HOME
echo $PATH

# Set a variable (current session)
export MY_VAR="value"

# Append to PATH
export PATH="$PATH:/new/directory"

# Persist variables (add to ~/.bashrc or ~/.zshrc)
echo 'export MY_VAR="value"' >> ~/.bashrc
source ~/.bashrc   # reload config

# Alias shortcuts
alias ll='ls -la'
alias gs='git status'
alias ..='cd ..'

# View command history
history
history | grep git

# Run previous command
!!

# Run command from history by number
!42
```
