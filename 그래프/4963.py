import sys
sys.setrecursionlimit(10000000)
while True:
    a,b=map(int,sys.stdin.readline().split())
    result =0
    if a==0 and b==0:
        break
    arr=[]
    for i in range(b):
        arr.append(list(map(int,sys.stdin.readline().split())))
    visit=[[False]*a for _ in range(b)]
    def dfs(x,y):
        if x<0 or x>=b or y<0 or y>=a:
            return False
        if visit[x][y]==False and arr[x][y]==1:
            visit[x][y]=True
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x+1,y-1)
            dfs(x-1,y+1)
            dfs(x-1,y-1)
            return True
        return False
    for i in range(b):
        for j in range(a):
            if dfs(i,j)==True:
                result +=1
    print(result)