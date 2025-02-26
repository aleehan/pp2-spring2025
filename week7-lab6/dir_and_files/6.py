import os

from string import ascii_uppercase
for letter in ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        pass

#delete these files
# for letter in ascii_uppercase:
#     os.remove(f"{letter}.txt")

