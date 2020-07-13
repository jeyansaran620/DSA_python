
from collections import deque 

def max_sliding_window(arr, n, k): 
    maximums = []
    Qi = deque() 
  
    for i in range(k):
        
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop()
            
        Qi.append(i); 
          
    for i in range(k, n):
        
        maximums.append(arr[Qi[0]])
          
        while Qi and Qi[0] <= i-k: 
              
            Qi.popleft()  
          
        while Qi and arr[i] >= arr[Qi[-1]] : 
            Qi.pop()     

        Qi.append(i) 
      

    maximums.append(arr[Qi[0]])
    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence,n, window_size))

