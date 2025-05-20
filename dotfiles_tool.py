import os
import tarfile
import argparse
import datetime
from pathlib import Path

DOTFILES = [
    ".bashrc", ".zshrc", ".vimrc", ".gitconfig", ".profile"
]

def backup_dotfiles(target_dir):
    target_dir = Path(target_dir).expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    archive_name = target_dir / f"dotfiles-{date_str}.tar.gz"
    
    with tarfile.open(archive_name, "w:gz") as tar:
        for dotfile in DOTFILES:
            file_path = Path.home() / dotfile
            if file_path.exists():
                print(f"✅ Backing up: {file_path}")
                tar.add(file_path, arcname=dotfile)
            else:
                print(f"⚠️ Skipped (not found): {file_path}")

    print(f"\n📦 Backup complete: {archive_name}")

def restore_dotfiles(archive_path):
    archive_path = Path(archive_path).expanduser().resolve()
    
    if not archive_path.exists():
        print(f"❌ Archive not found: {archive_path}")
        return

    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(path=Path.home())
        print(f"✅ Dotfiles restored to {Path.home()}")

def main():
    parser = argparse.ArgumentParser(description="Dotfile Backup & Restore Tool")
    parser.add_argument('--backup', action='store_true', help="Create dotfile backup")
    parser.add_argument('--restore', action='store_true', help="Restore dotfiles from archive")
    parser.add_argument('--target', help="Directory to save backup to", default="backups")
    parser.add_argument('--archive', help="Archive file to restore from")

    args = parser.parse_args()

    if args.backup:
        backup_dotfiles(args.target)
    elif args.restore and args.archive:
        restore_dotfiles(args.archive)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

