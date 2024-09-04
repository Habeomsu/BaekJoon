import sys

n=int(sys.stdin.readline())
arr=[]
result=0
for i in range(n):
    a=int(sys.stdin.readline())
    arr.append(a)
arr=sorted(arr,reverse=True)
for i in range(n):
    if result <=arr[i]*(i+1):
        result = arr[i]*(i+1)
print(result)