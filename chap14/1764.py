import sys

n,m=map(int,sys.stdin.readline().split())
dic={}
sum=0
arr=[]
for i in range(n):
    a=sys.stdin.readline().strip('\n')
    dic[a]=1
for j in range(m):
    b=sys.stdin.readline().strip('\n')
    if b in dic:
        arr.append(b)
        sum+=1
    else:
        dic[b]=1
print(sum)
print(*sorted(arr),sep='\n')