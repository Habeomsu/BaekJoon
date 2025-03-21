### distance 를 이차원 배열로 선언한다..
### 일단 (x,y,c) 를 힙큐에 넣어준다
### 이전 거리 + 현재 거리 < distance인 경우 distance를 변경해준다 !!!!!

import sys
import heapq

cnt = 0
INF = int(1e9)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break
    cnt += 1
    arr = []
    for i in range(a):
        arr.append(list(map(int,sys.stdin.readline().split())))
    distance = [[INF]*a for i in range(a)]
    que =[]
    heapq.heappush(que,[arr[0][0],0,0])
    distance[0][0] = arr[0][0]
    while que:
        cost, x, y = heapq.heappop(que)
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<a and 0 <=ny<a:
                if distance[nx][ny] > cost + arr[nx][ny]:
                    distance[nx][ny] = cost + arr[nx][ny]
                    heapq.heappush(que,[distance[nx][ny],nx,ny])

    print(f'Problem {cnt}: {distance[a-1][a-1]}')

