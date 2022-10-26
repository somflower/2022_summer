#조회 프로그램
import sqlite3

con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = None

con = sqlite3.connect("./Sample.db")#DB가 저장된 폴더까지 지정, ./Sample.db --> db로 제작, .db가 없으면 txt파일로 만들어짐
cur = con.cursor()
#테이블의 필드 불러오기
cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름      이메일             출생연도")
print("-"*30)

while(True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s %15s %15s %15d" % (data1, data2 ,data3, data4))

con.close()
