# python3

def SiftDown(H,i):
    Swaps = []
    maxIndex = i
    l = (i*2) + 1
    if l <= len(H)-1 and H[l] < H[maxIndex]:
        maxIndex = l
    r = (i*2) + 2
    if r <= len(H)-1 and H[r] < H[maxIndex]:
        maxIndex = r
    if i != maxIndex:
        Swaps.append([i,maxIndex])
        H[i], H[maxIndex] = H[maxIndex],H[i]
        H,Swap = SiftDown(H,maxIndex)
        Swaps += Swap
    return H,Swaps


def build_heap(data):
    Swaps = []
    for i in range(len(data)//2 , -1 ,-1):
        data,Swap = SiftDown(data,i)
        Swaps += Swap
    return Swaps 


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
