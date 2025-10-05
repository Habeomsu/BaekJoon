def solution(today, terms, privacies):
    answer = []
    today_day = make_day(today)

    terms_dict = {}

    for i in terms:
        a, b = i.split(' ')
        terms_dict[a] = int(b) * 28 - 1

    num = 1

    for i in privacies:
        day, type = i.split(' ')
        end_day = make_day(day) + terms_dict[type]
        if end_day < today_day:
            answer.append(num)
        num += 1

    return answer


def make_day(day):
    day_list = day.split('.')
    for i in range(len(day_list)):
        day_list[i] = int(day_list[i])
    new_day = day_list[0] * 12 * 28 + day_list[1] * 28 + day_list[2]
    return new_day


'''

1. 년,월,일 로 되어있는 날짜를 일로 변경한다.
2. 약관 종류에 따른 유효기간을 더해준다.
3. 비교한다.



'''