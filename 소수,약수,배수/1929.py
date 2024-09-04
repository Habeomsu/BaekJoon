import sys
def find_num(n):
    arr=[1]*(n+1)
    arr[0]=0
    arr[1]=0
    for i in range(2,int(n**0.5+1)):
        j=2
        while (j*i)<=n:
            arr[j*i]=0
            j+=1
    return arr

a,b=map(int,sys.stdin.readline().split())
arr=find_num(b)
for i in range(a,b+1):
    if arr[i]==1:
        print(i)