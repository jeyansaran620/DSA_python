# Uses python3
import sys

def optimal_summands(n):
    summands = []
    sums = 0
    i=1
    while sums + i <= n:
        summands.append(i)
        sums += i
        i+=1
    if sums < n:
        summands[-1] += n - sums 
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
