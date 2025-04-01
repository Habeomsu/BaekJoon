def solution(n, q, ans):
    answer = [0]
    arr = []
    back(arr, 1, n, q, ans, answer)
    return answer[0]


def back(arr, num, n, q, ans, answer):
    if len(arr) == 5:
        isOk = True
        for i in range(len(q)):
            cnt = 0
            for j in q[i]:
                if j in arr:
                    cnt += 1
            if cnt != ans[i]:
                isOk = False
                break
        if isOk == True:
            answer[0] += 1
        return
    for i in range(num, n + 1):
        arr.append(i)
        back(arr, i + 1, n, q, ans, answer)
        arr.pop()

### 1부터 n까지 5개의 배열을 생성한다.
### 백트레킹을 통해 만약 q의 조건이 전부 ans 개가 나오면 result를 1 추가한다
