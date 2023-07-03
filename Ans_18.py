# 18. Implement a decorator function called ‘timer’ that measures the execution time of a function. 
# The ‘timer’ decorator should print the time taken by the decorated function to execute. 
# Use the ‘time’ module in Python to calculate the execution time.

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time-start_time
        return execution_time
    return wrapper

@timer
def func(a,b):
    time.sleep(2)
    return a+b

print(func(1,2))