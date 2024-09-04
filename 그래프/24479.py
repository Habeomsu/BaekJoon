def dfs(t):
    global cnt
    visited[t] = cnt
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)
for i in range(1,N+1):
    line[i].sort()
dfs(R)
for i in range(1, N+1):
    print(visited[i])
