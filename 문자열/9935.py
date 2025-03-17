### 문자열이 포함되어 있는경우 문자열을 제거한다. 단, 문자열내에 여러개가 포함될 경우 모드 제거한다.
### 배열을 기준으로 처음부터 폭발문자열의 길이 만큼이 같다면 해당문자열은
### 해당 문자열을 푸쉬하기전에 폭발 문자열과 비교하여 맞으면 일단 넣어두고 cnt를 +1 한다
### stack 이 비어있는 경우 FRULA 출력
### 문자열 폭파후 해당 스택을 다시 폭발 알고리즘 적용 만약 스택이 이전과 같다면 break.
##### 그냥 계속 넣어주다가 슬라이싱을 활용하자 .....

import sys

str = sys.stdin.readline().strip()
boom = list(sys.stdin.readline().strip())

stack = []

for i in str:
    stack.append(i)
    if stack[len(stack)-len(boom):len(stack)] == boom:
        for _ in range(len(boom)):
            stack.pop()

if len(stack)==0 :
    print("FRULA")
else:
    print("".join(stack))