# 버스 요금 확인 함수
def get_fare(age, pay_type):
    if age < 8 or age > 75:
        fare = "무료"
    elif age < 14:
        fare = "450원"
    elif age < 20:
        if pay_type == "카드":
            fare = "720원"
        else:
            fare = "1000원"
    else:
        if pay_type == "카드":
            fare = "1200원"
        else:
            fare = "1300원"
    return fare

# 버스 요금 정보 출력 함수
def bus_fare(age, pay_type):
    print("\n<확인 결과>")
    print(f"나이: {age}세")
    print(f"지불유형: {pay_type}")
    fare = get_fare(age, pay_type)
    print(f"버스요금 : {fare}")

# 메인 함수
def main():
    print("<버스 요금 확인>")
    while(1):
        age = input("* 나이 입력 : ")
        try:
            age = int(age)
            if age < 0:
                print("0보다 큰 숫자를 입력해주세요.")
            else:
                break
        except:
            print("숫자형식으로 입력해주세요.")
    while(1):
        pay_type = input("* 지불유형 입력(카드/현금) : ")
        if pay_type != "카드" and pay_type != "현금":
            print("'카드' 또는 '현금' 중에 선택해주세요.")
        else:
            break
    
    bus_fare(age, pay_type)

main()