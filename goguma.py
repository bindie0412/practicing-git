print('첫번째 숫자를 입력하세요:')
num1 = int(input())
print('두번째 숫자를 입력하세요:')
num2 = int(input())
print('연산기호를 입력하세요(+,-,*,/):')
op = int(input())
answer = 0
if op == '+':
    answer = num1 + num2
elif op == '-':
    answer = num1 - num2
elif op == '*':
    answer = num1 * num2
elif op == '/':
    answer = num1 / num2
else:
    print('잘못된 연산자입니다.')
print('결과는', answer, '입니다.')
print('계산기가 종료되었습니다.')