import sys
n=int(sys.stdin.readline())
arr1=list(map(int,sys.stdin.readline().split()))
arr2=[]
count=1
for i in arr1:
    if i==count:
        count+=1
    else:
        arr2.append(i)
    while len(arr2) != 0:
        if arr2[-1]==count:
            arr2.pop()
            count+=1
        else:
            break

if len(arr2)==0:
    print('Nice')
else:
    print('Sad')