class Stack:
    def __init__(self):
        self.top=[]

    def len(self):
        return len(self.top)

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if not self.is_empty():
            return self.top.pop()
        else:
            return -1


    def peek(self):
        if not self.is_empty():
            return self.top[-1]
        else:
            return -1

    def is_empty(self):
        return len(self.top)==0

import sys
n=int(sys.stdin.readline())
S=Stack()
for i in range(n):
    a=sys.stdin.readline().strip("\n")
    b,c=0,0
    if len(a)==1:
        b=int(a)
    else:
        b,c=map(int,a.split())
    if b==1:
        S.push(c)
    elif b==2:
        print(S.pop())
    elif b==3:
        print(S.len())
    elif b==4:
        if S.is_empty():
            print(1)
        else:
            print(0)
    elif b==5:
        print(S.peek())