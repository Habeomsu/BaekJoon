import sys

result1=0
result2=0
def fib(n):
    global result1
    if n==1 or n ==2:
        result1+=1
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fi(n):
    global result2
    if n==1 or n==2:
        result2+=1
    else:
        for i in range(3,n+1):
            result2+=1

n=int(sys.stdin.readline())
fib(n)
fi(n)
print(result1,result2)
