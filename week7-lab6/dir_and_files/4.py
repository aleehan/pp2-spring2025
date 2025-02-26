import os

# or readlines()

path = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week7-lab6\dir_and_files\lines.txt"
lines = 0
with open(path, "r") as text:
    for count in text:
        lines += 1

print(lines)