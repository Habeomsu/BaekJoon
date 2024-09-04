arr = [0]*10
for i in range(10):
    a=int(input())
    arr[i] =a %42
answer =0
S = set(arr)
print(len(S))