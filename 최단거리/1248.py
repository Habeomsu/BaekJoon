###  1번 각 학생들은 정해진 마을 (x)로 가는 최단거리를 구한다. a
###  2번 x에서 자신의 마을로 가는 최단 거리를 구한다. b
###  a+b 를 구해서 가장 큰 사람을 구한다
### 단방향 그래프이다.

import sys
import heapq

INF = int(1e9)

N,M,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c= map(int,sys.stdin.readline().split())
    graph[a].append([c,b])

# def dijkstra(start,now):
#     que = []
#     distance[start]=0
#     heapq.heappush(que,[now,start])
#     while que:
#         now_dist,now_node = heapq.heappop(que)
#         if distance[now_node]<now_dist:
#             continue
#         for next_dist,next_node in graph[now_node]:
#             plus_dist = next_dist+now_dist
#             if plus_dist<distance[next_node]:
#                 distance[next_node] = plus_dist
#                 heapq.heappush(que,[plus_dist,next_node])
#
# final_dist=[0]*(N+1)
#
# for i in range(1,N+1):
#     distance=[INF]*(N+1)
#     dijkstra(i,0)
#     if i == X:
#         for i in range(1,N+1):
#             final_dist[i]+=distance[i]
#     else:
#         final_dist[i]+=distance[X]
#
# print(max(final_dist))