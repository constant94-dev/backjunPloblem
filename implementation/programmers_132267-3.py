def solution(a, b, n):
    answer = 0
    # 1. 빈 병의 개수 n이 교환 가능한 최소 숫자 a 이상일 때까지 반복
    while n >= a:
        # 2. newCount 개의 병 추가
        newCount = n // a * b # 이번턴에서 마트에서 받게될 콜라 수
        answer += newCount
        print("newCount", newCount)
        # 3. 남은 병 계산하기
        n = n % a + newCount # 이번턴에서 내가 가지고 있는 콜라 수
        print("n", n)
    return answer
