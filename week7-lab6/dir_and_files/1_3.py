import os

path = r"C:\Users\lesh\Desktop\Study"
files = []

for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        files.append(item)

print(files)