import sys
n = int(input())
dic={}
arr=list(map(int,sys.stdin.readline().split()))
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
m=int(input())
arr2=list(map(int,sys.stdin.readline().split()))
for i in arr2:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')