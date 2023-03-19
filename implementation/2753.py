# 윤년 백준 2753 문제

# 의사코드
import sys
input = sys.stdin.readline
# 연도가 주어진다.
n=int(input())
result = 0 # 윤년이 아닌 상태
if n%4 == 0: # 주어진 연도가 4의 배수
    if n%100 == 0 and n%400 != 0: # 주어진 연도가 100의 배수이고 400의 배수가 아니면
        result = 0 # 윤년이 아니다
    else: result = 1 # 윤년이다
# 윤년이면 1, 아니면 0 을 출력한다.
print(result)
