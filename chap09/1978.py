a = int(input())
arr = list(map(int,input().split()))
sum=0
for i in range(a):
    for j in range(2,arr[i]+1):
        if arr[i] == j:
            sum += 1
        if arr[i]%j==0:
            break;
print(sum)