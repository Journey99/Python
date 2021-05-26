# 정렬된 숫자 리스트와 보너스 숫자 함께 리턴

from random import randint

def generate_numbers(n):
    num_list = []

    while len(num_list) < n:
        num = randint(1, 45)

        if num not in num_list:
            num_list.append(num)
    return num_list


def draw_winning_numbers():
    rand_list = sorted(generate_numbers(6))
    while True:
        bonus = randint(1, 45)
        if bonus not in rand_list:
            rand_list.append(bonus)
            break

    return rand_list

# 테스트
print(draw_winning_numbers())


# 해설의 다른 풀이
# winning_numbers = generate_numbers(7)
# return sorted(winning_numbers[:6]) + winning_numbers[6:]