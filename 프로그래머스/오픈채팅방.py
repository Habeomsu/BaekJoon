def solution(record):
    answer = []
    id_dict = dict()
    cmd_dict = {'Enter': "님이 들어왔습니다.", 'Leave': "님이 나갔습니다."}

    for i in record:
        arr = i.split(" ")
        if arr[0] in ('Enter', 'Change'):
            id_dict[arr[1]] = arr[2]

    for i in record:
        arr = i.split(" ")
        if arr[0] in ('Enter', 'Leave'):
            result = id_dict[arr[1]] + cmd_dict[arr[0]]
            answer.append(result)

    return answer


'''

1. record를 반복해서 명령어, 아이디, 닉네임으로 분리를 해준다.
2. 아이디 : 닉네임 으로 딕셔너리를 만들어준다.
3. 명령어의 따라 "OOO님이 들어왔습니다.","OOO님이 나갔습니다."를 answer 배열에 넣어준다.
4. 아이디 배열을 생성후 명령어가 Enter, Leave 일경우 집어넣어준다.
5. 명령어가 Enter, Change일 경우 아이디 : 닉네임 딕셔너리를 변경해준다.
6. id_dict을 이용해서 아이디 배열과 answer을 합쳐준다.




'''