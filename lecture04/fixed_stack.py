# 고정 길이 스택 클래스 FixedStack 구현하기

from typing import Any

class FixedStack:
    '''고정 길이 스택 클래스'''

    class Empty(Exception):
        '''비어 있는 FixedStack에 팝 혹은 피크 할때 보내는 예외 처리'''
        pass # 비었으니 실행이 안되지

    class Full(Exception):
        '''가득 찬 FixedStack에 푸시할때 내보내는 예외 처리'''
        pass

    def __init__(self, capacity: int = 256) -> None:
        '''스택 초기화'''
        self.stk = [None] * capacity         # 스택 본체
        self.capacity = capacity             # 스택 크기기
        self.ptr = 0                         # 스택 포인터

    def __len__(self) -> int :
        '''스택에 쌓여 있는 data 개수 반환'''
        return self.ptr

    def isEmpty(self) -> bool:
        '''스택이 비어 있는지 판단한다'''
        return self.ptr <= 0 # 비어 있으면 true 내보냄

    def isFull(self) -> bool:
        '''스택이 가득 차있는지 판단한다'''
        return self.ptr >= self.capacity   # 가득차면 true임


    def push(self, value:Any) -> None:
        '''스택에 value를 푸시한다'''
        if self.isFull():                  # 스택 가득찬 경우
            raise FixedStack.Full          # 예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        '''스택에서 데이터를 팝팝(꺼내러 왈ㄹ랄라 냠냠 꾸울꺽)'''
        if self.isEmpty():                 # stack empty
            raise FixedStack.Empty         # exception
        self.ptr -= 1
        return self.stk[self.ptr - 1]

    def peek(self) -> Any:
        '''스택에서 데이터를 피크 (꼭대기 데이타값 관전)'''
        if self.isEmpty():                 # stack empty
            raise FixedStack.Empty         # exception
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        '''stack clean (all data remove)'''
        self.ptr = 0


    def find(self, value: Any) -> Any:
        '''in stack -> find value -> return index(nothing : return -1)'''
        for i in range(self.ptr -1, -1, -1):  # linear search (up -> down)
            if self.stk[i] == value:
                return i                      # success
            return -1                         # fail

    def count(self, value: Any) -> bool:
        '''return value's length'''
        c = 0
        for i in range(self.ptr): # linear search(down -> up)
            if self.stk[i] == value: # success
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        '''in stack value in ?'''
        return self.count(value)
    
    def dump(self) -> None:
        '''dump : print up -> down all data'''
        if self.isEmpty():                    # empty
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])