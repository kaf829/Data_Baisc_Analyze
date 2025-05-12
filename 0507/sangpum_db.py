import pymysql
from Sangpum import Sangpum
def connet_db():
    dbconn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',  # 문자열로 바꿨음
        db='sqldb',
        charset='utf8'
    )
    return dbconn


def create_table():
    dbconn = connet_db()
    dbcursor = dbconn.cursor()
    dbcursor.execute("""
    create table if not exists sangpum(
        code char(4) primary key,
        name char(10),
        count int,
        print int,
        kumack bigint
    )
    """)

    dbcursor.close()
    dbconn.close()


def f_menu():
    print("메뉴")
    print("1 상품정보 입력")
    print("2 상품정보 출력")
    print("3 상품정보 조회")
    print("4 상품정보 수정")
    print("5 상품정보 삭제")
    print("6 상품정보 종료")


def f_input():
    obj = Sangpum()

    print()
    obj.input_data()
    obj.proc_kumack()

    dbconn = connet_db()
    dbcursor = dbconn.cursor()
    sql = "insert into sangpum values(%s,%s,%s,%s,%s)"
    print(obj.code, obj.name, obj.count, obj.price, obj.kumack)
    try:
        dbcursor.execute(sql,(obj.code, obj.name, obj.count, obj.price, obj.kumack))
        dbconn.commit()
        print("\n상품정보 입력 성공\n")
    except Exception as e:
        print("\n상품정보 입력 실패\n",e.args[0])
    finally:
        dbcursor.close()
        dbconn.close()


def f_output():
    total_kumack = 0

    dbconn = connet_db()
    dbcursor =dbconn.cursor()

    dbcursor.execute("select count(*) from sangpum")
    cnt = dbcursor.fetchone()[0]
    res = dbcursor.fetchall()
    if(cnt == 0):
        print("\n 출력할 데이터가 없습니다")

    print("------------------상품정보-------------------")
    print(f"                                    총 상품수:{cnt}")
    print("상품코드     상품명     수량      단가      판매금액")
    print("===============================================")
    dbcursor.execute("select * from sangpum")
    res = dbcursor.fetchall()
    for row in res:
        total_kumack += row[4]
        print(f"{row[0]:>4}     {row[1]:>4}     {row[2]:6d}     {row[3]:8d}     {row[4]:8d}")
    print("===============================================")
    print(f"                                총 판매금액: {total_kumack}")
    dbcursor.close()
    dbconn.close()

def f_search():
    dbconn = connet_db()
    dbcursor = dbconn.cursor()
    code = input("조회할 상품코드를 입력하세요:")
    dbcursor.execute(f"select * from sangpum where code = {code}")
    row = dbcursor.fetchone()
    print("상품코드     상품명     수량      단가      판매금액")
    print("===============================================")
    print(f"{row[0]:>4}     {row[1]:>4}     {row[2]:6d}     {row[3]:8d}     {row[4]:8d}")

    dbcursor.close()
    dbconn.close()

def f_update():
    dbconn = connet_db()
    dbcursor = dbconn.cursor()
    obj = Sangpum()

    print()
    obj.input_data()
    obj.proc_kumack()
    sql = "UPDATE sangpum SET name = %s, price = %s, count = %s, kumack = %s WHERE code = %s"
    values = (obj.name, obj.price, obj.count, obj.kumack, obj.code)
    dbcursor.execute(sql, values)
    dbcursor.close()
    dbconn.close()

def f_delete():
    dbconn = connet_db()
    dbcursor = dbconn.cursor()
    code = input("조회할 상품코드를 입력하세요:")
    dbcursor.execute(f"select * from sangpum where code = {code}")
    row = dbcursor.fetchone()
    if row:
        print("test")
        dbcursor.execute(f"delete from sangpum where code = {code}")
        dbconn.commit()
        print("\n상품정보 삭제 성공\n")
    else:
        print("품번이 존재하지 않습니다")
    dbcursor.close()
    dbconn.close()

    
if __name__ == "__main__":
    create_table()

    while True:
        f_menu()

        menu = int(input("\n메뉴를 선택하세요: "))

        if menu == 1:
            f_input()
        elif menu == 2:
            f_output()
        elif menu == 3:
           f_search()
        elif menu ==4:
            f_update()
        elif menu ==5:
            f_delete()
        elif menu == 6:
            print("프로그램 종료...")
            break
        
        else:
            print("메뉴를 다시 선택하세요")
