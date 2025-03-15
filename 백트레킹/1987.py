import sys

R, C = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for _ in range(R)]

visited = [False]*26  # 알파벳 방문 여부 (A~Z)
dx = [0,0,1,-1]
dy = [1,-1,0,0]
max_len = 1

def dfs(x, y, count):
    global max_len
    max_len = max(max_len, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            alpha = board[nx][ny]
            idx = ord(alpha) - ord('A')
            if not visited[idx]:
                visited[idx] = True
                dfs(nx, ny, count + 1)
                visited[idx] = False  # backtracking

start_alpha = board[0][0]
visited[ord(start_alpha) - ord('A')] = True
dfs(0, 0, 1)

print(max_len)
