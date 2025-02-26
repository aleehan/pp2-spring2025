import os

path = r"C:\Users\lesh\Desktop\Study\KBTU\example.png"

if os.path.exists(path): 
    print("Filename: ", os.path.basename(path))
    print("Directory: ", os.path.dirname(path))
else:
    print("File doesn't exist")