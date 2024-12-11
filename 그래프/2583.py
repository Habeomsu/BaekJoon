import sys
from collections import deque

m,n,k = map(int,sys.stdin.readline().split())

arr=[]

for i in range(k):
    arr.append(list(map(int,sys.stdin.readline().split())))
result=[[0 for _ in range(n)] for _ in range(m)]
for i in range(k):
    a,b,c,d=arr[i]
    for j in range(a,c):
        for l in range(b,d):
            result[l][j]=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    que=deque()
    que.append((x,y))
    result[x][y]=1
    cnt=1
    while que:
        x,y=que.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<m and 0<=ny<n and result[nx][ny]==0:
                que.append((nx,ny))
                result[nx][ny]=1
                cnt +=1
    return cnt
sum=0
result2=[]
for i in range(m):
    for j in range(n):
        if result[i][j]==0:
            sum +=1
            result2.append(bfs(i,j))
result2.sort()
print(sum)
print(*result2)


