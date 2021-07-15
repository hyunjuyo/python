# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:  # 1부터 10까지 반복
    print("v1 is :", v1)
    v1 += 1
print()

for v2 in range(10):  # 0부터 9까지 반복
    print("v2 is :", v2)
print()

for v3 in range(1, 11):  # 1부터 10까지 반복
    print("v3 is :", v3)
print()

# 1 ~ 100 합

sum100 = 0
num = 1

while num <= 100:
    sum100 += num
    num += 1

print("1 ~ 100 :", sum100)
print("1 ~ 100 :", sum(range(1, 101)))  # 1부터 100까지 sum
print("1 ~ 100 :", sum(range(1, 101, 2)))  # 1부터 100까지 2칸씩 이동하며 sum

print()

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 리스트 자료형 반복
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for a in names:
    print("you are :", a)

# 문자열 자료형 반복
word = "dreams"

for b in word:
    print("Word : ", b)

# 딕셔너리 자료형 반복
my_info = {
    "name" : "Kim",
    "age" : 33,
    "city": "Seoul"
}

for c in my_info:  # 기본적으로 key값들이 호출됨
    print("1.", "my_info :", c)

for c in my_info.keys():  # 명시적으로 key값들을 지정
    print("2.", "my_info :", c)

for c in my_info.values():  # 명시적으로 value값들을 지정
    print("3.", "my_info :", c)

for c in my_info.items():  # 명시적으로 item값들을 지정
    print("4.", "my_info :", c)

for d, e in my_info.items():  # 명시적으로 item값들을 지정 및 key, value 각각 출력
    print("5.", "my_info :", d, e)

print()

# 대문자를 소문자로, 소문자를 대문자로 변경해 출력하기
name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower(), end='')
    else:
        print(n.upper(), end='')

print()

# for-else구문 및 break
numbers = [12, 3, 7, 2, 8, 35, 21, 37, 29, 77]

for a in numbers:
    if a == 29:
        print(numbers.index(a), "found 29")
        break
    else:
        print(numbers.index(a), "not found 29")
else:  # 반복문이 끝까지 정상적으로 수행된 경우에만 else 블럭이 수행됨(break로 중간에 빠져나온 경우는 수행 X)
    print("check numbers!")

print()

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("type :", type(v))
else:  # continue가 있더라도 반복문은 끝까지 수행되므로 마지막에 else 블럭 수행됨
    print("wow!")


# 자료구조 변환
name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(tuple(reversed(name)))

print(name[::-1])  # (비교용) 슬라이싱으로 역순으로 출력

for c in tuple(reversed(name)):
    print(c, end='')

print()

for c in reversed(name):
    print(c, end='')