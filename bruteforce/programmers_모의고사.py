# 문제 단순화
# 수포자 3명 중 가장 많은 문제를 맞힌 사람은 누구인가?

# 해결책
# 1. 수포자들이 찍는 방식의 규칙을 생각해 각각의 배열을 만든다.
# 2. 만들어진 배열을 정답과 비교해 가장 많이 맞힌 수포자를 찾는다.

# 시간복잡도
# 한 문제당 5번의 검색을 한다.
# 5x10,000=50,000
# O(N)


def solution(answers):
    answer = [0 for i in range(3)] # 최고점자는 3명을 넘을 수 없다.
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 이 반복문의 핵심은 수포자들의 순열을 1번부터 하나씩 탐색하는 것이다.
    # 탐색중 해당 번호의 answer 값 과 순열의 값이 같다면 수포자의 정답 카운트를 증가시키는 것이다.
    for i in range(len(answers)):
        ans = answers[i]
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1     
    
    result = [] # 수포자들 중 최고점자를 저장하는 공간
    for i in range(len(answer)):
        if(answer[i] == max(answer)): # 최고점자가 누구인지 알아내기 위한 반복문
            result.append(i+1)
    
    return sorted(result) # 최고점자가 여럿일 경우, 오름차순 정렬

print(solution([1,3,2,4,2]))
