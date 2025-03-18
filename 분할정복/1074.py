### N 이 주어지면 2**N x 2**N 배열을 생성한다 ...
### 해당 배열을 채우는 divide and conquer를 작성한다.
### 재귀가 끝나는 조건은 N값이 1인경우이다 ...
### N값이 1일때 순서대로 1,2,3,4 점점 하나씩 증가한다.


# import sys
#
# N, r, c = map(int,sys.stdin.readline().split())
# arr = [[0]*2**N for _ in range(2**N)]
# sum=1
# for i in range(2**N):
#     for j in range(2**N):
#         arr[i][j] = sum
#         sum +=1
#
# real_num = arr[r][c]
# sum=0
# def find_num(arr,num):
#     global sum
#     if num == 1:
#         if arr[0][0] == real_num:
#             print(sum)
#             exit()
#         sum +=1
#         return
#     else:
#         num = num//2
#         arr1 = [row[:num] for row in arr[:num]]
#         arr2 = [row[num:] for row in arr[:num]]
#         arr3 = [row[:num] for row in arr[num:]]
#         arr4 = [row[num:] for row in arr[num:]]
#         find_num(arr1, num)
#         find_num(arr2, num)
#         find_num(arr3, num)
#         find_num(arr4, num)
#
# find_num(arr,2**N)

import sys

N, r, c = map(int,sys.stdin.readline().split())

def find(num,r,c):
    if num == 1:
        return 0

    half = num // 2

    # 2사분면
    if(r<half and c < half):
        return find(num//2,r,c)

    # 1사분면
    if(r<half and c>=half):
        return half*half + find(num//2,r,c-half)

    # 3사분면
    if (r>=half and c<half):
        return half*half*2 + find(num//2,r-half,c)

    # 4사분면
    if (r>=half and c>=half):
        return half*half*3 + find(num//2,r-half,c-half)

print(find(2**N,r,c))