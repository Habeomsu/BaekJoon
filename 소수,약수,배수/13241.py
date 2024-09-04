import sys
a, b = map(int,sys.stdin.readline().split())
if a>b:
    max,min=a,b
else:
    max,min=b,a
while min!=0:
    max,min=min,max%min
print(a*b//max)