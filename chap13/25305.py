n,k=map(int,input().split())
arr=[]
arr=list(map(int,input().split()))
arr=sorted(arr,reverse=True)
print(arr[k-1])