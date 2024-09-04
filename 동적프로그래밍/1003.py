import sys


def fibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    dp = [(0, 0)] * (n + 1)
    dp[0] = (1, 0)
    dp[1] = (0, 1)

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

    return dp[n]



input = sys.stdin.readline
n = int(input().strip())

results = []
for _ in range(n):
    a = int(input().strip())
    results.append(fibo(a))

for result in results:
    print(result[0], result[1])
