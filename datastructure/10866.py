#--- 자료구조 덱 문제 백준 10866번

# 아이디어
# 8가지 명령을 처리하기 위한 조건문이 필요하다.
# 첫째 줄에 명령의 수 N 을 입력받는다.
# 출력 명령이 주어질 때 한 줄에 하나씩 출력한다.
# 양방향 큐인 deque 를 사용할 것이다.

# 시간복잡도
# O(N)

# 자료구조(변수)
# 명령의 수 N
# 한 줄마다 주어지는 명령 order

import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

N = int(input())
for _ in range(N):
    order = input().split()
    if order[0] == 'push_front':
        queue.appendleft(order[1])
    elif order[0] == 'push_back':
        queue.append(order[1])
    elif order[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else: print(queue.popleft())
    elif order[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else: print(queue.pop())
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else: print(0)
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else: print(queue[0])
    elif order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else: print(queue[len(queue)-1])
