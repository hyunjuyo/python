# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
#class 클래스명:
#    함수
#    함수
#    함수

# 예제1
# class UserInfo:
    # 속성, 메소드

class UserInfo:
    def __init__(self, name):  # 클래스를 초기화해주는 것
        self.name = name
    def user_info_p(self):
        print("Name :", self.name)

user1 = UserInfo("Kim")  # user1로 인스턴스 생성
user1.user_info_p()  # 인스턴스화 된 메소드 호출
print(user1.name)
user2 = UserInfo("Park")  # user2로 인스턴스 생성
user2.user_info_p()  # 인스턴스화 된 메소드 호출
print(user2.name)
print()

print(id(user1))
print(id(user2))  # user1과 user2의 id는 다른 것을 알 수 있음
print(user1.__dict__)
print(user2.__dict__)

print()


# 예제2
# self의 이해
class SelfTest:
    def function1():  # self 없이 선언
        print("function1 called!")
    def function2(self):
        print(id(self))
        print("function2 called!")

self_test = SelfTest()  # 이렇게 해야 에러 발생하지 않음
# self_test = SelfTest("Kim")  # 이 경우 에러 발생함

# self_test.function1()  # function1은 클래스 메소드이므로 이 경우 에러 발생함
SelfTest.function1()  # 이 경우 function1은 클래스 이름으로 호출해야 함
self_test.function2()
print()

print(id(self_test))
SelfTest.function2(self_test)  # 위와 동일한 id인 것을 확인 가능함
SelfTest.function2("Kim")  # 위와 다른 별도의 id로 생성된 것을 확인 가능함

# self_test.function2("Kim")  # 이 경우 에러 발생함
# SelfTest.function2()  # 이 경우 에러 발생함

print()

# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    stock_num = 0  # 클래스 변수
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)  # 클래스 변수인 stock_num이 3인 것을 확인 가능

print()

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)  # 자기 네임스페이스에 없으면 클래스 네임스페이스에 가서 해당 변수를 찾음
print(user2.stock_num)
print(user3.stock_num)

del user1

print(user2.stock_num)  # stock_num이 2로 바뀐 것을 확인 가능
print(user3.stock_num)