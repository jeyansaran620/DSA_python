# Uses python3
import sys

def get_pisano(m):
    past = 0
    current = 1
    for i in range(m*m):
        past , current = current , (current + past) % m
        if past == 0 and current == 1:
            return i+1
    return 
def get_fibonacci_huge_naive(n, m):
    n = n % get_pisano(m)
    if (n <= 1):
        return n
    past = 0
    current = 1
    for _ in range(n-1):
        past , current = current ,(current + past)
    return current % m 

if __name__ == '__main__':
    print(get_pisano(10))
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))

# 0 1 1 2 3 5 8 13

