import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[a-z]+\_[a-z]+"

print(re.findall(pattern, text))