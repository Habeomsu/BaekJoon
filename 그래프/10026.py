import sys

sys.setrecursionlimit(10000000)
def dfs1(x,y,a):
    if x<=-1 or x>=n or y<= -1 or y>=n:
        return False
    if rgb[x][y]==a:
        rgb[x][y]=0
        dfs1(x-1,y,a)
        dfs1(x+1, y, a)
        dfs1(x , y+1, a)
        dfs1(x , y-1, a)
        return True
    return False

def dfs2(x,y,a):
    if x<=-1 or x>=n or y<= -1 or y>=n:
        return False
    if rb[x][y]==a:
        rb[x][y]=0
        dfs2(x-1,y,a)
        dfs2(x +1, y, a)
        dfs2(x , y+1, a)
        dfs2(x , y-1, a)
        return True
    return False
n =int(sys.stdin.readline())
rgb=[]
rb=[[0]*n for _ in range(n)]
for i in range(n):
    rgb.append(list(sys.stdin.readline().strip("\n")))
for i in range(n):
    for j in range(n):
        if rgb[i][j]=='G':
            rb[i][j]='R'
        else:
            rb[i][j]=rgb[i][j]
result1=0
result2=0
for i in range(n):
    for j in range(n):
        if dfs1(i,j,'R')==True:
            result1 +=1
        elif dfs1(i,j,'G')==True:
            result1 +=1
        elif dfs1(i,j,'B')==True:
            result1 +=1
for i in range(n):
    for j in range(n):
        if dfs2(i,j,'R')==True:
            result2 +=1
        elif dfs2(i,j,'B')==True:
            result2 +=1
print(result1,result2)