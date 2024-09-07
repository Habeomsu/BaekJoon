import sys

sys.setrecursionlimit(1000000)
n=int(sys.stdin.readline())
node=[[] for _ in range(n+1)]
visit=[False]*(n+1)
result=[0]*(n+1)
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
def dfs(x):
    visit[x] = True
    for i in node[x]:
        if visit[i] == False:
            result[i]=x
            dfs(i)
dfs(1)
print(*result[2:],sep="\n")
