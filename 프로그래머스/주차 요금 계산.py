import math


def solution(fees, records):
    answer = []
    time_dict = {}
    car_set = set()
    car_fee = []
    acc_dict = {}

    for i in records:
        time, number, record = i.split(' ')

        ## 입차일 경우
        if record == 'IN':
            minute = to_min(time)
            time_dict[number] = minute
            car_set.add(number)

        ## 출차일 경우
        if record == 'OUT':
            minute = to_min(time)
            last_minute = time_dict[number]
            total_minute = minute - last_minute
            if number in acc_dict:
                acc_dict[number] += total_minute
            else:
                acc_dict[number] = total_minute
            car_set.remove(number)

    ## 출차 기록이 없는 차량 시간 구하기
    for i in car_set:
        total_minute = to_min('23:59') - time_dict[i]
        if i in acc_dict:
            acc_dict[i] += total_minute
        else:
            acc_dict[i] = total_minute

    key_list = list(acc_dict.keys())
    key_list = sorted(key_list)

    for i in key_list:
        total_minute = acc_dict[i]
        if total_minute <= fees[0]:
            price = fees[1]
        else:
            price = fees[1] + math.ceil((total_minute - fees[0]) / fees[2]) * fees[3]
        answer.append(price)

    return answer


def to_min(time):
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])
    result = hour * 60 + minute
    return result


'''

1. records를 반복한다.
2. 입차를 기준으로 딕셔너리를 생성한다. -> 차량 번호 : 시각 ( 시각을 분으로 변경해준다.) -> to_min 함수 이용
3. 출차일 경우 총 이용 시간을 구한 후 누적 딕셔너리에 더해준다.
4. 최종적으로 car_set에 남아있는 차는 출차를 23:59 분에 나간것으로 처리해준다.
5. 차량 번호가 작은 자동차 부터 요금을 구하고 결과값을 구해준다.


'''