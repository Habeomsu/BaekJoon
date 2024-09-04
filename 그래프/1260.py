import sys
from collections import deque

def dfs(k):
    visit1[k]=True
    result1.append(k)
    for i in node[k]:
        if visit1[i]==False:
            dfs(i)

def bfs(k):
    q=deque([k])
    visit2[k]=True
    while len(q)!=0:
        v=q.popleft()
        result2.append(v)
        for i in node[v]:
            if visit2[i]==False:
                q.append(i)
                visit2[i]=True

n,m,k=map(int,sys.stdin.readline().split())
node=[[] for _ in range(n+1)]
visit1=[False]*(n+1)
visit2=[False]*(n+1)
result1=[]
result2=[]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)
for i in range(n+1):
    node[i].sort()
dfs(k)
bfs(k)
print(*result1)
print(*result2)