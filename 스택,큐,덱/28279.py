import sys
from collections import deque

n=int(sys.stdin.readline())
S=deque()
for i in range(n):
    a=sys.stdin.readline().strip('\n').split()
    if a[0]=='1':
        S.appendleft(int(a[1]))
    elif a[0]=='2':
        S.append((int(a[1])))
    elif a[0]=='3':
        if len(S)==0:
            print(-1)
        else:
            print(S.popleft())
    elif a[0] =='4':
        if len(S)==0:
            print(-1)
        else:
            print(S.pop())
    elif a[0]=='5':
        print(len(S))
    elif a[0]=='6':
        if len(S)==0:
            print(1)
        else:
            print(0)
    elif a[0]=='7':
        if len(S)==0:
            print(-1)
        else:
            print(S[0])
    elif a[0]=='8':
        if len(S)==0:
            print(-1)
        else:
            print(S[-1])