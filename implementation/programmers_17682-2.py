# 1. 숫자는 무시하고 연산자만 처리한다.
# 2. 숫자는 시작 index 만 관리한다.
# 3. 최근 1개 혹은 2개 숫자에 대해 연산한다.
# 3-1. 다트 게임이 끝나기 전까지는 점수를 더하면 안된다.
# 3-2. 연산이 다 끝나고 한번에 더한다.
# 3-3. stack 자료구조 형태를 사용 해야한다.
def solution(dartResult):
    scores = []
    start_idx = 0
    option = {"S":1, "D":2, "T":3} # dictionary 사용

    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in option: # 'op' 값이 'option' 안의 있다면
            scores.append(int(dartResult[start_idx:i]) ** option[op]) # 문자형에서 정수형으로 변환하고 S,D,T 의 맞는 계산을 한다.
        elif op == "*":
            scores[-2:] = [x * 2 for x in scores[-2:]] # 가장 뒤의 있는 2개의 값을 가져오고 2배 계산을 한다.
        elif op == "#":
            scores[-1] = -scores[-1] # scores[-1] 은 가장 최근의 scores 의 추가된 값이다.
        
        if not op.isnumeric(): # 내가 지금 확인하고 있는 것이 숫자가 아니라면 다음 인덱스부터 숫자가 시작될 것이다.
            start_idx = i + 1
    return sum(scores)
