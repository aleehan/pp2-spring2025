def reverse_string(s):
    b = s.split()
    b.reverse()
    print(" ".join(b))

a = input("Write the string: ")
reverse_string(a)
