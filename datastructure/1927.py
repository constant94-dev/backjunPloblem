#---자료구조 최소 힙 백준 1927번

# 아이디어
# 입력 값 x 가 자연수라면 배열에 x 값을 추가한다.
# 입력 값 x 가 0 이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
# 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하는 경우 0 을 출력한다.
# 연산의 개수 N 만큼 반복문을 돌린다.
# 입력 값이 0 인지 아닌지를 판단해,
# 0일 때 배열에서 가장 작은 값 출력 후 배열에서 값 제거
# 0보다 클 때 배열에 값을 추가

# 시간복잡도
# O(N)
# 리스트로 구현했다가 시간초과 문제가 생겼다.
# 파이썬 모듈 heap 자료구조를 사용해서 문제를 해결했다.


# 자료구조
# 연산의 개수 int N
# 입력 값 int x

import sys
from heapq import heappush, heappop
input=sys.stdin.readline
heap = []

N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else: 
            print(heappop(heap))
    else:
        heappush(heap ,x)
