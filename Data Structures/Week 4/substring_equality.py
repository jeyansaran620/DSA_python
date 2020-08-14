# python3

import sys

_m1 = 1000000007
_m2 = 1000000009
_x = 17

class Solver:
    def __init__(self, s):
        self.s = s
        self.pol1 = self.poly_s(len(s)+1,_m1)
        self.pol2 = self.poly_s(len(s)+1,_m2)
        self.has1 = self.hash_s(s,_m1)
        self.has2 = self.hash_s(s,_m2)
        
    def hash_s(self,s,m): 
        has = [[0] for x in range(len(s)+1)]
        has[0] = 0
        for i  in range(1,len(s)+1):
            has[i] =  ((_x * has[i-1]) + ord(s[i-1])) % m
        return has

    def poly_s(self,l,m): 
        pol = [[1] for x in range(l)]
        pol[0] = 1
        for i  in range(1,l):
            pol[i] =  (_x * pol[i-1]) % m
        return pol

    def ask(self, a, b, l):
            
        hash11 = (self.has1[a+l] - (self.pol1[l] * self.has1[a])) % _m1
        while hash11 < 0:
            hash11 += _m1
        hash11 = hash11 % _m1
        hash12 = (self.has1[b+l] - (self.pol1[l] * self.has1[b])) % _m1
        while hash12 < 0:
            hash12 += _m1
        hash12 = hash12 % _m1
        hash21 = (self.has2[a+l] - (self.pol2[l] * self.has2[a])) % _m2
        while hash21 < 0:
            hash21 += _m2
        hash21 = hash21 % _m2
        hash22 = (self.has2[b+l] - (self.pol2[l] * self.has2[b])) % _m2
        while hash22 < 0:
            hash22 += _m2
        hash22 = hash22 % _m2

        return(hash11 == hash12 and hash21 == hash22)



s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
