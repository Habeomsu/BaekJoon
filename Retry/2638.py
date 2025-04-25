'''

치즈가 없는 구간에서 bfs를 통해 1보다 크거나 같으면 해당 공간을 +1 해준다
최종적으로 3이상인 경우엔 녹는 부분이다
여기서 문제는 '내부 치즈를 어떻게' 처리하냐 이다.
정답은 bfs를 한번만 한다 ! 방문 처리를 하면되는 것이다.
그리고 해당 위치가 1보다 크면 큐에 넣지 않는다

'''

import sys
from collections import deque

N ,M = map(int,sys.stdin.readline().split())

arr = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    visited = [[0] * M for i in range(N)]
    visited[x][y] = -1
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] != -1:
                if arr[nx][ny] == 1:
                    visited[nx][ny] +=1
                elif arr[nx][ny] == 0:
                    visited[nx][ny] = -1
                    que.append((nx,ny))
    return visited
cnt = 0
while True:
    visited = bfs(0,0)
    sum = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                arr[i][j] = 0
                sum +=1
    if sum == 0:
        break
    cnt +=1
print(cnt)