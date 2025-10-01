from collections import deque

def solution(queue1, queue2):
    answer = 0

    que1_sum = sum(queue1)
    que2_sum = sum(queue2)
    total_len = len(queue1) + len(queue2)

    que1 = deque(queue1)
    que2 = deque(queue2)

    while True:
        if answer > total_len * 2:
            answer = -1
            break

        if que1_sum == que2_sum:
            break
        elif que1_sum > que2_sum:
            num = que1.popleft()
            que2.append(num)
            que1_sum -= num
            que2_sum += num
        elif que1_sum < que2_sum:
            num = que2.popleft()
            que1.append(num)
            que1_sum += num
            que2_sum -= num
        answer += 1

    return answer