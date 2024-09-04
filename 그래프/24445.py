from collections import deque
import sys

def bfs(R):
    global cnt
    q=deque([R])
    visit[R]=True
    while len(q)!=0:
        a=q.popleft()
        result[a]=cnt
        cnt+=1
        for i in node[a]:
            if visit[i]==False:
                q.append(i)
                visit[i]=True

N,M,R = map(int,sys.stdin.readline().split())
node=[[] for _ in range(N+1)]
visit=[False]*(N+1)
result=[0]*(N+1)
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
for i in range(N+1):
    node[i].sort(reverse=True)
cnt=1
bfs(R)
print(*result[1:],sep="\n")