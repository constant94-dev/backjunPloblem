#---자료구조 요세푸스 문제 백준 1158번

# 아이디어
# 나열된 수 N 에서 K 번째 사람을 제거하는 문제
# 죽여야되는 K 번째 전까지 queue 오른쪽으로 옮겨놓는다
# 죽여야되는 K 번째라면 queue 삭제하고 문자열에 추가한다
# 반복은 queue 가 빌 때까지 반복한다

# 시간복잡도
# O(N^2)

# 자료구조
# 원을 이루면서 앉아있는 사람 수 N
# 제거할 사람의 위치 양의 정수 K

import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())

queue = deque()
[queue.append(i) for i in range(1, N+1)]
answer = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print('<'+str(answer)[1:-1]+'>')
