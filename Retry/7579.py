'''

DP를 이용한 풀이



'''


import sys

N , M = map(int,sys.stdin.readline().split())
byte = list(map(int,sys.stdin.readline().split()))
memo = list(map(int,sys.stdin.readline().split()))

max_memo = sum(memo)
dp = [[0]*(max_memo+1) for _ in range(N+1)]
result = max_memo

for i in range(1,N+1):
    now_byte = byte[i-1]
    now_memo = memo[i-1]
    for j in range(0,max_memo+1):
        if now_memo > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(now_byte+dp[i-1][j-now_memo],dp[i-1][j])
        if dp[i][j] >= M:
            result = min(result,j)
print(result)