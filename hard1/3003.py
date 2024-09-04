arr = list(map(int,input().split()))
arr1 = [1,1,2,2,2,8]
for i in range(len(arr1)):
    arr1[i] = arr1[i]-arr[i]
print(*arr1)
