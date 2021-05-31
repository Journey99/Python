# 온도 바꾸기

# 화씨 온도에서 섭씨 온도로 바꿔 주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return round((((fahrenheit) - 32) * 5) / 9, 1)


temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = fahrenheit_to_celsius(temperature_list[i])
    i += 1
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력