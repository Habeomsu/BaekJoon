from collections import deque

def solution(land):
    answer = 0
    num = 2
    result = {}
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:
                cnt = bfs(i, j, land, num)
                result[num] = cnt
                num += 1
    for i in range(len(land[0])):
        list = set()
        cnt = 0
        for j in range(len(land)):
            if (land[j][i] != 0):
                if land[j][i] not in list:
                    list.add(land[j][i])
        for k in list:
            cnt += result[k]
        if answer < cnt:
            answer = cnt
    return answer

def bfs(x, y, arr, num):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    que = deque()
    que.append([x, y])
    cnt = 1
    arr[x][y] = num
    while que:
        a, b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):
                if arr[nx][ny] == 1:
                    cnt += 1
                    que.append([nx, ny])
                    arr[nx][ny] = num
    return cnt

### bfs를 통해서 석유의 분포를 1씩 늘려가는 bfs를 만든다
### 집합을 통해서 1번 : 몇개, 2번 : 몇개 이런식으로 저장
### 그리고 최종적으로 1번 열에서 각각 다른