# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('Hello Python!')
print("Hello Python!!")
print("""Hello Python!""")
print('''Hello python!!''')

print()

# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'goole.com', sep='@')

# end 옵션 사용
print('Welcome To', end='')
print(' the World!', end=' ')
print('wow~!!')

print()

# format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} and {b}".format(a='You', b='Me'))

print("%s's favorite number is %d" % ('David', 3))

print("Test1: %5d, Price: %4.2f" % (123, 12345.6789))
print("Test2: {0:5d}, Price: {1:4.2f}".format(123, 12345.6789))
print("Test3: {a:5d}, Price: {b:4.2f}".format(a=123, b=12345.6789))

print("'you'")
print('\'you\'')
print('"you"')
print('\\you\\')
print('newline\n')
print("\twow!!")