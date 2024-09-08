import sys

answer=sys.stdin.readline().strip("\n")
answer=sorted(answer)
dic={}
for i in answer:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
count =0
result=''
result2=''
for key,value in dic.items():
    if count ==2:
        break
    if value %2==1:
        count +=1
        result += key*(value//2)
        result2+= key
    else:
        result += key*(value//2)
if count ==2 :
    print("I'm Sorry Hansoo")
else:
    print(result+result2+result[::-1])