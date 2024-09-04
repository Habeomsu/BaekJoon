a, b, c = map(int,input().split())
answer = 0
if (c-a)%(a-b) == 0:
    answer= (c-a)/(a-b) +1
else:
    answer=  (c-a)//(a-b) +2
print(int(answer))