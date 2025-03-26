def solution(mats, park):
    answer = -1
    col = len(park[0])
    row = len(park)
    mats = sorted(mats)
    for k in mats:
        for i in range(0, row - k + 1):
            for j in range(0, col - k + 1):
                if park[i][j] == '-1':
                    if find_mats(i, j, park, k):
                        answer = max(answer, k)

    return answer


def find_mats(x, y, arr, num):
    able = True
    for i in range(x, x + num):
        if able == False:
            break
        for j in range(y, y + num):
            if arr[i][j] != "-1":
                able = False
                break
    return able

### 그래프 문제 인것은 확인
### 이것은 브루트 포스...
### for 문을 돌려서 확인