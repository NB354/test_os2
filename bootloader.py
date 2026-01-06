# boot/bootloader.py

import time
from kernel.kernel import init_kernel
from ramdisk.state import reset_ram

def boot():
    print("[ZRAM-OS] Booting...")
    time.sleep(0.3)

    print("[MEM] Allocating volatile memory")
    reset_ram()
    time.sleep(0.3)

    print("[KERNEL] Initializing kernel")
    init_kernel()
    time.sleep(0.3)

    print("[FS] Mounting RAM filesystem")
    time.sleep(0.3)

    print("[SHELL] Launching shell\n")
