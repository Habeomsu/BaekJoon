import sys

n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
arr=list(map(int,sys.stdin.readline().split()))
arr1=[]
for i in range(4):
    if arr[i]:
        for _ in range(arr[i]):
            if i==0:
                arr1.append('+')
            if i==1:
                arr1.append('-')
            if i==2:
                arr1.append('*')
            if i==3:
                arr1.append('//')
print(arr1)
max=0
min=0
answer=''

def back(i):
    result=0
    if i==n:
        return result

