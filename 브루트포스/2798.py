N, M = map(int,input().split())
arr = list(map(int,input().split()))
sum=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i]+arr[j]+arr[k] <= M and sum <=arr[i]+arr[j]+arr[k]:
                sum = arr[i]+arr[j]+arr[k]
print(sum)