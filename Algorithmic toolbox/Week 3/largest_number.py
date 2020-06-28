#Uses python3

import sys

def merge(left,right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        
        if int(right[right_index] + left[left_index]) > int(left[left_index] + right[right_index]) :
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


def largest_number(a):
    res = ""
    if len(a)==0:
        return res
    a = mergesort(a)
    
    for i in range(len(a)):
        res += a[i]
        a[i] = a[i]
        
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
     
            
    
