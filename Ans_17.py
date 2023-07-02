# 17. Write a function that takes a list of numbers as input and returns a new list containing only the 
# even numbers from the input list. Use list comprehension to solve this problem.

even_list = []

def even_num_in_lst(lst):
    for num in lst:
        if num%2==0:
            even_list.append(num)
    
    return even_list

func = even_num_in_lst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(func)