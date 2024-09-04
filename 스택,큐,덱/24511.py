import queue
import sys
from collections import deque

n = int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
c=list(map(int,sys.stdin.readline().split()))
arr=[]
Q=deque()
for i in range(n):
    if a[i]==0:
        Q.appendleft(b[i])
for j in range(m):
    Q.append(c[j])
    arr.append(Q.popleft())
print(*arr)