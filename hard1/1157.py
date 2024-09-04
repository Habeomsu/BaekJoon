S = input()
S = S.upper()
S = sorted(S)
answer = ''
arr=[]
S1 = list(set(S))
for i in S1:
    arr.append(S.count(i))
M = max(arr)
count = arr.count(M)
if count == 1:
    answer = S1[arr.index(M)]
else:
    answer = '?'
print(answer)
