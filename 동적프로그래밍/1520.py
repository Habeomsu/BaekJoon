import sys

sys_input = sys.stdin.readline

n, m = map(int, sys_input().split())

arr = [list(map(int, sys_input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dp = [[-1] * m for _ in range(n)]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] < arr[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
