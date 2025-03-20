### 시작과 끝에서 각각 출발하여 위치를 점점 줄여간다 .
### 절댓값 기준 더 큰수를 변경해준다
### 최소값을 미리 선언해준다

import sys
INF = int(1e10)
n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = n-1

min_value = INF
x,y=0,end
while start<end:
    cur_value = arr[start]+arr[end]
    if abs(cur_value)<=min_value:
        x,y=start,end
        min_value=abs(arr[start]+arr[end])
    if arr[start]+arr[end]>0:
        end -=1
    else:
        start +=1
print(arr[x],arr[y])