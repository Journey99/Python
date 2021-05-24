# 숫자 맞히기 게임

import random

answer = random.randint(1, 20)
i = 4
while True:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(i)))
    if guess == answer:
        print("축하합니다. {}번만에 숫자를 맞히셨습니다.".format(5-i))
        break
    elif guess < answer:
        print("up")
    else:
        print("dowm")

    i -= 1

    if i == 0:
        print("아쉽습니다. 정답은 {}였습니다. ".format(answer))
        break