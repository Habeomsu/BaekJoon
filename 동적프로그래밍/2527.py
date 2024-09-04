import sys

n,k = map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
new=[]
for i in range(n-1):
    new.append(arr[i+1]-arr[i])
new=sorted(new)
sum=0
for i in range(n-k):
    sum+=new[i]
print(sum)