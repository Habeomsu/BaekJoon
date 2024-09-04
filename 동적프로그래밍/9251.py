import sys

a=sys.stdin.readline().strip("\n")
b=sys.stdin.readline().strip("\n")
c=len(a)
d=len(b)
dp=[[0]*(d+1) for _ in range(c+1)]
for i in range(1,c+1):
    for j in range(1,d+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[c][d])
