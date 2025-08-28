import sys

apple = []
move = {}

## 입력
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

for i in range(k):
    x1, y1 = map(int,sys.stdin.readline().split())
    apple.append((x1, y1))

l = int(sys.stdin.readline())

for i in range(l):
    x , c = sys.stdin.readline().split()
    move[int(x)] = c

## 이동 방향 오른쪽,아래,왼쪽,위 ( 0,1,2,3 ) -> D 이동시 +1, L 이동시 -1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

## 머리와 꼬리의 이동방향 및 좌표
head = 0
tail = 0

head_loc = [0,0]
tail_loc = [0,0]

## 변경 위치 딕셔너리
change_dict = {}

## 전체 판 0-> 빈 공간, 1-> 뱀이 차지하는 공간, 2-> 사과가 있는 공간
board = [[0]*n for _ in range(n)]

for i in apple:
    x1,y1 = i
    board[x1-1][y1-1] = 2

total_sec = 0

board[0][0] = 1

while True:
    total_sec += 1
    head_nx,head_ny = head_loc[0] + dx[head], head_loc[1] + dy[head]

    ## 다음 위치가 벽인 경우와 몸인 경우 while 종료
    if (0 > head_nx or n <= head_nx) or (0>head_ny or n <= head_ny):
        break
    if board[head_nx][head_ny] == 1:
        break

    ## 헤드의 포인터 변경
    head_loc[0], head_loc[1] = head_nx, head_ny

    ## 다음칸이 빈칸인 경우
    if board[head_nx][head_ny] == 0:
        board[tail_loc[0]][tail_loc[1]] = 0

        if (tail_loc[0], tail_loc[1]) in change_dict:
            tail = (tail + change_dict[(tail_loc[0], tail_loc[1])] + 4) % 4
            change_dict[(tail_loc[0], tail_loc[1])] = 0

        tail_loc = (tail_loc[0] + dx[tail], tail_loc[1] + dy[tail])

    ## 다음칸 이동 처리
    board[head_nx][head_ny] = 1

    ## 방향 변경 후 꼬리를 위해 change_dict 생성
    if total_sec in move:
        di = move[total_sec]
        if di == 'L':
            head = (head + 3) % 4
            change_dict[(head_nx,head_ny)] = -1
        elif di == 'D':
            head = (head + 1 ) % 4
            change_dict[(head_nx, head_ny)] = 1

print(total_sec)

'''

1. 처음 뱀의 위치는 1,1 이다. 또한, 뱀은 오른쪽으로 이동을 한다. -> 머리가 위치한 좌표를 board 배열에서 1로 변경한다.
    1.1 이동방향은 오른쪽 -> y+1, 왼쪽 -> y-1, 위 -> x-1, 아래 -> x+1
    1.2 상,하,좌,우 순서를 잘 해주어야 방향을 변경할때 규칙이 생긴다. -> 오른쪽을 기준으로 시계방향으로 1씩 증가한다. 
    1.3 오른쪽, 아래, 왼쪽, 위 순으로 배치를 해준다. -> 만약, L 일 경우 -1, D 일 경우 +1 해준다.
    1.4 현재 이동 방향 변수를 생성해준다. 단, 머리부분과 꼬리부분 둘다 생성해주어야한다.
    1.5 만약, 머리의 이동 방향이 변경되면, 변경된 위치를 변경 딕셔너리에 넣어준다. (x,y) : 1 or -1 
2. 먼저 뱀을 이동시킨다. -> 한번 움직일 때 마다 초를 증가시킨다. -> sec = sec + 1
3. 만약, 해당 위치가 자신의 몸, 벽인 경우에는 종료한다.
4. 뱀이 이동후 사과가 있냐 없냐를 판단한다.
    4.1 만약, 이동후 사과가 존재하면, 꼬리 부분은 움직이지 않는다.
    4.2 만약, 이동후 사과가 없으면, 꼬리 부분도 움직인다. -> 해당 꼬리의 위치가 변경 딕셔너리에 존재하면 꼬리 이동 방향을 변경한다.
    4.3 꼬리가 이동시 보드판에 자신의 이전 위치를 0으로 변경한다. 




'''