# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서 x, 중복 x, 수정 및 삭제 가능

# 선언
a = {'Name': 'Kim', 'Phone': '010-1111-1111', 'Birth': 910214}  # Key: Value / Key는 중복 불가
b = {0: 'Hello', 1: 'Python'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

print(a['Name'])
print(a.get('Name'))
print(a.get('Pho'))  # get : 잘못된 Key값이 주어졌을 때, 에러메시지 출력 대신 정상실행 후 "None"을 출력함
print(c['arr'])
print(c['arr'][1:3])
print()

# 딕셔너리 추가
a['Address'] = 'Seoul'  # 기존 딕셔너리에 Key와 Value 추가됨
print(a)
a['Rank1'] = [1, 2, 3]
a['Rank2'] = (1, 3, 5)
print(a)
print()

# keys, values, items
print(a.keys())  # a의 Key값들만 출력
print(type(a.keys()))
print(list(a.keys()))  # 인덱싱 또는 슬라이싱을 위해서는 list로 형변환 해야 함
print(list(a.keys())[0:2])  # 만약 그냥 print(a.keys()[0])라고 입력 후 실행하면 에러메시지 출력됨
print()

print('Name' in a)  # 'Name'이라는 Key가 a에 있는지 판단
print()

print(a.values())  # a의 Value들만 출력
print(a.items())  # a의 Key와 Value들을 묶어서 출력
print(list(a.items()))  # 리스트로 형변환
print()


# 집합 : 순서 x, 중복 x

# 선언 및 초기화
a = set()
b = set([1, 2, 3])  # set : 인자를 1개만 가짐. list 형태로 초기화해줘야 함
c = set([1, 3, 5, 5, 7])  # 값을 중복 입력하더라도 출력해보면 중복 제외됨

print(type(a))  # 타입 확인
print(c)  # 출력결과를 보면 중복을 허용하지 않는 것을 알 수 있음
print()

e = tuple(b)  # 튜플로 형변환
print(e)
e = list(b)  # 리스트로 형변환
print(e)
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([5, 6, 7, 8, 9, 10])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1 - s2)
print(s1.difference(s2))

print()


# 추가, 삭제

s3 = set([7, 8, 9, 10])

s3.add(12)
print(s3)

s3.remove(9)
print(s3)

print(type(s3))