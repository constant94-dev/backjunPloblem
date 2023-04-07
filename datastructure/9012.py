#---자료구조 괄호 백준 9012번

# 아이디어
# 입력되는 괄호 문자열을 변수에 저장한다
# 열린 괄호의 수 만큼 닫힌 괄호의 수도 필요하다
# 열린 괄호가 없을 때 닫힌 괄호가 생성되면 VPS 가 아닌 문자열이다
# 열린 괄호의 수 만큼 닫힌 괄호가 생성되지 않으면 VPS 가 아닌 문자열이다
# 입력 데이터의 수 만큼 도는 반복문 하나
# 입력된 괄호 문자열 만큼 도는 반복문 하나
# 괄호 문자열 만큼 반복문을 돌면서 열린괄호 수, 닫힌 괄호 수를 카운팅한다
# 위의 나열된 조건으로 카운팅 비교해 VPS 인지, 아닌지 판단 후 프린트한다

# 시간복잡도
# O(N^2)

# 자료구조
# 입력 데이터의 수 T
# 두번째 줄 부터는 괄호 문자열 테스트 데이터가 주어진다 PS

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    PS = input().rstrip()  
    closePS = PS.count(')')
    openPS = 0
    for i in range(len(PS)):
        if PS[0] == ')':
            break
        if PS[i] == '(':
            openPS += 1
        elif PS[i] == ')' and openPS > 0:
            openPS -= 1
            closePS -= 1
        elif PS[i] == ')' and openPS == 0:
            break
    if openPS == 0 and closePS == 0:
        print('YES')
    else: print('NO')
