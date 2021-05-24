# 단어 퀴즈

with open('vocabulary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        data = line.strip().split(": ")
        eng = data[0]
        kor = data[1]

        answer = input("{}: ".format(eng))
        if answer == kor:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(kor))