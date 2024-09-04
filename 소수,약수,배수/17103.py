import sys
def find_prime(n):
    arr=[1]*(n+1)
    arr[0]=0
    arr[1]=0
    for i in range(2,int(n**0.5)+1):
        for j in range(i*i,n+1,i):
            arr[j]=0
    return arr
def find_under(n):
    arr2=[]
    arr1=find_prime(n)
    for i in range(2,len(arr1)):
        if arr1[i]==1:
            arr2.append(i)
    return arr2

def print_gold(n):
    arr=find_under(n)
    S=set(arr)
    i=0
    answer=0
    while arr[i]<=n//2:
        if n-arr[i] in S:
            answer=answer+1
        i=i+1
    return answer

n=int(sys.stdin.readline())
for j in range(n):
    a=int(sys.stdin.readline())
    answer=print_gold(a)
    print(answer)