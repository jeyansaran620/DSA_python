# Uses python3
import sys

def get_majority_element(a):
    if len(a) < 1:
        return 0    
    if len(a) == 1:
        return 1
    point = a[0]
    count = 1
    for x in a[1:]:
        if point == x:
            count += 1
        else :
            count -=1
        if count == 0:
            point = x
            count = 1
    if count >= 1:
        mini = 0
        for x in a:
            if x == point:
                mini += 1
        if mini > (len(a)//2):
            return 1
        else:
            return 0
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) == 1:
        print(1)
    else:
        print(0)
