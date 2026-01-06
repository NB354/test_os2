# ramdisk/state.py

from vfs.nodes import Directory, File

# Liste des utilisateurs
USERS = {
    "root": {"password": "root", "home": "/home/root"},
    "bob": {"password": "bob", "home": "/home/bob"}
}

CURRENT_USER = None  # sera défini après login


RAM = {
    "booted": False,
    "processes": {},
    "next_pid": 1,
    "logs": [],
    "fs": None,
    "cwd": None
}

def init_fs():
    root = Directory("/", owner="root")
    home = Directory("home", owner="root")
    root.add(home)

    user_dir = Directory("user", owner="root")
    home.add(user_dir)

    note = File("note.txt", "Bienvenue dans ZRAM-OS\nTout est en RAM.", owner="root")
    user_dir.add(note)

    return root

def reset_ram():
    RAM["booted"] = False
    RAM["processes"].clear()
    RAM["next_pid"] = 1
    RAM["logs"].clear()
    RAM["fs"] = init_fs()
    RAM["cwd"] = RAM["fs"]
