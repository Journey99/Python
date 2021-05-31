# 팰린드롬 - 거꾸로 읽어도 똑같은 단어

def is_palindrome(word):
    # 코드를 입력하세요.
    list_word = list(word)
    reversed_list = list_word[::-1]
    if list_word == reversed_list:
        return "true"
    else:
        return "false"

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))