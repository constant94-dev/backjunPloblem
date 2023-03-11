#--- 자료구조 큐 문제 백준 (10845번)

# 아이디어
# 스택을 사용할 때는 list 를 사용해 구현했는데, 큐를 구현할 때도 list 를 사용할 수 있지만 수행시간이 오래걸릴 수 있다
# 그래서 양방향 큐인 deque 를 사용해서 문제를 풀것이다
# 명령의 수를 입력 받고 명령의 수 N 만큼 반복문을 돌린댜
# 주어지는 명령에 맞게 큐를 사용하고 값을 출력한다

# 시간복잡도
# O(N)

# 자료구조
# 명령의 수 N
# 주어지는 정수의 수 X 는 1 <= X <= 100,000

import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else: print(queue.popleft())
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
        temp = len(queue)
        if temp == 0:
            print(-1)
        else: print(queue[temp-1])
