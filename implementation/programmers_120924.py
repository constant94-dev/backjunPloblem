# 다음에 올 숫자 프로그래머스 120924번

# 의사코드
# 등차수열은 일정한 차이를 가지고 수가 나열된다.
# 등비수열은 일정한 비를 가지고 수가 나열된다.

import sys
input = sys.stdin.readline
# 등차 or 등비수열 common 이 입력된다.
common = list(map(int, input().split()))
# print(common)
# print(len(common))
if common[1] - common[0] == common[2] - common[1]: # 등차라면, 2번째 값 - 1번째 값 = 3번째 값 - 2번째 값
    print(common[-1] + (common[1] - common[0])) # 공차 값 연산    
else: # 등비라면, 2번재 값//1번재 값 == 3번째 값//2번째 값
    print(common[-1] * (common[1]//common[0])) # 공비 값 연산
# 공차 or 공비 값을 마지막 원소의 연산해주고 출력한다.
