# 과제 안 내신 분..? 백준 5597번

# 의사코드
# 학생 수 30명
# 출석번호 1번 부터 30번
# 제출 안 한 학생 2명의 출석번호 구하자

from collections import deque
import sys
input = sys.stdin.readline
check = deque()
# 1 부터 30까지 존재하는 출석부를 만든다.
[check.append(i) for i in range(1, 31)]
print(check)

# 28줄의 입력을 받는다.
for _ in range(28):
    submit = int(input())
    # 1줄마다 제출자의 출석번호를 출석부에서 제거한다.
    check.remove(submit)

# 출석부에 남은 출석번호를 출력한다.
for i in range(len(check)):
    print(check[i],end='\n')

