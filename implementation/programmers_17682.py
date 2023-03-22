def solution(dartResult):
    scores = []
    start_idx = 0
    power = {'S' : 1, 'D' : 2, 'T' : 3}
    
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power:
            scores.append(int(dartResult[start_idx:i]) ** power[op])
        elif op == '*':
            scores[-2:] = [x * 2 for x in scores[-2:]]
        elif op == '#':
            scores[-1] = -scores[-1]
        
        if not op.isnumeric(): # 정수가 아닐 때
            start_idx = i + 1 # 현재 검사한 문자의 인덱스 + 1 값이 정수일 것이다
        
    return sum(scores)
