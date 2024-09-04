n = int(input())
answer=''
result=0
for i in range(n):
    a=input()
    for i in range(len(a)):
        if i==0:
            answer=answer+a[i]
        else:
            if a[i] != a[i-1]:
                answer=answer+a[i]
    if len(answer) == len(set(answer)):
        result +=1
    answer=''
print(result)



