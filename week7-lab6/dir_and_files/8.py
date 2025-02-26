import os

path = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week7-lab6\dir_and_files\del.txt"

if os.access(path, os.F_OK):
    print(f"The file '{os.path.basename(path)}' exists, deleting...")
    os.remove(path)
else:
    print(f"The file '{os.path.basename(path)}' doesn't exists")
