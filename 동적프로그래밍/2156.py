import sys

def grape(n):

    dp=[0]*10001
    if n==1:
        return arr[1]
    if n==2:
        return arr[1]+arr[2]
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]
    for i in range(3,n+1):
        dp[i]=max(dp[i-1],dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i])
    return dp[n]
n=int(sys.stdin.readline())
arr=[0]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
print(grape(n))