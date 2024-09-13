import sys
n=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
arr2=list(map(int,sys.stdin.readline().split()))
arr1=sorted(arr1)
def find(x,arr):
    start=0
    end = len(arr)-1

    while start <=end:
        mid = (start+end)//2

        if arr[mid] == x:
            return 1
        elif arr[mid] >x:
            end = mid-1
        elif arr[mid] <x:
            start = mid+1
    return 0
for i in range(m):
    print(find(arr2[i],arr1))