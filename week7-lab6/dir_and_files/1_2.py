import os

path = r"C:\Users\lesh\Desktop\Study"
all_item = []
for item in os.listdir(path):
    all_item.append(item)

print(all_item)