def unique(list):
    list.sort()

    b = []
    for i in list:
        if i in b:
            continue
        if i not in b:
            b.append(i)
    return b

n = int(input("Write the amount of items: "))

a = []
for i in range(n):
    inp = input()
    a.append(inp)

print(unique(a))
