
import sys

N = int(sys.stdin.readline())

dragon = []
for i in range(N):
    dragon.append(list(map(int,sys.stdin.readline().split())))

dx = [1,0,-1,0]
dy = [0,-1,0,1]

board = [[0]*101 for _ in range(101)]

for i in dragon:
    x,y,d,g = i
    board[y][x] += 1
    now_g = 1
    arr_d = [d]
    x,y = x+dx[d], y+dy[d]
    board[y][x] += 1
    while now_g <= g:
        temp = arr_d[:]
        for j in temp[::-1]:
            next_d = (j + 1) % 4
            x,y = x+dx[next_d],y+dy[next_d]
            board[y][x] += 1
            arr_d.append(next_d)
        now_g += 1

def find(x,y):
    temp_dx= [1,0,1]
    temp_dy= [0,1,1]
    if board[y][x] == 0:
        return False
    else:
        for i in range(3):
            next_x = x + temp_dx[i]
            next_y = y + temp_dy[i]
            if board[next_y][next_x] == 0:
                return False
    return True

result = 0

for i in range(100):
    for j in range(100):
        if find(j,i):
            result += 1

print(result)



'''

1. 4방향을 구해준다
2. 다음세대의 좌표는 이전세대의 역순을 이용한다. -> 이전세대의 움직인 방향의 +1 을 해주면 된다.
3. 세대를 구하기 위해서 d 를 계속 저장해야한다.
4. d를 역순으로 꺼내와야한다.
5. 모든 좌표를 구하고 board를 처음부터 끝까지 순회한다.
6. 순회하면서 정사각형이 완성되면 결과값을 +1 해준다.



'''