"""
< 사전 - dictionary >
: key-value pair (키와 값으로 쌍을 이룸)
    ex) my_dictionry = {
            5: 25,
            2: 4,
            3: 9,
        }
        print(my_dictionary[3]) : key가 3인 value가 출력

        #값 추가
        my_dictionary[9] = 81

- 활용법

    my_family = {
        '엄마': '김자옥',
        '아빠': '이석진',
        '아들': '이동민',
        '딸': '이지영'
    }

    # value 출력
        print(my_family.values())

    # 값 확인
        print('이지영' in my_family.values())

    # 값을 하나씩
        for value in my_family.value()

    # 키 출력
        print(my_family.key())

    # 키, 값 출력
        for key, value in my_family.items():
        print(key, value)







"""