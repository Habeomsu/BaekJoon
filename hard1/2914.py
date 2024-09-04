arr=['c=','c-','dz=','d-','lj','nj','s=','z=']
answer = input()
for i in range(8):
    answer=answer.replace(arr[i],'1')
print(len(answer))