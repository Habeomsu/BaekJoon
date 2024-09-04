import sys

n=int(sys.stdin.readline())

def make1(n):
    dp=[0]*(n+1)
    dp[1]=0
    for i in range(2,n+1):
        dp[i]=dp[i-1]+1

        if i%2==0:
            dp[i]=min(dp[i//2]+1,dp[i])
        if i%3==0:
            dp[i]=min(dp[i//3]+1,dp[i])
    return dp[n]
print(make1(n))
