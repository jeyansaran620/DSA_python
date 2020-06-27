n = int(input())
arr = input().split(" ")

index1=0
max1=0

for i in range(0,n):
    if int(arr[i]) > max1:
        max1 = int(arr[i])
        index1=i
        
max2=0

for i in range(0,n):
    if int(arr[i]) > max2 and i != index1:
        max2 = int(arr[i])
print(max1*max2)
