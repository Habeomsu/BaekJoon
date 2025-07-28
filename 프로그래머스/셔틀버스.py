def solution(n, t, m, timetable):
    answer = ''

    ## 시간 테이블 정렬
    timetable = sorted(timetable)
    new_table = []

    ## 새로운 시간 테이블 생성
    for i in timetable:
        new_time = int(i[:2]) * 60 + int(i[3:])
        new_table.append(new_time)

    ## 시작 시간 + 최대 가능 인원
    now_time = 9 * 60
    max_cnt = n * m
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cnt == max_cnt - 1 and new_table:
                if now_time < new_table[0]:
                    return find_time(now_time)
                else:
                    return find_time(new_table[0] - 1)
            else:
                cnt += 1
                if new_table and now_time >= new_table[0]:
                    new_table.pop(0)
        now_time = now_time + t

    answer = find_time(now_time - t)

    return answer

    ## 시간을 문자열로 되될리기


def find_time(time):
    h = time // 60
    m = time % 60
    result = ''
    if h <= 9:
        h = "0" + str(h)
    else:
        h = str(h)
    if m <= 9:
        m = "0" + str(m)
    else:
        m = str(m)
    result = h + ':' + m
    return result


'''

1. 알아보기 쉽게 시:분 으로 된 timetable을 분으로 변경해준다.
2. timetable을 정렬 하여 준다.
3. 최대 가능 인원을 구해준다.
4. 9시를 기준으로 t분씩 증가하고, n회를 반복하는 반복문을 작성한다.
5. 만약 최대 인원 = 탑승 인원 -1 일 때, timetable의 0번째 원소와 현재 시각을 비교한다.
    5-1. now_time < timetable[0] -> answer = now_time
    5-2. now_time == timetable[0] -> answer = now_time - t
    5-3. now_time > timetable[0] -> answer = timetable[0]-1

'''