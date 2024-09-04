import sys
from collections import deque

def bfs(X):

    q=deque([X])
    visit[X]=True
    result[X]=0
    while len(q)!=0:
        a=q.popleft()
        for i in node[a]:
            if visit[i] == False:
                visit[i]=True
                result[i]=result[a]+1
                q.append(i)

N,M,K,X = map(int,sys.stdin.readline().split())
node=[[] for _ in range(N+1)]
visit=[False]*(N+1)
result=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
cnt =0
bfs(X)
P=False
for i in range(1,N+1):
    if result[i]==K:
        P=True
        print(i)
if P == False:
    print(-1)