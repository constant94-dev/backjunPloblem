import sys
input_fn = sys.stdin.readline

def solution(m:int, n:int):
    answer = []
    plus = 0
    # 2. 완전제곱수가 M 과 N 사이의 해당되는 값일 때 결과 리스트의 추가
    for i in range(1, n+1):
        compact = i**2
        print("compact 값: ",compact)
        if compact >= m and n >= compact: # 60 <= i**2 <= 100
            print("완전제곱수 추가: ",i)
            answer.append(compact)

    # 3. 리스트의 저장된 완전제곱수를 모두 더한값과 그 중 가장 작은 값을 출력
    if len(answer) == 0:
        print("-1")
    else:
        for i in answer:
            plus += int(i)
        print(plus)
        print(min(answer))

# 1. 첫째 줄에 M, 둘째 줄에 N 입력
M = int(input_fn())
N = int(input_fn())
solution(M, N)
