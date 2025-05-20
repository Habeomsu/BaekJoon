def solution(s):
    answer = True
    stack = []
    for i in s:
        stack.append(i)
        while stack:
            if stack[-2:] == ['(',')']:
                stack.pop()
                stack.pop()
            else:
                break
    if len(stack)>0:
        return False
    return True