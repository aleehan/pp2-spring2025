import re

with open("row.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern = r"ab{2,3}"

print(re.findall(pattern, text))