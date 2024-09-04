import sys

def paper(arr,n):
    global blue, white
    first = arr[0][0]
    same=True
    for i in range(n):
        for j in range(n):
             if arr[i][j] != first:
                same = False
                break
        if not same:
            break
    if same:
        if first == 0:
            white +=1
        else:
            blue +=1
    else:
        n=n//2
        arr1=[row[:n] for row in arr[:n]]
        paper(arr1,n)
        arr2=[row[n:] for row in arr[:n]]
        paper(arr2,n)
        arr3=[row[:n] for row in arr[n:]]
        paper(arr3,n)
        arr4=[row[n:] for row in arr[n:]]
        paper(arr4,n)


arr=[]
n=int(sys.stdin.readline())
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
blue,white=0,0
paper(arr,n)
print(white)
print(blue)