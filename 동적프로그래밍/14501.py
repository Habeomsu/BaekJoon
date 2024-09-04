import sys

n=int(sys.stdin.readline())
t=[]
p=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    t.append(a)
    p.append(b)
dp=[0]*(n+1)
for i in range(n):
    dp[i+1]=max(dp[i+1],dp[i])

    if i+t[i]<=n:
        dp[i+t[i]] = max(dp[i+t[i]],dp[i]+p[i])
print(dp[n])