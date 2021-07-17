# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 => 순서 O, 중복/수정/삭제 가능

# 선언
a= []
b = list()  # 명시적으로도 선언 가능

# 초기화
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']  # 다른 자료형 가능
e = [10, 100, ['Pen', 'Banana', 'Orange']]  # 중첩 리스트 가능

# 인덱싱
print(d[3])
print(d[-2])  # 역순 인덱스 기준 => 바로 위 예시(d[3])와 동일한 결과
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])  # 역순 인덱스 기준 => 바로 위 예시(e[2][1])와 동일한 결과
print()

# 슬라이싱
print(d[0:3])
print(e[2][1:3])
print()

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')
print()

# 수정 및 삭제(del)
c[0] = 77
print(c)
c[1:2] = [100, 1000, 10000]  # (슬라이싱의 경우) 리스트 원소 개수에 따라 추가 삽입이 됨
print(c)
c[1] = ['a', 'b', 'c']  # (인덱싱의 경우) 인덱스 1에 리스트 자체가 원소로 삽입이 됨
print(c)
del c[1]  # 인덱스 1에 있는 원소 지워지고, 뒤에 있는 원소가 앞으로 당겨짐
print(c)
del c[-1]  # 마지막 인덱스에 있는 원소 지워짐
print(c)
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6)  # 맨 뒤에 덧붙임
print(y)
y.sort()  # 정렬
print(y)
y.reverse()  # 역순 정렬
print(y)
y.insert(2, 7)  # 인덱스 2에 7을 원소로 삽입함
print(y)
y.remove(2)  # 원소 2를 remove (인덱스 2가 아님에 주의)
print(y)
y.remove(7)  # 원소 7을 remove (인덱스 7아 아님에 주의)
print(y)
y.pop()  # 맨 마지막 원소를 꺼냄 => y에서 지워짐
print(y)
ex = [88, 77]
y.extend(ex)  # 추가하려고 하는 리스트의 원소가 y의 원소로 삽입됨
print(y)
y.append(ex)  # 추가하려고 하는 리스트 자체가 y의 원소로 삽입됨
print(y)

# 삭제 : del, remove, pop

# 튜플 => 순서 O, 중복 허용, 수정/삭제 불가

a = ()
b = (1,)
c = (1, 2, 3, 4)

# del c[2]  # 이렇게 입력하고 실행할 경우 에러메시지 출력됨

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))

print(a)
print(b[0])
print(d[2][2])
print(d[2:])
print(d[2][0:2])
print(c + d)
print(c * 3)
print()

# 튜플 함수

z = (5, 2, 3, 1, 4, 1, 1)

print(z)
print(3 in z)  # 원소 3이 z에 있는지 판단
print(z.index(3))  # 원소 3의 인덱스를 반환
print(z.count(1))  # 원소 1의 개수를 반환