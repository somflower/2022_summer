#DB입력과 조회 예시
import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

con = sqlite3.connect("./Sample.db")#DB가 저장된 폴더까지 지정
cur = con.cursor()
#테이블 만들기
cur.execute("CREATE TABLE IF NOT EXISTS userTable (id char(4) PRIMARY KEY, userName char(15), email char(15), birthYear int)")

while (True) :
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break
    data2 = input("사용자 이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    #데이터 입력
    cur.execute(sql)

con.commit()#입력한 데이터 저장
con.close()#DB닫기

