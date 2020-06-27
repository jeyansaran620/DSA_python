# Uses python3

import sys
def merge(left,right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        
        if right[right_index][1]/right[right_index][0] > left[left_index][1]/left[left_index][0] :
            merged.append(right[right_index])
            right_index += 1
            
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged



def mergesort(my_list):

    if len(my_list) <= 1:
        return my_list
    
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    
    left = mergesort(left)
    right = mergesort(right)

    
    return merge(left,right)

def get_optimal_value(capacity, my_list):
    
    if len(my_list) < 1:
        return 0
    value = 0
    my_list = mergesort(my_list)
    weight = 0
    i=0
    while i < len(my_list) and weight < capacity:
        if weight + my_list[i][0] <= capacity:
            weight += my_list[i][0]
            value += my_list[i][1]
        else:
            factor = my_list[i][0]/(capacity - weight)
            weight += my_list[i][0]/factor
            value += my_list[i][1]/factor
        i += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    my_list = list(zip(weights,values))
    opt_value = get_optimal_value(capacity, my_list)
    print("{:.10f}".format(opt_value))
