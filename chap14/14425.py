import sys
a,b= map(int,sys.stdin.readline().split())
arr=[]
sum=0
for i in range(a):
    s=sys.stdin.readline().strip('\n')
    arr.append(s)
S=set(arr)
for i in range(b):
    s=sys.stdin.readline().strip('\n')
    if s in S:
        sum=sum+1
print(sum)