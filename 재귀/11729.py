import sys
def hanoi(n,start,des,pls):

    if n==1:
        print(start,des)
    else:
        return hanoi(n-1,start,pls,des),print(start,des),hanoi(n-1,pls,des,start)

import sys
n=int(sys.stdin.readline())
print(2**n-1)
hanoi(n,1,3,2)
