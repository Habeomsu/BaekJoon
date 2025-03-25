from collections import deque


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = int(video_len.replace(":", ""))
    pos = int(pos.replace(":", ""))
    op_start = int(op_start.replace(":", ""))
    op_end = int(op_end.replace(":", ""))
    for i in commands:
        if pos >= op_start and pos < op_end:
            pos = op_end
        if i == 'next':
            pos += 10
            if pos % 100 >= 60:
                pos = (pos // 100 + 1) * 100 + pos % 100 - 60
            if pos > video_len:
                pos = video_len
        elif i == 'prev':
            if pos % 100 < 10:
                pos = (pos // 100 - 1) * 100 + pos % 100 + 60
            pos -= 10
            if pos < 0:
                pos = 0
    if pos >= op_start and pos < op_end:
        pos = op_end
    arr = [i for i in str(pos)]
    que = deque(arr)
    while True:
        if len(que) == 4:
            for i in range(4):
                if i == 2:
                    answer = answer + ":"
                answer = answer + que[i]
            break
        else:
            que.appendleft('0')

    return answer

### pos 에 따라 규칙을 잘 수행한다
### +10 , -10 이후 60이 넘어가면 앞에 +1 해줘야 한다