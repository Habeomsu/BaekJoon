import sys

a,b = map(int,sys.stdin.readline().split())

arr=[i for i in range(1,a+1)]
result=[]
k=b-1

while len(arr)!=0:
    if(k>=len(arr)):
        k=k%len(arr)
    c=arr.pop(k)
    result.append(c)
    k=k+b-1
print(f"<{', '.join(map(str, result))}>")