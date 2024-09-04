answer ='abcdefghijklmnopqrstuvwxyz'
a = input()
arr = [-1]*26
for i,j in enumerate(answer):
    if j in a:
        arr[i] = a.index(j)
print(*arr)