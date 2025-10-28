def solution(user_id, banned_id):
    answer = 0

    n = len(banned_id)

    banned_list = [[] for _ in range(len(banned_id))]

    for i in range(len(banned_id)):
        target = banned_id[i]

        for user in user_id:
            if len(target) != len(user):
                continue
            else:
                result = True
                for j in range(len(user)):
                    if target[j] == '*':
                        continue
                    elif target[j] == user[j]:
                        continue
                    else:
                        result = False
                        break
                if result == True:
                    banned_list[i].append(user)

    total = []

    def dfs(banned_list, now_set, idx):
        if idx == n:
            now_list = list(now_set)
            now_list = sorted(now_list)
            total.append(now_list)
            return

        for banned in banned_list[idx]:
            if banned in now_set:
                continue
            else:
                now_set.add(banned)
                dfs(banned_list, now_set, idx + 1)
                now_set.remove(banned)

    start_set = set()
    dfs(banned_list, start_set, 0)

    total_set = set()

    for tot in total:
        tot_str = ''
        for t in tot:
            tot_str += t
        total_set.add(tot_str)

    answer = len(total_set)

    return answer


'''

1. user_id 를 순회한다.
2. user_id 원소르 순차비교하여 '*''이면 넘어가준다.
3. 각 banned_id 에 후보군을 구한다.
4. 구한 후 해당 가능한 조합을 모두 구한다.




'''