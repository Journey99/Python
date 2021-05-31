from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    i = 1
    while len(new_guess) < 3:
        guess_num = int(input("{}번째 숫자를 입력하세요: ".format(i)))
        if guess_num not in new_guess:
            new_guess.append(guess_num)
            i += 1
        else:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        for j in range(3):
            if guess[i] == solution[j]:
                if i == j:
                    strike_count += 1
                else:
                    ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

s = 0
b = 0
while s != 3:
    GUESS = take_guess()
    s, b = get_score(GUESS, ANSWER)
    print("{}S {}B".format(s, b))
    tries += 1


print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
