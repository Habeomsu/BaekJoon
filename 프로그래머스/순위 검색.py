from collections import defaultdict


def solution(info, query):
    answer = []
    con_dict = defaultdict(list)
    for condition in info:
        condition = condition.split(' ')
        score = int(condition[-1])

        ## 16가지 조합 만들고 점수 넣어주기
        for i in ['-', condition[0]]:
            for j in ['-', condition[1]]:
                for k in ['-', condition[2]]:
                    for l in ['-', condition[3]]:
                        temp = (i, j, k, l)
                        con_dict[temp].append(score)

    ## 딕셔너리안에 value 값을 오름차순 정렬
    for key in con_dict:
        con_dict[key] = sorted(con_dict[key])

    ## query를 이용해서 구하기
    for sol in query:
        sol = sol.replace('and ', '')
        sol = sol.split(' ')
        score = int(sol[-1])
        temp = (sol[0], sol[1], sol[2], sol[3])
        scores = con_dict[temp]

        idx = binary(scores, score)
        length = len(scores) - idx
        answer.append(length)

    return answer


def binary(arr, goal):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= goal:
            end = mid
        else:
            start = mid + 1
    return start


'''

1. info 배열을 for문을 통해 반복한다.
2. info 원소를 조건/- 2가지를 기준으로 4자리를 만든 후 딕셔너리를 만들어준다.
3. 해당 딕셔너리의 value는 점수 배열들이다.
4. query를 반복해준다.
5. 해당되는 key값이 있을 경우 query에 있는 점수 보다 큰 value의 갯수를 구해준다.
6. 이때 이분탐색으로 해준다.




'''