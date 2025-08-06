def solution(key, lock):
    answer = False
    N = len(key)
    M = len(lock)
    new_arr = [[0] * (M + 2 * (N - 1)) for _ in range(M + 2 * (N - 1))]
    for i in range(M):
        for j in range(M):
            new_arr[N + i - 1][N + j - 1] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for x in range(N + M - 1):
            for y in range(N + M - 1):

                for i in range(N):
                    for j in range(N):
                        new_arr[x + i][y + j] += key[i][j]

                if check(new_arr, N - 1, M):
                    return True

                for i in range(N):
                    for j in range(N):
                        new_arr[x + i][y + j] -= key[i][j]

    return answer


def rotate(key):
    N = len(key)
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[j][N - 1 - i] = key[i][j]
    return arr


def check(arr, N, M):
    result = True
    for i in range(M):
        for j in range(M):
            if arr[N + i][N + j] != 1:
                return False
    return True


'''

1. 90도 회전하는 함수를 만든다. -> rotate()
2. 완전 탐색을 위한 새로운 lock 배열을 생성한다. -> M+2*(N-1) 크기의 배열을 만든다
3. 새로 만든 배열의 중앙 부분을 lock 배열로 채워준다.
4. 90도 회전을 4번을 한다
5. 각각의 회전마다 key를 옮겨 가면서 완전탐색을 한다.
6. 새로운 배열의 중앙 부분이 모두 1 인경우 함수를 종료하고 true를 반환한다.
7. 아닐 경우 원래 key를 다시 빼주고 계속 진행한다.




'''