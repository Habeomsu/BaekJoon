import sys
arr=[0]*10001
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    arr[a] +=1
j=1
while True:
    if arr[j] !=0:
        print(j)
        arr[j] = arr[j]-1
    else:
        j=j+1
    if j == 10001:
        break;