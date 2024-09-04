x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
arr1=[x1,x2,x3]
arr2=[y1,y2,y3]
a,b=0,0
for i in range(3):
    if arr1.count(arr1[i])==1:
        a=arr1[i]
    if arr2.count(arr2[i]) == 1:
        b=arr2[i]
print(a,b)