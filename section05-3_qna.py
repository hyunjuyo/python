# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a, b in q1.items():
    if a == "가을":
        print(b)

for a in q1.keys():
    if a == "가을":
        print(q1[a])

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a in q2.values():
    if a == "사과":
        print("포함")
        break
else:
    print("불포함")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 95

if score > 100:
    print("체크 필요 : 숫자가 100보다 큼")
elif score >= 81:
    print("A학점")
elif score >= 61:
    print("B학점")
elif score >= 41:
    print("C학점")
elif score >= 21:
    print("D학점")
elif score >= 0:
    print("E학점")
else:
    print("체크 필요 : 숫자가 0보다 작음")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

lt = [12, 6, 18]
num = lt[0]
for i in lt:
    if i > num:
        num = i
print(num)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
num = "910214-1234567"

if num[7] == str(1) or num[7] == str(3):
    print("남자")
elif num[7] == str(2) or num[7] == str(4):
    print("여자")
else:
    print("확인 필요")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for v in q3:
    if v != "정":
        print(v)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for i in range(1, 101):
    if i % 2 == 1:
        print(i, end=' ')

print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for v in q4:
    if len(v) >= 5:
        print(v, end=' ')
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q5:
    if v.islower():
        print(v, end=' ')
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for v in q6:
    if v.islower():
        print(v.upper(), end=' ')
    elif v.isupper():
        print(v.lower(), end=' ')
print()

# 일반적인 방법
numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers, "\n")


# List Comprehension
numbers2 = [x for x in range(1, 101)]  # 한 줄로 입력 가능
print(numbers2, "\n")

numbers3 = [x for x in range(1, 101) if x % 2 != 0]  # if도 함께 적용 가능
print(numbers3, "\n")