# 피보나치 수열

num_1 = 1
num_2 = 1
i = 1

while i <= 50:
    print(num_1)
    nth = num_1 + num_2
    num_1 = num_2
    num_2 = nth
    i += 1


# 구구단

i = 1
j = 1

while i <= 9:
    while j <=9:
        print("{} * {} = {}".format(i, j, i*j))
        j += 1
    j = 1
    i += 1