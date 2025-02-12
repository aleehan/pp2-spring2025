import math

def area_of_trapezoid(a, b, h):
    s = (a+b)*h/2
    return s

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print(f"{area_of_trapezoid(a, b, h):.2f}")