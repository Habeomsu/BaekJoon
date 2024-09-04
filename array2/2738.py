N, M = map(int,input().split())
arr1=[0]*N
arr2=[0]*N
arr3=[[0]*M for _ in range(N)]
for i in range(N):
    arr1[i] = input().split()
for i in range(N):
    arr2[i] = input().split()
for i in range(N):
    for j in range(M):
        arr3[i][j] = int(arr1[i][j])+int(arr2[i][j])
    print(*arr3[i])


