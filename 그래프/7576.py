import sys
from collections import deque



m,n=map(int,sys.stdin.readline().split())
arr=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
start=deque()
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            start.append((i,j))
            arr[i][j]=1
while start:
    x,y=start.popleft()
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
            arr[nx][ny]=arr[x][y]+1
            start.append((nx,ny))
max=0
loof=True
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            max=0
            loof=False
            break
        if arr[i][j]>max:
            max=arr[i][j]
    if loof==False:
        break
print(max-1)
