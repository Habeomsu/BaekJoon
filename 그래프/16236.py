import sys
from collections import deque

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]


def bfs(x, y,weight):
    result = []
    que = deque()
    visit = [[0] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    que.append((x, y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if arr[nx][ny] <= weight:  # 빈 공간
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] +1
                    que.append((nx, ny))
                    if arr[nx][ny]<weight and arr[nx][ny] !=0:
                        result.append((nx,ny,dist[nx][ny]))


    return sorted(result, key=lambda x: (-x[2], -x[0], -x[1]))


start_x, start_y = 0, 0
time = 0
weight = 2

# 상어의 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            start_x, start_y = i, j
            arr[i][j] = 0  # 상어 위치를 비워줌
ctn = 0
while True:
    shark = bfs(start_x, start_y, weight)
    if len(shark) == 0:
        break

    nx, ny, dist = shark.pop() # 가장 가까운 물고기 선택
    time += dist
    arr[nx][ny],arr[start_x][start_y] = 0,0  # 먹은 물고기 위치 비우기
    start_x, start_y = nx, ny
    ctn +=1
    if ctn == weight:
        weight +=1
        ctn = 0

print(time)
