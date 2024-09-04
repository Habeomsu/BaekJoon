import sys

sys.setrecursionlimit(1000001)
def dfs(R):
    global cnt
    visit[R]=True
    result[R]=cnt
    cnt+=1
    for i in node[R]:
        if visit[i]==False:
            dfs(i)

N,M,R=map(int,sys.stdin.readline().split())
node=[[] for _ in range(N+1)]
visit=[False]*(N+1)
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
for i in range(N+1):
    node[i].sort(reverse=True)
cnt=1
result=[0]*(N+1)
dfs(R)
print(*result[1:],sep="\n")