a,b,c = map(int,input().split())
Max = max(a,b,c)
if Max < a+b+c-Max:
    print(a+b+c)
else:
    print(2*(a+b+c-Max)-1)