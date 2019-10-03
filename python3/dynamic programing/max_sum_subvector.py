array = [3, 2, -1, 3, -6, 3]

def max_sum_subarray(array):
    max_sum = array[0]
    sum_so_far = array[0]

    for i in range(1, len(array)):
        sum_so_far = max(array[i], array[i] + sum_so_far)
        max_sum = max(sum_so_far, max_sum)
    
    return max_sum

print(max_sum_subarray(array))