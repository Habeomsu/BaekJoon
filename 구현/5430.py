# ### R -> 뒤집기 ( arr =arr[::-1] )
# ### D -> 배열 가장 앞에 숫자 빼기 (각각의 함수를 정의한다)
# ### 데큐를 사용해서
# deque 선언해서 R 일경우 cnt +1 해주고
### D 일때 cnt 홀수이면 pop(), cnt 짝수 popleft()
import sys
from collections import deque
T = int(sys.stdin.readline())

for i in range(T):
    fun= input()
    fun = str(fun).replace('RR','')
    fun = list(fun)
    length = int(sys.stdin.readline())
    string = input()
    string =string.replace('[','')
    string = string.replace(']','')
    arr = string.split(',')
    que = deque()
    for i in range(length):
        que.append(int(arr[i]))
    cnt = 0
    error = False
    for i in fun:
        if i == 'R':
            cnt +=1
        elif i == 'D':
            if len(que)==0:
                error = True
                break
            if cnt % 2 ==0:
                que.popleft()
            else:
                que.pop()
    result=[]
    if error == True:
        print('error')
    else:
        if cnt %2 ==1:
            for i in range(len(que)):
                result.append(que.pop())
        else:
            for i in range(len(que)):
                result.append(que.popleft())
        result = str(result)
        result = result.replace(' ','')
        print(result)