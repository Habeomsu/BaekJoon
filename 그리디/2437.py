import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)
Max = sum(arr)


result = [False] * (Max + 1)
result[0] = True

for num in arr:
    for j in range(Max, num - 1, -1):
        if result[j - num]:
            result[j] = True

for i in range(Max + 1):
    if not result[i]:
        print(i)
        break