import sys
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
sum=0
n=int(sys.stdin.readline())
arr=[]
arr3=[]
S=set()
for i in range(n):
    a=int(sys.stdin.readline())
    arr.append(a)
for k in range(n-1):
    S.add(arr[k+1]-arr[k])
    arr3.append(arr[k+1]-arr[k])
arr2=list(S)
G=arr2[0]
for k in arr2:
    G=gcd(G,k)
for l in arr3:
    sum=sum+ (l//G-1)
print(sum)