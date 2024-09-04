import sys
n=int(sys.stdin.readline())
arr=[]
arr1=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr=sorted(arr,key=lambda x:x[0])
for i in range(n):
    arr1.append(arr[i][1])
dp1=[1]*(n)
for i in range(1,n):
    for j in range(i):
        if arr1[i]>arr1[j]:
            dp1[i]=max(dp1[i],dp1[j]+1)

print(n-max(dp1))
