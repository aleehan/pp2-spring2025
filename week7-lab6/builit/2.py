string = "KBTUshnick"

upper, lower = [], []

for letter in string:
    if letter.isupper(): upper.append(letter)
    else: lower.append(letter)

print(f"Upper case letters: {len(upper)}\nLower case letters: {len(lower)}")