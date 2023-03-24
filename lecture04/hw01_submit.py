
# 추가구현 : random으로 동덕이와 원준이의 숫자를 불러옴 input 안받았음 

import random
class Stack(list):
    push = list.append  # 데이터 삽입
    dele = list.pop # 최상단 데이터 삭제
    def isEmpty(self): # 데이터 없는지 확인
        if not self:
            return True
        else:
            return False

    def peek(self): # 최상단 데이터 확인
        return self[-1]

    def top(self):
        print
        



if __name__ == '__main__': 
    ws = Stack() # 원준 스택 기본설정
    ds = Stack() # 동덕 스텍 기본설정
    dSum = 0
    wSum = 0 # 총합은 둘다 0으로 둬야지 
    n = int(input('실행 횟수를 입력하세요.: '))
    for N in range(1, n + 1):
        if N % 2 == 1: # 홀수 -> 원준 시작
            w = random.randint(1,9) # 랜덤 호출
            if w % 3 == 0: # 3의 배수는 3으로 나누었을때 나머지가 0나와야지
                if len(ws)== 0: # 스택 비었을 경우 오류 방지
                    pass
                else:
                    ws.dele() # 이경우 삭제처리
            else:
                ws.push(w) # 아니면 집어넣어
            
        else:
            d = random.randint(1, 9) # 똑같이 랜덤
            if d % 3 == 0: # 3의배수
                if len(ds) == 0 : # 오류방지
                    pass
                else: 
                    ds.dele() # 3의배수 전 삭제처리
                
            else:    
                ds.push(d) # 아닐경우 집어넣기
            
    for k in range (0, len(ws)):
        wSum += ws[k] #원준합
    for j in range (0, len(ds)):
        dSum += ds[j] #동덕합
    print(f'원준 : {ws}')
    print(f'동덕 : {ds}')



    print(f"원준 총합 : {wSum}")
    print(f'동덕 총합 : {dSum}')

