import sys
from collections import deque
def bfs(x,y):
    q=deque()
    q.append((x,y))
    arr[x][y]=0
    cnt=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]==1:
                arr[nx][ny]=0
                q.append((nx,ny))
                cnt += 1
    return cnt
n=int(sys.stdin.readline())
arr=[]
result=[]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip("\n"))))
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            result.append(bfs(i,j))
print(result)