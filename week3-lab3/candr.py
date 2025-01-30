def solve(heads, legs):
    for chicken in range(heads + 1):
        rubbits = heads - chicken
        if 2 * chicken + 4 * rubbits == legs:
            return chicken, rubbits
    return "No solution"

heads = int(input("Write the amount of heads: "))
legs = int(input("Write the amount of legs: "))

print(solve(heads, legs))
    
