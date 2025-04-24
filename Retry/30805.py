'''

두 집합 중 겹치는 원소를 구한다
겹치는 원소중 가장 큰 수를 구한다
가장 큰수의 인덱스를 구하고 그 인덱스 이후 부터 반복한다.


'''

import sys

N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int,sys.stdin.readline().split()))

result = []
while True:
    A_set = set(A)
    B_set = set(B)
    common = A_set & B_set
    if len(common) == 0:
        break
    Max = max(common)
    result.append(Max)
    A_idx = A.index(Max)
    B_idx = B.index(Max)
    A = A[A_idx+1:]
    B = B[B_idx+1:]

print(len(result))
if len(result) != 0:
    print(*result)