import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()


pattern = r"\ba\w*?b\b"

matches = re.findall(pattern, text)
print(matches)