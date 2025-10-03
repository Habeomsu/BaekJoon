import sys

plus = []

total=[]
arr=[]
k=3

def back(cnt):
    if cnt == k:
        result=[0]*4
            for i in plus:
                new_arr = []
                for j in range(4):
                    new_arr.append(i%10)
                    i = i//10
                new_arr = new_arr[::-1]
                for k in range(4):
                    if new_arr[k]==1:
                        result[k]=1
            total.append(str(result))
        return
    else:
        for i in range(cnt,len(arr)):
            plus.append(int(arr[i]))
            back(cnt+1)
            plus.pop()