class VNode:
    def __init__(self, name, node_type, parent=None, owner="root", perms="rwx"):
        self.name = name
        self.type = node_type
        self.parent = parent
        self.owner = owner
        self.perms = perms  # rwx comme Linux

class File(VNode):
    def __init__(self, name, content="", parent=None, owner="root", perms="rw-"):
        super().__init__(name, "file", parent, owner, perms)
        self.content = content

class Directory(VNode):
    def __init__(self, name, parent=None, owner="root", perms="rwx"):
        super().__init__(name, "dir", parent, owner, perms)
        self.children = {}

    def add(self, node):
        self.children[node.name] = node
        node.parent = self
