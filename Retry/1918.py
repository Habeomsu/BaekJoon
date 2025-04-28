'''

부호는 ( , + , - , * , / , ) 이다
숫자가 나오면 결과 배열에 넣어 준다
대기 배열이 빈 배열인 상태에 부호가 들어가면 부호를 넣어준다.
1. ( 인경우 넘어간다.
2. ) 인경우 ( 나올때 까지 모든 배열을 팝시킨다.
3. +,- 인경우 앞에 +,-,*,/ 를 팝시킨다.
4. *,/ 인경우 앞이 +,- 인경우 빈배열에 집어넣은다.


'''


import sys

str = list(sys.stdin.readline().strip())

result = []
bean = []

while str:
    now = str.pop(0)
    if now not in ['+','-','*','/','(',')']:
        result.append(now)
    elif now == '(':
        bean.append(now)
    elif now == '+' or now =='-':
        while bean and bean[-1] != '(':
            result.append(bean.pop())
        bean.append(now)
    elif now == '*' or now == '/':
        if bean and (bean[-1] == '*' or bean[-1] == '/'):
            result.append(bean.pop())
        bean.append(now)
    else:
        while bean:
            new = bean.pop()
            if new == '(':
                break
            else:
                result.append(new)

while bean:
    result.append(bean.pop())

print("".join(result))