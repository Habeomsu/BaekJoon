import sys

N,M = map(int,sys.stdin.readline().split())

arr=[]
cnt =1
def back():
    if len(arr) == M:
        print(arr)
        return

    for i in range(1,N+1):
        if i not in arr:
            arr.append(i)
            back()
            arr.pop()

back()
