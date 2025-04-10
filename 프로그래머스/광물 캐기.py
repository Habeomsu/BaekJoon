Min = 100000000000


def solution(picks, minerals):
    answer = 0
    back(picks, minerals, 0, 0)
    return Min


def back(picks, minerals, idx, trying):
    global Min
    if idx >= len(minerals) or sum(picks) == 0:
        Min = min(Min, trying)
        return

    for i in range(3):
        if picks[i] > 0:
            new_trying = 0
            for j in range(5):
                if idx + j >= len(minerals):
                    break
                mineral = minerals[idx + j]
                if i == 0:
                    new_trying += 1
                elif i == 1:
                    if mineral == "diamond":
                        new_trying += 5
                    else:
                        new_trying += 1
                else:
                    if mineral == "diamond":
                        new_trying += 25
                    elif mineral == "iron":
                        new_trying += 5
                    else:
                        new_trying += 1
            picks[i] -= 1
            back(picks, minerals, idx + 5, trying + new_trying)
            picks[i] += 1


'''

'''