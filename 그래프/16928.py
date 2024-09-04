import sys
from collections import deque

def bfs(x):
    q=deque()
    q.append(x)
    arr2[x]=0
    while q:
        x=q.popleft()
        if x==100:
            break
        for i in range(6):
            nx=x+dx[i]
            if nx<0 or nx>100:
                continue
            if arr1[nx]!=0:
                nx=arr1[nx]
            if arr2[nx]==-1:
                arr2[nx]=arr2[x]+1
                q.append(nx)
    return arr2[100]

n,m=map(int,sys.stdin.readline().split())
arr1=[0]*101
arr2=[-1]*101
dx=[1,2,3,4,5,6]
for i in range(n+m):
    a,b=map(int,sys.stdin.readline().split())
    arr1[a]=b
print(bfs(1))