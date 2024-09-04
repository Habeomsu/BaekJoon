import sys
a = int(sys.stdin.readline())
arr=list(map(int,str(a)))
arr=sorted(arr,reverse=True)
print(*arr,sep='')