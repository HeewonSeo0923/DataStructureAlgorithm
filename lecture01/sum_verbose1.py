# a부터 b까지 정수의 합 구하기 1

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:   # i가 b보다 작으면 합을 구하는 과정 출력
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)

# 문제점 : for문 반복 개수와 if문 반복 개수 판단의 수가 동일하다 => 줄여야 한다