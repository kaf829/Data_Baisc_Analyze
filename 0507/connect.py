import pymysql  # PyMySQL 모듈을 불러옴

# 1. MySQL 데이터베이스에 연결
conn = pymysql.connect(
    host='localhost',     # DB 서버 주소 (자기 컴퓨터면 localhost)
    port=3306,            # 포트 번호 (기본값: 3306)
    user='root',          # 사용자 계정
    password=1234,        # 비밀번호 (보안상 실제 코딩 시 문자열로 '1234'로 작성하세요)
    db='sqldb',           # 사용할 데이터베이스 이름
    charset='utf8'        # 문자 인코딩 설정
)

# 2. 커서 생성
cursor = conn.cursor()

# 3. SQL 실행
sql = 'select * from usertbl'
cursor.execute(sql)

# 4. 결과 가져오기
rows = cursor.fetchall()

# 5. 출력
for row in rows:
    print(row)

# 6. 연결 종료
cursor.close()
conn.close()
