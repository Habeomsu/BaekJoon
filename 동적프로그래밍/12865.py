import sys

n,k=map(int,sys.stdin.readline().split())
w=[]
v=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    w.append(a)
    v.append(b)
dp=[[0]*(k+1) for _ in range(n+1)]
for i in range(k+1):
    dp[0][i]=0
for i in range(n+1):
    dp[i][0]=0
for i in range(1,n+1):
    for j in range(1,k+1):
        if j>=w[i-1]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
        else:
            dp[i][j]=dp[i-1][j]
Max=0
for i in range(1,n+1):
    if max(dp[i]) > Max:
        Max=max(dp[i])
print(Max)