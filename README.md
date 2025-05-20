# 🗃️ Dotfile Backup & Restore Tool (Python)

A lightweight Python CLI tool that backs up your important configuration files (dotfiles) into a compressed `.tar.gz` archive — and restores them with a single command.

---

## 🚀 Features

- ✅ Backup your common dotfiles (`.bashrc`, `.zshrc`, `.vimrc`, `.gitconfig`, etc.)
- ✅ Save to custom directory with timestamped archive name
- ✅ Restore dotfiles from any `.tar.gz` archive
- ✅ Clean, no dependencies, GitHub-safe

---

## 📦 Setup

### 1. Clone the repo
```bash
git clone https://github.com/elevelin/dotfiles-tool.git
cd dotfiles-tool
```
2. Run the tool

Backup dotfiles:

```bash
python3 dotfiles_tool.py --backup
```
Backup to a custom folder:

```bash
python3 dotfiles_tool.py --backup --target ~/my-backups
```
Restore from archive:

```bash
python3 dotfiles_tool.py --restore --archive backups/dotfiles-YYYY-MM-DD.tar.gz
```
🧠 Why Use This?
Dotfiles are critical for your development environment. This tool gives you:

-Version control-friendly backups

-Lightweight syncing to USB/GitHub

-Quick disaster recovery for local dev setups

✅ Roadmap Ideas
Git sync (push/pull dotfiles to a private repo)

Custom dotfile list support

Schedule with cron or launchd

📁 Files Included
```bash

dotfiles-tool/
├── dotfiles_tool.py       # Main script
├── backups/               # Default archive folder
├── README.md
└── .gitignore             # Excludes backups/
```
