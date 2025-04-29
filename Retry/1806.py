'''

1. 누적합을 구한다.
2. 두 포인터를 사용하여 목표값을 구한다.
3. 두 포인터의 차이가 목표값 보다 작으면 end 를 +1
4. 두 포인터의 차이가 목표값 보다 크면 start 를 +1

'''

import sys
INF = int(1e9)

N , S = map(int,sys.stdin.readline().split())

lis = list(map(int,sys.stdin.readline().split()))

arr = [0]*(N+1)

for i in range(N):
    arr[i+1] = arr[i] + lis[i]

start = 0
end = 1
result = INF
while end<=N:
    if start >= end:
        break
    if arr[end] - arr[start] < S:
        end = end + 1
    elif arr[end] - arr[start] >= S:
        result = min(end - start, result)
        start = start +1
if result == INF:
    print(0)
else:
    print(result)
