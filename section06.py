# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요


# 예제1
def hello(s1):  # 반환값이 없는 함수 정의
    print("Hello", s1)

hello("Python!")

# 예제2
def hello_return(s2):  # 반환값이 있는 함수 정의
    val = "Hello " + str(s2)
    return val

str = hello_return("Python!!!!!")
print(str)
print()

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)
print()

# 예제4(다중리턴) - 데이터 타입 반환
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]  # 리스트로 반환

lt = func_mul2(100)
print(lt, type(lt))
print()

# 예제5
# *args

def args_func1(*args):  # 가변인자를 튜플로 받음
    print(type(args), args)

def args_func2(*args):
    for i, v in enumerate(args):  # enumerate : 인덱스 값을 포함하는 enumerate 객체를 반환
        print(i, v)
    print(type(enumerate(args)))

args_func1('Kim')
args_func1('Kim', 'Park')
args_func2('Kim', 'Park', 'Lee')
print()

# **kwargs
def kwargs_func1(**kwargs):  # 딕셔너리로 인자를 받음
    print(kwargs)

def kwargs_func2(**kwargs):    
    for k, v in kwargs.items():
        print(k, v)

kwargs_func1(name1='Kim', name2='Park', name3='Lee')
kwargs_func2(name1='Kim', name2='Park', name3='Lee')
print()


# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20)  # 인자 2개는 필수로 있어야 함
example_mul(10, 20, 30, 31, 'Kim')  # 이후 인자들은 튜플로 받음
example_mul(10, 20, 'Park', 'Kim', complex(3), age1=24, age2=32)
example_mul(10, 20, age1=24, age2=32)  # 딕셔너리 형태의 인자들은 딕셔너리로 받음
print()

# 예제6
# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):  # 함수 안에 함수를 정의
        print(num)
    print("in func")
    func_in_func(num + 10000)  # 함수 안에 정의된 함수를 호출

nested_func(10000)
print()

# 예제7(hint)
def func_mul3(x : int) -> list:  # 힌트
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))
print()

# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func)  # 함수 객체 생성, 메모리 할당
print(type(var_func))
print(var_func(10))
print()

lambda_mul_10 = lambda num : num * 10
print(">>>", lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(7))

func_final(10, 10, lambda_mul_10)

func_final(10, 10, lambda num : num * 1000)  # 별도 함수 선언 없이 바로 입력 가능