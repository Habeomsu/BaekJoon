N , M = map(int,input().split())
arr=[0]*(N)
for i in range(M):
    a,b,c = map(int,input().split())
    for i in range(a-1,b):
        arr[i]=c

print(' '.join(map(str,arr)))