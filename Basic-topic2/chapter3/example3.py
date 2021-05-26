# 우승상금

price = 50000000
man = 1
i = 1
woman = 1100000000

while i <= 28:
    price = price * 1.12
    man = price
    i += 1

if (int(man) > woman):
    diff = int(man) - woman
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(diff))
else:
    diff = woman - int(man)
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(diff))