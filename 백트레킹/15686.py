import sys

# 입력 받기
m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# 치킨집과 집 위치 저장
chicken_locations = []
house_locations = []

for i in range(m):
    for j in range(m):
        if arr[i][j] == 1:  # 집
            house_locations.append((i, j))
        elif arr[i][j] == 2:  # 치킨집
            chicken_locations.append((i, j))

# 최소 거리 저장 변수
min_dist = float('inf')
selected_chickens = []  # 선택된 치킨집 좌표

# 백트래킹 함수
def backtrack(start):
    global min_dist

    # 치킨집 n개를 선택한 경우 거리 계산
    if len(selected_chickens) == n:
        total_distance = 0

        # 각 집에서 가장 가까운 치킨집 거리 찾기
        for hx, hy in house_locations:
            min_distance = float('inf')
            for cx, cy in selected_chickens:
                min_distance = min(min_distance, abs(hx - cx) + abs(hy - cy))
            total_distance += min_distance

            # 현재 최소 거리보다 크면 더 이상 탐색하지 않음 (가지치기)
            if total_distance >= min_dist:
                return

        min_dist = min(min_dist, total_distance)
        return

    # 백트래킹으로 치킨집 선택
    for i in range(start, len(chicken_locations)):
        selected_chickens.append(chicken_locations[i])
        backtrack(i + 1)  # 다음 치킨집 선택
        selected_chickens.pop()  # 원래 상태로 복구

# 백트래킹 시작
backtrack(0)

print(min_dist)
