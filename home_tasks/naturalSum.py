def solution(number):
    array = list(range(1,number))
    sum = 0
    for item in array:
        if (item % 3 == 0) or (item % 5 == 0):
            sum += item    
    return sum