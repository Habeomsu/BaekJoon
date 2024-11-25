import sys

def sum_all(n):
    sum =0
    new = str(n)
    for i in range(len(new)):
        sum = sum + int(new[i])
    sum = sum + n
    return sum

arr = [0]*10001
i=1
result=0
while i<10001:
    result = sum_all(i)
    if(result <10001):
        arr[result] = 1
    i=i+1
for i in range(1,len(arr)):
    if(arr[i]==0):
        print(i)