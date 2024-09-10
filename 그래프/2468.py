import sys

sys.setrecursionlimit(100000)

def dfs(x,y,i):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if arr[x][y] >i and visit[x][y]==False:
        visit[x][y]=True
        dfs(x-1,y,i)
        dfs(x+1,y,i)
        dfs(x,y-1,i)
        dfs(x,y+1,i)
        return True
    return False
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
Max=0
for i in arr:
    Max=max(max(i),Max)
total =0
for i in range(0,Max+1):
    result=0
    visit = [[False] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            if dfs(j,k,i)==True:
                result += 1
    total = max(total, result)
print(total)