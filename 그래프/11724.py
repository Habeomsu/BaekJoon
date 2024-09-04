import sys

sys.setrecursionlimit(100000)
def dfs(x):
    if visit[x]==False:
        visit[x]=True
        for i in arr[x]:
            if visit[i]==False:
                dfs(i)
        return True
    return False

n,m=map(int,sys.stdin.readline().split())
arr=[[] for _ in range(n+1)]
visit=[False]*(n+1)
result=0
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,n+1):
    if dfs(i)==True:
        result +=1
print(result)