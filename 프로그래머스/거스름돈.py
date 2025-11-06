def solution(n, money):
    answer = 0
    money = sorted(money)

    dp = [0] * (n + 1)

    for mon in money:
        dp[mon] = dp[mon] + 1
        for i in range(mon, n + 1):
            dp[i] = dp[i - mon] + dp[i]

    answer = dp[n]
    answer = answer % 1000000007

    return answer