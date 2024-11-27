import sys

n = int(sys.stdin.readline())
result=0
if n==0:
    result =0
elif n==1:
    result =1
else:
    arr=[0]*(n+1)
    arr[1]=1

    for i in range(2,n+1):
        arr[i]=arr[i-2]+arr[i-1]
    result =arr[n]
print(result)