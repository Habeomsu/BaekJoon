import sys
arr=[]
question=[]
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(m):
    question.append(list(map(int,sys.stdin.readline().split())))

dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i][j]=arr[i-1][j-1]+dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
for x1,y1,x2,y2 in question:
    result= dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
    print(result)