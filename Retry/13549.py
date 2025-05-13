'''

bfs 를 통해서 최단 시간을 구한다.
1. 좌 + 우 + *2 를 통해 방향을 정한다
2. 목표 위치에 도달할시 dp값을 반환한다.
3. 순간 이동 -> dp[x*2] = dp[x]
4. 좌, 우 -> dp[x-1] or dp[x+1] = min(dp[x] + 1, dp[x])
5. 루프 조건 -> dp[x+1] or dp[x-1] <= dp[x]

'''

import sys
from collections import deque

INF = int(1e9)

N, K = map(int,sys.stdin.readline().split())

dp = [INF]*(100001)
def find_sis(x):
    que = deque()
    dp[x]=0
    que.append(x)
    while que:
        now = que.popleft()
        if now == K:
            return dp[now]
        for i in (now*2,now+1,now-1):
            if 0<=i and i<100001:
                if i == now*2:
                    if dp[i] > dp[now]:
                        dp[i] = dp[now]
                        que.append(i)
                else:
                    if dp[i] > dp[now]+1:
                        dp[i] = min(dp[i],dp[now]+1)
                        que.append(i)
print(find_sis(N))