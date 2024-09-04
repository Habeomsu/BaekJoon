import sys
a,b=map(int,sys.stdin.readline().split())
c,d=map(int,sys.stdin.readline().split())
min=0
max=0
if b>d:
    max,min =b,d
else:
    max,min=d,b
while min !=0:
    max,min=min,max%min
a=a*d//max
c=c*b//max
e=a+c
f=b*d//max
if e>f:
    max,min=e,f
else:
    max,min=f,e
while min !=0:
    max,min=min,max%min
print(e//max,f//max)