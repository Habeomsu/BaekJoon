import sys
import copy
n=int(sys.stdin.readline())
arr=[]

dict={}
num=[]
result=[]
for i in range(n):
    arr.append(list(sys.stdin.readline().strip("\n")))
arr=sorted(arr,key=lambda x:len(x),reverse=True)
arr1=copy.deepcopy(arr)
m=len(arr[0])
for i in range(m):
    for j in range(n):
        if len(arr[j])!=0:
            num.append(arr[j].pop())
num=num[::-1]
cnt=9
for i in num:
    if i not in dict:
        dict[i] = cnt
        cnt-= 1

for line in arr1:
    result.append(int(''.join([str(dict[char]) for char in line])))

print(sum(result))
