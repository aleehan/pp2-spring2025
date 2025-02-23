import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

a = re.sub(r"_([a-z])", lambda s: s.group(1).upper(), text)

print(a)