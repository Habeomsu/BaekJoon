def solution(play_time, adv_time, logs):
    answer = ''
    start_logs = []
    end_logs = []
    play_sec = find_sec(play_time)
    adv_sec = find_sec(adv_time)

    total_sec = [0] * (play_sec + 1)

    ## logs 배열을 시작 초, 끝나는 초 배열로 만들어주기
    for i in logs:
        start, end = i.split("-")
        start_logs.append(find_sec(start))
        end_logs.append(find_sec(end))

    ## 전체 초 배열에 동영상 길이 채워주기
    for i in range(len(logs)):
        start = start_logs[i]
        end = end_logs[i]
        total_sec[start] += 1
        total_sec[end] -= 1
    for i in range(1, play_sec + 1):
        total_sec[i] += total_sec[i - 1]

    ## 슬라이딩 윈도우를 활용하여 답 구해주기
    cur = sum(total_sec[:adv_sec])
    best = cur
    best_start = 0

    for i in range(adv_sec, play_sec + 1):
        cur = cur + total_sec[i] - total_sec[i - adv_sec]
        if cur > best:
            best = cur
            best_start = i - adv_sec + 1

    if play_time == adv_time:
        answer = "00:00:00"
        return answer

    answer = to_time(best_start)
    return answer


## 초로 변경하기
def find_sec(time):
    sec = 0
    time = time.split(":")
    sec = int(time[0]) * 60 * 60 + int(time[1]) * 60 + int(time[2])
    return sec


## 시간으로 변경하기
def to_time(time):
    new_time = ''
    h = time // 3600
    m = time % 3600 // 60
    s = time % 3600 % 60
    if h // 10 == 0:
        h = '0' + str(h)
    else:
        h = str(h)
    new_time = new_time + h + ':'
    if m // 10 == 0:
        m = '0' + str(m)
    else:
        m = str(m)
    new_time = new_time + m + ':'
    if s // 10 == 0:
        s = '0' + str(s)
    else:
        s = str(s)
    new_time = new_time + s

    return new_time


'''

1. 모든 시각을 초로 계산한다.
2. 전체 영상 시각 만큼의 크기를 가진 배열을 생성한다.
3. 누적합을 이용해 해당 구간에서 영상을 시청한 인원수를 구해준다.
4. 처음부터 광고시간만큼 점점 증가하면서 누적 재생시간이 큰 시간을 구한다.




'''