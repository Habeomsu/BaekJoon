import sys
n= int(sys.stdin.readline())
S=[]
for i in range(n):
    a=int(sys.stdin.readline())
    if a==0:
        S.pop()
    else:
        S.append(a)
print(sum(S))