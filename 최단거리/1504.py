
### 주어진 2개의 정점은 꼭 지나가야한다
### 이동할 때 왔던 점도 지나가는게 가능하다
### 2차원 배열을 생성하고 배열을 채워준다
### 1에서 N으로 이동 가능한 모든 경우를 구해준다
### 이동한 정점을 표시할 배열을 선언한다
## 해당 위치에서 가장 거리가 짧은 노드로 이동한다
## 이동 배열중 2개의 정점을 가지고있고 목적지 정점일 경우 종료한다.
### 1 -> v1 -> v2 -> N
### 1 -> v2 -> v1 -> N
### start를 1 로 잡고 v1,v2 으로가는 최소 거리를 구한다.
### start를 v1 으로 잡고 v2, N 으로 가는 최소 거리를 구한다.
### start를 v2 으로 잡고 v1, N 으로 가는 최소 거리를 구한다.


import sys
import heapq
INF = int(1e9)

def dijkstra(start):
    hq =[]
    heapq.heappush(hq,[0,start])
    distance[start]=0
    while hq:
        now_dist,now_node = heapq.heappop(hq)
        if now_dist > distance[now_node]:
            continue
        for next_v in arr[now_node]:
            next_dist = now_dist + next_v[0]
            if next_dist<distance[next_v[1]]:
                distance[next_v[1]]=next_dist
                heapq.heappush(hq,[next_dist,next_v[1]])

N,E = map(int,sys.stdin.readline().split())

arr = [[] for i in range(N+1)]

for i in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    arr[a].append([c,b])
    arr[b].append([c,a])

v1,v2 = map(int,sys.stdin.readline().split())

distance=[INF]*(N+1)
dijkstra(1)

## 1 -> v1 , 1 -> v2 가는 최소 거리
final_dist=[INF,INF]
if(distance[v1]!=INF and distance[v2]!=INF and distance[N]!=INF):
    final_dist[0]=distance[v1]
    final_dist[1]=distance[v2]
else:
    print(-1)
    exit()
distance=[INF]*(N+1)
dijkstra(v1)

## v1 -> v2, v1 -> N 으로 가는 최소 거리
if(distance[v2]!=INF and distance[N]!=INF):
    final_dist[0] += distance[v2]
    final_dist[1] += distance[N]
else:
    print(-1)
    exit()

distance=[INF]*(N+1)
dijkstra(v2)

if(distance[v1]!=INF and distance[N]!=INF):
    final_dist[0] += distance[N]
    final_dist[1] += distance[v1]
else:
    print(-1)
    exit()

print(min(final_dist))
