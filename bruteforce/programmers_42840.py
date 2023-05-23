def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers): # 인덱스 번호와 값을 동시에 사용할 때 'enumerate' 사용
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    max_score = max(score)
    for idx, s in enumerate(score):
        if s == max_score:
            result.append(idx+1) # 인덱스는 0 부터 시작하는데 수포자 번호는 1 부터 시작해서 1 증가시켜준다

    return sorted(result)
