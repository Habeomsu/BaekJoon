### 치즈에서 4방향을 탐색하는데 만약에 2방향 이상이 0이다 -> 그럼 치즈는 0으로 변한다( 하지만 이건 동식에 발생해야한다 )
### 치즈 내부에서는 2방향 이상이어도 치즈가 녹지 않는다.
### 치즈가 내부에 존재하는 것은 어떻게 판단할지...
### 1. 전체 dfs를 진행한다 -> 처음 0 을 판단하고 다음번에도 0 이 나올경우 그것은 내부 공간 이라는 뜻 ...
### 그럼 내부 공간을 0이 아닌 수로 채워준다
### dfs를 통해서 삭제할 치즈를 구한다

import sys
from collections import deque
sys.setrecursionlimit(10**6)

N,M = map(int,sys.stdin.readline().split())

arr = []
for i in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def find_cheeze(i,j):
    que= deque()
    que.append((i,j))
    visit[i][j]=1
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]==0 and visit[nx][ny]==0:
                    que.append((nx, ny))
                    visit[nx][ny]=1
                elif arr[nx][ny]==1:
                    visit[nx][ny]+=1

time = 0
while True:
    visit = [[0] * M for _ in range(N)]
    find_cheeze(0,0)
    time +=1
    for i in range(N):
        for j in range(M):
            if visit[i][j]>=2:
                arr[i][j]=0
    block=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]==0:
                block+=1
    if block == N*M:
        break
print(time)