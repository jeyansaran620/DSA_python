#Uses python3

import sys

def lcs2(s, t):
    
    values = [ [0] * (len(t)+1) for _ in range(len(s)+1)]
        
    for j in range(1,len(t)+1):
        
        for i in range(1,len(s)+1):
            
            ins = values[i][j-1] 
            de = values[i-1][j] 
            mat = values[i-1][j-1] + 1
            mm = values[i-1][j-1]
            
            if s[i-1]==t[j-1]:
                values[i][j]=max(ins,de,mat)
            else:
                values[i][j]=max(ins,de,mm)
                
    return values[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
