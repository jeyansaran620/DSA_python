# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
        
    def __init__(self):
        self.children = []
        
    def addChild(self, child):
        self.children.append(child)
    
    def height(self):
        if len(self.children) == 0:
            return 1
        else:
            temp = []
            for child in self.children:
                temp.append(child.height())
            return 1 + max(temp)


def compute_height(n, parents):
    nodes = [Node() for i in range(n)]
    for vertex in range(n):
        pi = parents[vertex]
        if pi == -1:
            root = nodes[vertex]
        else:
            nodes[pi].addChild(nodes[vertex])
  
    return root.height()

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

threading.Thread(target=main).start()
