"""20. Write a function called ‘perform_hypothesis_test’ that takes two lists of numbers as input, 
representing two samples. 
The function should perform a two-sample t-test and return the p-value. 
Use the ‘scipy.stats’ module in Python to calculate the t-test and p-value."""

from scipy.stats import ttest_ind

def perform_hypothesis_test(lst1,lst2):
    t_statistics, p_value = ttest_ind(lst1,lst2)
    return p_value

lst1 = [5, 10, 15, 20, 25]
lst2 = [10, 20, 30, 40, 50]

func = perform_hypothesis_test(lst1=lst1,lst2=lst2)

print(func)

