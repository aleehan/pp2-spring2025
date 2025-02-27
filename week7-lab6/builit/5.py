def is_true(tuple):
    return True if all(tuple) else False

tup = (1, 3, 5, 6)

print(is_true(tup))