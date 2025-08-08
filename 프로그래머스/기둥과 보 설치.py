def solution(n, build_frame):
    answer = []

    for i in build_frame:
        x, y, a, b = i
        if b == 1:
            if can_install(x, y, a, answer):
                answer.append([x, y, a])
        else:
            answer.remove([x, y, a])
            arr = affect(x, y, a)
            for i in arr:
                nx, ny, na = i
                if [nx, ny, na] in answer and not can_install(nx, ny, na, answer):
                    answer.append([x, y, a])
                    break

    answer = sorted(answer, key=lambda x: [x[0], x[1], x[2]])
    return answer


def can_install(x, y, a, arr):
    if a == 0:
        return (
                y == 0 or
                [x, y - 1, 0] in arr or
                [x - 1, y, 1] in arr or
                [x, y, 1] in arr
        )
    else:
        return (
                [x, y - 1, 0] in arr or
                [x + 1, y - 1, 0] in arr or
                ([x - 1, y, 1] in arr and [x + 1, y, 1] in arr)
        )


def affect(x, y, a):
    if a == 0:
        return [[x, y + 1, 0], [x - 1, y + 1, 1], [x, y + 1, 1]]
    else:
        return [[x, y, 0], [x + 1, y, 0], [x - 1, y, 1], [x + 1, y, 1]]


'''

1. 배열을 차례대로 실행한다.
2. b가 1 일 경우 result 배열에 [x,y,a] 추가 ->  can_install 함수 생성
    2-1. a가 0일 경우 -> 기둥일 경우 
        2-1-1. 바닥일 경우 -> y 가 0 일 경우 항상 가능 
        2-1-2. 기둥일 경우 -> result 배열에 [x,y-1,0] 가 존재하면 가능
        2-1-3. 보일 경우 -> result 배열에 [x-1,y,1] 또는 [x,y,1] 가 존재하면 가능
    2-2. a가 1일 경우 -> 보일 경우
        2-2-1. 왼쪽 끝부분이 기둥일 경우 -> [x,y-1,0] 이 존재하면 가능
        2-2-2. 오른쪽 끝부부인 기둥일 경우 -> [x+1,y-1,0] 이 존재하면 가능
        2-2-3. 양쪽이 보인 경우 -> [x-1,y,1] 과 [x+1,y,1] 이 존재하면 가능
3. b가 0 일 경우 result 배열에서 삭제
    3-1. 일단 해당 기둥이나 보를 삭제 
    3-2. 삭제시 관련된 기둥이나 보의 배열을 생성 -> affect 함수 생성
        3-2-1. a 가 0일 경우 -> 기둥일 경우
            3-2-1-1. 바로 위 기둥 -> [x,y+1,0]
            3-2-1-2. 위에 양옆 보 -> [x-1,y+1,1] , [x,y+1,1]
        3-2-2. a 가 1일 경우 -> 보일 경우
            3-2-2-1. 바로 양옆 기둥 -> [x,y,0] , [x+1,y,0]
            3-2-2-2. 바로 양옆 보 -> [x-1,y,1], [x+1,y,1]
    3-3. affect함수를 통해 삭제시 영향을 받는 구조물들이 설치가 불가능하면 삭제 불가 
4. result 배열을 정렬해준다. -> lambda x : (x[0],x[1],x[2])




'''