import sys
from collections import deque

m,n,h = map(int,sys.stdin.readline().split())
arr=[]
for _ in range(h):
    layer = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        layer.append(row)
    arr.append(layer)
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==1:
                q.append((i,j,k))

while q:
    z,x,y=q.popleft()
    for i in range(6):
        nz=dz[i]+z
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nz<h and 0<=nx<n and 0<=ny<m and arr[nz][nx][ny]==0:
            arr[nz][nx][ny]=arr[z][x][y]+1
            q.append((nz,nx,ny))

max=0
error=False
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k]==0:
                error=True
            if arr[i][j][k]>max:
                max=arr[i][j][k]

if error==True:
    print(-1)
else:
    print(max-1)