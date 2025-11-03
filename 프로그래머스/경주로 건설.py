from collections import deque


def solution(board):
    n = len(board)
    INF = int(1e9)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    que = deque()

    for i in [0, 1]:
        nx, ny = dx[i], dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
            visited[nx][ny][i] = 100
            que.append((nx, ny, i, 100))

    while que:
        x, y, dir, cost = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = cost + (100 if i == dir else 600)
                if new_cost < visited[nx][ny][i]:
                    visited[nx][ny][i] = new_cost
                    que.append((nx, ny, i, new_cost))

    return min(visited[n - 1][n - 1])


'''

1. bfs 를 이용한다.
2. 해당 위치에 방문 겸 이동 거리를 저장한다.
3. bfs시에 해당 자동차의 방향을 표시한다. 
4. 방향에 따라 비용이 달라진다.
    4.1 방향이 이전과 같으면 -> 직선 거리 (100)
    4.2 방향이 이전과 다르면 -> 코너 거리 (500)
5. 각 방향별로 어떻게 움직이는 지를 잘 판단하자

'''