import sys

str = sys.stdin.readline().strip()
boom = list(sys.stdin.readline().strip())

stack = []
boom_len = len(boom)

for i in str:
    stack.append(i)
    if len(stack) >= boom_len:
        if stack[len(stack)-boom_len:] == boom:
            for _ in range(boom_len):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")