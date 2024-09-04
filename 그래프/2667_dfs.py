import sys

def dfs(x,y):
    global cnt
    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False

    if arr[x][y]==1:
        arr[x][y] =-1
        cnt+=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False



n=int(sys.stdin.readline())
arr=[]
result=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().strip("\n"))))

for i in range(n):
    for j in range(n):
        cnt=0
        if dfs(i,j)==True:
            result.append(cnt)

result=sorted(result)
print(len(result))
print(*result,sep="\n")
