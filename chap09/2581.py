a = int(input())
b = int(input())
sum=0
min=10000
for i in range(a,b+1):
    for j in range(2,i+1):
        if j == i:
            if min > i:
                min = i
            sum = sum +i
        if i %j ==0:
            break;
if sum== 0:
    print(-1)
else:
    print(sum)
    print(min)