arr = [0]*31
arr[0] = 1
for i in range(28):
    a = int(input())
    arr[a] = 1
print(arr.index(0))
arr[arr.index(0)]=1
print(arr.index(0))