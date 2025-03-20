### 최장 공통 부분 수열 @@@
### 점화식 -> dp[i][j] = dp[i-1][j-1] +1 or max(dp[i-1][j],dp[i][j-1])
### 문자열 구하기 -> 거꾸로 올라가면 됨


import sys

arr1 = list(sys.stdin.readline().strip())
arr2 = list(sys.stdin.readline().strip())

length1=len(arr1)
length2=len(arr2)

dp =[[0]*(length2+1) for _ in range(length1+1)]
result =[]

for i in range(1,length1+1):
    for j in range(1,length2+1):
        if arr1[i-1]==arr2[j-1]:
            dp[i][j] = dp[i-1][j-1]+ 1
        else:
            dp[i][j]= max(dp[i-1][j],dp[i][j-1])
final_len = dp[length1][length2]

i,j = length1,length2

while True:
    if dp[i][j]==0:
        break
    if arr1[i-1] == arr2[j-1]:
        result.append(arr1[i-1])
        i-=1
        j-=1
    else:
        if dp[i-1][j]>=dp[i][j-1]:
            i -= 1
        else:
            j -=1


if final_len>0:
    print(final_len)
    print("".join(result[::-1]))
else:
    print(final_len)
