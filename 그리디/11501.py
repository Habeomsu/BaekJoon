import sys

input = sys.stdin.readline


def calculate_max_profit(n, prices):
    max_price = prices[-1]  # 마지막 날의 주가를 최대 가격으로 초기화
    profit = 0

    # 역순으로 가격을 확인
    for i in range(n - 2, -1, -1):  # 마지막 날 제외하고 거꾸로 탐색
        if prices[i] < max_price:
            profit += max_price - prices[i]  # 최대 가격에서 현재 가격을 뺀 이익을 추가
        else:
            max_price = prices[i]  # 현재 가격이 더 높으면 최대 가격 업데이트

    return profit


T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    max_profit = calculate_max_profit(N, prices)
    print(max_profit)