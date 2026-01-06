from ramdisk.state import RAM, CURRENT_USER
from vfs.nodes import Directory, File

def check_permission(node, mode):
    """
    Vérifie si l'utilisateur courant a le droit sur le node.
    mode = 'r' / 'w' / 'x'
    """
    if CURRENT_USER == "root":
        return True
    if node.owner != CURRENT_USER:
        idx = {"r": 0, "w": 1, "x": 2}[mode]
        return node.perms[idx] == mode
    return True

# --------------------
# COMMANDES VFS
# --------------------

def ls():
    cwd = RAM["cwd"]
    if not check_permission(cwd, "r"):
        print("Permission denied")
        return
    for name, node in cwd.children.items():
        print(f"{name}/" if node.type == "dir" else name)

def cd(path):
    # Aller à la racine
    if path == "/":
        RAM["cwd"] = RAM["fs"]
        return

    # Revenir en arrière
    if path == "..":
        if RAM["cwd"].parent and check_permission(RAM["cwd"].parent, "x"):
            RAM["cwd"] = RAM["cwd"].parent
        else:
            print("Permission denied")
        return

    # Chemin absolu ou relatif
    if path.startswith("/"):
        current = RAM["fs"]
        parts = path.strip("/").split("/")
    else:
        current = RAM["cwd"]
        parts = path.split("/")

    for part in parts:
        if part == "..":
            if current.parent and check_permission(current.parent, "x"):
                current = current.parent
            else:
                print("Permission denied")
                return
        elif part in current.children:
            node = current.children[part]
            if node.type != "dir":
                print("Not a directory")
                return
            if not check_permission(node, "x"):
                print("Permission denied")
                return
            current = node
        else:
            print("No such directory")
            return

    RAM["cwd"] = current

def cat(filename):
    cwd = RAM["cwd"]
    if filename not in cwd.children:
        print("File not found")
        return
    node = cwd.children[filename]
    if node.type != "file":
        print("Not a file")
        return
    if not check_permission(node, "r"):
        print("Permission denied")
        return
    print(node.content)

def pwd():
    path = []
    current = RAM["cwd"]
    while current:
        path.append(current.name)
        current = current.parent
    print("/".join(reversed(path)).replace("//", "/"))

def mkdir(name):
    cwd = RAM["cwd"]

    if not check_permission(cwd, "w"):
        print("Permission denied")
        return
    if name in cwd.children:
        print("File or directory already exists")
        return

    new_dir = Directory(name, owner=CURRENT_USER)
    cwd.add(new_dir)

def write(filename, content):
    cwd = RAM["cwd"]

    if not check_permission(cwd, "w"):
        print("Permission denied")
        return

    # écrase si existe
    file = File(filename, content, owner=CURRENT_USER)
    cwd.add(file)

def rm(name):
    cwd = RAM["cwd"]

    if not check_permission(cwd, "w"):
        print("Permission denied")
        return

    if name not in cwd.children:
        print("No such file or directory")
        return

    node = cwd.children[name]

    # sécurité : ne jamais supprimer la racine
    if node == RAM["fs"]:
        print("Operation not permitted")
        return

    # dossier non vide
    if node.type == "dir" and node.children:
        print("Directory not empty")
        return

    if not check_permission(node, "w"):
        print("Permission denied")
        return

    del cwd.children[name]
