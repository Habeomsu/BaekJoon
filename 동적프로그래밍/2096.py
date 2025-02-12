import sys

N = int(sys.stdin.readline())
arr=[]

for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

def find():
    max_dp=[0,0,0]
    min_dp=[0,0,0]
    for i in range(3):
        max_dp[i]=arr[0][i]
        min_dp[i]=arr[0][i]
    for i in range(1,N):
        max_dp=[max(max_dp[0],max_dp[1])+arr[i][0],max(max_dp[0],max_dp[1],max_dp[2])+arr[i][1],max(max_dp[1],max_dp[2])+arr[i][2]]
        min_dp = [min(min_dp[0], min_dp[1]) + arr[i][0], min(min_dp[0], min_dp[1], min_dp[2]) + arr[i][1],
                  min(min_dp[1], min_dp[2]) + arr[i][2]]

    return max(max_dp),min(min_dp)

print(*find())

# def find_min():
#     dp=[[0]*3 for _ in range(N)]
#     for i in range(3):
#         dp[0][i]=arr[0][i]
#     for i in range(1,N):
#         for j in range(3):
#             if j==0:
#                 dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+arr[i][j]
#             elif j==2:
#                 dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+arr[i][j]
#             else:
#                 dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+arr[i][j]
#
#     return min(dp[-1])
#
# def find_max():
#     dp=[[0]*3 for _ in range(N)]
#     for i in range(3):
#         dp[0][i]=arr[0][i]
#     for i in range(1,N):
#         for j in range(3):
#             if j == 0:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + arr[i][j]
#             elif j == 2:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + arr[i][j]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1]) + arr[i][j]
#     return max(dp[-1])
# print(find_max(),find_min())
