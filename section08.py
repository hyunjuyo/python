# Section08
# 파이썬 모듈과 패키지

# 패키지 예제
# 상대 경로
# .. : 부모 디렉토리
# .  : 현재 디렉토리

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 :", Fibonacci.fib2(500))
print("ex1 :", Fibonacci().title)

print()

# 사용2(클래스)

from pkg.fibonacci import *  # 메모리를 많이 차지해 권장하지는 않음

Fibonacci.fib(700)

print("ex2 :", Fibonacci.fib2(1000))
print("ex2 :", Fibonacci().title)

print()

# 사용3(클래스)

from pkg.fibonacci import Fibonacci as fb  # Alias => 간결 & 가독성 향상

fb.fib(1500)

print("ex3 :", fb.fib2(2000))
print("ex3 :", fb().title)

print()


# 사용4(함수)

import pkg.calculations as c

print("ex4 :", c.add(10, 100))
print("ex4 :", c.mul(10, 100))
print("ex4 :", c.div(100, 9))

print()

# 사용5(함수)

from pkg.calculations import div as d  # 필요한 부분만 import

print("ex5 :", int(d(100, 9)))

print()

# 사용6

import pkg.prints as p

p.prt1()
p.prt2()

print()

import builtins  # 기본적으로 import되어 있어서 굳이 입력 불필요

print(dir(builtins))

print()


# "__init__.py" 파일
# "pkg" 디렉토리 내에 "__init__.py" 파일을 생성해야 함
# 용도 : 해당 디렉토리가 패키지임을 선언함
# 단, Python 3.x 버전에서는 해당 파일이 없어도 패키지 인식함
#  => but 하위버전 호환을 위해서 생성해놓는 것을 추천함