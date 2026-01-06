# shell/shell.py

from shell.builtins import cmd_help, cmd_ps, cmd_exit, cmd_login, cmd_su
from vfs.vfs import ls, cd, cat, pwd, mkdir, write, rm
from utils.colors import CYAN, RESET

def start_shell():
    while True:
        try:
            raw = input(CYAN + "zramOS# " + RESET).strip()
            if not raw:
                continue

            parts = raw.split()
            cmd = parts[0]
            args = parts[1:]

            if cmd == "help":
                cmd_help()
            elif cmd == "ps":
                cmd_ps()
            elif cmd == "ls":
                ls()
            elif cmd == "cd" and args:
                cd(args[0])
            elif cmd == "pwd":
                pwd()
            elif cmd == "cat" and args:
                cat(args[0])
            elif cmd == "mkdir" and args:
                mkdir(args[0])
            elif cmd == "write" and len(args) >= 2:
                filename = args[0]
                content = " ".join(args[1:]).strip('"')
                write(filename, content)
            elif cmd == "rm" and args:
                rm(args[0])
            elif cmd == "login" and args:
                cmd_login(args[0])
            elif cmd == "su" and args:
                cmd_su(args[0])
            elif cmd == "exit":
                cmd_exit()
            else:
                print("Unknown or invalid command")
        except SystemExit:
            break
        except Exception as e:
            print(f"Error: {e}")
