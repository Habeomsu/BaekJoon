### 트리의 시작에서 가장 거리가 먼 노드를 찾는다 ..
### 해당 노드에서 가장 거리가 먼 노드를 찾는다

import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]

for i in range(N-1):
    a,b,c=map(int,sys.stdin.readline().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def dfs(start,now):
    for (a,b) in tree[start]:
        if visit[a]==-1:
            visit[a]=now+b
            dfs(a,visit[a])

visit = [-1]*(N+1)
visit[1]=0
dfs(1,0)

start = visit.index(max(visit))
visit=[-1]*(N+1)
visit[start]=0
dfs(start,0)

print(max(visit))