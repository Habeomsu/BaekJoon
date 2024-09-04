import sys
from collections import deque

n= int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))
Q=deque(enumerate(b))
arr2=[]
while len(Q)>1:
    index,a = Q.popleft()
    arr2.append(index+1)
    if a<0:
        Q.rotate(abs(a))
    else:
        Q.rotate(-(a-1))
arr2.append(Q.pop()[0]+1)
print(*arr2)