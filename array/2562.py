max = 0
answer =0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        answer = i+1
print(max)
print(answer)

