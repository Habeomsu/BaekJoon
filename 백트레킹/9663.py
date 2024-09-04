import sys

n=int(sys.stdin.readline())
result=0
arr1=[False]*(n)
arr2=[False]*(2*n)
arr3=[False]*(2*n)

def nqueen(row):
    global result
    if row==n:
        result +=1
        return
    for col in range(n):
        if not arr1[col] and not arr2[row-col] and not arr3[row+col]:
            arr1[col]=True
            arr2[row-col]= True
            arr3[row+col]=True
            nqueen(row+1)
            arr1[col] = False
            arr2[row - col] = False
            arr3[row + col] = False

nqueen(0)
print(result)