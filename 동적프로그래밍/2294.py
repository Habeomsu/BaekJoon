import sys

n,k = map(int,sys.stdin.readline().split())

arr =[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

INF = int(1e9)

dp=[INF]*(k+1)
dp[0]=0

for i in arr:
    for j in range(i,k+1):
        dp[j] = min(dp[j-i]+1,dp[j])
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])