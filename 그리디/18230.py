import sys

n,a,b = map(int,sys.stdin.readline().split())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=list(map(int,sys.stdin.readline().split()))
arr1 = sorted(arr1)
arr2 = sorted(arr2)
answer=0
if n%2==1:
    answer+=arr1.pop()
    n=n-1
for i in range(0,n,2):
    if len(arr1)>=2 and len(arr2)>=1:
        k1=0
        k2=0
        k1=arr1[-1]+arr1[-2]
        k2=arr2[-1]
        if k1>=k2:
            answer=answer+k1
            arr1.pop()
            arr1.pop()
        else:
            answer+=k2
            arr2.pop()
    elif len(arr1)>=2:
        k1 = arr1[-1] + arr1[-2]
        answer = answer + k1
        arr1.pop()
        arr1.pop()
    elif len(arr2)>=1:
        k2=arr2[-1]
        answer=answer+k2
        arr2.pop()
print(answer)
