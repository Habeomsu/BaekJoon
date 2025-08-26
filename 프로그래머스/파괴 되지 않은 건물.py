def solution(board, skill):
    answer = 0
    sum_arr = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    ## 변화량 배열 만들기
    for i in skill:
        t, x1, y1, x2, y2, d = i
        if t == 1:
            d = -d
        sum_arr[x1][y1] += d
        sum_arr[x2 + 1][y1] -= d
        sum_arr[x1][y2 + 1] -= d
        sum_arr[x2 + 1][y2 + 1] += d

    ## 좌 -> 우 누적합
    for i in range(len(sum_arr)):
        for j in range(1, len(sum_arr[0])):
            sum_arr[i][j] = sum_arr[i][j - 1] + sum_arr[i][j]

    ## 위 -> 아래 누적합
    for j in range(len(sum_arr[0])):
        for i in range(1, len(sum_arr)):
            sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j]

    ## board + 누적합
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = board[i][j] + sum_arr[i][j]

    ## board 에서 0보다 큰 내구도 구하기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer


'''

1. type 이 1 인 경우 degree만큼 내구도를 낮춘다.
2. type 이 2 인 경우 degree만큼 내구도를 높인다.
3. 주어진 조건으로 이중 for문을 사용하면 정확성은 성공이지만 효율성은 실패할 것 같다.
4. 누적합을 이용한다.
5. 2차원 배열의 누적합은 x1,y1,x2,y2 를 기준으로 x1,y1 = +n, x1,y1+1 = -n, x2+1,y1 = -n , x2+1, y2+1 = n 이다. 
6. 그후 좌 -> 우 , 위 -> 아래로 값을 이전 값과 더해준다.
7. 최종적으로 해당 배열을 원래 board배열과 더해준다.



'''