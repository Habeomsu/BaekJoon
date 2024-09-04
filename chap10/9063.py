a = int(input())
arr1=[]
arr2=[]
for i in range(a):
    x,y = map(int,input().split())
    arr1.append(x)
    arr2.append(y)
if a == 1 :
    print(0)
else:
    maxX = max(arr1)
    minX = min(arr1)
    maxY = max(arr2)
    minY = min(arr2)
    result = ((maxX-minX) *(maxY -minY))
    print(result)