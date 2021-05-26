from random import randint

# 랜덤으로 번호 뽑기
def generate_numbers(n):
    num_list = []

    while len(num_list) < n:
        num = randint(1, 45)

        if num not in num_list:
            num_list.append(num)
    return num_list

#보너스 번호 추가
def draw_winning_numbers():
    rand_list = sorted(generate_numbers(6))
    while True:
        bonus = randint(1, 45)
        if bonus not in rand_list:
            rand_list.append(bonus)
            break

    return rand_list

# 겹치는 숫자 개수 찾기
def count_matching_numbers(list_1, list_2):
    cnt = 0
    for i in list_1:
        for j in list_2:
            if i == j:
                cnt += 1
    return cnt

# 당첨금액 출력
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

