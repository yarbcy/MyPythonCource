def count_positives_sum_negatives(arr):
    #your code here
    if not arr:
        return []
        
    positiveCount = 0
    sum = 0
    for item in arr:
        if item > 0:
            positiveCount += True
        if item < 0:
           sum += item
    str = []
    
    if positiveCount >= 0:
        str.append(positiveCount)
    if sum <= 0:
        str.append(sum)    
    
    return str