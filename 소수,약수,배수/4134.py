import sys

def check(a):
    if a<2:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True

n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())

    while True :
        result=check(a)
        if result:
            print(a)
            break
        else:
            a=a+1