import sys

n = int(sys.stdin.readline())
arr=[[0 for _ in range(2)] for _ in range(n)]
result = [0]*n
for i in range(n):
    arr[i][0],arr[i][1]=map(int,sys.stdin.readline().split())

for i in range(n):
    sum = 0
    for j in range(n):
        if(arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            sum +=1
    result[i]=sum+1

print(*result)