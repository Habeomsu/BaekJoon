import sys

N, K = map(int,sys.stdin.readline().split())

temp_arr = list(map(int,sys.stdin.readline().split()))

acc_arr = [0] * (N+1)

for i in range(1,N+1):
    acc_arr[i] = acc_arr[i-1] + temp_arr[i-1]

result = -1e9

for i in range(0,N+1-K):
    if result < acc_arr[i+K]-acc_arr[i]:
        result = acc_arr[i+K]-acc_arr[i]

print(result)



'''


연속적인 부분합 배열을 만든다.
단, 0번째를 추가해준다.



'''