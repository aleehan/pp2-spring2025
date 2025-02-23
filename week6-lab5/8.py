import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(re.sub(r'([A-Z])', lambda s: ' '+s.group(1), text).lstrip())