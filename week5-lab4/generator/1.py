def squares(n):
    i = 1
    while i <= n:
        yield i*i
        i+=1

n = int(input())
a = squares(n)

for i in a:
    print(i)