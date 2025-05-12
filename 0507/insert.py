import pymysql  # PyMySQL 모듈을 불러옴

# 1. MySQL 데이터베이스에 연결
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='1234',   # 문자열로 바꿨음
    db='sqldb',
    charset='utf8'
)

# 2. 커서 생성
cursor = conn.cursor()

# 3. SQL 실행 구문
sql = 'INSERT INTO usertbl VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

try:
    userID = input("아이디 입력: ")
    name = input("이름 입력: ")
    birthYear = input("생년 입력: ")
    addr = input("주소 입력: ")
    mobile1 = input("휴대폰 앞자리 입력: ")
    mobile2 = input("휴대폰 뒷자리 입력: ")
    height = int(input("키 입력: "))
    mDate = input("가입날짜 (예: 2024-10-30): ")

    cursor.execute(sql, (userID, name, birthYear, addr, mobile1, mobile2, height, mDate))
    conn.commit()

    # 결과 출력
    sql = 'SELECT * FROM usertbl'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print("\n입력 오류 발생:", e)

finally:
    cursor.close()
    conn.close()
