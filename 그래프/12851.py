### 3가지 방법으로 bfs를 시작한다.  (x-1, x+1, x*2)
### while을 돌리는데 조건을 만약에 이동횟수를 계속 부여해서 원하는 목표까지 도달했을 시...
### 이동횟수보다 커지면 그만하게 하고 최종 방문 가능한 횟수도 구한다.
### bfs를 통해서 원하는 위치에 도달할 경우 그때에 움직인 거리가 최단거리야 그리고 그 때 남아있는 큐는 해당 좌표로 이동 가능하면
### 방문 여부와 방문하면 이동한 거리를 저장해준다.
### 중복으로 이동이 가능하면 안된다 ... 그럼 무한 루프가 걸린다 단 ...
### 히지만 방문할 위치가 방문했는데 현재 위치에서 이동횟수 +1 이 = 다음위치에 이동횟수와 같으면 que에 푸쉬


import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
sum = 0
result=0
visit=[0]*100001
def bfs(start):
    global sum,result
    que=deque()
    que.append(start)
    while que:
        a=que.popleft()
        temp = visit[a]
        if a==K:
            result=temp
            sum +=1
            continue

        for nx in (a+1,a-1,a*2):
            if 0<=nx<100001 and (visit[nx]==0 or visit[nx]==visit[a]+1):
                visit[nx]=visit[a]+1
                que.append(nx)

bfs(N)

print(result)
print(sum)
