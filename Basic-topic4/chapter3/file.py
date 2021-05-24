"""
<파일 읽기>
* 파일이 있어야한다

with open('data/파일이름.txt', 'r') as f:
    for line in f:
        print(line)   -> 파일 줄 순서대로 출력

- 공백을 없애주는 방법
 : strip 사용
    ex) print(line.strip())

- 문자열을 나누는 방법
 : split 사용
    => split(" ") : " " 안을 기준으로 문자열을 자른다

    ex) full_name = "kim, yuna"
        print(full_name.split(", "))

        => ['kim', 'yuna']


<파일 쓰기>

* 파일 새로 쓰기 (덮어 쓰기) - w
with open('new_file.txt', 'w') as f:
    f.write("hello world"\n)
    f.write("my name is jeoni"\n)


* 파일 이어 쓰기 - a
with open('new_file.txt','a') as f:
    f.write("hello world")

: a 는 파일이 있으면 그 뒤부터 내용 생성되고
  파일이 없으면 파일을 새로 생성한 후에 내용이 쓰여진다.
  
"""