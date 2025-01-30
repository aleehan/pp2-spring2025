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

s = input("Write the string: ")
print(is_palindrome(s))
