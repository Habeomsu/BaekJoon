import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip("\n"))))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx,ny = a+dx[i],b+dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]==1:
                arr[nx][ny]=arr[a][b]+1
                que.append((nx,ny))

bfs(0,0)
print(arr[n-1][m-1])
