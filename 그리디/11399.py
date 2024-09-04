import sys

n= int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr2=sorted(arr)
arr3=[]
sum=0
for i in range(n):
    sum=sum+arr2[i]*(n-i)
print(sum)
