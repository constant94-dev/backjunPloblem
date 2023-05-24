def solution(n):
    answer = []
    # 1. 1~n 까지 나누는 반복 만들기
    for i in range(1, n+1):
        if n % i == 0:
            # 2. 나머지가 '0' 인 값은 answer 리스트에 추가
            answer.append(i)
    
    # 3. 오름차순 정렬 후 출력
    return sorted(answer)
