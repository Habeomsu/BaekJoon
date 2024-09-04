import sys

def fac(n):
    sum=1
    for i in range(1,n+1):
        sum *=i
    return sum

a,b=map(int,sys.stdin.readline().split())
result = fac(a)//(fac(b)*fac(a-b))
print(result)