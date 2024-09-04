import sys

n=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=arr1[::-1]
dp1=[1]*(n+1)
dp2=[1]*(n+1)
for i in range(1,n):
    for j in range(i):
        if arr1[i]>arr1[j]:
            dp1[i]=max(dp1[j]+1,dp1[i])
for i in range(1,n):
    for j in range(i):
        if arr2[i]>arr2[j]:
            dp2[i]=max(dp2[j]+1,dp2[i])
result = [a + b for a, b in zip(dp1[:-1], dp2[:-1][::-1])]
print(max(result)-1)