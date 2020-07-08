# Uses python3
import sys


def fast_count_segments(starts, ends, points):
    
    cnt = [0] * len(points)
    
    full = list(zip(starts, [1] * len(starts)))
    full += list(zip(ends, [-1] * len(ends)))
    full += list(zip(points, [0] * len(points), list(range(len(points)))))
    
    
    #print(starts_zip,"\n",ends_zip,"\n",points_zip,"\n",full)
    full.sort(key=lambda x: (x[0], -x[1]))
    
    res = 0
    for x in full:
        res += x[1]
        if len(x) == 3:
            cnt[x[2]] = res
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
