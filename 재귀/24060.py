import sys
def merge_sort(a,p,r,b):
    if p <r:
        q=(p+r)//2
        merge_sort(a,p,q,b)
        merge_sort(a,q+1,r,b)
        merge(a,p,q,r,b)
    return a,b

def merge(a,p,q,r,b):
    i,j,t=p,q+1,0
    arr=[]
    while i<=q and j<=r:
        if a[i]<=a[j]:
            arr.append(a[i])
            b.append(a[i])
            i+=1
        else:
            arr.append(a[j])
            b.append(a[j])
            j+=1
    while i<=q:
        arr.append(a[i])
        b.append(a[i])
        i+=1

    while j <=r:
        arr.append(a[j])
        b.append(a[j])
        j+=1

    for k in range(p,r+1):
        a[k]=arr[k-p]

n,k=map(int,sys.stdin.readline().split())
c=list(map(int,sys.stdin.readline().split()))
b=[]
c,b=merge_sort(c,0,n-1,b)
if len(b)>=k:
    print(b[k-1])
else:
    print(-1)