"""
리스트와 문자열은 굉장히 비슷하다.

-인덱싱 (Indexing)
두 자료형은 공통적으로 인덱싱이 가능
    ex) alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        print(alphabets_list[0])
        print(alphabets_list[1])
        print(alphabets_list[4])
        print(alphabets_list[-1])

        # 알파벳 문자열의 인덱싱
        alphabets_string = 'ABCDEFGHIJ'
        print(alphabets_string[0])
        print(alphabets_string[1])
        print(alphabets_string[4])
        print(alphabets_string[-1])


- for 반복문
두 자료형은 공통적으로 인덱싱이 가능. 따라서 for 반복문에도 활용할 수 있다.
    ex) # 알파벳 리스트의 반복문
        alphabets_list = ['C', 'O', 'D', 'E', 'I', 'T']
        for alphabet in alphabets_list:
        print(alphabet)

        # 알파벳 문자열의 반복문
        alphabets_string = 'CODEIT'
        for alphabet in alphabets_string:
        print(alphabet)


-슬라이싱 (Slicing)
두 자료형은 공통적으로 슬라이싱이 가능
    ex) # 알파벳 리스트의 슬라이싱
        alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        print(alphabets_list[0:5])
        print(alphabets_list[4:])
        print(alphabets_list[:4])

        # 알파벳 문자열의 슬라이싱
        alphabets_string = 'ABCDEFGHIJ'
        print(alphabets_string[0:5])
        print(alphabets_string[4:])
        print(alphabets_string[:4])


-덧셈 연산
두 자료형에게 모두 덧셈은 "연결"하는 연산

   ex) # 리스트의 덧셈 연산
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        list3 = list1 + list2
        print(list3)

        # 문자열의 덧셈 연산
        string1 = '1234'
        string2 = '5678'
        string3 = string1 + string2
        print(string3)
        
- len 함수
두 자료형은 모두 길이를 재는 len 함수를 쓸 수 있다.
   ex) # 리스트의 길이 재기
        print(len(['H', 'E', 'L', 'L', 'O']))

        # 문자열의 길이 재기
        print(len("Hello, world!"))

- Mutable (수정 가능) vs. Immutable (수정 불가능)
하지만 차이점이 있다. 리스트는 데이터를 바꿀 수 있지만, 문자열은 데이터를 바꿀 수 없다는 것이다.
리스트와 같이 수정 가능한 자료형을 'mutable'한 자료형이라고 부르고, 문자열과 같이 수정 불가능한 자료형을 'immutable'한 자료형이라고 부른다.
숫자, 불린, 문자열은 모두 immutable한 자료형.




"""