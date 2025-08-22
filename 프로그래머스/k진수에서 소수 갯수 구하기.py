def solution(n, k):
    answer = 0
    new_digit = make(n, k)
    new_digit = new_digit.split('0')
    for i in new_digit:
        if len(i) >= 1:
            if isPrime(int(i)):
                answer += 1

    return answer


def make(n, k):
    result = ''
    while n > 0:
        result += str(n % k)
        n = n // k
    return result[::-1]


def isPrime(digit):
    if digit == 1:
        return False
    for i in range(2, int(digit ** 0.5) + 1):
        if digit % i == 0:
            return False
    return True


'''

1. 진법 변환을 한다. -> make() 함수
2. 0을 기준으로 나누어 준다. 
3. 소수인지 판단한다. -> isprime() 함수
4. 소수가 맞으면 result 를 더해준다. 



'''