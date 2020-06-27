# Uses python3
import sys


def gcd_naive(a, b):
    if b==0:
        return a
    return gcd_naive(b ,a%b)

def lcm_naive(a, b):
    if a == 0 or b == 0:
        return 0
    return (a*b) // gcd_naive(a,b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

