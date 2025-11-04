def solution(enroll, referral, seller, amount):
    answer = []
    seller_dict = {}
    n = len(enroll)
    num_dict = {}

    node = [-1] * n
    for i in range(n):
        name = enroll[i]
        num_dict[name] = i
    for i in range(n):
        name = referral[i]
        if name == '-':
            continue
        else:
            idx = num_dict[name]
            node[i] = idx

    def find_money(name, price):
        minus_price = int(price * 0.1)
        save_price = price - minus_price
        if name in seller_dict:
            seller_dict[name] += save_price
        else:
            seller_dict[name] = save_price
        num_idx = num_dict[name]
        next_num = node[num_idx]
        if next_num == -1:
            return
        elif minus_price == 0:
            return
        else:
            find_money(enroll[next_num], minus_price)

    for i in range(len(seller)):
        name, price = seller[i], amount[i] * 100
        find_money(name, price)

    for name in enroll:
        if name not in seller_dict:
            answer.append(0)
        else:
            answer.append(seller_dict[name])

    return answer


'''

1. 각 판매자의 이름 : 금액의 딕셔너리를 만든다.
2. node를 만든다. -> 자신이 위로 올라가는 경우로 만든다.
3. 위로 올라가면서 10% 만큼 준다.



'''