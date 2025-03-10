# import sys
#
# n = int(sys.stdin.readline())
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))
#
# def dfs(x,y,dir):
#     global result
#     if x == n-1 and y ==n-1:
#         result +=1
#         return
#     #대각선 이동
#     if x+1<n and y+1<n:
#         if arr[x+1][y]==0 and arr[x][y+1]==0 and arr[x+1][y+1]==0:
#             dfs(x+1,y+1,2)
#     # 가로 이동
#     if dir == 0 or dir ==2:
#         if y+1 <n:
#             if arr[x][y+1]==0:
#                 dfs(x,y+1,0)
#     # 세로 이동
#     if dir ==1 or dir ==2:
#         if x+1 <n:
#             if arr[x+1][y]==0:
#                 dfs(x+1,y,1)
#
# result =0
# dfs(0,1,0)
# print(result)

import sys

home = []
N = int(input())
for _ in range(N):
    home.append([int(x) for x in sys.stdin.readline().rstrip().split()])

DP = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
# 0 가로, 1 세로, 2 대각선

DP[0][0][1] = 1
for i in range(2,N):
    if home[0][i] == 0:
        DP[0][0][i] = DP[0][0][i - 1]
#print(DP)

for i in range(1,N):
    for j in range(1,N):
        if home[i][j] == 0 and home[i][j - 1] == 0 and home[i - 1][j] == 0:
            DP[2][i][j] = DP[0][i - 1][j - 1] + DP[1][i - 1][j - 1] + DP[2][i - 1][j - 1]
            # 대각선 파이프 놓기

        if home[i][j] == 0:
            DP[0][i][j] = DP[0][i][j - 1] + DP[2][i][j - 1]
            # 가로 파이프 놓기

            DP[1][i][j] = DP[1][i - 1][j] + DP[2][i - 1][j]
            # 세로 파이프 놓기
print(DP[0][N - 1][N - 1] + DP[1][N - 1][N - 1] + DP[2][N - 1][N - 1])