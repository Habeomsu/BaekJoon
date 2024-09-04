import sys

n = int(sys.stdin.readline())
arr=[]
plus=[]
minus=[]
arr1=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr,reverse=True)
for i in arr:
    if i>1:
        plus.append(i)
    elif i==1:
        arr1.append(i)
    else:
        minus.append(i)
if len(plus) %2==1:
    arr1.append(plus.pop())
for i in range(0,len(plus),2):
    arr1.append(plus[i]*plus[i+1])
minus=sorted(minus)
if len(minus) %2 ==1:
    arr1.append(minus.pop())
for i in range(0,len(minus),2):
    arr1.append(minus[i]*minus[i+1])
print(sum(arr1))
