n = int(input())

for i in range(n):
    a= int(input())
    b,mod=divmod(a,25)
    c,mod=divmod(mod,10)
    d,mod=divmod(mod,5)
    print(b,c,d,mod)