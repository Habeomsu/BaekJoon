import sys


def tree(arr,n):
    global result
    same=True
    first = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != first:
                same = False
                break
        if same == False:
            break
    if same == True:
        result.append(first)
    else:
        n=n//2
        arr1 = [row[:n] for row in arr[:n]]
        arr2 = [row[n:] for row in arr[:n]]
        arr3 = [row[:n] for row in arr[n:]]
        arr4 = [row[n:] for row in arr[n:]]
        result.append('(')
        tree(arr1, n)
        tree(arr2, n)
        tree(arr3, n)
        tree(arr4, n)
        result.append(')')
arr=[]
n=int(sys.stdin.readline())
for i in range(n):
    arr.append(list(sys.stdin.readline().strip("\n")))
result=[]
tree(arr,n)
print(*result,sep='')