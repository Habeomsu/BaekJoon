### 모든 노드에서 시작하여 dfs 로 거리를 구한다 ..
### 가장 긴 거리를 출력한다 ...
### 임의의 노드에서 특정 노드까지의 거리를 구하고 가장 큰 것부터 다시 구한다.

import sys

sys.setrecursionlimit(1000000)
node = int(sys.stdin.readline())

graph =[[] for _ in range(node+1)]

for i in range(node):
    data = list(map(int,sys.stdin.readline().split()))
    v = data[0]
    i = 1
    while data[i] != -1:
        graph[v].append([data[i+1],data[i]])
        i = i+2

def find_big(start, now):
    for a,b in graph[start]:
        if visit[b]==-1:
            visit[b]=a+now
            find_big(b,visit[b])

visit = [-1] * (node + 1)
visit[1] = 0
find_big(1,0)
max_idx = visit.index(max(visit))

visit = [-1] * (node + 1)
visit[max_idx] = 0
find_big(max_idx,0)

print(max(visit))