def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        start = startday
        cnt = 0
        schedule = schedules[i] + 10
        if schedule % 100 >= 60:
            schedule = (schedule // 100 + 1) * 100 + (schedule % 100 - 60)
        for j in range(7):
            if start % 7 == 6 or start % 7 == 0:
                cnt += 1
                start += 1
            else:
                if timelogs[i][j] > schedule:
                    break
                else:
                    cnt += 1
                    start += 1
        if cnt == 7:
            answer += 1

    return answer

### 사원 수만큼 for문을 돌린다.
### 토요일, 일요일은 제외한다. startday == 6,7 인 경우는 제외
### for 문을 돌리고 start day를 하나씩 올린다.
### 목표 시간 +10이 60분 이상이면 시간을 변경해줘야한다.