# Section04-2

# 문자열 기본
str1 = "I am a Boy."
str2 = 'Niceman'
str3 = ''
print(len(str1), len(str2), len(str3))
escape_str1 = "I am a \"Boy\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)
print()

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
"""
문자열
멀티라인
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = "def"
str_o4 = "Niceman"

print(str_o1 * 30)
print(str_o2 + str_o3)
print('a' in str_o4)  # True or False
print('b' in str_o4)  # True or False
print('z'not in str_o4)  # True or False
print()

# 문자열 형변환
print(str(77) + 'a')  # 77이 문자이기 때문에 'a'와 결합 가능

# 문자열 함수
a = 'niceman'
b = 'orange'

print(a.islower())  # a가 모두 소문자인지 판단
print(b.endswith('e'))  # b가 'e'로 끝나는지 판단
print(a.capitalize())  # a의 첫글자를 대문자로 바꾸기
print(a.replace('nice', 'good'))  # a의 'nice'를 'good'으로 교체
print(list(reversed(b)))  # b를 리버스시키기(list로 출력)

# 문자열 슬라이싱 => *중요*

a = 'niceman'
b = 'orange'

print(a[0:3])  # 인덱스 0부터 3까지(인덱스 3은 불포함) => 3자리
print(a[0:len(a)])  # 인덱스 0부터 a의 길이만큼 => 처음부터 끝까지와 동일
print(a[:])  # 처음부터 끝까지
print(b[0:4:2])  # 인덱스 0부터 4까지, 2만큼씩 이동 => 인덱스 0 ~ 3 중 0과 2만 해당됨
print(b[1:-2])  # 인덱스 1부터 -2까지(인덱스 -2는 불포함) ※ 'orange'의 인덱스 -1은 'e', -2는 'g'임
print(b[::-1])  # 처음부터 끝까지, 역순으로 1만큼씩 이동 => 역순으로 처음부터 끝까지와 동일