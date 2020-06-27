# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    from_ %= 60
    to %= 60
    if to < from_ :
        to, from_ = from_ , 0 
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
