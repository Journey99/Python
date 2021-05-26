# 랜덤으로 번호 뽑기

from random import randint

def generate_numbers(n):
    num_list = []

    while len(num_list) < n:
        num = randint(1, 45)

        if num not in num_list:
            num_list.append(num)
    return num_list

# 테스트
print(generate_numbers(6))