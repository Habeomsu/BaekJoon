answer=''
a, b =map(int,input().split())
while a>0:
    a,mod = divmod(a,b)
    if mod<10:
        answer=answer+str(mod)
    else:
        answer=answer+chr(mod+55)
print(answer[::-1])
