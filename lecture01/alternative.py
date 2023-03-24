# +와 - 를 번갈아 출력하기 1

print('+와 -를 번갈아 출력하겠습니다.')
n = int(input('몇 개를 출력할까요?: '))

for i in range(n):
    if i % 2 :
        print('-', end='')
    else:
        print('+', end='')

print()

# 문제점 분석
# for문 반복할때마다 if문 수행
# 상황에 따라 유연한 수정이 어렵다
