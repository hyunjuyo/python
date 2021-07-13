# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없더라도, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크


# SyntaxError : 잘못된 문법

# print('Test)

#if True
#    pass

#x => y

a = 10
b = 15
#print(c)

# ZeroDivisionError : 0으로 나누기 에러
# print(10 / 0)

# IndexError : 인넥스 범위 오버

x = [10, 20, 30]
# print(x[3])

# KeyError

dic = {"Name" : "Kim", 'Age' : 33, 'City' : 'Seoul'}
# print(dic['hobby'])
print(dic.get('hobby'))

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시 에러

import time
print(time.time())  # 정상 케이스
# print(time.month())  # 에러 케이스

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.index(10)

# FileNotFoundError

# f = open("test.txt", 'r')

# TypeError

x = [1, 2]
y = (1, 2)
z = "test"
print(x + list(y))  # 정상 케이스
# print(x + y)

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

print()

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1

name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except ValueError:  # ValueError가 발생했을 경우에 실행됨
    print('Not fount it! - Occurred ValueError!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')

print()

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except ValueError:  # ValueError가 발생했을 경우에 실행됨
    print('Not fount it! - Occurred ValueError!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')

print()

# 예제2
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except:  # 어떤 Error든 발생했을 경우에 실행됨
    print('Not fount it! - Occurred Error!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')

print()

# 예제3-1
try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except Exception:  # 어떤 Error든 발생했을 경우에 실행됨
    print('Not fount it! - Occurred Error!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')
finally:  # Error가 발생하든 안하든 무조건 실행됨
    print('finally ok!')

# 예제3-2
try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except:  # 어떤 Error든 발생했을 경우에 실행됨
    print('Not fount it! - Occurred Error!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')
finally:  # Error가 발생하든 안하든 무조건 실행됨
    print('finally ok!')

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!')

print()

# 예제5
# 아래의 경우 "except Exception:"이 첫번째에 오면 ValueError, IndexError까지 포함해 처리되므로 순서 주의 필요

try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! {} in name'. format(z, x + 1))
except ValueError as V:
    print(V)  # Alias 후 출력하면 해당 에러메시지 출력됨
except IndexError:
    print('Not fount it! - Occurred IndexError!')
except Exception:  # ValueError, IndexError 외의 Error시 실행됨
    print('Not fount it! - Occurred Error!')
else:  # Error가 발생하지 않았을 경우에 실행됨
    print('Ok! else!')
finally:  # Error가 발생하든 안하든 무조건 실행됨
    print('finally ok!')

print()

# 예제6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Cho'
    if a == 'Kim':
        print("OK 허가!")
    else:
        raise ValueError  # 에러를 규정해서 발생시킴
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')