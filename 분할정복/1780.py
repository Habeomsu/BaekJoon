import sys

def paper(arr,n):
    global a,b,c
    first=arr[0][0]
    same=True
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=first:
                same=False
                break
        if same == False:
            break
    if same ==True:
        if first == -1:
            a +=1
        elif first == 0:
            b +=1
        elif first ==1:
            c +=1
    else:
        n=n//3
        arr1=[row[:n] for row in arr[:n]]
        arr2=[row[:n] for row in arr[n:2*n]]
        arr3=[row[:n] for row in arr[2*n:]]
        arr4=[row[n:2*n] for row in arr[:n]]
        arr5=[row[2*n:] for row in arr[:n]]
        arr6=[row[n:2*n] for row in arr[n:2*n]]
        arr7=[row[2*n:] for row in arr[n:2*n]]
        arr8=[row[n:2*n] for row in arr[2*n:]]
        arr9=[row[2*n:] for row in arr[2*n:]]
        paper(arr1,n)
        paper(arr2, n)
        paper(arr3, n)
        paper(arr4, n)
        paper(arr5, n)
        paper(arr6, n)
        paper(arr7, n)
        paper(arr8, n)
        paper(arr9, n)

n=int(sys.stdin.readline())
arr=[]
a,b,c=0,0,0
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
paper(arr,n)
print(a)
print(b)
print(c)


