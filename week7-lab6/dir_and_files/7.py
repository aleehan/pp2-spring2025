import os

path1 = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week7-lab6\dir_and_files\lines.txt"
path2 = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week7-lab6\dir_and_files\test.txt"

with open(path1, "r") as file1, open(path2, "a") as file2:
    file2.write(file1.read())