N , M = map(int,input().split())
arr = [0]*N
for i in range(N):
    arr[i]=i+1
for i in range(M):
    a ,b = map(int,input().split())
    arr[a-1:b]=arr[a-1:b][::-1]
print(*arr)