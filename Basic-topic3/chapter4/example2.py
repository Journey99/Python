# 주민번호 가리기

def mask_security_number(security_number):
    # 코드를 입력하세요.
    security_list = list(security_number)
    security_str = ""
    for i in range(len(security_list)):
        if len(security_list) - 4 <= i:
            security_list[i] = "*"
        security_str += security_list[i]
    return security_str

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))