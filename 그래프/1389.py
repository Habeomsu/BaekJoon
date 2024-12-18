import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())

node = [[] for _ in range(n+1)]

for i_ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)

def bfs(x):
    visit=[False]*(n+1)
    result=[0]*(n+1)
    que = deque()
    que.append(x)
    visit[x]=True
    while que:
        q=que.popleft()
        for i in node[q]:
            if visit[i]==False:
                result[i]= result[q]+1
                visit[i]=True
                que.append(i)
    sum=0
    for i in result:
        sum+=i
    return sum
result=[]
for i in range(1,n+1):
    result.append(bfs(i))
Min=min(result)
index=result.index(Min)
print(index+1)

