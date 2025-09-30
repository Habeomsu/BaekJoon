import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

acc_list = [0]*(N+1)
acc_list[1] = num_list[0]

for i in range(2,N+1):
    acc_list[i] = acc_list[i-1] + num_list[i-1]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    print(acc_list[b]-acc_list[a-1])


