# Section13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성


import random
import time
# 사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime

# DB생성 및 Auto Commit
# 본인 DB설정

conn = sqlite3.connect('C:/HJ\'s Notebook/Software/Python/resource/records.db', isolation_level=None)

# Cursor 연결
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,\
    cor_cnt INTEGER, record text, regdate text)")  # AUTOINCREMENT : 자동으로 연속되는 숫자를 입력시켜줌(직접 입력 불필요)

words = []  # 영어 단어 리스트(1000개 로드)

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open("./resource/word.txt", 'r') as f:
    for c in f:
        words.append(c.strip())  # strip() : 양쪽 공백 제거

# print(words)  # 단어 리스트 확인

input("Ready? Press Enter Key!")  # Enter Game Start!

start = time.time()  # 게임 시작 시간 "start"에 저장

while n <= 5:
    random.shuffle(words)  # words 리스트 내의 요소들 순서를 섞어줌
    q = random.choice(words)  # words에서 choice

    print()

    print("*Question # {}".format(n))
    print(q)  # 문제 출력

    x = input()  # 타이핑 입력

    print()

    if str(q).strip() == str(x).strip():  # 입력 확인(공백 제거)
        print("Pass!")
        # 정답 소리 재생
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        # 오답 소리 재생
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
        print("check!!")

    n += 1

end = time.time()  # 게임 종료 시간 "end"에 저장
et = end - start  # 수행시간 계산
et = format(et, ".3f")  # 소수점 셋째자리 float으로 포맷 설정

if cor_cnt >= 3:
    print("합격")
else:
    print("다시 한번~")

# 기록 DB 삽입

now = datetime.datetime.now()
nowDatatime = now.strftime('%Y-%m-%d %H:%M:%S')

cursor.execute("INSERT INTO records(cor_cnt, record, regdate) VALUES(?,?,?)",\
    (cor_cnt, et, nowDatatime))  # 위에서 AUTOINCREMENT 설정을 해주었기 때문에 여기서 id정보는 직접 입력할 필요 없음

# 수행시간 출력
print("게임 시간 :", et, "초,", "정답 개수 : {}".format(cor_cnt))

# 시작 지점
if __name__ == '__main__':
    pass