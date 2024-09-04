import sys

sys.setrecursionlimit(100000)
def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y >=m:
        return False
    if arr[x][y]==1:
        arr[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

num=int(sys.stdin.readline())
for i in range(num):
    m,n,k=map(int,sys.stdin.readline().split())
    result=0
    arr=[[0]*m for _ in range(n)]
    for j in range(k):
        x,y=map(int,sys.stdin.readline().split())
        arr[y][x]=1
    for k in range(n):
        for l in range(m):
            if dfs(k,l)==True:
                result +=1
    print(result)