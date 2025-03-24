def solution(n, w, num):
    answer = 0
    row = n // w + 1
    arr = [[0] * w for _ in range(row)]
    cnt = 1
    idx = []
    for i in range(row):
        for j in range(w):
            if cnt <= n:
                arr[i][j] = cnt
                cnt += 1
            else:
                break
    for i in range(1, row):
        if i % 2 == 1:
            arr[i][:] = arr[i][::-1]
    for i in range(row):
        for j in range(w):
            if arr[i][j] == num:
                idx.append((i, j))
    for i in range(idx[0][0], row):
        if arr[i][idx[0][1]] != 0:
            answer += 1

    return answer

### 일단 배열을 완성한다..
### 배열은 1부터 차례대로 만든다..
### 행이 짝수 일때 배열을 뒤집는다.
### 해당 수의 인덱스를 찾는다
### 해당 수 밑에 남은 열의 개수를 찾는다.