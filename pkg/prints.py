def prt1():
    print("I'm Niceboy!")

def prt2():
    print("I'm Goodboy!")

# 단위 실행(독립적으로 파일 실행) => 함수 테스트 등 위해 활용
if __name__ == "__main__":  # 이 조건에 의해, 다른 파일에서 실행 시 아래 부분은 실행되지 않음
    prt1()
    prt2()

    