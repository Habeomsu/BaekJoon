import sys

N, M = map(int,sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

cctv_arr = []

for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv_arr.append((i,j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cctv_idx = [[[0],[1],[2],[3]],[(0,2), (1,3)],[(0,1), (1,2), (2,3), (0,3)],[(0,1,2), (1,2,3), (0,2,3), (0,1,3)],[(0,1,2,3)]]

total = N*M

def back(board,idx):
    global total
    if idx == len(cctv_arr):
        result = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    result +=1
        if result < total:
            total = result
        return

    x,y = cctv_arr[idx]

    cctv_num = board[x][y]

    for i in cctv_idx[cctv_num-1]:
        temp_board = [row[:] for row in board]
        for j in i:
            nx, ny = x, y
            while True:
                nx,ny = nx+dx[j], ny + dy[j]
                if 0 > nx or N <= nx or 0 > ny or M <=ny:
                    break
                if temp_board[nx][ny] == 6:
                    break
                if 1 <= temp_board[nx][ny] <= 5:
                    continue
                if temp_board[nx][ny] == 0:
                    temp_board[nx][ny] = -1
        back(temp_board,idx+1)


back(board,0)

print(total)


'''


1. cctv의 번호에 따라 볼 수 있는 경우에 수가 달라진다.
    1.1 1번인 경우 -> [0,1,2,3]
    1.2 2번인 경우 -> [(0,2), (1,3)]
    1.3 3번인 경우 -> [(0,1), (1,2), (2,3), (0,3)]
    1.4 4번인 경우 -> [(0,1,2), (1,2,3), (0,2,3), (0,1,3)]
    1.4 5번인 경우 -> [(0,1,2,3)]
2. board 에서 0,6이 아닌 수를 찾아 둔다. -> cctv_arr
3. cctv_arr 를 백트레킹을 통해 모든 경우의 수를 구해준다.
    3.1 사각지대 아닌 경우는 -1을 이용한다.
    3.2 cctv에 감시 범위는 벽(6)을 만나거나 board의 범위를 벗어날 경우이다.

4. 그 중 가장 사각지대가 적은 경우를 반환한다.





'''