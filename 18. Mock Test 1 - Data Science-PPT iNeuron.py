18. Implement a decorator function called ‘timer’ that measures the execution time of a function. The ‘timer’ decorator should print the time taken by the decorated function to execute. Use the ‘time’ module in Python to calculate the execution time.

from time import time 

def my_timer_func(func): 
    
    def timer(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return timer

@my_timer_func 
def even_list(L): 
    even_L =[]
    for i in L: 

        if i%2 == 0: 
            even_L.append(i)
            i=i+1

    return even_L 

even_num_in_list = even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
even_num_in_list
