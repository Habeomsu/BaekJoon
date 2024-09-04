import sys
n=int(input())
arr=[]
for i in range(n):
    a=sys.stdin.readline()
    arr.append(a.replace('\n',''))
arr=set(arr)
arr=list(arr)
arr=sorted(arr,key=lambda x:(len(x),x))
print(*arr,sep="\n")