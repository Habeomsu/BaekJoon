### dp만으로 푸는 경우 초과난다 ...
### dp 배열을 만드는 과정에서 순차 탐색이니라 이진 탐색 가능


import sys

N = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))


result=[arr[0]]

def binary_search(num):
    start = 0
    end =len(result)-1
    while start<=end:
        mid = (start+end)//2
        if result[mid]<num:
            start =mid+1
        else:
            end = mid-1
    return start

for i in range(1,N):
    if arr[i]>result[-1]:
        result.append(arr[i])
    else:
        idx = binary_search(arr[i])
        result[idx]=arr[i]


print(len(result))