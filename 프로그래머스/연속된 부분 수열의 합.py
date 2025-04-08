def solution(sequence, k):
    answer = []
    dp = [0]*(len(sequence)+1)
    dp[1]= sequence[0]
    for i in range(2,len(sequence)+1):
        dp[i]=dp[i-1]+sequence[i-1]
    start = 0
    end = 1
    cnt = 0
    while end < len(sequence)+1:
        sum = dp[end] - dp[start]
        if k == sum:
            if len(answer) == 0:
                answer.append([start,end-1])
                cnt = end-start
            else:
                if cnt > end- start:
                    answer.pop()
                    answer.append([start,end-1])
                    cnt = end - start
            end += 1
        elif sum > k:
            start += 1
        elif sum < k:
            end += 1

    return answer[0]


### 누적합 배열을 만든다
### 두 포인터를 이용해서 부분합이 k 와 같은 지를 판단
### k보다 작다면 오른쪽 포인트를 이동
### k보다 크다면 왼쪽 포인트를 이동