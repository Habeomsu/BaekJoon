import sys

n=int(sys.stdin.readline())
def fiv(n):
    dp=[0]*(n+1)
    if n==1:
        return 1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(fiv(n))
