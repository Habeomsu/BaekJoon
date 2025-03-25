def solution(friends, gifts):
    answer = 0
    cnt = 0
    name_to_idx = {}
    for idx, friend_name in enumerate(friends):
        name_to_idx[friend_name] = idx
    arr = [[0]*len(friends) for _ in range(len(friends))]
    for gift in gifts:
        giver, receiver = gift.split()
        a = name_to_idx[giver]
        b = name_to_idx[receiver]
        arr[a][b] += 1
    final = [0]*len(friends)
    get_gift = [0]*len(friends)
    give_gift = [0]*len(friends)
    for i in range(len(friends)):
        for j in range(len(friends)):
            get_gift[j] += arr[i][j]
            give_gift[i] += arr[i][j]
    for i in range(len(friends)):
        for j in range(i,len(friends)):
            if arr[i][j] > arr[j][i]:
                final[i] +=1
            elif arr[i][j] == arr[j][i]:
                me_num = give_gift[i]-get_gift[i]
                you_num = give_gift[j]-get_gift[j]
                if me_num > you_num:
                    final[i] +=1
                elif me_num<you_num:
                    final[j] +=1
            else:
                final[j] +=1
    answer = max(final)
    return answer

### 이차원배열을 만든다.
### 자기가 속한 열은 자기가 받은 선물의 총 합이다.
### 자기가 속한 행은 자기가 준 선물의 총 합이다.


