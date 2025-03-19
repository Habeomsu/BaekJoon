### 일단 웜홀에 대한 조건을 따진다...
### 웜홀은 단방향 이기 때문에 모든 x 에서 웜홀 까지 오는 거리를 구하고 만약 옴훨에서 x까지의 거리가 이전 수보다 크면 yes
### 웜홀을 꺼내 그리고 만약 해당 위치에서
import sys

INF = int(1e9)

def bf(start):
    for i in range(N):
        for a,b,c in graph:
            if distance[b]>distance[a]+c:
                distance[b]=distance[a]+c
                if i ==N-1:
                    return False
    return True

Tc = int(sys.stdin.readline())
for i in range(Tc):
    N,M,W = map(int,sys.stdin.readline().split())
    graph = []
    for i in range(M):
        a,b,c = map(int,sys.stdin.readline().split())
        graph.append((a,b,c))
        graph.append((b,a,c))
    for i in range(W):
        a,b,c = map(int,sys.stdin.readline().split())
        graph.append((a,b,-c))
    distance=[INF]*(N+1)
    distance[1]=0
    if bf(1) == False:
        print('YES')
    else:
        print('NO')
