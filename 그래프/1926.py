import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

arr = []

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    que=deque()
    que.append((x,y))
    arr[x][y]=0
    sum = 1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if arr[nx][ny]==1:
                que.append((nx,ny))
                arr[nx][ny] = 0
                sum +=1
    return sum
result=[]
cnt =0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            cnt +=1
            result.append(bfs(i,j))
if cnt ==0:
    print(cnt)
    print(0)
else:
    print(cnt)
    print(max(result))