def solution(lines):
    # 1. 배열 및 변수 초기화
    result = 0 # 겹치는 선분의 길이
    arr = [0] * 200 # 선분의 전체 길이

    # 2. lines 정보를 arr 배열에 적용
    for i in range(len(lines)): # 3번 반복
        for j in range(lines[i][0] +100, lines[i][1] +100): # 2번 반복. 음수가 들어올 수 있으니 더하기 100 해준다
            arr[j] += 1

    # 3. arr 배열에서 겹친 부분 세기
    # 여기서 고민했던 내용은 선분 [-1,1], [1,3], [3,9] 가 겹치는 선분이 하나도 없어야 하는데
    # 내가 생각하기로 [-1,1] [1,3] 중의 1이 겹치고 [1,3] [3,9] 3이 겹친다
    # 어떻게 해당 부분이 겹치지 않는다고 판단해야할까는
    # 2. arr 배열에 적용을 할 때 lines[i][0] + 100 부터 lines[i][1] + 100 이전까지
    # 겹치는 선분으로 적용되어 위에서 생각되는 오류를 해결할 수 있었다.
    for i in range(len(arr)):
        if arr[i] >= 2:
            result += 1

    return result
