# input - 사용자에게 입력을 받는다

# 예시
name = input("이름을 입력하세요:")
print(name)

# input으로 받는 형은 '문자열'이기 때문에 밑에 코드는 에러
x = input("숫자로 입력하세요:")
print(x + 3)

#->
y = int(input("숫자로 입력하세요:"))
print(y + 3)