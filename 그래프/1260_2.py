import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())

arr=[]
arr2=[[] for _ in range(N + 1)]
for i in range(M):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in arr:
    a,b=i
    arr2[a].append(b)
    arr2[b].append(a)
for i in range(N+1):
    arr2[i].sort()
result1=[]
result2=[]
visit1=[False]*(N+1)
visit2=[False]*(N+1)

def dfs(arr,v,visit):
    visit[v]=True
    result1.append(v)
    for i in arr[v]:
        if visit[i]==False:
            dfs(arr,i,visit)

def bfs(arr,v,visit):
    que=deque([v])
    visit[v]=True
    while que:
        a=que.popleft()
        result2.append(a)
        for i in arr[a]:
            if visit[i]==False:
                que.append(i)
                visit[i]=True

dfs(arr2,V,visit1)
bfs(arr2,V,visit2)

print(*result1)
print(*result2)