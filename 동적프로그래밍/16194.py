import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))

dp=[0]*(n+1)
dp[1]=arr[0]
if n>1:
    for i in range(1,n+1):
        dp[i]=arr[i-1]
        for j in range(0,i):
            dp[i]=min(dp[i],dp[j]+arr[i-j-1])

print(dp[n])