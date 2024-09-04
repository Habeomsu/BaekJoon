n = int(input())
answer=-1
a= n//5
b=0
stop = False
for i in range(a,-1,-1):
    for j in range(167):
        if 5*i +3*j == n:
            answer=i+j
            stop =True
            break
        elif 5*i +3*j >n:
            break
    if stop ==True:
        break
print(answer)