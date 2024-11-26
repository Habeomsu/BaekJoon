import math
import sys
a = int(sys.stdin.readline())

arr=[]
for i in range(a):
    arr.append(int(sys.stdin.readline()))

arr=sorted(arr)

result1=round(sum(arr)/len(arr))
result2=arr[len(arr)//2]
dic= {}
for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
Max=max(dic.values())
new = []
for i in dic:
    if dic[i]==Max:
        new.append(i)
if(len(new)>1):
    new = sorted(new)
    result3 = new[1]
else:
    result3 = new[0]
if(len(arr)==1):
    result4=0
else:
    result4=arr[-1]-arr[0]

print(result1)
print(result2)
print(result3)
print(result4)

