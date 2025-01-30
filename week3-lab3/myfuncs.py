def is3to3(mylist):
    for i in range(n-1):
        if a[i] == 3 and a[i+1] == 3:
            return True
    return False

def solve(heads, legs):
    for chicken in range(heads + 1):
        rubbits = heads - chicken
        if 2 * chicken + 4 * rubbits == legs:
            return chicken, rubbits
    return "No solution"

def histogram(list):
    for i in range(len(list)):
        print(list[i] * '*')

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
    
def gramsForOunces(n):
    return n * 28.3495231

def all_permutations(s):
    from itertools import  permutations
    a = permutations(s)
    arr = []
    for i in a:
        print("".join(i))

def is_palindrome(s):
    right = 0
    left = int(len(s) - 1)

    behavior = False
    while left > right:
        if s[right] == s[left]:
            behavior = True
        elif right == left:
            behavior = True
        else:
            behavior = False
        right = right + 1
        left = left - 1

    if behavior == True:
        return "YES!"
    else:
        return "No..."
    
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

def reverse_string(s):
    b = s.split()
    b.reverse()
    print(" ".join(b))

def f_to_c(f):
    return (5 / 9) * (f - 32)

def unique(list):
    list.sort()

    b = []
    for i in list:
        if i in b:
            continue
        if i not in b:
            b.append(i)
    return b

def volume(r):
    v = (4/3)*3.14*(r**3)
    return v