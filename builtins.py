# shell/builtins.py

from kernel.kernel import list_processes
from vfs.vfs import ls, cd, cat
from ramdisk.state import USERS, CURRENT_USER, RAM
from utils.colors import RED, RESET

def cmd_help():
    print("Available commands:")
    print("  help               - show this message")
    print("  ps                 - list processes")
    print("  ls                 - list directory")
    print("  cd <dir>           - change directory")
    print("  pwd                - show current directory")
    print("  cat <file>         - show file content")
    print("  mkdir <dir>        - create directory")
    print("  write <file> <txt> - create or overwrite file")
    print("  rm <name>          - remove file or empty directory")
    print("  login <user>       - login as user")
    print("  su <user>          - switch user")
    print("  exit               - shutdown OS")

def cmd_ps():
    procs = list_processes()
    print("PID   NAME     STATE")
    for p in procs:
        print(f"{p['pid']:<5} {p['name']:<8} {p['state']}")

def cmd_exit():
    print(RED + "[ZRAM-OS] Shutting down..." + RESET)
    raise SystemExit

def cmd_login(username):
    if username not in USERS:
        print("No such user")
        return
    password = input("Password: ")
    if password != USERS[username]["password"]:
        print("Wrong password")
        return
    global CURRENT_USER
    CURRENT_USER = username
    print(f"Logged in as {username}")

def cmd_su(username):
    cmd_login(username)
