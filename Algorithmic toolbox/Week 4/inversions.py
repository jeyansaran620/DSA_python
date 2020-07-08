# Uses python3
import sys

def merge(left,right,n):
    
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] > right[right_index] :
            merged.append(right[right_index])
            right_index  += 1
            n += len(left) - left_index
    
        else:
            merged.append(left[left_index])
            left_index += 1
 
            
    merged += left[left_index:]
  
    merged += right[right_index:]   
    
    return merged,n



def mergesort(my_list):

    if len(my_list) <= 1:
        return my_list,0
    
    mid = len(my_list) // 2
    
    left = my_list[:mid]
    right = my_list[mid:]
    
    left,m = mergesort(left)
    right,n = mergesort(right)
    
    return merge(left,right,m+n)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(mergesort(a)[1])
