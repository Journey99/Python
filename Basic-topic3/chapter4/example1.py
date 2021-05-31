# 자리수 합

# 자리수 합 리턴
def sum_digit(num):
    total = 0
    str_num = str(num)
    for i in str_num:
        total += int(i)
    return total


result = 0
for j in range(1, 1001):
    result += sum_digit(j)

print(result)