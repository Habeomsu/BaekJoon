from collections import deque

def solution(players, m, k):
    answer = 0
    que = deque()
    for i in range(24):
        while que:
            if i-que[0] >=k:
                que.popleft()
            else:
                break
        player = players[i]
        need_server = player // m
        if len(que) < need_server:
            for _ in range(need_server-len(que)):
                que.append(i)
                answer +=1
    return answer

### 서버를 생성하면 해당 서버는 k 시간만큼 존재한다
### 해당 인원 // m 이 해당 시간에 존재해야 하는 서버에 수이다
### 그럼 서버를 어떻게 관리하는 게 좋을 지 정해야한다.
### deque를 만들고 가장 왼쪽에 있는 큐가 현재 시간 - 큐 시간 > m 이면 팝한다.