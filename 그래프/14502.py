import sys
from collections import deque


def bfs():
    q = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx, ny))

def get_safe_area():
    safe_count = 0
    for i in range(n):
        safe_count += temp[i].count(0)
    return safe_count
def build_walls(count):
    global Max
    if count == 3:

        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]

        bfs()
        Max = max(Max, get_safe_area())
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                build_walls(count + 1)
                arr[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
Max = 0
temp = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

build_walls(0)
print(Max)