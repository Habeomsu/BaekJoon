import sys


def find3(n):
    global arr
    dp=[[0]*i for i in range(501)]
    dp[0]=0
    dp[1]=arr[0]
    for i in range(2,n+1):
        for j in range(i):
            if j==0:
                dp[i][j]=dp[i-1][0]+arr[i-1][j]
            elif j==i-1:
                dp[i][j]=dp[i-1][-1]+arr[i-1][-1]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+arr[i-1][j]
    return max(dp[n])

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
print(find3(n))