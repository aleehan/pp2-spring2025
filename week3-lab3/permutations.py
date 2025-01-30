def all_permutations(s):
    from itertools import  permutations
    a = permutations(s)
    arr = []
    for i in a:
        print("".join(i))
b = input("Write your string: ")
all_permutations(b)
