# python3
import sys


def compute_min_refills( tank, stops):
    # write your code here
    count = 0
    i=0
    while i < len(stops)-1:
        last = i
        while i < len(stops)-1  and stops[i+1]-stops[last] <= tank :
            i+=1
            
        if i == last:
            return -1
        
        if i < len(stops)-1:
            count +=1
            
    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    stops.append(d)
    stops.insert(0,0)
    print(compute_min_refills( m, stops))
