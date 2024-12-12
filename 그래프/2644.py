import sys

n=int(sys.stdin.readline())
a,b=map(int,sys.stdin.readline().split())
m=int(sys.stdin.readline())
node = [[] for _ in range(n+1)]
for i in range(m):
    c,d=map(int,sys.stdin.readline().split())
    node[c].append(d)
    node[d].append(c)
result=[]
visit=[False]*(n+1)
def dfs(x,cnt):
    visit[x]=True
    cnt += 1
    if x == b:
        result.append(cnt)
    for i in node[x]:
        if visit[i]==False:
            dfs(i,cnt)
cnt=0
dfs(a,cnt)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)


