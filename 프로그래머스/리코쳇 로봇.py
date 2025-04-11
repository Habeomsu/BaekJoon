from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start_x, start_y = i, j

    def bfs():
        que = deque()
        visit = [[0] * len(board[0]) for _ in range(len(board))]
        que.append([start_x, start_y])
        visit[start_x][start_y] = 1
        while que:
            x, y = que.popleft()
            if board[x][y] == 'G':
                return visit[x][y] - 1
            for i in range(4):
                nx, ny = x, y
                while True:
                    tx = nx + dx[i]
                    ty = ny + dy[i]
                    if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] != 'D':
                        nx, ny = tx, ty
                    else:
                        break
                if visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    que.append([nx, ny])
        return -1

    answer = bfs()

    return answer


'''

di 0 -> 상 , 1 -> 하, 2 -> 좌 , 3-> 우
결과값이 -1 인 경우는 G 주변(4방향)에 . 이나 벽이 없을경우이다.
방향 탐색을 계속하게 하는건 어떻게 하지 ..

'''