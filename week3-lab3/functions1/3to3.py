def is3to3(mylist):
    for i in range(n-1):
        if a[i] == 3 and a[i+1] == 3:
            return True
    return False

n = int(input("Amount of items: "))
a = []
for i in range(n):
    b = int(input())
    a.append(b)
print(is3to3(a))
