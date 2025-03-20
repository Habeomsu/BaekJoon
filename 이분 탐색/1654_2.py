### 최대 길이를 구하는것
### mid 값을 구하고 , 각 값을 mid값으로 나눠서
### 만약에 나눈 값들의 합이 목표 개수보다 크면 start값을 +1, 작으면 end -1
### 만약 같다면?? start +1

import sys

K, N = map(int,sys.stdin.readline().split())

arr =[]
for i in range(K):
    arr.append(int(sys.stdin.readline()))

arr = sorted(arr)
def find_string(arr):
    start=1
    end=arr[-1]
    while start<=end:
        mid = (start+end)//2
        cnt=0
        for i in range(K):
            cnt += arr[i]//mid
        if cnt < N:
            end = mid - 1
        elif cnt >= N:
            start = mid + 1

    return end

print(find_string(arr))