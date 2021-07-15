# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중 상속

# 예제1
# 상속 기본

# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 공통적인 속성을 부모클래스로 생성

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar("520d", "sedan", "red")

print(model1.color)  # Super
print(model1.type)  # Super
print(model1.car_name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub
print(model1.__dict__)

print()

# Method Overriding
model2 = BenzCar("220d", "suv", "black")
print(model2.show())  # 슈퍼클래스에 있는 메소드이지만 서브클래스에서 새롭게 정의되어 있을 때 => "Overriding"

print()

# Parent Method Call
class BenzCar2(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name
    
    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())  # super 키워드를 통해 슈퍼클래스의 속성에 접근 가능
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)

model3 = BenzCar2("350s", "sedan", "silver")
print(model3.show())

print()

# Inheritance Info(상속 정보)
print(BmwCar.mro())  # 클래스 상속 관계를 리스트 타입으로 확인 가능 (마지막에는 object 클래스)
print(BenzCar.mro())

print()

# 예제2
# 다중 상속

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())  # 다중 상속 관계 확인 가능
print(A.mro())