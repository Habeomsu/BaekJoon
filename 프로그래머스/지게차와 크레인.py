def solution(storage, requests):
    answer = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    storage = [list("0" + i + "0") for i in storage]
    storage.insert(0, list("0" * len(storage[0])))
    storage.append(list("0" * len(storage[0])))
    for i in requests:
        if len(i) == 1:
            fork(storage, i)
        else:
            crane(storage, i[0])
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] != '0' and storage[i][j] != '1':
                answer += 1
    return answer


def fork(storage, box):
    arr = []
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if storage[nx][ny] == '0':
                        arr.append([i, j])
                        break
    for a, b in arr:
        storage[a][b] = '0'
        find_zero(storage, a, b)


def crane(storage, box):
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] == box:
                storage[i][j] = '1'
                find_zero(storage, i, j)


def find_zero(storage, x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    isout = False
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if storage[nx][ny] == '0':
            storage[x][y] = '0'
            isout = True
    if isout:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if storage[nx][ny] == '1':
                storage[nx][ny] = '0'
                find_zero(storage, nx, ny)

### 알파벳이 한번만 쓰인 경우 -> 해당 위치에서 상하좌우에 0이 거나, i,j중 하나라도 0일 경우
### 알파벳이 반복된 경우 : for 문을 통해서 전부 찾는다
### 가장 처음 조건은 일단 알파벳이 일치하는지
### 크레인 작업으로 끄내면 가운데가 빈공간이 생긴다. 이런경우 4방향 탐색후 0이 존재하면 0, 아닐경우 1
