# Uses python3

def get_change(m):
    total = 0
    count=0
    while total < m:
        while total + 10 <= m:
            total += 10
            count += 1
            
        while total + 5 <= m:
            total += 5
            count += 1
            
        while total + 1 <= m:
            total += 1
            count += 1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
