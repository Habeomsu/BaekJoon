import sys

def lcs(n):
    if n==1:
        return 1
    dp=[1]*1001
    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

n = int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
print(lcs(n))
