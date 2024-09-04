import sys
from collections import deque

n=int(sys.stdin.readline())
Q=deque([i for i in range(1,n+1)])
while len(Q) >1:
    Q.popleft()
    a=Q.popleft()
    Q.append(a)
print(Q[0])