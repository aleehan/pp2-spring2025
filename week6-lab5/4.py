import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"[A-Z]{1}[a-z]+"

matches = re.findall(pattern, text)

print(matches)
