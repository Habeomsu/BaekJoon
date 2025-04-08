'''
1 -> N 으로 가는 최단 경로를 구하는 문제
단, 원하는 두점을 지나는 최단 경로를 구해야한다
만약 두점이 v1, v2 일 경우
1 -> v1 -> v2 -> N
1 -> v2 -> v1 -> N 이 존재한다

3번을 다익스트라를 하면 된다
1. 1 에서 다익스트라
2. v1 에서 다익스트라
3. v2 에서 다익스트라

'''

import sys
from collections import deque
INF = int(1e9)

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for i in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    que = deque()
    que.append((0,start))
    dist[start] = 0
    while que:
        now_dist,now_node = que.popleft()
        if dist[now_node] < now_dist:
            continue
        for i in graph[now_node]:
            next_dist,next_node = i
            if dist[next_node] > now_dist + next_dist:
                dist[next_node] = now_dist + next_dist
                que.append((dist[next_node],next_node))

arr_v1 = 0
arr_v2 = 0
dist=[INF for _ in range(N+1)]
dijkstra(1)
if dist[v1] == INF or dist[v2] == INF or dist[N] == INF:
    print(-1)
    exit()
arr_v1 += dist[v1]
arr_v2 += dist[v2]
dist=[INF for _ in range(N+1)]
dijkstra(v1)
if dist[v1] == INF or dist[v2] == INF or dist[N] == INF:
    print(-1)
    exit()
arr_v1 += dist[v2]
arr_v2 += dist[N]
dist=[INF for _ in range(N+1)]
dijkstra(v2)
if dist[v1] == INF or dist[v2] == INF or dist[N] == INF:
    print(-1)
    exit()
arr_v1 += dist[N]
arr_v2 += dist[v1]


result = min(arr_v1,arr_v2)

print(result)
