import sys

def plus(n):
    global arr
    arr[1]=1
    arr[2]=2
    arr[3]=4
    for i in range(4,n+1):
        arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
n=int(sys.stdin.readline())
arr=[0]*11
plus(10)
for i in range(n):
    a=int(sys.stdin.readline())
    print(arr[a])