import sys

n,l = map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr=sorted(arr)
result = 0
now =0
for i in arr:
    if now-0.5<i:
        now=i+l-0.5
        result +=1
print(result)