#---자료구조 N번째 큰 수 백준 2075번

# 아이디어
# 우선순위 큐 안에 들어있는 원소의 개수가 N 개 미만이면 -> 우선순위 큐에 추가한다.
# 우선순위 큐 안에 들어있는 원소의 개수가 N 개라면 ->
# 1) 현재 확인하고 있는 숫자가 우선순위 큐의 최솟값보다 작은 경우, 무시한다.
# 2) 나머지 경우, 우선순위 큐의 최솟값을 제거하고 현재 확인하고 있는 숫자를 우선순위 큐에 추가한다.

# 시간복잡도
# 입력되는 숫자 모두를 받아서 정렬하는 방식을 사용해도 풀이가 가능하다.
# 하지만 메모리 제한으로 풀이를 제출 시 메모리 초과 발생한다.
# 따라서 N^2 개의 숫자 모두를 배열에 저장하고 그 후에 문제 조건에 따라 처리하는 방식은 문제를 풀지 못한다.
# N^2 개의 숫자 모두를 살펴보면서 로직을 수행하되 N 짜리 우선순위 큐에서 처리하면 문제를 해결할 수 있다.

# 자료구조
# 각 줄 마다 입력할 수 int N

import sys
import heapq
input=sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < N:
            heapq.heappush(heap, number)
        else:
            if number > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])
