# 19. Write a function called ‘calculate_mean’ that takes a list of numbers as input and 
# returns the mean (average) of the numbers. 
# The function should calculate the mean using the sum of the numbers divided by the total count.


def mean(lst):
    return sum(lst)/len(lst)

func = mean([1,2,33])
print(func)