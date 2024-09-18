import sys

n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr=sorted(arr)
def find(start,end,bring):
    while start<=end:
        mid=(start+end)//2
        result =0
        for i in arr:
            if i>=mid:
                result +=i-mid
        if result<bring:
            end=mid-1
        else:
            start=mid+1
    return end

print(find(1,arr[-1],m))
