import sys

def will(k,n):
    dp=[[0]*15 for _ in range(15)]
    for i in range(15):
        dp[0][i]=i
    for i in range(1,15):
        for j in range(1,15):
            dp[i][j]=dp[i][j-1]+dp[i-1][j]
    return dp[k][n]

n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())
    b=int(sys.stdin.readline())
    print(will(a,b))