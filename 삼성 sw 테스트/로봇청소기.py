import sys

N, M = map(int,sys.stdin.readline().split())
x,y,d = map(int,sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

result = 0

nx, ny = x,y

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 4방향 탐색
def find(x,y):
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny] == 0:
                return True
    return False

while True:
    if board[nx][ny] == 0:
        result += 1
        board[nx][ny] = -1

    if find(nx,ny):
        for i in range(4):
            d = (d - 1 + 4) % 4
            tx, ty = nx + dx[d], ny + dy[d]
            if board[tx][ty] == 0:
                nx,ny = tx,ty
                break
    else:
        nx,ny = nx+dx[(d+2)%4], ny+dy[(d+2)%4]
        if board[nx][ny] == 1:
            break

print(result)




'''

1. 방향이 (d) 가 0일 경우 북쪽 , 1일 경우 동쪽, 2일 경우 남쪽, 3일 경우 서쪽
    1.1 즉, dx,dy를 [북,동,남,서] 순으로 만들어 준다.
    1.2 만약 청소기가 반시계방향으로 돌 경우 -1을 해준다.
2. 청소기가 위치한 곳에 board값이 0일 경우 청소를 해준다. 그 후 -1로 변경해준다. ->  result += 1
3. 4방향 탐색을 해준다.
    3.1 0인 곳이 없을 경우
        3.1.1 방향(d)는 유지하고 뒤로 한칸 움직인다. dx[d+2],dy[d+2], 그 후 2번 실행
        3.1.2 만약 뒤에가 벽인 경우 -> 종료한다.
    3.2 0인 곳이 존재하는 경우
        3.2.1 반시계 방향으로 변경한다. d = (d - 1 + 4) % 4
        3.2.2 앞에 칸이 0 인 경우 전진한다. -> 그 후 2번 실행
        3.2.3 아닐 경우 3.2.1 로 돌아간다.
    




'''