"""
< 모듈 - moduel >
: 파이썬 모듈은 전역변수, 함수등 을 모아둔 파일이다.

- 사용방법
 : import 모듈이름

ex)
- import math
    1. n = math.factorial(i)
    2. math.log10
    3. math.cos
    4. math.pi
    .........

- import random
    1. random.random() -> 0과 1사이의 랜덤한 수
    2. random.randint(a, b) -> a와 b 사이에 어떤 랜덤한 정수를 리턴
    3. random.uniform(a, b) -> a와 b 사이에 어떤 랜덤한 소수 리턴
    .........

- import datetime
    1. datetime.datetime(년도, 월, 일, 시, 분, 초)
    2. datetime.datetime.now() -> 지금 이 순간의 날짜와 시간
    3. today= datetime.datetime.now()
            today.year
            today.month
            today.day
            ..........
"""