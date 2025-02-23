import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

a = re.sub(r"\B([A-Z])", lambda s: '_'+s.group(1), text).lower()

print(a)