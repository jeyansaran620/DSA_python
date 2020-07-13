#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        
    def Size(self):
        return len(self.__stack)
    
    def Values(self):
        return self.__stack


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            maxi = int(query[1])
            if stack.Size() != 0:
                maxi = max(stack.Values()[-1][1],maxi)
            stack.Push([int(query[1]),maxi])
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Values()[-1][1])
        else:
            assert(0)
