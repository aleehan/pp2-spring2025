import os

path = r"C:\Users\lesh\Desktop\Study\KBTU\PP2\pp2-spring2025\week7-lab6\dir_and_files\lines.txt"
mylist = ["babab", "dududuru"]

with open(path, "w") as text:
    text.write(str(mylist))

# with open(path, "r") as content:
#     text_content =  content.read()

# print(text_content)