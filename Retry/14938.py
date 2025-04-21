'''

각 지역에서 다익스트라 알고리즘을 통해 최단거리를 구한다.
-> 추후에 플로이드 워셜 가능
다익스트라를 통해서 수색범위 안에 있으면 아이템을 얻을 수 있다는 것이므로 아이템을 더해준다


'''

import sys
import heapq
INF = int(1e9)

N, M ,R = map(int,sys.stdin.readline().split())
item = list(map(int,sys.stdin.readline().split()))

graph =[[] for _ in range(N+1)]

for _ in range(R):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append([c,b])
    graph[b].append([c,a])


def dijkstra(now,start):
    visit  = [INF]*(N+1)
    que= []
    visit[start] = now
    heapq.heappush(que,(now,start))
    while que:
        pre_now, pre_start = heapq.heappop(que)
        if visit[pre_start] < pre_now:
            continue
        for i in graph[pre_start]:
            next_dist ,next_node = i[0],i[1]
            if visit[next_node] > next_dist + pre_now:
                visit[next_node] = next_dist + pre_now
                heapq.heappush(que,(visit[next_node],next_node))
    return visit

Max = 0

for i in range(1,N+1):
    visit = dijkstra(0,i)
    cnt = 0
    for j in range(1,N+1):
        if visit[j] <= M :
            cnt = cnt + item[j-1]
    if Max < cnt:
        Max = cnt

print(Max)