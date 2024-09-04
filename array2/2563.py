N = int(input())
arr=[[0]*100 for _ in range(100)]
for i in range(N):
    a,b = map(int,input().split())
    for j in range(a-1,a+9):
        for k in range(b-1,b+9):
            arr[j][k] = 1
answer=0
for i in arr:
    answer = answer+i.count(1)
print(answer)