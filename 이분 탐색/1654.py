import sys

sys.setrecursionlimit(10000000)

k, n = map(int, sys.stdin.readline().split())
arr = []
for i in range(k):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)


def find_mid(start, end, num):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for i in arr:
            result += i // mid

        if result < num:
            end = mid - 1
        else:
            start = mid + 1

    return end

Min = find_mid(1, arr[-1], n)
print(Min)