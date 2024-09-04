import sys
def find_prime(n):
    arr=[1]*(n+1)
    arr[0]=0
    arr[1]=0
    for i in range(2,int(n**0.5+1)):
        j=2
        while j*i<=n:
            arr[i*j]=0
            j=j+1
    return arr
arr=find_prime(123456*2)
while True:
    a=int(sys.stdin.readline())
    sum=0
    if a!=0:
        for i in range(a+1,2*a+1):
            if arr[i]==1:
                sum=sum+1
        print(sum)
    else:
        break