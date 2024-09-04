import sys

def dfs(R):
    visit[R]=True
    result[R]+=1
    for i in node[R]:
        if visit[i] ==False:
            dfs(i)

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
node=[[] for _ in range(n+1)]
visit=[False]*(n+1)
result = [0]*(n+1)
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
dfs(1)
sum=0
for i in range(2,n+1):
    if result[i] !=0:
        sum+=1
print(sum)