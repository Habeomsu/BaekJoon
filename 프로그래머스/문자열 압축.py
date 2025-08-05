def solution(s):
    answer = 0
    length = len(s)
    answer = length
    for i in range(1, length // 2 + 1):
        arr = split_string(s, i)
        now_len = zip_string(arr)
        if answer >= now_len:
            answer = now_len

    return answer


def split_string(string, length):
    arr = []
    cnt = 0
    while True:
        if cnt + length >= len(string):
            break
        else:
            now = string[cnt:cnt + length]
            arr.append(now)
            cnt = cnt + length
    arr.append(string[cnt:])
    return arr


def zip_string(array):
    zip = ""
    cnt = 0
    before = array[0]
    for i in array:
        if i == before:
            cnt += 1
        else:
            if cnt != 1:
                before = str(cnt) + before
            zip += before
            before = i
            cnt = 1
    if cnt != 1:
        before = str(cnt) + before
    zip += before
    return len(zip)


'''


1. 주어진 문자열 s의 길이를 구한다.
2. 1부터 최대 길이 까지 문자열을 나눈다. -> split_string 함수
3. 나눈 문자열을 가지고 압축된 문자열을 구한다. -> zip_string 함수
4. 반복해서 가장 짧은 수를 구한다.



'''