import sys

sys.setrecursionlimit(1000000)


def solution(p):
    answer = ''

    def find_sol(string):
        if string == '':
            return ""
        u, v = div(string)
        if find_all(u):
            return u + find_sol(v)
        else:
            return '(' + find_sol(v) + ')' + change(u)

    answer += find_sol(p)
    return answer


def div(string):
    u = ""
    v = ""
    cnt1 = 0
    cnt2 = 0
    for i in range(len(string)):
        if string[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            u = u + string[:i + 1]
            v = v + string[i + 1:]
            break
    return u, v


def find_all(string):
    que = []
    for i in string:
        que.append(i)
        while len(que) >= 2:
            if que[-2] == '(' and que[-1] == ')':
                que.pop(-1)
                que.pop(-1)
            else:
                break
    if len(que) == 0:
        return True
    else:
        return False


def change(string):
    string = string[1:-1]
    new_string = ''
    for i in string:
        if i == '(':
            new_string += ')'
        else:
            new_string += '('

    return new_string


'''
1. find_sol(str) 함수를 만든다. -> find_sol 함수
2. u,v 를 반환하는 함수를 만든다. -> div 함수
    1-1. u는 (,)쌍의 갯수가 맞아야한다.
3. u 가 올바른 문자열인지 확인하는 함수를 만든다. -> find_all 함수
4. u 가 올바른 문자열일 경우 u + find_sol(v) 를 최종적으로 반환한다.
5. u 가 올바른 문자열이 아닐 경우, "("+ find_sol(v) + ")"
6. u 의 첫번째와 마지막 문자열 제거하고, 나머지는 괄호 방향을 뒤집는 함수를 만든다. -> change 함수



'''