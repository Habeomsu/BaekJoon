import sys

def find1(arr):
    arr=sorted(arr,key=lambda  x: x[1])
    result=1
    new=arr[0][1]
    for i in range(1,n):
        if arr[i][0] >=new:
            new=arr[i][1]
            result +=1
    return result

def find2(arr):
    arr=sorted(arr)
    result =1
    new=arr[0][1]
    for i in range(1,n):
        if arr[i][0] >=new:
            new=arr[i][1]
            result +=1
    return result

n= int(sys.stdin.readline())
arr=[]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    arr.append([a,b])
result1=find1(arr)
result2=find2(arr)
print(max(result1,result2))