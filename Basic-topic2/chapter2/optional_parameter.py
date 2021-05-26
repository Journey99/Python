"""
< 옵셔널 파라미터 - optional parameter >



def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)  # 옵셔널 파라미터를 제공하지 않는 경우


=> 출력
    내 이름은 코드잇
    나이는 1살
    국적은 미국

    내 이름은 코드잇
    나이는 1살
    국적은 한국


-오류가 생기는 예시
  def myself(name, nationality="한국", age):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


    myself("코드잇", 1)  # 기본값이 설정된 파라미터를 바꾸지 않을 때
    print()
    myself("코드잇", "미국", 1)  # 기본값이 설정된 파라미터를 바꾸었을 때

 => 옵셔널 파라미터는 꼭 마지막에 있어야 한다
    개수는 상관업다!
"""