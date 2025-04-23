'''

bfs를 통해서 미세먼지가 존재하는 칸을 찾는다.
모든 칸이 0 인 새로운 배열을 생성한다.
거기에 미세먼지 확산 과정을 진행한다.
그리고 공기 청정기 진행을 시작한다.

'''

import sys
from collections import deque

R, C, T = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

clean=[]
for i in range(R):
    if arr[i][0] == -1:
        clean.append(i)

def find_mise(arr):
    new_arr = [[0]*C for _ in range(R)]
    que = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] != 0 and arr[i][j] != -1:
                que.append((i,j))
    while que:
        x, y = que.popleft()
        cnt = 0
        mise = arr[x][y] // 5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <R and 0 <= ny <C and arr[nx][ny] != -1:
                new_arr[nx][ny] += mise
                cnt +=1
        new_arr[x][y] += (arr[x][y] - mise*cnt)
    return new_arr

def clean_mise(arr,start,end):
    # 윗방향 공기 청정기
    for i in range(start-1,0,-1):
        arr[i][0] = arr[i-1][0]
    for i in range(0,C-1):
        arr[0][i] = arr[0][i+1]
    for i in range(0,start):
        arr[i][C-1] = arr[i+1][C-1]
    for i in range(C-1,0,-1):
        arr[start][i] = arr[start][i-1]
    # 아랫 방향 공기 청정기
    for i in range(end+1,R-1):
        arr[i][0] = arr[i+1][0]
    for i in range(0,C-1):
        arr[R-1][i] = arr[R-1][i+1]
    for i in range(R-1,end,-1):
        arr[i][C-1] = arr[i-1][C-1]
    for i in range(C-1,0,-1):
        arr[end][i] = arr[end][i-1]
    return arr

def count_mise(arr):
    sum = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] != -1 and arr[i][j] != 0:
                sum += arr[i][j]
    return sum

cnt = 0
while cnt != T:
    new_arr = find_mise(arr)
    new_arr = clean_mise(new_arr,clean[0],clean[1])
    new_arr[clean[0]][0] = -1
    new_arr[clean[1]][0] = -1
    arr = new_arr
    cnt +=1

print(count_mise(arr))

