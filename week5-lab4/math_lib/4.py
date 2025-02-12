from math import *

def area_of_parallelogram(a, h):
    result = a * h
    return result

a = int(input("Write the length of base: "))
h = int(input("Write the height og parallelogram: "))
print(f"{area_of_parallelogram(a, h):.1f}")