import sys

n,k = map(int,sys.stdin.readline().split())

arr = list(map(str,sys.stdin.readline().strip("\n")))
for i in range(k):
    arr.append('0')
sum=0

for i in range(n):
    if arr[i]=='P':
        start = i-k
        if start<0:
            start = 0
        for j in range(start,i+k+1):
            if arr[j]=='H':
                arr[j]=0
                sum+=1
                break
print(sum)