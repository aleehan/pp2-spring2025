def inversal_order(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("n: "))
for i in inversal_order(n):
    print(i)
