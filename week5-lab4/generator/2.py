def print_num():
    n = int(input("n: "))
    def even_nums(n):
        for i in range(0, n+1, 2):
            yield i

    nums = ", ".join(str(num) for num in even_nums(n))
    '''
    temp_list = []                    
    for num in even_gen(n):           
    temp_list.append(str(num))   

    even_numbers = ', '.join(temp_list)

    '''
    print(nums)

print_num()