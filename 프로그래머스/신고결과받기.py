def solution(id_list, report, k):
    answer = []

    for _ in range(len(id_list)):
        answer.append(0)

    ## 신고 딕셔너리를 만든다.
    report_dict = {}

    ## 신고 딕셔너리를 완성한다.
    for names in report:
        a, b = names.split(" ")
        if b not in report_dict:
            report_dict[b] = [a]
        else:
            report_dict[b].append(a)

    ## 신고가 k이상이면 메세지를 발송한다.
    for name in report_dict:
        arr = report_dict[name]
        arr = set(arr)
        if len(arr) >= k:
            for id in list(arr):
                idx = id_list.index(id)
                answer[idx] += 1

    return answer


'''

1. 신고당한 유저 딕셔너리를 만든다. -> report_dict
2. report_dict에 배열을 생성하여 신고한 유저를 넣어준다.
3. 마지막까지 report배열을 돌고 k이상 신고당한 유저면 id_list에 따른 새로운 아이디 배열에 횟수를 더해준다.


'''