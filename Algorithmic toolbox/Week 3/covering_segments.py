# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda tup: tup[0])
    
    start = segments[0].start
    end = segments[0].end
    
    for x in segments[1:]:
        
        if x.end < end:
            end = x.end
        if x.start > start:
            start = x.start
            
        if x.start > end or x.start > start:
            points.append(end)
            start = x.start
            end = x.end
                    
    if segments[-1].start <= start:
        points.append(segments[-1].start)
    else:
        points.append(segments[-1].end)
         
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
