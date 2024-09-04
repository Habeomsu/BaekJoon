import sys

a, b, c = map(int, sys.stdin.readline().split())

def div(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = div(a, b // 2, c)
        return (half * half) % c
    else:
        return (a * div(a, b - 1, c)) % c

n = div(a, b, c)
print(n)