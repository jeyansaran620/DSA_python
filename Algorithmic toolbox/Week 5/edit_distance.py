# Uses python3
def edit_distance(s, t):
    
    values = [ [0] * (len(t)+1) for _ in range(len(s)+1)]
    
    for i in range(len(s)+1):
        values[i][0]= i
    for i in range(len(t)+1):
        values[0][i]= i
        
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            ins = values[i][j-1] + 1
            de = values[i-1][j] + 1
            mat = values[i-1][j-1]
            mm = values[i-1][j-1] + 1
            if s[i-1]==t[j-1]:
                values[i][j]=min(ins,de,mat)
            else:
                values[i][j]=min(ins,de,mm)
    print(values)
    return values[-1][-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
