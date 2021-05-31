"""
< 리스트 - list >
 ex) numbers = [2, 3, 5]
     names = ["아린", 카리나", "윈터"]

- 인덱싱 ( indexing )
    리스트이름[i] : i번째 인덱스에 들어있는 원소
    * 리스트이름[-1] = 마지막값

- 리스트 슬라이싱 ( list slicing )
    numbers[0:4] : 인덱스 0부터 3까지 4개를 자른다
    numbers[2:]  : 인덱스 2부터 맨 마지막까지
    numbers[:3]  : 처음부터 인덱스 2까지

- 리스트에 값 추가
    리스트이름.append()

- 리스트 값 삭제
    del 리스트이름[i] : 인덱스 i번째를 삭제

- 리스트 값 삽입
    리스트이름.insert(i, n) : 인덱스 i에 n을 삽입

- 리스트 정렬
    num_list = [19, 3, 34, 51, 23, 4]
    list = sorted(num_list) : 작은순으로 정렬된 함수
    list = sorted(num_list, reverse=TRUE) : 큰순으로 정렬

    num_list.sort() : 기존 리스트를 정렬
    
    * sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
    * sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬


"""