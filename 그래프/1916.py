import sys
import heapq
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = int(1e9)

result =[INF]*(n+1)
node=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    node[a].append((c,b))

start , end = map(int,sys.stdin.readline().split())
result[start]=0

heap = []
heapq.heappush(heap,[0,start])

while heap:
    cost,now = heapq.heappop(heap)

    if(result[now] < cost):
        continue

    for city in node[now]:
        new_cost, new_now = city[0],city[1]
        up_cost = new_cost + cost
        if (up_cost < result[new_now]):
            result[new_now] = up_cost
            heapq.heappush(heap,[up_cost,new_now])

print(result[end])
    