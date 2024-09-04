import sys
a,b = map(int,sys.stdin.readline().split())
A=set(map(int,sys.stdin.readline().split()))
B=set(map(int,sys.stdin.readline().split()))
C=A-B
D=B-A
c=len(C)
d=len(D)
print(c+d)