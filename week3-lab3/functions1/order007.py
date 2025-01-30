def spy_game(a):
    pairs = {}
    for i in range(len(a)):
        pairs.update({i : a[i]})

    remove_keys = []
    for i in pairs:
        if pairs[i] != 0 and pairs[i] != 7:
            remove_keys.append(i)

    for i in remove_keys:
        del pairs[i]

    ordered = [0, 0, 7]
    valuesofp = []
    for i in pairs.values():
        valuesofp.append(i)

    if valuesofp == ordered:
        return True
    else:
        return False
    

n = int(input("Write the amount of items: "))
a = []
for i in range(n):
    b = int(input())
    a.append(b)

print(spy_game(a))