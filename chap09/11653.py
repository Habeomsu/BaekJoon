a = int(input())
arr=[]
i=2
if a==1:
    pass
while a !=1:
    if a%i==0:
        a=a/i
        print(i)
    else:
        i = i+1