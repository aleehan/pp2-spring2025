import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[\s,.]"
a = re.sub(pattern, ":", text)

print(a)