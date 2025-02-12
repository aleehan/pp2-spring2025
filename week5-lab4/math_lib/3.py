from math import *

def area_of_poligon(n, length):
    apothem = length/(2 * tan(pi/n))
    result = (n * length * apothem) / 2
    return result

n = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
print(f"{area_of_poligon(n, length):.2f}")

