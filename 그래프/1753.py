import sys
import heapq

v ,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
node = [[] for _ in range(v+1)]
for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    node[a].append((b,c))

INF = int(1e9)
que = []
distance=[INF]*(v+1)

def dijkstra(start):
    distance[start]=0
    heapq.heappush(que,(0,start))
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:  # distance는 방문 안하면 inf이므로 무조건 클수밖에 없는데 작다는 것은 방문처리 완료 라는 뜻
            continue

        for b,c in node[now]:
            cost = c+dist
            if cost <distance[b]:
                distance[b]=cost
                heapq.heappush(que,(cost,b))

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
