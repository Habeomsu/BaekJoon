### 연속된 수들의 부분합 -> 새로운 배열에 모든 이전의 모든 수를 더한 배열을 계속 추가해준다.
### 0부터 시작하여 끝까지 모든 수를 더한 부분합 배열을 구해준다.
### 두 포인터는 같은 위치에서 시작이 가능하다 ...

import sys

N,S = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

plus_arr = [0]*(N+1)
plus_arr[1]=arr[0]

for i in range(2,N+1):
    plus_arr[i] = plus_arr[i-1]+arr[i-1]

min_value = 100000001
start = 0
end = 1

while end<N+1:
    if plus_arr[end]-plus_arr[start]>=S:
        min_value=min(end-start,min_value)
        start +=1
    else:
        end +=1
if min_value == 100000001:
    print(0)
else:
    print(min_value)