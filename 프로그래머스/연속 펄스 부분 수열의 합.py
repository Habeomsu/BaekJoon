def solution(sequence):
    answer = 0
    plus_sequence = []
    minus_sequence = []

    n = len(sequence)

    start1 = 1
    start2 = -1
    for i in range(len(sequence)):
        plus_sequence.append(sequence[i] * start1)
        start1 = start1 * (-1)

    for i in range(len(sequence)):
        minus_sequence.append(sequence[i] * start2)
        start2 = start2 * (-1)

    plus_dp = [0] * (len(sequence) + 1)
    minus_dp = [0] * (len(sequence) + 1)

    if n == 1:
        return max(plus_sequence[0], minus_sequence[0])
    else:
        plus_dp[1] = plus_sequence[0]
        minus_dp[1] = minus_sequence[0]

        for i in range(2, n + 1):
            plus_dp[i] = max(plus_dp[i - 1] + plus_sequence[i - 1], plus_sequence[i - 1])
            minus_dp[i] = max(minus_dp[i - 1] + minus_sequence[i - 1], minus_sequence[i - 1])

        plus_max = max(plus_dp)
        minus_max = max(minus_dp)

        answer = max(plus_max, minus_max)

    return answer


'''

1. dp 를 사용하는 것은 맞다.
2. 어떻게 dp를 사용하지? 
3. 경우의 수는 5가지다. 자신을 포함하지 않거나, 자신을 포함하되 더해 해주거나, 자신을 포함하되 빼주거나 이다. 또는 자신만 포함되거나?? 

dp[i] = max(dp[i-1],dp[i-1]+arr[i],dp[i-1]-arr[i],arr[i],-arr[i]) 


1. 근데 생각을 해보면 [+,-,+,-,+,-] 이런 식으로 시작한다.
2. 즉, 두가지 경우로 arr를 만든다.
3. dp는 자신이거나 자신과 이전 dp의 합이다.

즉. max(dp[i-1] + arr[i] , arr[i])



'''