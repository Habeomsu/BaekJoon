a= int(input())
arr =list(map(int,str(a)))
num = len(arr)
answer=0
if a<=18:
    for i in range(a):
        arr2=list(map(int,str(i)))
        if a==sum(arr2)+i:
            answer=i
            break;
else:
    b=a-9*num
    while b<=a:
        arr1 = list(map(int,str(b)))
        if b+sum(arr1) == a:
            answer=b
            break;
        else:
            b=b+1
print(answer)