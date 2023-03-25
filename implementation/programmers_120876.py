# 겹치는 선분의 길이 - 프로그래머스 120876번

def solution(lines):
    # arr 배열 및 변수 초기화
    answer = 0
    arr = [0]*200

    # lines 정보를 arr 배열에 적용
    for i in range(len(lines)):
        for j in range(lines[i][0] + 100, lines[i][1] + 100):
            arr[j] += 1

    # arr 배열에서 겹친 부분 세기
    for i in range(0, 200):
        if arr[i] > 1:
            answer += 1

    return answer
