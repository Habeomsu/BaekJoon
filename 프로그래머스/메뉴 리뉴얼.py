from itertools import combinations


def solution(orders, course):
    answer = []
    order_dict = {}

    ## 딕셔너리 만들기
    for order in orders:
        for i in range(2, len(order) + 1):
            for j in combinations(order, i):
                j = list(j)
                j = sorted(j)
                j = "".join(j)
                if j in order_dict:
                    order_dict[j] += 1
                else:
                    order_dict[j] = 1

    for i in course:
        now_result = find_order(order_dict, i)
        for j in now_result:
            answer.append(j)

    answer = sorted(answer)
    return answer


def find_order(dict, course):
    arr = []
    result = []
    for i in dict:
        if len(i) == course:
            arr.append([dict[i], i])
    if len(arr) == 0:
        return result
    else:
        arr = sorted(arr, key=lambda x: [-x[0], x[1]])
        if arr[0][0] == 1:
            return result
        else:
            now_num = arr[0][0]
            while arr:
                next = arr.pop(0)
                if now_num == next[0]:
                    result.append(next[1])
                else:
                    break
    return result


'''

1. orders의 각 원소를 길이가 2부터 len(order)까지 combinations을 통해서 order_dict에다가 여태까지 나온 횟수를 구한다. 
2. course에 해당하는 원소의 값은 order_dict에 Key값의 길이를 기준으로 판단한다. -> find_order 함수
    2.1 해당하는 order_dict의 key가 존재하면 [value, key] 순으로 새로운 배열에 넣어준다.
    2.2 정렬을 해준다. -> key = lambda x : [-x[0],x[1]]
    2.3 만약 가장 첫번째 원소에 [0][0] 값이 1 이면 한번만 주문된 경우로 넘어간다.
    2.4 만약 1이 아니라면 가장 앞의 원소의 나온 횟수를 구하고 해당 수와 같은 원소들은 최종 반환값에 추가한다.
3. 최종 반환하기 전에 정렬을 해준다.

'''