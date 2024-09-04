import sys
from collections import deque
sys.setrecursionlimit(100000)
def bfs(x,y):
    global result
    q=deque()
    q.append((x,y))
    arr[x][y]=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if arr[nx][ny] ==1:
                arr[nx][ny]=0
                q.append((nx,ny))

num=int(sys.stdin.readline())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(num):
    m,n,k=map(int,sys.stdin.readline().split())
    result=0
    arr=[[0]*m for _ in range(n)]
    for j in range(k):
        x,y=map(int,sys.stdin.readline().split())
        arr[y][x]=1
    for l in range(n):
        for w in range(m):
            if arr[l][w]==1:
                bfs(l,w)
                result+=1
    print(result)
