# Uses python3
import sys

def optimal_sequence(n):
    x = [None for i in range(max(4, n + 1))]
    x[0] = []
    x[1] = [1]
    x[2] = [1, 2]
    x[3] = [1, 3]
    for num in range(4, n + 1):
        n3 = float('Inf')
        n2 = float('Inf')
        if num % 3 == 0:
            n3 = len(x[num // 3]) + 1
        if num % 2 == 0:
            n2 = len(x[num // 2]) + 1
        n1 = len(x[num - 1]) + 1
        minn = min(n3, n2, n1)
        if minn == n3:
            x[num] = x[num // 3] + [num]
        elif minn == n2:
            x[num] = x[num // 2] + [num]
        elif minn == n1:
            x[num] = x[num - 1] + [num]

    return x[n]

input = sys.stdin.read()
n = int(input)

sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
