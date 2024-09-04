import sys
from collections import deque

a,b= map(int,sys.stdin.readline().split())
S=deque([i for i in range(1,a+1)])
arr=[]
while len(S)>1:
    S.rotate(-(b-1))
    arr.append(S.popleft())
arr.append(S.popleft())
print('<',end="")
print(', '.join(map(str,arr)),end='')
print('>')
