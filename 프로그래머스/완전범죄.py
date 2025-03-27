def solution(info, n, m):
    answer = -1
    dp = [[False]*m for _ in range(n)]
    dp[0][0] = True
    for a,b in info:
        new_dp = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if dp[i][j] == False:
                    continue
                if i+a<n:
                    new_dp[i+a][j] = True
                if j+b<m:
                    new_dp[i][j+b] = True
        dp = [row[:] for row in new_dp]
    for i in range(n):
        for j in range(m):
            if dp[i][j]==True:
                return i
    return answer