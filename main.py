# main.py

from boot.bootloader import boot
from shell.shell import start_shell

def main():
    boot()
    start_shell()

if __name__ == "__main__":
    main()
