import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

def djkistra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start][start]=0
    while que:
        cost,now = heapq.heappop(que)
        if distance[start][now]<cost:
            continue

        for b,c in graph[now]:
            dist = cost + c
            if dist<distance[start][b]:
                distance[start][b] = dist
                heapq.heappush(que, (dist,b))

for i in range(1,n+1):
    djkistra(i)

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] == INF:
            distance[i][j] = 0

for i in range(1,n+1):
    print(*distance[i][1:])