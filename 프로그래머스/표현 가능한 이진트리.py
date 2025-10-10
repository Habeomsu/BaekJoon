def solution(numbers):
    answer = []
    for number in numbers:
        num_2 = make_2(number)
        tree = make_tree(num_2)
        stack = []
        stack.append(tree)

        result = True
        while stack:
            now = stack.pop()

            if len(now) == 1:
                continue

            root = len(now) // 2
            left = now[:root]
            right = now[root + 1:]

            if now[root] == '0':

                if left.find('1') == -1 and right.find('1') == -1:
                    continue
                else:
                    result = False
                    break

            else:
                stack.append(left)
                stack.append(right)

        if result == True:
            answer.append(1)
        else:
            answer.append(0)

    return answer


## 이진수 만들기
def make_2(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        num = num // 2
    return result[::-1]


## 완전 이진 트리 만들기
def make_tree(num_str):
    len_num = len(num_str)
    start = 1
    while len_num >= start:
        start = start * 2
    answer = '0' * (start - 1 - len_num) + num_str
    return answer


## 각각의 루트노드가 0인지 탐색하기
def find(str):
    if len(str) == 1:
        return
    root = len(str) // 2
    left = str[:root]
    right = str[root + 1:]
    if str[root] == 0:
        if len(left) > 0 or len(right) > 0:
            return False
    find(left)
    find(right)
    return True


'''

1. 불가능한 조건을 찾는게 빠르다. -> 101 안된다. why? -> 3개씩 짝이라고 주어졌을때, 가운데가 0이면 불가능하다.

 len(x) + a = 2**n + 1

 1 3 7 15 31 63 127 
11111 -> +2 5 -> 
->0011111
111111 -> +1  6
1111111  7 


1자리일떄 
1~3 사이일때 -> 3자리를맞추기 위해 앞에 0을 붙여준다.
4~7일때 -> 7자리를 맞추기 위해 앞에 0을 붙여준다.
자리를 2**n - 1 로 맞춰준다.
그리고 재귀를 사용하여 루트를 검사해준다. 단, 루트가 0이면 종료하고 0을 리턴한다.


'''