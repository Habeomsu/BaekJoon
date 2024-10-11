import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
new = [0]*n
for i in range(n):
    k=arr[i]
    cnt=0
    for j in range(n):
        if new[j]==0:
            if cnt == k:
                new[j]=i+1
                break
            cnt +=1
print(*new)