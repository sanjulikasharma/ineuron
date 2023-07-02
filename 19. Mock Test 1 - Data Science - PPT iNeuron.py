19. Write a function called ‘calculate_mean’ that takes a list of numbers as input and returns the mean (average) of the numbers. The function should calculate the mean using the sum of the numbers divided by the total count.

@my_timer_func
def calculate_mean(l): 
    sum = 0 
    for i in l : 
        sum = sum + i 
        i =i+1 
    return sum/len(l)

calculate_mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
