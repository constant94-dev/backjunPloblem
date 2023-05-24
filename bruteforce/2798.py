import sys
input_fn = sys.stdin.readline

def recur(n: int, m: int, cards: list, start: int, cnt: int, result: int, answer: int):
    if cnt == 3:
        if result <= m:
            answer[0] = max(answer[0], result)  # 4. 3장의 카드 합이 M 을 넘지 않고 M 과 가까운 숫자는 결과 저장
        return # 카드 3개를 확인했으니 연속한 다음 수를 비교하기 위해 return
    for i in range(start, n):
        recur(n, m, cards, i+1, cnt+1, result + cards[i], answer)


def solution(n: int, m: int, cards: list):
    answer = [0] # m 에 가장 근접한 결과를 저장할 변수
    # 3. 3장의 카드를 뽑는다
    recur(n, m, cards, 0, 0, 0, answer)

    # 5. 모든 카드의 합을 확인 후 결과 출력
    return answer[0]

# 1. 카드 개수와 딜러가 말한 숫자 입력
# 2. n 만큼 카드 숫자 입력
n, m = map(int, input_fn().split())
card = list(map(int, input_fn().split()))
print(solution(n,m,card))
