def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        else:
            for i in range(2, int((n ** 0.5) + 1)):
                if (n % i == 0):
                    return False
        return True

    a = list(map(int, numbers.split()))

    primelist = []
    for i in a:
        if is_prime(i):
            primelist.append(i)
    return primelist



b= (input("Write the numbers separated with space: "))
print(filter_prime(b))