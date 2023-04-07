#---자료구조 프린터 큐 백준 1966번

# 아이디어
# 문제에서 제시한 대로 queue 자료구조를 사용한다
# 테스트케이스 수 만큼 반복문을 돌린다
# 반복문이 한번 돌 때마다 두 줄의 입력을 받는다
# 두 줄의 입력을 받은 후 타겟 문서 위치를 변수에 저장하고 N 개의 문서만큼반복문을 돌린다
# 두번째 반복문이 돌면서 중요도가 높은 문서가 하나라도 있다면, queue의 가장 뒤에 재배치한다
# 중요도가 높은 순서로 배치가 마무리 되면, (타겟 문서 위치 +1)을 출력한다.

# 시간복잡도
# O(N^2)

# 자료구조
# 테스트케이스 수 int test_case
# 테스트케이스 첫째 줄: 문서의 개수 N, 인쇄 순서 궁금한 문서 현재 위치 M
# 테스트케이스 두 번째 줄: N 개 문서의 중요도 imp

import sys
input = sys.stdin.readline

test_cases = int(input())

for _ in range(test_cases):
    n, m = list(map(int, input().split()))
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    order = 0

    while True:
        if imp[0] == max(imp):
            order += 1
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
