import mysql.connector

try:
    db = mysql.connector.connect(
        host='mysql.railway.internal',          # 예: 'containers-us-west-123.railway.app'
        port=3306,            # 예: 3306 또는 12345 (Variables에서 확인)
        user='root',
        password='tUjcCqzpfUtnqTEiCVuuqFNpJiNMKJHl',
        database='railway'
    )

    print("MySQL 연결 성공!")

    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    if tables:
        print("테이블 목록:")
        for table in tables:
            print(table[0])
    else:
        print("테이블이 없습니다.")

    cursor.close()
    db.close()

except mysql.connector.Error as err:
    print("연결 실패:", err)
