import sys

n=int(sys.stdin.readline())
a=300
b=60
c=10
d=0
e=0
f=0
if n%c !=0:
    print(-1)
else:
    d,n=n//a,n%a
    e,n=n//b,n%b
    f=n//c
    print(d,e,f)