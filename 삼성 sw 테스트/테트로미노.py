import sys

N,M = map(int,sys.stdin.readline().split())
board = []

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

result = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = 0

visitied = [[0]*M for _ in range(N)]


def back(x,y,visit,sum,cnt):
    global result
    if cnt == 4:
        if result < sum:
            result = sum
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >=0 and nx <N and ny >=0 and ny <M and visit[nx][ny] == 0:

            if cnt == 2:
                visit[nx][ny] = 1
                back(x, y, visit, sum + board[nx][ny], cnt + 1)
                visit[nx][ny] = 0

            visit[nx][ny] = 1
            back(nx,ny,visit,sum + board[nx][ny],cnt + 1)
            visit[nx][ny] = 0

    ## ㅗ 모양 만들기, 그 자리에서 한번더 back() 함수 실행
    # if cnt == 2:
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if nx >= 0 and nx < N and ny >= 0 and ny < M and visit[nx][ny] == 0:
    #             visit[nx][ny] = 1
    #             back(x,y,visit,sum + board[nx][ny],cnt + 1)
    #             visit[nx][ny] = 0

for i in range(N):
    for j in range(M):
        temp = visitied
        temp[i][j] = 1
        total = board[i][j]
        back(i,j,temp,total,1)
        temp[i][j] = 0

print(result)


'''

1. 4칸으로 가능한 모든 경우의 수를 벡트래킹을 이용해서 만드는 방법
2. 벡트래킹 함수를 만들어준다. -> back()
3. 백트래킹 시 cnt에 따라 값을 반환한다. 
    3.1. cnt == 2 일 경우 -> ㅗ 모양을 만들어야한다.
    3.2. cnt == 4 일 경우 -> 종료한다.
4. board 의 전체를 돌아가면서 백트래킹을 실행한다.





'''