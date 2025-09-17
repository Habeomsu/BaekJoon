import sys

N, L = map(int,sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

result = 0

def find(temp):
    now = 0
    move = 1
    last = temp[0]
    for i in range(1,N):
        now = temp[i]
        if now == last:
            move += 1
            last = now
        else:
            if now == last+1:
                if move >= L:
                    last = now
                    move = 1
                else:
                    return False
            elif now+1 == last:
                if i + L - 1 < N:
                    for j in range(i+1,i+L):
                        if now == temp[j]:
                            continue
                        else:
                            return False
                    move = 1 - L
                    last = now
                else:
                    return False
            else:
                return False
    return True

for i in range(N):
    if find(board[i]):
        result += 1

for j in range(N):
    temp = []
    for i in range(N):
        temp.append(board[i][j])
    if find(temp):
        result += 1

print(result)


'''


1. 기본은 자신의 높이를 확인하고 이동한 횟수를 변경한다. 이전 높이 = last , 이동 횟수 = move, 현재 높이 = now
2. 자신의 높이와 이전 높이가 다를 경우
    2.1 만약 현재 높이가 이전보다 클 경우, 이동한 횟수가 L 보다 크면 계속 진행한다.
    2.2 만약 현재 높이가 이전보다 작을 경우 이동 횟수를 초기화 한다. move를 L만큼 자신이 존재하는지 파악한다.
        2.2.1 만약 L만큼 자신의 높이와 같을 경우 내리막 길을 형성이 가능하다.
        2.2.2 만약 L만큼 자신의 높이가 없을 경우 불가능하다.
3. 자신의 높이와 이전 높이가 같을 경우 넘어간다.
4. 문제가 없으면 최종 답을 구한다.

'''