#Uses python3
import sys
import math


def minimum_distance(x, y):
    if len(x) == 1:
        return float('Inf')
    if len(x) == 2:
        xd = x[0] - x[1]
        yd = y[0] - y[1]
        return xd * xd + yd * yd
    
    med = len(x) // 2
    d1 = minimum_distance(x[:med], y[:med])
    d2 = minimum_distance(x[med:], y[med:])
    d = min(d1, d2)

    mid_point = (x[med - 1] + x[med]) / 2
        
    i = med - 1
    while i > -1 and (mid_point - x[i]) <= math.sqrt(d):
        i -= 1
        
    j = med
    while j < len(x) and (x[j] - mid_point) <= math.sqrt(d):
        j += 1
    temp2sort = list(zip(x[(i + 1):j], y[(i + 1):j]))
    temp2sort.sort(key=lambda cor: cor[1])
    d_min_temp = float('Inf')
    
    if len(temp2sort) > 0:
        x_temp, y_temp = list(zip(*temp2sort))
            
        for y_i in range(0, len(x_temp)):
            for y_i_seven in range(y_i + 1, min(y_i + 8, len(x_temp))):
                xd = x_temp[y_i] - x_temp[y_i_seven]
                yd = y_temp[y_i] - y_temp[y_i_seven]
                t = (xd) * (xd) + (yd) * (yd)
                d_min_temp = min(t, d_min_temp)
        
    return min(d, d_min_temp)
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]

    sorted_res = sorted(list(zip(x, y)), key=lambda x: (x[0], x[1]))
    x, y = zip(*sorted_res)
    x = list(x)
    y = list(y)
    
    print("{0:.15f}".format(math.sqrt(minimum_distance(x, y))))
