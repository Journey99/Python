# 겹치는 숫자 개수 찾기

def count_matching_numbers(list_1, list_2):
    cnt = 0
    for i in list_1:
        for j in list_2:
            if i == j:
                cnt += 1
    return cnt

# 테스트
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))