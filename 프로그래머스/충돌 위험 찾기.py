def solution(points, routes):
    answer = 0
    for i in routes:
        start, end = i
        start_x, start_y = points[start - 1]
        end_x, end_y = points[end - 1]
        arr = []
        arr.append([start_x, start_y])
        while start_x != end_x:
            if start_x > end_x:
                start_x = start_x - 1
            else:
                start_x = start_x + 1
            arr.append([start_x, start_y])
        while start_y != end_y:
            if start_y > end_y:
                start_y = start_y - 1
            else:
                start_y = start_y + 1
            arr.append([start_x, start_y])
        print(arr)
    return answer

### 상하좌우중 상하를 먼저 움직인다.
### 각 로봇의 최단거리를 먼저 구해서 해당 배열을 만들고
### 같은 시간으로 위치가 같은 것이 있는지 파악한다
### 문제는 뭐냐 ?? 최단거리를 어떻게 구하냐 이다 ...
### 현재 좌표랑 이동할 좌표를 기준으로 처음엔 x값을 같게 만들고 그다음엔 y값을 같게 만드는게 최단거리다.
