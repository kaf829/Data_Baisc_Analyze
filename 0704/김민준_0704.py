import re

def validate_id(user_id):
    pattern = r'^[a-zA-Z0-9]{4,10}$'
    if re.fullmatch(pattern, user_id):
        print(f"아이디 가능: {user_id}")
    else:
        print("아이디 오류 최소 4자에서 10자 한글 안됨:.")

def validate_phone(phone):
    pattern = r'^010-\d{4}-\d{4}$'
    if re.fullmatch(pattern, phone):
        print(f"유효한 전화번호입니다: {phone}")
    else:
        print("전화번호 오류: 010-1234-5678 형식이어야 합니다.")

def validate_email(email):
    pattern = r'^[a-zA-Z0-9]{4,10}@hanmail.net$'
    if re.fullmatch(pattern, email):
        print(f"유효한 이메일입니다: {email}")
    else:
        print("이메일 오류: 아이디는 영문+숫자 4~10자이며, 도메인은 hanmail.net 이어야 합니다.")

# 입력
user_id = input("아이디를 입력하세요 (영문+숫자 4~10자): ")
validate_id(user_id)

phone = input("휴대폰 번호를 입력하세요 (예: 010-1234-5678): ")
validate_phone(phone)

email = input("이메일 주소를 입력하세요 (예: abcd123@hanmail.net): ")
validate_email(email)
