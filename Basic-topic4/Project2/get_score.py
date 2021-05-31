# 스트라이크와 볼 개수 출력

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


# 테스트
s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
print(s_1, b_1)

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)
