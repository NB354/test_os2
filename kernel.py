# kernel/kernel.py

from ramdisk.state import RAM
from kernel.process import Process

def init_kernel():
    RAM["booted"] = True
    create_process("init")
    create_process("shell")

def create_process(name):
    pid = RAM["next_pid"]
    RAM["next_pid"] += 1

    proc = Process(pid, name)
    RAM["processes"][pid] = proc
    return proc

def list_processes():
    return [p.to_dict() for p in RAM["processes"].values()]
