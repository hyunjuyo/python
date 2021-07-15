# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB파일 조회(없으면 새로 생성)
conn = sqlite3.connect('C:/HJ\'s Notebook/Software/Python/resource/database.db')  # DB 경로 입력

# 커서 바인딩
c = conn.cursor()


# 데이터 조회(전체)
c.execute("SELECT * FROM users")  # users 테이블 전체를 SELECT

# 커서 위치 변경 확인
# 1개 row 선택
print('One -> \n', c.fetchone())  # 한번 호출에 하나의 row만 클라이언트로 가져옴

# 지정 row 선택
print('Three -> \n', c.fetchmany(size=3))  # 3개의 row 데이터를 가져옴

# 전체 row 선택
print('All -> \n', c.fetchall())  # 모든 데이터를 한꺼번에 클라이언트로 가져옴

print('All -> \n', c.fetchall())  # 더 이상 읽어올 데이터가 없음 확인

print()

# 순회1
c.execute("SELECT * FROM users")  # 다시 users 테이블 전체를 SELECT

rows = c.fetchall()  # 모든 데이터를 한꺼번에 클라이언트로 가져옴

for row in rows:  # 한 줄씩 반복 출력
    print('retrieve1 >', row)
print()

# 순회2
c.execute("SELECT * FROM users")  # 다시 users 테이블 전체를 SELECT

for row in c.fetchall():  # 모든 데이터를 가져온 뒤, 한 줄씩 반복 출력
   print('retrieve2 >', row)
print()

# 순회3
# 아래와 같이 SELECT까지 한번에 처리하는 것도 가능
for row in c.execute('SELECT * FROM users ORDER BY id desc'):  # "ORDER BY id desc" => id 기준 내림차순 정렬
   print('retrieve3 >', row)

print()

# WHERE Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())  # id가 3인 데이터 행을 읽어온 것을 확인 가능
print('param1', c.fetchall())  # 더 이상 읽어올 데이터가 없음을 확인 가능
print()

# WHERE Retrieve2
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())
print()

# WHERE Retrieve3
c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall())
print()

# WHERE Retrive4
param4 = (3, 5)
c.execute('SELECT * FROM users WHERE id IN(?, ?)', param4)
print('param4', c.fetchall())
print()

# WHERE Retrive5
c.execute('SELECT * FROM users WHERE id IN(%d, %d)' % (3, 4))
print('param5', c.fetchall())
print()

# WHERE Retrive6
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2', {"id1": 2, "id2": 5})
print('param6', c.fetchall())
print()


# Dump 출력
with conn:
    with open('C:/HJ\'s Notebook/Software/Python/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# with문 사용 => f.close(), conn.close() 모두 자동으로 적용이 됨

print()
