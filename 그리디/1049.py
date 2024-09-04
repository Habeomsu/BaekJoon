import sys

n,m=map(int,sys.stdin.readline().split())
arr1=[]
arr2=[]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr1.append(a)
    arr2.append(b)
arr1=sorted(arr1)
arr2=sorted(arr2)
sum=0
if n>6:
    if arr1[0]<=arr2[0]*6:
        sum+=n//6*arr1[0]
        n=n%6
    else:
        sum+=n*arr2[0]
        n=0
if n*arr2[0]>arr1[0]:
    sum+=arr1[0]
else:
    sum+=n*arr2[0]
print(sum)