import sys

r, c, k = map(int,sys.stdin.readline().split())

arr = []
for i in range(3):
    arr.append(list(map(int,sys.stdin.readline().split())))

def new_sort(arr):
    new_arr = []
    dict = {}
    temp = []
    for i in arr:
        if i==0:
            continue
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for j in dict:
        temp.append([j,dict[j]])
    temp = sorted(temp, key = lambda x:(x[1],x[0]))
    for i in temp:
        a,b = i
        new_arr.append(a)
        new_arr.append(b)
        if len(new_arr) >= 100:
            break
    return new_arr[:100]

def make_zero(arr):
    Max_len = 0
    ## 최대 길기 구하기
    for i in arr:
        if Max_len < len(i):
            Max_len = len(i)

    if Max_len >= 100:
        Max_len = 100

    for i in range(len(arr)):
        padding = Max_len - len(arr[i])
        for _ in range(padding):
            arr[i].append(0)
    return arr

time = 0

while time <= 100:

    if 0<= r-1 <len(arr) and 0<= c-1 < len(arr[0]) and arr[r-1][c-1] == k:
        break

    row_num, col_num = len(arr), len(arr[0])

    if row_num >= col_num:
        temp = []
        for i in arr:
            temp.append(new_sort(i))
        temp = make_zero(temp)
        arr = temp
    else:
        new_arr = []
        temp = []
        ## 열을 추출해서 새로운 배열로 만들기
        for j in range(len(arr[0])):
            row_arr = []
            for i in range(len(arr)):
                row_arr.append(arr[i][j])
            new_arr.append(row_arr)
        ## 정렬하기
        for i in new_arr:
            temp.append(new_sort(i))
        ## 0으로 채우기
        temp = make_zero(temp)
        ## 원래 배열처럼 다시 만들기
        real_arr = [[] for _ in range(len(temp[0]))]
        for i in temp:
            for j in range(len(i)):
                real_arr[j].append(i[j])
        arr = real_arr

    time +=1

if time == 101:
    print(-1)
else:
    print(time)


'''

1. 행의 수와 열의 수를 구한다. -> len(arr) : 행의 수, len(arr[0]) : 열의 수
2. 행의 수와 열의 수를 비교한다.
    2.1 행의 수가 열의 수보다 크거나 같을 경우 -> 행을 기준으로 정렬한다.
    2.2 열의 수가 행의 수보다 클 경우 -> 열을 기준으로 정렬한다.
3. 각 행의 정렬을 arr를 순회한다. 각 열의 정렬을 어떻게 할까?
4. 정렬 하는 함수를 만들어준다. -> def new_sort()
5. 각각의 행 또는 열을 정렬 후 각각의 정렬된 값의 길이를 구해준다.
6. 가장 킨 행 또는 열을 기준으로 부족한 만큼 0을 채워준다.
7. 만약 길이가 100보다 크 100을 기준으로 짤라준다.
8. arr[r][c] == k 인 경우를 구해준다.

'''