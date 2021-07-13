# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print("a1 :", len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("a2 : apple;orange;banana;lemon")

# 3. 화면에 * 기호 100개를 표시하세요.
print("a3 :", '*' * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
a = 30
print(a)
print(float(a))
print(complex(a))
print(str(a))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
b = "Niceman"
print(b[4:])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
c = "Strawberry"
print(c[::-1])

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
d = "010-7777-9999"
print(d.replace('-', ''))

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
e = "http://daum.net"
print(e.replace("http://", ""))

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
f = "NiceMan"
print(f.upper())
print(f.lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
g = "abcdefghijklmn"
print(g[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
h = ["Banana", "Apple", "Orange"]
print(h)
h.remove("Apple")
print(h)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
i = (1, 2, 3, 4)
print(type(i))
print(i)
j = list(i)
print(type(j))
print(j)

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
k = {"성인": 100000, "청소년": 70000, "아동": 30000}
print(type(k))
print(k)

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
k["소아"] = 0
print(type(k))
print(k)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(k.keys())

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(k.values())

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
