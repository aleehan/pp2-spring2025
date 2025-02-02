def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int((n**0.5) + 1)):
            if n % i == 0:
                return False
    return True

nums = [1, 3, 4, 5, 6, 8, 10, 7, 23]
mylist = list(filter(lambda x : is_prime(x), nums))

print(mylist)