#--- 자료구조 스택 문제 백준 (10828번)

# 아이디어
# 스택의 구조는 연탄구덩이를 생각해보면 쉽다
# 가장 먼저 들어온 연탄이 가장 나중에 나가는 원리이다 (LIFO)

# 시간복잡도
# O(NlogN) 최대 수행시간을 목표로 하자

# 자료구조
# 스택사용
# 명령의 수 N
# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys
input=sys.stdin.readline

N=int(input())
stack=[]

for _ in range(N):
    operation=input().split()
    if operation[0]=='pop':
        if len(stack)==0:            
            print(-1)
        else: print(stack.pop())
    elif operation[0]=='size':
        print(len(stack))        
    elif operation[0]=='empty':
        if len(stack)==0:
            print(1)            
        else: print(0)
    elif operation[0]=='top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(operation[1])
