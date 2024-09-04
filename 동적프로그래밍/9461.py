import sys

def find(n):
    global arr
    arr[1]=1
    arr[2]=1
    arr[3]=1
    arr[4]=2
    arr[5]=2
    arr[6]=3
    arr[7]=4
    arr[8]=5
    for i in range(9,n+1):
        arr[i]=arr[i-1]+arr[i-5]

arr=[0]*101
n=int(sys.stdin.readline())
find(100)
for i in range(n):
    a=int(sys.stdin.readline())
    print(arr[a])