import sys

n=int(sys.stdin.readline())
for i in range(n):
    m=int(sys.stdin.readline())
    arr=[]
    sum=1
    for _ in range(m):
        arr.append(list(map(int,sys.stdin.readline().split())))
    arr=sorted(arr)
    min = arr[0][1]
    for k in range(1,m):
        if min>arr[k][1]:
            sum+=1
            min=arr[k][1]
    print(sum)