import sys
from collections import deque

def bfs(x,y):
    q=deque()
    q.append((x,y))
    arr[x][y]=0
    while q:
        x,y=q.popleft()
        if x == c and y == d:
            return arr[x][y]
        for i in range(8):
            nx,ny=move[i]
            nx=x+nx
            ny=y+ny

            if 0<=nx<m and 0<=ny<m and arr[nx][ny]==-1:
                arr[nx][ny]=arr[x][y]+1
                q.append((nx,ny))
    return arr[c][d]

move=[(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(2,1),(2,-1),(1,-2)]
n=int(sys.stdin.readline())
for i in range(n):
    m=int(sys.stdin.readline())
    a,b=map(int,sys.stdin.readline().split())
    c,d=map(int,sys.stdin.readline().split())
    arr=[[-1]*m for _ in range(m)]
    print(bfs(a,b))
