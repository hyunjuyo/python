# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r
# 쓰기 모드(기존 파일에 덮어씀) : w
# 추가 모드(파일 생성 또는 추가) : a
# .. : 상대경로
# .  : 절대경로

# 기타 : https://docs.python.org/3.7/library/functions.html#open


# 파일 읽기
# 예제1
f =  open("./resource/review.txt", 'r')
content = f.read()
print(content)  # 읽은 내용 확인
print(dir(f))  # f라는 변수의 인스턴스 확인
# 반드시 close로 리소스 반환
f.close()

print("========================================================")

# 예제2
with open("./resource/review.txt", 'r') as f:  # with문 => close를 자동으로 처리해줌
    c = f.read()
    print(c)
    print(list(c))  # 문자 하나하나 리스트 형태로 출력
    print(iter(c))  # 반복문에서 활용 가능

print("========================================================")

# 예제3
with open("./resource/review.txt", 'r') as f:
    for c in f:
        print(c)  # 개행 단위로 가져와 출력하는 것을 확인 가능

print()

with open("./resource/review.txt", 'r') as f:
    for c in f:
        print(c.strip())  # strip() : 문자열 양쪽끝에 있는 공백 및 '\n'을 삭제

print("========================================================")

# 예제4
with open("./resource/review.txt", 'r') as f:
    content = f.read()
    print(">>>", content)  # 전체 내용 출력
    content = f.read()
    print(">>>>>", content)  # 출력된 내용 없음

print("========================================================")

# 예제5
with open("./resource/review.txt", 'r') as f:
    line = f.readline()  # readline() : 한줄씩 읽어옴
    while line:
        print(line, end=">>>")
        line = f.readline()

print()
print("========================================================")

# 예제6
with open("./resource/review.txt", 'r') as f:
    contents = f.readlines()  # readlines() : '\n' 포함한 한줄 단위의 요소들을 리스트 형태로 반환
    print(contents)
    for c in contents:
        print(c, end="  ***")

print()
print("========================================================")

# 예제7
with open("./resource/score.txt", 'r') as f:
    count1 = 0
    sum1 = 0
    for num in f:
        sum1 += int(num)
        count1 += 1
        print("[%d] %d" % (count1, sum1))
    print("average :", sum1 / count1)

print()

score = []
with open("./resource/score.txt", 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print("Average : %6.3f" % (sum(score)/len(score)))
print("Average : {:6.3}".format(sum(score)/len(score)))

print()

# 파일 쓰기

# 예제1
with open("./resource/text1.txt", 'w') as f:
    f.write("Niceman!\n")
with open("./resource/text1.txt", 'r') as f:  # write() 내용 확인용
    print(f.read())

# 예제2
with open("./resource/text1.txt", 'a') as f:
    f.write("Goodman!\n")
with open("./resource/text1.txt", 'r') as f:  # write() 내용 확인용
    print(f.read())

# 예제3
from random import randint

with open("./resource/text2.txt", 'w') as f:
    for cnt in range(6):  # 0부터 5까지
        f.write(str(randint(1, 50)))  # 1부터 50 중 random 추출
        f.write('\n')
with open("./resource/text2.txt", 'r') as f:  # write() 내용 확인용
    print(f.read())

# 예제4
# writelines : 리스트를 파일로 저장
with open("./resource/text3.txt", 'w') as f:
    list = ["Kim\n", "Park\n", "Cho\n"]
    f.writelines(list)
with open("./resource/text3.txt", 'r') as f:  # write() 내용 확인용
    print(f.read())

# 예제5
with open("./resource/text4.txt", 'w') as f:
    print("Test Contents1!", file=f)  # 출력 내용을 파일로 보냄
    print("Test Contents2!", file=f)  # 출력 내용을 파일로 보냄
with open("./resource/text4.txt", 'r') as f:  # write() 내용 확인용
    print(f.read())