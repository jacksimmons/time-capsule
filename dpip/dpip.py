import os
import sys
import shutil

# A program to fix pip not installing packages to the correct directory
def main(args, dest_dir):
    command = "py -m pip"
    for arg in args:
        command += " " + arg
    command += " --target=\"" + dest_dir + "\""
    print(command)
    os.system(command)

# Prevents dpip from being called as a module
if __name__ == "__main__":
    dest_dir = r"C:\Users\sack-\AppData\Local\Programs\Python\Python311\Lib\site-packages"
    args = []

    if len(sys.argv) > 1:
        # First arg is always the file
        args = sys.argv[1:]
    main(args, dest_dir)
