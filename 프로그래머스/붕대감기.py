def solution(bandage, health, attacks):
    answer = 0
    attack_cnt = 0
    heal_cnt = 0
    answer = health
    final_time = attacks[-1][0]
    for i in range(1, final_time + 1):
        if attacks[attack_cnt][0] != i:
            answer = answer + bandage[1]
            heal_cnt += 1
            if heal_cnt == bandage[0]:
                answer += bandage[2]
                heal_cnt = 0
        elif attacks[attack_cnt][0] == i:
            answer = answer - attacks[attack_cnt][1]
            heal_cnt = 0
            attack_cnt += 1
        if answer > health:
            answer = health
        elif answer <= 0:
            answer = -1
            break

    return answer

### total 시간을 0 부터 마지막 시간 까지
### 만약 공격이 없다면 cnt +=1
### 공격이 들어오면 cnt = 0
### cnt == bandage[0] health + bandage[2]
