arr=[0]*9
max=0
a,b=0,0
for i in range(9):
    arr[i]= list(map(int,input().split()))
for i in range(9):
    for j in range(9):
        if arr[i][j]>max:
            max=arr[i][j]
            a=i
            b=j
print(max)
print(a+1,b+1)
