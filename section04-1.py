# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999
big_int2 = 7777777777777777777777777777777
f1 = 1.234
f2 = 3.789
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** 2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))
print()


# 형변환
# int, float, complex(복소수)

a = 5.
b = 4
c = 10

result2 = a + b
print(result2)
print(int(result2))
print(float(c))
print(complex(3))
print(int(True), int(False), sep=', ')
print(int('3'))
print()

result3 = c / b
print(result3, type(result3))
print(int(result3))
result4 = c // b
print(result4, type(result4))


y = 100
y *= 70
print(y)

# 수치 연산 함수

print(abs(-7))
n, m = 10, 20
print(n, m)
q, w = divmod(100, 9)
print(q, w)
print()

# 진수 변환

print(bin(10))
print(hex(21))

import math

print(math.ceil(5.1))
print(math.floor(3.789))
print(math.pi)