import sys

n = int(sys.stdin.readline())
dp =[0]*(n+1)

def min_coins(n):

    coins_5 = n // 5
    while coins_5 >= 0:
        remainder = n - (coins_5 * 5)
        if remainder % 2 == 0:
            coins_2 = remainder // 2
            return coins_5 + coins_2
        coins_5 -= 1
    return -1
print(min_coins(n))