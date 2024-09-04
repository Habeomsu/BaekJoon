import sys
a,b=map(int,sys.stdin.readline().split())
d=b
arr=[]
for i in range(a):
    c=int(sys.stdin.readline())
    arr.append(c)
arr=sorted(arr,reverse=True)
sum=0
result=0
for j in range(len(arr)):
    if arr[j]<=b:
        sum = sum + arr[j] * (b // arr[j])
        result = result + b // arr[j]
        b = b % arr[j]
print(result)