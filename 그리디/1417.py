import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))

result =0

if n==1:
    result = 0
else:
    while True:
        Max=max(arr)
        idx = arr.index(Max)
        if(idx ==0 and arr.count(Max)>1):
            result +=1
            break
        elif(idx == 0):
            break
        else:
            arr[0]+=1
            arr[idx]-=1
            result +=1
print(result)
