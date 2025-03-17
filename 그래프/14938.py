### 어디로 떨어질지를 알 수 없기 때문에 1 ~ N 까지의 노드 모두를 생각을 해야한다.
### 각 시작 노드에서 모든 노드로 갈 수 있는 최단 거리를 구한다.
### 최단 거리가 활동 반경보다 작을 경우 탐색가능한 아이템이다 .
### 즉 각 노드에서 다익스트라를 하고 얻을 수 있는 아이템에 최고 수를 구한다.
### 그중 가장 많은 아이템이 정답이다.


import sys
import heapq
INF = int(1e6)

def dijkstra(now,start):
    heap =[]
    dist[start]=0
    heapq.heappush(heap,[now,start])
    while heap:
        now_dist,now_node = heapq.heappop(heap)
        if dist[now_node]<now_dist:
            continue
        for next_dist,next_node in arr[now_node]:
            if dist[next_node]>now_dist+next_dist:
                dist[next_node]=now_dist+next_dist
                heapq.heappush(heap,[dist[next_node],next_node])

n,m,r = map(int,sys.stdin.readline().split())
item = list(map(int,sys.stdin.readline().split()))
arr = [[] for _ in range(n+1)]

## 노드 만들기(그래프 만들기)
for i in range(r):
    a,b,c=map(int,sys.stdin.readline().split())
    arr[a].append([c,b])
    arr[b].append([c,a])

## 노드별 최대 아이템 수
max_item=[0]*(n+1)

for i in range(1,n+1):
    dist = [INF] * (n + 1)
    dijkstra(0,i)
    for j in range(1,n+1):
        if dist[j]<=m:
            max_item[i]+=item[j-1]

print(max(max_item))