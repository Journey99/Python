# 단어장 만들기

with open('vocabulary.txt', 'w', encoding="utf-8") as f:
    while True:
        eng_word = input("영어 단어를 입력하세요: ")
        if eng_word == 'q':
            break

        kor_word = input("한국어 뜻을 입력하세요: ")
        if kor_word == 'q':
            break

        f.write('{}: {}\n'. format(eng_word, kor_word))

