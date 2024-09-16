import sys

n= int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr=arr[::-1]
min = arr[0]
result = 0
for i in arr[1:]:
    if i >=min:
        result = result + (i-min+1)
        min = min -1
    else:
        min=i
print(result)