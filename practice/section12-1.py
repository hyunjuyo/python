# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()  # 현재 날짜 및 시간 정보
print('now :', now)

nowDatatime = now.strftime('%Y-%m-%d %H:%M:%S')  # 원하는 포맷 설정
print('nowDatatime :', nowDatatime)

# sqlite3
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version :', sqlite3.sqlite_version)

print()

# DB 생성 & Auto Commit 설정("isolation_level=None")
conn = sqlite3.connect('C:/HJ\'s Notebook/Software/Python/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type :', type(c))

print()

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text,\
email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'KIM', 'Kim@naver.com', '010-0000-0000',\
    'Kim.com', ?)", (nowDatatime,))  # nowDatatime값이 ? 부분에 반영됨
c.execute("INSERT INTO users(id, username, email, phone, website, regdate)\
    VALUES(?,?,?,?,?,?)", (2, 'Park', 'Park@gmail.com', '010-1111-1111', 'Park.com', nowDatatime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatatime),
    (4, 'Cho', 'Cho@Daum.net', '010-3333-3333', 'Cho.com', nowDatatime),
    (5, 'Yoo', 'Yoo@gmail.com', '010-1212-2323', 'Yoo.com', nowDatatime)
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate)\
    VALUES(?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
#conn.execute("DELETE FROM users")  # 데이터 전체 삭제됨
#c.execute("DELETE FROM users")  # 위와 동일한 결과
#print("users db deleted :", conn.execute("DELETE FROM users").rowcount)  # rowcount : 지원진 결과 row개수 확인
# print("users db deleted :", c.execute("DELETE FROM users").rowcount)  # 위와 동일한 결과

# 커밋 : isolation_level=None일 경우 자동으로 커밋 반영됨(Auto Commit)
# Auto Commit 아닐 경우는 conn.commit() 해줘야 함

# 롤백
# conn.rollback()

# 접속 해제
conn.close()