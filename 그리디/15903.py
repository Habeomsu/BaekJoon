import sys

n,m=map(int,sys.stdin.readline().split())

arr= list(map(int,sys.stdin.readline().split()))

for i in range(m):
    arr=sorted(arr)
    a1=arr.pop(0)
    a2=arr.pop(0)
    a3=a1+a2
    arr.append(a3)
    arr.append(a3)
print(sum(arr))

# heap 으로 표현 가능
