# 유저에게 숫자 3개 예측받기

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

print(take_guess())

