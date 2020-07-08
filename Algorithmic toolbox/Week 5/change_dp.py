# Uses python3
import sys

def get_change(m):
    #write your code here
    values=[0]
    for i in range(1,m+1):
        if i-1 >= 0:
            x = values[i-1] + 1
        if i-3 >= 0:
            x = min(x, values[i-3] + 1)
        if i-4 >= 0:
            x = min(x, values[i-4] + 1)
        values.append(x)
    return values[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
