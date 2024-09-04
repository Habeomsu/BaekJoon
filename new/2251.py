import sys

n = int(sys.stdin.readline())
lengths = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))
answer = 0

prices.pop()
min=min(prices)
for i in range(n-1):
    num = lengths[i]
    idx = i
    if prices[i] == min:
        answer += prices[i] * sum(lengths[i:])
        break
    while prices[i] < prices[idx+1] and idx <= n-1:
        num += lengths[idx+1]
        lengths[idx+1] = 0
        idx += 1

    answer += prices[i] * num

if len(prices) == 1:
    answer = prices[0] * lengths[0]

print(answer)