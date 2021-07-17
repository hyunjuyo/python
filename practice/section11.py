# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader)  # 한 줄을 스킵할 때 사용
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # '__iter__'가 있음 확인 => 반복문으로 출력 가능

    for c in reader:
        print(c)

print()

# 예제2
with open('./resource/sample2.csv', 'r') as f:
    #reader = csv.reader(f)
    reader = csv.reader(f, delimiter='|')  # delimiter : 콤마 외 구분자 설정
    #next(reader)  # 한 줄을 스킵할 때 사용
    # 확인
    print(reader)
    print(type(reader))

    for c in reader:
        print(c)

print()

# 예제3 (Dict변환)

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('------------------')

print()

# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:  # "newline=''" 없으면 한줄씩 빈 줄이 생김
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)  # 한 번에 한 라인씩 씀

# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)  # 한 번에 전체 라인을 다 씀

# XSL, XLSX
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용함(openpyxl, xlrd 포함)
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# 적용 가능 옵션 => sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')

# 데이터 확인
print(xlsx.head())  # 첫번째 행 포함 6행 출력(위 5행)
print()

print(xlsx.tail())  # 첫번째 행 포함 6행 출력(아래 5행)
print()

print(xlsx.shape)  # 행과 열 개수 확인(첫번째 행 제외 기준)

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)

print()