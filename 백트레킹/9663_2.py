### 조건 - 하나의 말을 놓는다
### 만약 해당 위치에 가로, 세로, 대각선 위치에 말이 존재할 경우 백트레킹
### 대각선은 가로,세로의 차이가 1대1이다
###

import sys

N = int(sys.stdin.readline())
sum =0

def queen(row):
    global sum
    if row == N:
        sum +=1
        return
    for col in range(N):
        if arr1[col]==False and arr2[row+col]==False and arr3[row-col]==False:
            arr1[col] = True
            arr2[row+col]= True
            arr3[row-col] = True
            queen(row+1)
            arr1[col] = False
            arr2[row+col] = False
            arr3[row-col] = False

arr1 = [False]*N
arr2 = [False]*((N-1)*2+1)
arr3= [False]*((N-1)*2+1)

queen(0)
print(sum)