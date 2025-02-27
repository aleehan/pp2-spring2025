from functools import reduce

my_list = [2, 4, 7, 9, 1, 3]
sum_of_list = reduce(lambda a, b:a+b, my_list)

print(sum_of_list)