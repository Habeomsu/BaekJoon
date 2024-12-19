import sys

n=int(sys.stdin.readline())

dp=[[1]*10 for _ in range(n)]
result = 0
if n == 1:
    result= 10
else:
    for i in range(1,n):
        for j in range(10):
            dp[i][j]=sum(dp[i-1][j:])
    result=sum(dp[n-1])

print(result%10007)