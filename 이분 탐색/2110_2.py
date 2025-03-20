### 갯수가 크다?? 그럼 start = mid +1
### 개수가 부족하다?? 그럼 end =mid -1


N, C = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()


def binary_search(arr):
    start = 1
    end = arr[-1] - arr[0]
    while start<=end:
        mid = (start+end)//2
        current =arr[0]
        cnt = 1
        for i in range(1,N):
            if arr[i]>=current +mid:
                cnt +=1
                current = arr[i]
        if cnt < C:
            end =mid -1
        elif cnt >= C:
            start = mid +1
    return end

print(binary_search(arr))
