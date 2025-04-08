import sys
import heapq

INF = int(1e9)
n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

def dijktra(start):
    dist = [INF]*(n+1)
    dist[start] = 0
    que =[]
    heapq.heappush(que,(0,start))
    while que:
        now_dist,now_node = heapq.heappop(que)
        if dist[now_node] < now_dist:
            continue
        for i in graph[now_node]:
            next_dist,next_node = i
            if dist[next_node] > now_dist + next_dist:
                dist[next_node] = now_dist + next_dist
                heapq.heappush(que,(dist[next_node],next_node))

    return dist

arr1 = dijktra(1)
idx = arr1.index(max(arr1[1:]))
result = dijktra(idx)

print(max(result[1:]))