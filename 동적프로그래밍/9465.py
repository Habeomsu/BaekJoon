import sys

t=int(sys.stdin.readline())
for i in range(t):
    n=int(sys.stdin.readline())
    arr=[]
    for j in range(2):
        arr.append(list(map(int,sys.stdin.readline().split())))
    dp=[[0]*n for _ in range(2)]
    dp[0][0]=arr[0][0]
    dp[1][0]=arr[1][0]
    for k in range(1,n):
        dp[0][k]=max(dp[1][k-1]+arr[0][k],dp[0][k-1])
        dp[1][k]=max(dp[0][k-1]+arr[1][k],dp[1][k-1])
    print(max(dp[0][n-1],dp[1][n-1]))