from collections import deque
import sys

que1 = deque(list(map(int,sys.stdin.readline().strip('\n'))))
que2 = deque(list(map(int,sys.stdin.readline().strip('\n'))))
que3 = deque(list(map(int,sys.stdin.readline().strip('\n'))))
que4 = deque(list(map(int,sys.stdin.readline().strip('\n'))))

k = int(sys.stdin.readline())

change = []

for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    change.append((a,b))

def turn(que,d):
    if d == 1:
        a = que.pop()
        que.appendleft(a)
    else:
        a = que.popleft()
        que.append(a)
    return que

two_six = [0,0,0,0,0,0]

def change_two_six(two_six,que1,que2,que3,que4):
    two_six[0] = que1[2]
    two_six[1] = que2[6]
    two_six[2] = que2[2]
    two_six[3] = que3[6]
    two_six[4] = que3[2]
    two_six[5] = que4[6]

change_two_six(two_six,que1,que2,que3,que4)

for i in change:
    a,b = i
    if a == 1:
        if two_six[0] == two_six[1]:
            que1 = turn(que1,b)
        else:
            if two_six[2] == two_six[3]:
                que1 = turn(que1,b)
                que2 = turn(que2,-b)
            else:
                if two_six[4] == two_six[5]:
                    que1 = turn(que1, b)
                    que2 = turn(que2, -b)
                    que3 = turn(que3, b)
                else:
                    que1 = turn(que1, b)
                    que2 = turn(que2, -b)
                    que3 = turn(que3, b)
                    que4 = turn(que4, -b)
        change_two_six(two_six,que1,que2,que3,que4)
    elif a == 2:
        if two_six[0] != two_six[1]:
            que1 = turn(que1, -b)

        if two_six[2] == two_six[3]:
            que2 = turn(que2, b)
        else:
            if two_six[4] == two_six[5]:
                que2 = turn(que2, b)
                que3 = turn(que3, -b)
            else:
                que2 = turn(que2, b)
                que3 = turn(que3, -b)
                que4 = turn(que4, b)
        change_two_six(two_six, que1, que2, que3, que4)
    elif a == 3:
        if two_six[4] != two_six[5]:
            que4 = turn(que4, -b)
        if two_six[2] == two_six[3]:
            que3 = turn(que3, b)
        else:
            if two_six[0] == two_six[1]:
                que3 = turn(que3, b)
                que2 = turn(que2, -b)
            else:
                que3 = turn(que3, b)
                que2 = turn(que2, -b)
                que1 = turn(que1, b)
        change_two_six(two_six, que1, que2, que3, que4)
    else:
        if two_six[4] == two_six[5]:
            que4 = turn(que4, b)
        else:
            if two_six[2] == two_six[3]:
                que4 = turn(que4, b)
                que3 = turn(que3, -b)
            else:
                if two_six[0] == two_six[1]:
                    que4 = turn(que4, b)
                    que3 = turn(que3, -b)
                    que2 = turn(que2, b)
                else:
                    que4 = turn(que4, b)
                    que3 = turn(que3, -b)
                    que2 = turn(que2, b)
                    que1 = turn(que1, -b)
        change_two_six(two_six, que1, que2, que3, que4)

result = 0

def find_result(result,que1,que2,que3,que4):
    if que1[0] == 1:
        result += 1
    if que2[0] == 1:
        result += 2
    if que3[0] == 1:
        result += 4
    if que4[0] == 1:
        result += 8

    return result

result = find_result(result,que1,que2,que3,que4)
print(result)




'''


1. 서로 다른 극으로 붙어 있을 경우 반대 방향으로 회전한다.
2. deque를 이용해서 12시 방향을 계속 변경해준다.
3. 만약 시계방향으로 회전하면 -> d = 1 이면, pop 후, appendleft 해준다. -> turn_right 함수
4. 만약 반시계방향으로 회전하면 -> d = -1 이면, popleft 후, append 해준다. -> turn_left 함수
5. 1번 톱니는 2번째 톱니, 2번은 2,6 톱니, 3번은 2,6 톱니, 4번은 6톱니가 중요하다.
6. 돌기전에 2번6번 톱니를 저장하고 전체적으로 톱니바퀴를 회전후 다시 변경해준다.
7. 최종적으로 12시에 위치한 톱니에 따라 결과값을 구한다.



'''