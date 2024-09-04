import sys
from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny]=arr[a][b]+1
                q.append((nx, ny))

n,m=map(int,sys.stdin.readline().split())
arr=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip("\n"))))
bfs(0,0)
print(arr[n-1][m-1])