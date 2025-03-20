### 최종 스택과 연산식을 보관할 스택을 두개 선언한다..
### 숫자는 바로 넣어주고 연산식은 연산식 스택에 넣어준다.
### 숫자를 넣어주면 연산식에 보관된 연산식을 넣어준다.
### but 다음 연산식이 *, /, (,) 인 경우 해당 연산식을 다시 연산식 배열에 넣고 숫자를 최종에 넣어준다.
### -,+ 가 들어올때는 무조건 빈배열 상태여야한다 ..
### *,/ 가 들어올때 하나라도 존재하면 한개 빼준다

import sys

str = list(sys.stdin.readline().strip())
result=[]
num = []

for i in str:
    if i=='(':
        num.append(i)
    elif i =='-' or i=='+':
        while num and num[-1]!='(':
           result.append(num.pop())
        num.append(i)
    elif i =='*' or i=='/':
        while num and (num[-1]=='*' or num[-1] == '/'):
            result.append(num.pop())
        num.append(i)
    else:
        while num and num[-1] != '(':
            result.append(num.pop())
        num.pop()
for i in range(len(num)):
    result.append(num.pop())

print("".join(result))