import sys
n=int(sys.stdin.readline())
def find2(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    a,b=1,2
    for _ in range(3,n+1):
        b,a=(a+b)%10007,b

    return b
print(find2(n))