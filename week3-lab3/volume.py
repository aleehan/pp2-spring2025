def volume(r):
    v = (4/3)*3.14*(r**3)
    return v

r = int(input("Write the radius of sphere: "))
print(volume(r))