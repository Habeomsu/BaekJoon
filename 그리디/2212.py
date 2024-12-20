import sys

n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr=sorted(arr)
new_arr=[]
result=0

for i in range(n-1):
    new_arr.append(arr[i+1]-arr[i])

new_arr=sorted(new_arr,reverse=True)
if k>=n:
    result=0
else:
    for _ in range(k-1):
        new_arr.pop(0)
    result=sum(new_arr)
print(result)
