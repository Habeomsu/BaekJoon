import math
arr=[]
for i in range(5):
    n=int(input())
    arr.append(n)
arr=sorted(arr)
sum=sum(arr)
print(sum//5)
print(arr[2])