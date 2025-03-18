### 2 x 2 의 정사각형으로 나누어서 그중 2번째로 큰 수를 구한다. ->
### 처음 2^n승인 경우 -> 다음은 2^n-1승이 된다.
### 배열을 계속 변경한다??
### 각각 나눠서 2 2 2 를 하고 또다시 합친다음에 2 2 2 를 n 이 1 일때 까지 계속한다.
### 그냥 합치기 전에 또다시 2 2 2 를 그 구간에서 처리하면 최종적으로 4분면에서 1개씩만 남는다.
import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def conv(arr,num):
    if num ==2:
        new_arr = []
        for i in range(2):
            for j in range(2):
                new_arr.append(arr[i][j])
        new_arr.sort()
        return new_arr[2]
    else:
        num = num//2
        arr1 = [row[:num] for row in arr[:num]]
        arr2 = [row[num:] for row in arr[:num]]
        arr3 = [row[:num] for row in arr[num:]]
        arr4 = [row[num:] for row in arr[num:]]
        v1 = conv(arr1,num)
        v2 = conv(arr2,num)
        v3 = conv(arr3,num)
        v4 = conv(arr4,num)
        combine = [v1,v2,v3,v4]
        combine.sort()
        return combine[2]

print(conv(arr,n))

