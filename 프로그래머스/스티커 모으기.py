def solution(sticker):
    answer = 0

    n = len(sticker)

    if n == 1:
        return sticker[0]
    elif n == 2:
        return max(sticker)
    else:
        dp1 = [0] * (n + 1)
        dp1[1] = sticker[0]
        dp1[2] = max(sticker[0], sticker[1])
        for i in range(3, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i - 1])

        dp2 = [0] * (n + 1)
        a = sticker.pop()
        sticker.insert(0, a)
        dp2[1] = sticker[0]
        dp2[2] = max(sticker[0], sticker[1])
        for i in range(3, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i - 1])

        dp1_max = max(dp1)
        dp2_max = max(dp2)
        answer = max(dp1_max, dp2_max)

    return answer


'''

구하고자 하는 것은 점수의 최대값이다.
배열을 기준으로 순차적으로 탐색을 하는데 
해당 스티커를 뜯는 경우의 수는 
이전 스티커가 안뜯어진경우이다.
만약 해당 스티커를 띄고 -1 의 값과 
dp[i] = max(dp[i-1],dp[i-2]+arr[i])
단 dp 마지막인 경우에는 dp[1] 도 비교해야한다?? 





'''