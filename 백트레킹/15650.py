import sys

n,m = map(int,sys.stdin.readline().split())
arr=[]

def back(start):
    if len(arr)==m:
        print(" ".join(map(str,arr)))
        return
    for i in range(start,n+1):
        if i not in arr:
            arr.append(i)
            back(i+1)
            arr.pop()
back(1)

