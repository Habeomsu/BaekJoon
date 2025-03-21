### 방향은 x+1, x-1 , x *2 이다
### 만약 x*2 일경우 dp[x*2] = dp[x] 이다

### 0 - 1 bfs 이다 ...
### 가중치가 0 인 것은 왼쪽에서 빼준다 .. 왜 ?

import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
arr = deque()
arr.append(N)
INF=int(1e9)
visit =[INF]*(100001)
visit[N]=0
while len(arr)>0:
    x = arr.popleft()
    if x == K:
        break
    for i in (x-1,x+1,x*2):
        if 0 <= i < 100001:
            if i == x*2:
                if visit[i] > visit[x]:
                    visit[i] = visit[x]
                    arr.appendleft(i)
            else:
                if visit[i] > visit[x] + 1:
                    visit[i] = visit[x] + 1
                    arr.append(i)

print(visit[K])