# 피타고라스

for a in range(1, 1000):
    for b in range(1, 1000):
        if a< b < 1000-(a+b) and a**2 + b**2 == (1000-(a+b))**2:
            print(a*b*(1000-a-b))

# 리스트 뒤집기

numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(len(numbers) // 2):
    right = len(numbers) - left - 1
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))