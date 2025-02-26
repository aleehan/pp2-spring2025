import os

# path = os.getcwd()
path = r"C:\Users\lesh\Desktop"
directories = []
for item in os.listdir(path):
    if os.path.isdir(os.path.join(path, item)):
        directories.append(item)

print(directories)
