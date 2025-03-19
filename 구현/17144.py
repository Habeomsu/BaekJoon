### 미세먼지는 상,하,좌,우 확산한다 .. -> bfs, dfs 를 통해서 1초 미세먼지를 구한다.
### 조건은 0 <= nx < r , 0 <= ny < c , arr[nx][ny] != -1
### 공기 청정기를 어떻게 구할까 ...
### 미세먼지는 동시에 확장한다...

import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 공기청정기 위치 찾기 (첫 번째 열에 -1이 있는 두 행)
purifiers = []
for i in range(R):
    if arr[i][0] == -1:
        purifiers.append(i)
upper = purifiers[0]  # 윗공기청정기 위치
lower = purifiers[1]  # 아랫공기청정기 위치


def diffuse(arr):
    """미세먼지 확산을 동시 진행 (보조 배열 사용)"""
    new_arr = [[0] * C for _ in range(R)]
    # 공기청정기 위치는 그대로 -1로 복사
    new_arr[upper][0] = -1
    new_arr[lower][0] = -1

    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                spread = arr[i][j] // 5
                count = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        new_arr[ni][nj] += spread
                        count += 1
                new_arr[i][j] += arr[i][j] - spread * count
            elif arr[i][j] != -1:
                new_arr[i][j] += arr[i][j]
    return new_arr


def clean(arr, upper, lower):
    """공기청정기 작동 (윗부분: 반시계, 아랫부분: 시계 방향)"""
    # 윗부분 (반시계 방향)
    # 위쪽 이동: upper행의 위쪽 부분, 0열
    for i in range(upper - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    arr[upper][0] = -1  # 공기청정기 자리 유지

    # 왼쪽 이동: 맨 위 행
    for j in range(0, C - 1):
        arr[0][j] = arr[0][j + 1]
    # 오른쪽 이동: 0열 오른쪽 끝
    for i in range(0, upper):
        arr[i][C - 1] = arr[i + 1][C - 1]
    # 아래쪽 이동: upper행, 오른쪽 끝부터 왼쪽으로 이동
    for j in range(C - 1, 1, -1):
        arr[upper][j] = arr[upper][j - 1]
    arr[upper][1] = 0  # 공기청정기에서 나오는 깨끗한 공기

    # 아랫부분 (시계 방향)
    # 아래쪽 이동: lower행의 아래쪽 부분, 0열
    for i in range(lower + 1, R - 1):
        arr[i][0] = arr[i + 1][0]
    arr[lower][0] = -1  # 공기청정기 자리 유지

    # 왼쪽 이동: 맨 아래 행
    for j in range(0, C - 1):
        arr[R - 1][j] = arr[R - 1][j + 1]
    # 위쪽 이동: 맨 오른쪽 열
    for i in range(R - 1, lower, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    # 오른쪽 이동: lower행, 오른쪽 끝부터 왼쪽으로 이동
    for j in range(C - 1, 1, -1):
        arr[lower][j] = arr[lower][j - 1]
    arr[lower][1] = 0  # 정화된 공기
    return arr


# T초 동안 시뮬레이션
for _ in range(T):
    arr = diffuse(arr)
    arr = clean(arr, upper, lower)

# 남은 미세먼지의 총합 (공기청정기(-1)는 제외)
total = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            total += arr[i][j]

print(total)
