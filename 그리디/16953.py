import sys
from collections import deque

a,b=map(int,sys.stdin.readline().split())

def bfs(x):
    q=deque()
    q.append(x)
    arr={x:1}
    while q:
        x=q.popleft()
        if x==b:
            return arr[b]
        for i in [x*2,x*10+1]:
            if 1<=i<=b and i not in arr:
                arr[i]=arr[x]+1
                q.append(i)
    return -1

result=bfs(a)
if result==-1:
    print(-1)
else:
    print(result)